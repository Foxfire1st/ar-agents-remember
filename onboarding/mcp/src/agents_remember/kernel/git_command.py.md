# mcp/src/agents_remember/kernel/git_command.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Shared Git runners and preparation owners; this is not the sole process-starting module, since landing_commit_check also starts Git/hook processes directly. The module also
holds the exact-bytes readers of Git objects, the batched blob reader with its optional shared-read block, the
option tuples for diffs whose output is parsed, the index copy for disposable captures, the three-way file
merge, and sealed existing/private-output observations. The removed preparation-command dispatcher and closeout-ref publication dispatcher are not current execution owners.

## Code Commentary

The object memo exists only for one request and keys the repository, effective work directory/environment, exact argv and output mode. It keeps successes only. Exact-object existence/verification and explicitly replace-proof supported peels may collapse; failures, refs, index mutation and replacement-sensitive or malformed/suffixed names run natively again.


### The runner

- `git_environment()` copies the process environment and removes the eight repository selectors of
  `GIT_REPOSITORY_SELECTOR_ENV` (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
  `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`). An exported selector
  therefore cannot aim a command at another repository. Every command additionally runs with
  `GIT_OPTIONAL_LOCKS=0` (rule 6): a read must never take a lock the repository did not ask for.
- `_git_argv` builds `git -C <work dir> -c core.longpaths=true -c safe.directory=<repo root> <args>`.
  `safe.directory` names the one repository the command is about, never a wildcard.
- `_run_git` runs that argv with the work directory as `cwd`, captures both streams, sets `check=False`, and
  applies the timeout. Text mode decodes UTF-8 with `surrogateescape`; `raw_output=True` returns bytes and
  encodes a text input as UTF-8. Standard input is the given input or `DEVNULL`, never the parent's.
- `run_git(repo_root, args, options)` is the general entry. `GitRunnerOptions` carries `work_dir` (where Git
  runs when that differs from the repository, as for `git clone`), `input_text` (standard input), `timeout`
  and `identity`. `identity` adds environment names such as `GIT_AUTHOR_*` on top of the scrubbed
  environment; a selector name in it raises `ValueError`.
- Four timeout classes are declared: `GIT_LOCAL_TIMEOUT_SECONDS = 300` (the default),
  `GIT_REMOTE_TIMEOUT_SECONDS = 120`, `GIT_METADATA_TIMEOUT_SECONDS = 30` and
  `GIT_BULK_REMOTE_TIMEOUT_SECONDS = 1800`. Timeout raises TimeoutExpired; the explicitly owned process-group runner bounds descendants under its caller, while the landing-hook owner separately owns its hook process group. Readback errors retain actual output.
- `run_git_with_index` sets `GIT_INDEX_FILE` to one explicit index after the scrub.
  `run_git_with_isolated_index_and_objects` also sets a disposable object directory with the repository's
  object store as a read-only alternate (`IsolatedGitState`). Both accept input text.
- `copy_git_index(source, target)` copies an index and gives the copy the source's access and modification
  times. Bytes and times come from one open file. With the source's time, Git still compares by content an
  entry that was rewritten in the second the index was written.

### Diffs whose output is parsed

`DIFF_PREFIX_OPTIONS` is `("--src-prefix=a/", "--dst-prefix=b/")` and `PARSED_DIFF_OPTIONS` is
`("--no-color", "--no-ext-diff", *DIFF_PREFIX_OPTIONS)`. A caller that parses `git diff` output passes them,
so the user's Git configuration cannot change the format: `diff.noprefix`, `diff.srcPrefix`,
`diff.dstPrefix` and `diff.mnemonicPrefix` change the `a/` and `b/` of a file header, `diff.external`
replaces the output, and forced colour wraps it in escape sequences. Options on the command line win over
each of these settings. The reviewer's knowledge diff, source inventory and rename inference pass
`PARSED_DIFF_OPTIONS`; the worklist's blob diff adds `DIFF_PREFIX_OPTIONS` to its own fixed options. The
runner itself adds none of them: a caller that does not pass them gets Git's configured format.

### Exact readers

- `read_git_configuration_bytes`, `read_git_commit_bytes`, `read_git_blob_bytes` and `read_git_tree_bytes`
  return original bytes without decoding or newline translation. Each object ID is checked with
  `require_git_object_id`; a failed read raises `GitPreparationError`.
- `read_git_blobs_bytes(root, blob_ids)` reads many blobs through one `git cat-file --batch`
  (`_batch_blobs`). The IDs are de-duplicated, sorted and validated. Each batch header must name the
  requested ID with type `blob`; a missing object or another type raises `GitPreparationError`. The result
  maps every requested ID to its bytes.
