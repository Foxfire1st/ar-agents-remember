# mcp/tests/test_codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b`|
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

Fake-transport conformance tests for the Codex app-server adapter.

## Code Commentary

The suite drives stable handshake/model/thread setup, exact effort acceptance and loud rejection,
start/resume preservation, busy steer/queue behavior, structured approvals and elicitation,
experimental request rejection, reconnect reconciliation without resend, and terminal/transcript
mapping using the pinned fixture.

## Conventions

The fake transport records requests and emits protocol messages deterministically; AnyIO supplies
the asyncio backend used by the adapter.

## Invariants And Boundaries

- Tests prove protocol acceptance rather than pane/log readiness.
- Experimental surfaces and absent/unconfirmed effort fail loudly.
- Reconnect assertions require `resend: false`; no production registration is tested here.

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
| Tests use the exact-version protocol fixture. | L27-L29; L186-L199 | [codex_app_server_0_144_3.json](fixtures/codex_app_server_0_144_3.json) |
| Adapter under test owns normalized lifecycle and reconnect behavior. | L63-L128; L490-L506 | [codex_app_server_adapter.py](../src/agents_remember/serving/codex_app_server_adapter.py) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer reproduced the focused conformance and live no-prompt smoke passes. | L22-L29 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

## 260713-PHA-L6 Evidence Boundary

Adapter regressions prove a compatible newer structured Codex identity is accepted and malformed or
inconsistent initialization/thread evidence is rejected; exact package strings are fixture evidence.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented negotiated-version acceptance and loud rejection
  coverage.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for fake-protocol
  conformance, R11 strictness, server requests, busy policy, terminal mapping, and no-resend
  reconnect coverage. Verification remains unset until closeout stamps the code commit.
