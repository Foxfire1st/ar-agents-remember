# mcp/tests/test_git_command.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests of the one Git runner in `kernel/git_command.py`: that an exported repository selector cannot
redirect a command, that a timeout bounds a stalled command, that the shared blob-read block reads a blob
from a repository once, that concurrent candidate captures are isolated, and that the private preparation
of a commit keeps exact state and refuses forged or stale authority.

## Code Commentary

- The module's helpers create real repositories in temporary directories (`_init`, `_commit`).
  `_selectors(decoy)` points all eight selector variables at a decoy repository. The redirection test sets
  them inside its own scope, because `conftest.py` removes them from the environment at import; the test
  therefore passes only when the production runner strips them.
- `DecoyRepositoryTests`: with every selector pointing at the decoy, `commit_if_dirty` on the real
  repository advances the real branch and leaves the decoy's head and files unchanged.
- `SharedBlobReadTests`: `subprocess.run` of the runner module is counted. Outside a
  `shared_blob_reads()` block two reads of one blob start two Git processes. Inside a block a batch of two
  blobs starts one process, a second batch of the same blobs and a single read start none, and the answers
  are equal and keyed in sorted order. The same blob ID asked of a second repository that lacks the object
  raises `GitPreparationError`. After the block a read starts a process again.
- `RunnerContractTests`: an explicit timeout still bounds a stalled command.
- `CandidateTreeConcurrencyTests`: concurrent `worktree_candidate_tree` observers are isolated from each
  other.
- `PrivateGitPreparationTests`: an exact private commit keeps the logical head and index and runs the
  normal hook policy; raw commit bytes keep CRLF and an opaque signature header; a cancelled owner and a
  forged capability start no commit; hidden index flags and changed physical bytes refuse; a stale logical
  tip and rebound private metadata refuse before any mutation; a failed hook returns its own failure and
  is not retried.

## Evidence

- The module docstring: why the redirection tests set the selectors themselves. [10]
- A commit lands in the real repository and not in the decoy. [11]
- A repeated blob read inside the block starts no Git process and never crosses repositories. [12]
- An explicit timeout bounds a stalled command. [13]
- Concurrent candidate captures are isolated. [14]
- The private preparation cases. [15]
- The block under test. [16]
