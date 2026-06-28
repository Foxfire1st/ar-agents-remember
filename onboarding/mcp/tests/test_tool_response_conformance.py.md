# test_tool_response_conformance.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/tests/test_tool_response_conformance.py`      |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-27T22:00+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`         |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                      |

## Purpose

`test_tool_response_conformance.py` moves the production response-contract
guarantee into the test suite: every response-modeled MCP payload builder produces
a payload that conforms to its registered Pydantic response model, so controller
drift is caught at dev time instead of in a live tool call.

## Code Commentary

### Logic

Production already validates each tool payload through
`tools._tool_payload()` against `models.tool_registry.TOOL_RESPONSE_MODELS`
(strict models use `extra="forbid"`). These tests reproduce that guarantee by
obtaining a *representative* payload for every modeled builder from the real
`*_payload` builder, then asserting conformance.

`setUpClass` builds seven temporary fixtures (each in its own temp dir) and
collects one representative payload per tool into `cls.payloads`:

- `_base_fixture` / `_simple_payloads`: a code repo, memory layer, and
  `.codex/mcp` settings drive the 25 tools that run directly (core, context,
  runtime, memory, skills, provider status/diagnostics/watchers, GrepAI/CGC
  dry-run, baseline, benchmarks).
- `_worktree_payloads`: a real worktree lifecycle in disabled-memory mode
  produces `worktree_start`, `worktree_status`, `worktree_attach`,
  `worktree_sync` (dry-run, GitHub #54 sub-task D), `worktree_closeout_preview`,
  `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`, and
  `lifecycle_finalize_task` (dry-run) against a real contract.
- `_carryover_payloads`: a landed-branch fixture drives `memory_carryover_plan`
  and `memory_carryover_apply` (a docstring names the
  `c-11-memory-carryover-from-branch` skill).
- `_lifecycle_payloads`: installs an ambient lifecycle over a temp `EventStore`
  and drives the lifecycle signal payloads (task 28 adds a representative
  `lifecycle_turn_end_notification` payload — the NOTIFY-AND-CONTINUE turn end that
  leaves the lifecycle `awaiting-developer`); `lifecycle_block` remains here as
  lower-level compatibility coverage, not as an advertised public MCP tool.
- `_task_doc_payloads`: a base fixture authoring one representative `task_doc`
  document (a `create`), so the JSON-primary task tool has a payload (slice 3c).
- `_gate_payloads`: a base fixture driving `lifecycle_gate` with an injected
  developer decision for deterministic conformance, then create/decide/wait/response-wait/list
  compatibility payloads, so both the public unified gate response and retained
  lower-level gate response models have representative payloads.
- `_operator_inbox_payloads`: a base fixture posting, polling, and consuming one
  external-chat inbox entry, so the three `operator_inbox_*` tools have
  representative payloads (task 10).

The former `_direct_closeout_payloads` fixture was removed with the
`direct_closeout_*` tools (issue #62 worktree-only closeout).

`tearDownClass` removes the temp dirs with `shutil.rmtree(..., ignore_errors=True)`
because git worktrees leave read-only pack files that otherwise break cleanup on
Windows.

`test_every_modeled_tool_has_a_representative_payload` asserts the payload set
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
  (currently none are needed — every modeled tool runs for real, including the
  task-28 `lifecycle_turn_end_notification`).
- Strict response models must keep `extra="forbid"`; flexible models keep
  `extra="allow"`. The structural rule is `FlexibleResponseModel` membership.
- This is a dev-time conformance net; the runtime contract still lives in
  `_tool_payload()`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The registry maps each public tool to its response model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| `_tool_payload()` is the production validation path mirrored here. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The strict/flexible response-model taxonomy lives in the model base. | [base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| Worktree/carryover fixtures reuse worktree test helpers. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Schema-level registry coverage is asserted separately. | [test_models.py](agents-remember/mcp/tests/test_models.py) |
| Inbox representative payloads call the real post, poll, and consume builders. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |
| Lifecycle finalizer representative payload exercises the new terminal worktree tool. | [lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py) |

## Update History

- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): `_lifecycle_payloads` now also drives a representative `lifecycle_turn_end_notification` payload, so the new public tool's registered response model is covered by `test_every_modeled_tool_has_a_representative_payload` / `test_representative_payloads_conform_to_registered_models`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T18:43+02:00 — Regression fixture update: `_gate_payloads`
  now resolves the representative `lifecycle_gate_payload` through an injected
  developer-attributed decision instead of the internal zero-timeout path.
- 2026-06-26T17:05+02:00 — Regression fixture update: `_gate_payloads`
  preserves deterministic conformance coverage after the public junction became blocking.
- 2026-06-26T14:16+02:00 — Task 25: conformance now targets `TOOL_RESPONSE_MODELS`, adds a representative `lifecycle_gate` payload, and keeps split gate/block/wait payloads as compatibility coverage rather than public-tool coverage.
- 2026-06-25T07:17+02:00 — Task 19: `_gate_payloads` now includes a representative `gate_response_wait` payload so the new public helper is covered by response conformance. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added a representative `lifecycle_finalize_task` payload to the worktree fixture, so all 51 public tools still validate through their registered response models. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `_operator_inbox_payloads` and a seventh fixture so the three `operator_inbox_*` tools have representative payloads; the suite now covers 50 public tools. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00: Task 6 slice 6a — added the `_gate_payloads` fixture (a sixth fixture) so the four `gate_*` tools have representative payloads; the suite now covers 47 public tools. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34: Slice 3c commit 1 — added the `_task_doc_payloads` fixture (a fifth fixture) so the `task_doc` tool has a representative payload; the suite now covers 43 public tools. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00: Slice 2b — added the `_lifecycle_payloads` fixture (a fourth fixture) so the six `lifecycle_*` tools have representative payloads; the suite now covers 42 public tools. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-11T06:47+02:00 — Removed the `_direct_closeout_payloads` fixture and its temp dir (issue #62 worktree-only closeout); the suite now covers the 36 public tools across three fixtures.
- 2026-06-10T09:56+02:00: Added the `worktree_sync` dry-run representative payload to the worktree fixture (GitHub #54 sub-task D).
- 2026-06-06T12:28+02:00: Corrected the `_tool_payload()` reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-06-02T16:24+02:00: A docstring now references the `c-11-memory-carryover-from-branch` skill in full (was "C-11"). Reference-style normalization; behavior unchanged.
- 2026-06-01T20:45+02:00 — Extended conformance coverage to the new `worktree_abandon` payload/response model.
- 2026-05-29T08:53+02:00: Created onboarding for the dev-time tool-response conformance tests covering all public tools.
