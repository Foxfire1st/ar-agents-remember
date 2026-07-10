# dashboard/src/data/sessionGroups.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionGroups.test.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `fdff55f2921d7aaa8ba240c11087d02c15a170d7`       |
| lastVerifiedCommitDate | 2026-07-10T15:53:23+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit tests for the pure L16 rail grouping in `data/sessionGroups.ts`. The grouping is store-free, so
repo isolation, membership, tiering, malformed-claim handling, enclosure independence, and the
30-chat shape are pinned as data-in/data-out cases; `SessionList.test.tsx` covers rendering.

## Code Commentary

### 260707-HFX2-L17 Binding-Role Grouping Proof

Adds a stale-provenance case proving command-deck classification follows current `seatRole`, so a
session rebound as a command seat is not misgrouped by its original spawn role.

### Logic

Eight cases cover: a command-claiming sprint beside claim-less command roles; an uncommanded sprint;
the no-orchestration flat run; explicit landed-only archive membership; valid grouping without
consulting enclosure casing/liveness; a 30-chat fleet split into two sprint boxes plus the landed
archive and a flat command remainder; identical master folders isolated by repository (including
the repo guard on `orchestrates`); and an explicit error group for malformed leaf claims.

### Invariants And Boundaries

Pure logic tests (no DOM, no store). Fixture builders satisfy the full `TaskDocNode` /
`EnclosureNode` projection shapes so type drift in the mirror surfaces here.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The derivation under test. | L48-L159 | [sessionGroups.ts](sessionGroups.ts) |
| The component suite pins forest completeness, manager collapse, width bounding, and hover recovery. | L114-L420 | [SessionList.test.tsx](../panels/SessionList.test.tsx) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: proved sprint group classification is binding-role
  authoritative when spawn provenance disagrees.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16: rewrote the grouping expectations for one
  repo-qualified box per sprint, enclosure-independent valid claims, claim-less command rows, the
  malformed-claim error box, same-folder cross-repo isolation, and the revised 30-chat shape.
  Verification metadata stays pinned until closeout stamps the eventual L16 code commit.

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive, round 2 F4 fix): `status:"landed"` rows
  route into the new collapsed "landed archive" group; legacy `status:"exited"`/absent-enclosure rows
  no longer fold into that group (round-1 behavior) and instead route to the pre-existing `ungrouped`
  ("Open sessions") bucket, so the landed-archive group only ever contains rows the backend
  landed-cleanup endpoint can actually close. Asserts `ungrouped == ["legacy-exited","active-absent"]`
  style expectations. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-07T21:17+02:00 — 260707-HFX-L6 review remediation: deck membership tests now
  expect the developer-facing architect chat plus backend orchestrator/strategist/manager command
  seats on the deck, and the at-scale fixture uses an architect command session. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-06T23:56:18+02:00 — 260703-L14 (visual hierarchy + chat grouping): created — deck
  membership by role provenance + orchestration claim, uncommanded-master grouping, the D3
  flat-run zero-group regression, landed/absent archive roll-up, the case-insensitive leaf join,
  and the 30-chat scale fixture. Verification metadata pinned until closeout stamps the L14 commit.
