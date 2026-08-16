# mcp/tests/test_l4_authority_branch_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_authority_branch_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T09:45+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces fail-closed Git branch/default facts, exact lifecycle-operation and configured-contract
authority, integration recovery, topology publication, source lineage, and atomic-series edges.

## Code Commentary

Repository tests cover blank, cyclic, malformed, missing, detached, and Git-error branch facts.
Operation tests cover absent/wrong journal identity, source/candidate drift, code and memory repository
identity changes, and internal/external memory authority-shape mismatches.
The public integration preparation case advances the protected source inside queue/repository
publication and proves the structured source-moved refusal wins before irreversible progress.
Focused additions cover task-path/worktree ownership, stale worker recovery, queue binding identity,
candidate validation, torn ref recovery, unavailable organizational lineage, and incomplete atomic
leaf sets through the production helpers that own those checks.

## Invariants And Boundaries

- Negative cases reach the production authority owner, not duplicated test logic.
- A refusal occurs before protected-ref mutation.
- Code and external-memory identities remain exact and independently proven.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite owns focused negative forcing for repository and journal authority. | `IntegrationBranchRepositoryCoverageTests`; `IntegrationOperationAuthorityCoverageTests` | mcp/tests/test_l4_authority_branch_coverage.py:61-195; mcp/tests/test_l4_authority_branch_coverage.py:198-618 |
| Configured topology, integration validation/recovery, lineage, and series completeness are forced at their production owners. | `IntegrationBranchAuthorityCoverageTests`; `IntegrationValidationCoverageTests`; `LineageAndSeriesCoverageTests` | mcp/tests/test_l4_authority_branch_coverage.py:621-763; mcp/tests/test_l4_authority_branch_coverage.py:766-899; mcp/tests/test_l4_authority_branch_coverage.py:902-1032 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T09:55+02:00 — Added a real exact-series positive case to the atomic surface probe, proving canonical task-tree resolution rather than only false cases.
- 2026-08-16T09:45+02:00 — Added production-owner coverage for configured contract identity, lifecycle recovery, task publication, integration candidate/ref recovery, organizational lineage, and atomic-series completeness after the targeted Dagger diff-coverage report.
- 2026-08-16T08:12+02:00 — Created focused L4 negative-branch forcing during targeted Dagger coverage repair.
