# dashboard/src/panels/session-cockpit/InteractionBar.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/InteractionBar.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **InteractionBar** (spec §1.2-4, design §7.3): the ONE interaction axis.
Rendered by SessionsView directly ABOVE the composer — it NEVER replaces the composer — and renders
ONE BAR PER pending interaction (review R6): the parent's singular
`controlPendingInteraction` slot first, then the multiplexed sub-agent entries in the additive
plural `controlPendingInteractions`. Each bar badges WHO is asking from the adapter-bound
`raw.agentLabel` when present — never a fabricated name. The landed gate-decision channel is
the SOLE answer path (`data/interactionAnswer` → `POST /api/actions/approve`, the answer as the
decision note; structured AskUserQuestion pages and allow/deny permissions POST the session-direct
interaction-response route instead — channel routing looks up the payload across BOTH slots, so an
agent approval answers exactly like the parent's): on controlled sessions the PTY can NEVER answer —
a terminal-typed line queues an ordinary message, and the always-present honesty hint says exactly
that. Kind-aware (F8): choices → one button per choice; free-text/confirm kinds → the composer
becomes the visibly labeled answer input; payloads with no `interactionId` → an honest
"unrepresentable" line pointing at the inspector's verbatim payload — never dead chrome.

## Code Commentary

### Logic

- **Multiplexed fan-out (review R6)** (L250-L281): `InteractionBar` maps
  `pendingInteractionPayloads(session)` — the parent's singular slot first, then the
  interactionId-deduped agent entries (multiplexing bridges carry the parent in BOTH slots) — to one
  `SingleInteractionBar` per pending payload, keyed by interactionId (`unidentified-<index>`
  fallback); the forwarded ref lands on index 0; zero payloads ⇒ null.
- **Per-payload representation + WHO badge** (L301-L304, L405-L408, L437-L453): each
  `SingleInteractionBar` represents its OWN payload via `representPendingInteraction`; the
  adapter-bound `pendingInteractionAgentLabel` renders as the `interaction-bar-agent` chip and
  joins the aria-label as `<agentLabel> (<sessionLabel>)` — absent on the parent's slot.
- **Id-matched round-trip (review R6)** (L396-L404, L492-L517): the round-trip record is
  per-SESSION, so each bar derives `ownAnswerState` by interactionId match — inflight / verbatim
  error + retry / answered render only on the bar whose interaction the record belongs to; a
  sibling bar never inherits it.
- **Stale-state clear (review finding 5, refined by R6)** (L306-L315): a stored record clears when
  its id is no longer among `activeInteractionIds` (every id currently pending on the session) —
  a SIBLING bar's different id is NOT staleness, while a FOLLOWING unrepresentable payload (id
  absent) still clears the old "answered — waiting" line.
- **Focus honesty** (L317-L336): never steals focus on appearance (the assertive `role="alert"`
  live region covers the poll-bounded appearance for AT users — L418-L428); a `focusin` listener
  remembers the outside invoker, and the unmount cleanup hands focus back when the bar held it.
- **Composer answer-mode** (L338-L350, L475-L488): non-choice kinds mark the shared composer
  (`data-answer-mode` + `aria-description` = the visible gate-channel label) and offer the
  explicit "send composer text as the answer" button (`answerFromComposer`, L368-L384 — empty
  text becomes an inline error, never a blind POST).
- **Round-trip (F7), store-backed** (L352-L366, L492-L517): `submitAnswer`/`submitAnswers` write
  `interactionAnswer {interactionId, inflight}` to the cockpit store (survives view switches),
  then `answerPendingInteraction` resolves to answered (`answeredAt`; the poll-bounded
  `INTERACTION_ANSWERED` copy) or a VERBATIM error + retry that re-sends the SAME answer
  (`retryStoredInteractionAnswer`, L501-L510). Buttons disable while in-flight OR answered
  (L402-L404).
- **Missing-gate honesty (review finding 2)** (L352-L360; `data/interactionAnswer.ts` L449-L470):
  the session (with its `lifecycleId`) rides along so the data layer can distinguish NOT-YET
  (poll-bounded retry copy) from CANNOT (a lifecycle-less seat's gate never projects — the
  upstream-ask copy).

### Invariants And Boundaries

- ZERO terminal writes exist in the answer path — no terminal import in this file or
  `interactionAnswer.ts` (reviewed invariant a); the composer stays the shared element, only marked.
