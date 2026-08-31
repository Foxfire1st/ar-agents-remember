# codex_driver.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/codex_driver.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:20:19+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Owns the real Codex consumer boundary for the clean-room scenario: candidate MCP probing, ambient
app-server execution, bounded notification collection, negotiated-version evidence, and subprocess
diagnostics.

## Code Commentary

### Logic

The public helpers bridge synchronous scenario code into bounded async probes. Candidate MCP
registration is checked independently, then a fresh real Codex app-server session starts against
the deterministic Responses endpoint and normally configured MCP server. Evidence keeps bounded
turn/notification summaries, exact process status, negotiated 0.151.0 identity, and explicit
absence of ambient plane/role environment identity rather than copying entire logs. The caller may
select the initial or same-seat-idempotency fixture prompt; neither path adds model-held retries.

### Conventions

Codex is invoked from the candidate container's selected executable. Environment construction is
explicit and fixture-scoped; no host configuration or production credentials are inherited by
accident.

### Invariants And Boundaries

- This module never fakes Codex or the MCP transport.
- The deterministic model provider controls choices only; real app-server protocol and MCP tool
  discovery remain in force.
- Timeouts are bounded and failure evidence is size-limited.
- The executed client must report the pinned 0.151.0 release in acceptance evidence.

### Todos

None.

## Docs References

No Domain Documentation source is configured. Runtime negotiation is the authority for the client
actually exercised by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| The real app-server probe and ambient turn collect negotiated runtime evidence. | `_run_ambient_codex` | scripts/e2e_harness/codex_driver.py:100-194 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP registration and handshake are inspected before ambient execution. | `codex_mcp_registration` | scripts/e2e_harness/codex_driver.py:34-49; scripts/e2e_harness/codex_driver.py:72-97 |
| Process and notification summaries stay bounded for actionable reports. | `_notification_summary` | scripts/e2e_harness/codex_driver.py:197-252 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| All external state is fixture-provided rather than imported from another repository. | `_codex_environment` | scripts/e2e_harness/codex_driver.py:254-289 |

## Update History

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: added explicit ambient-identity-absence
  evidence and the deliberate same-seat repeat prompt while retaining one real Codex boundary per
  call. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for the real Codex 0.151.0 driver. Verification metadata remains closeout-owned.
