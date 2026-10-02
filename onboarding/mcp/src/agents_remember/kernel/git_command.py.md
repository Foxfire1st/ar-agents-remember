# mcp/src/agents_remember/kernel/git_command.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`git_command.py` owns the only `git` subprocess spawn in this package. Six near-identical private
`_run_git` copies used to sit beside it and had drifted apart — only this one passed a scrubbed
`env=` — so the copies were deleted and every caller now goes through `run_git`. It fixes command
isolation, decoding, stdin, and the timeout class in one place.

## Code Commentary

### Logic

`git_environment()` copies the process environment and removes all eight repository-selection
variables named by cit:([`GIT_REPOSITORY_SELECTOR_ENV`], mcp/src/agents_remember/kernel/git_command.py:56-65): `GIT_DIR`, `GIT_WORK_TREE`,
`GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`,
`GIT_NAMESPACE`, and `GIT_PREFIX`.

`run_git(repo_root, args, options=None)` cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:150-214) injects
`safe.directory`, runs at the supplied repository root, captures output as UTF-8 with
`surrogateescape`, applies the scrubbed environment, and returns non-zero outcomes for typed
interpretation by its caller. `options` is a `GitRunnerOptions`
cit:([`GitRunnerOptions`], mcp/src/agents_remember/kernel/git_command.py:116-129), a frozen dataclass carrying the ways a caller
tells a git command something its argv cannot say:

- `work_dir` separates *where git runs* from *which repository the command is about*: `git clone
  <url> <dest>` cannot run inside `<dest>`, and `cwd=` a directory that does not exist raises before
  git is reached. The clone in `worktrees/modules/quality/clean_executor.py` uses the destination's parent.
- `input_text` cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:150-214) feeds git's stdin; when it is `None`, stdin is `subprocess.DEVNULL`.
  `patch_id()` cit:([`patch_id`], mcp/src/agents_remember/memory/carryover.py:171-182) — `git patch-id --stable` — is one of the callers that
  passes it, alongside the `hash-object --stdin`, `apply --index -` and `update-ref --stdin` sites.
  When the private `_run_git` runs with `raw_output=True` (bytes out), it encodes `input_text` as UTF-8
  before passing it, because a bytes-mode subprocess cannot take `str` input. Before MIK-R22 no raw-output
  caller passed stdin, so no existing caller changes behaviour.
- `timeout` cit:([`GIT_LOCAL_TIMEOUT_SECONDS`, `GIT_REMOTE_TIMEOUT_SECONDS`, `GIT_METADATA_TIMEOUT_SECONDS`], mcp/src/agents_remember/kernel/git_command.py:93-95) selects one of four module-level timeout classes instead of the former hard-coded
  five seconds: `GIT_LOCAL_TIMEOUT_SECONDS = 300` is the default and bounds work that can
  legitimately churn (`rebase`, `merge`, `worktree add`); `GIT_REMOTE_TIMEOUT_SECONDS = 120` bounds
  network calls, which are wedged rather than slow; `GIT_METADATA_TIMEOUT_SECONDS = 30` bounds the
  constant-time reads that sit on interactive paths (`rev-parse`, `branch --show-current`,
  `ls-files`). Callers name the class they need — `route_index_census._run_git` and
  `kernel/coordination_context/cross_repo.py` take the metadata bound, `worktrees/modules/cleanup.py`
  takes the remote one — and `git_freshness.fetch_remote` keeps its own shorter
  `DEFAULT_FETCH_TIMEOUT = 30` for the fetch. `GIT_BULK_REMOTE_TIMEOUT_SECONDS = 1800` is the fourth
  class, for foreground bulk network work outside an interactive MCP call.
- `identity` adds `GIT_AUTHOR_*`/`GIT_COMMITTER_*` names on top of the sanitized environment, and it
  was introduced for `git commit-tree`, which reads the author, the committer and both
  timestamps from those variables and from nowhere else, so a history rewrite that must reproduce an
  existing commit byte for byte has no argv spelling for it. It is additive and never subtractive —
  the selector strip runs first, and a name in `GIT_REPOSITORY_SELECTOR_ENV` raises `ValueError`
  rather than being set, so this cannot put a repository selector back.

