# mcp/src/agents_remember/kernel/git_command.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/kernel/git_command.py`           |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview      | `../../../overview.md`                                   |

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
  `patch_id()` cit:([`patch_id`], mcp/src/agents_remember/memory/carryover.py:168-179) — `git patch-id --stable` — is one of the callers that
  passes it, alongside the `hash-object --stdin`, `apply --index -` and `update-ref --stdin` sites.
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

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

The generic runner has distinct Git-fact callers and private/publication observers. These direct source references preserve that ownership split and the explicit history-rewrite identity use; cache regeneration itself never invokes a history rewrite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| One immutable options object carries cwd, stdin, timeout and authorized identity facts. | L116-L129 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| Ambient repository selectors are removed before the actual Git invocation. | L141-L147 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| The one Git runner preserves stdin, timeout and surrogate-safe command results. | L150-L214 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| The census wrapper selects the metadata timeout and preserves typed failures. | L193-L213 | [mcp/src/agents_remember/kernel/route_index_census.py](mcp/src/agents_remember/kernel/route_index_census.py) |
| The census separately interprets NUL-delimited output. | L225-L231 | [mcp/src/agents_remember/kernel/route_index_census.py](mcp/src/agents_remember/kernel/route_index_census.py) |
| Carryover delegates input-bearing calls to this runner through GitRunnerOptions. | L112-L120 | [mcp/src/agents_remember/memory/carryover.py](mcp/src/agents_remember/memory/carryover.py) |
| Patch-id calculation supplies diff bytes through the shared input option. | L168-L179 | [mcp/src/agents_remember/memory/carryover.py](mcp/src/agents_remember/memory/carryover.py) |
| Explicit memory-history rewriting preserves original author/committer identities and timestamps. | L821-L834 | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |
| The code-profile sandbox supplies a separate clone working directory and staged input bytes. | L344-L392 | [mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py](mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py) |
| Memory index/flag checks omit only root memory.md; code keeps the complete checks. | L390-L427 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| Raw HEAD/tree checks precede projected content proof. | L451-L465 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| The required memory certificate subject is compared against raw HEAD with only cache removed. | L468-L486 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| Existing output is revalidated around reading exact raw commit bytes. | L489-L498 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| Context branch reads use the shared runner and its metadata timeout. | L25-L37 | [mcp/src/agents_remember/kernel/coordination_context/cross_repo.py](mcp/src/agents_remember/kernel/coordination_context/cross_repo.py) |
| Coverage support is a typed wrapper around the same production Git runner. | L80-L90 | [mcp/test_support/agents_remember_test_support/code_quality/diff_coverage.py](mcp/test_support/agents_remember_test_support/code_quality/diff_coverage.py) |
| Remote cleanup selects the bounded remote timeout rather than creating a second runner. | L312-L327 | [mcp/src/agents_remember/worktrees/modules/cleanup.py](mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| The module declares a separate 1800-second bulk-network timeout. | L96-L96 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## 260821-CLIVE-L2 Current Contract

The current source seams include `IsolatedGitState`, `git_environment`, `run_git`. This supporting seam carries bounded error/command evidence used by the L2 owners. It does not become a second lifecycle authority, exception-family translator, or Git fallback path.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Isolated execution state keeps index/object/environment redirection explicit. | L132-L138 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| The environment scrub remains the shared command boundary. | L141-L147 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| All commands continue through the same runner. | L150-L214 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |

## L34 Current Implementation

Binary configuration, commit, blob and tree readers preserve exact bytes. Private preparation uses the named sealed capability and journal-bound create/materialize/commit plan. Closeout publication performs an exact expected-old update-ref once, retains command evidence, and reopens physical/ref state; already-new and existing observations do not repeat the write. The memory-only cache projection does not relax raw object/parent proof or the sole Git-spawn/environment boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The publication observation rejects cache-bearing new memory output and rechecks exact refs. | L688-L720 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| Admission creates only the caller-authorized publication capability. | L723-L733 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |
| The actual CAS is issued once and both observations/command evidence are retained. | L760-L783 | [mcp/src/agents_remember/kernel/git_command.py](mcp/src/agents_remember/kernel/git_command.py) |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Reconciled the typed existing-output binding, independent raw/certified tree proof, memory-only index/flag/physical projection, strict code domain, and cache-free new publication; re-derived current runner/caller citations. Source SHA-256 `079e6786b56a5fdfc877d1be6878339117d22ce1c87b1e3377d00cd29d5a3a3d`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (residue citation pass): re-derived the source
  range of 1 claim(s) whose anchor no longer sat in its cited range and normalised 3 further
  range(s) from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`). No claim wording was changed to fit an anchor; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T18:20+02:00 — 260913-LCA-L3 follow-up (same uncommitted change set on
  `ar/260913-lca-l3-ar`, base `7317108b`): No content impact on this module — the reviewed fix to the
  memory-history backfill changed only `kernel/memory_backfill.py`, `cli/memory_backfill.py`, its test
  module and the cards that describe them. Two citation anchors in this card point into that module
  and both moved when it grew from 686 to 1024 lines, so they were re-derived: `_identity` 510-523 →
  821-834 and `_IDENTITY_FIELDS` 82 → 106. Verification metadata remains closeout-owned; no acceptance
  claim and no verification stamp advanced.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): `run_git` no longer takes `work_dir`/`input_text`/`timeout` as keyword arguments. It
  takes one optional `GitRunnerOptions` object (`work_dir`, `input_text`, `timeout`, `identity`), so
  the runner's signature is back to the two facts every call shares and a new way to aim a command is
  a field rather than a parameter. The new capability is `identity`: `git commit-tree` reads the
  author, the committer and both timestamps from `GIT_AUTHOR_*`/`GIT_COMMITTER_*` and from nowhere
  else, so the memory-history rewrite that must reproduce an existing commit byte for byte had no
  argv spelling for it. It is additive and cannot reintroduce a selector — a name in
  `GIT_REPOSITORY_SELECTOR_ENV` raises `ValueError` — and two invariants were added for that.
  `Logic` was rewritten around the object, `Conventions` gained the one-object rule, and every
  citation in this card was re-derived against the grown file: `run_git` 85-151 → 149-213,
  `GitCommandPlan` 99-104 → 98-104, `_GitRun` 108-112 → 107-112, the CLIVE-L2 seam row 85-91 /
  94-100 / 103-154 → 131-137 / 140-146 / 149-213, the L34 rows 646-656 → 675-685, 659-669 → 688-698,
  672-680 → 701-709 and 683-706 → 712-735, the census row 91-91 / 222-222 → `_run_git` 193-213 and
  `_nul_records` 225-231, and the carryover row 113-117 / 181-188 → 114-122 / 186-197. The
  `%ai`/`%ci`-rather-than-`%aI` date rule the identity replay depends on is recorded on the
  backfill module's card. Verification metadata remains closeout-owned; no acceptance claim and no
  verification stamp advanced.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `GIT_REPOSITORY_SELECTOR_ENV` repointed to mcp/src/agents_remember/kernel/git_command.py:55-64. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `GIT_LOCAL_TIMEOUT_SECONDS`; `GIT_REMOTE_TIMEOUT_SECONDS`; `GIT_METADATA_TIMEOUT_SECONDS` repointed to mcp/src/agents_remember/kernel/git_command.py:92-92; mcp/src/agents_remember/kernel/git_command.py:93-93; mcp/src/agents_remember/kernel/git_command.py:94-94. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-08-31T20:30+02:00 — No content impact: corrected the source-file verification citation
  from the retired `mcp/tests/code_quality/` location to the current
  `mcp/test_support/agents_remember_test_support/code_quality/single_owner.py` owner. Git runner
  behavior and boundaries are unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 4 repository-internal reference rows and normalized 5 prose citation references for the single Git runner boundary; final scoped result 0 (checker-clean).

- 2026-07-31T20:50+02:00 — 260731-EFA-L3 curator: this file became the single owner, so the body
  was rewritten. Corrected the false "enforces a five-second timeout" claim: `run_git` now takes
  `timeout` and defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`, with `GIT_REMOTE_TIMEOUT_SECONDS =
  120` and `GIT_METADATA_TIMEOUT_SECONDS = 30` as the other two classes cit:(["GIT_REMOTE_TIMEOUT_SECONDS = 120"], mcp/src/agents_remember/kernel/git_command.py:93-93), and callers pick
  one. Corrected the unconditional `stdin=DEVNULL` claim: stdin is `DEVNULL` only when the new
  `input_text` keyword is `None` cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:149-213). Recorded the consolidation (six drifted `_run_git`
  copies removed, this the only module that may spawn git) in Purpose and as a new invariant.
  Repaired 2 citations into files this leaf changed: the census row's whole-file `L1-L226` became
  `L189-L205; L217-L223` (`_run_git` + `_nul_records`), and the carryover row's unanchored "Git
  runner" became `L92-L96; L200-L208` — that row's claim of a "separate input-bearing Git adapter"
  was false, since carryover's local `run_git` was deleted and `require_git`/`patch_id` now call
  this one. Added a row for the new `mcp/tests/test_git_command.py`. The `conftest.py` /
  `test_route_index.py` ranges were left alone: this leaf did not touch either file. The L2 entry
  below cites `git_command.py L9-L18` for the selector tuple; that was true at its commit and is
  left as the historical record — the tuple now sits at L24-L33.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The row
  carries two source paths, and only its second range moved: `conftest.py` L34-L39 still holds the
  `GIT_REPOSITORY_SELECTOR_ENV` import and the `os.environ.pop` scrub loop, while the coverage test
  `test_ambient_git_repository_selectors_cannot_redirect_the_census` shifted to `test_route_index.py`
  L592-L640. Re-verified that its `selectors` dict still names all eight tuple entries from
  `git_command.py` L9-L18.

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the authoritative selector scrub and
  surrogate-preserving output boundary used by deterministic route-index census and carryover.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
