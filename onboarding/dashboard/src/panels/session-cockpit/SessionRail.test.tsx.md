# dashboard/src/panels/session-cockpit/SessionRail.test.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The component under test. [1]
- The shared fixtures every case builds from. [2]
- The grammar the matrix compares against. [3]
- The notice store + harvest store the L6 block seeds. [4]
- The harvest store the bell/hint cases drive. [5]
- The typed wire builders the gate/brief cases now call (`lifecycleWithGate`, `taskDoc`, `agentPickup`, `analytics`). [6]
- `heldGatesByLeafKey` + `briefPendingSessionIds` — the only readers of the seeded lifecycles/pickups, and the reason the richer bases change nothing. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Expands coverage for the relocated legacy list/group duties: role/spawn and master/leaf rendering, attention jumps, completed folders, exact cleanup targets/outcomes, per-row terminate failure/confirm, stale health, and rendered-row virtualization thresholds.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Current L5I Maintenance

The rail suite now pins immediate single-seat termination, retained bulk confirmation, failure
recovery, and the absence of the duplicate bus-footer presentation.
