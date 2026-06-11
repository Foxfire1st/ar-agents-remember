# Task: Pydantic Tool Response Contracts

**Status:** inProgress
**Repo:** agents-remember
**Type:** Code
**Created:** 2026-05-28T16:53

---

## Reframing

Surface request: add Pydantic response models and use them to fix the oversized `context_packet` contract, starting from an explicit task plan with nine implementation sections.

Deeper objective: make MCP tool responses inspectable, versioned, testable, and bounded so agents can trust tool output shape without reverse-engineering loose dictionaries.

Highest-leverage framing: introduce a model-owned public response layer under `mcp/src/agents_remember/models/`, then refactor controllers and provider status projection so `context_packet` is a compact bootstrap contract and detailed provider diagnostics live behind a dedicated `provider_diagnostics` tool.

---

## Objective

Introduce explicit Pydantic models for Agents Remember MCP tool responses, beginning with `context_packet` and provider status. Use those models to shrink `context_packet`, remove duplicate raw provider payloads, and make response contracts enforceable by runtime serialization and tests.

---

## Requirements

- Add Pydantic as a first-class MCP package dependency and document the project expectation that public tool responses serialize through named models.
- Create model files under `mcp/src/agents_remember/models/`; this is the package path for the requested `agents_remember/models` folder.
- Define a compact `ContextPacketV2` contract that removes duplicate `pathRules`, removes `rawStatus`, and keeps provider data to up/runtime/identity/capability/target readiness.
- Keep detailed provider diagnostics available through a dedicated `provider_diagnostics` tool call, not through `context_packet`.
- Continue emitting a compact provider summary in `context_packet`; this summary should be projected from provider status/current-state facts rather than embedding the provider raw status payload.
- Emit a `tokens` field on every modeled tool response, calculated from the serialized response payload.
- Use token budgets rather than byte or KB budgets so Agents Remember overhead can be measured in the same unit that affects model context.
- Leave room for a later logging mode that records token cost across a session or bounded task, especially for benchmarks that need to separate Agents Remember tool cost from other prompt/context tokens.
- Add quality rules that keep public response schemas honest through Pydantic validation, schema tests, token-budget tests, and fixture coverage.
- Refactor and consolidate existing loose-dict builders before wiring models where needed, especially provider status projection and context packet composition.
- Run the full repository code quality wrapper before closeout.
- Update onboarding after implementation so future agents know the response-contract model and the context/detail tool boundary.

---

## Assumptions

- Use Pydantic v2.
- Keep MCP tool functions returning plain JSON-compatible dictionaries at the transport boundary, but require those dictionaries to be produced from Pydantic models.
- Introduce `contextPacketVersion: 2` and make V2 the active context packet contract.
- Do not preserve the oversized v1 packet as a compatibility output; v1 is considered unusable because it can quickly fill context windows and degrade model quality.
- Define provider diagnostics as a dedicated tool contract with its own model shapes during S2.
- Token counts should always be emitted, even before full session/task logging exists.
- Avoid defensive compatibility layers unless a real caller is identified; the package is still evolving and the goal is a clean contract.

---

## Invariants And Non-Goals

- Detailed provider diagnostics move behind a dedicated diagnostics tool; provider readiness in normal context remains compact.
- `context_packet` remains the fast startup/bootstrap surface.
- Provider checks may write the current provider state file as they do today, but the context packet should only include a path and compact summary.
- No source file above the repo's size thresholds should receive new feature logic without extraction or a specific justification.
- This task does not redesign provider lifecycle, indexing semantics, or provider startup behavior beyond response shaping.

---

## Evidence And Validation Plan

- Repo-internal evidence: inspect `controllers/context_packet.py`, `providers/status.py`, `providers/current_state.py`, `mcp/tools.py`, `mcp/server.py`, current tests, and package metadata.
- Contract evidence: Pydantic schemas generated from models match intended public response structures.
- Runtime evidence: MCP tool handlers serialize model instances through `model_dump(mode="json", exclude_none=True)` or an agreed equivalent.
- Regression evidence: tests cover ready, degraded/failed, no-provider, skipped-provider, inactive worktree, and drift-not-checked/checked cases.
- Budget evidence: normal ready-state `context_packet` response stays below an agreed token threshold and contains no `rawStatus`.
- Token evidence: every modeled tool response includes a calculated `tokens` field so later logging can aggregate tool overhead by session or task.

