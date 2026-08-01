# mcp/src/agents_remember/models/read_files.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/models/read_files.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-01T09:38+02:00                      |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`  |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

`read_files.py` defines the AR-owned, strict response contract for the
`read_ar_files` tool (slice 07): one batch of paired source+onboarding reads plus
the auto-attached, session-deduplicated overview front-door.

## Code Commentary

`FileReadStatus` is the onboarding-lookup outcome Literal
(`found | missing | disabled | unsupported | not_requested`) — the *onboarding*
status, never a source-read condition. **It is not declared here.** Since
260731-EFA-L4 it is imported (L18-L22) from
`controllers.read_files` (L54 there), the module that decides it:
`_resolve_onboarding` returns it and `_read_one` puts it into an untyped payload
dict, so a copy on this side would only ever be measured against the producer
when a real read carried a new member — as a `ValidationError`, on the
`read_ar_files` tool path, with no handler for one. The controller also derives
`VALID_FILE_READ_STATUSES` from the alias by `get_args`, and
`test_wire_vocabulary_exhaustiveness` asserts the set `_resolve_onboarding`
actually returns *equals* it. `FileRead` (L26-L38, a `StrictResponseModel`,
`extra="forbid"`) is one requested file's result: `path`, `status`, an optional
`source` (the full file or the exact requested line range, omitted when the file
is absent or binary/non-decodable), and an optional `onboarding` body (the
`meaningful_body` when `status == found`, omitted otherwise) — so `source` is
independent of `status`.

`ReadArFilesResponse` (L41-L54) subclasses `ToolResponse` (strict): `operation`
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
  `source` field. `found` with an absent `source` is not a contradiction.
- **The status vocabulary lives with its producer, not with the wire model.**
  `FileReadStatus` is imported from `controllers.read_files`; this module must
  not re-declare it. The direction is producer → model because
  `_resolve_onboarding` is the only function that decides the value.
- Token fields are part of the contract but populated only at the choke point.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The strict response base and `ToolResponse`. | [models/base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| The controller producing the dict this validates, and now the DECLARER of `FileReadStatus` (L54) with its derived `VALID_FILE_READ_STATUSES` (L57); `_resolve_onboarding` (L216-L218) returns the narrowed type. | [controllers/read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |
| The registry mapping `read_ar_files` to this response model (L120). | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| `test_every_onboarding_status_the_read_controller_returns_validates` asserts the produced set equals the declared alias. | [test_wire_vocabulary_exhaustiveness.py](agents-remember/mcp/tests/test_wire_vocabulary_exhaustiveness.py) |

## Update History

- 2026-08-01T09:38+02:00 — 260731-EFA-L4 curator: body corrected. The card described
  `FileReadStatus` as this module's Literal; it is now imported (L18-L22) from
  `controllers.read_files` L54, the module whose `_resolve_onboarding` is the only function that
  decides the value. Recorded the derived `VALID_FILE_READ_STATUSES` and the exhaustiveness test
  that asserts produced == declared, and added the producer-owns-the-vocabulary invariant plus the
  explicit note that `found` with an absent `source` is not a contradiction. Citations: `FileRead`
  pinned to L26-L38, `ReadArFilesResponse` to L41-L54, the import to L18-L22; the controller
  reference row gained `FileReadStatus` L54 / `VALID_FILE_READ_STATUSES` L57 /
  `_resolve_onboarding` L216-L218, the registry row gained L120, and a row was added for the
  exhaustiveness suite. Verification metadata pinned until closeout stamps the L4 commit.

- 2026-06-22T22:33+02:00 — Created for slice 07: the `FileRead` + `ReadArFilesResponse` strict response contract for `read_ar_files`. Verification metadata pinned until closeout stamps the slice-07 code commit.
