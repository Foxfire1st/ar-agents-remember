# mcp/tests/test_atomic_series_seal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_seal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-20T05:12+02:00 |
| lastVerifiedCommitHash | `0a746c9f157e3e536f2ac947e999559c74be9e73` |
| lastVerifiedCommitDate | 2026-08-19T11:22:41T+0200|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces complete-leaf-chain sealing, child-admission closure, terminal child census, reserved enclosure names, and queue/repository TOCTOU rechecks.

## Code Commentary

The suite uses real code and external-memory refs/contracts and asserts terminal refusal preserves child tips, worktrees, contracts, reports, and tombstones. It also refuses direct atomic-series terminal capability minting, proves valid use only inside queue/repository publication, rejects wrong operation and path, rejects replay after normal and exceptional exit, rejects copied-context replay after issuer revocation, and proves the authorized race recheck runs while both authorities are held.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `AtomicSeriesSealTests` | mcp/tests/test_atomic_series_seal.py:49-756 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-20T05:12+02:00 — L13 landed-wave refresh: the series closeout-report routing
  commit (0a746c9f) touched this source; card re-verified against the current file, verification
  stamp advanced to 0a746c9f. Body unchanged — the documented contract still holds.


- 2026-08-19T04:05+02:00 — No content impact: 260815-DAG-L10 strengthened the seal test to write
  series reports under `worktrees/repo-a/master-b-ar/reports` (with an explicit absolute-path
  assertion, both terminal removers deleting them) while the colliding child leaf stays at
  `task_root/enclosures/reports/series-contract.md`; this card's refusal-preservation claims never
  asserted a reports location and remain accurate. Verification metadata stamped at the landed
  code commit `e41ea31d`.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-16T01:30+02:00 — Added copied-context replay forcing for the issuer-revoked terminal permit; verification remains closeout-owned.
- 2026-08-16T00:45+02:00 — Added direct series capability-mint refusal to the production-bound terminal seal suite; verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created atomic series seal forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
