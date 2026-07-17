# dashboard/src/panels/session-cockpit/InteractionBar.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/InteractionBar.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom InteractionBar suite (260715-FEUI-L6 R4/R9): kind-awareness, the gate-only answer path,
and the full round-trip — answering… → verbatim error + retry | answered-waiting. The bar has no
terminal dependency by construction, so xterm never appears here.

## Code Commentary

### Logic

- **`projectGate` helper** (L20-L36): seeds `dashboardStore.lifecycles` with an open
  `agent-question` gate carrying the REAL packet shape
  (`packet.adapterInteraction.{sessionId,interactionId}`) — the exact stamp
  `hosted_interactions.py` writes.
- **Kind-awareness (F8)** (L51-L91): choices render one button per choice + kind chip + the
  honesty hint; non-choice kinds mark the composer (`data-answer-mode`) with the gate-channel
  label; unrepresentable payloads say so with ZERO dead buttons; no pending interaction ⇒
  renders nothing.
- **Round-trip (F7)** (L93-L180): a deferred-promise fetch pins the in-flight `answering…` +
  disabled buttons before release → "answered — waiting" with the poll-bounded copy; the
  500-with-body case asserts the VERBATIM server words and that retry re-sends the SAME body
  (captured fetch bodies compared — `note: "deny"` twice); the missing-gate case proves NO blind
  POST (fetch spy never called) and poll-bounded copy; composer answer-mode asserts the EXACT
  URL + body (`/api/actions/approve`, `{target, gateId, note}`) — never /submit.
- **Stale round-trip state (review finding 5)** (L182-L203): a pre-seeded "answered" record on
  the seat + a FOLLOWING unrepresentable payload ⇒ the store record clears and no answered line
  renders (fails on the old guard that skipped `interactionId === undefined`).
- **Focus + announce** (L205-L227): appearance never steals focus (outside button keeps it) and
  the `role="alert"` region carries the prompt; unmount while holding focus returns it to the
  invoker.

### Invariants And Boundaries

Fetch is stubbed per case (`vi.unstubAllGlobals` in afterEach); stores reset in beforeEach; the
URL/body assertions are the regression net against any drift toward a terminal/queue write.
Test-only.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L79-L293 | [InteractionBar.tsx](InteractionBar.tsx) |
| The gate matcher + POST the suite exercises end-to-end. | L71-L130 | [../../data/interactionAnswer.ts](../../data/interactionAnswer.ts) |
| The L6 interaction fixtures (choices / freetext / unrepresentable). | L205-L257 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The copy constants asserted verbatim (honesty hint). | L54-L71 | [lifecycleCopy.ts](lifecycleCopy.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The suite now drives the shared composer handle across the interaction kind matrix and proves one
exact gate round trip, retained failed-answer text/revision, newer-draft preservation, focus changes,
and stale-interaction rejection. It asserts that `/submit` is not an answer fallback.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: added shared answer-mode, exact retry, revision, and sole-
  channel regression coverage.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4/R9 (13 cases): kind-awareness incl. the
  honest unrepresentable fallback, the exact-URL/body gate-channel assertions, the deferred
  in-flight disable, verbatim-error + same-answer retry, the no-blind-POST missing-gate case,
  the finding-5 stale-answered clear before a following unrepresentable payload, and the
  no-steal/return focus + assertive announce cases. Verification metadata pinned to the leaf
  base until closeout stamps the L6 code commit.
