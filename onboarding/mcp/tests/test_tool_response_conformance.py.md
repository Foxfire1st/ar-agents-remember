# mcp/tests/test_tool_response_conformance.py

## Current operative account — MIK-R112



The literal declarations include the grant adapter and its handler, `role_start_set` and native `retire_child`. Numeric roster/module/handler guards are source declarations, not a fresh execution or live tool-list result.

### Source and authority bounds

- The module declares `ROSTER_SIZE=44`, `TOOL_MODULE_COUNT=14` and `TOOL_HANDLER_COUNT=46`, including `explainer_control`. Assertions compare populations rather than granting acceptance from numbers.
- `test_every_registered_model_is_strict_or_declared_flexible` derives strict/flexible model sets; imports do not enlarge the public roster.
- No current dispatch contract is established by this module.



Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Internal services and historical fixtures do not re-advertise deleted MCP tools.

## Current source contract evidence

- Current source pins are 44 public tools, 14 adapter modules and 46 handlers. Both removed task reads assert the refusal code, file names and absence of steps. The test validates the logged whole result and checks the stripped delivered envelope for `read_steps`.

## Governing Overview

[Test suite overview](overview.md)

## Purpose

The conformance tests check registered MCP response contracts against selected emitting branches and the adapter structure. The adapters pass the computed result to `mcp/tools/base.py:_tool_payload`, which invokes application validation before shaping the caller’s response.

## Current source account

The deliberate population pins are 44 public tools, 14 adapter modules and 46 handler/call sites. Registration equality and AST return-through-choke-point assertions guard both directions.

## Code Commentary

### Current Contract

The removed-read case asserts `get` and `read_steps` return `operation-removed`, name the JSON and rendered document and carry no steps. After that loop it validates the `read_steps` whole result as `TaskDocResponse` and checks that its delivered answer omits the four envelope fields.

### Logic

Two layers answer different questions. `ToolResponseSurfaceTests` checks registration and adapter equality, requires every registered response model to be advertised, pins fixture models to registry objects, derives strict/flexible models and checks every adapter handler’s return through the choke point. `ToolResponseFiringStateTests` calls selected producers in scratch coordination worlds and asserts the payload and conditional keys for each case. These are source-defined checks, not execution results from this inspection.

The helpers are read-only instruments over source text: `adapter_tool_ids` (`:91-113`) parses the
adapter's own id literals, `choke_point_handlers` (`:116-151`) counts module-level handlers against
`_tool_payload(...)` call sites by AST, `advertised_description` (`:154-169`) reads the description
off the **registered** `FastMCP` surface, and `literal_keyword_values` (`:231-248`) derives the
`next_tool=` literals the lifecycle package actually passes. `_RegistrationStub` (`:172-176`) is a
two-method registrar double, not a fake of the product.

### Conventions

`unittest.TestCase` throughout, with no module pytest marker; its evidence-lane registration is **architecture-fitness**.
`ScratchWorldTests` (`:278-291`) builds each case’s temporary coordination root through this module’s own `scratch_coordination_root`; its teardown removes the roots that case registered.

**A fixture must reach the emitting branch.** The firing-state cases assert the conditional key they exercise so a fixture in an early-return branch cannot silently supply that witness.

### Invariants And Boundaries

- **A runtime dependency on source text.** `adapter_tool_ids`, `choke_point_handlers` and `literal_keyword_values` parse `mcp/src` and the lifecycle package, so this module is coupled to their shape as well as behavior.
- **The structural and firing-case populations differ.** Model population comes from the registry; structural coverage does not invoke every model’s producer. The firing-state class covers its explicitly named cases.
- The module has no pytest marker and is registered in `architecture-fitness`; membership is not execution evidence.
- The coordination-world fixture is defined in this module; its use does not establish execution or certification of a neighboring suite.

Registered TaskDocResponse validation distinguishes available rows carrying requirements (including an empty list) from unavailable rows without them. Empty sibling populations are valid; unknown or missing states, incompatible requirements and extra fields fail. The description oracle requires the literal Kind: subTask or master. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Retained Source-Epoch Context

These attributed excerpts preserve earlier module history, rationale, deliberate omissions and evidence limits recorded in the memory base. Source coordinates, populations, outcomes and ownership describe their recorded epochs. They do not renew execution results or replace the current source account. This pass did not rerun the historical checks.

### Earlier population and strict-model inventories

Retained account from memory base `81cfe4a8`, 12–13:

