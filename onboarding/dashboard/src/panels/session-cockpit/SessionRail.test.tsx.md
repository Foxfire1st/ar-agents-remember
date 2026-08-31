# dashboard/src/panels/session-cockpit/SessionRail.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T09:45+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom rail suite (260715-FEUI-L2 S4/R11): every ruled rail behavior asserted on REAL DOM over
the shared `FLEET` fixtures.

## Code Commentary

### Logic

The rail tests now pin separate headers and seat membership for multiple sprint-qualified command
groups. They also pin the migration-only legacy group, ensuring unbound historical rows remain
inspectable without being rendered as the owner or parent of a live bound sprint.

- **Rail-state matrix (R14)** — every fixture row's dot carries exactly the `stateGrammar` visual
  (`data-state`/color/pulse per row); FEUI-L4 also pins `role="img"` and the literal
  `aria-label="state: <word>"`, so the truncation-surviving dot is never color-only.
- **Set attention (L4 R6)** — an unacknowledged unsupported ledger entry renders only that
  seat's `set!` marker with a worded accessible name; explicit acknowledgment removes it.
- **Vocabulary negative (R6)** — plants `resolvedModel`/`resolvedEffort` in fixtures and asserts
  they appear NOWHERE in the rail container; anatomy order dot | role | title | status | End
  proven via `compareDocumentPosition`; the `input?` chip tooltip carries the R16 prompt preview.
- **Ruled hierarchy (R5)** — spine flat, managers flat inside the master box, clusters indented
  with the active seat on top; the tree toggle swaps to the spawn-edge provenance view.
- **Fleet attention (R12)** — live rollup counts as filter buttons focusing the first matching
  seat; **highlight expiry** (fix round 1, finding 3): click → ring, resolve the seat via the poll
  path, re-render → ring gone (fails on the old snapshot-Set code); ZERO-STATE renders nothing
  even with seats working; master headers carry the dominant rollup badge.
- **Gate + brief joins (R13, R8)** — gate badge on rows whose leaf holds an UNDECIDED gate; the
  brief column is strictly two-state.
- **Completed folder + bulk end (R17)** — per-master fold collapsed by default and expandable
  (dormant rows render the compact `✕` End — fix round 1, finding 5); bulk end arms an inline
  preview NAMING every removed session, and the fetch-level assertion captures the exact posted
  sessionIds.
- **Freshness + footer (R15, R8)** — the stale banner past the missed-beat cutoff; anchored bus
  numbers; the honest never-ticked line (never fake numbers). **R5/A4 (260718-CHATS-L5P):** the footer
  heartbeat/cutoff pin is now the HUMANIZED form `heartbeat 2 s / stale cutoff 1 m 0 s` (was the raw
  `heartbeat 2s / stale 60s`); the anchored `2 pending / 0 redeliverable` case is preserved.
- **Cross-surface consistency (R14)** — renders the rail AND a HeaderStrip and diffs the two
  dots' `data-state`/color/pulse attributes (two surfaces, not one function twice).
- **Zero state (R9)** — the empty rail explains itself; waiting(reason) renders steady
  muted-amber when supplied.
