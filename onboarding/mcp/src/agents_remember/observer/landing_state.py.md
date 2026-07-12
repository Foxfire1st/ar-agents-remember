# mcp/src/agents_remember/observer/landing_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/observer/landing_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:30+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[observer overview](overview.md)

## Purpose

`LandingStateRefresher` moves remote landing observation out of the recurring projection hot path. It owns one lifecycle-managed loop, refreshes due landing-active contracts with bounded concurrency, and publishes immutable exact-contract facts for projection consumers.

## Code Commentary

`contract_key` includes repository, worktree group, code and memory identities, and the contract path, preventing observations from bleeding across rewritten or neighboring worktrees. Each sweep builds a bounded due set, gathers observations with the configured concurrency cap, and publishes a copy-on-write mapping. Startup is explicit `missing`; failed refreshes carry the last truthful observation as `stale`; age also becomes stale after the configured threshold. Cancellation propagates through the loop and leaves no writer task behind. Unexpected cycle failures are logged and the next ordinary cadence remains the only retry.

## Invariants And Boundaries

- The refresher performs remote work only outside projection.
- Published facts are immutable snapshots and retention is limited to the latest landing-active sweep.
- Failures never invent remote or PR state.
- Lifecycle cancellation is safe and does not create per-tick tasks or unbounded workers.

## Docs References

No external Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Projector owns startup and cancellation. | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| Landing facts are merged into projected status. | [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |

## Cross-Repo References

No cross-repo references.

## Update History

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: created for the bounded, exact-keyed, lifecycle-managed background landing observer.
