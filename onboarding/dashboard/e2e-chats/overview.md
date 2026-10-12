# dashboard/e2e-chats/ — Durable Chats End-to-End Suite Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/e2e-chats/`                           |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

This directory holds the durable, opt-in Chats end-to-end suite. It boots a real dashboard daemon and drives installed codex, claude and pi harnesses through the composed browser surface. Its standing regression intent is to catch startup and frame floods, refused model pairs, version-mismatch demotion, launch projection alarms, missing working-state feedback, duplicate settlement and growth across repeated open/End cycles. The source describes this intent as FB5/R7; the implemented checks and their limits are described below.

The suite lives beside `dashboard/src/`, so the root overview is its nearest governing ancestor. The cockpit frontend overview's sibling pointer is a discoverability relationship, not suite ownership.

## Hot Path Summary

Start at `dashboard/playwright.chats-e2e.config.ts`: it requires a Dagger test attestation before configuring the suite. `support/gate.ts` skips individual tests unless `AR_RUN_CHATS_E2E=1`; global setup independently checks the same switch before booting. `support/daemon.ts` builds and syncs the bundle, chooses a free port, creates scratch coordination state and prepares `CODEX_HOME`. `support/drive.ts` owns launch, turn, interrupt, End and browser assertions. The four `*.chats.spec.ts` files compose those helpers into harness-specific and cross-harness scenarios. `README.md` describes the original run procedure, but its direct host command does not describe the current Dagger admission requirement.

## Construction

### Admission and configuration

The config selects `*.chats.spec.ts` in `e2e-chats`, Chromium, one worker, `fullyParallel: false`, a 180-second test timeout and a 30-second expectation timeout. It wires global setup and teardown. Before any opt-in skip can apply, the config calls `requireDaggerTestEnvironment`: the environment nonce must be 32 lowercase hexadecimal characters and exactly match the attestation file at `/tmp/ar-quality/dagger-test-attestation`.

Within an admitted run, leaving `AR_RUN_CHATS_E2E` unset skips the tests and makes setup and teardown return without booting a daemon. The opt-in switch therefore prevents real harness work; it does not make an arbitrary host invocation a green no-op.

`AR_CHATS_E2E_PYTHON` selects the daemon/build-sync Python interpreter, defaulting to `python3`. `AR_CHATS_E2E_SKIP_BUILD=1` reuses the already-synced bundle. `AR_CHATS_E2E_HARNESSES` scopes only the composed specs, defaulting to `codex,claude,pi`; the individual harness specs remain independently selected by the config.

### Daemon and isolation

The daemon helper runs `agents_remember.cli dashboard` with loopback host and an OS-selected free port. It creates a per-run temporary base containing a scratch coordination directory and a settings JSON alongside that directory. The settings placement satisfies the runtime predicate rejecting MCP settings inside the coordination root. This construction avoids targeting the developer's live daemon port or shared coordination state.

Unless the caller supplies `CODEX_HOME`, the helper creates a scratch `codex-home` and attempts to symlink the existing `~/.codex/auth.json` into it. It copies no other Codex configuration. An explicitly supplied `CODEX_HOME` is used unchanged, so its isolation depends on the caller. The child inherits the remaining environment; this helper does not construct isolated Claude or pi homes. F7's recorded hardening intent—isolating those homes while retaining authentication—remains distinct from the implemented isolation.

Unless build skipping is requested, the helper runs the dashboard build and, when `scripts/sync-dashboard.py` exists, runs that sync script. It captures daemon stdout/stderr in the temporary base's `daemon.log` and polls `/api/state` for up to 60 seconds. Setup publishes `AR_CHATS_E2E_BASE_URL` and a same-process stop handle. Teardown invokes that handle; stopping sends SIGTERM, then SIGKILL after five seconds if the child has not exited.

Setup also writes a fixed `ar-chats-e2e-state.json` under the OS temporary directory. Teardown does not read that file. F9's recorded intent to remove it or make it per-run and consumed remains unresolved in these owners; concurrent runs share the file path.

### Scenarios

| Spec | Implemented scenario |
| --- | --- |
| `codex.chats.spec.ts` | Four cases: clean open and turn; visible working state during a longer prompt; two ordinary turns; interrupt. Each ends the chat. |
| `claude.chats.spec.ts` | Ordinary launch and turn with flood, version-demotion and launch-banner checks; a separate model-control case whose selection and apply actions are conditional on controls being present. |
| `pi.chats.spec.ts` | Clean open, one turn, allowed result-kind checks, no failed-launch banner, then End. |
| `composed.chats.spec.ts` | Open/turn/End for each configured harness; separately, warm-up and five open/turn/End cycles using only the first configured harness. |

