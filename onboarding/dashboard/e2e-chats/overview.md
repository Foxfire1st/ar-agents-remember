# dashboard/e2e-chats/ — Durable Chats End-to-End Suite Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/e2e-chats/`                           |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-21T11:30+02:00                           |
| lastVerifiedCommitHash |                                                  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |                                                  2026-07-21T11:31:07+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[agents-remember root overview](../../overview.md)

Discoverability sibling: the cockpit frontend overview
[dashboard/src overview](../src/overview.md) carries a pointer to this sibling suite; `e2e-chats/`
lives beside `dashboard/src/` (not under it), so the root overview is its nearest governing
ancestor.

## Purpose

The durable, opt-in **Chats end-to-end suite** promoted in half-time feedback FB5
(260718-CHATS-L5F R7). Unlike `e2e-production/` (which route-mocks the backend to test the shipped
bundle in isolation, and is itself undocumented in memory), this suite drives the **real composed
app against the real installed harnesses** — codex 0.144.5, claude 2.1.216, pi 0.80.7 — through the
full lifecycle: open → submit → full turn → set-model/effort with **acceptance validation** →
interrupt → End. It is the regression net that would have caught, before merge, every half-time
functional defect (the codex startup flood, the claude frame flood, the opus[1m] refused pair, the
version-mismatch demotion, the cried-wolf launch strip). Its assertions are sharp, not smoke: each
one is calibrated so that one of the developer's three acceptance screenshots fails it.

### Opt-in gate — a green no-op by default

`support/gate.ts::gateChatsE2E()` registers a `test.beforeEach` that `test.skip`s every spec unless
`AR_RUN_CHATS_E2E=1`. Without that env the whole run is a green "all skipped" no-op: the daemon
never boots and no real harness is spawned, so the suite is safe to keep in the tree and out of the
default gate (it spawns real, authenticated harnesses and is slow — `workers: 1`, `timeout: 180s`).
Knobs: `AR_CHATS_E2E_PYTHON` (a python with the agents-remember mcp package installed, default
`python3`), `AR_CHATS_E2E_HARNESSES` (comma list to scope the composed drive, default
`codex,claude,pi`), `AR_CHATS_E2E_SKIP_BUILD=1` (reuse the already-synced `package_data` bundle).

### Isolation pattern — the collision truth (durable)

`support/daemon.ts::bootDaemon()` boots the **same** `agents_remember.cli dashboard` process the
product ships, but fully isolated so the developer's live `:8871` daemon is never touched:

- **Free port** — `freePort()` binds `:0` and hands the OS-chosen port to the daemon; never `8871`.
- **Scratch coordination root** — a per-run `mkdtemp` base holds the coordination root, so the
  daemon's `runtime/harness-control` control socket lands under the scratch root, never in the
  shared `ar-coordination/runtime/harness-control`. (The settings JSON must live OUTSIDE the
  coordination root — the daemon rejects a settings file inside it — so it is written alongside.)
- **Isolated `CODEX_HOME` by construction (the L5P re-verification lesson, baked in)** — a scratch
  `codex-home` is created and the developer's real `~/.codex/auth.json` is **symlinked** in so codex
  still authenticates for ordinary turns; nothing else is copied, so no MCP-server fleet from the
  developer's config re-launches, and a scratch codex chat's session rollouts never land in the
  developer's live `~/.codex`. An explicitly provided `CODEX_HOME` is respected. **F7 (recorded
  follow-on):** only `CODEX_HOME` is isolated — scratch claude/pi sessions still run against the
  developer's real `CLAUDE_CONFIG_DIR` / pi home; isolating those with the same symlinked-auth
  pattern is the named hardening follow-on.
- **Daemon log capture** — the daemon's stdout/stderr are captured to `<baseDir>/daemon.log` so an
  E2E failure surfaces the daemon-side error (composition tracebacks, harness runner exits) instead
  of losing it into Playwright's piped stdout.

`buildAndSyncBundle()` builds the dashboard and runs `scripts/sync-dashboard.py` so the daemon
serves the freshly-synced worktree bundle; `waitHealthy()` polls `/api/state` for up to 60s.
`support/global-setup.ts` boots the daemon once and publishes `AR_CHATS_E2E_BASE_URL`;
`support/global-teardown.ts` stops it (SIGTERM then SIGKILL after 5s).

## Hot Path Summary

Start at `support/gate.ts` (the opt-in skip) and `support/daemon.ts::bootDaemon` (the isolated real
daemon: free port + scratch coordination root + by-construction `CODEX_HOME`). The shared drivers
and the sharp assertions live in `support/drive.ts` (`openChat` with its cried-wolf retry-recovery,
`driveTurn`, `interruptTurn`, `assertNoUnknownVendorRows`, `assertAcceptanceValidated`,
`assertNoVersionMismatchDemotion`, `assertNoProjectionAlarm`, `assertWorkingStateSeenDuringTurn`,
`assertSingleTurnResultInvariants`, `sampleHeapBytes`). The four `*.chats.spec.ts` drive per-harness
and composed scenarios; `playwright.chats-e2e.config.ts` (serial, `testMatch` `*.chats.spec.ts`)
wires the global setup/teardown. `README.md` is the runbook.

## Spec Manifest