## Implementation Steps

### S1 - Install And Configure Pydantic

- [x] Add and verify the Pydantic dependency.
  - [x] Add `pydantic>=2,<3` or a more precise v2 range to `mcp/pyproject.toml`.
  - [x] Verify package import behavior under the existing test environment.
  - [x] Record any packaging or dependency-lock follow-up if the project uses generated lock artifacts elsewhere.
  - [x] Verification: focused test/import check proves the dependency is available from the MCP package.

### S2 - Create Model Files

- [x] Create the `agents_remember.models` package and complete public tool response model inventory.
  - [x] Add `mcp/src/agents_remember/models/__init__.py`.
  - [x] Add shared primitives for strict model configuration, JSON dumping, token metadata, status enums or literals, and common path/string fields.
  - [x] Add context packet models, provider summary models, dedicated provider diagnostics models, drift summary models, worktree summary models, and tool envelope helpers where useful.
  - [x] Define the common token metadata fields shared by all modeled tool responses.
  - [x] Add core/server response models for `ping` and `server_info`.
  - [x] Add runtime/coordination response models for `runtime_install` and `resolve_context`.
  - [x] Add memory/onboarding response models for `drift_check`, `memory_quality_check`, `route_index_refresh`, `memory_init`, `memory_baseline_status`, `memory_baseline_adopt`, `memory_carryover_plan`, and `memory_carryover_apply`.
  - [x] Add skill-install response model for `skills_install`.
  - [x] Add provider response models for `provider_status`, `provider_diagnostics`, `provider_watchers`, `grepai_search`, `grepai_trace`, `cgc_symbol_search`, `cgc_callers`, `cgc_callees`, `cgc_dependencies`, `cgc_complexity`, and `cgc_visualize`.
  - [x] Add worktree/direct-closeout response models for `worktree_start`, `worktree_attach`, `worktree_status`, `worktree_closeout_preview`, `worktree_closeout_apply`, `direct_closeout_preview`, `direct_closeout_apply`, `worktree_integrate`, and `worktree_cleanup`.
  - [x] Add benchmark response models for `codex_benchmark_prepare` and `codex_benchmark_run`.
  - [x] Add a public tool-to-response-model registry that accounts for every `PUBLIC_TOOLS` entry.
  - [x] Verification: schema-generation tests can import every public model, produce JSON Schema, and prove every public MCP tool has a declared response model.

### S3 - Refactor And Consolidate Before Wiring Models

- [x] Consolidate loose response-building code into clean projection boundaries.
  - [x] Split provider status into raw lifecycle result, current-state projection, context provider summary, and dedicated provider diagnostics projection.
  - [x] Remove exact duplication between provider `items[*].rawStatus` and parent raw lifecycle results.
  - [x] Remove top-level `pathRules` from the new context packet shape and keep `memory.storage.pathRules` as the single authoritative field.
  - [x] Inspect large files before edits; avoid adding feature logic to `controllers/skill_tools.py` or `mcp/tools.py` if extraction is the clearer boundary.
  - [x] Verification: existing behavior is preserved for detail/status tools while the context projection becomes compact.

### S4 - Wire Pydantic Models Into Tool Responses

- [x] Serialize all public MCP tool responses from Pydantic models.
  - [x] Update `context_packet` to return `ContextPacketV2` data.
  - [x] Add or prepare the dedicated provider diagnostics tool response contract for detailed/raw provider state.
  - [x] Keep provider readiness summaries compact in context-facing responses.
  - [x] Wire remaining public tool payloads through their declared response model classes.
  - [x] Keep MCP transport handlers thin: they call controllers, receive model-backed payloads, and return JSON-compatible dictionaries.
  - [x] Update CLI output for `context_packet` to use the same modeled serialization path.
  - [x] Verification: tool handler tests confirm response dictionaries conform to the models.

