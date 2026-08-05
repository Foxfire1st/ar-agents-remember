# mcp/src/agents_remember/observer/events.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/events.py`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T11:15+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The store serializes and reads these events. | `append`, `read`, `read_log` | mcp/src/agents_remember/observer/store.py:119-132; mcp/src/agents_remember/observer/store.py:134-148; mcp/src/agents_remember/observer/store.py:150-163 |
| Ids come from the local ULID mint. | `new_ulid` | mcp/src/agents_remember/observer/ulid.py:30-41 |
| The response-contract convention this envelope mirrors (camelCase fields, strict extras). | `StrictResponseModel` | mcp/src/agents_remember/models/base.py:10-13 |

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 6 citations (citation_anchor_missing=3, citation_prose_not_in_cit_form=0, citation_source_malformed=3); final scoped citation check clean.
- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
