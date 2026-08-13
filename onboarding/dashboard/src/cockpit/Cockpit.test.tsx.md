# dashboard/src/cockpit/Cockpit.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:30+02:00                           |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`       |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `../overview.md`                                |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest + Testing Library coverage for production cockpit composition, persistent layers, selection
routing, takeovers, and store updates. The FEUI-L8 cases pin Operations as initial, one Chats item,
no Sessions item or legacy Chats component, persistent same-node `SessionsView` behavior behind the
Chats product label, shell-level reconciliation, and accepted-id-only highlight routing. The sole
JSX mount in `Cockpit.tsx`, not this test's singular query, establishes exact-one source cardinality.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The serving-build suite now distinguishes a stale executing bundle from a matching one. It pins
`data-client-build-current="false"` plus an explicit reload control for a mismatch, and `true` with
no reload control for an exact fingerprint match. The test never exercises an automatic reload
because the product contract requires operator timing.

### Logic

L15 adds the servingBuild stamp assertions (renders commit + boot time when present; absent-field tolerance for old payloads).

260712-TRH-L1 adds a shape-accurate Operations projection and fetch stub for the permanently mounted
cockpit surfaces. It clicks a direct leaf, master, drilled subtask, and lifecycle-bound row while
changing only summary projection objects; each path proves one body request for the unchanged revision
and renders the complete objective after resolution. A second case holds task A, switches to task B,
resolves A late, and proves A cannot contaminate B; B remains one request and hydrates only after its
own response. The fetch fixture returns the response shapes required by the mounted file, harness,
terminal, change-set, and notes surfaces, modeling composition rather than adding production fallback
behavior.

A local `seed(stateName)` applies a `GALLERY` fixture projection to the real Zustand store
(`dashboardStore.getState().applySnapshot(...)`) — the same hydration the dev bench uses. The lazy
`../panels/Terminal` is mocked to a jsdom-safe stub so toggling the rail to chat never pulls xterm (a
canvas probe) into jsdom. `afterEach` runs RTL `cleanup`, resets the `sessions` store, and resets the
dashboard store.

- "rails the Operations view but goes full-bleed for the Engine Room" — seeds `engine-fleet`, renders
  `<CockpitShell />`, asserts the default Operations view has `.shell__body[data-fullbleed="false"]`
  plus both `.rail--left`/`.rail--right`; clicks the `role="radio"` "Engine Room" mode-bar toggle and
  asserts `data-fullbleed="true"`, both rails gone, and the room's `engine-room-header` +
  `engine-room-diagnostics` zones present.
- "keeps the rails for Operations and Memory" — switching to Memory stays railed (`data-fullbleed="false"`).
- "canonical Chats route: full-bleed keep-alive cockpit" (FEUI-L8 S5) — asserts there is no Sessions
  route and finds a `[data-testid="sessions-view"]` implementation node. Its parent layer is hidden on
  Operations, the same captured node is revealed full-bleed under the Chats product label, and
  returning to Operations hides that same node without remounting the PTY owner. The test proves
  existence and same-node persistence; the sole JSX mount/source census proves cardinality.
- "toggles the right rail between the Event River and the leaf chat" (slice L5) — on a railed view the
  default `rail--right` shows the Event River; clicking the `rail-toggle-chat` `role="radio"` segment
  swaps in the single-instance `RailChat` (`rail-chat` testid), and clicking `rail-toggle-river` swaps
  the Event River back, pinning the `railView` switch without unmounting the railed body.
