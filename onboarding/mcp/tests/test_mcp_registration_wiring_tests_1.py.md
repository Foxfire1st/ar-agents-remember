# mcp/tests/test_mcp_registration_wiring_tests_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_mcp_registration_wiring_tests_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Registration wiring suite for context, memory, provider, and structural agent tools.

## Code Commentary

L23 proves MCP `citation_fix` forwards the required leaf contract plus document/snapshot guard and dry-run flag.

### Logic

The suite proves `dispatch_agent` forwards only task-document identity, role, brief, and label; child rename/retire/message tools use structural document+role or ambient parent identity; exact occupant-id arguments are absent. It also pins memory-health contract scoping and provider/tool forwarding.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the registered or owning seam directly.

### Invariants And Boundaries

MCP registration is a thin adapter: structural authority is forwarded to application services and private occupant identity never crosses the tool schema.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `RegistrationWiringTests1` | mcp/tests/test_mcp_registration_wiring_tests_1.py:6-6 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_mcp_registration_wiring_tests_1.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
