# mcp/src/agents_remember/mcp/tools/capsule_serving.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/capsule_serving.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ff97072c2d816dc6bc15d55bf8578db7fdd376b8` |
| lastVerifiedCommitDate | 2026-09-16T12:47:44+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `overview.md` |

## Governing Overview

[tools route overview](overview.md)

## Purpose

The three payload builders for the capsule operation and the skill surface. Each one re-shapes the
declaration's flat arguments into the application request record, calls the application entry point,
and passes the result through the route's shared transport envelope.

This module is transport-thin by the route's own invariant: deterministic behavior belongs in
`application/skill_resources/`, not here.

## Code Commentary

### Logic

- `role_capsule_compile_payload(config, *, contract_path, task_path, role, operation)` builds a
  `CapsuleOperationRequest` and returns `_tool_payload("role_capsule_compile", <response>.to_payload())`.
- `skill_catalog_list_payload(*, origin=None, root=None)` and
  `skill_catalog_read_payload(uri, *, origin=None, root=None)` build a `SkillCatalogRequest` **only
  when** `origin` or `root` was supplied; otherwise they pass `None` and the application layer uses the
  shipped corpus. The `origin`-or-default expression means supplying a root alone still names the
  shipped origin rather than an empty string.
- The builders take the request fields as keyword-only arguments, so a call site cannot silently swap
  `origin` and `root`.

### Conventions

Every builder funnels through `base._tool_payload`, which is the route's single choke point: it
validates the response against `TOOL_RESPONSE_MODELS`, attaches the lifecycle tail before the one
`model_dump`, and records the completed call after finalization. Nothing here re-implements any part
of that.

### Invariants And Boundaries

- **The builders are for tests and for registration; the corpus override is not a public capability.**
  `registration/capsule_serving.py` calls the two skill builders with no arguments, so a live client
  cannot select a different tree. The override exists so the test module can drive a synthetic corpus.
- **No behavior lives here.** No selection, no revision check, no refusal decision: a refusal is
  already a value returned by the application layer, and this module only wraps it.
- The response models are registered in `TOOL_RESPONSE_MODELS`, so an unregistered name would raise in
  `finalize_tool_response` rather than return a payload — the L29 lesson this route records.

### Todos

None recorded.

## Docs References

No external documentation governs this internal payload adapter. No relevant documentation found
after checking live sources.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The capsule builder re-shapes the flat declaration arguments into the application request record. | `role_capsule_compile_payload` | mcp/src/agents_remember/mcp/tools/capsule_serving.py:22-41 |
| The two skill builders build a corpus request only when an override was supplied, so the shipped corpus is the default. | `skill_catalog_list_payload`; `skill_catalog_read_payload` | mcp/src/agents_remember/mcp/tools/capsule_serving.py:44-63 |
| The route's single choke point every builder funnels through. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The registrations that call these builders, which pass no corpus override. | `_register_skill_tools` | mcp/src/agents_remember/mcp/registration/capsule_serving.py:120-139 |
| The application entry points these builders forward to. | `role_capsule_compile_tool`; `skill_catalog_list_tool`; `skill_catalog_read_tool` | mcp/src/agents_remember/application/skill_resources/operation.py:68-107 |
| The response-model registry rows that make these names returnable. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:155-238 |
| The test module that drives the corpus override these builders expose. | `_synthetic_corpus`; `World` | mcp/tests/test_capsule_serving.py:279-279; mcp/tests/test_capsule_serving.py:370-370 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the three payload builders.
  Recorded that the corpus override exists for tests and is deliberately absent from the registered
  signatures, and that the module carries no behavior beyond re-shaping the request and passing the
  response through the route's one choke point. Verification metadata remains closeout-owned; no
  acceptance claim is made.
