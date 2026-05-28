# Handover: Pydantic Tool Response Contracts

**Task:** `260528_pydantic-tool-response-contracts`  
**Repo:** `agents-remember-md`  
**Written:** 2026-05-28T20:04+02:00  
**Source baseline used for provisional onboarding metadata:** `9680d150ac9d2e6c1ae04dbab42eac0088dceef8`

## Current State

S1 through S4 are implemented. S9 onboarding was refreshed for the work done so
far, but its final verification checkbox remains open because source changes
are still uncommitted and onboarding verification metadata is provisional.

Remaining implementation sections are S5 through S8, plus final S9
closeout-quality verification:

- S5: enforceable contract quality rules.
- S6: wire calculated token metadata through the final response serialization.
- S7: broader fixture/test coverage.
- S8: full repository quality wrapper and in-scope remediation.
- S9: final drift/memory-quality verification after source state is settled.

## Completed Work

### Dependency And Tooling Setup

- Added `pydantic>=2,<3` as an MCP runtime dependency.
- Added `tiktoken>=0.12,<1` for response token accounting.
- Restored the local MCP dependency to `mcp==1.27.1` in `mcp/requirements.txt`
  after the stale pin caused an accidental downgrade during installation.
- Added `pyright>=1.1,<2` to the MCP dev dependency group.
- Added root `[tool.pyright]` config covering `mcp/src/agents_remember` and
  `mcp/tests`.
- Added Pyright to the source quality wrapper in
  `mcp/src/agents_remember/code_quality/check.py`.
- Updated source checkout instructions and memory-layer tooling docs to include
  Pyright.

### Response Model Package

Created `mcp/src/agents_remember/models/` as the public response-contract model
package.

Key modules:

- `base.py`: strict/flexible response base classes, shared response token
  metadata fields, `ToolResponse`.
- `tokens.py`: token counter protocol, `TiktokenTokenCounter`,
  `ApproximateTokenCounter`, `response_payload(...)`, and token-count
  stabilization.
- `context_packet.py`: compact `ContextPacketV2` and nested repo/path/memory
  summaries.
- `providers.py`: compact provider summary, typed GrepAI/CGC watcher state,
  provider diagnostics, provider watcher, GrepAI, and CGC response models.
- `worktree.py`: worktree context summary and worktree/direct-closeout response
  models.
- `memory.py`, `runtime.py`, `skills.py`, `benchmarks.py`, `core.py`,
  `drift.py`: response models for the rest of the public tool surface.
- `tool_registry.py`: `PUBLIC_TOOL_RESPONSE_MODELS` mapping all 36 public MCP
  tools to response model classes.
- `__init__.py`: explicit public exports for the model package.

Design choices now captured in code:

- Owned compact contracts should be strict and reject unknown fields.
- Provider/service-native detail payloads may use flexible envelopes only where
  intentional.
- `ContextPacketV2` is the active context packet contract; V1 is not preserved.
- Token metadata fields exist on modeled responses, but S6 still needs to wire
  calculated counts into the final MCP output path.

### Context Packet And Provider Split

`context_packet` is now compact V2:

- `contextPacketVersion` is `2`.
- Top-level duplicate `pathRules` were removed.
- `memory.storage.pathRules` is the single path-rules location.
- Embedded provider `rawStatus`, full `currentState`, and duplicate provider
  internals were removed from the context packet.
- Worktree `rawStatus` passthrough was removed.
- The packet includes a diagnostics hint pointing to `provider_diagnostics`.

Provider status now has two explicit surfaces:

- `provider_status`: compact modeled provider summary.
- `provider_diagnostics`: detailed/raw provider diagnostics, including
  current-state payloads, integrity details, process namespace, recovery
  actions, and raw lifecycle status.

Important behavior preserved:

- Provider status still runs the status/current-state path and writes the
  current provider state file.
- The context packet now projects that information into compact facts instead
  of embedding the raw tree.

### Controller Refactor

The old `controllers/skill_tools.py` mega-facade was split by domain.

New controller modules:

- `benchmark_tools.py`
- `coordination_tools.py`
- `memory_tools.py`
- `provider_tools.py`
- `worktree_tools.py`

Current intended boundary:

- `mcp/server.py` registers FastMCP tools.
- `mcp/tools.py` owns public payload builders and response-model validation.
- Controller modules own operation-level composition.
- Service modules own deterministic behavior.
- `skill_tools.py` now only owns `skills_install_tool`.

