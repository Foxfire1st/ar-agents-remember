# mcp/tests/test_codex_capsule_delivery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-18T13:43+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l5-ar` uncommitted source; base `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| path | `mcp/tests/test_codex_capsule_delivery.py` |
| doc_type | `file-level-onboarding` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**The contract for the Codex capsule-delivery seam and its whole carrier chain, from the launch
boundary to the adapter's settings.** `260915-CAPS-L5` created the module; it collects **28 cases**
(`pytest --collect-only -m ""` → `28 tests collected`, and the default selection collects the same 28 —
this module carries no `integration` marker). Its lane row is `provider-conformance` in
`test-evidence-lanes.toml`.

Its subject is an **authority and lifetime boundary**, so the cases are grouped by the question they
answer rather than by the function they call:

| Group | Cases | What is pinned |
| --- | --- | --- |
| instruction channel | `test_instruction_channel_is_the_schema_supported_thread_open_field`, `test_thread_instruction_params_carry_only_the_trusted_stream` | the field is the schema-supported `developerInstructions`, the parameter **set** is exactly that one key, and `baseInstructions` is absent |
| refusal and mixing | `test_refused_refresh_yields_no_instruction_params`, `test_task_and_skill_content_cannot_enter_the_instruction_slot` | a refused refresh yields nothing; task text, skill content and model-authored text have no route in |
| lifetime | `test_same_digest_restates_bytes_and_a_changed_digest_needs_a_boundary`, `test_a_second_turn_and_a_resume_do_not_restate_the_corpus`, `test_changed_revision_on_a_live_thread_opens_a_fresh_binding`, `test_the_session_decision_path_compares_the_recorded_binding_and_digest` | same digest → in place; changed revision → a supported boundary; the recorded binding and digest are compared, never substituted |
| the real DTOs | `test_the_frozen_shapes_this_conversion_depends_on`, `test_delivery_consumes_a_genuine_compilation_result`, `test_a_launcher_seat_reports_its_sentinel_role`, `test_a_real_launcher_compilation_reports_the_sentinel_role`, `test_a_seat_the_conversion_does_not_recognise_is_refused` | L2's landed shapes, driven through the public compiler — no stand-in classes |
| the production factory | `test_the_production_factory_fills_the_capsule_carrier`, `test_the_factory_filled_settings_put_the_capsule_on_the_wire`, `test_the_production_factory_refuses_a_capsule_for_a_harness_without_the_channel` | the factory — the only producer of the settings — fills the carrier, the filled settings reach the wire, and a channel-less harness is refused |
| the launch boundary and transport | `test_a_launch_boundary_capsule_reaches_the_adapter_settings`, `test_the_launch_boundary_request_carries_the_capsule_into_the_runner_config`, `test_the_no_selection_branch_also_carries_the_capsule`, `test_a_capsule_free_launch_configuration_carries_nothing`, `test_a_malformed_capsule_payload_is_refused_before_delivery`, `test_the_carrier_value_type_guards_its_own_wire_form` | the carrier travels `TerminalLaunchRequest.control` → `RunnerConfig` → the encoded payload → parse → **both** factory calls; a malformed payload refuses; a capsule-free configuration carries nothing |
| legacy chain and observation | `test_legacy_launch_without_a_capsule_is_unchanged`, `test_legacy_chain_switch_decision_respects_the_capsule_gate`, `test_legacy_chain_switch_is_scoped_to_the_capsule_launch`, `test_snapshot_reports_applied_capsule_and_observed_instruction_sources`, `test_initial_thread_open_sends_instructions_on_the_wire` | the capsule-free launch is unchanged, the suppression key is scoped to a capsule launch, and the host's own `instructionSources` is published verbatim |
| live native | `test_live_app_server_observes_instruction_sources_and_accepts_the_capsule` | a real `codex app-server` on a workspace that **does** contain `AGENTS.md` reports zero loaded instruction documents under the experimental launch (gated by `skipif` on the pinned CLI version — a skip is not a pass) |

## Code Commentary

### Logic

The module drives production seams rather than re-implementing them. Two doublings are deliberate and
named: `RecordingTransport` (a transport that records the requests the session actually sends, so wire
shape is asserted without a vendor process) and `_StubDiscoverer` (the transient capability-preflight
adapter, doubled so the launch-boundary case does not start a second vendor process). The **real**
adapter in those cases still comes from the production factory, because the factory owns that choice.

The launch-boundary case is the one the round-3 review demanded: it drives the real
`_prepare_controlled_launch` with a fully resolved Codex `RunnerConfig` whose carrier was round-tripped
through `control_runner_command` → `parse_runner_config`, and asserts the delivered value equals
`settings.capsule_delivery`. Removing either factory call's argument fails it.

### Conventions

Cases are falsifiable by construction: each production line named in the leaf's audit has a seed that
mutates it and a case that fails. Real DTOs are imported from the compiler package — the round-2
stand-in classes (`_CompilerBinding`/`_CompilerCapsule`/`_CompilerResult`) were deleted, and
`grep -c '_Compiler'` over this module is `0`. The live case reads the installed CLI version first and
skips with a message naming the mismatch.

### Invariants And Boundaries

- The instruction parameter is **only** `developerInstructions`; `baseInstructions` is the vendor's.
- A capsule-free launch emits **no** instruction field and **no** suppression key.
- The payload key `capsuleDelivery` exists only when a capsule is present, so the capsule-free encoded
  payload is byte-identical to the base payload — this module pins the absence structurally
  (`"capsuleDelivery" not in decoded`, plus the pre-existing keys still present) rather than by length.
