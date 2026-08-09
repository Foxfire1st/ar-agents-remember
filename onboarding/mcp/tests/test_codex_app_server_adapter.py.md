# mcp/tests/test_codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a` |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport conformance tests for the native Codex app-server adapter. The suite proves the
hosted control lifecycle, dynamic token-free advertisement, and ordered mid-thread model/effort
switching used by the normalized harness capability contract.

## Code Commentary

### 260714-ACPUI-L3 Ordered Mid-Thread Selection

Setter tests distinguish desired state from effective state on the existing Codex thread. A valid
model or effort change returns `queued` without an effective value, rebases effort to the new
model's dynamic default when needed, and becomes effective only when a subsequent `turn/start`
carrying that exact selection is accepted. The same transport and thread id remain in use; no
resume or reconnect implements the switch.

Ordering cases pin the selection epoch at prompt acceptance. A busy prompt accepted before a
setter keeps the old model/effort even if it starts later, while a prompt accepted after the setter
carries the new pair. Pending settings force a fresh turn instead of steering the active turn.
`inProgress` and `completed` turn-start statuses promote the carried selection; `failed` and
`interrupted` reject the prompt and leave desired state pending. Reversing desired model and effort
back to their current effective values clears the fresh-turn barrier rather than manufacturing more
queued work.

Validation remains catalog-owned: unknown models and effort values outside the desired model's
dynamic menu are `unsupported` without another RPC. Matching deliberate settings notifications
may promote state, a notification echoing the still-effective pair leaves the pending selection
alone, and unrelated external settings drift fails loudly. Idempotent setters return `immediate`
without inventing effective-value evidence.

### 260714-ACPUI-L2 Codex Initial Configuration

The adapter tests now pin both settings-resolved and roleless initial configuration. A configured
session sends model at `thread/start` and includes both `model` and
`model_reasoning_effort` in its configuration, retaining the same pair on resume. A roleless
session selects the single visible advertised default model and that model's own default effort
after token-free discovery, ignoring any need for a reconnect or a TUI launch override. Assertions
inspect the exact request and effective echo; no turn is submitted by this setup coverage.

### Logic

The deterministic transport records requests, notifications, responses, and shutdown modes while
the pinned app-server fixture supplies structured initialize, model-list, thread, turn, approval,
and elicitation frames. Existing scenarios cover startup/resume identity, exact reasoning-effort
acceptance, busy steer/queue policy, structured interactions, terminal mapping, reconnect without
resend, and strict correlation.

The ACPUI-L1 additions assert that a started adapter returns its retained model catalog without
issuing another request, including display text, descriptions, the current model, and the current
effort. A separate discovery scenario pages through `model/list` with `includeHidden: true`, retains
hidden models and their model-specific effort menus, leaves current selections unset before a
thread exists, and proves discovery never calls `thread/*` or `turn/*`. A repeated pagination cursor
fails loudly and still forces the transient app-server process to stop.

The experimental server-request case (`test_unknown_server_request_is_declined_while_experimental_history_stays_enabled`)
pins the remediation contract: an unknown/experimental request METHOD is still
DECLINED (`respond_error` -32601 — no experimental API is ever enabled), but the failure contract
deliberately changed: the method is vendor traffic that degrades to preserved raw evidence on any
thread, so the bridge stays `ready` with nothing left outstanding instead of marking `failed`
(multiplexed seats make new request types routine). The deeper method-first matrix (unknown vs
known-malformed vs boolean-rpc-id) lives in `test_codex_adapter_thread_demux.py`.

### Conventions

Tests use `pytest` with the AnyIO asyncio backend. `FakeCodexTransport` deep-copies protocol values
so fixture mutation and adapter behavior remain deterministic. The pinned `0.144.3` fixture is
schema evidence for the tests, not a production version enum or fallback catalog.

