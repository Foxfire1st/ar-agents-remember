# mcp/src/agents_remember/serving/codex_app_server_state.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The session retains parsed pages and projects them into the normalized catalog; the adapter consumes
the same strict thread and event helpers.

- Session reads all model pages and validates desired/effective model-local settings against these rows. [1]
- Adapter reserves each prompt with the current desired selection and dispatches the retained pair on `turn/start`. [2]
- Initialize parsing extracts the primary Codex product version while requiring exact client identity on host-first responses. [3]
- Thread-open parsing now also reads the host's own loaded instruction documents onto the evidence object. [4]

### Cross-Repo References

No external repository boundary is implemented by this parser module.

No meaningful cross-repo references found.
