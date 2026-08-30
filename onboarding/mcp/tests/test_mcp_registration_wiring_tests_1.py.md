# mcp/tests/test_mcp_registration_wiring_tests_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_mcp_registration_wiring_tests_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T14:19+02:00                                            |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5`                                        |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
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
| Current suite declaration anchoring this card. | `RegistrationWiringTests1` | mcp/tests/test_mcp_registration_wiring_tests_1.py:16-771 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-DAGQC-L2 Public Request Grammar Proof

The memory-quality cases drive the registered FastMCP tool with each strict request mode, prove
poll refuses explicit execution fields before dispatch, and inspect the published schema for one
discriminated request object. They do not preserve or exercise the retired flat grammar.

## MCAR-L03 Poll Schema Wiring

Registration forcing now permits and forwards the exact candidate `contract_path` on poll while
continuing to reject execution-only poll fields.

## Update History

- 2026-08-29T21:46+02:00 — MCAR-L03: covered contract-bound candidate polling in the public
  request schema and adapter. Dagger verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added live FastMCP proofs for exact sync/start/poll dispatch, poll-field conflict refusal, and the one discriminated request schema. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added the wait=false start-run and run_id poll registration tests for memory_quality_check (start returns {status, runId}; a poll returns the identical full result; run-not-found → rerun guidance). Verified at code commit de3a0fd9.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_mcp_registration_wiring_tests_1.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