- Multiplexed bars are strictly per-payload: status is derived by interactionId match, staleness
  by absence from `activeInteractionIds` — never by an id DIFFERING from a sibling bar's. The
  agent badge comes only from adapter-bound `raw.agentLabel` evidence, never fabricated.
- The re-answer affordance for an answered-but-never-cleared interaction is DELIBERATELY absent:
  the gate is decided after the 202, so any client re-answer would 409 (`no-open-gate`) by
  construction; the synchronizer itself retries vendor delivery each observe beat. Delivery-state
  row evidence is an upstream ask (worker report, reviewer-accepted skip).
- Unrepresentable payloads must keep pointing at the inspector's raw payload — honesty over
  chrome.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Multiplexing fan-out + per-payload bar: representation, badge, stale clear, focus, composer mode, id-matched round-trip, retry. | L242-L281, L283-L525 | [InteractionBar.tsx](InteractionBar.tsx) |
| The answer path + the plural-pending helpers (`pendingInteractionPayloads`, `pendingInteractionAgentLabel`, `representSessionPendingInteraction`). | L136-L246, L449-L640 | [../../data/interactionAnswer.ts](../../data/interactionAnswer.ts) |
| The payload selector the rail/triage chrome previews (parent first, else first agent entry). | L454-L473 | [../../data/sessions.ts](../../data/sessions.ts) |
| The `interactionAnswer` per-seat slice this bar round-trips through. | L71-L81, L291-L294 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The centralized copy (honesty hint, answered/answering, composer-mode label). | L54-L71 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The view mounting the bar above the composer + the palette triage that focuses it. | L1231, L643-L673 | [SessionsView.tsx](SessionsView.tsx) |
| The inspector's verbatim payload the unrepresentable fallback points at. | L113-L136 | [SeatInspector.tsx](SeatInspector.tsx) |
| The jsdom suite (kind-awareness, round-trip, focus, stale clear, + the multiplexed block). | L1-L521 | [InteractionBar.test.tsx](InteractionBar.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## Reliable Submit Delta

Free-text/confirm interactions now use the shared composer handle and its explicit answer mode,
rather than a bar-owned draft. The exact interaction, stored answer text, and revision survive a
failed gate call for retry; a later edit wins through revision-CAS clearing. Choice interactions
remain direct gate decisions and ordinary submission stays disabled as an answer channel.

## Current Structured-Interaction Maintenance

Structured `AskUserQuestion` interactions now render each question with its own option group. A
multi-select question records a joined single answer only after explicit confirmation; all question
answers submit together through the direct session route once every question is answered. Permission
interactions share that direct route, while legacy shapes retain the gate fallback and unsupported
payloads remain explicit rather than dead controls.

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the multiplexed sub-agent approval
  chrome (review R6) — `InteractionBar` fans `pendingInteractionPayloads` out to one
  `SingleInteractionBar` per pending payload (parent's singular slot first, keyed by
  interactionId), each bar representing its OWN payload, badging WHO asks via the adapter-bound
  `raw.agentLabel` (`interaction-bar-agent` chip + `<agentLabel> (<sessionLabel>)` aria-label),
  and matching the per-session round-trip record by interactionId so a sibling bar never inherits
  inflight/answered/error. Staleness is now absence from `activeInteractionIds` — a sibling's id
  is never staleness. Corrected the pre-L7 claims that the bar appears only for the singular
  `controlPendingInteraction` slot and that the stale clear was raw id-inequality. Source
  uncommitted; closeout re-stamps verification.

- 2026-07-24T13:17:17Z — Curator: documented per-question pages, all-or-nothing answer submission,
  and direct-route versus legacy-gate routing; verification fields remain pre-commit.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented shared-composer answer mode, exact retry state, and
  revision-safe clearing.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4 (F7/F8; review findings 2 + 5 fixed
  in-leaf): the single interaction axis above the composer — gate-only answers with the answer
  as the decision note, kind-aware rendering (choices/composer/unrepresentable), store-backed
  round-trip with verbatim errors + same-answer retry, poll-bounded answered copy, the
  always-present honesty hint, no-steal/return focus discipline, the assertive announce region,
  and the NOT-YET vs CANNOT missing-gate split. The skipped re-answer affordance is recorded as
  a 409-by-construction upstream ask. Verification metadata pinned to the leaf base until
  closeout stamps the L6 code commit.
