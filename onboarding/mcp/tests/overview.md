# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | mcp/tests |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-16T07:27+02:00 |
| lastVerifiedCommitHash | `d99a1a7f3ac251957ae155ea9beb878b9ba1ab25`|
| lastVerifiedCommitDate | 2026-07-16T07:36:40+02:00|

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

The current Codex completion regressions prove that a null protocol `requestId` is resolved only by
the protocol-owned text vendor correlation on exactly one accepted inbox row in the same hosted
session. Missing, non-text, unmatched, and ambiguous correlation evidence fails loudly. Completion
records adapter delivery metadata on that same row while explicit inbox state remains `pending` and
unconsumed; terminal state is `idle` / `immediate` without a queued replacement and
`settling` / `queued` only for an actual replacement. Exact 2.1.207, 0.144.3, and 0.80.6 values
remain fixture/smoke evidence, not production pins.

The 260713-PHA-L2 tests add pinned Claude Code 2.1.207 JSONL fixtures, fake-transport conformance,
and an opt-in credential-safe live smoke. The smoke submits the advertised local `/cost` command
through the same correlated acceptance/result path without a model API request. A mixed
`success`/`is_error=true` API-429 regression remains failed and retains only safe terminal metadata;
no result text, stderr, credentials, environment, or settings are emitted or retained.

260714-ACPUI-L1 moves the active Claude fake-transport fixture root to 2.1.210. Its initialization
fixture is the current test authority for separate control initialization, `system/init`, a
zero-turn bootstrap result, and correlated `list_models`; its interaction and turn companions keep
durable gates and acceptance-versus-completion covered in the same versioned cohort. The 2.1.207
fixtures remain historical evidence and are no longer loaded by the active adapter suite.

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

260714-ACPUI-L5 adds the final live-conformance and Claude discovery-isolation regressions. Claude
fake-transport cases cover separate variadic/repeated and equals-attached MCP selectors, the `--`
suffix boundary, exactly one strict empty discovery config, and byte-preserved normal startup. The
explicit-opt-in Codex live case performs dynamic initialize/model-list discovery without a thread or
token event, validates a settings-shaped launch pair, then spends exactly two bounded turns to prove
queued model/effort promotion and subsequent-turn retention on the same PID/thread. Its recorder
retains only method, selection, thread, version, timing, and numeric token-usage evidence; ordinary
suites skip the token-spending case. Captured versions, catalog rows, and counts remain live evidence
rather than production constants.

260714-ACPUI-L4 tests the frozen daemon consumer boundary and its production races. Capability
catalog cases prove token-free current-environment discovery, install fingerprint invalidation,
bounded single-flight retention, failed-refresh quarantine/recovery, and protection of a later
concurrent success. API/client/IPC/queue cases prove strict normalized advertise/set parsing,
first-byte ambiguity without blind retry, whole UTF-8 multiline submit, pending and retained
request-id idempotency, retained-known reconciliation without native resend, raw-free public
serialization, and liveness-first 404/409 classification. Opener/app cases prove complete-pair
pre-spawn validation, same-pair live reopen, changed launch conflict with actual retained truth,
fresh dead replacement, and a cross-process different-pair race with one host creation/catalog row.
Role-spawn uses that same opener and conflicts without an alternate launch path.

260714-ACPUI-L3 tests the complete same-session setter delegate graph. Shared contract and queue
coverage fail closed outside the five `SetResult` outcomes, reject contradictory effective values,
preserve FIFO set/prompt order, and prove a cancelled waiter cannot poison later commands. Claude
tests require exact session, UUID, canonical command replay, and terminal evidence; near-miss
labels, late/duplicate replay, generic native refusal, and successful dynamic Fable-shaped rows are
separate cases. Codex tests pin desired/pending/effective state, captured prompt selection epochs,
fresh-turn status gating, reversal-to-effective behavior, unrelated drift rejection, and no
reconnect. Pi tests bound mutation/state/catalog stalls, preserve requested-versus-clamped effort,
reject incoherent catalogs atomically, and keep late cancelled responses from the next request.
Scaling cases at 8 and 64 requests prove Codex/Pi cancellation reclamation without tombstone
growth. A static 17-module dependency guard covers the full shared/Claude/Codex/Pi setter graph and
rejects composer, tmux, session-command, terminal-paste, injector, and terminal-surface imports.
L4 now covers the daemon serving endpoints while retaining the same no-paste delegate graph.

