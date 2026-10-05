# mcp/src/agents_remember/models/read_files.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`read_files.py` defines the AR-owned, strict response contract for the
`read_ar_files` tool (slice 07): one batch of paired source+onboarding reads plus
the auto-attached overview front-door deduplicated by lifecycle and code/onboarding root.

Defines the strict paired source/onboarding read response.

## Code Commentary

`FileReadStatus` is the onboarding-lookup outcome Literal
(`found | missing | disabled | unsupported | not_requested`) — the *onboarding*
status, never a source-read condition. It is declared HERE
(cit:([`FileReadStatus`], mcp/src/agents_remember/models/read_files.py:29-29)):
a served status is a field of the response below, so it is wire vocabulary and
this package owns it — declaring it in the application entry point that decides
it was the one edge that made `models` and `application` mutually dependent
(`layers.toml`). The application entry point imports the alias,
`_resolve_onboarding` returns it, and `_read_one` puts it into an untyped
payload dict, so a real read carrying a new member surfaces on this side as a
`ValidationError`, on the `read_ar_files` tool path, with no handler for one.
This module also derives `VALID_FILE_READ_STATUSES` from the alias by `get_args`
(cit:([`VALID_FILE_READ_STATUSES`], mcp/src/agents_remember/models/read_files.py:32-32)),
and `test_wire_vocabulary_exhaustiveness` asserts the set `_resolve_onboarding`
actually returns *equals* it. `FileRead`
(cit:([`FileRead`], mcp/src/agents_remember/models/read_files.py:35-53), a
`StrictResponseModel`, `extra="forbid"`) is one requested file's result: `path`,
`status`, an optional
`source` (the full file or the exact requested line range, omitted when the file
is absent or binary/non-decodable), and an optional `onboarding` body (the
`meaningful_body` when `status == found`, omitted otherwise) — so `source` is
independent of `status`.

Since MIK-R24 (rules 5 and 9) `FileRead` has three more optional fields, set only when the file's onboarding
was returned. `format` is `"text/v2"` for a converted memory tree or `"legacy-format"` for an unconverted
one. `sidecar` is the converted card's sidecar document, and `references` its resolved references, both
for a converted tree only. On an unconverted tree the card is returned as it is, with nothing resolved.
Their content is decided by `application/read_files_format.py`; this model only admits them.

cit:([`ReadArFilesResponse`], mcp/src/agents_remember/models/read_files.py:56-80) subclasses `ToolResponse` (strict): `operation`
(`"read_ar_files"`), `repoId`, the `files` list, the optional
`repository_overview` / `route_overviews` dicts, and the optional `published_intent` dict. The two
overview dicts are the
front door — each served once per lifecycle and resolved code/onboarding root pair, or again when
its content changed, and omitted when already served unchanged (or when
onboarding was suppressed for every file). Token fields are stamped by
`finalize_payload_tokens` at the `_tool_payload` choke point — this module never
sets them.

`published_intent` cit:([`published_intent`], mcp/src/agents_remember/models/read_files.py:80-80) is the repository's published intent
read through the existing selective read (ICR-R19@v1). It is deliberately **always present**, because its
own `state` is the answer: `recorded` carries the dataset identity, the snapshot and one bounded page per
seed, while `not-recorded` and `unusable` name why no publication could be read. Since MIK-R24 an unconverted memory tree
gets the state `legacy-format` instead: no knowledge section is read, and the block names the routes by
which such a tree converts. The model is unchanged by that, because it carries the block as a dict. Its shape is owned by
`application.published_intent` — the route that selects, seeds and names the absences — so this model
carries it as a dict rather than re-declaring a second contract for the same read, exactly as
`repository_overview` and `route_overviews` are carried for the front door.

### Role Runtime and Scope

The documented front-door dedup extent is lifecycle plus code/onboarding root, matching the application change. The strict response fields, independent source/status relationship, published-intent block and shared token choke point remain unchanged. Preserve the existing field explanations; update only the former lifecycle-only dedup sentence.

## Invariants And Boundaries

- STRICT AR-owned shape: both models forbid extra fields. `ReadArFilesResponse` is
  registered in `tool_registry.PUBLIC_TOOL_RESPONSE_MODELS` and exercised by the
  conformance suite, which requires a representative payload per registered tool.
- `status` is the onboarding outcome only; source presence rides the independent
  `source` field. `found` with an absent `source` is not a contradiction.
- **The status vocabulary lives with the wire model, not with its producer.**
  `FileReadStatus` is declared here; `application.read_files` imports it and
  must not re-declare it. The direction is model → producer because the status
  is served wire vocabulary — `_resolve_onboarding` only decides the value.
- Token fields are part of the contract but populated only at the choke point.
- **`published_intent` is carried here, not owned here.** The application entry point populates it on
  every call and the block's own `state` is the answer; `None` is the field's declared default, not a
  state the route produces. The model declares no field of that block, so the selection contract stays in
  `application/published_intent.py` and this module cannot drift into a second spelling of it.

## Evidence

### Repo-Internal References

- The strict response base and `ToolResponse`. [1]
- **The new field, and the owning module that decides its shape.** [2]
- The application entry point producing the dict this validates; it imports `FileReadStatus` from this module, and `_resolve_onboarding` returns the narrowed type. [3]
- The three optional format fields a file result gains, and the module that fills them. [4]
- The registry mapping `read_ar_files` to this response model (L120). [5]

### Runtime Source References

- Frozen implementation of ReadArFilesResponse supporting the stated file behavior. [6]
