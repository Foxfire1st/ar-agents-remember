# mcp/src/agents_remember/serving/projections/landing_state.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`LandingStateRefresher` moves remote landing observation out of the recurring projection hot path. It owns one lifecycle-managed loop, refreshes due landing-active contracts with bounded concurrency, and publishes immutable exact-contract facts for projection consumers.

## Truthful terminal history and exact finishing eligibility

A completed arc lacking a valid current-contract final may receive exactly one finishing attempt per process, including at startup, with at most four terminal admissions per sweep. Matching valid finals serve without an attempt. The attempt stays consumed after success, failure or later final loss; only a real reopen re-arms that arc. Abandoned/build-only keys remain probe-free. This deliberately supersedes the earlier startup-zero exclusion, not the exact-key, matching-final or no-recurring-history boundaries.

Missing, corrupt or contract-predating finals stay honest terminal missing facts (`no final observation recorded`), not a promise of recurring repair. Successful complete finishing facts may freeze once. Existing manual exact-current reads remain available. Real reopen invalidates the prior final; build-only phases stay probe-free until closeout or integration activates landing again. The concurrency cap remains four. Serving-bound open probes deliberately replace the former fixed 30-second cadence with actual page interest and unchanged-answer age scheduling; explicit unbound refresh callers retain their prior API.

## Page Interest And Due Scheduling

The app binds actual Projector subscriber membership. Without interest, `refresh_once` returns before contract discovery, rechecks after its awaited discovery, and rechecks again after semaphore admission before each probe. A probe already admitted is not cancelled merely because the last page departs; no new admission proceeds once that boundary observes no interest. Unbound explicit refreshes remain unconditional.

For bound serving refreshes, `LandingProbeSchedule` retains only the currently eligible exact identities. A new or changed contract is due immediately on the next interested pass. A published semantic answer keeps its unchanged-age epoch only while its selected fields and row order match. Due intervals are 30 seconds below 120 seconds of unchanged age, 120 below 600, 600 below 3600, and 3600 thereafter. A changed answer or a clock before the remembered epoch resets the schedule. Observation-age noise is excluded, but the fact's own `at` is semantic. Due timestamps are eligibility for the next ordinary sweep, not an end-to-end freshness guarantee.

The schedule advances only after rows are actually published; a disconnect-skipped probe neither publishes nor consumes the terminal attempt. Existing shared-ref sweep scope, accounted drained offload, immutable observations, exact final validation and one-attempt-per-completed-arc protection remain. Reopen/rewrite/new identities cannot inherit a departed contract's deadline. No subscriber means no new landing discovery or remote work, not zero work for the entire dashboard.



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


### Cross-Repo References

No cross-repo references.

## 260718-CHATS-L5I Current Delta

Completed contracts can freeze one fully observed landing result in `landing-final.json`, removing them from recurring remote probes. Frozen rows are validated and projected to reducer-known fields; corrupt, stale, or pre-reopen files are rejected so a reopened contract returns to live observation rather than serving the old landing result.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

Successful atomic replacement of a final file invalidates the writer's parsed-final cache for that exact path, including an equal old/new mtime. The next read serves the new valid facts without an additional observation or historical retry; failed writes keep the existing reported failure path.


- Projector owns startup and cancellation. [1]

- Landing facts are merged into projected status.  Anchor: "def _safe_status_payload(  # pragma: no cover"; "def refresh_engine_process_landing(  # pragma: no cover" [2]
- Exact completed arcs with no valid final are eligible once, including startup, under bounded admissions. [3]

- A terminal finishing attempt remains consumed after success, failure and subsequent final loss until reopen. [4]


- Final facts are served only after complete matching reducer/participant validation, otherwise as honest missing. [5]


- Bound interest gates discovery, due selection, publication-driven schedule advance and probe admission; unbound callers retain explicit refresh behavior. [7]
- Current-identity retention and semantic-answer age determine transient due times. [8]

- Successful final replacement invalidates the old parsed cache before fresh facts are served, including equal filesystem timestamps.  Anchor: `LandingStateRefresher._maybe_freeze` [6]
