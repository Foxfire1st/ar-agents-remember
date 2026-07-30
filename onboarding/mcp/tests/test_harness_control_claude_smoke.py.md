# test_harness_control_claude_smoke.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude_smoke.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-30T15:25+02:00 |
| lastVerifiedCommitHash | `2b47ed9520a770b9858e8af1f112f58745dcf473` |
| lastVerifiedCommitDate | 2026-07-30T16:00:03+02:00|
| governingOverview | `../overview.md` |

## Governing Overview
[tests overview](../overview.md)

## Purpose
Opt-in credential-safe live smoke for exact Claude Code 2.1.207.

## Code Commentary
Starts the real adapter, submits the advertised local `/cost` command through the correlated path,
requires completed terminal evidence, and shuts down without printing model, credential, environment,
or settings content.

## Invariants And Boundaries
Pinned and opt-in. `/cost` avoids an API request; it does not weaken production 429 handling.
The submission carries an exact `ControlOperationRef`, which the state machine has required since
operation refs became mandatory; the smoke had drifted behind that signature and failed on
construction rather than on protocol truth.

### Pending Capability (260727-CHATS-IM-L4)

This smoke asserts a capability the harness does not implement yet. Harness slash commands are
unimplemented and scheduled as an upcoming master task (developer ruling, 2026-07-30), so the `/cost`
submission cannot complete: against claude 2.1.220 the smoke reaches `control` = `ready` with an
accepted submission, then fails in the terminal wait with "Claude replay-user-message body changed for
its retained correlation" because the harness echoes a rewritten body for the slash command and the
retained-correlation comparison rejects it. Ordinary prompts are unaffected — a plain-text submission
on the same build completes normally.

Until the slash-command master lands, treat a red run of this suite as the expected state for its
`/cost` arm rather than a regression, and read the control-readiness half of the test as the live
signal. Do NOT convert the submission to a plain prompt to make it green: that would spend model
tokens and abandon the credential-safe local-command design this smoke exists to preserve. Note the
failure only became reachable after the transport restart repair — before it, the smoke never got
past the handshake.

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter exercised. | `L1-L25` | [harness_control_claude.py](../src/agents_remember/serving/harness_control_claude.py) |

## 260713-PHA-L6 Fixture Boundary

The Claude `2.1.207` stream fixture is a reproducible smoke baseline only. It must not be read as a
production exact-version requirement; production accepts the installed/current CLI through the
structured contract.

## Update History
- 2026-07-30T15:25+02:00 — 260727-CHATS-IM-L4: recorded the developer ruling that harness slash
  commands are unimplemented and owned by an upcoming master, so this suite's `/cost` arm asserts a
  pending capability and its red state is expected rather than a regression.
- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: supplied the required exact operation ref so the smoke
  again reaches real protocol behavior, and recorded the remaining slash-command replay-body gap that
  the transport restart repair uncovered.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: marked the exact fixture version as non-production evidence.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