The three earlier keyword arguments arrived one at a time and became one object because they are one
concept, and because the runner's own signature should stay at the two facts every call shares.
At that introduction, 38 call sites across 19 files were migrated mechanically; not one of them
changed which command it runs or which timeout class it names.

Existing-output observation takes one `ExistingGitPreparationBinding`, retaining the real raw HEAD and tree. A memory binding also requires an independent `memory_content_tree`; the runner proves equality after removing only root memory.md from the raw entries. No normalized content tree is substituted for HEAD's actual tree.

The memory domain filters that exact cache path from index rows, index flags, and physical membership. Code and private-output checks remain strict, including other ignored files and similarly named content. New memory publication rejects a prepared tree containing the cache, then performs the same original-parent/ref CAS and physical readback. Cache-only staging can neither become a new output nor strand an otherwise valid memory publication.

`read_git_blobs_bytes(root, blob_ids)` (MIK-R22) reads many blobs through one `git cat-file --batch`
and returns a `dict` of each requested ID to its exact bytes. The IDs are de-duplicated, sorted and
validated with `require_git_object_id`; each batch header must name the requested ID with type `blob`,
and anything else (a missing object, a non-blob) raises `GitPreparationError`. The output is read raw,
without decoding or newline normalisation, so the knowledge validator's canonical-format check sees the
bytes that will be committed; reading a whole onboarding tree one `cat-file blob` at a time was too slow.

`merge_file_bytes(root, ours, base, theirs, labels)` (MIK-R24) runs `git merge-file -p` over three files
and returns the merged bytes (read raw) with the conflict count, which is Git's exit status. Conflict hunks
carry the three labels. Nothing is written: `-p` only prints. An exit status below 0 or above 127 is a Git
failure and raises `GitPreparationError`. The crossing sync's structural merge
(`memory/conversion/crossing.py`) uses it to merge a card's Markdown three-way by line.
The validator's Git tree reader (`memory_quality/knowledge_validator/trees.py`) is its caller.

`copy_git_index(source, target)` (L37, INV-656CYW) copies a Git index for a disposable capture and gives the copy
the source file's modification time. Git trusts an index entry's recorded stat data unless the file may have been
rewritten in the second the index was written; it recognises such a "racily clean" entry by its recorded time not
being older than the index file's own time, and compares it by content. A plain copy has a new time, so no entry is
racily clean on it, and a same-size rewrite made in that second keeps its old blob in whatever `git add` then
captures. Bytes and time are read from one open file, so an index replaced meanwhile cannot pair one index's bytes
with another's time. The knowledge index's capture (`memory/knowledge_index/tree.py`) and the mutation snapshot
(`worktrees/integration/mutation_evidence.py`) copy through it.

### Conventions

The selector tuple is production authority and is imported by tests instead of copied. Repository
paths are rendered with `as_posix()` for stable Git configuration values. The generic runner stays standard-library-based and leaves domain census interpretation to callers.
The preparation/publication helpers separately interpret exact Git object, ref, index, and physical facts. `run_git`'s aim is expressed as one frozen
`GitRunnerOptions` object rather than a growing keyword list, so the runner's own signature stays at
the repository and the argv, and a new way to aim a command is a field rather than a parameter.

### Invariants And Boundaries

- Ambient repository selectors must never redirect a command away from the explicit `repo_root`.
- UTF-8 `surrogateescape` is required so NUL-delimited Git records retain non-UTF-8 path identity.
- `check=False` is intentional: callers translate return codes and stderr into their domain's typed
  failure without losing evidence.
- Every command stays bounded, but by a class that fits it. Five seconds was a fine bound for
  `rev-parse` and an impossible one for `rebase`/`merge`/`push --delete`, so raising the default to
  `GIT_LOCAL_TIMEOUT_SECONDS` is paired with call sites that name the shorter class; a raised
  default is not a removed bound, and `subprocess.TimeoutExpired` still escapes to the caller.
