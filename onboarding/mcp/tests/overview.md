# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/tests/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-07-21T11:00+02:00 |
| lastVerifiedCommitHash | `68b3205526dae210cd902eef39d93c4f4352c2d4`|
| lastVerifiedCommitDate | 2026-07-21T01:12:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

260715-FEUI-L9 adds the stable structured-conversation contract gate. The contract suite uses
hostile sibling-product matrices to pin purpose-bound cursors, exact provenance, canonical status,
evidence-backed capabilities, operation identity/rollback, authoritative queued withdrawal
recovery, attachments, metrics, and fixture non-promotion. The foundation suite separately pins
exactly two read ports, three behavior-empty owned child routers, one global registration seam,
repository-only native-helper resolution, and redacted installed-runtime fixtures. These tests do
not claim a projector, native-history implementation, control service, or renderer exists.

260718-CHATS-L1 adds the active conversation serving regression set. Four focused suites cover
the implemented slice — canonical status classification/revision discipline with full-product
orchestration parity, per-harness mapper grammars with hostile shapes, the projector engine and
store (hydration, ordering, idempotence, provenance, rehydration, tool convergence, overflow and
zipper gap mechanics), and the production routes over a REAL composition (bridge + IPC server on
a real socket, real catalog row, L0 route registration, HTTP over loopback uvicorn) proving
native identity, cursor forgery refusals, dual-cursor agreement, epoch-flip gap+close,
provenance through the real authority, orchestration parity, and absence of PTY/runner-log/
fixture production authority. The foundation pin asserts the active child's exact two-route
surface.

260718-CHATS-L2 adds the native conversation library regression set. Six focused suites cover the
implemented slice on doubled boundaries — ASGI routes with the exact O4 status ladder, cursor/key
and scope contracts, live gate demotion rules, port normalization with hostile shapes, and the
open service's idempotence/race/ownership arms — while the opt-in installed-runtime suite proves
the live Codex and Pi gates, both real end-to-end opens, and the Claude version-mismatch
fail-closed posture. The foundation pin asserts the library child's exact five-route surface and
the extended helper source set; the three runtime fixtures record observed (never enabling)
gate/open rows.

260718-CHATS-L2E adds the native control-plane regression set. The contract suite
(`test_harness_control_plane.py`, 25 tests + 35 subtests) pins the interrupt write/ack/replay-once
with exact-turn and expected-operation guards plus the successor zero-write refusal, the paged
never-bodies timeline (all sources/kinds, union completeness, eviction-floor honesty, the full
256-record budget edge, epoch-flip typed), the asset channel (schema/traversal/verification
batteries, native construction with zero-write rejection, unsupported receipt, asset-conditional
digest), the once-only withdrawal recovery with byte-preserved tombstone/`cockpit_only`, and the
strict client validators. The opt-in installed suite (`test_harness_control_plane_installed.py`)
captures the same seams live against pinned codex 0.144.5 and pi 0.80.7 and enforces the Claude
version-honesty rows; the three runtime fixtures gain redacted `control-plane/*` rows with
`enablesCapabilities: false` — evidence, never enablement.

260718-CHATS-L3 adds the authoritative control-API regression set. A shared topology
(`_control_plane.py`) runs the real bridge + IPC server on a real socket, the real submission
authority, and the L0 route composition with only the harness adapter doubled, plus the manager-
authorized `NOW`-anchored control service seeded into the `_SERVICES` memo so lease arithmetic is
time-consistent. Four focused service/route suites drive it: `test_conversation_control_operations.py`
(interrupt ledger — ack≠settlement, fingerprint idempotence with native-write counting, lost-response
reconcile, the guard battery, and both the Finding 1 content-ful and Finding 2 oversized/clipped pi
settlement regressions, each proven non-vacuous), `test_conversation_control_queue.py` (never-bodies
queue truth, the queued→dispatching race, the bounded recovery lease with an untouched frozen-clock
expiry proof, and the forgery battery), `test_conversation_control_attachments.py` (boundary-exact
limit refusals, one-use exact-receipt submit, recoverable-under-lease rebind with on-disk deletion,
timeline-driven reconcile, GET-only policy, and absent-not-zero telemetry), and
`test_conversation_control_api.py` (the seventeen routes over a real uvicorn wire with O4 mapping,
remote-peer 403, policy 405s, and the no-paste/no-substitution source scan). The opt-in
`test_conversation_control_installed.py` proves live codex/pi interrupt ack+settlement, queue truth,
withdrawal recovery, typed attachment submit, and telemetry through the registered routes plus the
Claude version-honesty gate. The foundation pin asserts the control child's exact seventeen-route
surface.