`make_adapter(transport, settings=TEST_SETTINGS)` takes one `CodexAppServerSettings` value rather
than a parallel keyword list: the module-level `TEST_SETTINGS` (xhigh effort, `gpt-5.6-sol`,
ephemeral) is the baseline every test starts from, and a case that needs a different resume thread,
approval policy, sandbox, config map, or submission limit varies exactly that field with
`dataclasses.replace(TEST_SETTINGS, ...)`. Three shared helpers keep the correlation cases honest:
`drain_events()` empties the adapter queue and returns the sequence number to compare against,
`assert_notification_is_inert()` emits an already-settled notification and proves the sequence did
not move from that known-empty queue, and `next_event_of_kind()` awaits the next event of a given
kind while skipping the ones emitted on the way there.

### Invariants And Boundaries

- Catalog discovery is protocol-only and prompt-free; it initializes app-server and reads every
  `model/list` page without opening a thread or turn.
- `advertise()` is a cached read after startup and must not spend another transport request.
- Hidden installed models remain represented in the full normalized catalog, with effort options
  nested under the model that advertised them.
- Repeated pagination cursors and absent or unconfirmed effort fail loudly; no static default model
  or effort menu is substituted.
- Setter acceptance is honest: desired changes are queued without an effective value, and only an
  accepted turn carrying the captured selection can promote that pair.
- Prompt selection is captured when the prompt enters the adapter; a later setter cannot
  retroactively change an already accepted busy-queue item.
- Failed or interrupted turn starts preserve pending desired state, while reversing desired state
  to the effective pair clears the fresh-turn barrier.
- Mid-thread switching never reconnects, resumes, or pastes; it uses `turn/start` overrides on the
  same thread and transport.
- Existing reconnect coverage requires `resend: false`, and the tests do not register a production
  driver or exercise pane/log readiness.
- An experimental request type is declined, never enabled — and the decline is a degrade (bridge
  stays `ready`), not a bridge failure.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test module and native Codex implementation directly prove the catalog-retention and