### S5 - Define Contract Quality Rules

- [ ] Add enforceable response-contract rules after the refactor and model wiring exist.
  - [ ] Require public MCP response models to use explicit fields and forbid unknown fields unless a raw/detail model intentionally allows provider-native payloads.
  - [ ] For modeled tool responses, do not rely on Pydantic nested dict coercion. Construct nested model instances explicitly, or call `NestedModel.model_validate(raw_payload)` at a narrow adapter boundary when the input is intentionally raw provider/controller data.
  - [ ] Define serialization rules for omitting `None`, preserving version fields, and keeping transport output JSON-compatible.
  - [ ] Add tests that reject `rawStatus` and duplicate path-rule fields in `ContextPacketV2`.
  - [ ] Define where token-budget and token-metadata tests belong after response wiring.
  - [ ] Verification: tests fail if response builders bypass the agreed model shape.

### S6 - Wire Token Accounting After Modeled Responses

- [ ] Add calculated token metadata to modeled response serialization after the final response shape is wired.
  - [ ] Route modeled tool responses through `response_payload(...)` or the final agreed equivalent.
  - [ ] Ensure `tokens`, `tokenizer`, and `tokenCountExact` are calculated from the final JSON-compatible payload, including token metadata fields.
  - [ ] Add a normal ready-state token-budget check for `ContextPacketV2`.
  - [ ] Add tests that every modeled tool response includes calculated token metadata.
  - [ ] Keep session/task logging out of this slice except for any minimal hook needed to avoid rewrites later.
  - [ ] Verification: token metadata is stable, present on modeled tool responses, and budget tests use token counts rather than byte counts.

### S7 - Test Coverage

- [ ] Expand focused tests around model contracts and response behavior.
  - [ ] Update `mcp/tests/test_context_packet.py` for `ContextPacketV2`.
  - [ ] Update provider status/current-state tests to distinguish summary contracts from dedicated diagnostics/raw contracts.
  - [ ] Add schema tests for `agents_remember.models`.
  - [ ] Add fixture tests for ready, degraded/failed, no providers, provider skipped, active/inactive worktree, and drift checked/not checked.
  - [ ] Verification: focused pytest runs pass for context packet, provider status, current state, tools, and schema tests.

### S8 - Run Full Code Quality Suite

- [ ] Run the repository-owned quality suite and resolve in-scope findings.
  - [ ] Run focused Ruff/Pyright/pytest/Radon checks during implementation as needed.
  - [ ] Run `python -m agents_remember.code_quality.check` from the source repo root before closeout.
  - [ ] Record Ruff, Pyright, pytest, coverage, Radon, and CRAP-Calculator results in the task notes or final handoff.
  - [ ] Verification: full wrapper completes, or exact blockers and closest equivalent checks are recorded.

### S9 - Onboarding Updates

- [ ] Update onboarding for the new model-owned response contract.
  - [x] Refresh onboarding for new/changed model files.
  - [x] Refresh onboarding for changed controller/provider/MCP tool files.
  - [x] Update the root overview feature inventory or related overview notes if the public tool contract changes.
  - [x] Run route index refresh if onboarding/index files need regeneration.
  - [ ] Verification: drift and memory quality checks are clean or any actionable follow-up is recorded.

---

## Proposed Code Examples

### E1 - Strict Public Response Model

Distinct change covered: the new model layer should make public response fields explicit and reject accidental shape drift.

Why this example is included: this is the core contract enforcement mechanism, and it shows why Pydantic is more than a typing convenience.

```python
from typing import Literal

from pydantic import BaseModel, ConfigDict


class StrictResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RepoSummary(StrictResponseModel):
    id: str
    root: str
    branch: str
    head: str
    dirty: bool
    state: Literal["available", "detached", "unavailable"]
```

### E2 - Compact Context Packet Provider Summary

Distinct change covered: `context_packet` should include provider readiness, runtime, identity, and target repo availability, not detailed raw diagnostics.

Why this example is included: this is the response-shape change that directly fixes the 1,813-line context packet.

