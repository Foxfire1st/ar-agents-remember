# dashboard/src/data/interactionAnswer.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The **InteractionBar's answer path** (design §7.3): kind classification and authority-routed answers
for pending vendor interactions. Structured question pages and allow/deny permissions use the
session-direct `/api/terminal/{session}/interaction-response` route with the current bridge epoch;
free-text and unsupported shapes retain the matching `agent-question` gate fallback. **NEVER a PTY
write**: on a controlled session a terminal-typed line queues as an ordinary user message and can
never answer the interaction; no terminal code exists in this module, by construction.

For multiplexed seats the module also derives the FULL pending set —
the parent thread's singular `controlPendingInteraction` slot plus the additive plural
`controlPendingInteractions` (harness sub-agent pendings), de-duplicated by interactionId — exposes
the adapter-bound sub-agent label (evidence only, never fabricated), and routes every answer against
the ONE interaction looked up across BOTH slots.

## Code Commentary

### Logic

- **`representPendingInteraction(raw)`** cit:([`representPendingInteraction`], dashboard/src/data/interactionAnswer.ts:136-184) — kind-aware classification of ONE
  `controlPendingInteraction` payload into the `InteractionRepresentation` union cit:([`InteractionRepresentation`], dashboard/src/data/interactionAnswer.ts:53-61):
  structured questions → `questions` (per-question pages through the direct route); choices exactly
  allow/deny → `permission` (direct-route `response`); other choices → `choices` (legacy gate
  buttons); none → `composer` (the composer becomes the answer input, still routed through the
  gate); no usable `interactionId`, or a structured question with no options, → `unrepresentable`
  with an honest reason pointing at the inspector's raw payload — never dead buttons, never
  silently dropped. A missing prompt stays answerable: `prompt` is the empty string, reported not
  invented. Absent payload → `null` (no bar).
- **`pendingInteractionAgentLabel(raw)`** cit:([`pendingInteractionAgentLabel`], dashboard/src/data/interactionAnswer.ts:202-209) — the adapter-bound sub-agent label on a
  multiplexed pending interaction, read from `raw.raw.agentLabel` ONLY (the codex adapter binds it
  when a sub-agent thread raises the request). Absent on the parent thread's singular slot;
  missing/blank → `undefined` — the bar badges WHO is asking only from this evidence, never a
  fabricated name.
- **`pendingInteractionPayloads(session)`** cit:([`pendingInteractionPayloads`], dashboard/src/data/interactionAnswer.ts:208-223) — every pending interaction payload on the
  row: the parent-thread singular slot first, then the multiplexed sub-agent entries from the
  additive plural `controlPendingInteractions`, de-duplicated by interactionId (multiplexed bridges carry
  the parent in BOTH slots). Entries without an interactionId still render (the bar says why they
  cannot be answered) but never dedupe against each other.
- **`representSessionPendingInteraction(session, interactionId)`** cit:([`representSessionPendingInteraction`], dashboard/src/data/interactionAnswer.ts:231-246) — the
  representation of ONE pending interaction by id, looked up across the singular slot AND the
  multiplexed sub-agent entries (`unrepresentable` payloads skipped). Answer-channel routing must
  see an agent permission/questions payload exactly like the parent's — routing against only the
  singular slot silently dropped agent answers into the legacy gate fallback.
- **`findInteractionGate(lifecycles, sessionId, interactionId)`** cit:([`findInteractionGate`], dashboard/src/data/interactionAnswer.ts:258-274) — walks the
  projection for the OPEN `agent-question` gate whose
  `packet.adapterInteraction.{sessionId,interactionId}` matches — the exact identity the
  synchronizer stamps (`hosted_interactions.py`). Null = the gate has not appeared in the
  projection yet (gate creation is observe/poll-bounded) — the caller states that instead of
  inventing an answer path. No invented fields, no fuzzy matching.
- **`answerPendingInteraction(args)`** cit:([`answerPendingInteraction`], dashboard/src/data/interactionAnswer.ts:449-481) — the legacy gate fallback. It trims + rejects
  an empty answer; with no matching gate it splits the copy on the seat's lifecycle binding: a seat
  WITH `sessionLifecycleId` gets the poll-bounded "retry in a moment" truth, a seat WITHOUT one
  gets "cannot be answered from the cockpit" — its gate never projects, since gates ride lifecycles
  (a gate-id-only projection is the recorded upstream ask). With a gate:
  `postGateDecisionDetailed(lifecycleId, "approve", {gateId, note: answer})` — one verb, the note
  IS the vendor response (the durable gate record reads "approved + note"; developer-attributed).
  Failures return the server's words verbatim (retryable by the caller with the same answer).
- **`submitInteractionAnswer(args)`** cit:([`submitInteractionAnswer`], dashboard/src/data/interactionAnswer.ts:654-702) — acquires the per-interaction store lock,
  retains the exact retry payload, then derives channel routing from the session's CURRENT pending
  interaction via `representSessionPendingInteraction(args.session, args.interactionId)`
  cit:([`representSessionPendingInteraction`], dashboard/src/data/interactionAnswer.ts:231-246) — across the singular slot AND the multiplexed agent entries, never the caller's
  say-so and never the parent's singular slot alone. Structured maps → direct-route answers
  covering EVERY question (the backend's all-or-nothing contract — a partial map is refused
  client-side first); permission-kind → direct-route `response`; anything else → the legacy gate
  fallback. A stale bridge epoch is re-read and retried ONCE, then the server's own `not-pending`
  words land instead of a loop.

