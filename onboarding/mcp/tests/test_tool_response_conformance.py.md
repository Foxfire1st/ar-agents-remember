# mcp/tests/test_tool_response_conformance.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

- Registration and adapter id sets are derived from source and asserted equal both ways. [1]
- The 17 internal compatibility registrations are named, not implied. [2]
- The fixtures' models are the registry's own objects. [3]
- Every registered model is strict or declared flexible; the 48/36 split is pinned. [4]
- Every tool adapter module routes through the `_tool_payload` choke point, per handler on the return. [5]
- `lifecycle_finalize_task` validates with the series release produced, and asserts it reached the emitting branch. [6]
- The same response validates on the `activation-release-blocked` arm, where only the release key is present. [7]
- The declaring set for the two atomic-series keys is exactly `lifecycle_finalize_task`. [8]
- `task_doc`'s `read_steps` validates and returns the authored units. [9]
- The registered description and the refusal name the same `kind` vocabulary. [10]
- Every `next_tool=` literal the lifecycle package passes is declared on the response model. [11]
- The `sprint-owner-required` refusal is a typed payload, driven through the real tool. [12]
- A queued operator post must still report `entryId`, `state`, `messageKind`, `deliveryState`. [13]
- `session_retire` reports the stranded row after the seat is already gone. [14]
- The structural delivery projection is declared on the shared base every consumer inherits. [15]
- The lane row that keeps this module in the default lane. [16]
- The choke point whose guarantee this module moves into the suite. [17]
- The registry whose models the structural layer sweeps. [18]
- The advertised public roster the surface layer checks against. [19]

### Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

No repository or external-system boundary is proved by this module.
