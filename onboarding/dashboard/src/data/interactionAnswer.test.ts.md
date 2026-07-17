# dashboard/src/data/interactionAnswer.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.test.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The unit suite for the **gate-decision answer path** (260715-FEUI-L6 R4): kind classification,
gate matching, and the answer POST — pinning that the gate channel is the SOLE answer path (no
terminal code exists in the module at all) and that no blind POST ever fires without a matched
gate. 10 cases over `representPendingInteraction`, `findInteractionGate`, and
`answerPendingInteraction`; fetch is stubbed per case (`vi.stubGlobal`), unstubbed in `afterEach`.

## Code Commentary

### Logic

- **`lifecycleWithGate(overrides)`** (L13-L40) — builds a `LifecycleProjection` carrying one gate
  with the synchronizer-stamped `packet.adapterInteraction` identity; defaults = an open
  `agent-question` gate for `seat-1`/`ix-1`.
- **Kind-awareness (F8)** (L46-L88): choices → `choices` mode with the validated view; no choices
  → `composer` mode; missing `interactionId` → `unrepresentable` whose reason names "cannot be
  answered" + "inspector" (never dead buttons); missing prompt stays answerable with the honest
  empty string; absent payload → null.
- **Gate matching** (L90-L108): matches the open `agent-question` gate by (sessionId,
  interactionId) across lifecycles; decided gates and non-question kinds are ignored.
- **Round-trip (F7)** (L110-L190): the answer rides as the decision note on the approve verb —
  asserted against the EXACT URL and body (`/api/actions/approve`,
  `{target, gateId, note}`) (L128-L133); a 409 failure keeps the server's words verbatim
  (`stale-gate` + detail) (L136-L156); a missing gate with a lifecycle states the poll-bounded
  truth AND the fetch spy is never called — no blind POST (L158-L171); a lifecycle-less seat gets
  CANNOT (not "retry in a moment"), fetch never called (review finding 2 regression, fails on
  pre-fix code) (L173-L189).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L36-L130 | [interactionAnswer.ts](interactionAnswer.ts) |
| The exact-URL/body and in-flight/retry cases at the component level. | — | [../panels/session-cockpit/InteractionBar.test.tsx](../panels/session-cockpit/InteractionBar.test.tsx) |
| The projection types the gate fixture instantiates. | — | [../types/projection.ts](../types/projection.ts) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4/R9 (incl. fix round 1 finding 2): the
  10-case suite — kind matrix (choices/composer/unrepresentable/empty-prompt/null), open-gate
  matching, exact approve-verb URL+body, verbatim 409 words, no-blind-POST, and the NOT-YET vs
  CANNOT copy split for lifecycle-less seats. Verification metadata pinned to the leaf base until
  closeout stamps the L6 code commit.
