# test_git_freshness.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_git_freshness.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T08:39+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                         |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_git_freshness.py` unit-tests the issue #54 freshness kernel
(`kernel/git_freshness.py`) against real temporary git fixtures.

## Code Commentary

### Logic

`make_clone_pair` builds a bare `origin.git` with two clones so remote movement
is simulated by committing in one clone and pushing, then reading freshness
from the other. State coverage: non-git directory (`unavailable`/`no-branch`),
no remote (`no-upstream`), detached HEAD (`no-branch`), matching upstream
(`current`, fetched), remote moved (`behind` 0/1), local unpushed (`ahead`
1/0), both moved (`diverged` 1/1), fetch failure via a missing remote URL
(`unknown` with error, counts still computed from the stale tracking ref),
`fetch=False` (counts without fetching), and the helper primitives
(`upstream_ref`, `fetch_remote`, `ahead_behind`) directly.

### Invariants And Boundaries

Tests use real git subprocesses, no mocking — the kernel's contract is the
actual git CLI behavior. Fixtures set explicit git identity so commits work in
clean CI environments.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The kernel under test. | [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| Packet-level freshness coverage lives with the context packet tests. | [test_context_packet.py](agents-remember/mcp/tests/test_context_packet.py) |

## Update History

- 2026-06-10T08:39+02:00: Created with the issue #54 freshness kernel (9 tests over bare-origin clone-pair fixtures).