> - Pre-repair card claim: Card’s current-source account pins 74 tools/21 modules/98 handlers; current source pins 39/19/63. This is superseded archival wording, not a current prescription.
> - Pre-repair card claim: Evidence says strict/flexible 48/36 split is pinned; source now derives both sets without numeric pins. This is superseded archival wording, not a current prescription.

### Earlier declarations and retired dispatch proof

Retained account from memory base `81cfe4a8`, 17–19:

> - Source comparison: the current module declares ROSTER_SIZE=44, TOOL_MODULE_COUNT=14 and TOOL_HANDLER_COUNT=46, including explainer_control. The A10 declarations 42/13/44 and the earlier 41/20/65 and 39/19/63 accounts describe earlier source epochs. The remaining source assertions compare populations rather than granting acceptance from numbers.
> - Source comparison: test_every_registered_model_is_strict_or_declared_flexible derives strict/flexible model sets; imports and compatibility rows do not enlarge the public roster.
> - Historical source comparison only: the former DispatchAgentResponse field assertion is removed on A10 and supplies no current dispatch contract.

### Native-role population transition

Retained account from memory base `81cfe4a8`, 52–52:

> The deliberate population pins become 74 public tools, 21 adapter modules and 98 handler/call sites after native role tools replace the removed preparation route. Live registration equality and AST return-through-choke-point assertions still guard both directions. Older source/sidecar counts remain historical rather than current.

### Earlier composed source declarations

Retained account from memory base `81cfe4a8`, 58–58:

> The composed source declares41 public tools,20 modules and65 handlers; the R111 pre-sync42/20/66 and older39/19/63 figures are historical. Removed task-read coverage asserts both operations return operation-removed/file names, no steps, log-backed TaskDocResponse validation and no delivered framework envelope. The deleted successful-checklist method cannot witness current behavior. These declarations and assertions are not a fresh live advertisement; retain the separately disclosed delivered-payload fallback rather than claiming every whole-result check is independent.

### Earlier structural and firing-state coverage

Retained account from memory base `81cfe4a8`, 62–71:

> Two layers, and they answer different questions.
> `ToolResponseSurfaceTests` (`:261-423`) is **total and structural**: registration and adapter
> surface agree in both directions, the 17 internal compatibility registrations are named rather
> than implied, the fixtures' models are `assertIs`-pinned to the registry's own objects, every
> registered model is strict or declared flexible, and every adapter module routes through the
> choke point. `ToolResponseFiringStateTests` (`:424-864`) is **executed**: each case drives the real
> producer, through the real adapter, against a hermetic scratch coordination root
> (`scratch_coordination_root`, `:213-239`), and asserts the payload validates **and** that the
> conditional key was actually produced — the witness assertion is what makes the fixture's
> reachability observable rather than assumed.

### Reason for replacing the earlier conformance sweep

Retained account from memory base `81cfe4a8`, 87–94:

> **The rule this module is built on, and the reason it was written rather than restored: a fixture
> that sits in a guard's false branch is a false green.** The 1,174-line conformance sweep deleted at
> `d3610903` captured `lifecycle_finalize_task` with `dry_run=True` — where the atomic-series release
> bridge returns early and never emits the two keys its own model forbids — and captured `task_doc`
> with `operation="create"` only, never `read_steps`. It passed for the whole life of both defects.
> Every executed case here therefore asserts the emitting branch first; a fixture that fell into the
> early return fails instead of passing quietly. The deleted sweep was also
> `@pytest.mark.integration`, so the default lane deselected the very cases it existed to land.

### Earlier selected-defect and coverage-limit account

Retained account from memory base `81cfe4a8`, 98–108:

> - **A runtime dependency on source text.** `adapter_tool_ids`, `choke_point_handlers` and
>   `literal_keyword_values` parse `mcp/src` and the lifecycle package, so this module is coupled to
>   their shape, not only to their behaviour.
> - **Model population is derived from the registry; surface coverage is structural, not executed.** The
>   executed layer covers the seven defects this leaf repaired and their projections. Landing an
>   executed payload for every registered model needs the fixture infrastructure the deleted sweep
>   had, and that infrastructure is what rotted (11 rot sites; it does not collect verbatim).
> - **No `-m` override and no marker**: lane membership is `architecture-fitness`
>   (`mcp/tests/test-evidence-lanes.toml`), which is what keeps these cases in the default lane.
> - Importing `test_agent_notifier` for its fixtures means this module shares that module's world
>   builder; it does not re-run or certify it.

### Earlier source-caption custody

Retained account from memory base `81cfe4a8`, 158–158:

