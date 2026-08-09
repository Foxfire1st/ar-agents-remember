# mcp/src/agents_remember/models/read_files.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/models/read_files.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-02T01:05+02:00                      |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`  |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

`read_files.py` defines the AR-owned, strict response contract for the
`read_ar_files` tool (slice 07): one batch of paired source+onboarding reads plus
the auto-attached, session-deduplicated overview front-door.

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
(cit:([`FileRead`], mcp/src/agents_remember/models/read_files.py:35-47), a
`StrictResponseModel`, `extra="forbid"`) is one requested file's result: `path`,
`status`, an optional
`source` (the full file or the exact requested line range, omitted when the file
is absent or binary/non-decodable), and an optional `onboarding` body (the
`meaningful_body` when `status == found`, omitted otherwise) — so `source` is
independent of `status`.

cit:([`ReadArFilesResponse`], mcp/src/agents_remember/models/read_files.py:50-63) subclasses `ToolResponse` (strict): `operation`
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
- **The status vocabulary lives with the wire model, not with its producer.**
  `FileReadStatus` is declared here; `application.read_files` imports it and
  must not re-declare it. The direction is model → producer because the status
  is served wire vocabulary — `_resolve_onboarding` only decides the value.
- Token fields are part of the contract but populated only at the choke point.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict response base and `ToolResponse`. | `ToolResponse` | mcp/src/agents_remember/models/base.py:63-66 |
| The application entry point producing the dict this validates; it imports `FileReadStatus` from this module, and `_resolve_onboarding` returns the narrowed type. | `_resolve_onboarding` | mcp/src/agents_remember/application/read_files.py:209-238 |
| The registry mapping `read_ar_files` to this response model (L120). | `read_ar_files` | mcp/src/agents_remember/models/tool_registry.py:121-121 |
| `test_every_onboarding_status_the_read_entry_point_returns_validates` asserts the produced set equals the declared alias. | `test_every_onboarding_status_the_read_entry_point_returns_validates` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:775-782 |

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 8 citation findings and repaired the
  reversal this card had self-flagged. `FileReadStatus` is declared in this module at line 29 and
  `VALID_FILE_READ_STATUSES` is derived here at line 32; the body, the vocabulary invariant, and the two
  reference rows now state the model → producer direction (`application.read_files` imports the
  alias; `_resolve_onboarding` at 209-238 decides the value). The exhaustiveness row follows the
  renamed `test_every_onboarding_status_the_read_entry_point_returns_validates` (778-785). Scoped
  recheck clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact from the rename itself: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`; the references and the vocabulary here follow ("the application layer" for the package, "an application entry point" for one function). **FLAGGED, NOT FIXED — this body is stale for a reason that is NOT the rename, and the curator who owns that change should repair it.** A separate staged change in the same code worktree moved `FileReadStatus` and `VALID_FILE_READ_STATUSES` back INTO this module (L29 and L32); `application/read_files.py` now imports the alias at L43. That reverses the 260731-EFA-L4 decision recorded below, so the "`FileReadStatus` is imported from `application.read_files`; this module must ..." invariant and the reference row calling `application/read_files.py` "the DECLARER of `FileReadStatus` with its derived `VALID_FILE_READ_STATUSES`" are both false against the current worktree, as are the L54/L57/L216-L218 anchors in that row. The claims are left verbatim rather than rewritten into something plausible, because the intent behind the reversal belongs to that change, not to this one. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:38+02:00 — 260731-EFA-L4 curator: body corrected. The card described
  `FileReadStatus` as this module's Literal; it is now imported from
  `controllers.read_files` L54, the module whose `_resolve_onboarding` is the only function that
  decides the value. Recorded the derived `VALID_FILE_READ_STATUSES` and the exhaustiveness test
  that asserts produced == declared, and added the producer-owns-the-vocabulary invariant plus the
  explicit note that `found` with an absent `source` is not a contradiction. Citations: `FileRead`
  pinned to L26-L38, `ReadArFilesResponse` to L41-L54, the import to L18-L22; the controller
  reference row gained `FileReadStatus` L54 / `VALID_FILE_READ_STATUSES` L57 /
  `_resolve_onboarding` L216-L218, the registry row gained L120, and a row was added for the
  exhaustiveness suite. Verification metadata pinned until closeout stamps the L4 commit.

- 2026-06-22T22:33+02:00 — Created for slice 07: the `FileRead` + `ReadArFilesResponse` strict response contract for `read_ar_files`. Verification metadata pinned until closeout stamps the slice-07 code commit.
