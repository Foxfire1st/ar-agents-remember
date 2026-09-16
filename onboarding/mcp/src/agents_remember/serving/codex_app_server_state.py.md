# mcp/src/agents_remember/serving/codex_app_server_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:15+02:00 |
| lastVerifiedCommitHash | `34f818a190c35238dca33552d586ea2ace5d9e06` |
| lastVerifiedCommitDate | 2026-09-16T14:33:47+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l5-ar` uncommitted source; base `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Contains strict Codex app-server model, thread, state, interaction, submission-ledger, activity,
terminal, transcript, and reconciliation parsing helpers used by the native adapter/session pair.
260718-CHATS-L0E adds the `thread/read` → native-evidence-frame flatten helper.
260915-CAPS-L5 adds the thread-open `instructionSources` observation to `CodexThreadEvidence`.

## Code Commentary

L23 accepts any reported server product token but still requires the exact Agents Remember client identity suffix and reported version; the observed product is retained as diagnostic evidence.

### Logic

`CodexModelCapability` now retains the model id/token, display name, description, default reasoning
effort, descriptive `EffortOption` rows, hidden state, and default state. `parse_model_page` validates
every row and preserves that metadata while checking the default belongs to that model's own effort
menu. Selection resolves exactly one configured id/model or exactly one visible advertised default.
Thread parsing verifies echoed effective effort. `SubmissionEvidence` now captures the exact
`CodexModelCapability` and effort selected when a prompt is reserved, and the bounded ledger stores
that immutable selection epoch beside request state/turn identity. The remaining helpers map
structured activity and terminal statuses, transcript items, and stable server requests.

L0E's `native_evidence_frames_from_thread` flattens one `thread/read` thread into typed
`NativeEvidenceFrame` rows in stored order: every turn contributes its id as the item's
`nativeParentId`, every item must carry a unique `id` and a `type`, and a repeated id raises
`CodexAppServerError` instead of manufacturing a cursor that could overlap or skip items across
pages. Item payloads cross whole as the frame `raw`; `created_at` stays `None` rather than invented.

**CAPS-L5's `_instruction_sources`,** called from `parse_thread_open_response`, reads the thread-open
response's `instructionSources` — the **host's own** list of instruction documents it loaded for that
thread — onto `CodexThreadEvidence.instruction_sources`. An absent or null field is a legitimate answer
on a version that does not expose it and yields `()`; a present value that is not a list of non-empty
strings raises `CodexAppServerError` naming the method. This is observation, not authority: the session
publishes it verbatim so automatic host injection (for example a workspace `AGENTS.md`) is visible, and
the legacy-chain switch's *reason* is built from it.

### Conventions

Parser helpers require typed JSON fields and include context in failures. Reasoning-effort display
names preserve vendor tokens while descriptions preserve vendor explanatory text. Stable server
requests are explicitly enumerated; `item/tool/requestUserInput` remains rejected as experimental.
Initialize identity accepts only the current Codex Desktop host-first wire shape. Its diagnostics
must end in the exact requested `(agents_remember; <client-version>)` token. The Desktop product's
version remains the negotiated Codex version and must later agree with thread evidence.

### Invariants And Boundaries

- Each model owns its own effort menu and default; defaults outside that menu fail loudly.
- Hidden models remain catalog evidence but are not eligible as the implicit default.
- Advertised desired effort and echoed effective effort must agree exactly.
- Reconciliation retains exact request/turn/item identity and never authorizes blind resend.
- A queued prompt carries its own model/effort pair; later desired-state changes cannot rewrite the
  selection under which that work entered the adapter.
- Submission and interaction state is bounded and saturates loudly.
- Native evidence identity is exact: missing item id/type fails parsing and duplicate ids fail
  closed; paging never proceeds without per-item uniqueness.
- A host-first initialize response without the exact requested client name/version suffix is not
  accepted as Agents Remember's app-server session.
- **The instruction-source observation is reported, never authored.** `instructionSources` is the
  host's own list; an absent field is `()` (a version that does not expose it) while a malformed one
  raises, and nothing here may synthesize a source the host did not report.

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
| Session reads all model pages and validates desired/effective model-local settings against these rows. | `discover` | mcp/src/agents_remember/serving/codex_app_server_session.py:245-255 |
| Adapter reserves each prompt with the current desired selection and dispatches the retained pair on `turn/start`. | `submit`; `_start_turn` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:285-310; mcp/src/agents_remember/serving/codex_app_server_adapter.py:484-530 |
| Initialize parsing extracts the primary Codex product version while requiring exact client identity on host-first responses. | `validate_initialize_response` | mcp/src/agents_remember/serving/codex_app_server_state.py:139-169 |
| Thread-open parsing now also reads the host's own loaded instruction documents onto the evidence object. | `_instruction_sources`; `parse_thread_open_response`; `CodexThreadEvidence` | mcp/src/agents_remember/serving/codex_app_server_state.py:274-294; mcp/src/agents_remember/serving/codex_app_server_state.py:297-327; mcp/src/agents_remember/serving/codex_app_server_state.py:59-75 |

## Cross-Repo References

No external repository boundary is implemented by this parser module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: documented the thread-open `instructionSources`
  observation on `CodexThreadEvidence` — absent/null yields `()`, a malformed present value raises with
  the method named, and the value is host-reported observation published verbatim (the legacy-chain
  switch's reason is built from it). Re-anchored `discover` and `validate_initialize_response` and added
  the observation's ranges. Verification metadata moves to the last committed source `c1dbebf8`;
  closeout re-stamps the real code commit.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: documented the clean-cut current
  Desktop initialize grammar, exact client suffix, and unchanged initialize/thread version
  agreement; no unused CLI compatibility branch remains.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

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