- `shared_blob_reads()` is a context manager. Inside the block a blob that was read from a repository is
  answered from the block's own dictionary and is not read from Git again; only the IDs the block does not
  hold go to `_batch_blobs`. The dictionary is keyed by repository path and blob ID, so an ID that one
  repository holds is still read, and still fails, in a repository that lacks it. The dictionary lives in a
  context variable and ends with the block. Outside a block every call reads from Git. The reviewer's
  worklist child, complete-review owner and review-tree owner enter the block; nested scopes join the existing block.
- `merge_file_bytes` runs `git merge-file -p` over three files and returns the merged bytes and the number
  of conflicts, which is Git's exit status. It writes nothing. An exit status below 0 or above 127 raises.

### Private preparation and closeout publication

- `inspect_existing_git_preparation` proves an existing logical output (root, common directory, branch ref,
  `HEAD`, tree, index, index flags and physical files) before and after it reads the commit's raw bytes. For
  a memory binding the root `memory.md` is left out of the index and physical comparison, and the tree
  without it must equal the supplied content tree.
- `admit_private_git_preparation` retains the caller-authorized capability used by strict private-output inspection. It does not restore the removed create/materialize/commit dispatcher or authorize ref publication. Existing/private output evidence remains read-only and physically bound.
- `ref_compare_and_swap_args(ref, new_commit, expected_old_commit, reason=...)` builds the expected-old `update-ref` arguments, adding `-m <reason>` only when a reflog reason is supplied. It returns argv; it starts no Git process and publishes no ref. The publication caller executes those arguments, so Git refuses a move whose old value changed. [56]

Exact-object eligibility predicates and their regex constants live in the sibling `git_object_memo_keys.py`. This runner imports the two predicate consumers directly; request scope, memo keys, successful-result retention and Git execution remain here.

## Byte-exact Git observation

A NUL-delimited Git pathname is an exact byte identity. Ordinary run_git still uses text transport, whose universal-newline handling can collapse CR and LF pathnames. run_git_bytes selects raw output through the same _git_run environment, identity guard, working directory, timeout and session options. _tree_change_after_images splits b"\0", keeps pathname keys as bytes, and decodes only the ASCII mode/blob fields. It raises on failed or malformed raw diff output; it does not normalize, rename-pair or infer path equivalence.

The extraction of _git_run shares the former run_git setup; it does not make the general text runner byte-preserving or add a second Git environment policy.


## Current Behavior

The shared runner accepts a cancellation event through `_GIT_CANCELLATION` and `cancellable_git_commands` (lines 517–529). `_run_git` uses `_wait_process` when a cancellation event is present or a new session is requested (lines 356–412). The wait polls at intervals of at most 0.05 seconds when cancellation is enabled; `_kill_process_group` is the runner's one process-group kill owner for a timeout or abandoned read (lines 415–468). Without an event, the ordinary timeout behavior remains. [57] [58]


## Evidence

- The byte runner bypasses text decoding and universal-newline conversion. [54]

- Both public transports share environment scrubbing, identity validation and execution options. [55]


- The existing general runner remains text-mode through the shared setup. [34]



- The eight repository selectors that are removed from the environment. [31]
- The scrubbed environment every runner starts from. [32]

- The options object: work directory, input, timeout and identity. [33]


- The one argv: work directory, long paths and the exact safe directory. [35]

- The one spawn: captured output, no check, input or DEVNULL, text or raw bytes. [36]

- The four timeout classes. [37]
- The option tuples for parsed diffs and the settings they override. [38]
- The runner with one explicit index. [39]
- The runner with a disposable index and object directory. [40]
- The index copy keeps the source file's times, read from one open file. [41]

- The shared-read block: one dictionary per block, reset on exit. [42]


- The batched reader answers held blobs from the block and reads only the others. [43]

- Held blobs are looked up by repository path and blob ID. [44]

- One cat-file batch; a header that is not the requested blob raises. [45]

- The three-way merge prints its result and returns the conflict count. [46]
- The existing-output proof runs before and after the raw commit read. [47]
- A repeated blob read inside the block starts no Git process and never crosses repositories. [51]
- The parsed diffs of the reviewer and the worklist carry the options. [52]

- The runner keeps memo ownership and imports exact-object eligibility from its direct sibling. [53]
- The CAS helper builds expected-old update-ref arguments with an optional reflog reason; it does not execute them. [56]
- The cancellation context supplies one event to the shared runner. [57]
- The shared wait bounds cancellation polling and owns timeout and abandoned-read termination. [58]