```python
class ProviderIdentity(StrictResponseModel):
    scope: str
    instanceId: str


class ContextProviderItem(StrictResponseModel):
    id: str
    capability: Literal["semantic-memory-search", "code-relationship-search"]
    state: Literal["ready", "degraded", "failed", "disabled", "unknown"]
    ok: bool | None
    runtime: Literal["docker", "local", "unknown"]
    identity: ProviderIdentity
    watchers: GrepAIWatcherState | list[CGCWatcherState] | None = None
    targetRepo: dict[str, object] | None = None
```

### E3 - Dedicated Diagnostics Tool Keeps Raw State Out Of Context Packet

Distinct change covered: detailed provider diagnostics remain available, but through a dedicated diagnostics response model rather than embedded context packet duplication.

Why this example is included: it preserves troubleshooting value without forcing every startup context call to pay the token cost.

```python
class ProviderRawStatus(FlexibleResponseModel):
    provider: str
    action: str
    ok: bool | None = None


class ProviderDiagnosticsItem(StrictResponseModel):
    id: str
    state: ProviderState | str = "unknown"
    ok: bool | None = None
    rawStatus: ProviderRawStatus | None = None


class ProviderDiagnosticsResponse(ToolResponse):
    operation: Literal["provider_diagnostics"] = "provider_diagnostics"
    items: list[ProviderDiagnosticsItem]
    rawStatus: ProviderRawStatus | None = None
```

### E4 - Controller Serializes Through Models

Distinct change covered: controllers can still return MCP-friendly dictionaries, but the dictionary should come from a validated model.

Why this example is included: it shows the intended boundary between application code, model validation, and MCP transport.

```python
packet = ContextPacketV2(
    ok=repo.state in {"available", "detached"},
    operation="context_packet",
    contextPacketVersion=2,
    repo=repo_summary,
    paths=paths,
    memory=memory_summary,
    worktree=worktree_summary,
    providers=provider_summary,
    drift=drift_summary,
)
return packet.model_dump(mode="json", exclude_none=True)
```

### E5 - Token Field On Every Tool Response

Distinct change covered: every modeled tool response emits a token cost for its serialized payload.

Why this example is included: token budgets are the real context-window cost, and the same field can later feed session/task logging and benchmark cost attribution.

```python
class ToolResponse(StrictResponseModel):
    ok: bool
    operation: str
    tokens: int = 0
    tokenizer: str = ""
    tokenCountExact: bool = False


def response_payload(
    response: ToolResponse,
    *,
    token_counter: ResponseTokenCounter = DEFAULT_TOKEN_COUNTER,
) -> dict[str, object]:
    payload = response.model_dump(mode="json", exclude_none=True)
    payload["tokens"] = 0
    payload["tokenizer"] = token_counter.name
    payload["tokenCountExact"] = token_counter.exact
    _finalize_token_count(payload, token_counter=token_counter)
    return payload
```

---

## Decision Log

