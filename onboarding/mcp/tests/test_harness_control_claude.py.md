# mcp/tests/test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport conformance coverage for the native Claude stream-JSON adapter, including structured
startup, token-free and MCP-isolated model catalog discovery, same-session model/effort setters with
terminal evidence, correlated delivery, interactions, reconciliation, limits, shutdown, and
terminal normalization.

## Code Commentary

### Sub-Agent Text Forwarding Floor

The fail-closed `--forward-subagent-text` version floor is covered by the launch and
forwarding cases listed in Repo-Internal References.
The fake transport records launch argv and replays startup frames on the second start; the mapper-tier
floor verdicts live in `test_conversation_projector_claude_agents.py`.

Those cases prove the argv contract but not the transport lifecycle it assumes: `_FakeClaudeTransport`
accepts a second `start` on the same object, so the at-floor case passed while the production
transport would have refused its own re-launch (260727-CHATS-IM-L4).
`ClaudeProductionTransportRelaunchTests` closes that gap by driving the real adapter with
`transport_factory=ClaudeSubprocessTransport` against a local stream-json stub that reports 2.1.220
and appends each launch argv to a log file. It asserts exactly two launches with the flag only on the
second, `control` = `ready`, and a selectable model whose effort options are advertised — the
dashboard's model/effort surface. The stub is a local interpreter script, so the case stays
credential-free while still exercising real process ownership.

### Discovery Isolation And Live Closure

Claude catalog discovery stays token-free while the transient probe is kept from starting
unrelated MCP servers inherited through the caller's native argv. The discovery-only regression
table covers the selector grammar accepted by the observed Claude Code 2.1.210 install: one
separate config, variadic and repeated separate configs, equals-attached configs, the exact strict
flag, and the first `--` end-of-options separator. It requires all accepted selectors before the
separator to be replaced by exactly one strict empty config. Unrelated options retain their order,
an equals-attached config never consumes a following positional, and the entire post-`--` suffix
remains byte-for-byte intact. The test deliberately does not invent rejected boolean or negated
strict spellings.

This isolation is scoped to `discover()`. A separate normal-start case requires existing caller MCP
selectors to survive byte-for-byte, so ordinary settings-owned sessions continue to load their
installed MCP configuration. The original fake discovery case still proves the synthetic bootstrap
has zero turns and zero cost, uses one strict empty config, and force-stops the transient transport.

Live evidence closes the relationship between those fake pins and the native process:
a two-marker A/B made normal startup create both configured markers while discovery created
neither, returned the same model-gated catalog at zero turns/cost, and cleaned up. The independent
reviewer then reproduced an adversarial marker collision against the corrected candidate; its
marker stayed absent and the same five observed model keys returned. Those row counts and keys are
live installation/auth observations, not production enums or expectations encoded by this suite.

### Same-Session Setter Evidence

The same-session scenarios drive `/model` and `/effort` as structured Claude session commands through the
native stream transport. A set becomes `echo-verified` only after the replayed user frame matches
the retained correlation, session id, and exact canonical command body and a following terminal
result echoes an allowed effective label. Model changes immediately re-gate effort against the
new model's dynamic menu; an unavailable effort is `unsupported` without another write. A
completed command with no effective echo is only `immediate` and does not promote advertised
state, while a failed native command is `unsupported`.

Fable behavior is deliberately native-result-driven. A provider-qualified model whose key does not
contain `fable` can return `noninteractive_set_blocked` and map to `unsupported` with launch-flag
guidance. Conversely, an advertised alias literally named `fable` can echo a Sonnet terminal label
and succeed. This proves there is no key/prefix heuristic. Exact terminal-label tests also reject
prefix impostors and arbitrary `(default)` strings; allowed aliases are derived from the dynamic
catalog row and matching resolved-model identities.

Timeout and cancellation cases retain only enough abandoned command state to neutralize late
replay/result frames before a clean retry. A later setter is not sent while an abandoned command
has not terminated, completed duplicate replay is ignored, strict correlation/body/session
mismatches fail loudly, and a duplicate retained correlation is never written a second time.

### Effective-Launch Mismatch

The Claude suite can inject an expected `ResolvedLaunch` and now proves the fail-loud acceptance
boundary. When `system/init` echoes a different effective model, the adapter force-closes its
transport and propagates `HarnessControlError` so the runner can persist
`control=failed`/`acceptance=rejected` with exact bridge evidence. Genuine protocol negotiation
incompatibility remains the distinct `unsupported` result covered by the adjacent test.

