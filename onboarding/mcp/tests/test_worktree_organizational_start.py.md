# mcp/tests/test_worktree_organizational_start.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_organizational_start.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T09:45+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Proves an organizational master opens a leaf directly from the sprint super without creating an atomic series contract or branch.

## Code Commentary

The production start builder and real external coordination topology distinguish organizational
direct-super ownership from atomic series ownership. Memory is explicitly disabled for this
code-topology test while the configured external memory root is still materialized for context
resolution.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `OrganizationalWorktreeStartTests` | mcp/tests/test_worktree_organizational_start.py:19-121 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T09:45+02:00 — Made the external-coordination fixture coherent by materializing its configured external memory root while disabling memory for the direct-super code-path assertion.
- 2026-08-16T08:12+02:00 — Dagger fixture repair: materialized the canonical organizational leaf task document named by the master row before exercising the real direct-super start owner.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the organizational direct-super start selects the internal topology matching its initialized repo-local memory and requested contract mode.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: internal-memory organizational start creates both required memory-system directories before exercising direct-super leaf construction.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created organizational leaf start forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