`mcp/tools.py` now imports domain controllers directly and routes every public
payload builder through:

```python
def _tool_payload(tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
    model = PUBLIC_TOOL_RESPONSE_MODELS[tool_name]
    return model.model_validate(payload).model_dump(mode="json", exclude_none=True)
```

A scan for public payload builders returning without `_tool_payload(...)` found
only the helper return itself.

### Contract And Typing Rules Captured So Far

- Provider watcher state is now typed as `GrepAIWatcherState` or
  `list[CGCWatcherState]` instead of a free-form `watcherState` string.
- Worktree state fields with closed vocabularies use `Literal` aliases.
- Locally assembled nested response-model fields should use explicit nested
  model instances.
- `NestedModel.model_validate(...)` is acceptable at narrow raw-adapter
  boundaries for provider/controller/service payloads.
- Avoid Pydantic nested dict coercion as the normal construction style for
  owned public contracts.

## Tests And Verification Already Run

Focused checks that passed during the task:

- Ruff check and Ruff format checks on touched model/controller/tool/test files.
- Focused Pyright on touched files after each extraction/wiring stage.
- `pytest mcp/tests/test_models.py mcp/tests/test_context_packet.py mcp/tests/test_tools.py -q`
  passed after the full S2 inventory and S4 model wiring.
- Full pytest passed after S4: `236 passed, 3 skipped, 48 subtests passed`.
- Radon CC/MI focused checks were run during controller extraction.
- Focused CRAP checks reported no over-threshold functions in the touched
  controller slices.

Full quality wrapper status:

- `ruff` passed.
- Full pytest passed.
- Full wrapper still exits non-zero because full-project Pyright has inherited
  baseline errors outside the immediate touched-file set.
- CRAP-Calculator remains report-only and still reports inherited threshold
  rows.

Do not treat the full wrapper as clean yet. S8 needs a fresh run and an exact
current report.

## Onboarding Updated

The onboarding pass added or refreshed memory for:

- New `models/` route overview and sidecars.
- New `controllers/` route overview and sidecars.
- `mcp/tools.py`, `mcp/server.py`, `context_packet.py`,
  `providers/status.py`, `worktrees/status.py`.
- Dependency/tooling files: root `pyproject.toml`, `mcp/pyproject.toml`,
  `mcp/requirements.txt`, `AGENTS.md`, quality wrapper sidecar.
- Affected tests including `test_models.py`, `test_tools.py`,
  `test_context_packet.py`, provider current-state/integrity tests, provider
  workflow integration, and code-quality wrapper tests.
- Root feature inventory for public MCP response contracts, compact
  `ContextPacketV2`, and `provider_diagnostics`.

Route index refresh:

- Refreshed 17 route overviews.
- Added `mcp/src/agents_remember/controllers/overview.index.json`.
- Added `mcp/src/agents_remember/models/overview.index.json`.
- Updated parent/root indexes as needed.
- Final missing-onboarding check: `sourceCount=20`, `missingCount=0`.

Full drift/memory-quality verification remains open because the source changes
are not committed and sidecar metadata is provisional.

## Known Dirty Source Files

Current source changes include:

- `AGENTS.md`
- `pyproject.toml`
- `mcp/pyproject.toml`
- `mcp/requirements.txt`
- `mcp/src/agents_remember/code_quality/check.py`
- `mcp/src/agents_remember/controllers/context_packet.py`
- `mcp/src/agents_remember/controllers/skill_tools.py`
- `mcp/src/agents_remember/controllers/benchmark_tools.py`
- `mcp/src/agents_remember/controllers/coordination_tools.py`
- `mcp/src/agents_remember/controllers/memory_tools.py`
- `mcp/src/agents_remember/controllers/provider_tools.py`
- `mcp/src/agents_remember/controllers/worktree_tools.py`
- `mcp/src/agents_remember/mcp/server.py`
- `mcp/src/agents_remember/mcp/tools.py`
- `mcp/src/agents_remember/models/`
- `mcp/src/agents_remember/providers/status.py`
- `mcp/src/agents_remember/worktrees/status.py`
- `mcp/tests/test_code_quality_check.py`
- `mcp/tests/test_context_packet.py`
- `mcp/tests/test_integrity.py`
- `mcp/tests/test_models.py`
- `mcp/tests/test_provider_current_state.py`
- `mcp/tests/test_provider_workflow_integration.py`
- `mcp/tests/test_tools.py`

