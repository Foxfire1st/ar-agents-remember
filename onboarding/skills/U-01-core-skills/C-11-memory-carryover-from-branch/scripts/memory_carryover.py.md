# memory_carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-11-memory-carryover-from-branch/scripts/memory_carryover.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-11T03:00                           |
| lastVerifiedCommitHash | `65e91dc05628e0652647be8d3bed865b195ad6e1`                         |
| lastVerifiedCommitDate | 2026-05-11T03:15:36+02:00|

## Purpose

`memory_carryover.py` is the C-11 command helper. It compares official code, source branch code, official memory, and source branch memory so richer branch onboarding can be carried into official memory only when the corresponding code landed.

## Code Commentary

### Logic

The helper exposes `plan` and `apply` subcommands. `plan` resolves the official/source-branch/old-base refs, lists paths changed on the source branch, compares them to official changes, builds carryover candidates, and emits a JSON report with decisions. Candidate evidence is derived from exact landed commit ancestry, patch-id equivalence, final content equality, same-path ambiguity, or not-landed absence. `apply` requires `--approved` plus an approval note, requires official memory to be clean, copies selected onboarding from source branch memory into official memory, refreshes `lastVerifiedCommitHash` and `lastVerifiedCommitDate` to the official code commit/date, commits official memory content, prepends a new official memory ledger mapping, and commits the ledger.

### Conventions

The script uses explicit paths and refs rather than resolving project context through C-08, because C-11 needs to compare two code refs and two memory locations that may not be the active checkout. Output paths are serialized as POSIX strings. Only proven evidence tiers are auto-carry by default; same-path candidates can be included through explicit review-required selection.

### Invariants And Boundaries

The helper mutates only the official memory repo during apply. It does not move code branches, does not copy source branch ledger rows, does not carry rejected candidates, and does not overwrite different existing official onboarding unless the caller opts into replacement or review-required inclusion. A missing `memory.md`, dirty official memory repo, missing onboarding metadata, or missing approval blocks apply.

### Todos

Future iterations can add structural onboarding merge strategies and a manifest-based approval file for review-required candidates.

### Docs References

No external documentation is needed for this standard-library helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper defines Git wrappers, evidence classification, onboarding path mapping, candidate planning, metadata refresh, selected candidate application, official memory content commit, and official ledger commit behavior. | current | [memory_carryover.py](agents-remember-md/skills/U-01-core-skills/C-11-memory-carryover-from-branch/scripts/memory_carryover.py) |
| The test suite covers landed carryover, same-path ambiguity, and not-landed rejection against temporary Git repos. | current | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-11T03:00: Created onboarding for the C-11 memory carryover command helper and generalized its public inputs from workbench-only to source branches.
