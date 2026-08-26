# mcp/src/agents_remember/serving/projections/landing_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/projections/landing_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:30+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving projections overview](overview.md)

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Projector owns startup and cancellation. | `run` | mcp/src/agents_remember/serving/projector.py:193-236 |
| Landing facts are merged into projected status. | "def _safe_status_payload(  # pragma: no cover"; "def refresh_engine_process_landing(  # pragma: no cover" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:302-302; mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:348-348 |

## Cross-Repo References

No cross-repo references.

## 260718-CHATS-L5I Current Delta

Completed contracts can freeze one fully observed landing result in `landing-final.json`, removing them from recurring remote probes. Frozen rows are validated and projected to reducer-known fields; corrupt, stale, or pre-reopen files are rejected so a reopened contract returns to live observation rather than serving the old landing result.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T11:40:58+02:00 — 260731-EFA-L6 S18-B08 curator: bound startup/cancellation and landing-merge claims to the current projector and snapshot constructs.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: created for the bounded, exact-keyed, lifecycle-managed background landing observer.