- `stdin` is `DEVNULL` unless a caller passes `input_text`: under the stdio MCP transport the
  parent's stdin IS the JSON-RPC request pipe, and a child holding or reading it wedges the tool
  call (GitHub #49).
- An `identity` may never reintroduce a repository selector. The names it accepts are checked against
  `GIT_REPOSITORY_SELECTOR_ENV` and a match raises `ValueError`, so the option that exists to make a
  commit replay faithful cannot be used to redirect the command that writes it.
- Only the selectors are stripped, and only from the environment: `identity` is applied after
  `git_environment()`, so it can add author and committer facts and cannot restore `GIT_DIR` or any
  of its seven siblings.
- No second runner may appear. Only this module may spawn `git`; re-exports and typed wrappers
  (`kernel/coordination_context/cross_repo.py`,
  `mcp/test_support/agents_remember_test_support/code_quality/diff_coverage.py`) are fine, a new
  `subprocess.run(["git", ...])` anywhere in the package is not.
- Root validation, census parsing, and containment belong to callers such as
  `route_index_census.py` when using the generic runner. The preparation/publication helpers additionally
  prove their own exact Git roots, refs, trees, index entries, and physical output; lifecycle decisions
  remain with their callers.

### Todos

None known for the MX-FIX-4 Git command boundary.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

The generic runner has distinct Git-fact callers and private/publication observers. These direct source references preserve that ownership split and the explicit history-rewrite identity use; cache regeneration itself never invokes a history rewrite.

- One immutable options object carries cwd, stdin, timeout and authorized identity facts. [1]
- Ambient repository selectors are removed before the actual Git invocation. [2]
- The one Git runner preserves stdin, timeout and surrogate-safe command results. [3]
- The census wrapper selects the metadata timeout and preserves typed failures. [4]
- The census separately interprets NUL-delimited output. [5]
- Carryover delegates input-bearing calls to this runner through GitRunnerOptions. [6]
- Patch-id calculation supplies diff bytes through the shared input option. [7]
- Explicit memory-history rewriting preserves original author/committer identities and timestamps. [8]
- The code-profile sandbox supplies a separate clone working directory and staged input bytes. [9]
- Memory index/flag checks omit only root memory.md; code keeps the complete checks. [10]
- Raw HEAD/tree checks precede projected content proof. [11]
- The required memory certificate subject is compared against raw HEAD with only cache removed. [12]
- Existing output is revalidated around reading exact raw commit bytes. [13]
- Context branch reads use the shared runner and its metadata timeout. [14]
- Coverage support is a typed wrapper around the same production Git runner. [15]
- Remote cleanup selects the bounded remote timeout rather than creating a second runner. [16]
- Raw-output runs encode their stdin text, so a bytes-mode batch command can take input. [17]
- A three-way line merge of three files' exact bytes that writes nothing and returns the conflict count; a Git failure raises. [18]
- Many blobs are read as exact bytes through one batch call; a missing or non-blob object raises. [19]
- The knowledge validator reads a memory tree's knowledge files through the batch reader. [20]
- The module declares a separate 1800-second bulk-network timeout. [21]

- A copied index keeps the index file's modification time. [28]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IsolatedGitState`, `git_environment`, `run_git`. This supporting seam carries bounded error/command evidence used by the L2 owners. It does not become a second lifecycle authority, exception-family translator, or Git fallback path.

### Reconciled Source Evidence

- Isolated execution state keeps index/object/environment redirection explicit. [22]
- The environment scrub remains the shared command boundary. [23]
- All commands continue through the same runner. [24]

## L34 Current Implementation

Binary configuration, commit, blob and tree readers preserve exact bytes. Private preparation uses the named sealed capability and journal-bound create/materialize/commit plan. Closeout publication performs an exact expected-old update-ref once, retains command evidence, and reopens physical/ref state; already-new and existing observations do not repeat the write. The memory-only cache projection does not relax raw object/parent proof or the sole Git-spawn/environment boundary.

- The publication observation rejects cache-bearing new memory output and rechecks exact refs. [25]
- Admission creates only the caller-authorized publication capability. [26]
- The actual CAS is issued once and both observations/command evidence are retained. [27]
