# mcp/tests/test_git_command.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests of the shared Git runners in `kernel/git_command.py`: that an exported repository selector cannot
redirect a command, that a timeout bounds a stalled command, that the shared blob-read block reads a blob
from a repository once, that concurrent candidate captures are isolated, and that the private preparation
of a commit keeps exact state and refuses forged or stale authority.

## Code Commentary

- The imported shared test-support helpers create real repositories in temporary directories (`_init`, `_commit`).
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

Tree publication now runs pre-commit before ref movement and records Commit-Check-Pass. Ref-transaction refusal remains native Git evidence after that check. Message comparison strips only the required pass trailer before comparison with porcelain; it does not assert raw equality of a stamped message to an unstamped argument. Both private preparation policy spellings now exercise ordinary commit hooks; the old strict-code spelling supplies compatibility vocabulary, not a skip.

The shared `_init` and `_commit` fixtures live in `agents_remember_test_support.testing.git_command` and are imported directly. `ReplaceFreshnessTests` lives in `test_git_object_memo.py`; its replacement-sensitive freshness controls moved unchanged. The runner and publication tests remain in this module.

## Evidence

- The module docstring: why the redirection tests set the selectors themselves. [10]
- A commit lands in the real repository and not in the decoy. [11]
- A repeated blob read inside the block starts no Git process and never crosses repositories. [12]
- An explicit timeout bounds a stalled command. [13]
- Concurrent candidate captures are isolated. [14]
- The private preparation cases. [15]
- The block under test. [16]

- Tree publication now runs pre-commit before ref movement and records Commit-Check-Pass. Ref-transaction refusal remains native Git evidence after that check. Message comparison strips only the required pass trailer before comparison with porcelain; it does not assert raw equality of a stamped message to an unstamped argument. Both private preparation policy spellings now exercise ordinary commit hooks; the old strict-code spelling supplies compatibility vocabulary, not a skip. [17]

- Shared real-Git fixtures and replacement-freshness cases have direct owners, with no duplicated helper or re-export. [18]
