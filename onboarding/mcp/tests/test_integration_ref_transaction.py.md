# mcp/tests/test_integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
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

## Update History

- 2026-08-16T08:12+02:00 — Dagger coverage repair: expanded exact transaction forcing across preparation races, both recovery sides, checkout refusal branches, and the durable-before-crash external retry order.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the checkout-refresh crash/retry case isolates queue publication/completion while retaining the real integration recovery and named-ref transaction owners under test.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration ref transaction forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
