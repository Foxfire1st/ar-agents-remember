# mcp/src/agents_remember/serving/codex_app_server_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T19:36+02:00 |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a` |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Contains strict Codex app-server model, thread, state, interaction, submission-ledger, activity,
terminal, transcript, and reconciliation parsing helpers used by the native adapter/session pair.
It also owns method-specific response serialization. Empty-form MCP tool approvals expose
`accept`/`decline`/`cancel` choices and translate bare actions to Codex's native elicitation result;
non-empty MCP forms remain structured-JSON-only.

## Code Commentary

### Logic

`CodexModelCapability` now retains the model id/token, display name, description, default reasoning
effort, descriptive `EffortOption` rows, hidden state, and default state. `parse_model_page` validates
every row and preserves that metadata while checking the default belongs to that model's own effort
menu. Selection resolves exactly one configured id/model or exactly one visible advertised default.
Thread parsing verifies echoed effective effort. `SubmissionEvidence` now captures the exact
`CodexModelCapability` and effort selected when a prompt is reserved, and the bounded ledger stores
that immutable selection epoch beside request state/turn identity. The remaining helpers map
structured activity and terminal statuses, transcript items, and stable server requests.

`parse_server_interaction` retains a defensive copy of the request params beside the normalized
pending interaction. `interaction_result` uses those original params to distinguish an empty
`mode=form` schema from a content-bearing elicitation. Only the exact empty schema exposes action
buttons; `accept` becomes `{action: "accept", content: {}}`, while decline/cancel remain action-only.
Non-empty forms neither expose misleading scalar buttons nor accept a bare `accept`.

L0E's `native_evidence_frames_from_thread` flattens one `thread/read` thread into typed
`NativeEvidenceFrame` rows in stored order: every turn contributes its id as the item's
`nativeParentId`, every item must carry a unique `id` and a `type`, and a repeated id raises
`CodexAppServerError` instead of manufacturing a cursor that could overlap or skip items across
pages. Item payloads cross whole as the frame `raw`; `created_at` stays `None` rather than invented.

### Conventions

Parser helpers require typed JSON fields and include context in failures. Reasoning-effort display
names preserve vendor tokens while descriptions preserve vendor explanatory text. Stable server
requests are explicitly enumerated; `item/tool/requestUserInput` remains rejected as experimental.

### Invariants And Boundaries

- Each model owns its own effort menu and default; defaults outside that menu fail loudly.
- Hidden models remain catalog evidence but are not eligible as the implicit default.
- Advertised desired effort and echoed effective effort must agree exactly.
- Reconciliation retains exact request/turn/item identity and never authorizes blind resend.
- A queued prompt carries its own model/effort pair; later desired-state changes cannot rewrite the
  selection under which that work entered the adapter.
- Submission and interaction state is bounded and saturates loudly.
- MCP elicitation action buttons are safe only when `requestedSchema.properties` is an empty map;
  content-bearing forms preserve their structured JSON contract.
- Native evidence identity is exact: missing item id/type fails parsing and duplicate ids fail
  closed; paging never proceeds without per-item uniqueness.

### Todos

None known for the L3 submission-evidence model.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The session retains parsed pages and projects them into the normalized catalog; the adapter consumes
the same strict thread and event helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| Session reads all model pages and validates desired/effective model-local settings against these rows. | `discover` | mcp/src/agents_remember/serving/codex_app_server_session.py:214-224 |
| Adapter reserves each prompt with the current desired selection and dispatches the retained pair on `turn/start`. | `submit`; `_start_turn` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:239-264; mcp/src/agents_remember/serving/codex_app_server_adapter.py:434-480 |
| The adapter passes the retained request params back into method-specific result serialization. | `respond` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:324-353 |
| Empty-form detection and MCP elicitation result serialization. | `mcp_elicitation_result`; `mcp_elicitation_is_empty_form` | mcp/src/agents_remember/serving/codex_app_server_state.py:498-540 |

## Cross-Repo References

No external repository boundary is implemented by this parser module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-09T19:36+02:00 — 260713-TES-L5F2: retained server-request params and documented safe
  scalar handling for Codex's empty-form MCP tool approvals while keeping non-empty forms structured.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 2 Codex app-server session/adapter reference claims with exact lifecycle method anchors; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the stored-order
  `native_evidence_frames_from_thread` flatten — typed item id/type, turn parent identity,
  duplicate-id fail-closed, and whole-item raw payloads. Verification metadata stays pinned until
  closeout stamps the candidate commit.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented model/effort selection epochs on
  bounded prompt evidence so later setters cannot retroactively rewrite queued work.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented retained display/description
  metadata, descriptive model-local effort options, hidden/default selection, and default-menu
  validation.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented opaque structured-version extraction and strict
  initialization capability validation.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for typed protocol state,
  exact effort validation, server interactions, terminal mapping, and bounded reconciliation.
  Verification remains unset until closeout stamps the code commit.