### Invariants And Boundaries

- Direct responses carry a current bridge epoch and preserve server wording; the gate channel remains
  the fallback for shapes the direct route cannot represent. Neither path writes to a PTY.
- Structured question answers must cover every exact wire question text; a stale epoch gets one fresh
  epoch read rather than a blind retry loop.
- Channel routing is derived from the interaction looked up across BOTH pending slots — an agent
  payload answered through the parent's singular slot would silently fall into the legacy gate
  fallback.
- The plural list is de-duplicated by interactionId (multiplexed bridges carry the parent in both slots);
  id-less entries render but never dedupe. The sub-agent label comes from `raw.agentLabel` only —
  absent evidence renders no badge rather than an invented name.
- Copy honesty still distinguishes a poll-bounded gate fallback from an unavailable answer route; error
  text keeps the server's words verbatim.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Kind classification, the agent label, the multiplexed payload set, and the per-interaction lookup. | `representPendingInteraction`; `pendingInteractionAgentLabel`; `pendingInteractionPayloads`; `representSessionPendingInteraction` | dashboard/src/data/interactionAnswer.ts:157-194; dashboard/src/data/interactionAnswer.ts:202-209; dashboard/src/data/interactionAnswer.ts:218-233; dashboard/src/data/interactionAnswer.ts:241-256 |
| Gate matching, the direct-route POST + epoch retry, the legacy gate fallback, and the locked submit. | `findInteractionGate`; `answerPendingInteraction`; `submitInteractionAnswer` | dashboard/src/data/interactionAnswer.ts:268-284; dashboard/src/data/interactionAnswer.ts:477-509; dashboard/src/data/interactionAnswer.ts:654-702 |
| The `OpenSession` mirror of both pending slots + the catalog mapping that carries them. | `OpenSession` | dashboard/src/data/sessions.ts:28-83 |
| The detailed gate-decision POST carrying the verbatim body back. | `postGateDecisionDetailed` | dashboard/src/data/actions.ts:49-82 |
| The server side: interaction → gate projection + verbatim note return. | `HostedInteractionSynchronizer` | mcp/src/agents_remember/serving/hosted_interactions.py:52-264 |
| The bar that renders one bar per pending payload and badges the agent label. | `InteractionBar` | dashboard/src/panels/session-cockpit/InteractionBar.tsx:54-93 |
| The rail preview naming WHO asks via the same label helper. | `SessionRail` | dashboard/src/panels/session-cockpit/SessionRail.tsx:149-236 |
| The waiting-seat triage titles deriving asker + preview from the helpers. | `SessionsView` | dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx:23-23 |
| The round-trip state slice this path's outcomes land in. | `sessionCockpitStore` | dashboard/src/data/sessionCockpitStore.ts:588-601 |
| The suite: kind matrix, gate matching, structured/direct-route round-trips, agent-label pins, NOT-YET vs CANNOT. | "representPendingInteraction (kind-awareness, F8)" | dashboard/src/data/interactionAnswer.test.ts:67-115 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## Reliable Submit Delta

Answer delivery now preserves the exact pending interaction plus answer text and draft revision
across a retry. The shared lock admits only the matching gate-backed interaction, and successful
clearing is revision-CAS so a concurrent operator edit survives. This remains wholly separate from
prompt submission and PTY input: a normal message can never satisfy a vendor interaction.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 4 repeated path:start-end Citation objects from 2 same-claim citation group(s) at card line(s) 111, 112; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 18 citation entries (27 findings); no Tier-3 findings.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: documented the R6 multiplexed pending-interaction
  path — `pendingInteractionPayloads` (singular slot first, then the additive plural, de-duplicated
  by interactionId), `pendingInteractionAgentLabel` (`raw.agentLabel` evidence only, never
  fabricated), and `representSessionPendingInteraction`, with `submitInteractionAnswer` channel
  routing now looking the interaction up across BOTH slots (the singular-only routing silently
  dropped agent answers into the legacy gate fallback). Refreshed every stale line citation to the
  current source. The L7 code is uncommitted in the code worktree; closeout re-stamps verification.

- 2026-07-24T13:17:50Z — Corrected the dangerous claim that gates are the only answer channel.
  Documented direct structured/permission responses, exact-map validation, epoch retry, and the retained
  gate fallback. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented stored answer/revision retry, shared answer lock,
  and revision-safe clearing on the gate-only path.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4 (incl. fix round 1 finding 2): the sole
  gate-channel answer path — kind-aware representation (choices / composer / honestly
  unrepresentable), open-gate matching by the synchronizer's stamped identity, the
  answer-as-decision-note POST on the approve verb, verbatim failure text, and the NOT-YET vs
  CANNOT copy split on the seat's lifecycle binding. Verification metadata pinned to the leaf
  base until closeout stamps the L6 code commit.