| Date-Time        | Decision | Rationale |
| ---------------- | -------- | --------- |
| 2026-05-28T16:53 | Use a light task workflow and stop before implementation. | The work needs a durable task file, explicit contract review, and an approval gate before source edits. |
| 2026-05-28T16:53 | Place response models under `mcp/src/agents_remember/models/`. | This is the importable package path matching the requested `agents_remember/models` concept. |
| 2026-05-28T16:53 | Treat detailed provider status as a separate contract from `context_packet`. | Startup context should be compact; provider internals belong in provider detail tools. |
| 2026-05-28T16:53 | Use Pydantic runtime validation plus schema/fixture tests to keep response structures honest. | Static typing alone cannot prove runtime MCP JSON shapes. |
| 2026-05-28T17:12 | Use a dedicated provider diagnostics tool for detailed provider state. | The context packet only needs provider up/runtime/identity facts; diagnostics should be requested explicitly. |
| 2026-05-28T17:12 | Use token budgets and always emit a `tokens` field on modeled tool responses. | Token counts map directly to context-window and benchmark overhead; later logging can aggregate the same field across sessions or tasks. |
| 2026-05-28T17:12 | Move forward with V2 only for `context_packet`. | V1 is unusably large and can degrade model quality by filling context windows too quickly. |
| 2026-05-28T17:22 | Approved implementation of S1 and S2 only. | Dependency setup and initial model definitions can proceed; controller wiring, contract quality rules, tests, full quality, and onboarding remain later steps. |
| 2026-05-28T17:22 | Added Pydantic to both MCP package metadata and MCP requirements. | `mcp/pyproject.toml` owns packaging, while `mcp/requirements.txt` is the local requirements mirror for MCP runtime setup. No generated lock artifact was found. |
| 2026-05-28T17:22 | Created initial response model package without wiring controllers. | This satisfies S2 while preserving the approved boundary that behavior changes begin in later steps. |
| 2026-05-28T17:24 | Keep the checkout MCP SDK at `mcp==1.27.1`. | The environment was already working with 1.27.1; the stale `mcp/requirements.txt` pin to 1.12.4 caused an accidental downgrade during dependency install and should not be repeated. |
| 2026-05-28T17:26 | Replace free-form provider `watcherState` with typed watcher shapes. | `watcherState: str` hid the distinction between one GrepAI watcher and per-repo CGC watchers; `GrepAIWatcherState | list[CGCWatcherState]` makes the contract self-explanatory. |
| 2026-05-28T17:28 | Tighten worktree status fields to literals where the lifecycle already has closed vocabularies. | Worktree status, memory mode, review/closeout/integration/cleanup states, phase, next operation, and next tool are contract values, not arbitrary strings. |
| 2026-05-28T18:04 | Use `tiktoken:o200k_base` as the default response token counter and expose counter metadata. | Token budget reporting needs a concrete tokenizer name and exactness flag; an explicit approximate counter remains available for non-exact modes. |
| 2026-05-28T18:16 | Add a dedicated public `provider_diagnostics` tool for detailed provider state. | Detailed provider troubleshooting remains available without forcing every bootstrap `context_packet` call to carry raw provider payloads. |
| 2026-05-28T18:16 | Preserve a compact provider summary in `context_packet`. | Agents still need up/runtime/identity/capability/target readiness during bootstrap; only detailed raw diagnostics move out of the packet. |
| 2026-05-28T18:23 | Move token-counter wiring to its own step after model wiring. | Token counts should be calculated after modeled responses are fully wired, so the measured payload is the final tool response shape. |
| 2026-05-28T18:26 | Move contract quality rules after refactor and model wiring. | The rules are more meaningful once the actual projection boundaries and modeled tool responses exist. |
| 2026-05-28T18:27 | Keep token accounting after contract-quality rules. | Token metadata tests depend on both final modeled payloads and the response-contract rules that define allowed serialization. |
| 2026-05-28T18:39 | Keep `provider_status` as the compact provider summary tool and add `provider_diagnostics` for raw detail. | The model-facing status path should be cheap and predictable; raw lifecycle/current-state payloads remain available through an explicitly named diagnostics tool. |
| 2026-05-28T19:12 | Extract worktree/direct-closeout tool controllers from `skill_tools.py` into `worktree_tools.py`. | `skill_tools.py` was above the repo soft limit and was a refactor target; a facade extraction preserves public tool imports while moving a coherent worktree responsibility to its own controller module. |
| 2026-05-28T19:25 | Extract provider-facing tool controllers from `skill_tools.py` into `provider_tools.py`. | Provider status, diagnostics, watcher lifecycle, GrepAI, and CGC tools share the provider lifecycle boundary; keeping them in one controller module removes mixed responsibilities from `skill_tools.py` without changing public MCP tool wiring. |
| 2026-05-28T19:34 | Extract memory-facing and benchmark-facing tool controllers from `skill_tools.py`. | Memory quality, drift, route indexes, memory init, baseline, and carryover share the memory/onboarding layer; Codex benchmark execution is its own external execution boundary. Both are clearer as named controller modules behind the stable facade. |
| 2026-05-28T19:40 | Wire `mcp/tools.py` directly to owning controller modules and stop using `skill_tools.py` as a mass facade. | The facade was only a temporary extraction bridge. Public MCP payload builders should import controller functions from their real responsibility modules; `skill_tools.py` now only owns `skills_install_tool`, and coordination-context resolution lives in `coordination_tools.py`. |
| 2026-05-28T19:42 | S2 must cover every public MCP tool, not only context/provider first-wave models. | A model-owned response contract is incomplete unless the inventory accounts for all 36 `PUBLIC_TOOLS` entries. Stable tool surfaces get stricter models; provider-native and lower-level pass-through tools get explicit flexible envelopes until their payloads are normalized in S4/S5. |
| 2026-05-28T19:48 | Validate every public MCP payload builder through the response-model registry. | S4 should enforce the declared model inventory at the MCP payload boundary while preserving controller behavior. A single `_tool_payload(...)` adapter keeps transport wiring thin and makes bypasses easy to detect. |