- "rail chat keys by the drilled leaf" (L5 fix 1) — a local `seedDrillableMaster` (+ a
  `taskDoc` factory) seeds a lifecycle-bound master with one authored, drillable leaf. The test selects
  the master, toggles the rail to chat, and asserts the master overview shows no leaf slot yet
  (`rail-chat-no-leaf`); drilling into the master's `subtask-open-1` then makes the `rail-chat-heading`
  contain the **leaf** id (`leaf-one`) and not the master id (`master-x`) — pinning that the rail keys off
  the displayed leaf (via `DetailPanel.onViewLeaf` → the shell's `viewedLeafKey`).
- "workspace rollup — the handoff reaches the header" (**260731-EFA-L4**) — a `withStates(...states)`
  helper clones the `calm` GALLERY lifecycle once per requested state and derives the rollup with
  `metricsFor(lifecycles)` rather than hand-listing buckets beside it. Two cases pin the new top-bar
  segment from both sides: three lifecycles (two `awaiting-developer`, one `running`) put
  `2 awaiting you` inside `[data-testid="task-metrics"]`; a `running` + `blocked` pair makes the same
  node contain no `"awaiting"` at all while still reading `1 running` and `1 blocked` — the segment is
  appended, it displaces nothing, and it never renders a reassurance zero.
- "the left rail shows lifecycle states and attention severities at the same time" (**260731-EFA-L4**) —
  three cases, and they render the **whole `CockpitShell`** rather than the two panels, because the
  panels being siblings in one always-visible rail is exactly the claim under test (the justification
  `grammar/Dot.tsx` previously used for `warn` and `awaiting-developer` sharing amber was true per LIST
  and false per VIEW). A local `railProjection(attentionQueue)` seeds one `awaiting-developer` lifecycle
  plus its `liveEnclosure` (the rail renders a leaf only while a worktree exists) and a `warn`
  `actionable-drift` row. (1) `[data-testid="task-state"]` and `[data-testid="attn-severity"]` both
  resolve a first child, and their `outerHTML` differ — both are amber, so telling them apart is the
  glyph's job. (2) The severity is queried BY ROLE AND NAME — `getByRole("img", { name: "Severity: warn" })`
  must be the `attn-severity` node — because the wrapper used to be a bare `<span aria-label>`, and ARIA
  prohibits naming a `generic`: a `getAttribute("aria-label")` assertion would have passed while the
  computed tree carried nothing. The state dot's label reaches the tree by a different route and is
  asserted as such: React Aria gives the row `role="option"`, whose name-from-content absorbs the span,
  so it is matched by `getByRole("option", { name: /Task progress: awaiting-developer; phase: build/ })`.
  (3) An `axe.run` over a standalone `<AttentionQueue>` render must report zero violations, with
  `color-contrast` and `region` disabled because jsdom has no layout engine; `aria-prohibited-attr` is
  `serious` and is what would fail. Scoped to the panel, not the shell, because axe walks every node it
  is given. (`axe-core` was already a `dashboard` devDependency; this is its first use in this suite.)

**Fixtures are now built through the typed wire builders (260731-EFA-L4).** The local `taskDoc(over)`
factory no longer returns an `as TaskDocNode` object literal — it delegates to
`taskDoc as wireTaskDoc` from `test/fixtures/wire.ts`, so an excess property fails `tsc -b` at the call
site instead of being erased by the assertion. That immediately paid: the master's `subTasks[0]` row in
`seedDrillableMaster` carried `createdAt: "2026-06-20T09:00:00+00:00"`, a field
`TaskSubTaskRefNode` does not declare on either side (`projection.py::TaskSubTaskRefNode` is
`extra="forbid"`), so the server could never have sent it — and it is gone. (`TaskDocNode.createdAt`
itself IS declared and is still set on the doc bases.) Both hand-written `metrics: { lifecycleCount, runningCount, blockedCount, pausedCount,
totalTokens, stalenessHistogram }` literals — in `seedDrillableMaster` and `taskReaderProjection` — are
replaced by `metricsFor([...lifecycles])`, the client mirror of `reducer.py::_metrics` (the two new
projections use it from birth). The hand-kept bucket lists were the reason a new state could be counted
nowhere. Note what this DID change for the older cases: those seeds now receive complete rollups derived
from their own lifecycles rather than the numbers the author typed.

### Invariants And Boundaries

Relies on the shared jsdom stubs in `test/setup.ts` (`matchMedia` for `useShouldAnimate`, `ResizeObserver`
 for React Aria). The ModeBar items are queried by `role="radio"` (React Aria `ToggleButtonGroup`,
single-select), driven by `fireEvent.click`. Uses plain `container.querySelector` + vitest `expect`
(no `@testing-library/jest-dom`). Older cases are pure render assertions; the new body cases stub
browser `fetch` and drive `dashboardStore.applyDelta("analytics", ...)` to reproduce analytics churn
and selection timing.

### Conventions

Shell tests drive the shared gallery fixtures and query stable test ids rather than private styles.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

The shell suite now checks dirty/stale serving-stamp cues, mounted rail and Engine Room identity across
full-bleed switches, and the React.memo export contract for all persistent cockpit layers.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `CockpitShell` under test, and the `fullBleed` derivation the rails-hide cases exercise. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:850-850 |
| `GALLERY` fixtures + the `applySnapshot` hydration pattern. | `GalleryEntry`; `seed` | dashboard/src/cockpit/Cockpit.test.tsx:29-33; dashboard/src/dev/fixtures.ts:11-11; dashboard/src/dev/fixtures.ts:127-131 |
| The shared jsdom stubs the render relies on. | "jsdom omits scrollIntoView"; "jsdom's media elements don't implement playback" | dashboard/src/test/setup.ts:86-86; dashboard/src/test/setup.ts:125-125 |
| The L1 composition cases cover all four reader entry paths, unchanged-revision analytics churn, and late A-to-B response discard. | "renders complete bodies for direct"; "discards task A's late body after selecting task B and hydrates B exactly once" | dashboard/src/cockpit/Cockpit.test.tsx:336-396; dashboard/src/cockpit/Cockpit.test.tsx:398-440 |
| The S5 cutover case proves existence of a `sessions-view` node, no Sessions route, and same-node hide/reveal persistence. | "defaults to Operations" | dashboard/src/cockpit/Cockpit.test.tsx:767-794 |
| The production source census, separately from the singular test query, establishes the sole `<SessionsView>` JSX mount. | "<SessionsView" | dashboard/src/cockpit/Cockpit.tsx:781-781 |
| The `withStates` helper + the two `task-metrics` cases (`2 awaiting you`; nothing at zero). | `withStates` | dashboard/src/cockpit/Cockpit.test.tsx:448-457 |
| `railProjection` / `WARN_ROW` and the three rail cases: differing dot markup, `getByRole("img", { name: "Severity: warn" })` + `getByRole("option", …)`, and the scoped `axe.run`. | `railProjection`; `WARN_ROW`; "keeps a handoff state and a queue warning apart in the one rail that shows both"; "speaks the severity of an attention row into the accessibility tree"; "passes axe on the panel the severity label lives in" | dashboard/src/cockpit/Cockpit.test.tsx:859-907; dashboard/src/cockpit/Cockpit.test.tsx:909-919; dashboard/src/cockpit/Cockpit.test.tsx:921-931; dashboard/src/cockpit/Cockpit.test.tsx:933-949; dashboard/src/cockpit/Cockpit.test.tsx:951-961 |
| The `role="img"` + `aria-label` wrapper (`severityMark`, `data-testid="attn-severity"`) the accessibility-tree assertion targets. | `severityMark` | dashboard/src/panels/AttentionQueue.tsx:49-49 |
| The `Task progress: …; phase: …` label on `data-testid="task-state"` that React Aria's `role="option"` absorbs. | "task-state" | dashboard/src/panels/lifecycle-list/LifecycleList.tsx:673-673 |
| The typed builder the local `taskDoc` factory now delegates to (and the header explaining why the `createdAt` it removed compiled before). | `taskDoc` | dashboard/src/test/fixtures/wire.ts:282-287 |
| `metricsFor()` — the client mirror of `reducer.py::_metrics` these seeds now call instead of listing buckets. | `metricsFor` | dashboard/src/types/projection.ts:339-346 |

## Historical FEUI-L8 Reviewed Candidate Delta

Pins the L8 product cutover: Operations is the initial route, the mode bar has one Chats item and no
Sessions item, and one persistent `SessionsView` layer survives route changes. Highlight delivery
switches/focuses only the accepted exact session.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which this card now verifies.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: removed duplicated Source ranges;
  exact non-fixing check returns zero findings.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 20 citation finding(s); scoped recheck clean.

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the one row citing that file: `metricsFor()` L203-L220 → L246-L257
  (the comment naming `reducer.py::_metrics` at L246, the function at L250). No body claim changed —
  the seeds still call `metricsFor(...)`.

- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: the body listed neither of the two new describes, so
  both were added. cit:(["workspace rollup — the handoff reaches the header"], dashboard/src/cockpit/Cockpit.test.tsx:443-476) pins
  `[data-testid="task-metrics"]` containing `2 awaiting you` for two `awaiting-developer` lifecycles and
  containing no `"awaiting"` — while still reading `1 running` / `1 blocked` — when none are handed back.
  cit:(["the left rail shows lifecycle states and attention severities at the same time"], dashboard/src/cockpit/Cockpit.test.tsx:849-962) renders
  the whole `CockpitShell` on purpose and adds the accessibility-tree assertions: I confirmed against
  `AttentionQueue.tsx` L222-L230 that the severity really is a `role="img"` + `aria-label` wrapper (so
  `getByRole("img", { name: "Severity: warn" })` is a tree query, not an attribute read) and against
  `LifecycleList.tsx` L385-L392 that the state span's label is absorbed by React Aria's `role="option"`,
  which is why the two dots are asserted differently. Recorded the fixture conversion honestly: the
  local `taskDoc` now delegates to `test/fixtures/wire.ts`'s builder, the leaf sub-task's `createdAt`
  (declared by no server model) is gone, and the two hand-listed `metrics` literals became
  `metricsFor(...)` — meaning the pre-existing L1/L5 cases now run against complete derived rollups
  rather than typed-in numbers. `axe-core` was checked in `dashboard/package.json` and was ALREADY a
  devDependency (`^4.10.2`) — this is its first use in this suite, not a new dependency. Citation
  repairs, each re-anchored on its proving symbol: `CockpitShell` L124-L205 → L385-L442 (the old range
  is inside the Panda `cva` block); the S5 cutover case L640-L667 → L759-L788; the sole `<SessionsView>`
  JSX mount L551-L560 → L612-L628; the L1 composition range L329-L434 → L328-L434 so it opens on the
  `describe`. Five rows added for the new coverage and its collaborators.

- 2026-07-24T13:17:50Z — Added persistent-layer and serving-identity regression coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: replaced the retired `<Chats>`/`data-testid="chats"`
  keep-alive claim with the landed S5 evidence: the test proves a found `sessions-view` node persists
  through hide/reveal with no Sessions route, while the separate source census establishes the sole
  JSX mount. Also labeled the former uncommitted-candidate note as historical after landing. Verified
  against code commit `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T12:43+02:00 — FEUI-L9R: documented the client/server fingerprint match and mismatch
  regressions; verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 (R1): added the "Sessions view: full-bleed keep-alive
  layer" describe — same-node identity across switches, display/aria-hidden toggling, full-bleed
  rails-hide, and the scope marker present while hidden. Pure addition; no existing case changed.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
- 2026-07-12T16:45+02:00 — 260712-TRH-L1 reopen correction: added Operations click-to-detail
  composition coverage for direct leaf, master, drilled, and lifecycle-bound readers under analytics
  summary churn, plus a pending A-to-B switch with late A resolution. Verification metadata remains
  blank until closeout stamps the code commit.

- 2026-07-07T10:50+02:00 — L15: servingBuild stamp tests added. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:26+02:00 — 260703-L15 S3: added the serving-build stamp describe — the muted
  stamp renders the snapshot's commit short-hash + "up <boot time>", falls back to `v<version>`
  when the stamp has no commit, and renders NOTHING when the wire carries no `servingBuild`
  (a pre-L15 server; never faked).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: added a `seedDrillableMaster` (+ `taskDoc` factory) and a "rail chat keys by
  the drilled leaf, not the master" case — drilling a master's sub-task makes the `rail-chat-heading` the
  leaf id, not the master, pinning the displayed-leaf key (L5 fix 1). Also mocked the lazy
  `../panels/Terminal` (jsdom-safe) and reset the `sessions` store in `afterEach`. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added a right-rail River⇄Chat toggle case — clicking the
  `rail-toggle-chat` radio swaps the Event River for the single-instance `RailChat` and
  `rail-toggle-river` swaps it back, pinning the `railView` switch on a railed view. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: added the "Chats persistence across view switches" describe — pins that `<Chats>` stays mounted (its parent layer toggles `display` none↔flex) across a view switch and is the **same** DOM node throughout, so the live terminal is never re-created. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-16T02:30 — Created for slice 5f S1: render test pinning the full-bleed rails-hide (Engine
  Room / Topology) vs railed (Operations / Memory) behaviour. Verification metadata pinned until
  closeout stamps the S1 code commit.
