# dashboard/src/data/interactionAnswer.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **InteractionBar's answer path** (260715-FEUI-L6 R4, design §7.3): kind classification, gate
matching, and the answer POST for pending vendor interactions — the ONE ruled answer channel.
Pending interactions are already projected into `agent-question` gates server-side
(`serving/hosted_interactions.py`), and a gate decision's note is returned VERBATIM to the exact
pending interaction (`_gate_response` prefers `decisionNote`) — so answering = `POST
/api/actions/approve` with the answer text as the note, against the matching gate. **NEVER a PTY
write**: on a controlled session a terminal-typed line queues as an ordinary user message and can
never answer the interaction; no terminal code exists in this module, by construction.

## Code Commentary

### Logic

- **`representPendingInteraction(raw)`** (L36-L58) — kind-aware classification (F8) of one
  `controlPendingInteraction` payload into the `InteractionRepresentation` union (L21-L26):
  choices present → `choices` (buttons); absent → `composer` (the composer becomes the answer
  input, still routed through the gate); no usable `interactionId` → `unrepresentable` with an
  honest reason pointing at the inspector's raw payload — never dead buttons, never silently
  dropped. A missing prompt stays answerable: `prompt` is the empty string, reported not invented
  (L16-L17, L54). Absent payload → `null` (no bar).
- **`findInteractionGate(lifecycles, sessionId, interactionId)`** (L71-L87) — walks the
  projection for the OPEN `agent-question` gate whose
  `packet.adapterInteraction.{sessionId,interactionId}` matches — the exact identity the
  synchronizer stamps (`hosted_interactions.py`). Null = the gate has not appeared in the
  projection yet (gate creation is observe/poll-bounded) — the caller states that instead of
  inventing an answer path. No invented fields, no fuzzy matching.
- **`answerPendingInteraction(args)`** (L98-L130) — the SOLE answer POST. Trims + rejects an
  empty answer (L108-L109); with no matching gate it splits the copy on the seat's lifecycle
  binding (review finding 2, fix round 1): a seat WITH `sessionLifecycleId` gets the poll-bounded
  "retry in a moment" truth, a seat WITHOUT one gets "cannot be answered from the cockpit" — its
  gate never projects, since gates ride lifecycles (a gate-id-only projection is the recorded
  upstream ask) (L110-L118). With a gate: `postGateDecisionDetailed(lifecycleId, "approve",
  {gateId, note: answer})` (L119-L122) — one verb, the note IS the vendor response (the durable
  gate record reads "approved + note"; developer-attributed, the carried OQ-E residual). Failures
  return the server's words verbatim (F7 — retryable by the caller with the same answer)
  (L124-L129).

### Invariants And Boundaries

- The gate channel is the ONLY answer path: zero terminal imports here or in the bar
  (reviewer-audited — no `sendInput`/`conn.send`/`paste`/`/submit` anywhere in the path).
- Gate matching uses only server-stamped identity; there is no blind POST — no gate, no fetch.
- Copy honesty: NOT-YET (lifecycle present, poll-bounded) vs CANNOT (no lifecycle) must stay
  distinct; error text keeps the server's words verbatim.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Classification, gate matching, and the answer POST. | L36-L130 | [interactionAnswer.ts](interactionAnswer.ts) |
| The detailed gate-decision POST carrying the verbatim body back. | L40-L83 | [actions.ts](actions.ts) |
| The server side: interaction → gate projection + verbatim note return. | L47-L88; L194-L204 | [../../../mcp/src/agents_remember/serving/hosted_interactions.py](../../../mcp/src/agents_remember/serving/hosted_interactions.py) |
| The bar that renders the representation and drives the round-trip store state. | L86-L180 | [../panels/session-cockpit/InteractionBar.tsx](../panels/session-cockpit/InteractionBar.tsx) |
| The round-trip state slice this path's outcomes land in. | L71-L79; L288-L294 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The suite: kind matrix, gate matching, exact URL+body, verbatim failure, no blind POST, NOT-YET vs CANNOT. | L46-L190 | [interactionAnswer.test.ts](interactionAnswer.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

Answer delivery now preserves the exact pending interaction plus answer text and draft revision
across a retry. The shared lock admits only the matching gate-backed interaction, and successful
clearing is revision-CAS so a concurrent operator edit survives. This remains wholly separate from
prompt submission and PTY input: a normal message can never satisfy a vendor interaction.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: documented stored answer/revision retry, shared answer lock,
  and revision-safe clearing on the gate-only path.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4 (incl. fix round 1 finding 2): the sole
  gate-channel answer path — kind-aware representation (choices / composer / honestly
  unrepresentable), open-gate matching by the synchronizer's stamped identity, the
  answer-as-decision-note POST on the approve verb, verbatim failure text, and the NOT-YET vs
  CANNOT copy split on the seat's lifecycle binding. Verification metadata pinned to the leaf
  base until closeout stamps the L6 code commit.