260718-CHATS-L5 adds the evidence-backed hardening regression set for the production-E2E gate. The
new `test_chats_l5_hardening.py` pins the two master hardening obligations at their origin, each
non-vacuous on stashed source: H1 (the hosted-interaction synchronizer 500 that aborted the whole
terminal-catalog sweep — now quarantined fail-loud per row, with F2 logging only on state change) and
H2 (the unknown-input provenance-validator 500 from a native re-map splitting a resolved user item's
authority triple — now pinned, with F4's identical re-map a true no-op). `test_conversation_active_service.py`
gains the projector-tier companions (the H2 model-valid re-map and the three F1 twin-suppression
tests, driving the real poll path), and the opt-in `test_conversation_control_installed.py` gains the
F1 installed regression proving a settled live codex turn projects EXACTLY once on the re-read
conversation page (`2 != 1` on stashed `projector.py`). The 10,000-item DOM/interaction baseline + axe
tripwire (L4.4) lands in the dashboard test tree (`renderer.test.tsx`), not here.

260715-FEUI-L5 adds the first end-to-end authoritative submit/withdraw regression matrix. The new
focused authority suite and expanded common/API/native-adapter suites prove one epoch-bound
prompt/setter timeline, atomic queued-withdraw versus dispatch, exact full-ref completion,
completion-before-receipt dominance, no native queue/steer fallback, bounded privacy-aware retention,
and browser-visible status semantics. The backend blockers found during review rounds 1–5 are closed;
round 6 is canonical PASS.

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

## FEUI-L9R Runtime-Truth Regression Gate

The candidate expands serving coverage across four exact boundaries: client/build fingerprint and
HTML revalidation; raw-event record realignment and invalid/non-object cursor progression; owned
tmux client environment under contaminated launcher state; and omission of fictitious pre-session
adapter control. Integration coverage skips only when tmux itself is absent.

## MX-FIX-1 Atomic Folded-State Stream Gate

`test_serving.py` now forces both formerly lost state paths. One case publishes while the initial
snapshot generator is suspended but already subscribed and requires the exact next delta. One case
registers before failed-prime recovery, requires one full build-decorated snapshot, proves the
identical state is not duplicated, and then requires an ordinary later delta. A third case cancels a
waiting stream and proves immediate subscriber removal. These are synchronization-driven assertions,
not sleep-based race probabilities.

## MX-FIX-4 Route-Index And Carryover Authority Gate

`test_route_index.py` pins the production census boundary across ignored and generated paths,
tracked/untracked identity, symlinks without target following, sparse checkouts, index/worktree
deletions, gitlinks, all eight ambient Git repository selectors, non-UTF-8 names, and typed Git,
timeout, OS, and `lstat` failures with preserved causes. Regular, linked-worktree, and selector-
contaminated generation must produce identical bytes and a zero-write second pass.

`test_carryover.py` pins official-memory write authority before full apply. JSON and Markdown
settings with missing, invalid, unsupported, reset-to-empty, blank-member, or otherwise
semantically empty path rules must refuse with exact zero mutation. Positive retention,
repopulation, mode/layout selection, root fallback, and official-over-source cases prove the raw
preflight agrees with the typed settings parser rather than creating a second settings language.
`test_worktree_support.py` provisions explicit supported storage authority in initialized-memory
fixtures, while `conftest.py` imports the production selector inventory so tests cannot drift from
the Git boundary they exercise.

## MX-FIX-5 Generated Bundle Whitespace Policy Gate

`test_sync_dashboard.py::GeneratedDashboardWhitespacePolicyTests` exercises the repository's real
Git attribute in an isolated temporary repository. It stages a direct shipped dashboard JavaScript
asset whose tab-only line is semantic template-literal content beside an authored
`dashboard/src/main.tsx` file with ordinary trailing spaces. The actual
`git diff --cached --check` result must omit the generated asset and retain the exact authored-source
diagnostic, so the exception cannot silently become a source-wide relaxation.

Vite owns and recreates the generated `dashboard/dist` bytes; `scripts/sync-dashboard.py` copies and
hashes those bytes without transformation. Generic end-of-line normalization is rejected because
the generated tab is CodeMirror Python-completion indentation and removing it changes the runtime
string. The root policy therefore targets only direct shipped
`mcp/src/agents_remember/package_data/dashboard/assets/*.js` and disables only `blank-at-eol`.
Generated CSS, nested or unrelated JavaScript, authored source/test/configuration,
`blank-at-eof`, and `space-before-tab` remain strict. Two clean build/sync passes produced identical
dist/package bytes and the same source/package fingerprint, confirming the exception survives
content-hash regeneration without manual asset edits.

## Hot Path Summary

For generated dashboard whitespace policy, begin at root `.gitattributes` for the exact direct-asset
scope, then `test_sync_dashboard.py::GeneratedDashboardWhitespacePolicyTests` for the real-Git
generated-positive/authored-negative regression. Use `dashboard/package.json` and
`dashboard/vite.config.ts` for Vite ownership, and `scripts/sync-dashboard.py` for raw copy/digest
parity. Do not route this seam through generated asset file cards or a generic normalizer.

For route-index/carryover authority changes, begin with `test_route_index.py` for the frozen census
and byte-convergence matrix, then `test_carryover.py` for full-apply zero-mutation refusals and
parser-equivalent positive controls. Use `test_worktree_support.py` for closeout caller wiring.

For folded-state transport changes, begin at `test_serving.py::StreamEventsTests`: the MX-FIX-1
cases pin atomic activation, first-recovery snapshot semantics, later-delta continuity, and
close/cancellation cleanup against the production `Projector` and `stream_events` seam.

260715-FEUI-L9 centers `test_conversation_contracts.py` for semantic authority and
`test_conversation_foundation.py` for package/router/helper/fixture topology. The three
`fixtures/conversation_runtime/*.json` files are allow-listed installed observations with
`enablesCapabilities:false`; exact versions and observed counts are evidence, never maintained
feature declarations. Helper protocol behavior is also covered in its own Node test package.

260718-CHATS-L1 centers four focused suites: `test_conversation_active_status.py` (canonical
classification, revision discipline, full-product orchestration parity),
`test_conversation_active_projectors.py` (per-harness mapper identity/blocks/tools/provenance),
`test_conversation_active_service.py` (engine hydration/ordering/idempotence plus the F1/F2/F3
fix pins), and `test_conversation_active_api.py` (production routes over a real socket, incl.
the live epoch-flip gap and the no-PTY source scan). The foundation pin asserts the active
child's exact two routes; fixture rows stay evidence-not-enablement.

260718-CHATS-L2 centers six focused suites: `test_conversation_library_api.py` (real-ASGI routes
and the O4 status ladder), `test_conversation_library_cursor.py` (signed token and scope
contracts), `test_conversation_library_gates.py` (capability demotion rules),
`test_conversation_library_ports.py` (hostile normalization), `test_conversation_library_open.py`
(idempotent exact open arms), and `test_conversation_library_installed.py` (opt-in live gates and
both real opens). The foundation pin asserts the library child's exact five routes and the
four-file helper source set; fixture rows stay evidence-not-enablement.

260718-CHATS-L3 centers four focused suites plus a shared topology and an installed proof:
`_control_plane.py` (the real bridge/IPC/authority/L0 seam with only the harness adapter doubled and
the `NOW`-anchored control service), `test_conversation_control_operations.py` (interrupt ledger,
Finding 1/Finding 2 pi settlement regressions), `test_conversation_control_queue.py` (never-bodies
queue truth, withdrawal race, bounded recovery lease + frozen-clock expiry, forgery battery),
`test_conversation_control_attachments.py` (limit refusals, one-use submit, recoverable-lease rebind,
policy/telemetry), and `test_conversation_control_api.py` (the seventeen routes over a real uvicorn
wire, O4 mapping, no-paste source scan), with `test_conversation_control_installed.py` the opt-in
version-locked live proof. The foundation pin asserts the control child's exact seventeen routes;
fixture rows stay evidence-not-enablement.

260718-CHATS-L0 adds `test_conversation_runtime_composition.py` and
`test_conversation_authorization.py` for the runtime composition repair: single install-once
binding at both composition seams, duplicate/missing/foreign/missing-member fail-closed shapes,
per-app child isolation over real HTTP, no import-time singleton, no production identity-injection
or fixture/PTY/browser-identity reliance, server-resolved local-operator identity, loopback-only
resolution, and cross-principal rejection in both directions through an injected seam double.

260718-CHATS-L0E adds `test_harness_control_evidence.py` for the native evidence and resume
substrate: per-harness reserved-key round-trips with the no-leak guarantee across `snapshot.raw`,
projected `control_raw`, and subscriber snapshots; unknown-vendor pass-through; buffer bounds and
clip visibility at two sizes; native-page continuation without overlap/gap, null-terminated, with
typed cross-domain rejection and epoch-mismatch detection; the provenance matrix through the sole
queue delegation; and the codex resume channel end-to-end with pre-spawn refusals.
`test_harness_control_evidence_installed.py` captures the same seam against installed runtimes
(opt-in, version-locked) into redacted `substrate-evidence/*` fixture rows, keeping the
version-mismatched Claude row honestly `not-exercised` and `enablesCapabilities` false everywhere.

260718-CHATS-L3E extends `test_harness_control_evidence.py` with the evidence-truncation settlement
coverage: `ClipHelperTests` gains three byte-level clip terminal-identity preservation tests (a
clipped pi `message_end` keeps only `type` + `message.stopReason`; a clipped codex `turn/completed`
keeps only `turn.id` + `turn.status`; absent identity is never invented) plus a giant-scalar
drop-whole regression with a 256/257 boundary check, and the new
`EvidenceTruncationSettlementIpcTests` drives oversized (>32 KiB) production pi/codex terminal frames
end-to-end through the real bridge clip and the real `read_control_evidence` IPC surface, asserting
the preserved enums survive to scan helpers that mirror L3's `_pi_stop_reason` /
`_codex_terminal_outcome` reads verbatim (the in-leaf acceptance proxy for `probe_l3_delta.py`).

260718-CHATS-L2E centers `test_harness_control_plane.py` for the control-plane contract suite:
the interrupt batteries (bridge epoch guard, codex exact-turn, pi expected-operation guard,
successor zero-write refusal, content-less `message_end` honesty), the timeline batteries
(all-sources/kinds union, eviction floor, the 256-record budget edge), the asset batteries
(schema/traversal/verification/construction/digest/unsupported), the recovery battery, and the
client validation battery. `test_harness_control_plane_installed.py` captures the same seams live
against pinned codex 0.144.5 and pi 0.80.7 (opt-in, version-locked) into redacted
`control-plane/*` fixture rows, with the Claude version-honesty test keeping those rows
`not-exercised` and `enablesCapabilities` false everywhere.

260715-FEUI-L5 centers `test_harness_submission_authority.py`: slow-adapter responsiveness,
dispatch/withdraw races, early terminal completion, full-ref id reuse, ordering, idempotency/source-
payload conflicts, certified pre-dispatch retry, impossible safe retry after possible bytes, epoch
mismatch, privacy, and retention. `test_harness_control.py` extends the same timeline across IPC,
outer response loss, durable sources, reconcile, and raw-free projection. API tests pin 64-id
status/withdraw and typed 409/503 mapping. Claude/Codex/Pi suites each prove their guarded write and
exact completion semantics; Codex/Pi live smokes remain opt-in installation evidence, not generic
authority.

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

## Invariants And Boundaries

- Authority races use explicit synchronization at the preflight/claim/write seams; sleep timing is
  not accepted as proof of withdrawal linearization.
- Every completion test carries epoch + sequence + id + kind. Bare-id/FIFO completion must fail to
  release a successor.
- Safe retry tests distinguish the exact certified pre-dispatch error from first-byte ambiguity and
  assert native submit call counts to catch duplication.
- Bounds may trim terminal history but never live, active, or unknown work; public fixtures remain
  raw-free and terminal records do not retain full prompt text.
- Live smokes are credential-safe, explicit opt-in evidence for installed harnesses. Deterministic
  protocol truth remains in fake/stdio tests.
- Structured-conversation tests preserve separate active/library cursors and ports, exact
  authorization/identity/generation binding, and fail closed on contradictory state products.
- Runtime fixtures and locked helper packages are evidence surfaces only; neither enables history
  or control capability without a production-seam pass.
- Folded-state race regressions force ordering through explicit generator/task boundaries; timing
  sleeps alone are not accepted as proof of snapshot/subscription convergence.
- First recovery is exactly one full snapshot with boot identity, identical state is silent, later
  content uses the normal delta grammar, and every closed/cancelled consumer releases its queue.
- Route-index tests compare complete generated bytes and require a zero-write second pass; source
  counts and covered-file membership must come from the same frozen Git/path-rule snapshot.
- Carryover authority refusals assert official HEAD, status, non-Git bytes, source bytes, and
  route-index absence so parser-default authority cannot mutate any official-memory surface.
- Generated dashboard whitespace coverage must exercise Git's real attribute resolution. Only direct
  shipped `assets/*.js` may suppress `blank-at-eol`; authored source and generated near misses remain
  strict, and semantic JavaScript string bytes must remain identical through sync.

## Docs References

The resolved Domain Documentation registry has no entries. This route uses direct repository code,
fixtures, and tests and makes no external behavioral claim from dependency names alone.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this test-route update. | — | — |

## Cross-Repo References

The structured-conversation contract and helper/fixture tests execute entirely inside
`agents-remember`; no neighboring repository governs them.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Structured-conversation hostile matrices cover cursor, provenance, status, capability, operation, withdrawal, attachment, metric, and fixture authority. | L208-L1185 | [test_conversation_contracts.py](agents-remember/mcp/tests/test_conversation_contracts.py) |
| Foundation coverage pins two ports, child ownership (the active child's exact two L1 routes, the library child's exact five L2 routes, and the control child's exact seventeen L3 routes), one registration seam, exact helper resolution/source set, and raw-free non-enabling fixtures. | L21-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| Active serving coverage pins canonical status/parity, per-harness mapper grammars, engine/store mechanics, and the real-socket production routes with the no-PTY source scan. | L362-L865 | [test_conversation_active_api.py](agents-remember/mcp/tests/test_conversation_active_api.py) |
| Library coverage pins the ASGI status ladder, cursor/scope contracts, gate demotion, hostile port normalization, open idempotence/race/ownership, and the opt-in live gates and real opens. | L1-L9 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |
| Control coverage pins the interrupt ledger (ack≠settlement, idempotence, Finding 1/2 pi settlement), never-bodies queue truth with cockpit-only withdrawal recovery, the typed attachment lifecycle with on-disk spool proofs, read-only policy, evidence-bound telemetry, and the seventeen routes over a real wire — all over the shared `_control_plane.py` topology. | L1-L381 | [test_conversation_control_api.py](agents-remember/mcp/tests/test_conversation_control_api.py) |
| Composition contract coverage pins install-once, fail-closed binding shapes, per-app isolation, no singleton, and no injected identity or fixture/PTY reliance. | L106-L260 | [test_conversation_runtime_composition.py](agents-remember/mcp/tests/test_conversation_runtime_composition.py) |
| Authorization contract coverage pins local-operator identity, loopback-only resolution, no identity channel, ignored browser claims, and cross-principal rejection. | L109-L282 | [test_conversation_authorization.py](agents-remember/mcp/tests/test_conversation_authorization.py) |
| Evidence contract coverage pins per-harness round-trips, no-leak, bounds, continuation, cross-domain/epoch rejection, provenance, and the resume channel. | L268-L1470 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| Installed-runtime coverage captures the redacted `substrate-evidence/*` fixture rows through the production seam with version-locked honesty. | L115-L362 | [test_harness_control_evidence_installed.py](agents-remember/mcp/tests/test_harness_control_evidence_installed.py) |
| Control-plane contract coverage pins the interrupt guards/replay, the paged never-bodies timeline with the 256-record budget edge, the asset schema/traversal/verification/construction batteries, the once-only recovery, and the strict client validators. | L252-L1575 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |
| Installed-runtime control-plane coverage captures the redacted `control-plane/*` fixture rows through the production seam and enforces the Claude version-honesty posture. | L126-L384 | [test_harness_control_plane_installed.py](agents-remember/mcp/tests/test_harness_control_plane_installed.py) |
| Focused authority concurrency, completion, identity, retention, epoch, and privacy matrix. | L1-L687 | [test_harness_submission_authority.py](agents-remember/mcp/tests/test_harness_submission_authority.py) |
| Common timeline, IPC/response loss, idempotency, reconcile, status, and withdraw coverage. | L1-L1180 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Public API epoch/conflict/certificate/privacy/status matrix. | L1-L700 | [test_serving_harness_control_api.py](agents-remember/mcp/tests/test_serving_harness_control_api.py) |
| Native adapter exact-operation coverage is split by harness. | L1-L1 | [Claude tests](agents-remember/mcp/tests/test_harness_control_claude.py); [Codex tests](agents-remember/mcp/tests/test_codex_app_server_adapter.py); [Pi tests](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Folded-state stream regressions force the handoff mutation, failed-prime snapshot/non-duplication/later delta, and cancellation cleanup. | L395-L457 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| Route-index regressions cover ignored/generated exclusion, symlink/sparse/gitlink/non-UTF-8 identity, ambient selectors, typed failures, and repeat convergence. | L199-L911 | [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |
| Carryover full-apply regressions compare raw JSON/Markdown authority with typed parser semantics and prove exact zero mutation for every refusal. | L374-L1268 | [test_carryover.py](agents-remember/mcp/tests/test_carryover.py) |
| Worktree fixtures install explicit supported external-memory storage settings so closeout tests exercise real write authority. | L224-L252 | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| The generated-whitespace test copies the real attribute into a temp repository and proves the direct generated JavaScript allowance together with strict authored TSX behavior. | L216-L247 | [test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The root attribute narrows the exception to direct shipped dashboard JavaScript assets and only the `blank-at-eol` check. | L1-L3 | [.gitattributes](agents-remember/.gitattributes) |
| The sync helper copies and compares raw dist/package bytes; it does not introduce or normalize emitted whitespace. | L59-L68; L133-L172 | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |
| The production build runs Vite and recreates `dashboard/dist`, making Vite the physical-byte owner. | package L6-L10; config L61-L67 | [dashboard/package.json](agents-remember/dashboard/package.json); [dashboard/vite.config.ts](agents-remember/dashboard/vite.config.ts) |

### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Update History

- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: added the evidence-backed hardening regression
  narrative — the new `test_chats_l5_hardening.py` (H1 catalog-sweep quarantine + F2, H2
  authority-pin + F4), the projector-tier H2/F1 companions in `test_conversation_active_service.py`,
  and the F1 installed regression in `test_conversation_control_installed.py` — and noted the 10k
  renderer DOM/interaction baseline lands in the dashboard test tree, not here. New file card
  `test_chats_l5_hardening.py.md` registered in the route index. Verification metadata stays pinned
  until L5 closeout stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: added the authoritative control-API regression
  set — the shared `_control_plane.py` topology (real bridge/IPC/authority/L0 seam, `NOW`-anchored
  service), the four focused suites (operations incl. Finding 1/2 pi settlement regressions; queue
  incl. the frozen-clock expiry proof; attachments incl. on-disk spool deletion; the seventeen-route
  API over a real wire), and the opt-in installed proof — plus the seventeen-route foundation pin, a
  control coverage reference row, and the corrected "control empty" claim. Verification metadata stays
  pinned until L3 closeout stamps the candidate commit.
- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: added the evidence-truncation settlement
  coverage to the `test_harness_control_evidence.py` description — the `ClipHelperTests` byte-level
  terminal-identity preservation tests plus the giant-scalar drop-whole (256/257 boundary)
  regression, and the new `EvidenceTruncationSettlementIpcTests` oversized-frame end-to-end
  regressions mirroring L3's `_pi_stop_reason` / `_codex_terminal_outcome` reads. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: added the native control-plane regression
  set — the contract suite `test_harness_control_plane.py` (interrupt/timeline/asset/recovery and
  client-validation batteries, 25 tests + 35 subtests), the opt-in version-locked installed
  capture `test_harness_control_plane_installed.py`, and the redacted `control-plane/*` fixture
  rows with `enablesCapabilities: false`. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  library regression-set content with the L1 active regression-set content after the master
  memory branch advanced — both suite families, the merged foundation-pin coverage (active two
  routes + library five routes; control empty), and both reference rows survive. Verification
  metadata remains pinned until L1 closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: added the active conversation serving
  regression set — four focused suites (canonical status/parity, mapper grammars, engine/store
  with the F1/F2/F3 fix pins, and the real-socket production routes proving identity, cursor
  refusals, epoch-flip gap+close, provenance, parity, and no-PTY authority) plus the foundation
  pin's exact two-route active-child assertion. Verification metadata remains pinned until
  closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: added the native conversation library
  regression set — six focused suites over doubled boundaries (ASGI status ladder, cursor/scope,
  gates, ports, open arms) plus the opt-in installed-runtime suite proving the live Codex/Pi
  gates, both real end-to-end opens, and the Claude version-mismatch posture — the foundation
  pin's exact five-route library assertion and helper source set, and the observed
  evidence-not-enablement fixture rows. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: added the native evidence contract suite and
  the opt-in installed-runtime capture — per-harness round-trips with no-leak proofs, buffer and
  continuation bounds, cross-domain/epoch typed rejection, the provenance matrix, the codex resume
  channel, and the redacted version-locked `substrate-evidence/*` fixture rows. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: added the conversation runtime composition
  and authorization contract suites — install-once/fail-closed composition shapes, per-app
  isolation, no-singleton and no-injected-identity proofs, loopback-only local-operator resolution,
  and cross-principal rejection — plus the one-line `coordination_root` call-shape follows in the
  two harness-control suites. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 added the real-Git generated-positive/authored-negative
  whitespace regression, the direct shipped-JavaScript `blank-at-eol` boundary, Vite/raw-sync byte
  ownership, the rejected-normalization rationale, retained near-miss checks, and the two-build
  byte/fingerprint determinism proof. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the deterministic Git/path-rule census matrix,
  regular/linked/contaminated byte-convergence proof, typed failure coverage, and full-apply
  JSON/Markdown carryover-authority refusal/retention matrix with exact zero-mutation assertions.
- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: added route-level coverage for deterministic
  snapshot/subscription handoff, first-recovery full snapshot with build identity, identical-state
  silence, later named delta, and explicit close/cancellation subscriber cleanup. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the build/static, raw-event, tmux-environment, and
  narrow harness-discovery regression matrix. Verification metadata remains pinned pending
  candidate closeout.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the hostile normalized-contract
  matrix, exact two-port/three-router topology, repository-only helper resolution, and redacted
  non-enabling runtime fixtures. Added current governing/reference structure; verification remains
  pinned to committed source truth until closeout stamps the candidate.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: added the authoritative submit/withdraw
  adversarial matrix, exact-ref and early-completion proofs, safe-retry/first-byte split, raw-free
  status/API bounds, native no-queue guarded-write semantics, and retention/privacy invariants after
  canonical review round 6 PASS.
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
