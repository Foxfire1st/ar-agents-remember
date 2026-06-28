# mcp/src/agents_remember/observer/events.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/events.py`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T11:15+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                     |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The store serializes and reads these events. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| Ids come from the local ULID mint. | [ulid.py](agents-remember/mcp/src/agents_remember/observer/ulid.py) |
| The response-contract convention this envelope mirrors (camelCase fields, strict extras). | [models/base.py](agents-remember/mcp/src/agents_remember/models/base.py) |

## Update History

- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