### Logic

Pinned stream-JSON fixtures and a deterministic transport drive initialize, synthetic bootstrap,
catalog, turn, interaction, replay, failure, and result frames. Existing cases cover launch
preservation, discovery-only MCP isolation, compatible structured version negotiation, prompt
correlation, busy ordering, durable interaction responses, supported commands, ambiguous
disconnect reconciliation, bounded history, and safe terminal failure metadata.

The fixture baseline tracks the live-confirmed `2.1.210` shape with catalog-specific
coverage. Discovery performs only the synthetic `shouldQuery: false` bootstrap plus the
`list_models` control request, asserts zero turns and zero cost, and always stops the transient
process. Started advertisement is cached, selects the current model, keeps effort levels nested per
model, leaves current effort unknown instead of inventing it, and preserves disabled models as
non-selectable catalog rows. Current initialization is accepted without stale `models` or `account`
fields, while duplicate model keys or a rejected `list_models` response make the adapter
unsupported and fail advertisement loudly without a fallback.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed UUIDs/timestamps, and JSONL fixtures under
the exact observed version directory. Selector cases are table-driven by grammar shape rather than
captured model names. Fake writes and argv are inspected structurally; secrets placed in the launch
environment must never appear in handshake evidence.

### Invariants And Boundaries

- Enumeration is token-free: the bootstrap is synthetic and non-querying, and the fixture proves
  zero turns and zero cost before `list_models` completes.
- Discovery removes every installed-grammar MCP selector before the first `--`, inserts one strict
  empty config, preserves unrelated argv and the complete positional suffix, and always stops the
  transient transport.
- Normal session startup must preserve caller MCP selectors byte-for-byte; discovery isolation is
  never applied to the real settings-owned session path.
- The adapter uses Claude's native control request; no ACP transport, composer paste, static enum,
  or Toad host is involved.
- Effort options remain model-gated, and current effort remains absent when Claude does not report
  it.
- Malformed, duplicate, contradictory, or rejected catalog evidence fails loudly; there is no
  hardcoded production fallback.
- Model/effort promotion requires same-session exact replay correlation plus terminal effective
  echo; completion without that echo never becomes `echo-verified`.
- Claude's native `noninteractive_set_blocked` result determines unsupported switching. Model keys,
  aliases, or provider prefixes are never used to guess a Fable refusal before sending.
- Dynamic model terminal aliases match exactly; prefix collisions and unrelated default labels do
  not promote capability state.
- Timed-out/cancelled command frames are neutralized without stealing a later setter result or
  writing a duplicate retained correlation.
- `--forward-subagent-text` is fail-closed: emitted only behind a probed >= 2.1.220 install via a
  probe-launch-then-relaunch flow; below-floor or unparseable versions run exactly one flagless
  launch with an honest `unverified` note (fix-round finding 8).
- The fake transport is restart-tolerant and therefore cannot witness process ownership; any claim
  about the probe re-launch actually launching belongs to the real-transport case, not the fake tier.
- Fixture versions are test evidence rather than a production pin, and credentials/model output
  remain excluded from retained startup evidence.

### Todos