> - Current literal source populations are 44 roster names, 14 adapter modules and 46 handlers, while strict/flexible sets remain derived. Anchor: `ROSTER_SIZE`, `TOOL_MODULE_COUNT`, `TOOL_HANDLER_COUNT` [Past-epoch source caption, detached from live reference 22. Recorded citation custody: mcp/tests/test_tool_response_conformance.py blob f59be949fc3fa155da0ce68d6c8301c02ac3e624 (available); historical event commit not identified. No historical event or intent inferred.]

## Retained Full-Card Audit Context

These distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe their recorded epochs; this pass adds no execution, mutation result or acceptance. Historical reference labels are custody text and do not select live anchors.

### Earlier numbered-reference custody warning

> > **Retained historical source account — superseded by the current contract:**
> > Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

The warning describes the earlier reference condition. It does not assert that renewed current references remain stale, or excuse checking them; historical custody does not establish present proof truth.

## Evidence
### Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

- The structural sweep compares the imported response registry, AST-derived adapter IDs, advertised roster and actual registered FastMCP listing. Registry and adapter differences must be empty in both directions. [1]

- The fixtures' models are the registry's own objects.

- Every registered model is strict or declared flexible, and the split is derived twice — from the declared base class and from each model's own `extra` config — so the two derivations must agree by name.

- Every tool adapter module routes through the `_tool_payload` choke point, per handler on the return.

- A constructed series contract reaches the finalization result builder. The success result carries both activation keys with an already-vacant release.

- The release double raises OSError. The case checks activation-release-blocked, a release-failed payload, OSError type and the same blocked release state in the validated model. [7]
- Among strict response models, the declaring sets for both atomic-series keys are equal and contain only lifecycle_finalize_task. [8]

- The registered description and the refusal name the same `kind` vocabulary.

- The test scans literal `next_tool` values and calls `_retired_generation_refusal` for closeout and integrate to collect `worktree_closeout_apply` and `worktree_integrate`. A response-boundary probe submits each of the four collected successors in a constructed `closeout-candidate-state-moved` refusal through the public response adapter and checks that the typed model retains `nextTool`.



- The choke point whose guarantee this module moves into the suite. Anchor: `_tool_payload` [17]


- The registry whose models the structural layer sweeps. [18]

- The advertised public roster the surface layer checks against. [19]

### Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

No repository or external-system boundary is proved by this module.

### Repo-Internal References (renewed)

- The module defines scratch_coordination_root and ScratchWorldTests locally; setUp tracks roots, world registers them and tearDown removes them. [24]

## Current source evidence



Current source: The literal PUBLIC_TOOLS source tuple contains 44 names. The conformance test source pins ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46 and derives strict/flexible model sets from base classes and extra configuration. These are literal declarations and test assertions, not a fresh module/handler collection or execution result.

- The fixtures' models are the registry's own objects. Anchor: `test_the_models_these_fixtures_validate_are_the_registered_ones` [3]
- Every registered model is strict or declared flexible, and the split is derived twice — from the declared base class and from each model's own `extra` config — so the two derivations must agree by name. Anchor: `test_every_registered_model_is_strict_or_declared_flexible` [4]
- Every tool adapter module routes through the `_tool_payload` choke point, per handler on the return. Anchor: `test_every_tool_adapter_module_routes_through_the_choke_point` [5]
- A constructed series contract reaches the result builder and activates the emitting arm. The case requires both payload keys, validates finalized state and checks an already-vacant release. [6]
- The registered description and the refusal name the same `kind` vocabulary. Anchor: `test_task_doc_description_and_refusal_name_the_same_kind_vocabulary` [10]

- The test scans literal `next_tool` values and calls `_retired_generation_refusal` for closeout and integrate to collect `worktree_closeout_apply` and `worktree_integrate`. A response-boundary probe submits each of the four collected successors in a constructed `closeout-candidate-state-moved` refusal through the public response adapter and checks that the typed model retains `nextTool`. [11]



- The roster tuple contains 44 names. The conformance declarations set ROSTER_SIZE to 44, TOOL_MODULE_COUNT to 14 and TOOL_HANDLER_COUNT to 46. Structural assertions check the exact populations and derive strict and flexible sets from both base classes and extra configuration. [22]



- Registered TaskDocResponse validation distinguishes available rows carrying requirements (including an empty list) from unavailable rows without them. Empty sibling populations are valid; unknown or missing states, incompatible requirements and extra fields fail. The description oracle requires the literal Kind: subTask or master. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [23]

- The architecture-fitness lane selects mcp/tests/test_tool_response_conformance.py. Execution evidence is recorded separately. [20]
