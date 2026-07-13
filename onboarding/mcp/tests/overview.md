# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | mcp/tests |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-12T20:24+02:00 |
| lastVerifiedCommitHash | `b120efbfda76931cfa8eb9f24c9a808a62c10d1e`|
| lastVerifiedCommitDate | 2026-07-13T12:33:57+02:00|

## Purpose

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

The L7 test route additionally proves the projection/landing boundary: slow or failed remote observations do not delay local publication; observer results remain exact-contract and freshness-labeled; stale landing rendering is visible but motion-inert; invalid snapshot reads preserve local status; and a failed refresher does not skip serving shutdown. These are focused leaf regressions; the manager owns the full repository gate.

The 260712-PTS-L3 additions (new `test_change_watcher.py`, plus touched `test_serving.py`/
`test_dashboard_daemon.py` fixtures) prove change-driven projection pacing: the derived watch-root
list and self-trigger event filter, the pure `ChangePacer` deadline table (heartbeat/debounce/
interval-floor/max-delay/degraded), heartbeat-only quiet-world projection, debounce-bounded change
latency, burst coalescing, LOUD fixed-interval degrade on missing `watchfiles`/crashed
watcher/failed root derivation (with retry), watch-task lifecycle ownership, exact legacy pacing
without a watcher, `--heartbeat` CLI/daemon argv plumbing, and one real-inotify end-to-end pass.
The 260712-PTS-L2 additions to the projection scaling suite prove the shared per-tick contract
snapshot: one contract enumeration and at most one parse per contract per projection tick, zero
re-parses while the `(mtime_ns, size, ctime_ns)` stat identity holds, reader-output parity with and
without the injected snapshot, cache retention bounded to live contracts, chmod-000 and
utime-pinned-rewrite invalidation via ctime, and parse failures retried every build.

## Hot Path Summary

260712-PTS-L1 tests prove the worktree-contract read/heal split: zero-traversal contract loads (loud
tripwires on the resolver entry points and pathlib walk primitives), legacy leaf ids returned verbatim
by reads, heal parity with the removed read-time normalization, canonical-skip idempotence without
resolution, dry-run reporting, torn-contract tolerance, and the `heal-leaf-ids` CLI seam.

260712-TRH-L5 tests prove the narrow confirmed-gone eligibility boundary, terminal and tmux
positive-gone evidence, fail-closed indeterminate behavior, one-fold/one-snapshot boundedness,
same-lock resolve-plus-compact ordering, stale-snapshot non-resurrection, unchanged TTL fallback,
persisted folded-id removal counts, body-free aggregate events, and silence on no-op sweeps.

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

## Update History
- 2026-07-12T20:24+02:00 — 260712-PTS-L3 curator: added route coverage for the change-driven
  projection pacing regressions — new `test_change_watcher.py` (roots/filter/pacer/projector/real
  inotify) plus the `test_serving.py` `watch_changes=False` ETag fixture note and the
  `test_dashboard_daemon.py` heartbeat plumbing pins. Verification metadata remains pinned until
  closeout.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2 curator: added route coverage for the shared per-tick
  contract-snapshot regressions in `test_projection_scaling_cs6.py` (one enumeration/parse pass per
  tick, stat-identity cache with ctime hardening, output parity, live-set retention, failure retry).
  Verification metadata remains pinned until closeout.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1 curator: added route coverage for walk-free contract loads
  and the explicit heal sweep (parity, idempotence, dry-run, error tolerance, CLI seam) in
  `test_leaf_ref_resolution.py`. Verification metadata remains pinned until closeout.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: added governing route coverage for the new
  inbox-reclamation regression suite and its final PASS delta tests, including event silence and
  corrected persisted removal semantics. Verification metadata remains pinned until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: added route coverage for bounded landing observation, no-wait projection, stale rendering, invalid-snapshot containment, and shutdown after observer failure.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
