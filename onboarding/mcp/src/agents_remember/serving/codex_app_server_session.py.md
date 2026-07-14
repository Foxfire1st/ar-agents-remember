# mcp/src/agents_remember/serving/codex_app_server_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b`|
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Establishes and records the Codex app-server initialize, model discovery, and thread start/resume
session contract.

## Code Commentary

`CodexAppServerSession.connect` performs stable initialize/initialized, paginated model discovery,
exact model and advertised reasoning-effort selection, then starts or resumes the exact thread. It
preserves launch configuration and exposes the capability/effective-settings snapshot used by the
adapter.

## Conventions

The runtime user-agent must prove Codex `0.144.3`. Reasoning effort is selected from the advertised
model menu and travels through thread configuration and turn parameters; it is never mapped onto
argv.

## Invariants And Boundaries

- Experimental API remains false and unsupported capabilities fail explicitly.
- Start/resume preserves exact thread identity, model, cwd, sandbox, approval, configuration, and
  effective reasoning effort.
- Missing, conflicting, or unadvertised effort values fail loudly.

## Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry; the validated
protocol snapshot is recorded in the repository fixture instead.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Model effort menu and thread echoes are fixture evidence. | L39-L99 | [codex_app_server_0_144_3.json](../../../../tests/fixtures/codex_app_server_0_144_3.json) |
| Session output is consumed by the adapter handshake and reconnect flow. | L87-L153; L490-L506 | [codex_app_server_adapter.py](codex_app_server_adapter.py) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer confirmed exact-version initialize/model/thread behavior. | L17-L25 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

### 260713-PHA-L6 Structured Identity

The `initialize` user-agent token must have the documented client/opaque-version form and must
agree with the `thread/start` or `thread/resume` `cliVersion`. Selected model, reasoning effort,
cwd, sandbox, and approval policy remain concrete required evidence; no semver compatibility guess
is made.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented cross-message Codex capability negotiation and
  loud failure for inconsistent structured identity.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for exact initialize,
  model/effort discovery, thread start/resume, and preserved settings. Verification remains unset
  until closeout stamps the code commit.
