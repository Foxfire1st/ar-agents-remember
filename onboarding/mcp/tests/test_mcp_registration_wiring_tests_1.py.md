# mcp/tests/test_mcp_registration_wiring_tests_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_mcp_registration_wiring_tests_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T21:30+02:00                                            |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df`                                        |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00|
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

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260815-DAG-L15 memory_quality_check Background-Run Registration

Two registration tests drive the live FastMCP schema for the keyword-only `wait`/`run_id`:
`test_memory_quality_check_wait_false_starts_a_background_run` proves `wait: false` routes to the
start payload (returns `{status, runId}`) with the same default forwarding; `test_memory_quality_check_run_id_polls_the_run`
proves `run_id` routes to the poll payload (a poll returns the identical full result; a
run-not-found envelope → rerun guidance).

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added the wait=false start-run and run_id poll registration tests for memory_quality_check (start returns {status, runId}; a poll returns the identical full result; run-not-found → rerun guidance). Verified at code commit de3a0fd9.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_mcp_registration_wiring_tests_1.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
