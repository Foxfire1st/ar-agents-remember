# mcp/tests/test_conversation_control_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Interrupt ledger contract tests (R1/R7). Every test drives the real composition up to the harness
edge — a real bridge + IPC server on a real socket, the real submission authority, and the landed L2E
client reads — with the structural fake adapter as the only double. Covers acknowledgement vs
settlement, idempotence, per-session serialization, lost-response reconcile, the guard battery, and
both pi settlement classes (content-less, content-ful, and oversized/clipped).

## Code Commentary

### Logic

`CodexInterruptTests` (L34): accepted → `interrupted`/`already-settled`/`failed` settlement over the
completion surface; identical-tuple replay returns the stored projection with one native write;
reused id + different tuple → `request-conflict`; concurrent same-tuple gathers serialize to one
write; lost `may_have_sent` → `unknown` (202) → reconcile recovers the first ack with one write;
pre-write failure → 503 with no phantom record. `PiInterruptTests` (L178): the pi settlement battery
including the Finding 1 regression pair (content-ful `stop` → `already-settled`, content-ful
`aborted` → `interrupted`) driven through the real bridge evidence path, plus the Finding 2 facet
regressions over the closed L3E envelope preservation (an oversized `x*40_000` content-ful frame
settles not-`pending`; a small `toolUse` then an oversized final `aborted` settles `interrupted`,
never `already-settled`) — both proven non-vacuous by neutralizing the L3E preservation.
`ClaudeInterruptGateTests` (L370): the capability gate refuses claude/unsupported before any native
call (zero adapter calls).

### Conventions

Every path crosses the real socket; only the lost-response classes patch the client boundary inside
the ledger (documented). The service is read from `harness.service` (the `NOW`-anchored instance), so
lease arithmetic is time-consistent regardless of wall clock.

### Invariants And Boundaries

- Acknowledgement ≠ settlement is asserted for every terminal class, per harness.
- Idempotence proofs count native writes (exactly one for identical replay / concurrent same-tuple).
- The pi content-ful and oversized/clipped regressions fail on the exact Finding 1 / Finding 2
  symptoms without the fix and pass with it — non-vacuity is proven, not assumed.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the interrupt contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite exercises the interrupt ledger over the shared topology and the L3E-preserved evidence
fields.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The interrupt ledger under test, incl. the Finding 1 payload-type settlement match. | L87-L449 | [control/operations.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/operations.py) |
| The shared fake-topology harness (real bridge/IPC/authority, `NOW`-anchored service, pi emit helpers). | L88-L520 | [_control_plane.py](agents-remember/mcp/tests/_control_plane.py) |
| The L3E truncation-envelope identity preservation the Finding 2 regressions depend on. | L569-L667 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the interrupt ledger
  suite — codex/pi/claude coverage over the real seam, idempotence write-counting, lost-response
  reconcile, and the Finding 1 content-ful + Finding 2 oversized/clipped settlement regressions
  (non-vacuous). Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