---

## Open Questions

- What token budget should `ContextPacketV2` enforce for a normal provider-ready state? The budget should be set during implementation after the first modeled packet fixture exists.

---

## Progress Notes

- 2026-05-28T17:22: Completed S1 and S2. Focused verification passed: Pydantic import/schema generation, sample modeled payload token calculation, Ruff check, and Ruff format check for `mcp/src/agents_remember/models`.
- 2026-05-28T17:24: Restored checkout `.venv` to `mcp==1.27.1` after an accidental downgrade from installing the stale requirements pin. Updated `mcp/requirements.txt` to pin 1.27.1.
- 2026-05-28T17:26: Refined provider model watcher typing after review: provider summaries now use typed GrepAI and CGC watcher models instead of a free-form `watcherState` string.
- 2026-05-28T17:28: Refined worktree model typing after review: closed worktree lifecycle fields now use `Literal` aliases instead of broad `str`.
- 2026-05-28T18:04: Added the S2 token response boundary as `agents_remember.models.tokens.response_payload(...)`. This is an Agents Remember helper, not an MCP dependency override. It serializes Pydantic tool responses, writes `tokens`, `tokenizer`, and `tokenCountExact`, and stabilizes the count after token metadata is present.
- 2026-05-28T18:04: Added `tiktoken` as the preferred token counting dependency with a default `tiktoken:o200k_base` counter. Kept an explicit approximate counter class for later non-exact or non-tiktoken accounting modes.
- 2026-05-28T18:04: Verified the repo venv has `mcp 1.27.1`, `pydantic 2.13.4`, and `tiktoken 0.13.0`; focused model Ruff checks and schema generation pass.
- 2026-05-28T18:16: Confirmed the public response boundary: `context_packet` emits a compact provider summary, while detailed provider troubleshooting data is requested through a dedicated `provider_diagnostics` tool.
- 2026-05-28T18:23: Reordered the plan so token-counter wiring is S6; test coverage, full quality, and onboarding are now S7, S8, and S9.
- 2026-05-28T18:26: Reordered contract quality rules to S5, after refactor and model wiring. Refactor is now S3 and model wiring is now S4.
- 2026-05-28T18:27: Cleaned up stale task wording after step reordering: nine sections, token-budget wording, and step-number references now match the current plan.
- 2026-05-28T18:39: Completed S3 and S4. `context_packet` now returns modeled V2 data with compact provider/worktree summaries, `provider_status` returns a modeled provider summary response, and `provider_diagnostics` exposes raw provider diagnostics. Focused Ruff, pytest, schema-generation, and Radon CC/MI checks pass for the touched response path.
- 2026-05-28T18:47: Follow-up S4 cleanup: `context_packet` now constructs nested response models explicitly instead of relying on Pydantic dict coercion, so Pylance and runtime validation agree on the controller boundary.
- 2026-05-28T18:47: Captured the no nested dict coercion rule in S5 and in repo-specific coding guidelines. For public response models, locally assembled nested fields should be explicit model instances; `model_validate(...)` is reserved for raw adapter/provider/controller payload boundaries.
- 2026-05-28T18:57: Added Pyright to the dev dependency set and the full quality wrapper without scoping it down. Full-project Pyright initially reported inherited baseline failures (`152 errors, 1 warning`), so the quality wrapper will surface those until the baseline is cleaned up.
- 2026-05-28T19:00: Fixed Pyright findings in touched files. `skill_tools.py` now narrows public `topology` strings before calling the typed resolver and correctly annotates carryover request construction; `test_tools.py` now narrows MCP fallback content to `TextContent` before reading `.text`. Focused Pyright for touched files is clean; full-project Pyright remains failing on inherited baseline issues (`144 errors, 1 warning`).
- 2026-05-28T19:12: Extracted worktree/direct-closeout tool controller functions into `mcp/src/agents_remember/controllers/worktree_tools.py` and kept `skill_tools.py` as the existing facade/import surface. `skill_tools.py` dropped from 1,237 lines to 960 lines; the new module is 317 lines. Focused verification passed: Ruff check, Ruff format check for touched source/test files, Pyright on touched files, `pytest mcp/tests/test_tools.py mcp/tests/test_worktree_support.py -q`, Radon CC/MI, and CRAP-Calculator. CRAP rollup has zero functions over threshold 30; max scores are `15.24` in `worktree_tools.py` and `14.72` in `skill_tools.py`.
- 2026-05-28T19:16: Ran the full repository quality wrapper after the worktree controller extraction. `ruff` passed, full pytest passed (`234 passed, 3 skipped`), Radon reported existing complexity pressure, and CRAP-Calculator reported eight inherited threshold rows. The wrapper still exits non-zero because full-project Pyright reports the known inherited baseline (`144 errors, 1 warning`); no focused touched-file Pyright errors remain.
- 2026-05-28T19:25: Extracted provider-facing controller functions into `mcp/src/agents_remember/controllers/provider_tools.py` and kept `skill_tools.py` as the existing facade/import surface. `skill_tools.py` dropped from 960 lines to 444 lines; `provider_tools.py` is 568 lines. Focused verification passed: Ruff check, Ruff format check, Pyright on touched files, `pytest mcp/tests/test_tools.py -q`, Radon CC/MI, and CRAP-Calculator. The moved provider lifecycle test now patches `agents_remember.controllers.provider_tools.lifecycle_service.run_watchers_lifecycle`, matching the new implementation boundary. Focused CRAP rollup has zero functions over threshold 30; max scores are `15.24` in `worktree_tools.py`, `14.72` in `skill_tools.py`, and `14.08` in `provider_tools.py`.
- 2026-05-28T19:34: Extracted memory-facing controller functions into `mcp/src/agents_remember/controllers/memory_tools.py` and benchmark-facing controller functions into `mcp/src/agents_remember/controllers/benchmark_tools.py`. `skill_tools.py` dropped from 444 lines to 135 lines and now acts mostly as a stable facade plus `resolve_context` and `skills_install`. Focused verification passed: Ruff check, Ruff format check, Pyright on touched files, `pytest mcp/tests/test_tools.py -q`, Radon CC/MI, and CRAP-Calculator. Focused CRAP rollup has zero functions over threshold 30; max scores are `15.24` in `worktree_tools.py`, `14.72` in `skill_tools.py`, `14.08` in `provider_tools.py`, `9.03` in `benchmark_tools.py`, and `4.68` in `memory_tools.py`.
- 2026-05-28T19:39: Re-ran the full repository quality wrapper after all controller extractions. `ruff` passed, full pytest passed (`234 passed, 3 skipped`), Radon reported existing complexity pressure, and CRAP-Calculator reported eight inherited threshold rows. The wrapper still exits non-zero because full-project Pyright reports the known inherited baseline (`144 errors, 1 warning`); focused touched-file Pyright remains clean.
- 2026-05-28T19:40: Removed the temporary `skill_tools.py` mass re-export facade. `mcp/tools.py` now imports worktree, provider, memory, benchmark, coordination, context packet, runtime install, and skill-install controllers directly from their owning modules. `resolve_context_tool` moved into `mcp/src/agents_remember/controllers/coordination_tools.py`; `skill_tools.py` is now only 30 lines and only owns `skills_install_tool`. Updated the provider workflow integration test import to use `worktree_tools.py` directly and fixed local helper typing so focused Pyright stays clean.
- 2026-05-28T19:40: Direct-wiring verification passed: focused Ruff check, Ruff format check, focused Pyright (`0 errors, 0 warnings`), `pytest mcp/tests/test_tools.py mcp/tests/test_provider_workflow_integration.py -q` (`25 passed, 3 skipped, 6 subtests passed`), Radon CC/MI on touched controller/tool files, focused controller coverage (`71%` total), and focused controller CRAP (`0` functions over threshold 30; `skill_tools.py` max CRAP `2.00`).
- 2026-05-28T19:40: Re-ran the full repository quality wrapper after direct controller wiring. `ruff` passed and full pytest passed (`234 passed, 3 skipped`). The wrapper still exits non-zero because full-project Pyright reports the inherited baseline, now `111 errors, 1 warning`; CRAP-Calculator remains report-only and still reports eight inherited threshold rows.
- 2026-05-28T19:42: Returned to S2 and completed the full public tool response model inventory. Added model modules for core/server, runtime/coordination, memory/onboarding, skill install, benchmarks, and a public tool response registry. Extended provider and worktree model modules with response classes for every provider-native and worktree/direct-closeout tool. Added `mcp/tests/test_models.py` to prove every `PUBLIC_TOOLS` entry has a declared response model and each model generates JSON Schema.
- 2026-05-28T19:42: S2 verification passed: Ruff check, Ruff format check, focused Pyright (`0 errors, 0 warnings`), `pytest mcp/tests/test_models.py mcp/tests/test_context_packet.py mcp/tests/test_tools.py -q` (`33 passed, 2 skipped, 42 subtests passed`), and full pytest (`236 passed, 3 skipped, 48 subtests passed`). S4 is now explicitly reopened for wiring the remaining public tool payloads through these declared models.
- 2026-05-28T19:48: Completed S4 after the full S2 inventory. `mcp/tools.py` now routes every public payload builder through `_tool_payload(tool_name, payload)`, which validates against `PUBLIC_TOOL_RESPONSE_MODELS[tool_name]` and serializes with `model_dump(mode="json", exclude_none=True)`. A scan for non-adapter returns in payload builders found only the helper return itself. Existing controller behavior remains unchanged; the model check sits at the MCP payload boundary.
- 2026-05-28T19:48: S4 verification passed: Ruff check, Ruff format check, focused Pyright (`0 errors, 0 warnings`), `pytest mcp/tests/test_models.py mcp/tests/test_context_packet.py mcp/tests/test_tools.py -q` (`33 passed, 2 skipped, 42 subtests passed`), and full pytest (`236 passed, 3 skipped, 48 subtests passed`). `ping_payload` exact-output test was updated to account for the shared model metadata defaults.
- 2026-05-28T19:52: Refreshed onboarding for the response-contract model package, split MCP controller modules, compact context/provider status boundary, provider diagnostics tool, Pyright quality wiring, dependency files, and affected tests. Route index refresh wrote new `controllers` and `models` route indexes plus parent index updates across 17 route overviews; a second refresh after adding `controllers/__init__.py.md` wrote the controllers index only. Missing-onboarding check passed for current additions (`sourceCount=20`, `missingCount=0`). Full drift/memory-quality verification remains for closeout because source changes are still uncommitted and verification metadata is provisional.

---

## References

- `/home/mohamedreadone/Projects/agents-remember/context-packet.json`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/context_packet.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/benchmark_tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/coordination_tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/memory_tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/provider_tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/skill_tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/models/benchmarks.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/models/core.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/models/memory.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/models/runtime.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/models/skills.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/models/tool_registry.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/providers/status.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/providers/current_state.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/mcp/tools.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/src/agents_remember/mcp/server.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/tests/test_context_packet.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/tests/test_models.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/tests/test_provider_current_state.py`
- `/home/mohamedreadone/Projects/agents-remember/mcp/tests/test_provider_workflow_integration.py`
- `/home/mohamedreadone/Projects/ar-coordination/memory-repos/ar-agents-remember/system/tools.md`
- Drift gate before planning: `actionableCount=0`, report `/home/mohamedreadone/Projects/ar-coordination/temp/drift-reports/agents-remember/agents-remember_main_drift-report.md`
