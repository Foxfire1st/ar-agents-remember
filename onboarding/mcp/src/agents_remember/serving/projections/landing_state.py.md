# mcp/src/agents_remember/serving/projections/landing_state.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`LandingStateRefresher` moves remote landing observation out of the recurring projection hot path. It owns one lifecycle-managed loop, refreshes due landing-active contracts with bounded concurrency, and publishes immutable exact-contract facts for projection consumers.

## Truthful terminal history and exact finishing eligibility

Historical completed/abandoned keys receive no periodic Git/network probe, including at startup. An exact key retained from the preceding active sweep may receive one finishing attempt after completion only when it lacks a valid current-contract persisted final. Matching valid finals are served without another attempt. The active observation map drops completed keys after that attempt even if it failed or could not freeze complete facts.

Missing, corrupt or contract-predating finals stay honest terminal missing facts (`no final observation recorded`), not a promise of recurring repair. Successful complete finishing facts may freeze once. Existing manual exact-current reads remain available. Real reopen invalidates the prior final; build-only phases stay probe-free until closeout or integration activates landing again. Open due probes retain 30-second cadence/four concurrency.


- Exact keys and final validity govern finishing eligibility. [3]
- Terminal keys leave the retained sweep after their single attempt. [4]
- Final facts are served or honestly reported missing. [5]

## Code Commentary

`contract_key` includes repository, worktree group, code and memory identities, and the contract path, preventing observations from bleeding across rewritten or neighboring worktrees. Each sweep builds a bounded due set, gathers observations with the configured concurrency cap, and publishes a copy-on-write mapping. Startup is explicit `missing`; failed refreshes carry the last truthful observation as `stale`; age also becomes stale after the configured threshold. Cancellation propagates through the loop and leaves no writer task behind. Unexpected cycle failures are logged and the next ordinary cadence remains the only retry.

## Invariants And Boundaries

- The refresher performs remote work only outside projection.
- Published facts are immutable snapshots and retention is limited to the latest landing-active sweep.
- Failures never invent remote or PR state.
- Lifecycle cancellation is safe and does not create per-tick tasks or unbounded workers.

## Evidence

### Docs References

No external Domain Documentation source is configured.

### Repo-Internal References

- Projector owns startup and cancellation. [1]
- Landing facts are merged into projected status. [2]

### Cross-Repo References

No cross-repo references.

## 260718-CHATS-L5I Current Delta

Completed contracts can freeze one fully observed landing result in `landing-final.json`, removing them from recurring remote probes. Frozen rows are validated and projected to reducer-known fields; corrupt, stale, or pre-reopen files are rejected so a reopened contract returns to live observation rather than serving the old landing result.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

Successful atomic replacement of a final file invalidates the writer's parsed-final cache for that exact path, including an equal old/new mtime. The next read serves the new valid facts without an additional observation or historical retry; failed writes keep the existing reported failure path.

- Successful final replacement invalidates the old parsed cache before fresh facts are served, including equal filesystem timestamps. [6]
