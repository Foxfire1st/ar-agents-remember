# mcp/src/agents_remember/kernel/git_command.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

The one place in the package that starts a `git` process. Every command goes through `run_git` or one of the
runners beside it, which share one argument builder and one spawn (`_git_argv`, `_run_git`). The module also
holds the exact-bytes readers of Git objects, the batched blob reader with its optional shared-read block, the
option tuples for diffs whose output is parsed, the index copy for disposable captures, the three-way file
merge, and the two guarded mutation families: private preparation and closeout ref publication.

## Code Commentary

### The runner

- `git_environment()` copies the process environment and removes the eight repository selectors of
  `GIT_REPOSITORY_SELECTOR_ENV` (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
  `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`). An exported selector
  therefore cannot aim a command at another repository.
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
  `GIT_BULK_REMOTE_TIMEOUT_SECONDS = 1800`. A timeout raises `subprocess.TimeoutExpired` to the caller.
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
  worklist child is the one caller that enters the block.
- `merge_file_bytes` runs `git merge-file -p` over three files and returns the merged bytes and the number
  of conflicts, which is Git's exit status. It writes nothing. An exit status below 0 or above 127 raises.

### Private preparation and closeout publication

- `inspect_existing_git_preparation` proves an existing logical output (root, common directory, branch ref,
  `HEAD`, tree, index, index flags and physical files) before and after it reads the commit's raw bytes. For
  a memory binding the root `memory.md` is left out of the index and physical comparison, and the tree
  without it must equal the supplied content tree.
- `admit_private_git_preparation` returns a capability for one detached private worktree after the caller's
  `authorize` callback. `preparation_command` describes the one command of each step (`worktree add
  --detach --no-checkout`, `read-tree --reset -u`, `commit`), and `run_git_preparation` runs a step only
  from its required state (`absent`, `created`, `materialized`) and reads the state back afterwards.
- `admit_git_closeout_publication`, `closeout_publication_command` and `publish_git_closeout_ref` publish a
  prepared commit with one `update-ref <ref> <new> <expected old>`. A ref that already names the prepared
  commit, or an output that equals the old commit, returns evidence without a command. A new memory
  publication whose tree holds `memory.md` is refused.

## Evidence

- The eight repository selectors that are removed from the environment. [31]
- The scrubbed environment every runner starts from. [32]
- The options object: work directory, input, timeout and identity. [33]
- The general runner; an identity that names a selector raises. [34]
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
- The command of each private preparation step. [48]
- A preparation step runs only from its required state. [49]
- The closeout publication is one compare-and-swap of the ref. [50]
- A repeated blob read inside the block starts no Git process and never crosses repositories. [51]
- The parsed diffs of the reviewer and the worklist carry the options. [52]
