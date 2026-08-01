# dashboard/src/data/setClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Set, snapshot, promotion, pair, cycling, and watcher cases. | L63-L694 | [setClient.test.ts](setClient.test.ts) |
| Driver under test. | L1-L433 | [setClient.ts](setClient.ts) |
| Shared deterministic fixtures. | — | [../test/fixtures/capabilityEnvelopes.ts](../test/fixtures/capabilityEnvelopes.ts) |
| The shared `observerEvent` builder the R4 promotion-watcher case (L671) now feeds `applySeatEvent`; it supplies the `schema`/`id`/`trust`/`actor` defaults the old inline envelope lacked. | L369-L381 | [../test/fixtures/wire.ts](../test/fixtures/wire.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **the 09:22 entry's analysis is
  sound and is kept in full; its `No content impact:` header was not.** The conversion introduced a
  new dependency this card did not record — `setClient.test.ts` L12 now imports `observerEvent` from
  `../test/fixtures/wire.ts` and calls it at L671 — while the `Repo-Internal References` table's
  "Shared deterministic fixtures" row named only `capabilityEnvelopes.ts`. A card that needs a new
  reference row has content impact by definition, so the attestation is re-stated as **no
  behavioural impact**, which is what the 09:22 analysis actually establishes. Added the missing row
  pointing at `../test/fixtures/wire.ts` (`observerEvent`, L369-L381), matching the row the same
  curator added on `railModel.test.ts.md`, `interactionAnswer.test.ts.md` and `store.test.ts.md` for
  this identical change; the table is three-column here, so the new row carries three cells.
  Re-verified the kept citations from the working tree: the six describes are at L64/L230/L267/L340/
  L538/L609 and `L63-L694` spans all six in the 697-line source; `seatEvents.ts::applySeatEvent`
  runs L40-L92 with the dedup guard `event.ts <= session.turnStateChangedAt` at L86 exactly as
  described; and the R4 conversion sits inside the cited L667-L680. Verification metadata untouched.

- 2026-08-01T09:22+02:00 — 260731-EFA-L4 curator: No behavioural impact (this entry originally read
  "No content impact"; corrected 11:40 — the card gained a `wire.ts` reference row): the whole diff against
  `abc7cbc` is one fixture conversion in the R4 promotion-watcher case (L667-L680) — the seat event
  it feeds `applySeatEvent` moved from an inline object closed with `as never` to
  `test/fixtures/wire.ts::observerEvent`, and the card makes no claim about how fixtures are built.
  The check that could have made this consequential: `observerEvent` ADDS `schema`, `id`, `trust`
  and `actor` to an envelope that previously carried none of them, so I read the consumer —
  `seatEvents.ts::applySeatEvent` (L40-L92) branches only on `event.kind`, resolves the row through
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
