# mcp/src/agents_remember/mcp/tools/capsule_serving.py

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

## Evidence

### Docs References

No external documentation governs this internal payload adapter. No relevant documentation found
after checking live sources.

### Repo-Internal References

- The capsule builder re-shapes the flat declaration arguments into the application request record. [1]
- The two skill builders build a corpus request only when an override was supplied, so the shipped corpus is the default. [2]
- The route's single choke point every builder funnels through. [3]
- The registrations that call these builders, which pass no corpus override. [4]
- The application entry points these builders forward to. [5]
- The response-model registry rows that make these names returnable. [6]
- The test module that drives the corpus override these builders expose. [7]

### Cross-Repo References

No meaningful cross-repository reference applies.
