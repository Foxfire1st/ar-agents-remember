# mcp/src/agents_remember/observer/events.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`events.py` defines the `ar-observer-event/v1` envelope (`Event`) — one
append-only, durable record of something that happened in or to a lifecycle.

## Code Commentary

`OBSERVER_EVENT_SCHEMA` is the versioned wire tag. `Trust`
(`declared | observed | inferred | approved`) and `Actor`
(`model | system | developer`) are Literals so a typo cannot corrupt the audit
trail; the rendering rule is "never pretend declared is observed", and for
developer actions `data["via"]` (chat | dashboard | cli) carries "through what"
so who and through-what never share a field. `now_iso()` is the ISO-8601 +
offset timestamp source.

`Event` is a Pydantic `BaseModel` with `extra="forbid"`. Fields are camelCase to
match the package's response-model convention, so construction, `model_validate`,
and `model_dump` agree on the wire keys without per-field aliases (which also
keeps the synthesized `__init__` honest for static checkers). `schema_version` is
the single exception — it carries `alias="schema"` because `schema` is an awkward
Python attribute name — so records must be dumped with
`model_dump_json(by_alias=True, exclude_none=True)` for it to render as `schema`.

## Invariants And Boundaries

- This is a persisted-record model, **not** an MCP response: it has no token
  fields and is never returned by a tool, so it is not registered in
  `PUBLIC_TOOL_RESPONSE_MODELS`.
- The format must round-trip: a dumped line re-validates via `model_validate`
  (read side / replay), so aliases and `extra="forbid"` must stay consistent.
- `data` is the open extension point; the envelope fields are fixed and
  Literal-guarded.

## Evidence

### Repo-Internal References

- The store serializes and reads these events. [1]
- Ids come from the local ULID mint. [2]
- The response-contract convention this envelope mirrors (camelCase fields, strict extras). [3]
