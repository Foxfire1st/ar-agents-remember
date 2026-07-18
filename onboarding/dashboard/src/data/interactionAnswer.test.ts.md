# dashboard/src/data/interactionAnswer.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/interactionAnswer.test.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L36-L130 | [interactionAnswer.ts](interactionAnswer.ts) |
| The exact-URL/body and in-flight/retry cases at the component level. | — | [../panels/session-cockpit/InteractionBar.test.tsx](../panels/session-cockpit/InteractionBar.test.tsx) |
| The projection types the gate fixture instantiates. | — | [../types/projection.ts](../types/projection.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R4/R9 (incl. fix round 1 finding 2): the
  10-case suite — kind matrix (choices/composer/unrepresentable/empty-prompt/null), open-gate
  matching, exact approve-verb URL+body, verbatim 409 words, no-blind-POST, and the NOT-YET vs
  CANNOT copy split for lifecycle-less seats. Verification metadata pinned to the leaf base until
  closeout stamps the L6 code commit.
