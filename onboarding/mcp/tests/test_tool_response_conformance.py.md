# mcp/tests/test_tool_response_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_tool_response_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:02+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82`|
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source (new file, **864 lines / 15 cases**); base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
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
  (`mcp/tests/test-evidence-lanes.toml:244`), which is what keeps these cases in the default lane.
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
| Registration and adapter id sets are derived from source and asserted equal both ways. | `test_registration_and_adapter_surface_agree_in_both_directions` | mcp/tests/test_tool_response_conformance.py:264-291 |
| The 17 internal compatibility registrations are named, not implied. | `test_the_seventeen_internal_registrations_are_named_not_implied` | mcp/tests/test_tool_response_conformance.py:292-323 |
| The fixtures' models are the registry's own objects. | `test_the_models_these_fixtures_validate_are_the_registered_ones` | mcp/tests/test_tool_response_conformance.py:324-344 |
| Every registered model is strict or declared flexible; the 48/36 split is pinned. | `test_every_registered_model_is_strict_or_declared_flexible` | mcp/tests/test_tool_response_conformance.py:345-362 |
| Every tool adapter module routes through the `_tool_payload` choke point, per handler on the return. | `test_every_tool_adapter_module_routes_through_the_choke_point` | mcp/tests/test_tool_response_conformance.py:363-423 |
| `lifecycle_finalize_task` validates with the series release produced, and asserts it reached the emitting branch. | `test_lifecycle_finalize_validates_with_the_series_release_produced` | mcp/tests/test_tool_response_conformance.py:471-497 |
| The same response validates on the `activation-release-blocked` arm, where only the release key is present. | `test_lifecycle_finalize_validates_on_the_release_blocked_arm` | mcp/tests/test_tool_response_conformance.py:498-527 |
| The declaring set for the two atomic-series keys is exactly `lifecycle_finalize_task`. | `test_the_two_atomic_series_keys_are_declared_together` | mcp/tests/test_tool_response_conformance.py:528-561 |
| `task_doc`'s `read_steps` validates and returns the authored units. | `test_task_doc_read_steps_validates_and_returns_the_checklist` | mcp/tests/test_tool_response_conformance.py:562-628 |
| The registered description and the refusal name the same `kind` vocabulary. | `test_task_doc_description_and_refusal_name_the_same_kind_vocabulary` | mcp/tests/test_tool_response_conformance.py:629-667 |
| Every `next_tool=` literal the lifecycle package passes is declared on the response model. | `test_every_next_tool_its_own_refusals_advertise_is_declared` | mcp/tests/test_tool_response_conformance.py:668-722 |
| The `sprint-owner-required` refusal is a typed payload, driven through the real tool. | `test_operator_inbox_post_sprint_owner_refusal_is_a_typed_payload` | mcp/tests/test_tool_response_conformance.py:723-756 |
| A queued operator post must still report `entryId`, `state`, `messageKind`, `deliveryState`. | `test_a_queued_operator_inbox_post_still_must_report_its_entry` | mcp/tests/test_tool_response_conformance.py:757-793 |
| `session_retire` reports the stranded row after the seat is already gone. | `test_session_retire_reports_the_stranded_row_after_the_seat_is_gone` | mcp/tests/test_tool_response_conformance.py:794-826 |
| The structural delivery projection is declared on the shared base every consumer inherits. | `test_the_structural_delivery_projection_is_declared_on_every_consumer` | mcp/tests/test_tool_response_conformance.py:827-860 |
| The lane row that keeps this module in the default lane. | "mcp/tests/test_tool_response_conformance.py" | mcp/tests/test-evidence-lanes.toml:244-244 |
| The choke point whose guarantee this module moves into the suite. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The registry whose models the structural layer sweeps. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:243-247 |
| The advertised public roster the surface layer checks against. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-22 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): **created**. The module is new in this leaf (790 lines at delivery; 864 after the `F1` fix round widened the choke-point case to a per-handler assertion on the return). It replaces the 1,174-line conformance sweep deleted at `d3610903` -- restoring that sweep reaches 11 rot sites, does not collect verbatim, and its sweep class is `@pytest.mark.integration`, so the default lane would have deselected the cases this leaf exists to land. Recorded the two-layer split, the firing-state witness rule, the 15-case / 84-model coverage boundary, and the source-text coupling of the three AST instruments. Verification metadata is the recorded base commit; the candidate is uncommitted and the governed closeout stamps the real code commit.