| spec | scenario | composed assertions (support/drive.ts) |
|---|---|---|
| `codex.chats.spec.ts` | open → working-state → turn; second turn; interrupt | zero unknown-vendor rows, no cried-wolf strip, working state visible, single turn-result |
| `claude.chats.spec.ts` | ordinary session; set-model via control | acceptance validated (no refused pair), no version-mismatch demotion, zero flood |
| `pi.chats.spec.ts` | open → turn | zero flood, single turn-result, no failed-launch banner |
| `composed.chats.spec.ts` | every installed harness open/turn/End; then 5× open→turn→End | acceptance validated + zero flood per harness; JS-heap does not balloon across cycles (R5 daemon-side release rides here) |

## Assertion → Guarded Defect

Each assertion is sharp enough that one screenshot fails it (targeting stable `data-testid`s on the
composed surface):

| Assertion | Screenshot / requirement it guards |
|---|---|
| `assertNoUnknownVendorRows` | codex startup flood (image.png, R1) + claude frame flood (image3, R3) |
| `assertAcceptanceValidated` | opus[1m] "refused pair — requested provenance" (image3, R2) |
| `assertNoVersionMismatchDemotion` | claude wholesale "unverified" version demotion (image3, R3/R4) |
| `assertNoProjectionAlarm` | the cried-wolf codex launch red strip (R10 / audit V13) |
| `assertWorkingStateSeenDuringTurn` | a streaming turn shown settled-green (R9 / audit V5) |
| `assertSingleTurnResultInvariants` | a settled turn double-projecting / a flood row masquerading as a settlement |
| composed heap sampling (`sampleHeapBytes`) | per-session structure release across open/End cycles (R5) |

## Live State At Handoff (honest, durable)

The suite is durable and green-no-op-safe, but only the codex lane is proven fully green
end-to-end; the other lanes surfaced fidelity gaps and one real product gap that are named
follow-ons, not binding defects:

- **codex — proven green (4/4, reproduced independently by the reviewer):** fresh open with zero
  unknown-vendor rows and no cried-wolf strip (R1, R10), a live working state during a streaming
  turn (R9 surfaces for codex), flood-free second turn, clean interrupt.
- **claude — red at the launch dialog (F6, pre-assertion, NOT a binding defect):** `launch-model-list`
  never becomes visible in headless because the dialog's claude catalog probe is slow/flaky there;
  the run fails before reaching the R2/R3/R4 assertions. The claude binding proofs stand at daemon
  authority (opening claude via the API bypasses the dialog and validates). Fix: harden the
  catalog-probe wait or drive the claude open via the API as the dialog fallback.
- **pi — surfaced a real pi product gap (F3, a required follow-on):** stock pi 0.80.7 renders
  `pi:turn_start` / `pi:turn_end` rpc events the pi mapper never learned as unknown-vendor rows,
  plus a live turn that settled FAILED with no assistant message. This is outside the L5F letters
  (R1=codex, R3=claude; pi was the "confirmed unexposed" harness) — exactly the class the suite was
  built to catch — and needs a follow-on pi leaf (capture the pi rpc specimens, teach/drop
  turn_start/turn_end, diagnose the failed settlement).
- **composed — not yet run green** (would fail on the same claude/pi gaps); the codex-only
  heap-cycle was not separately driven at handoff.

### Recorded suite deductions (E2E sharpness follow-ons)

- **F2** — `support/drive.ts::openChat` recovers a stuck cried-wolf strip by clicking its own "retry
  projection" control across a bounded window. This keeps the codex lane green on a slow bridge
  startup, but it also MASKS the exact cried-wolf class R10 targets: a regression re-introducing the
  strip on any path still passes whenever the driver's own retry recovers it. Follow-on: track and
  surface the recovery clicks (return value / test annotation) and assert zero recoveries once the
  epoch-resolve product hardening lands. The retry is a driver workaround for a pre-existing,
  R10-adjacent frontend connect-race on the epoch-resolve/repage path (`ChatsStageBody.tsx`, L4
  work), which L5F did not touch.
- **F4** — `driveTurn` / `interruptTurn` count every `conversation-turn-result` kind for the
  single-settlement invariant, so a notice/flood row can masquerade as a settlement (this mislabeled
  the pi failure as a "test-expectation gap"). Follow-on: narrow the counter to
  `[data-kind="turn-result"]` and keep `assertNoUnknownVendorRows` separate.
- **F9** — `support/global-setup.ts` writes a fixed `/tmp/ar-chats-e2e-state.json` STATE_FILE that
  teardown never reads (teardown uses a same-process handle) and that collides across concurrent
  runs. Follow-on: drop it or make it per-run and actually consume it.

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: created this governing route overview for the
  new durable, opt-in Chats E2E tree (R7/FB5). Documented the tree as a single governing overview
  rather than per-file sidecars because the dashboard side has NO existing e2e onboarding precedent
  (`e2e-production/` is itself undocumented in memory). Captured the opt-in `AR_RUN_CHATS_E2E` gate,
  the isolated-real-daemon pattern (free port + scratch coordination root + by-construction
  `CODEX_HOME` — the L5P collision truth), the four-spec manifest, the assertion→screenshot map, and
  the honest live-state at handoff (codex green; claude F6; pi F3; F2/F4/F7/F9 follow-ons).
  Verification is blank because the new source tree is uncommitted; closeout owns its first source
  stamp, and `route_index_refresh` should be run so this overview gains its generated
  `overview.index.json`.