thread-free discovery contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The started-adapter test verifies cached advertisement, retained descriptions, current model/effort, and the exact initialize/model-list/thread-start request sequence after startup. | `test_handshake_uses_stable_protocol_and_exposes_effort_menu` | mcp/tests/test_codex_app_server_adapter_basic.py:26-83 |
| Discovery retains a paginated hidden model, sends only initialize/model-list requests, opens no thread or turn, and rejects a repeated cursor while stopping the process. | `test_discover_retains_paginated_hidden_catalog_without_opening_a_thread`; `test_discover_rejects_repeated_model_cursor_without_opening_a_thread` | mcp/tests/test_codex_app_server_adapter_basic.py:113-159; mcp/tests/test_codex_app_server_adapter_basic.py:162-177 |
| Model and effort changes remain queued until one same-thread turn accepts their exact override, with no reconnect or resume. | `test_set_model_and_effort_stay_pending_until_same_thread_turn_accepts` | mcp/tests/test_codex_app_server_adapter_turns.py:78-114 |
| Turn statuses promote only `inProgress`/`completed`; failed/interrupted starts reject and retain the fresh-turn requirement. | `test_turn_start_promotes_only_successful_submission_status`; `test_turn_acceptance_blocking_and_terminal_mapping` | mcp/tests/test_codex_app_server_adapter_turns.py:23-57; mcp/tests/test_codex_app_server_adapter_turns.py:117-156 |
| Busy-queue prompts preserve their acceptance-time selection epoch, and reversing pending settings back to effective clears the barrier. | `test_busy_second_submit_certifies_zero_bytes_without_steer_or_adapter_queue`; `test_reversing_pending_codex_settings_clears_fresh_turn_barrier` | mcp/tests/test_codex_app_server_adapter_correlation.py:231-257; mcp/tests/test_codex_app_server_adapter_turns.py:60-75 |
| Unknown model/model-local effort values cause no RPC; pending settings force a fresh turn rather than steer; deliberate notification matching and external-drift rejection stay distinct. | `test_codex_set_rejects_unadvertised_model_and_model_local_effort_without_rpc`; `test_pending_codex_settings_force_fresh_turn_instead_of_steering_active_turn`; `test_settings_notification_promotes_only_deliberate_match_and_keeps_drift_guard` | mcp/tests/test_codex_app_server_adapter_correlation.py:260-282; mcp/tests/test_codex_app_server_adapter_correlation.py:285-306; mcp/tests/test_codex_app_server_adapter_correlation.py:309-360 |
| Idempotent setters return immediate without falsely claiming an effective echo. | `test_idempotent_codex_set_is_immediate_without_invented_effective_evidence` | mcp/tests/test_codex_app_server_adapter_reconnect.py:27-40 |
| The experimental-request case pins the decline-not-fail remediation contract. | `test_unknown_server_request_is_declined_while_experimental_history_stays_enabled` | mcp/tests/test_codex_app_server_adapter_reconnect.py:164-201 |
| The shared `TEST_SETTINGS` baseline and the `drain_events`/`assert_notification_is_inert`/`next_event_of_kind` helpers every correlation case reuses. | `TEST_SETTINGS`; `drain_events`; `assert_notification_is_inert`; `next_event_of_kind` | mcp/tests/test_codex_app_server_adapter.py:231-235; mcp/tests/test_codex_app_server_adapter.py:261-268; mcp/tests/test_codex_app_server_adapter.py:271-280; mcp/tests/test_codex_app_server_adapter.py:283-288 |
| The adapter validates the native Codex harness id and delegates transient discovery and cached advertisement to its session. | `CodexAppServerAdapter`; `start`; `discover` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:91-1115 |
| Session discovery performs initialize plus paged model-list only and always stops its transient transport; started advertisement requires a retained catalog. | `CodexAppServerSession`; `discover`; `_read_models` | mcp/src/agents_remember/serving/codex_app_server_session.py:102-458 |
| Adapter setters update desired state, return queued or immediate honestly, and never make a setter RPC. | "    async def set_model("; "    async def set_effort("; "    def set_desired_model(self, model_key"; "    def set_desired_effort(self, effort" | mcp/src/agents_remember/serving/codex_app_server_adapter.py:163-194; mcp/src/agents_remember/serving/codex_app_server_adapter.py:196-224; mcp/src/agents_remember/serving/codex_app_server_session.py:226-245; mcp/src/agents_remember/serving/codex_app_server_session.py:247-253 |
| Each accepted prompt reserves its desired model/effort snapshot; pending settings force a fresh turn and remain attached to that evidence while queued. | `submit`; `_start_turn`; `preflight_operation` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:229-237; mcp/src/agents_remember/serving/codex_app_server_adapter.py:239-264; mcp/src/agents_remember/serving/codex_app_server_adapter.py:434-480 |
| Turn-start overrides carry the captured selection and promote it only after a non-failed/non-interrupted status. | "    async def _start_turn("; "    async def _accept_started_turn("; "    def accept_settings_selection(" | mcp/src/agents_remember/serving/codex_app_server_adapter.py:438-484; mcp/src/agents_remember/serving/codex_app_server_adapter.py:537-572; mcp/src/agents_remember/serving/codex_app_server_session.py:265-283 |
| Session state validates dynamic model-local effort, separates desired from effective state, promotes only an accepted selection, and guards settings notifications against unrelated drift. | `set_desired_model`; `set_desired_effort`; `accept_settings_selection`; `accept_settings_update` | mcp/src/agents_remember/serving/codex_app_server_session.py:226-245; mcp/src/agents_remember/serving/codex_app_server_session.py:247-253; mcp/src/agents_remember/serving/codex_app_server_session.py:265-283; mcp/src/agents_remember/serving/codex_app_server_session.py:285-303 |
| The fixture path remains an explicit test baseline rather than a runtime catalog source. | `fixture`; `TEST_SETTINGS` | mcp/tests/test_codex_app_server_adapter.py:140-141; mcp/tests/test_codex_app_server_adapter.py:231-235 |

## Cross-Repo References

The earlier coordination-repo review remains useful historical evidence for the pre-ACPUI Codex
protocol contract; it does not replace the current source tests.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260715-FEUI-L5 Submission Authority Delta

The suite now proves Codex has no vendor queue/steer path: settings and prompts bind full operation
refs to fresh turns, terminal evidence promotes exactly once, early completion is retained, rejected
guards clean pending state, and stale/duplicate/reused turn ids cannot release a successor. Both
synchronous and async correlation maps are bounded.

## 260727-CHATS-IM-L2 Experimental Capability Delta

