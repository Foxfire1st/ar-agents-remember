# dashboard/src/data/setClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

End-to-end unit contract for the set-control I/O driver and its store-visible honesty semantics.

## Code Commentary

### Logic

Exercises exact wire routes and bodies; all acceptance outcomes; clamp, unknown, unsupported, and
route-error state; superseded responses; focused announcements; snapshot classification and
single-flight; queued/unknown promotion; serialized pair success, refusal, and route termination;
effort cycling; and turn/focus watcher triggers.

### Conventions

Fetch is mocked at the boundary while the real reducers and store are used, so assertions cover
the state that UI consumers actually receive.

### Invariants And Boundaries

Tests distinguish requested, pending, echo-evidenced effective, and readback-confirmed values.
They also prove that pair effort cannot POST before model evidence and that route failures cannot
fabricate effectiveness.

### Todos

The final reviewer PASS retains the production sev-4 observations recorded in `setClient.ts.md`;
they are not release blockers for this leaf.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Set, snapshot, promotion, pair, cycling, and watcher cases. | "sendSet — wire + honesty table application"; "refreshSessionSnapshot (R1/F16)"; "queued promotion by readback (R4)"; "serialized pair change (R5)"; "cycleEffortRequested (R7)"; "startSetPromotionWatcher (R4 + v3 drift delta)" | dashboard/src/data/setClient.test.ts:64-228; dashboard/src/data/setClient.test.ts:230-265; dashboard/src/data/setClient.test.ts:267-338; dashboard/src/data/setClient.test.ts:340-536; dashboard/src/data/setClient.test.ts:538-607; dashboard/src/data/setClient.test.ts:609-697 |
| Driver under test. | `refreshSessionSnapshot`; `applySnapshotReadback`; `sendSet`; `applySetResult`; `commitPairDirective`; `startPairChangeFlow`; `acknowledgeSetAttention`; `cycleEffortRequested`; `startSetPromotionWatcher` | dashboard/src/data/setClient.ts:72-119; dashboard/src/data/setClient.ts:149-161; dashboard/src/data/setClient.ts:228-274; dashboard/src/data/setClient.ts:326-348; dashboard/src/data/setClient.ts:352-368; dashboard/src/data/setClient.ts:375-383; dashboard/src/data/setClient.ts:386-391; dashboard/src/data/setClient.ts:405-426; dashboard/src/data/setClient.ts:450-497 |
| Shared deterministic fixtures. | `ENVELOPES_BY_CACHE_STATUS` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:175-179 |
| The shared `observerEvent` builder supplies `schema`/`id`/`trust`/`actor` defaults to every event it creates. | `observerEvent` | dashboard/src/test/fixtures/wire.ts:373-385 |
| The R4 promotion-watcher test routes the turn-ended L2 SEAT-EVENT through `applySeatEvent` using the shared observer-event fixture. | "fires on a turn-ended delivered by L2's SEAT-EVENT channel"; "applySeatEvent("; "observerEvent(" | dashboard/src/data/setClient.test.ts:655-655; dashboard/src/data/setClient.test.ts:670-671 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-04T17:16:00+02:00 — 260731-EFA-L6 S18-B08 curator: split the shared observer-event builder from the R4 SEAT-EVENT test dataflow, regenerated the unique observer-event call extent, and rechecked the narrowed title/call claim. Residual repair after the delta verdict: the R4 routing claim's `applySeatEvent` anchor was bound to the in-test dynamic import, not the routing invocation; rebound it as the exact call anchor `"applySeatEvent("`, and the scoped fixer regenerated the row's sources to the test title and the full routing-call extent that passes the shared observer-event fixture to `applySeatEvent`, dropping the import occurrence. Single-document recheck clean (0 findings).

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 7 citation claims (4 table rows, 3 prose citations); scoped recheck clean (0 findings).

- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **the 09:22 entry's analysis is
  sound and is kept in full; its `No content impact:` header was not.** The conversion introduced a
  new dependency this card did not record — `setClient.test.ts` L12 now imports `observerEvent` from
  `../test/fixtures/wire.ts` and calls it at L671 — while the `Repo-Internal References` table's
  "Shared deterministic fixtures" row named only `capabilityEnvelopes.ts`. A card that needs a new
  reference row has content impact by definition, so the attestation is re-stated as **no
  behavioural impact**, which is what the 09:22 analysis actually establishes. Added the missing row
  pointing at cit:([`observerEvent`], dashboard/src/test/fixtures/wire.ts:373-385), matching the row the same
  curator added on `railModel.test.ts.md`, `interactionAnswer.test.ts.md` and `store.test.ts.md` for
  this identical change; the table is three-column here, so the new row carries three cells.
  Re-verified the kept citations from the working tree: the six describes are at L64/L230/L267/L340/
  L538/L609 and `L63-L694` spans all six in the 697-line source; `seatEvents.ts::applySeatEvent`
  runs L40-L92 with the dedup guard `event.ts <= session.turnStateChangedAt` at L86 exactly as
  described; and the R4 conversion sits inside the cited L667-L680. Verification metadata untouched.

- 2026-08-01T09:22+02:00 — 260731-EFA-L4 curator: No behavioural impact (this entry originally read
  "No content impact"; corrected 11:40 — the card gained a `wire.ts` reference row): the whole diff against
  `abc7cbc` is one fixture conversion in the R4 promotion-watcher case (cit:([`startSetPromotionWatcher`], dashboard/src/data/setClient.ts:450-497)) — the seat event
  it feeds `applySeatEvent` moved from an inline object closed with `as never` to
  `test/fixtures/wire.ts::observerEvent`, and the card makes no claim about how fixtures are built.
  The check that could have made this consequential: `observerEvent` ADDS `schema`, `id`, `trust`
  and `actor` to an envelope that previously carried none of them, so I read the consumer —
  cit:([`applySeatEvent`], dashboard/src/data/seatEvents.ts:40-92) branches only on `event.kind`, resolves the row through
  `event.sessionId ?? event.data.session`, and reads `event.ts` and `event.data.*`; it never looks at
  `trust`, `actor` or `schema`. The one value the R4 case actually measures, the strictly-newer
  `ts: "2099-01-01T00:00:00Z"` against the stored transition (the L86 dedup guard), is byte-identical
  before and after, as is the single-capabilities-fetch assertion. Verified the six describes
  (L64/L230/L267/L340/L538/L609) are unchanged in name and count, and that the L63-L694 citation
  still spans all of them in the now-697-line source.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R1–R8 regression matrix after
  fix round 3 and final reviewer PASS. Base verification metadata is temporary until code commit.
