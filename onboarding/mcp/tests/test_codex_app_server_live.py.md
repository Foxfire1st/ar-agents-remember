# mcp/tests/test_codex_app_server_live.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_live.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `acb308c50072d8cde0015c4828e39d12480872ed`|
| lastVerifiedCommitDate | 2026-07-14T12:32:48+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

Opt-in credential-safe live smoke for the pinned Codex app-server handshake, model menu, reasoning
effort, and ephemeral thread.

## Code Commentary

The test is skipped unless explicitly enabled, launches the selected exact-version package, starts
the adapter with environment-provided model/effort settings, asserts advertised/effective effort,
and stops the ephemeral session without sending a prompt.

## Conventions

Runtime package, model, and effort are explicit environment inputs; the default test path remains
non-live and skipped.

## Invariants And Boundaries

- No credential value is read or printed and no prompt is delivered.
- The smoke does not register, cut over, or persist a production session.
- Exact protocol readiness is established through initialize/model/thread evidence.

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
| Live smoke constructs an ephemeral, no-prompt adapter session. | L24-L53 | [test_codex_app_server_live.py](test_codex_app_server_live.py) |
| Session owns exact model and effort capability validation. | L95-L153 | [codex_app_server_session.py](../src/agents_remember/serving/codex_app_server_session.py) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer confirmed the exact-version live no-prompt smoke passed safely. | L22-L24 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

## Update History

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for the opt-in exact-version
  live handshake smoke and credential/prompt safety boundary. Verification remains unset until
  closeout stamps the code commit.