The unknown server-request regression now distinguishes two independent facts: experimental history
is enabled at initialization, while an unrelated unsupported server-to-client request is still
declined/degraded. It does not infer that any history method exists or that experimental server
requests are accepted; the dedicated history-reader tests own runtime method probing.

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T21:13:21+02:00 — W2-B07 curator: repaired 16 repository-reference citations and normalized 2 prose citations after bounded source reads; all 16 surviving rows use exact anchors and generated ranges. Under the 2026-08-02 14:10 R27 ruling, deleted 1 legacy reviewer-verdict row because it is true legacy review evidence rather than a semantic Tier-3 source-code claim, and no resolver-supported code/memory mirror exists.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The turn-start
  override material is now split across two methods in `codex_app_server_adapter.py`: `_start_turn`
  plus `_turn_start_params` at L528-L593 (which carries `evidence.model.model` / `evidence.effort` and
  rejects a `failed`/`interrupted` start status), and `_accept_started_turn` at L657-L701 (which calls
  `self._session.accept_settings_selection(...)` — the promotion). Was the single range L519-L615.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the suite's own fixture surface changed, so
  the Conventions section was rewritten rather than attested. `make_adapter` no longer takes the
  seven keywords it used to assemble into a settings object; it takes one
  `CodexAppServerSettings` defaulting to the new module-level `TEST_SETTINGS`, and the resume,
  submission-limit, and approval/sandbox/config cases vary a single field with
  `dataclasses.replace(TEST_SETTINGS, ...)`. Three extracted helpers — `drain_events`,
  `assert_notification_is_inert`, and `next_event_of_kind` — replace the inline queue-draining
  and `while True` event loops the correlation cases repeated, and are now named alongside a
  reference row at L225-L284. That 31-line block plus the `AdapterEvent` import shifted every
  test below it, so all eight own-file reference ranges were re-verified against the current
  definitions and re-anchored (for example the experimental-request row from L1078-L1118 to
  L1091-L1129 and the discovery row from L294-L357 to L388-L454), and the fixture-path row was
  re-pointed from the long-stale L27-L29 to the current `FIXTURE_PATH` at L34 plus the
  schema-pinning test at L1251-L1259. The Logic paragraph's experimental-case name was also
  corrected to the source's actual
  `test_unknown_server_request_is_declined_while_experimental_history_stays_enabled`. No test
  was added, removed, or renamed, and every decline/degrade, promotion, and validation claim
  still holds.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: corrected the adapter-suite capability
  record to experimental history opt-in without overclaiming method or server-request support.
  Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the deliberately changed
  experimental-request failure contract — the decline is unchanged (`respond_error` -32601, no
  experimental API), but an unknown/experimental request METHOD now degrades to preserved evidence
with the bridge `ready` instead of marking it `failed` — and added the matching invariant plus a
reference row. Re-anchored the four adapter-source citations the remediation
  shifted (L88-L126 → L137-L190; L153-L208 → L226-L313; L220-L272 → L314-L355; L344-L415 →
  L519-L615). Verification metadata stays pinned at the file's last committed touch; the adapter
  change itself is uncommitted.
- 2026-07-17T21:39+02:00 — FEUI-L5: replaced busy-queue/steer expectations with fresh-turn,
  exact-ref, early-completion, cleanup, id-reuse, and bounded-correlation proofs.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented queued desired-versus-effective
  state, same-thread turn overrides, prompt selection epochs, successful-status-only promotion,
  reversal collapse, model-local validation, and deliberate-notification drift guarding.
  Verification metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added the configured and roleless Codex
  `thread/start` launch contract, including model-local default effort and resume preservation.
  Verification metadata remains pinned until closeout stamps the L2 code commit.

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented cached current-session
  advertisement, paginated hidden-model discovery, model-gated effort metadata, thread/turn-free
  enumeration, and repeated-cursor cleanup; corrected the governing overview backlink while
  preserving existing verification metadata.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented null-requestId correlation, same-row
  completion projection, loud failure cases, and no-replacement terminal state assertions.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented negotiated-version acceptance and loud rejection
  coverage.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for fake-protocol
  conformance, R11 strictness, server requests, busy policy, terminal mapping, and no-resend
  reconnect coverage. Verification remains unset until closeout stamps the code commit.
