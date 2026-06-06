# test_tool_response_conformance.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember-md                                 |
| path                   | `mcp/tests/test_tool_response_conformance.py`      |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-06T12:28+02:00                             |
| lastVerifiedCommitHash | `11f28a2035f06f8bc33f11b0617b41cda1122c1f`         |
| lastVerifiedCommitDate | 2026-06-06T13:01:33+02:00|
| governingOverview      | `overview.md`                                      |

## Purpose

`test_tool_response_conformance.py` moves the production response-contract
guarantee into the test suite: every public MCP tool produces a payload that
conforms to its registered Pydantic response model, so controller drift is caught
at dev time instead of in a live tool call.

## Code Commentary

### Logic

Production already validates each tool payload through
`tools._tool_payload()` against `models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`
(strict models use `extra="forbid"`). These tests reproduce that guarantee by
obtaining a *representative* payload for every public tool from the real
`*_payload` builder, then asserting conformance.

`setUpClass` builds four temporary fixtures (each in its own temp dir) and
collects one representative payload per tool into `cls.payloads`:

- `_base_fixture` / `_simple_payloads`: a code repo, memory layer, and
  `.codex/mcp` settings drive the 25 tools that run directly (core, context,
  runtime, memory, skills, provider status/diagnostics/watchers, GrepAI/CGC
  dry-run, baseline, benchmarks).
- `_worktree_payloads`: a real worktree lifecycle in disabled-memory mode
  produces `worktree_start`, `worktree_status`, `worktree_attach`,
  `worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`,
  and `worktree_cleanup` against a real contract.
- `_direct_closeout_payloads`: an external-memory direct-checkout fixture drives
  `direct_closeout_preview` and `direct_closeout_apply`.
- `_carryover_payloads`: a landed-branch fixture drives `memory_carryover_plan`
  and `memory_carryover_apply` (a docstring names the
  `c-11-memory-carryover-from-branch` skill).

`tearDownClass` removes the temp dirs with `shutil.rmtree(..., ignore_errors=True)`
because git worktrees leave read-only pack files that otherwise break cleanup on
Windows.

`test_every_public_tool_has_a_representative_payload` asserts the payload set
exactly covers the registry. `test_representative_payloads_conform_to_registered_models`
asserts, per tool, that the payload validates and that round-tripping
(`model_validate(...).model_dump(mode="json", exclude_none=True)`) fabricates no
keys. `test_strict_response_models_forbid_extra_fields` asserts the
strict/flexible split matches the response-model taxonomy.

### Conventions

Fixtures reuse helpers from `test_worktree_support` (`init_repo`, `commit_file`,
`git`, `initialized_memory_repo`, `write_file_onboarding`) and settings from
`test_config`. `_allowed_keys()` collects a model's field names plus any
aliases/serialization aliases.

The round-trip check is taxonomy-aware: strict models (not built on
`FlexibleResponseModel`) may emit only declared fields, while intentionally
flexible models (`extra="allow"`, e.g. provider-native command plans that carry an
undeclared `command` key by design) may also pass through keys present on the
input payload — so the assertion is "round trip invents no keys that are neither
declared nor part of the input."

### Invariants And Boundaries

- Prefer the real controller/`*_payload` builder for representative payloads; fall
  back to hand-built fixtures only where invoking the controller is impractical
  (currently none are needed — all 36 tools run for real).
- Strict response models must keep `extra="forbid"`; flexible models keep
  `extra="allow"`. The structural rule is `FlexibleResponseModel` membership.
- This is a dev-time conformance net; the runtime contract still lives in
  `_tool_payload()`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The registry maps each public tool to its response model. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| `_tool_payload()` is the production validation path mirrored here. | [base.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/base.py) |
| The strict/flexible response-model taxonomy lives in the model base. | [base.py](agents-remember-md/mcp/src/agents_remember/models/base.py) |
| Worktree/direct-closeout/carryover fixtures reuse worktree test helpers. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |
| Schema-level registry coverage is asserted separately. | [test_models.py](agents-remember-md/mcp/tests/test_models.py) |

## Update History

- 2026-06-06T12:28+02:00: Corrected the `_tool_payload()` reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-06-02T16:24+02:00: A docstring now references the `c-11-memory-carryover-from-branch` skill in full (was "C-11"). Reference-style normalization; behavior unchanged.
- 2026-06-01T20:45+02:00 — Extended conformance coverage to the new `worktree_abandon` payload/response model.
- 2026-05-29T08:53+02:00: Created onboarding for the dev-time tool-response conformance tests covering all public tools.
