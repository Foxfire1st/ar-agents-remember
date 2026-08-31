# mcp/tests/test_e2e_harness_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_e2e_harness_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T07:35+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves the ambient role-chat E2E selector names every direct repository dependency derived from the
canonical dependency facts.

## Code Commentary

### Logic

The test loads the repository harness selector, derives the direct dependency closure from
`RepositoryDependencyFacts`, and fails with the missing path set if any dependency can change without
selecting the scenario.

### Conventions

Dependency facts are source-derived; the test does not duplicate a second manually asserted closure.

### Invariants And Boundaries

- Every direct production dependency selects the expensive E2E.
- Selection remains prefix-based and explicit.
- Transitive Python consumer ownership remains outside this focused contract.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selector must cover the full derived direct dependency set. | `test_targeted_selection_covers_every_direct_repository_dependency` | mcp/tests/test_e2e_harness_selection.py:40-51 |

## Cross-Repo References

No cross-repository implementation dependency governs this suite.

## Update History

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
