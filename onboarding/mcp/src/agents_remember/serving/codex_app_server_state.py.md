# mcp/src/agents_remember/serving/codex_app_server_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b`|
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Contains typed state, parsing, capability, interaction, submission-ledger, activity, terminal, and
transcript helpers for the Codex app-server adapter.

## Code Commentary

The module parses model pages and thread/turn responses, validates exact reasoning effort, maps
structured active flags and terminal statuses, extracts transcript items, classifies stable versus
experimental server requests, and retains bounded submission evidence for reconnect reconciliation.

## Conventions

Parser helpers require typed JSON fields and include context in failures. Stable server requests are
explicitly enumerated; `item/tool/requestUserInput` remains rejected as experimental.

## Invariants And Boundaries

- Advertised effort and echoed effective effort must agree exactly.
- Reconciliation evidence retains request/turn/item identity and never authorizes blind resend.
- Submission and interaction state is bounded and saturates loudly.

## Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stable and experimental request inventory is fixture-pinned. | L13-L31 | [codex_app_server_0_144_3.json](../../../../tests/fixtures/codex_app_server_0_144_3.json) |
| Adapter consumes parsing, interaction, activity, and terminal helpers. | L326-L459 | [codex_app_server_adapter.py](codex_app_server_adapter.py) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer confirmed structured status, server requests, reconnect, and boundedness. | L25-L30 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

### 260713-PHA-L6 Structured Initialization

Initialization extracts an opaque CLI token from the documented `client/<version>` identity form
and preserves concrete platform evidence. It rejects malformed identity rather than accepting
arbitrary fallback text.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented opaque structured-version extraction and strict
  initialization capability validation.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for typed protocol state,
  exact effort validation, server interactions, terminal mapping, and bounded reconciliation.
  Verification remains unset until closeout stamps the code commit.
