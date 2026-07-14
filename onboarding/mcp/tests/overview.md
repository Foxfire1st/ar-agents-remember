# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | mcp/tests |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-12T20:24+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b`|
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|

## Purpose

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

The L1 regression set adds a fake-adapter conformance suite for normalized harness control,
correlated acceptance/reconciliation, private IPC, bounded queue/ledger behavior, shutdown failure
paths, and R11 surface-owned draft preservation. Existing settings, harness, catalog, opener, and
WebSocket tests pin the additive launch/API projections and preserve legacy behavior.
The 260713-PHA-L3 additions add fake and stdio transport coverage for the pinned Codex app-server:
exact initialize/model/thread setup, protocol-only effort validation and echoing, structured
status/completion and server requests, explicit busy behavior, bounded malformed/oversized input,
and reconnect correlation without resend. An opt-in live smoke proves exact-version readiness using
an ephemeral thread with no prompt or credential output.

The 260713-PHA-L2 tests add pinned Claude Code 2.1.207 JSONL fixtures, fake-transport conformance,
and an opt-in credential-safe live smoke. The smoke submits the advertised local `/cost` command
through the same correlated acceptance/result path without a model API request. A mixed
`success`/`is_error=true` API-429 regression remains failed and retains only safe terminal metadata;
no result text, stderr, credentials, environment, or settings are emitted or retained.

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

260713-PHA-L6 tests preserve exact Claude/Codex/Pi versions only as fixture and smoke baselines,
while proving structured capability acceptance/rejection and the exact additive inbox allowlist.
No test documents R10 resource performance as current behavior.

260712-PTS-L1 tests prove the worktree-contract read/heal split: zero-traversal contract loads (loud
tripwires on the resolver entry points and pathlib walk primitives), legacy leaf ids returned verbatim
by reads, heal parity with the removed read-time normalization, canonical-skip idempotence without
resolution, dry-run reporting, torn-contract tolerance, and the `heal-leaf-ids` CLI seam.

260712-TRH-L5 tests prove the narrow confirmed-gone eligibility boundary, terminal and tmux
positive-gone evidence, fail-closed indeterminate behavior, one-fold/one-snapshot boundedness,
same-lock resolve-plus-compact ordering, stale-snapshot non-resurrection, unchanged TTL fallback,
persisted folded-id removal counts, body-free aggregate events, and silence on no-op sweeps.

260713-PHA-L4 tests prove the Pi boundary at three levels: pinned capability/framing and schema
policy, fake-adapter queue/retry/compaction/settlement, extension UI, disconnect, cursor
reconciliation, and no-resend behavior, and the real subprocess's correlation, malformed stdout,
EOF ambiguity, and clean stop. The opt-in real smoke installs Pi 0.80.6 under a temporary
prefix/HOME/cache and verifies `get_state` readiness without changing global tools.

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the test-route body for structured
  capability negotiation, rolling inbox compatibility, and the deferred R10 boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: added fake protocol, pinned JSONL fixture, and
  credential-safe `/cost` live-smoke coverage for Claude 2.1.207, including failed API-429 semantics.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator: added route coverage for the Codex app-server
  fixture, adapter/protocol fake tests, and credential-safe live smoke. Verification remains pinned
  until closeout stamps the leaf commit.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: added governing route coverage for the Pi RPC
  protocol, subprocess, adapter, fixture, and isolated real-smoke regression files. Verification
  metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: added route-body coverage for the
  bridge conformance suite and its five changed serving regression files.
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
