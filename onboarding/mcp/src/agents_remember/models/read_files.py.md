# mcp/src/agents_remember/models/read_files.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/models/read_files.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-06-22T22:33+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`  |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

`read_files.py` defines the AR-owned, strict response contract for the
`read_ar_files` tool (slice 07): one batch of paired source+onboarding reads plus
the auto-attached, session-deduplicated overview front-door.

## Code Commentary

`FileReadStatus` is the onboarding-lookup outcome Literal
(`found | missing | disabled | unsupported | not_requested`) — the *onboarding*
status, never a source-read condition. `FileRead` (a `StrictResponseModel`,
`extra="forbid"`) is one requested file's result: `path`, `status`, an optional
`source` (the full file or the exact requested line range, omitted when the file
is absent or binary/non-decodable), and an optional `onboarding` body (the
`meaningful_body` when `status == found`, omitted otherwise) — so `source` is
independent of `status`.

`ReadArFilesResponse` subclasses `ToolResponse` (strict): `operation`
(`"read_ar_files"`), `repoId`, the `files` list, and the optional
`repository_overview` / `route_overviews` dicts. The latter two are the
session-deduplicated front door — each served once per lifecycle, or again when
its content changed, and omitted when already served unchanged (or when
onboarding was suppressed for every file). Token fields are stamped by
`finalize_payload_tokens` at the `_tool_payload` choke point — this module never
sets them.

## Invariants And Boundaries

- STRICT AR-owned shape: both models forbid extra fields. `ReadArFilesResponse` is
  registered in `tool_registry.PUBLIC_TOOL_RESPONSE_MODELS` and exercised by the
  conformance suite, which requires a representative payload per registered tool.
- `status` is the onboarding outcome only; source presence rides the independent
  `source` field.
- Token fields are part of the contract but populated only at the choke point.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The strict response base and `ToolResponse`. | [models/base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| The controller producing the dict this validates. | [controllers/read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |
| The registry mapping `read_ar_files` to this response model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-06-22T22:33+02:00 — Created for slice 07: the `FileRead` + `ReadArFilesResponse` strict response contract for `read_ar_files`. Verification metadata pinned until closeout stamps the slice-07 code commit.