None.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The tests and native Claude adapter modules directly prove the startup, parsing, and cached
advertisement contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Token-free discovery uses one non-querying synthetic user frame, records zero turns/cost, inserts one strict empty config, selects the current model, and stops the transient transport. | `test_discover_uses_only_token_free_bootstrap_and_list_models` | mcp/tests/test_harness_control_claude_stream_1.py:33-53 |
| Discovery replaces separate, variadic/repeated, and equals-attached MCP selectors; preserves unrelated argv and the full post-`--` suffix; and leaves exactly one strict empty config before the separator. | `test_discover_replaces_all_installed_mcp_selector_spellings` | mcp/tests/test_harness_control_claude_stream_1.py:55-167 |
| Normal startup preserves caller MCP selectors byte-for-byte, proving isolation is discovery-only. | `test_normal_start_preserves_existing_mcp_selectors_byte_for_byte` | mcp/tests/test_harness_control_claude_stream_1.py:169-189 |
| Startup preserves native launch settings, issues `list_models`, caches the selected catalog, gates efforts by model, leaves current effort unknown, and marks disabled rows non-selectable. | `test_launch_preserves_arguments_environment_and_requires_structured_init` | mcp/tests/test_harness_control_claude_stream_1.py:191-246 |
| Forwarding at or above the supported version floor relaunches with `--forward-subagent-text`. | `test_forward_subagent_text_relaunches_with_the_flag_at_or_above_the_floor` | mcp/tests/test_harness_control_claude_stream_1.py:248-273 |
| An unparseable version keeps `--forward-subagent-text` fail-closed. | `test_forward_subagent_text_stays_fail_closed_on_an_unparseable_version` | mcp/tests/test_harness_control_claude_stream_1.py:275-290 |
| Current initialization omits stale model/account fields, while duplicate or rejected catalog evidence yields unsupported/loud failure with no fallback. | `test_current_initialize_without_models_or_account_is_accepted`; `test_malformed_or_rejected_list_models_fails_loud_without_fallback` | mcp/tests/test_harness_control_claude_stream_1.py:292-308; mcp/tests/test_harness_control_claude_stream_1.py:310-342 |
| Same-session model/effort setters require native replay plus terminal echo, update the model gate only on evidence, and refuse effort unavailable for the selected model without a write. | `test_model_and_effort_set_require_terminal_echo_and_update_model_gate` | mcp/tests/test_harness_control_claude_stream_2.py:66-118 |
| Native failure and non-echo completion remain unsupported/immediate without promotion; provider-qualified Fable refusal and a successful alias named `fable` prove there is no name heuristic. | `test_terminal_refusal_or_non_echo_never_promotes_claude_capability`; `test_native_noninteractive_set_blocked_refusal_maps_without_alias_guessing` | mcp/tests/test_harness_control_claude_stream_2.py:120-142; mcp/tests/test_harness_control_claude_stream_2.py:144-209 |
| Exact dynamic terminal aliases reject prefix impostors and arbitrary default labels. | `test_model_terminal_labels_are_exact_dynamic_aliases_not_prefixes` | mcp/tests/test_harness_control_claude_stream_2.py:211-294 |
| Repeated late replay of an expired set restores one turn rather than one turn per replay. | `test_repeated_late_replay_of_an_expired_set_restores_one_turn_not_two` | mcp/tests/test_harness_control_claude_stream_2.py:330-371 |
| The Claude catalog parser validates the native response, exact unique model keys, model-specific effort consistency, disabled state, and current-model membership. | `parse_list_models_response`; `_parse_model`; `_require_unique_model_keys`; "def _select_current_model" | mcp/src/agents_remember/serving/claude_stream_capabilities.py:15-32; mcp/src/agents_remember/serving/claude_stream_capabilities.py:50-75; mcp/src/agents_remember/serving/claude_stream_capabilities.py:78-83; mcp/src/agents_remember/serving/claude_stream_capabilities.py:86-110 |
| The adapter negotiates startup then catalog before readiness, isolates only transient discovery, force-stops that probe, and retains cached advertisement for started sessions. | `start`; `discover`; `advertise` | mcp/src/agents_remember/serving/harness_control_claude.py:283-318; mcp/src/agents_remember/serving/harness_control_claude.py:327-341; mcp/src/agents_remember/serving/harness_control_claude.py:343-350 |
| The discovery argv builder removes only accepted pre-separator MCP selector spellings, preserves unrelated arguments/suffixes, and adds one strict empty set; the ordinary stream argv builder stays separate. | `build_claude_discovery_argv`; `build_claude_stream_argv` | mcp/src/agents_remember/serving/claude_stream_protocol.py:88-113; mcp/src/agents_remember/serving/claude_stream_protocol.py:116-145 |
| Native startup frames define the exact `list_models` control request and a synthetic non-querying bootstrap. | `list_models`; `bootstrap_message`; "\"shouldQuery\": False" | mcp/src/agents_remember/serving/claude_stream_protocol.py:162-162; mcp/src/agents_remember/serving/claude_stream_protocol.py:208-218 |
| Claude setters validate the dynamic catalog/model gate, send structured commands, promote only echo-verified results, and derive exact model terminal aliases from the selected catalog row. | `set_model`; `set_effort`; `_submit_set_command`; `_model_terminal_results` | mcp/src/agents_remember/serving/harness_control_claude.py:352-376; mcp/src/agents_remember/serving/harness_control_claude.py:402-442; mcp/src/agents_remember/serving/harness_control_claude.py:686-707; mcp/src/agents_remember/serving/harness_control_claude.py:378-400 |
| State submission retains canonical command replay text, waits for a terminal result, and marks timed-out commands abandoned. | `submit`; `wait_terminal`; `abandon_submission` | mcp/src/agents_remember/serving/claude_stream_state.py:163-211; mcp/src/agents_remember/serving/claude_stream_state.py:225-241; mcp/src/agents_remember/serving/claude_stream_state.py:243-251 |
| Replayed-user handling requires exact retained correlation, session, and body; completed abandoned replays are ignored rather than requeued. | `_handle_replayed_user`; `_handle_abandoned_replay`; `_require_faithful_replay` | mcp/src/agents_remember/serving/claude_stream_state.py:624-670; mcp/src/agents_remember/serving/claude_stream_state.py:672-718; mcp/src/agents_remember/serving/claude_stream_state.py:720-738 |

