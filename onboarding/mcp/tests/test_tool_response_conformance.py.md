# mcp/tests/test_tool_response_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_tool_response_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Dev-time conformance for MCP tool response contracts, **at the firing state**. Production
validates every tool payload against its registered response model inside
`mcp/tools/base.py:_tool_payload`, and that validation runs *after* the producer has already
performed its writes — so a producer key the model forbids costs the caller the payload that
would have told it the work was done. This module moves that guarantee into the suite.

## Code Commentary

### Logic

Two layers, and they answer different questions.
`ToolResponseSurfaceTests` (`:261-423`) is **total and structural**: registration and adapter
surface agree in both directions, the 17 internal compatibility registrations are named rather
than implied, the fixtures' models are `assertIs`-pinned to the registry's own objects, every
registered model is strict or declared flexible, and every adapter module routes through the
choke point. `ToolResponseFiringStateTests` (`:424-864`) is **executed**: each case drives the real
producer, through the real adapter, against a hermetic scratch coordination root
(`scratch_coordination_root`, `:213-239`), and asserts the payload validates **and** that the
conditional key was actually produced — the witness assertion is what makes the fixture's
reachability observable rather than assumed.

The helpers are read-only instruments over source text: `adapter_tool_ids` (`:108-131`) parses the
adapter's own id literals, `choke_point_handlers` (`:132-167`) counts module-level handlers against
`_tool_payload(...)` call sites by AST, `advertised_description` (`:168-185`) reads the description
off the **registered** `FastMCP` surface, and `literal_keyword_values` (`:193-212`) derives the
`next_tool=` literals the lifecycle package actually passes. `_RegistrationStub` (`:186-192`) is a
two-method registrar double, not a fake of the product.

### Conventions

`unittest.TestCase` throughout; no `pytest` marks, so the module runs in the **default** lane.
`ScratchWorldTests` (`:240-260`) gives each executed case its own temporary coordination root, and
the import of `_entry`/`_FakeHost` from `test_agent_notifier` is the neighbouring suite's fixture
reused rather than re-implemented.

**The rule this module is built on, and the reason it was written rather than restored: a fixture
that sits in a guard's false branch is a false green.** The 1,174-line conformance sweep deleted at
`d3610903` captured `lifecycle_finalize_task` with `dry_run=True` — where the atomic-series release
bridge returns early and never emits the two keys its own model forbids — and captured `task_doc`
with `operation="create"` only, never `read_steps`. It passed for the whole life of both defects.
Every executed case here therefore asserts the emitting branch first; a fixture that fell into the
early return fails instead of passing quietly. The deleted sweep was also
`@pytest.mark.integration`, so the default lane deselected the very cases it existed to land.

### Invariants And Boundaries

- **A runtime dependency on source text.** `adapter_tool_ids`, `choke_point_handlers` and
  `literal_keyword_values` parse `mcp/src` and the lifecycle package, so this module is coupled to
  their shape, not only to their behaviour.
- **15 cases over 84 registered response models; face coverage is structural, not executed.** The
  executed layer covers the seven defects this leaf repaired and their projections. Landing an
  executed payload for every registered model needs the fixture infrastructure the deleted sweep
  had, and that infrastructure is what rotted (11 rot sites; it does not collect verbatim).
- **No `-m` override and no marker**: lane membership is `architecture-fitness`
  (`mcp/tests/test-evidence-lanes.toml:246`), which is what keeps these cases in the default lane.
- Importing `test_agent_notifier` for its fixtures means this module shares that module's world
  builder; it does not re-run or certify it.

## Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| Registration and adapter id sets are derived from source and asserted equal both ways. | `test_registration_and_adapter_surface_agree_in_both_directions` | mcp/tests/test_tool_response_conformance.py:303-360 |
| The 17 internal compatibility registrations are named, not implied. | `test_the_seventeen_internal_registrations_are_named_not_implied` | mcp/tests/test_tool_response_conformance.py:362-392 |
| The fixtures' models are the registry's own objects. | `test_the_models_these_fixtures_validate_are_the_registered_ones` | mcp/tests/test_tool_response_conformance.py:394-413 |
| Every registered model is strict or declared flexible; the 48/36 split is pinned. | `test_every_registered_model_is_strict_or_declared_flexible` | mcp/tests/test_tool_response_conformance.py:415-456 |
| Every tool adapter module routes through the `_tool_payload` choke point, per handler on the return. | `test_every_tool_adapter_module_routes_through_the_choke_point` | mcp/tests/test_tool_response_conformance.py:458-525 |
| `lifecycle_finalize_task` validates with the series release produced, and asserts it reached the emitting branch. | `test_lifecycle_finalize_validates_with_the_series_release_produced` | mcp/tests/test_tool_response_conformance.py:580-605 |
| The same response validates on the `activation-release-blocked` arm, where only the release key is present. | `test_lifecycle_finalize_validates_on_the_release_blocked_arm` | mcp/tests/test_tool_response_conformance.py:607-635 |
| The declaring set for the two atomic-series keys is exactly `lifecycle_finalize_task`. | `test_the_two_atomic_series_keys_are_declared_together` | mcp/tests/test_tool_response_conformance.py:637-667 |
| `task_doc`'s `read_steps` validates and returns the authored units. | `test_task_doc_read_steps_validates_and_returns_the_checklist` | mcp/tests/test_tool_response_conformance.py:671-736 |
| The registered description and the refusal name the same `kind` vocabulary. | `test_task_doc_description_and_refusal_name_the_same_kind_vocabulary` | mcp/tests/test_tool_response_conformance.py:738-773 |
| Every `next_tool=` literal the lifecycle package passes is declared on the response model. | `test_every_next_tool_its_own_refusals_advertise_is_declared` | mcp/tests/test_tool_response_conformance.py:777-828 |
| The `sprint-owner-required` refusal is a typed payload, driven through the real tool. | `test_operator_inbox_post_sprint_owner_refusal_is_a_typed_payload` | mcp/tests/test_tool_response_conformance.py:832-864 |
| A queued operator post must still report `entryId`, `state`, `messageKind`, `deliveryState`. | `test_a_queued_operator_inbox_post_still_must_report_its_entry` | mcp/tests/test_tool_response_conformance.py:866-880 |
| `session_retire` reports the stranded row after the seat is already gone. | `test_session_retire_reports_the_stranded_row_after_the_seat_is_gone` | mcp/tests/test_tool_response_conformance.py:903-932 |
| The structural delivery projection is declared on the shared base every consumer inherits. | `test_the_structural_delivery_projection_is_declared_on_every_consumer` | mcp/tests/test_tool_response_conformance.py:936-973 |
| The lane row that keeps this module in the default lane. | "mcp/tests/test_tool_response_conformance.py" |mcp/tests/test-evidence-lanes.toml:383-383|
| The choke point whose guarantee this module moves into the suite. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The registry whose models the structural layer sweeps. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:163-253 |
| The advertised public roster the surface layer checks against. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-97 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`test-evidence-lanes.toml`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept); 1 passing row(s) normalised by the fixer. The fixer's normalisation also re-measured ranges into files this leaf did not change (`public_roster.py`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:33:21+00:00: Generated citation repair: "mcp/tests/test_tool_response_conformance.py" repointed to mcp/tests/test-evidence-lanes.toml:383-383. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 1 citation into `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T16:25:39+02:00 — 260921-ICR-L42 curator: No content impact: re-pointed this card's citations into `test-evidence-lanes.toml` after this leaf's line insertions (candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`). Each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_tool_response_conformance.py" repointed to mcp/tests/test-evidence-lanes.toml:330-330. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "mcp/tests/test_tool_response_conformance.py" repointed to mcp/tests/test-evidence-lanes.toml:308-308. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_registration_and_adapter_surface_agree_in_both_directions` repointed to mcp/tests/test_tool_response_conformance.py:303-360. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_the_seventeen_internal_registrations_are_named_not_implied` repointed to mcp/tests/test_tool_response_conformance.py:362-392. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_the_models_these_fixtures_validate_are_the_registered_ones` repointed to mcp/tests/test_tool_response_conformance.py:394-413. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_every_registered_model_is_strict_or_declared_flexible` repointed to mcp/tests/test_tool_response_conformance.py:415-456. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_every_tool_adapter_module_routes_through_the_choke_point` repointed to mcp/tests/test_tool_response_conformance.py:458-525. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_lifecycle_finalize_validates_with_the_series_release_produced` repointed to mcp/tests/test_tool_response_conformance.py:580-605. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_lifecycle_finalize_validates_on_the_release_blocked_arm` repointed to mcp/tests/test_tool_response_conformance.py:607-635. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_the_two_atomic_series_keys_are_declared_together` repointed to mcp/tests/test_tool_response_conformance.py:637-667. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_task_doc_read_steps_validates_and_returns_the_checklist` repointed to mcp/tests/test_tool_response_conformance.py:671-736. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_task_doc_description_and_refusal_name_the_same_kind_vocabulary` repointed to mcp/tests/test_tool_response_conformance.py:738-773. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_every_next_tool_its_own_refusals_advertise_is_declared` repointed to mcp/tests/test_tool_response_conformance.py:777-828. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_operator_inbox_post_sprint_owner_refusal_is_a_typed_payload` repointed to mcp/tests/test_tool_response_conformance.py:832-864. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_a_queued_operator_inbox_post_still_must_report_its_entry` repointed to mcp/tests/test_tool_response_conformance.py:866-880. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_session_retire_reports_the_stranded_row_after_the_seat_is_gone` repointed to mcp/tests/test_tool_response_conformance.py:903-932. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_the_structural_delivery_projection_is_declared_on_every_consumer` repointed to mcp/tests/test_tool_response_conformance.py:936-973. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_tool_response_conformance.py" repointed to mcp/tests/test-evidence-lanes.toml:301-301. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:163-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): **created**. The module is new in this leaf (790 lines at delivery; 864 after the `F1` fix round widened the choke-point case to a per-handler assertion on the return). It replaces the 1,174-line conformance sweep deleted at `d3610903` -- restoring that sweep reaches 11 rot sites, does not collect verbatim, and its sweep class is `@pytest.mark.integration`, so the default lane would have deselected the cases this leaf exists to land. Recorded the two-layer split, the firing-state witness rule, the 15-case / 84-model coverage boundary, and the source-text coupling of the three AST instruments. Verification metadata is the recorded base commit; the candidate is uncommitted and the governed closeout stamps the real code commit.
