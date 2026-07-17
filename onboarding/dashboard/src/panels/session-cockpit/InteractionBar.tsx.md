# dashboard/src/panels/session-cockpit/InteractionBar.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/InteractionBar.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **InteractionBar** (260715-FEUI-L6 R4, spec §1.2-4, design §7.3): the ONE interaction axis.
Rendered by SessionsView directly ABOVE the composer — it NEVER replaces the composer — and only
while the focused row carries `controlPendingInteraction`. The landed gate-decision channel is
the SOLE answer path (`data/interactionAnswer` → `POST /api/actions/approve`, the answer as the
decision note): on controlled sessions the PTY can NEVER answer — a terminal-typed line queues an
ordinary message, and the always-present honesty hint says exactly that. Kind-aware (F8):
choices → one button per choice; free-text/confirm kinds → the composer becomes the visibly
labeled answer input; payloads with no `interactionId` → an honest "unrepresentable" line
pointing at the inspector's verbatim payload — never dead chrome.

## Code Commentary

### Logic

- **Representation switch** (L91-L94, L210-L256): `representPendingInteraction` yields
  `choices` / `composer` / `unrepresentable`; the kind chip + prompt render for representable
  kinds (`INTERACTION_NO_PROMPT_TEXT` when the prompt is empty).
- **Stale-state clear (review finding 5)** (L96-L105): the round-trip record clears whenever
  `answerState.interactionId !== interactionId` — INCLUDING `interactionId === undefined` (a
  FOLLOWING unrepresentable payload must never render beside a stale "answered — waiting" line).
- **Focus honesty** (L107-L126): never steals focus on appearance (the assertive `role="alert"`
  live region covers the poll-bounded appearance for AT users — L203-L209); a `focusin` listener
  remembers the outside invoker, and the unmount cleanup hands focus back when the bar held it.
- **Composer answer-mode** (L128-L140, L240-L253): non-choice kinds mark L5's composer
  (`data-answer-mode` + `aria-description` = the visible gate-channel label) and offer the
  explicit "send composer text as the answer" button (`answerFromComposer`, L175-L189 — empty
  text becomes an inline error, never a blind POST).
- **Round-trip (F7), store-backed** (L146-L173, L257-L285): `submitAnswer` writes
  `interactionAnswer {interactionId, inflight}` to the cockpit store (survives view switches),
  then `answerPendingInteraction` resolves to answered (`answeredAt`; the poll-bounded
  `INTERACTION_ANSWERED` copy) or a VERBATIM error + retry that re-sends the SAME answer
  (`lastAnswerRef`, L142/L266-L277). Buttons disable while in-flight OR answered (L191-L193).
- **Missing-gate honesty (review finding 2)** (L151-L156): `session.lifecycleId` rides along so
  the data layer can distinguish NOT-YET (poll-bounded retry copy) from CANNOT (a lifecycle-less
  seat's gate never projects — the upstream-ask copy).

### Invariants And Boundaries

- ZERO terminal writes exist in the answer path — no terminal import in this file or
  `interactionAnswer.ts` (reviewed invariant a); the composer stays L5's element, only marked.
- The re-answer affordance for an answered-but-never-cleared interaction is DELIBERATELY absent:
  the gate is decided after the 202, so any client re-answer would 409 (`no-open-gate`) by
  construction; the synchronizer itself retries vendor delivery each observe beat. Delivery-state
  row evidence is an upstream ask (worker report, reviewer-accepted skip).
- Unrepresentable payloads must keep pointing at the inspector's raw payload — honesty over
  chrome.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Representation, stale clear, focus discipline, composer mode, round-trip, retry. | L79-L293 | [InteractionBar.tsx](InteractionBar.tsx) |
| The gate-only answer path: representation, gate match, answer POST, copy split. | L36-L130 | [../../data/interactionAnswer.ts](../../data/interactionAnswer.ts) |
| The `interactionAnswer` per-seat slice this bar round-trips through. | L71-L81, L291-L294 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The centralized copy (honesty hint, answered/answering, composer-mode label). | L54-L71 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The view mounting the bar above the composer + the palette triage that focuses it. | L367, L644-L646 | [SessionsView.tsx](SessionsView.tsx) |
| The inspector's verbatim payload the unrepresentable fallback points at. | L113-L136 | [SeatInspector.tsx](SeatInspector.tsx) |
| The 13-case jsdom suite (kind-awareness, round-trip, focus, stale clear). | L51-L227 | [InteractionBar.test.tsx](InteractionBar.test.tsx) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4 (F7/F8; review findings 2 + 5 fixed
  in-leaf): the single interaction axis above the composer — gate-only answers with the answer
  as the decision note, kind-aware rendering (choices/composer/unrepresentable), store-backed
  round-trip with verbatim errors + same-answer retry, poll-bounded answered copy, the
  always-present honesty hint, no-steal/return focus discipline, the assertive announce region,
  and the NOT-YET vs CANNOT missing-gate split. The skipped re-answer affordance is recorded as
  a 409-by-construction upstream ask. Verification metadata pinned to the leaf base until
  closeout stamps the L6 code commit.
