# dashboard/src/panels/session-cockpit/SessionRail.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T09:45+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom rail suite (260715-FEUI-L2 S4/R11): every ruled rail behavior asserted on REAL DOM over
the shared `FLEET` fixtures.

## Code Commentary

### Logic

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
- **L6 block (R5/R7, 6 cases)** (L648-L776) — End arms an inline confirm NAMING session · leaf ·
  state with ZERO terminates while armed and the exact terminate URL after confirm; a FAILED
  terminate POST (502 + body) renders `role="alert"` with the VERBATIM server words and retry
  fires exactly one terminate after recovery (review finding 4's net); cancel disarms without a
  fetch; the landed-cleanup outcome renders closed + skipped-with-reasons and dismisses; a
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | L348-L889 | [SessionRail.tsx](SessionRail.tsx) |
| The shared fixtures every case builds from. | L10-L172 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The grammar the matrix compares against. | L44-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The notice store + harvest store the L6 block seeds. | L46-L118 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The harvest store the bell/hint cases drive. | L51-L126 | [../../data/ptyHarvest.ts](../../data/ptyHarvest.ts) |
| The typed wire builders the gate/brief cases now call (`lifecycleWithGate`, `taskDoc`, `agentPickup`, `analytics`). | L233-L322 | [../../test/fixtures/wire.ts](../../test/fixtures/wire.ts) |
| `heldGatesByLeafKey` + `briefPendingSessionIds` — the only readers of the seeded lifecycles/pickups, and the reason the richer bases change nothing. | L378-L414 | [../../data/railModel.ts](../../data/railModel.ts) |

## FEUI-L8 Reviewed Candidate Delta

Expands coverage for the relocated legacy list/group duties: role/spawn and master/leaf rendering, attention jumps, completed folders, exact cleanup targets/outcomes, per-row terminate failure/confirm, stale health, and rendered-row virtualization thresholds.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Current L5I Maintenance

The rail suite now pins immediate single-seat termination, retained bulk confirmation, failure
recovery, and the absence of the duplicate bus-footer presentation.

## Update History

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
  consumer is `heldGatesByLeafKey` (`data/railModel.ts` L378-L392), which touches only `doc.lifecycleId`,
  `lifecycles[id]?.gate?.state` and `qualifiedLeafKey`'s `repository`/`docPath`/`id` — all explicitly
  overridden by the case. `briefPendingSessionIds` (L397-L414) reads `messageKind`, `state` and
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
