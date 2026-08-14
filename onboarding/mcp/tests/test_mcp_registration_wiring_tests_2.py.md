# mcp/tests/test_mcp_registration_wiring_tests_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_mcp_registration_wiring_tests_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Registration wiring suite for worktree, task-document, lifecycle, and structural gate tools.

## Code Commentary

L23 proves `worktree_operation_cancel` forwards only the task address, operation kind, developer intent, and dry-run choice—never an operation ID.

### Logic

The suite pins closeout message grouping, task-document edit/read shapes, ambient lifecycle signals, structural lifecycle-gate raise, and `gate_decide` by canonical document plus kind without a gate id.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the registered or owning seam directly.

### Invariants And Boundaries

Registration must not reintroduce exact gate, lifecycle, or occupant addressing; application composition owns authority and refusal.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `RegistrationWiringTests2` | mcp/tests/test_mcp_registration_wiring_tests_2.py:6-6 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_mcp_registration_wiring_tests_2.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `include_terminal` poll kwarg
  pin (N11) and the `operator_inbox_supersede` wiring test (R11). Verification metadata pinned
  until closeout stamps the 260713-TES-L4 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