260714-ACPUI-L2 adds focused and production-path coverage for settings-resolved initial
configuration. `test_harness_launch.py` proves the normalized contract, Pi's exact
provider-qualified identity, model-gated effort, honest echoes, and the complete Codex selector
grammar. Runner, opener, spawn, settings, and registry suites prove pre-discovery conflict refusal,
token-free discovery before configured vendor startup, native Claude/Codex/Pi launch channels,
roleless Codex dynamic defaults, persistent exact failure evidence, and removal of normalized
model/effort paste synthesis. Adapter tests pin Codex thread/resume configuration and Claude
effective-model mismatch classification. No launch test submits a prompt or turn.

260714-ACPUI-L1 tests dynamic, token-free catalog discovery across all three native adapters.
Claude uses the 2.1.210 initialize/bootstrap/`list_models` fixture, Codex proves paginated hidden
catalog retention without thread creation, and Pi proves provider-qualified identity plus
model-gated thinking menus without prompting. Exact fixture versions remain test evidence only.

260713-PHA-L6 tests preserve exact Claude/Codex/Pi versions only as fixture and smoke baselines,
while proving structured capability acceptance/rejection and the exact additive inbox allowlist.
They preserve R9's optional-only `adapterDeliveryState` and `adapterDeliveryDetail` compatibility,
reject unrelated extras, and do not document R10 resource performance as current behavior.

The L6 IPC regression additionally proves that a delayed reply after accepted dispatch can lose its
peer without an unhandled callback exception: only `BrokenPipeError`/`ConnectionResetError` during
write/drain/close/`wait_closed` are contained, while dispatch, identity, protocol, validation, and
unrelated failures remain loud. The accepted timeout remains ambiguous but bridge-reconcilable, and
the regression confirms the preserved vendor correlation with no retry or fallback.

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
- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: added route coverage for the complete Claude
  discovery-selector grammar and normal-launch preservation, plus the explicit-opt-in two-turn
  Codex live advertise/launch/queued-set/retention proof with sanitized evidence recording.
  Verification metadata remains pinned until closeout stamps the L5 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: added route coverage for install/auth cache
  fencing, failed-refresh quarantine, complete-pair launch, live-reopen/dead-replacement truth,
  cross-process one-process publication, exact-session first-byte ambiguity, request-id idempotency,
  retained reconciliation without resend, raw-free public responses, liveness-first status, and
  shared role-spawn conflict behavior. Verification metadata remains pinned until closeout stamps
  the L4 code commit.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: added route coverage for exact five-value
  setter truth, FIFO/cancellation behavior, Claude correlated terminal and dynamic Fable evidence,
  Codex ordered selection epochs and successful fresh-turn promotion, Pi bounded coherent
  error/clamp readback, 8/64 reclamation scaling, and the transitive 17-module no-paste guard.
  Daemon setter endpoints remain L4. Verification metadata remains pinned until closeout stamps
  the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added route coverage for the normalized
  launch contract, complete settings fixtures, native per-harness application, Codex selector
  census and roleless defaults, Pi exact identity, Claude mismatch failure, no-paste enforcement,
  and token-free failure/echo evidence. Verification metadata remains pinned until closeout stamps
  the L2 code commit.
- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: made the 2.1.210 Claude JSONL cohort the
  active fake-transport fixture authority and documented token-free dynamic catalog coverage across
  Claude, Codex, and Pi. Verification metadata remains pinned until closeout stamps the L1 commit.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: added route-level delayed-reply IPC peer-disconnect
  containment and bridge reconciliation evidence.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added route-level Codex completion correlation,
  same-row pending semantics, loud failure cases, replacement-only queue state, and fixture-only pins.
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