`context-packet.json` exists at the repo root as a user-created sample output.
It should not be deleted unless the developer explicitly asks for cleanup.

## Remaining Work Guidance

### S5 Contract Quality Rules

Recommended next checks:

- Add tests that public response models default to strict extras unless a model
  intentionally inherits from a flexible base.
- Add tests that `ContextPacketV2` rejects `rawStatus` and top-level
  `pathRules`.
- Add tests that public payload builders cannot bypass `_tool_payload(...)`.
- Decide whether the enforcement should be a static AST scan, a focused unit
  test over public builder functions, or both.
- Keep the no nested dict coercion rule in tests where practical: local
  response construction should instantiate nested models explicitly, while raw
  provider/service payloads should be validated at adapter boundaries.

### S6 Token Accounting

Current code has token helpers but does not yet use them in `_tool_payload(...)`.

Likely implementation path:

- Change `_tool_payload(...)` to validate to the declared model class, then
  serialize through `response_payload(...)` for `ToolResponse`-style models.
- Consider adding a protocol/base method if flexible response envelopes need
  the same token path.
- Ensure token counting happens after `exclude_none=True` final shape is known.
- Add tests that every public payload emits calculated `tokens`, `tokenizer`,
  and `tokenCountExact`.
- Add a token-budget test for a normal ready-state `ContextPacketV2`.

### S7 Test Coverage

Add broader fixtures for:

- ready provider state,
- degraded/failed provider state,
- no providers,
- skipped provider summary,
- inactive worktree,
- active worktree,
- drift checked,
- drift not checked,
- diagnostics raw detail remains available outside context.

### S8 Full Quality

Run the repository-owned wrapper again from the source repo:

```bash
PYTHONPATH=mcp/src ./.venv/bin/python -m agents_remember.code_quality.check
```

Expect full-project Pyright baseline errors unless they are cleaned up first.
Record exact current counts in the task file. Do not silently scope the full
quality wrapper down.

## Potential Investigation: TOON Response Rendering

There is a promising follow-up investigation around rendering some tool
responses as TOON or another compact agent-readable notation at the response
boundary.

Problem:

- JSON is precise and machine-friendly, but large nested tool responses can be
  hard for agents to scan and can waste tokens through repeated punctuation and
  keys.
- The original `context_packet` showed that raw JSON shape can become costly
  fast.
- Pydantic gives us stable models, which makes alternate renderers more
  plausible because field order and public schemas are now explicit.

Important constraint:

- Do not replace JSON blindly. MCP clients, tests, and scripts may expect
  structured JSON dictionaries from tool calls.
- Any TOON rendering should be an explicit presentation mode, not a silent
  transport-breaking change.

Investigation questions:

- Does the MCP Python SDK/tool transport support returning alternate content
  types or text content while preserving structured output?
- Should tools expose a `format` or `render` option, or should the server choose
  JSON versus TOON based on a model-facing hint?
- Which tools benefit most: `context_packet`, `provider_diagnostics`,
  `memory_quality_check`, and route/drift summaries are likely first candidates.
- Can Pydantic JSON Schema drive a generic TOON renderer without hand-written
  per-tool formatting?
- Can a rendered TOON response stay round-trippable enough for agents, or is it
  purely for human/agent reading while JSON remains the canonical payload?
- How do token counts compare across canonical JSON, compact JSON, and TOON for
  ready-state and degraded-state fixtures?

Possible technical shape:

1. Keep `model_dump(mode="json", exclude_none=True)` as canonical structured
   output.
2. Add a renderer layer after model validation and token calculation:

   ```python
   payload = response_payload(model)
   if render == "toon":
       return {
           "ok": payload["ok"],
           "operation": payload.get("operation"),
           "tokens": payload["tokens"],
           "tokenizer": payload["tokenizer"],
           "tokenCountExact": payload["tokenCountExact"],
           "format": "toon",
           "body": render_toon(payload),
       }
   return payload
   ```

3. Measure token budgets for JSON and TOON with the same `tiktoken` counter.
4. Keep TOON out of raw provider-native payloads until there is a clear mapping
   for nested arbitrary provider output.

Recommendation:

- Treat TOON as a separate investigation task after S6 token accounting lands.
- Start with measurement fixtures before changing any public tool behavior.
- Prefer an explicit output/presentation mode over changing default MCP return
  shapes.

## Next Suggested Action

Proceed with S5. The code already has the model registry and response boundary
needed to make contract quality tests meaningful.
