# dashboard/src/cockpit/Cockpit.memo.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/cockpit/Cockpit.memo.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Render-count regression coverage for the cockpit's persistent, hidden-not-unmounted layers.

## Code Commentary

### Logic

Memoized probes wrap real persistent panels and count parent-driven renders. The suite sweeps cockpit
views, preserves DOM identity and ARIA/display visibility, checks real prop changes still pass the memo
gate, and confirms the right-rail River/Chat switch remains interactive.

### Conventions

Mocks preserve the production export shape and use React's ordinary shallow memo comparison; store-driven
updates inside a panel are intentionally outside these parent-render counts.

### Invariants And Boundaries

The test guards tab-switch reconciliation cost without accepting unmount/remount as an optimization.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry; no external
documentation was invented.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The seven `vi.mock` render-count probes (`counts`, `CountedEngineRoom` … `CountedEventRiver`). | "function CountedEngineRoom()", "function CountedDetailPanel(props: ComponentProps<typeof Real>)", "function CountedSessionsView(props: ComponentProps<typeof Real>)", "function CountedFileViewer(props: ComponentProps<typeof Real>)", "function CountedAttentionQueue(props: ComponentProps<typeof Real>)", "function CountedLifecycleList(props: ComponentProps<typeof Real>)", "function CountedEventRiver()" | dashboard/src/cockpit/Cockpit.memo.test.tsx:32-32; dashboard/src/cockpit/Cockpit.memo.test.tsx:43-43; dashboard/src/cockpit/Cockpit.memo.test.tsx:54-54; dashboard/src/cockpit/Cockpit.memo.test.tsx:65-65; dashboard/src/cockpit/Cockpit.memo.test.tsx:76-76; dashboard/src/cockpit/Cockpit.memo.test.tsx:87-87; dashboard/src/cockpit/Cockpit.memo.test.tsx:98-98 |
| The keep-alive DOM-identity case (same `.rail--left` / `engine-room` / `sessions-view` nodes across switches). | "keeps the visibility/aria contract and DOM identity across switches (keep-alive intact)" | dashboard/src/cockpit/Cockpit.memo.test.tsx:253-290 |
| The production shell owns the persistent layers under test: the `chatsLayer`/`filesLayer`/`operationsLayer`/`engineLayer` consts and the four divs that toggle their `display`. | "const chatsLayer = css({", "const filesLayer = chatsLayer;", "const operationsLayer = chatsLayer;", "const engineLayer = chatsLayer;", "className={engineLayer}", "className={operationsLayer}", "className={filesLayer}", "className={chatsLayer}" | dashboard/src/cockpit/Cockpit.tsx:327-327; dashboard/src/cockpit/Cockpit.tsx:337-337; dashboard/src/cockpit/Cockpit.tsx:342-342; dashboard/src/cockpit/Cockpit.tsx:348-348; dashboard/src/cockpit/Cockpit.tsx:755-755; dashboard/src/cockpit/Cockpit.tsx:760-760; dashboard/src/cockpit/Cockpit.tsx:772-772; dashboard/src/cockpit/Cockpit.tsx:780-780 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is dashboard-local test coverage. | "persistent layers skip the setView reconcile (260721 tab-switch CPU)" | dashboard/src/cockpit/Cockpit.memo.test.tsx:218-322 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:33:03+02:00 — W3-B04 curator: curated 4 table citations and 3 prose citations (7 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **three corrections to the entry
  below, whose own stated purpose was repairing out-of-bounds citations.** (1) It said the file shrank
  "325 → 320 lines". The working tree is **319** (`wc -l dashboard/src/cockpit/Cockpit.memo.test.tsx`
  = 319; `git show HEAD:… | wc -l` = 325 — read off the working tree, not the index). (2) Its own new
  Cross-Repo citation `L1-L320` was therefore **one line past EOF**; corrected to `L1-L319`, and the
  last statement in the file is confirmed at L319 (`});` closing the outer `describe`). (3) It claimed
  the master's `subTasks[0]` shed a `createdAt` "that `TaskSubTaskRefNode` declares on neither side" —
  **false in both directions**. `git show abc7cbc:dashboard/src/types/projection.ts` declares
  `createdAt?: string` on `TaskSubTaskRefNode` at L206-L214, and this same leaf removed it there
  (now L368-L375) and moved it onto the new `SeriesSubTaskNode` (cit:([`SeriesSubTaskNode`], dashboard/src/types/projection.ts:496-503)) as part of splitting one
  interface back into the two `extra="forbid"` server models it had collapsed. So the fixture edit was
  compile-forced by that mirror split, not a tidy-up. The card's conclusion survives — nothing reads
  the subtask row's `createdAt` either way — so only the stated reason changed. Also re-verified the two
  kept ranges by opening them: the first starts at `const counts = vi.hoisted(() => ({` and ends at the
  close of the `CountedEventRiver` probe (cit:(["const counts = vi.hoisted(() => ({", "function CountedEventRiver()"], dashboard/src/cockpit/Cockpit.memo.test.tsx:18-18; dashboard/src/cockpit/Cockpit.memo.test.tsx:98-98));
  the keep-alive identity case is exactly the test cited by cit:(["keeps the visibility/aria contract and DOM identity across switches (keep-alive intact)"], dashboard/src/cockpit/Cockpit.memo.test.tsx:253-290). Widened the `Cockpit.tsx`
  row from `L579-L628` to `L579-L629`: the four `className={*Layer}` divs open at L581/L590/L606/L618
  and the fourth one's `</div>` is at L629, so the old range stopped one line short of enclosing it
  (the four `*Layer` consts at L322/L332/L337/L343 are all inside `L318-L343` as written). Verification
  metadata untouched.

- 2026-08-01T09:30+02:00 — 260731-EFA-L4 curator: **No content impact:** the file changed only in its
  fixtures — the local `taskDoc` now delegates to `test/fixtures/wire.ts`'s typed builder, the master's
  `subTasks[0]` shed a `createdAt`, and the
  hand-listed `metrics` literal became `metricsFor([lc])`. I checked each against what this suite
  measures. `lc.state` is `"running"`, so `metricsFor` differs from the old literal by exactly one added
  key, `awaitingDeveloperCount: 0`; `TopBar` renders the `awaiting you` segment only above zero, so the
  header string is byte-identical — and `TopBar` is not one of the seven counted probes in any case, so
  no render count could move. The dropped `createdAt` was **compile-forced, not a tidy of a field that
  never existed**: at `abc7cbc`, `types/projection.ts` L206-L214 declared `createdAt?: string` on
  `TaskSubTaskRefNode`, and this same leaf split that one interface into two server-faithful mirrors —
  `TaskSubTaskRefNode` (now L368-L375, `createdAt` gone) and the new `SeriesSubTaskNode` (L380-L387,
  where `createdAt` moved) — so once the fixture became a contextually-typed `wireTaskDoc({…})`
  argument instead of an `as TaskDocNode` cast, `subTasks[0].createdAt` no longer type-checked against
  `TaskDocNode.subTasks: TaskSubTaskRefNode[]`. The conclusion is unchanged, because nothing reads it
  either way: `LifecycleList.tsx` L625 reads
  `doc.createdAt` (the `TaskDocNode` field, still declared and still set by the base), never the subtask
  row, and the drill assertion goes through `getByText("Ops Master")`. The four described behaviours
  (probe sweep, ARIA/display + DOM identity, real-prop-change pass-through, River⇄Chat swap) still match
  the four `it` blocks one-for-one. Citation repairs only: the file shrank 325 → **319** lines
  (`git show HEAD:… | wc -l` = 325, working-tree `wc -l` = 319), putting both
  `L…-L324` ranges out of bounds — split into `L18-L103` (the `counts` probes) and `L250-L287` (the
  identity case), cross-repo row to `L1-L319`, and the `Cockpit.tsx` row narrowed from `L263-L760` to
  `L318-L343; L579-L629`, which is where the four `*Layer` consts and their divs actually are.

- 2026-07-24T13:17:50Z — Created for persistent cockpit-layer memoization and keep-alive regression
  coverage. Verification hash/date remain pinned to the pre-commit source stamp.