Launch selects the first selectable model in the installed catalog and an effort option when one exists. It does not pin the historical version labels codex 0.144.5, claude 2.1.216 or pi 0.80.7 as runtime admission predicates. Those labels survive in source comments as historical context.

## Invariants and Verification Boundaries

### Assertions and standing regression intent

| Helper/check | Implemented predicate and intended guard |
| --- | --- |
| `assertNoUnknownVendorRows` | Requires zero unknown-vendor run, member, evidence and unknown-vendor result rows; intended to guard codex startup and Claude frame floods (R1/R3). |
| `assertAcceptanceValidated` | Requires absence of refused-pair and failed-launch banners; intended to guard the opus[1m] refusal class (R2). It does not positively inspect an acceptance authority result. |
| `assertNoVersionMismatchDemotion` | Requires absence of two version-mismatch text patterns; intended to guard wholesale demotion (R3/R4). |
| `assertNoProjectionAlarm` | Requires absence of reconnect rows in `projection-failed` or `failed` phase; intended to guard the cried-wolf launch strip (R10/V13). |
| `assertWorkingStateSeenDuringTurn` | Requires a working-line or chat-activity locator to be visible within 30 seconds after sending; intended to guard a streaming turn shown settled throughout (R9/V5). |
| `driveTurn` / `interruptTurn` | Polls for exactly one additional `conversation-turn-result` row; interrupt also checks for unknown-vendor rows. |
| `assertSingleTurnResultInvariants` | Checks unknown-vendor absence and permits row kinds `turn-result`, `error`, `interrupt` and `notice`; it does not itself count settlements. |
| Composed heap check | Samples browser `usedJSHeapSize` after warm-up and after five cycles; when both samples are positive, requires the latter to be less than 2.5 times baseline. Intended to guard growth across sessions (R5). |

The intended guards remain standing intent, but they do not establish that every historical defect would fail the current suite. `openChat` retries the projection control during a bounded 60-second window before returning. F2's recorded concern still applies: a recovered launch alarm can disappear before the alarm assertion, and recovery clicks are neither returned nor asserted absent. Tracking recoveries and requiring zero recoveries remains a recorded follow-on, not an implemented check.

F4's recorded concern also remains: turn and interrupt helpers count all result rows rather than only `data-kind="turn-result"`, and the kind assertion permits notices and errors. A matching count alone does not prove successful assistant completion. The recorded intent to narrow settlement counting while retaining the separate flood check is not implemented here.

The Claude model-control case can reach its final banner checks without finding or applying a model control. Its name and comments express validation intent; its conditional actions do not guarantee a model change occurred.

The heap assertion measures browser memory, not daemon projector, lock or queue retention. It uses only the first configured harness and performs no numeric assertion when either sample is zero. R5's daemon-release intent therefore exceeds the deciding predicate in this browser test.

The current pi conversation projector has no dedicated `turn_start` or `turn_end` branch: if either reaches its live-frame mapper, it follows the unknown-vendor branch. This confirms the mapping discrepancy behind the recorded F3 concern, but does not establish a current failed pi run or its historical failed-settlement cause.

### Lifecycle and status uncertainty

The original card reported a handoff with codex independently green in four cases, Claude blocked before assertions by a headless launch catalog wait, pi unknown-vendor events and a failed settlement without assistant output, and composed/heap lanes not yet green. These are historical reports, explicitly outside this overview's operative promises. The assigned source owners contain scenarios and predicates, not authoritative current execution results or lifecycle acceptance. Current lane status, the Claude wait's present failure rate, the pi failed-settlement diagnosis and completion of the recorded follow-ons remain unverified.

## Evidence

- Suite selection, serial configuration, timeouts and admission before opt-in [1]
- Dagger admission requires a matching nonce and attestation file [2]
- Test opt-in skip [3]
- Scratch Codex home, inherited override, build/sync, scratch settings, free port, daemon logs, health wait and stop [4]
- Runtime rejects settings inside coordination root [5]
- Setup opt-in, base URL, shared state file and same-process handle [6]
- Teardown uses the stop handle rather than the state file [7]
- Launch selection and bounded projection recovery [8]
- Actual assertion predicates, turn counting, interruption, End and heap sampling [9]
- Four Codex cases and historical version label [10]
- Claude cases and conditional model-control actions [11]
- Pi scenario and historical version label [12]
- Composed harness scoping and first-harness browser heap predicate [13]
- Pi live-frame mapper leaves unhandled event types as unknown-vendor [14]
- Original suite intent, screenshot associations and host runbook [15]