- A malformed payload is a refusal, never a silent drop: a caller that supplied a capsule must not
  receive a capsule-free process.
- A capsule handed to a harness without a verified instruction channel is refused at the factory.
- The suite carries no `integration` marker, so the live case's version guard is the only gate on it.
- **Not covered here, deliberately:** the delivered payload's size bound (`D12`), the vendor-side
  `thread/resume` effect (unmeasurable without a real turn), and a live end-to-end spawn through
  `terminal_opener`. All three are declared limits, not silent gaps.

### Todos

None known. The three one-case coverages the round-3 review named as observations (O19 no-selection
branch, O21 malformed payload, O22 the carrier's `from_json` guard) are now cases in this module.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The recording transport is the wire-shape boundary: cases assert the requests the session really sends. | `RecordingTransport` | mcp/tests/test_codex_capsule_delivery.py:142-295 |
| The applied parameter is pinned as a key **set**, so a second instruction field cannot ride along. | `test_thread_instruction_params_carry_only_the_trusted_stream` | mcp/tests/test_codex_capsule_delivery.py:316-333 |
| The conversion is driven over a genuine compilation built through the public compiler. | `test_delivery_consumes_a_genuine_compilation_result` | mcp/tests/test_codex_capsule_delivery.py:463-482 |
| The factory fills the carrier, the filled settings reach the thread-open request, and a channel-less harness refuses. | `test_the_production_factory_fills_the_capsule_carrier`; `test_the_factory_filled_settings_put_the_capsule_on_the_wire`; `test_the_production_factory_refuses_a_capsule_for_a_harness_without_the_channel` | mcp/tests/test_codex_capsule_delivery.py:560-638 |
| The launch boundary — real `_prepare_controlled_launch`, both factory calls, round-tripped carrier. | `test_a_launch_boundary_capsule_reaches_the_adapter_settings` | mcp/tests/test_codex_capsule_delivery.py:640-702 |
| The no-selection branch and the legacy configuration are pinned separately. | `test_the_no_selection_branch_also_carries_the_capsule`; `test_a_capsule_free_launch_configuration_carries_nothing` | mcp/tests/test_codex_capsule_delivery.py:777-815; mcp/tests/test_codex_capsule_delivery.py:960-983 |
| A malformed payload refuses before delivery, and the value type guards its own wire form. | `test_a_malformed_capsule_payload_is_refused_before_delivery`; `test_the_carrier_value_type_guards_its_own_wire_form` | mcp/tests/test_codex_capsule_delivery.py:816-885; mcp/tests/test_codex_capsule_delivery.py:886-959 |
| The session decision path compares the recorded binding and digest across four resume branches. | `test_the_session_decision_path_compares_the_recorded_binding_and_digest` | mcp/tests/test_codex_capsule_delivery.py:1055-1120 |
| The live case runs against the installed app-server; a version mismatch skips with its reason. | `test_live_app_server_observes_instruction_sources_and_accepts_the_capsule` | mcp/tests/test_codex_capsule_delivery.py:1208-1256 |
| The registry requires a lane row for every test module; this module's row is `provider-conformance`. | "\"mcp/tests/test_codex_capsule_delivery.py\"" | mcp/tests/test-evidence-lanes.toml:311-311 |

## Cross-Repo References

The live case and the instruction-channel fixture are pinned to the installed vendor app-server.

| Finding | Anchor | Source |
| --- | --- | --- |
| The live case is gated on the installed CLI version and reports a mismatch as a skip, never as a pass. | `test_live_app_server_observes_instruction_sources_and_accepts_the_capsule` | mcp/tests/test_codex_capsule_delivery.py:1206-1256 |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:303-303. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:298-298. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:297-297. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:296-296. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:293-293. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:43+02:00 — 260918-TSIP-L2 curator (uncommitted change set on `ar/260918-tsip-l2-ar`,
  base `d9becade`): **citation repair, no content change.** The `provider-conformance` lane-row claim
  above cited `mcp/tests/test-evidence-lanes.toml:254-254`; this leaf inserted one row into the
  `architecture-fitness` array at `:246`, which moved every entry below it by +1, so this module's own
  row is now at **`:255`** and the cited range held a neighbour (`test_codex_app_server_adapter_turns.py`)
  instead. The range was re-derived from the post-edit bytes and the file read back to confirm the
  anchor resolves inside it; the product's own `range_resolution` check had reported the same finding.
  Claim bytes are unchanged, so `lastUpdated` moves with this citation edit and the verification
  metadata stays at the leaf's base. The historical generated-repair bullet below is retained verbatim:
  it records what that mechanical repair did at its own revision, not what the row reads now.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:290-290. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T09:46:27+00:00: Generated citation repair: "\"mcp/tests/test_codex_capsule_delivery.py\"" repointed to mcp/tests/test-evidence-lanes.toml:254-254. No content impact: mechanical anchor-range projection bound to citation source snapshot 8e3e09b7b677dec09df0166f3450a2d9625d30e9bcf243ce7027ad865fd26365; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_live_app_server_observes_instruction_sources_and_accepts_the_capsule` repointed to mcp/tests/test_codex_capsule_delivery.py:1206-1256. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: created onboarding for the module that pins the
  capsule-delivery seam and the full carrier chain, recording the eight question groups, the two
  deliberate doublings, the byte-identical capsule-free wire requirement, the malformed-payload
  refusal, the channel-less-harness refusal, the lane row, and the three deliberately uncovered
  limits. Verification metadata stays pinned to the last committed source (`c1dbebf8`); closeout
  stamps the real commit.
