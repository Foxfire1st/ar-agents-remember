# mcp/tests/test_integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces pre-CAS ref races, direct recovery capability routing, protected-checkout refusal states,
post-CAS untracked-file refusal, and idempotent external-pair retry after one checkout was already
refreshed.

## Code Commentary

The suite verifies exact named refs remain authoritative while checkout repair accepts only clean
old or already-new state. Recovery tests cover both code and memory sides plus invalid-side,
wrong-tip, untracked, unrelated-change, wrong-HEAD, and durable pre-crash evidence branches.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `IntegrationRefTransactionTests` | mcp/tests/test_integration_ref_transaction.py:41-221 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260815-DAG Master Full-Gate Repair

Imports re-point to the restructured `worktrees/integration/` package (`integration_ref_transaction`,
`lifecycle_operations`, `lifecycle_operation_store`). The suite gained two negative proofs for
`require_integrated_ledger_mapping`: a foreign code commit with no landed ledger mapping refuses
with the exact requirement, and a forged ledger commit whose ancestry excludes the landed memory
content refuses as unreachable.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: re-pointed imports to the
  worktrees/integration package and added the no-landed-mapping and unreachable-memory-content
  refusal proofs for `require_integrated_ledger_mapping`. Verified at code commit e5cb139f.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — No content impact: L5 extends the suite for the organizational-completion super-to-leaf ledger mapping; the documented transaction behavior is unchanged and the additions are covered by the new completion cards.

- 2026-08-16T08:12+02:00 — Dagger coverage repair: expanded exact transaction forcing across preparation races, both recovery sides, checkout refusal branches, and the durable-before-crash external retry order.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the checkout-refresh crash/retry case isolates queue publication/completion while retaining the real integration recovery and named-ref transaction owners under test.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration ref transaction forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