- **L6 block (R5/R7, 6 cases)** — cit:(["End terminates the seat IMMEDIATELY — no armed inline confirm (F-g ruling)"], dashboard/src/panels/session-cockpit/SessionRail.test.tsx:645-679): End terminates the selected seat immediately; there is no armed inline-confirm state. The
  selected session identity is carried by the control title, and the first click posts the exact
  terminate URL. A FAILED
  terminate POST (502 + body) renders `role="alert"` with the VERBATIM server words and retry
  fires exactly one terminate after recovery (review finding 4's net). The immediate-terminate case
  asserts that confirm, execute, and cancel controls are all absent; the former cancel test was removed
  with that state. The landed-cleanup outcome renders closed + skipped-with-reasons and dismisses; a
  harvested bell renders the text-equivalent attention marker; harvested title/turn hints join
  the row TOOLTIP as labeled parts while the dot stays pure grammar.

### Invariants And Boundaries

DOM-position and DOM-negative assertions are the anatomy/vocabulary regression net; fetch is
stubbed per case; stores (incl. the L6 `lifecycleNoticeStore` + `ptyHarvestStore`) reset between
cases. Test-only.

**Wire nodes come from the typed builders (260731-EFA-L4).** The two `gate + brief joins` cases no
longer cast object literals (`{…} as never`, `{…} as unknown as Analytics`): they call
`lifecycleWithGate`, `taskDoc`, `agentPickup` and `analytics` from `test/fixtures/wire.ts`, so a field
the mirror does not declare fails `tsc -b` at the call site instead of being erased by the assertion.
Seat rows themselves still come from `FLEET`/`catalogRow` — that is a client-side catalog shape, not a
projection node, and it is unaffected.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | `SessionRail` | dashboard/src/panels/session-cockpit/SessionRail.tsx:155-235 |
| The shared fixtures every case builds from. | `FLEET`; `catalogRow` | dashboard/src/test/fixtures/catalogRows.ts:10-27; dashboard/src/test/fixtures/catalogRows.ts:32-172 |
| The grammar the matrix compares against. | `seatVisualState` | dashboard/src/data/stateGrammar.ts:101-125 |
| The notice store + harvest store the L6 block seeds. | `lifecycleNoticeStore`; `ptyHarvestStore` | dashboard/src/data/sessionLifecycle.ts:68-121; dashboard/src/data/ptyHarvest.ts:51-73 |
| The harvest store the bell/hint cases drive. | `ptyHarvestStore` | dashboard/src/data/ptyHarvest.ts:51-73 |
| The typed wire builders the gate/brief cases now call (`lifecycleWithGate`, `taskDoc`, `agentPickup`, `analytics`). | `lifecycleWithGate`; `taskDoc`; `agentPickup`; `analytics` | dashboard/src/test/fixtures/wire.ts:256-266; dashboard/src/test/fixtures/wire.ts:282-287; dashboard/src/test/fixtures/wire.ts:296-301; dashboard/src/test/fixtures/wire.ts:317-322 |
| `heldGatesByLeafKey` + `briefPendingSessionIds` — the only readers of the seeded lifecycles/pickups, and the reason the richer bases change nothing. | `heldGatesByLeafKey`; `briefPendingSessionIds` | dashboard/src/data/railModel.ts:603-617; dashboard/src/data/railModel.ts:622-634 |

## FEUI-L8 Reviewed Candidate Delta

Expands coverage for the relocated legacy list/group duties: role/spawn and master/leaf rendering, attention jumps, completed folders, exact cleanup targets/outcomes, per-row terminate failure/confirm, stale health, and rendered-row virtualization thresholds.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

The rail suite now pins immediate single-seat termination, retained bulk confirmation, failure
recovery, and the absence of the duplicate bus-footer presentation.

## Update History
- 2026-08-14T06:30+02:00 — L23 final candidate review: rail grouping tests now consume the shared
  fleet task-document fixture, keeping sprint/master/leaf assertions aligned with the scenario
  catalog. Verification remains closeout-owned.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: added rendering coverage for concurrent sprint command
  groups and the isolated legacy bucket. Verification metadata remains pinned until closeout
  stamps the code commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: replaced the obsolete inline-confirm account
  with the current immediate single-seat termination regression, including the title-carried
  identity and one-click POST. The new self-citation is explicit `:1-1` curator input.

- 2026-08-03T09:45+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 16 citation findings (7 missing anchors, 7 malformed sources, and 2 prose citations); one semantically obsolete L6 inline-confirm citation remains reported as Tier 3.

- 2026-08-01T09:45+02:00 — 260731-EFA-L4 curator: two edits. (1) The inline citation for the L6 block
  was `L361-L473`, which now lands inside `completed folder + bulk end`; the
  `L6/F-g: immediate terminate …` describe is `L648-L776`, so it was repaired. (2) Recorded the fixture
  conversion in Invariants: the `gate + brief joins` cases dropped `{…} as never` /
  `{…} as unknown as Analytics` for `lifecycleWithGate` / `taskDoc` / `agentPickup` / `analytics`. I
  verified the described behaviours are unaffected rather than assuming it, because the new bases are
  materially richer: `LC1` now carries `state: "blocked"`, `phase`, `tokens: 1200` and the rest of
  `BASE_LIFECYCLE`, where it previously had only `{ id, gate }`; the task doc gained every required
  `TaskDocNode` field; and the ten `Analytics` lists that were `undefined` are now `[]`. `SessionRail.tsx`
  reads `state.lifecycles` and `analytics.taskDocuments` at L505-L539 and nowhere else, and the sole
  consumer is `heldGatesByLeafKey` (cit:([`heldGatesByLeafKey`], dashboard/src/data/railModel.ts:603-617)), which touches only `doc.lifecycleId`,
  `lifecycles[id]?.gate?.state` and `qualifiedLeafKey`'s `repository`/`docPath`/`id` — all explicitly
  overridden by the case. `briefPendingSessionIds` (cit:([`briefPendingSessionIds`], dashboard/src/data/railModel.ts:622-634)) reads `messageKind`, `state` and
  `deliveredToSession`, also all overridden, and `git diff -U2` confirms no field value inside either
  literal changed. The two residual deltas the sweep warns about do not reach here: this gate sets
  `decisions: []` explicitly (so `BASE_GATE`'s `["approve","revise"]` never applies), and no assertion
  reads a lifecycle state. Behaviour bullets left as written.

- 2026-07-24T13:17:17Z — Curator: recorded immediate-end and rail-declutter regression coverage;
  verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: updated the bus-footer freshness pin to the
  humanized `heartbeat 2 s / stale cutoff 1 m 0 s` form (R5/A4); the anchored pending/redeliverable case
  is unchanged. (The RV-2 rail-row geometry is pinned by the e2e `cockpit.spec.ts`, not this jsdom suite
  — jsdom has no layout.) Verification pinned to the leaf base (`352d5cd`) until closeout stamps the
  candidate commit.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R6/R8 extended the state matrix with accessible dot
  words and added the unacknowledged set-outcome marker/acknowledgment regression. Verification
  metadata is pinned to the contract base until code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R5/R7): added the L6 block — arm/confirm with exact
  URL + zero-kills-while-armed, verbatim 502 failure + single-POST retry (review finding 4),
  cancel-without-fetch, closed+skipped cleanup outcome + dismiss, the text-equivalent bell
  marker, and labeled tooltip hints with the dot-purity pin.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R11; fix round 1 added the
  highlight-expiry case and the dormant-✕ assertion): the rail-state matrix, anatomy +
  model-leakage negatives, ruled hierarchy + tree toggle, attention strip incl. expiry +
  zero-state, gate/brief joins, completed folder + naming bulk end, freshness/footer honesty, the
  cross-surface dot comparison, and the explained zero state. Verification metadata pinned to the
  leaf base until closeout stamps the L2 code commit.