## Cross-Repo References

The live and reviewer artifacts corroborate the fake selector grammar with real process
side-effect markers. Their five-row result is a captured install/auth observation, not a test enum.

| Finding | Anchor | Source |
| --- | --- | --- |

## Submission Authority Delta

Claude hosted-control tests now prove sole-operation authority across prompt/interaction/setter
traffic, exact terminal completion, late/cancel/duplicate immunity, and bounded retained history.
Unknown setter evidence remains the shared blocker until exact resolution.

## Native Interrupt Acceptance Delta

Claude control regressions now pin native interrupt request acceptance and the corresponding typed failure/detail paths without mistaking acknowledgement for turn settlement.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260731-EFA-L2 Delta — repeated late replay

`test_repeated_late_replay_of_an_expired_set_restores_one_turn_not_two`: replaying an expired set
more than once restores **one** turn, not one per replay. Replay is idempotent per set, so a
duplicated late frame cannot inflate the transcript.

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: reissued whole-claim evidence for Claude catalog parsing and native startup frames for same-reviewer closure.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 line citations. In
  `harness_control_claude.py` the startup/discovery/advertisement row moved from L97-L215 to
  L115-L269 (`start` L115-L237 negotiating startup then catalog, `discover` L246-L261 which builds
  the isolated argv and force-stops the probe in its `finally`, `advertise` L262-L269 returning the
  cached snapshot), and the setter row moved from L233-L308; L467-L550 to L287-L396 (`set_model`,
  `set_effort`, `_submit_set_command`, `_selected_model`, `_unsupported_set`) plus L545-L677 (the
  module-level set-result classifiers through `_model_terminal_results` and
  `_resolved_model_terminal_label`). In this suite itself the Fable row moved from L709-L799 to
  L942-L1031 (`test_terminal_refusal_or_non_echo_never_promotes_claude_capability` L942-L965 and
  `test_native_noninteractive_set_blocked_refusal_maps_without_alias_guessing` L966-L1031). Not
  repaired and reported upward instead: the other eight self-citations in this table are stale by
  roughly the same drift and need their own pass.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: recorded `ClaudeProductionTransportRelaunchTests`, the
  real-transport probe/relaunch proof, and named the restart-tolerant fake as the reason the at-floor
  argv case passed over a transport that would have refused its own re-launch.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the `--forward-subagent-text`
  flag-floor coverage (fix-round finding 8) — the fake transport's scripted re-launch
  (`start_argvs`/`restart_frames`), the below-floor one-launch omission with the exact
  `unverified` note, the at-floor probe-then-relaunch flow, and the unparseable-version
  fail-closed case. Verification metadata stays pinned (uncommitted); closeout re-stamps the
  candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-17T21:39+02:00 — FEUI-L5: added Claude sole-authority, exact completion, stale-event, and
  bounded-history regression proof.

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 test curator: documented discovery-only Claude MCP
  selector isolation across separate, variadic/repeated, equals-attached, and end-of-options forms;
  normal-start argv preservation; the zero-turn fake/live relationship; and the independent marker
  collision closure. Live catalog counts/keys remain observations, not enums. Verification metadata
  remains at the last landed source commit until closeout stamps the uncommitted L5 candidate.
- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented same-session structured setters,
  exact replay plus terminal-echo evidence, model-gated effort, native-result-driven Fable refusal,
  exact dynamic aliases, and cancellation/timeout/duplicate-correlation neutralization. Verification
  metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented expected-launch injection and the
  force-close/propagate behavior that distinguishes an effective model mismatch from protocol
  unsupported. Verification metadata remains pinned until closeout stamps the L2 code commit.

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the `2.1.210` catalog fixture,
  zero-turn/zero-cost discovery, cached model-gated advertisement, honest unknown effort, modern
  initialize shape, and loud no-fallback catalog failures; corrected the governing overview
  backlink while preserving existing verification metadata.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: recorded structured Claude negotiation and incompatible
  contract coverage.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
