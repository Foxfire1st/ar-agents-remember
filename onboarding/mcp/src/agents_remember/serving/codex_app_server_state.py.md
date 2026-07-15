# mcp/src/agents_remember/serving/codex_app_server_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Contains strict Codex app-server model, thread, state, interaction, submission-ledger, activity,
terminal, transcript, and reconciliation parsing helpers used by the native adapter/session pair.

## Code Commentary

### Logic

`CodexModelCapability` now retains the model id/token, display name, description, default reasoning
effort, descriptive `EffortOption` rows, hidden state, and default state. `parse_model_page` validates
every row and preserves that metadata while checking the default belongs to that model's own effort
menu. Selection resolves exactly one configured id/model or exactly one visible advertised default.
Thread parsing verifies echoed effective effort. The remaining helpers map structured activity and
terminal statuses, transcript items, stable server requests, and bounded submission evidence.

### Conventions

Parser helpers require typed JSON fields and include context in failures. Reasoning-effort display
names preserve vendor tokens while descriptions preserve vendor explanatory text. Stable server
requests are explicitly enumerated; `item/tool/requestUserInput` remains rejected as experimental.

### Invariants And Boundaries

- Each model owns its own effort menu and default; defaults outside that menu fail loudly.
- Hidden models remain catalog evidence but are not eligible as the implicit default.
- Advertised desired effort and echoed effective effort must agree exactly.
- Reconciliation retains exact request/turn/item identity and never authorizes blind resend.
- Submission and interaction state is bounded and saturates loudly.

### Todos

None known for the L1 capability parse.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The session retains parsed pages and projects them into the normalized catalog; the adapter consumes
the same strict thread and event helpers.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Session reads all model pages, selects model-local effort, and retains the complete catalog. | L100-L239 | [codex_app_server_session.py](codex_app_server_session.py) |
| Adapter uses parsed turns, activity, terminal, interaction, and transcript evidence. | L239-L408 | [codex_app_server_adapter.py](codex_app_server_adapter.py) |

## Cross-Repo References

No external repository boundary is implemented by this parser module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented retained display/description
  metadata, descriptive model-local effort options, hidden/default selection, and default-menu
  validation.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented opaque structured-version extraction and strict
  initialization capability validation.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for typed protocol state,
  exact effort validation, server interactions, terminal mapping, and bounded reconciliation.
  Verification remains unset until closeout stamps the code commit.
