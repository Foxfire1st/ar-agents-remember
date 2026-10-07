# dashboard/src/ — Mission-Control Cockpit Frontend Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/`                                 |

## 260928-MIK-L29 The Cockpit Gains A Knowledge Mode

The path-based knowledge reader (MIK-R29) is one of the Cockpit destinations. [`cockpit/Cockpit.tsx`](cockpit/Cockpit.tsx.md)
adds `knowledge` to `CockpitView` and "Knowledge" to the mode bar, and passes `initialView="knowledge"` to
`CockpitShell` when the URL hash is a reader address (`#knowledge?…`), so a shared reader link opens on its view.
The reader owns its state in that hash; the shell holds none of it. The panel lives in
`panels/knowledge-reader/` and its adapter in `data/knowledgeReader.ts` (both recorded in their route overviews).

**Since 260928-MIK-L79 the mode is a full-width retained layer, not a transient railed view.** The product bar is
Chats, Operations, Knowledge and File Viewer (in that order); the dashboard opens on Chats; and the four pages that
left the bar (Engine Room, Memory, Topology, Hangar) have no dashboard entry and are not built or fetching at page
load. Knowledge is `fullBleed` and kept mounted (hidden, never unmounted) like the File Viewer, so a document and its
reading position survive a tab switch. The retained pages' layouts are still exercised through injected `initialView`
values. The hash persists across a tab switch, so a reload returns to Knowledge.

- The Knowledge destination in the registry. [1]

- A reader URL opens the shell on the Knowledge view. [2]
- The retained Knowledge layer renders the reader beside the path tree; the former transient ViewBody case is gone. [3]

## 260921-ICR-L32 The Change-Set Read Carries Its Refusal Instead Of Discarding It

The live-leaf "committed" change-set read used to swallow its own refusal detail, so a **refused** read and an **unanswered** one rendered identically — the defect `260921-ICR-L16` routed to this route's owners and R12/R24 both landed without taking. `260921-ICR-L32` applies the R16 treatment here: `data/changeset.ts` no longer clears the counters and stops on a rejected counters read, it carries the refusal's own code and reason through to the caller, and `data/files.ts` follows the same shape for the reader. A read still in flight is a **third** state and is reported as one, so loading, refused-with-a-named-code-and-reason, and answered-with-counts are three distinguishable renderings rather than two. The rendering half lives on `panels/detail-panel/changeSetBar.tsx`, whose cases drive the click and assert the rendered reason; the route's own typecheck rail is `tsc -b` and it is clean on these bytes.

## 260921-ICR-L33 A Landed Master's Leaves, And A Superseded Optimisation

Two of this route's governed sources changed together, and the change is about **what a finished master
looks like once its worktrees are gone**.

> **WITHDRAWN by `a9a1a41b`, recorded by the `260921-ICR-L34` curation.** The paragraph below describes
> the landed-leaf admission and the collapse hook's second half — a change commit **`a9a1a41b`**
> (*"Revert L33's operations-list change; clear the pre-existing ruff-format red"*) took back out. That
> revert was a **direct emergency commit with no curator pass behind it**, so this route went on
> describing a deleted module: `panels/lifecycle-list/landedLeaves.ts` exists in **neither** tree (and
> its sidecar was deleted by this curation), `LifecycleList.tsx` is 1189 lines again with no landed pass
> or default-collapse rule, `hierarchy.test.tsx` is 355 lines again, and `useCollapsedTaskGroups.ts` is
> back to one collapse set with `toggleCollapsed(key)`. The **second** half of this section — the
> per-leaf breakdown in the change-set readers — is **not** affected by the revert and stands.

**The operations list admits landed leaves.** *(withdrawn — see the banner above)* `LifecycleList.tsx` used to render a leaf only while its
worktree physically existed, so a master whose leaves had all closed out rendered as a bare row with
none of its finished work reachable. It now materializes a `Completed` leaf's row under its open master
(`data-landed="true"`), bounded by a default-collapse rule — a master whose only children are its own
landed leaves is held closed and says `N landed` — and by an exclusion that keeps a row carrying OTHER
rows (`structuralChildren.get(row.key) ?? 0 === 0`) from ever being closed, because one such command
row owns a 161-row subtree on the live projection. The rules live in the new
`panels/lifecycle-list/landedLeaves.ts`, and the collapse state gained its second half
(`operations.tasks.opened.v1`) in `panels/useCollapsedTaskGroups.ts` so "the reader opened it" is
representable beside "the reader collapsed it". The header count keeps one meaning — task ENTRIES, not
projected documents (534 documents against 167 entries by default at this leaf) — and now states it in
the `h2`'s own tooltip.

**The series read asks for the breakdown.** `panels/changeset/ChangeSetViewer.tsx` and
`panels/detail-panel/changeSetBar.tsx` both pass `includeLeaves: true`, so a master's net arrives with
one row per leaf; the viewer renders it as a `by leaf (N)` rail whose rows open that leaf's own
committed range — the historical route, which needs no live worktree — and the bar prints the
attribution beside the total. **This supersedes the `includeLeaves: false` optimisation** commit
`a1521685` introduced (its own docstring: callers rendering only the net "can skip those extra per-leaf
git diffs"). The option is retained by `data/changeset.ts` and the serving route; what changed is that
no dashboard master reader is a net-only caller any more. What could not be shown is now NAMED: a
refused read renders the route's own code, status, reason, offending input and next action, and a
change-set that measured empty in both halves says so instead of showing the pick-a-file backdrop.

- The header count itself. **Withdrawn in part:** this row cited a tooltip that stated *what* the count counts ("task entries this list carries"), and the L33 revert removed that tooltip with the landed-leaf change, so the h2 is again a bare `Tasks · {count}`. A reader must not read the number as "task entries" on the strength of this card. [4]
- Both master readers now ask for the per-leaf breakdown. [5]

## 260921-ICR-L25 Four Accepted-Design Defects Fixed Across This Route's Panels

The round-2 acceptance work fixed four defects the accepted design revealed, and each one is a surface
that had been describing a state it was not in. Grouped here because they are one body of work across
this route, with the detail on each panel's own route.

**An unrecorded change-set range is named, not printed as a zero (B6).** A `committed` read of a live
leaf has no landed commit to read yet; the route answered that state with a `404`, which is a browser
console error on the page whose accepted criterion is **zero** — and the bar probes it on every leaf's
open. It is now answered in the body (`state: "unrecorded"` + the route's own sentence), carried by
`data/changeset.ts`'s optional `state`/`stateDetail`, and rendered by
`panels/detail-panel/changeSetBar.tsx` as the control's **own** state with its `+0 −0` total withheld.
An unknown leaf, a bad `mode` and an enclosure `scope` remain three distinct refusals.

**The narrow jump route sits above the family tree, and the empty centre names its own plane (B3).**
The accepted design's finding P2-3 requires the affordance "near the top" because the tree's height is
why it exists; it was rendered below the tree, at `y=1183` in a 900 px viewport. It is now one
`NarrowJump` in `panels/review/ReviewWorkspace.tsx`, between the header and the tree, with the tree
untouched. `panels/review/FamilyReviewCenter.tsx`'s empty sentence said "No family or member is
selected", colliding with the **server's** "selected" used on the same screen; it now says a family or
member has not been **chosen in this column** yet. The measured `data-selection-kind` was `none` and no
tree row carried `aria-current`, so the sentence was never false about its own pane: this is a wording
fix and the centre's layout was deliberately not changed. **One caveat the round-2 verifier measured,
which round 3 then removed on the reviewer's own side (F2):** at 320 px the reviewer had supplied no
scrollport of its own, so with `MAIN` at `overflow-y: hidden` its 7 620 px of content were reachable only
by programmatic focus scroll — the narrow reader's route to the review was not one they could scroll.
`panels/review/ReviewSurface.tsx`'s root is now the scrollport (`userScrollableCount` **0 → 1**, a wheel
over the review moving it **0 → 800 px**), so the affordance reaches a column a reader can actually
scroll. The composition requirement and the wording fix are unchanged by that.

**The review surface's raw colour literal is gone (B1), and the claim is stated in the form that is
true.** `panels/review/FamilyTree.tsx` carried the only two raw literals — `oklch(0.82 0.16 75 / 0.08)`
and `… / 0.16`, `--amber`'s channels copied by hand — and they are now one `AMBER_WASH(percent)` helper
stating `color-mix(in oklab, var(--amber) N%, transparent)`. The interpolation space is the reason it
matters: an `oklch` mix interpolates the **hue**, which is how the accepted page's own selected row first
came out visibly teal. **What is false as worded, and must not be repeated:** *"zero `oklch` users remain
in the review surface"* — the dashboard's own tokens are defined in `oklch` (`styles/tokens.css:8-23`) and
`getComputedStyle` resolves `var(--token)`, so token-resolved `oklch` values are everywhere in the surface
**by design**. **What is true and measured:** the raw amber-wash literal is gone, the wash computes as
`oklab(0.82 0.041411 0.154548 / 0.08)` through `var(--amber)`, and hue **215** appears nowhere in the
review sources. A reader scanning computed styles for the word `oklch` will otherwise conclude the fix
failed.

**A long path wraps instead of being clipped (B7), and B7 took two rounds to close — both readings of
its residual are recorded here.** `panels/review/SourceExplorer.tsx`'s path button gained
`overflow-wrap: anywhere` and `max-width: 100%`; measured at 320 px it was 556 px wide inside a 294 px
column with its right 262 px neither visible nor reachable, because a `mono` path has a very
**min-content** width and `anywhere` — unlike `break-word` — lowers it. Round 2 then claimed the residual
was cockpit chrome *"outside the review surface"*, and **that was false as worded**: the count had been
classified against the **inner** `[data-testid="review-workspace"]` root while the Intent Reviewer's own
root is `[data-testid="review-surface"]` (`ReviewSurface.tsx:906`, mounted by `Cockpit.tsx:585`).
Against the reviewer's own root, **51 of the 64** elements past the right edge at 320 px were **inside**
the reviewer (13 were chrome), the pane sections were 565 px in a 294 px column, and **nothing in the
document was user-scrollable at all**. **Round 3 fixed both halves in the reviewer's own code:** the panes
got `min-width: 0` + `overflow-wrap: anywhere`, the disclosure track became `minmax(0, 1fr)`, the header
row wraps, and the surface root took `height: 100%` / `minHeight: 0` / `overflowY: auto`. Re-measured:
descendants of `review-surface` past the edge **51 → 0**, total **64 → 13**, panes **565 → 294 px** in a
294 px column, the root's own **311/294 → 294/294**, `userScrollableCount` **0 → 1**, a wheel over the
review moving the surface **0 → 800 px**. **The number was not improved by changing the root** — the inner
root's count was 0 in both rounds. **Routed, and now the shell's rather than the reviewer's:** `MAIN`'s
deliberate `overflow: hidden` (`cockpit/Cockpit.tsx:323`, *"the viewport does not scroll — its panel
scrolls on its own"*, shared by every view) and the **13** cockpit-chrome elements, owned by R24's
cockpit takeover. **The shell consequence, stated so it is not lost:** any other panel in this shell that
renders taller than the viewport without its own scrollport has the same defect.

## Hot Path Summary

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

The generated lifecycle schema/types and matching fixture carry only code and memory-content mutation phases. The contract test rejects retired ledger mutation vocabulary; consumer ledger display remains distinct from transaction authority.

The cockpit composes projected task and lifecycle state, while `data/` owns server transport and stores and `panels/` owns task/artifact views. For CCR, start with `data/taskArtifacts.ts`, the notes/requirements reader discriminator, and the versioned lifecycle projection with its server-owned meaningful revision.

## Governing Overview

[agents-remember root overview](../../overview.md)

## Current native Role Chats route

Chats directly mounts one persistent RoleChats pane/Paseo iframe. The dashboard draws no chat navigation of its own (MIK-R75 rules 7 to 10): the host's own list is the navigation, view switches and result reads retain the mounted frame, and the launcher's strip shows only its controls plus one failure line. The plugin's Parent control follows the current native child and its SDK parent/workspace relation, offered only while the live front value is known. Dynamic agent/model/effort/service-tier validation and default/override disclosure retain requested intent separately from observed host values. Historical hosted-session routes elsewhere keep their own scope.

- Current imported source owns this scoped route boundary. [34]

- The route's Role-chats pane owner. [35]
- The route's embedded chat frame. [36]

## L23 Lifecycle Operation Projection

Operations now receives a task-addressed lifecycle-operation projection for closeout and
integration. Hangar and enclosure rows show queued/running/input-required/completed/failed state,
phase, bounded current command, heartbeat age, and guidance without learning a private operation
key or worker PID. Hangar now renders the exact durable command in a one-line ellipsized badge and
keeps the full value in `title`, so viewport pressure cannot create line breaks or require a brittle
character-count cutoff. This is observation only: the dashboard does not become operation authority.

## Purpose

TES-L6 makes sprint provenance a cross-dashboard projection invariant. The data layer preserves
`spawnRepo`/`spawnSprint`, flow models keep equal role names distinct across sprints, and the
session cockpit renders one command group per sprint while isolating unbound legacy rows.

The dashboard frontend is the operator-facing React cockpit. It projects server-composed observer,
task, provider, terminal-catalog, adapter, and control evidence into Operations, Chats, Detail,
Engine Room, file/notes/change-set readers, and supporting panels.

FEUI-L8 deliberately separates strategic ownership:

- [data overview](data/overview.md) — catalog/session state, reliable submit and withdrawal,
  lifecycle cleanup, controls, announcements, and authority boundaries.
- [panels overview](panels/overview.md) — shared panel composition.
- [session-cockpit overview](panels/session-cockpit/overview.md) — the sole full-page Chats product.
- Existing focused child overviews under data, grammar, and panels own their routes. The bounded
  `cockpit/` and `dev/` source slices remain governed here rather than gaining thin overview files.
- [e2e-chats overview](../e2e-chats/overview.md) — the durable, opt-in Chats end-to-end suite
  (260718-CHATS-L5F R7/FB5) is a **sibling** route to `dashboard/src/` (it lives at
  `dashboard/e2e-chats/`, not under `src/`): it boots an isolated real dashboard daemon from the
  worktree and drives the real installed harnesses through this cockpit. Governed by its own route
  overview under the root; linked here for discoverability.

## FEUI-L9R Runtime Truth Repair

Runtime identity crosses this route in three separate ways. The server advertises the fingerprint
of its shipped dashboard while the executing bundle carries its own build-time fingerprint; only a
definite mismatch offers an explicit reload, and absence remains unknown. A new serving boot may
cause exactly one chooser catalog reread and one explicit terminal-socket reattach, but neither is
coupled to SSE loss or a background retry loop. Reattach preserves the mounted xterm and durable
tmux session; transport close alone is not terminal exit.

ARSPAWN-L4 extends that same generated serving-build wire identity with optional Python-source
digest, exact interpreter, and package root. The frontend remains a diagnostic consumer; it gains
no package-update or candidate-selection authority.

## FEUI-MX-FIX-2 Authoritative Session Open

Every browser create entrance now converges on `data/terminalOpen.ts`, the sole client for
`POST /api/terminal`. The opener validates exact request/response identity and accepts only the
server row it returns; raw responses that claim harness/control state are contradictions. The
session store commits and broadcasts only an accepted row, while callers display typed failures and
withhold focus, readiness, submit, and contextual delivery. Request-shaped local rows are not an
alternate success path.

The dev cockpit scenarios replace transport with request-matched raw and harness responses through
the real client seam. They remain fixtures governed by this route overview, not a production
authority — `dev/` remains governed by this overview, including its expanded fixture and probe inventory.

## 260731-EFA-L2 — `dev/` Is A Contract Between Two TypeScript Projects

`dev/` is not only fixtures. `/dev/bench` and `/dev/pty-bench` install probes on `window` so the
Playwright drivers under `e2e/`, `e2e-chats/`, `e2e-production/` and `perf/` can read what the app
actually did — which makes those globals **an interface between two TypeScript programs**: the app
installs them, the drivers read them, and the drivers compile under their own tsconfig project.

`dev/benchProbes.ts` is that interface, declared once. It holds `CockpitBenchProbe`,
`CockpitBenchRequest`, `CockpitBenchTransition`, `CockpitResetAudit`, `PtyFrameStats`,
`PtySerializeProbe` and the `Window` augmentation for `__ptyBench` / `__ptyBenchCols`;
`cockpitScenarios.ts` and `PtyRenderBench.tsx` now import those types rather than each declaring
its own copy. **The module has no imports on purpose** — `tsconfig.driver.json` names it directly,
so the driver program gains the `Window` augmentation without pulling the app's module graph in
behind it. Adding an import to `benchProbes.ts` would drag the app graph into the driver build.

`tsconfig.driver.json` is a new project reference (added to the root `tsconfig.json` alongside
`tsconfig.node.json`) covering `src/dev/benchProbes.ts`, the four e2e/perf suites and the four
Playwright configs under the same `strict` / `noUnusedLocals` / `noUnusedParameters` settings the
app uses. Before it, the driver sources were type-checked by nothing. `tsconfig.node.json` also
picked up `panda.config.ts`, which was likewise unchecked.

The rule this establishes: **a value the browser hands a driver is declared in `benchProbes.ts`.**
Hand-copying a probe field into a spec, or re-declaring `Window`, is how the two halves drift — and
the drift is invisible, because the driver side simply reads `any`.

No production cockpit behaviour, panel, store or authority boundary changed in this leaf.

## 260731-EFA-L4 — Wire Contracts And Typed Vocabularies

This leaf is about what the dashboard's server contract is actually pinned by. Read the first
subsection before writing anything anywhere that cites `fixtures/snapshot.json` or
`types/projection.ts`.

### Generated producer contract, manually sampled fixtures

`dashboard/src/fixtures/snapshot.json` remains a hand-maintained sample. The TypeScript mirror is no
longer hand-maintained: `scripts/sync-projection-types.py` emits the schema artifact and
`types/projection.ts` from `WorkspaceProjection.model_json_schema()` plus the served projection tail,
and its `--check` mode fails drift. The chain therefore separates generated authority from sampled
coverage:

```text
models/projections/workspace.py schema --A--> generated types/projection.ts
                                      ↑ type-checked fixture builders
                                      ↕ measured sample coverage
                               fixtures/snapshot.json
```

- **Producer schema → generated mirror.** Enforced by the projection generator, its Python
  regressions, and `scripts/sync-projection-types.py --check`. A serve-time key added to
  `ServedWorkspaceProjection` is therefore never a one-file change: the generator's folded definition
  set is compared exactly, and the new closed unions reach this side as `contract.test.ts` `Record`s —
  so the companion pair (generated mirror regenerated, `VOCABULARIES`/`KnownUnsampled` registry updated,
  and the served sample in `fixtures/snapshot.json` carrying a value) has to move together, verified
  with `npm run typecheck` plus the contract vitest and not with Python tests alone (`LOCR-R17@v1`
  measured exactly that: a type-only allowlist turns `tsc` green while the runtime walk still fails
  `no served value at projection.terminalObserverHealth.status`).
- **Fixture builders against the mirror.** Enforced by `tsc -b`. Every base in
  `test/fixtures/wire.ts` is assembled from `snapshot.json` **and annotated with its mirror type**,
  so it is pinned from both sides: a required field the mirror gains fails to compile until it is
  filled, and it can only be filled from a served row. Call-site overrides go through
  `Overrides<O, Node>` rather than `Partial<Node>`. `test/wireFixtureGuard.test.ts` refuses the
  one-token moves by which a fixture opts out of the mirror altogether.
- **Generated mirror against the sampled payload.** Enforced by `test/contract.test.ts`, and it
  is **not** a one-way containment. Three type-level directions: the mirror declares everything the
  sample carries (`ServedOnlyPaths` fed to `mirrorMustDeclare`, which fails naming the missing
  path); the sample carries everything the mirror declares (`asServedProjection`, whose *parameter*
  type is the check); and the sample **reaches** every path the mirror declares (`fixtureMustSample`
  — the oracle checking itself, because a path the sample never touches, or an empty array, is
  invisible to the other two). Plus runtime `VOCABULARIES` assertions for the closed string unions
  that `resolveJsonModule` widens to `string`, which nothing type-level on this side can see.
The snapshot itself is not generated, so a green sample-coverage test says the manual sample
exercises the generated contract. The generator separately says the TypeScript contract matches the
producer schema. Keep those claims distinct: sample provenance is manual; producer-to-TypeScript
provenance is generated and stale-checked.

### What `wireFixtureGuard.ts` guards, and exactly where its coverage ends

An AST + type-checker sweep over `src/`, `e2e/`, `e2e-production/`, `e2e-chats/` and `perf/`
(`SCANNED_ROOTS`), answering one question: can a test assert against a payload the server could never
send? `tsc` alone cannot, because every opt-out is one token wide (`as Wire`, `as unknown as Wire`,
`as never`, a `@ts-expect-error`, a literal that lost freshness through a variable, `Object.assign`,
`JSON.parse`). Five rules. Rule 1 — an assertion naming a wire type — runs over every scanned file.
Rules 2–5 run over the **fixture surface** only: files ending `.test.ts(x)` / `.spec.ts(x)`, a path
segment named `fixture(s).ts(x)` or a `fixture(s)/` directory, everything under `src/test/` and
`src/dev/`, any top-level directory whose name starts with `e2e`, and `perf/` (`isFixtureSurface`,
which the guard's test pins with worked examples on both sides). Outside that
surface a cast to a wire type is the decode boundary trusting the server, a different and legitimate
act; those sites live in the test's `SANCTIONED_WIRE_SITES` registry with a written reason, counted
exactly and reconciled in both directions (an entry that stops matching fails too).

**How it discovers the vocabulary, and the blind spot that follows.** It holds no list. `isWireModule`
admits a module when its path starts with `src/types/` **or** its first line matches `MIRROR_MARKER`
— `// TypeScript mirror of` or `// Browser mirror of` (`declaresItselfAMirror`). Seven modules carry
the marker today and `wireFixtureGuard.test.ts` pins that exact set, so a mirror that **loses** its
marker fails loudly. The discovery is fail-closed in one direction only: a module that **never**
carried a marker never enters the vocabulary, and the assertion still passes. Live instances, named
in the guard header and in the test's KNOWN GAP note: `data/harnessCatalog.ts`,
`data/submissionLifecycleClient.ts`, `data/changeset.ts`, `data/files.ts`, `data/notes.ts` — API
clients that declare wire-shaped response types inline beside client-side option and handler types.
Fixtures for those routes are unguarded, and both impossible fixtures this leaf deleted (a `control`
field on the harness-catalog row, a `bridgeEpoch` on `WithdrawalResultWire`) lived in that gap.
Widening the rule to "the header cites a `.py` file" was measured and rejected — it sweeps up the
option types too. The fix is to move those response types into a marker-carrying module: app-code
refactor, not fixture work, and not done here.

Four further holes are recorded in the guard's header rather than left to be inferred from a clean
run: rule 4 reads only `Identifier` / `CallExpression` / `PropertyAccessExpression` / object literal,
so `rows[0]`, `await`, `new` and `rows.at(0)!` escape it; one generic helper defeats rules 1 and 4
together; type predicates and assertion functions narrow with no `as` anywhere; and every rule
measures property **names**, so a correct name carrying an explicit `undefined` is invisible to all
five (which is what `test/fixtures/overrides.ts` exists to cover).

### The state vocabulary — generated from the projection schema and stale-checked

`observer/lifecycle_state.py` **composes** the server's `State` from named halves
(`LiveState` / `EndOutcome` → `TerminalState`), and `check_state_partition` refuses at import any
state filed on neither side, so "which states exist" and "which states are terminal" cannot become
two lists that disagree.

`types/projection.ts` now declares the same partition in the same shape: `LIVE_STATES` and
`TERMINAL_STATES` are written out as the two halves, `LIFECYCLE_STATES` is spread from them
(`[...LIVE_STATES, ...TERMINAL_STATES]`), `State` and `ActiveState` are derived, and `ACTIVE_STATES`
is bound to `LIVE_STATES` **directly** rather than as `Exclude<State, TerminalState>` — so the
second list that could disagree is gone on this side too. It replaced exactly the whole-plus-second-
list shape the Python side had stopped having, which `projection.py`'s "STATE OF THE MIRROR" comment
used to name as not done and now records as done.

**Where the two sides differ is what each can REFUSE, and only in the server's favour.** Composition
makes two of `check_state_partition`'s three refusals unrepresentable on either side. The third —
one state filed on BOTH halves — Python refuses at import; TypeScript refuses at compile time, via
`StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>` with `FiledOnce<S extends never>`, so
`tsc -b` fails naming the offender (`TS2344`). What TypeScript **cannot** refuse is a duplicate
within one half: `Literal["a", "a"]` collapses to one member in Python, while a tuple keeps both, so
`LIVE_STATES = ["running", "running", …]` type-checks clean and is caught only at runtime by
`test/contract.test.ts` (three failures, including "gives each live state a bucket of its own").
Weaker than the server's gate, not absent.

The producer/consumer agreement is now generated rather than maintained as two independent lists.
On producer import, `check_state_partition` refuses invalid state filing and `state_count_fields`
refuses bucket-name collisions. The generator's `_state_partition` then reads the producer `State`
enum and already-validated `Metrics` bucket fields, rejects unmatched mappings, and `_vocabulary_block`
emits the TypeScript partition and enumerable tuples from those schema enums.
`stale_generated_files` compares both committed generated targets with fresh output, so the documented
`scripts/sync-projection-types.py --check` command fails after either a producer-only change or a hand
edit on the TypeScript side, until the artifacts are regenerated cit:(["def check_state_partition(", "def state_count_fields(", "def _state_partition(", "def _vocabulary_block(", "def stale_generated_files("], mcp/src/agents_remember/observer/lifecycle_state.py:74-74; mcp/src/agents_remember/observer/projection.py:267-267; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:439-451; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:475-475; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:602-602; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:487-487; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:614-614).
edit on the TypeScript side, until the artifacts are regenerated cit:(["def check_state_partition("; "def state_count_fields("; "def _state_partition("; "def _vocabulary_block("; "def stale_generated_files("], mcp/src/agents_remember/observer/lifecycle_state.py:74-99; mcp/src/agents_remember/observer/projection.py:267-289; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:451-465; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:487-523; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:614-620).
The separate `contract.test.ts` vocabulary suite still measures whether the manual `snapshot.json`
sample covers every generated member/path and catches a duplicate within one TypeScript tuple; it is
not the cross-language authority.

The sixth state `awaiting-developer` is the notify-and-continue turn end: non-terminal, neither
healthy nor a fault, so every state→colour surface owes it a "your move" treatment rather than a
fall-through to running/ok.

`Metrics` no longer lists buckets. It extends `LifecycleStateCounts`, a mapped type keyed by
`StateCountField<S>` over `ActiveState`, so adding a state adds a **required** field and every object
claiming to be a `Metrics` stops compiling until it counts the new one. That derivation is what the
former hand-written three-bucket list could not do, and why `awaiting-developer` was counted nowhere.
`stateCountField()` is its runtime twin; `metricsFor()` builds the whole rollup from a lifecycle
list, so fixtures state lifecycles instead of re-listing buckets. The camelCase rule is duplicated by
construction (`Camel<>` here, `projection.py::state_count_field` there) and the Python side was moved
to `word[:1].upper() + word[1:]` to agree, because `Capitalize<>` cannot lower-case a tail.

`cockpit/Cockpit.tsx`'s top bar appends a `N awaiting you` segment to the task-metrics chip only
while `metrics.awaitingDeveloperCount > 0` — never a standing `0 awaiting you`, and it does not
displace the running/blocked/tokens rhythm. Before it, the bucket rode the wire and no surface read
it.

Other mirror repairs in the same file: `TaskSubTaskRefNode` and the new `SeriesSubTaskNode` are split
back to one interface per Python model (the collapse had invented a `createdAt` the server never
sends and lent `linkedLifecycleId` to series rows that never carry it); `SeriesSectionNode` gets a
name and a slot while being honest that it is field-identical to `TaskSectionNode` and therefore
structurally interchangeable — it buys a landing place for a future divergence, not a check.
`EngineProcessEdge.refusedPolarity` and its `refused` state are **removed**; the renderer derives
flash polarity from `state`. `ATTENTION_SEVERITIES`, `ATTENTION_LANES`, `PROCESS_FACT_STATES` and
`PROCESS_HEALTHS` became tuples with derived types, because runtime membership checks need
enumerable values. Schema generation now emits `GateNode.evidenceRefs`,
`LifecycleProjection.stateEnteredAt`, and `Analytics.expectationRows` as required fields, matching
their producer schemas rather than preserving the former optional client-tolerance gap.

### Totality replaces defaults in `topology/`

`topology/model.ts` replaced an if-chain ending in `return "ok"` with
`CONSTEL_STATUS_BY_STATE: Record<State, ConstelStatus>` — total by type, so a seventh state stops
that object literal compiling. `CONSTEL_STATUSES` is the tuple `ConstelStatus` derives from, and `UNCLASSIFIED_STATUS` is
the declared answer (`"warn"`) for a state from a newer server.

The subtle part is `STATUS_BY_DECLARED_STATE`, a `Partial<Record<string, ConstelStatus>>` **read
view** over the same table. Indexing `Record<State, …>` directly types the miss away — `tsc` hands
back `ConstelStatus`, never `undefined` — which would make `?? UNCLASSIFIED_STATUS` in
`lifecycleStatus()` read as deletable dead code. The read view is what makes that fallback
load-bearing: delete the `??` and `tsc -b` fails at that line. Remove the alias instead and the
compiler goes quiet while an unclassified state's `undefined` flows onward.
`noUncheckedIndexedAccess` would say the same thing project-wide; it is not on (measured: 601 errors
across 81 files).

`topology/constel.ts` closed the other half of the same defect: the palette was
`Record<string, string>` read through `COLORS[status] ?? COLORS.ok`, so an unclassified state came
out cyan — the healthy fill. It is now `constelColors(cssVar): Record<ConstelStatus, string>`,
extracted out of `mountConstel` so `constel.test.ts` can prove totality without a canvas, with **no**
fallback at the lookup because that key really is a value this package produced.

### Fixture ergonomics: the two type-level devices worth knowing

- `test/servedProjection.ts` — `resolveJsonModule` widens every literal in the payload (`"running"`
  becomes `string`, `3` becomes `number`), so `snapshot.json` can never be *assigned* to a mirror
  that types its vocabularies as literal unions. The old reflex was a double cast
  (`snapshot as unknown as WorkspaceProjection`), which turned off assignability and
  excess-property checking together.
  `AsJsonModule<T>` applies exactly the import's widening to the mirror and nothing else, so
  `asServedProjection()` is a full structural check of everything widening does not touch. Every
  test reading `snapshot.json` must come through it; a second `as unknown as` elsewhere silently
  re-opens the hole for that file.
- `test/fixtures/overrides.ts` — `Overrides<O, T>` replaces `Partial<T>` in the builders because
  `exactOptionalPropertyTypes` is **not set** on this project, so a `Partial<T>` slot admits an
  explicit `undefined` and `lifecycle({ state: undefined })` compiles a required field into absence
  with no cast for the guard to find. `Overrides` binds at the call site, in whichever tsconfig
  project the caller sits in. Its limits are stated in its own header: the override must stay a
  fresh literal, it reaches one level deep, and it binds only `fixtures/wire.ts` and
  `fixtures/conversationWire.ts`. Turning the flag on project-wide was measured at 222 errors across
  71 files and deliberately not attempted here.
- `dev/fixtures.ts` now delegates every node builder to `test/fixtures/wire.ts` and derives `metrics`
  through `metricsFor()`; the gallery keeps its own display defaults by passing them explicitly, and
  no longer keeps a second copy of the required-field list. `dev/cockpitScenarios.ts`'s
  `/api/harnesses` stub uses `satisfies HarnessInfo[]` precisely because `data/harnessCatalog.ts` is
  one of the unmarked modules the guard cannot see. `dev/` remains fixtures, not a production
  authority.

### Checking this route

`dashboard/tsconfig.json` is a **solution-style** config (`"files": []` plus three project
references). `tsc --noEmit` there compiles nothing and exits 0 vacuously — it is evidence of nothing.
The real gate is `npm run typecheck` (`tsc -b`), which is what every "stops compiling" claim above
means. Most of this leaf's guarantees are type-level and free at runtime, so a green `vitest run`
alone does not exercise them.

## Layered Architecture

1. Projection types are generated and stale-checked from the server's Pydantic schema; the separate
   hand-maintained snapshot is measured for fixture coverage.
2. Data modules normalize, reconcile, and retain browser projection state around explicit server
   authorities.
3. Grammar primitives provide shared state words, badges, panels, and markdown treatment.
4. Panels compose focused operator surfaces over the shared stores.
5. CockpitShell owns navigation, persistent keep-alive layers, selection routing, and shell-wide
   drivers.

The terminal catalog and adapter/control routes remain authoritative. Browser state may cache and
project them, but is not a replacement conversation-history database.

## Route Model

### Operations

Chats is the shell's initial destination (260928-MIK-L79). Operations remains a product destination
selected from the four-entry bar; its task list, detail reader, attention, diagnostics,
and contextual RailChat retain their existing contracts. RailChat is useful task-local context, not
a second full-page chat destination.

### Chats

FEUI-L8 removes the legacy Chats/SessionList path and the separate Sessions navigation concept.
CockpitShell exposes one Chats item backed by the persistent session-cockpit layer. That layer keeps
the mechanics built through L1–L7 — role/spawn rail, reliable composer and authoritative pop-back,
interaction answers, lifecycle controls, evidence/capabilities/bus, and status — while adding L8
hardening, accessibility, scenarios, and product-duty transfer.

Since 260718-CHATS-L4 the controlled-session stage body is the structured `ConversationSurface`, not
a PTY: `ChatsStageBody` selects the structured surface (default), the in-stage history library, or
the legacy-raw PTY, and owns the default-off read-only terminal-diagnostics drawer. The exact-turn
interrupt is wired into the WorkingLine as the `conversation.stop` chord. The inspector is
supplementary evidence, closed by default, toggleable, and responsive without overwriting deliberate
user intent. The stage is the primary space.

### Other Full-Page Surfaces

Detail/Operations takeovers, Engine Room, File Viewer, Notes Reader, Change-Set Viewer, and dev-only
design/bench routes retain their existing focused overviews. The L8 split does not introduce another
production view.

## Product Truth And Conversation Boundary (structured renderer landed in 260718-CHATS-L4)

The canonical Chats stage now renders the **structured conversation surface** for controlled
sessions: a harness-neutral grammar over a reconstructable browser projection of the landed L1/L2/L3
adapter-normalized contracts. The controlled runner line-log survives only as the default-off
read-only terminal-diagnostics drawer; legacy raw sessions still host the vendor TUI. This is the one
shared visual message roof across Claude, Codex, and Pi, with visible harness identity and
capability reasons.

The two capabilities are both served and stay distinct: the **active transcript**
([data/conversation](data/conversation/overview.md) + the `conversation/` grammar) and the
**previous-conversation library/index** ([data/conversation-library](data/conversation-library/overview.md) +
the `conversation-library/` browser). Both obtain normalized history/index/resume from the server
contracts and hold only a projection/cache — no durable browser conversation database (R1). UA-1 is
no longer absent. Two forward constraints remain L5 hardening: interrupt capability gating is
attempt-and-reflect on the L3 evidence until a control-capabilities GET or L1-view refresh lands, and
the measured virtualization/scale baseline plus the E1/E2 environmental faults are enumerated in the
`conversation/` L5-Facing Register.

Harness sub-agents are now a first-class additive layer on both capabilities. The active-transcript
data plane carries per-item agent refs (evidence-bound identity, absent on parent items) and keeps
the operator's agent-lane focus outside the projection so it survives LRU eviction and is
re-validated against the live roster. The library groups sub-agent conversations as child rows
under their parent and renders the server's verbatim `agentsNote` when agent history is (partially)
unavailable. Pending interactions are multiplexed: an additive plural wire slot carries sub-agent
approvals alongside the parent's singular slot, and every attention surface — rail badge,
announcer, seat visual grammar, and the palette's question triage — derives from the combined set
via one shared predicate, so a seat blocked solely on a sub-agent approval never goes dark; the
adapter-bound agent label names who is asking, never a fabricated name.

User submissions, agent-to-agent bus messages, lifecycle/control commands, and adapter-interaction
answers remain distinct paths. The original orchestration failure mode was collisions caused by
routing agent communication through the same paste/input channel as operator typing; the dashboard
must not recreate that coupling.

## Invariants And Boundaries

- Chats is the opening view and there is exactly one full-page Chats destination; Operations is a product destination (260928-MIK-L79).
- The shell owns one catalog poll/reconciler for its lifetime. Views do not create competing feeds.
- Focus/inspection may name a landed row; only a live row owns action routing and reload preference.
- Reliable submit and withdrawal preserve request/epoch identity and never blind-resend or locally
  fake an authoritative result.
- Session open is accepted-response-authoritative: failed requests cause no registry row, focus
  movement, readiness transition, or dependent delivery.
- PTYs stay mounted across focus and transient handoff gaps; ended rows never create a live socket.
- Inspector visibility is optional presentation. Core Chats actions remain usable with it closed.
- State words and evidence remain explicit; absent transport/capability/history facts are not
  inferred.
- No Domain Documentation source is configured; direct source/tests, reviewed task evidence, and
  recovered same-repository history are the authority for FEUI-L8 curation.

## Child Route Onboarding Map

| Child route | Governing overview |
| --- | --- |
| `data/` | [Cockpit state and authority](data/overview.md) |
| `panels/` | [Panel composition](panels/overview.md) |
| `grammar/` | [Grammar](grammar/overview.md) |
| `cockpit/` | File cards governed by this overview; shell ownership starts at [Cockpit.tsx](cockpit/Cockpit.tsx.md). |
| `dev/` | File cards governed by this overview; dev scenario authority starts at [cockpitScenarios.ts](dev/cockpitScenarios.ts.md). |
| root ambient types | [vite-env.d.ts](vite-env.d.ts.md) declares the dashboard build fingerprint consumed by the data layer. |

## Evidence

### Docs References

The curator checked `system/sources.md`; it contains no configured Domain Documentation entries.
The L8 architecture statements were verified from repository-local source/tests, task/reports, and
the recovered same-repository history pack.

No relevant domain documentation was found for `dashboard/src`.

### Cross-Repo References

No cross-repository implementation is imported as the dashboard authority. Historical Toad/T3
references informed product framing only; current code truth stays in agents-remember.

No applicable cross-repository implementation source governs this route.

### Repo-Internal References

- Shell navigation, persistent layers and shared drivers. [6]
- State and authority architecture. [7]
- Panel composition. [8]
- Sole Chats route, deletion map, and future boundary. [9]
- Dev scenario authority and end-to-end states. [10]
- Fixture-honesty sweep, its five rules, its scanned roots, and the unmarked-module blind spot. The third anchor is the guard header's own question, quoted as it is written; this row previously carried a paraphrase that occurs in no file. [11]
- State/phase/severity vocabularies and the derived `Metrics` bucket fields. [12]
- Total state-to-status and status-to-colour grammars; the load-bearing unclassified fallback. [13]
- JSON-module widening and the override type that survives `exactOptionalPropertyTypes` being off. [14]

Current working-candidate evidence for this route:

- Public lifecycle recovery commits contain only real code and memory outputs. [15]

## 260718-CHATS-L5I Current Route Impact

The cockpit now treats a focused chat or terminal as a persistent operator surface rather than disposable tab content: switch and hidden-view transitions preserve mounted identity, scroll/selection/geometry state, and only resume visible-only work when appropriate. Its global data consumers also adopt bounded stream/watchdog, single-flight, timeout, build-identity, and wake-lock behavior. Detailed mechanics remain owned by the existing `data/`, `panels/`, and nested session-cockpit overviews; this route records only the shared frontend consequence.

Selection-driven panels also preserve stable external-store snapshot identity when no task-document
projection exists. In particular, `HighlightComposer` uses one shared empty task-document value
rather than allocating an empty array during every snapshot read, preventing a React
`useSyncExternalStore` render loop without changing selection or injection authority.

## 260727-CHATS-IM-L2 No Route-Level Architecture Impact

This leaf changes internals inside existing children: roster identity in `data/conversation/`,
selected-child projection in `panels/session-cockpit/conversation/`, and effect isolation in
`panels/engine-room/`. The dashboard source layering and ownership model described here are
unchanged.

## 260731-EFA-L7 — Conversation-Timeline Wiring

The dashboard route absorbed the L7 live-thinking change on top of the L8 split: the conversation-timeline family now renders one coalesced live `thinking` indicator per active turn (`collapse.ts` stable-row refactor + `ThinkingItem` animated indicator), with acceptance pins in `liveThinking.test.tsx` and `collapse.test.ts`. No dashboard file is over the file-size hard limit; the detector's `dashboard/src` TS/TSX scope is enforced by the project wrapper.

### 260713-TES-L5 Route Impact — Regenerated Projection Schema

The 260713-TES-L5 change set regenerated `dashboard/src/types/projection.schema.json`: the
`AgentPickupNode.description` now surfaces "pending / not yet landed" (N16 turn-boundary
landing; `operator_inbox_consume` attribution-only; sweep predicates never read the
projection).

## L23 Lineage Visibility

The dashboard consumes strict source-lineage projection types, schema, and
fixtures from the server contract. Engine Room shows the aggregate admission
state and full summary; it does not compare branches or choose a sync locally.

## 260815-DAG-L4 L4 Projection Contract

The dashboard projection adds the organizational `super-to-leaf` lineage relation and remains generated from the server schema. Organizational direct-super and atomic super-to-master-to-leaf topology therefore use one closed, parity-tested wire vocabulary.

## 260815-DAG-L14 Dashboard Route

The task-document projection types carry sprint structure: `TaskDocNode.seats` (`TaskSeatNode`)
and optional `TaskSubTaskRefNode.masterRef`; the detail panel threads `docPathForRef` so sprint
rows open their commanded master document.


## 260815-DAG-L12 Route Impact

The sprint execution graph is viewable when present: `types/projection.ts` (+ schema) carry the render-ready `TaskExecutionGraphView`/`TaskExecutionNodeView`/`TaskExecutionPredecessorNode` wire shapes and optional `TaskDocNode.executionGraphView`; `panels/sprint-graph/` is the wave-grid view route; `dev/DevApp.tsx` exposes `/dev/sprint-graph` for mounted-UI evidence; and `fixtures/snapshot.json` exercises the node vocabularies (L12-R1/R2/R4-R7). The sprint-scoped closeout projection is mounted independently, so a valid graph-less atomic-sequential sprint retains scheduling visibility.

## 260821-CLIVE Disposable Scheduling And Discard Audit

The generated projection now exposes closeout scheduling as disposable exact-current state:
service/source condition, bounded source problems with repair actions, and generation-keyed members
with producer-owned classification, priority, order, and reasons. The dashboard renders this view
without owning claims, lifecycle, commit, certification, recovery, or terminal evidence.

Task projections also retain audited discard-before-start history. Detail surfaces show the discarded
identity, reason, timestamp, and proof separately; Operations appends a distinct discarded count to
live progress. A discarded item never increments completion. The JSON Schema remains runtime
authority for numeric, string, fingerprint, and collection refinements; generated TypeScript carries
deterministic refinement documentation rather than pretending those constraints are structural types.


## 260815-DAG Master Full-Gate Repair Route Impact

`fixtures/snapshot.json` extended with a super-to-leaf source-relation entry and two execution-graph view nodes (segment + lump with frontier states) for dashboard vocabulary coverage.

## 260824-PDLS Final Projection Reconciliation

The generated dashboard contract removes the impossible `not-created` invalidation outcome and
the contract suite now forces parity with the producer's always-materialized invalid-empty state.
This keeps the browser on the projection plane: file absence never becomes queue or lifecycle
authority.

## Python 3.14 Generated-Schema Representation

The canonical schema now represents named attention and process `Literal` vocabularies as local
`$defs` enums referenced by their model properties. Their values and the generated TypeScript
surface are unchanged; the dashboard remains a consumer of one server-owned generated contract.

## 260831-CCR-L23 Notes Takeover Widen

The cockpit takeover now distinguishes the artifact kind it opens: the notes reader view marker is
`notes-reader` for a notes target and `requirements-reader` for a task-local requirement
packet, with the shared `TaskArtifactReaderTarget` imported from `data/taskArtifacts.ts`.
Route-shape, takeovers, and layer retention are unchanged; detail lives in the Cockpit.tsx sidecar.

## CCR-R18@v1 Lifecycle Envelope Mirror

260831-CCR-L18 regenerated the lifecycle-operation projection surface consumed by the dashboard: `types/projection.ts` and `types/projection.schema.json` now carry `schemaVersion`/`stateMatrixVersion`, the `incoherent` status, and the identity/componentBindings/worker/approval/recommendedAction envelope cells; `fixtures/snapshot.json` gained the matching fixture samples; `test/contract.test.ts` registers the new signature site and vocabularies. File-level detail lives in the route sidecars.

## Lifecycle Wait Cursor Mirror

`types/projection.ts` carries optional `meaningfulRevision` and `taskIntent` in the versioned lifecycle
operation envelope. The revision is a server-owned observation cursor and the intent is a canonical task digest; neither is a browser-produced activity
counter. `fixtures/snapshot.json` includes the matching sample alongside the coherent projection
fields; the task-artifact takeover remains independently discriminated by notes/requirements.

- The generated lifecycle mirror carries the cursor beside coherent identity and version fields. [16]
- The fixture supplies a meaningful revision for the sample operation. [17]


## Integrated IAS Recovery Contract

The generated lifecycle phase union and schema now include `recovering-private-preparation`. This is a server-owned recovery state projected through the existing lifecycle view; it adds no frontend command or recovery authority. Keep the schema and TypeScript mirror generated from the same producer.

## 260915-KS-L22 The Reviewer Takeover Beside The Change-Set Viewer

The cockpit gained a second identity for an existing full-page takeover without gaining a second
takeover. `ChangeSetTarget` — the value the detail panel and the doc readers hand the shell — now
carries an optional `review` variant holding the reviewed subject's recorded identity, and
`ChangeSetTakeover` dispatches on its presence: `target.review` selects `data-view="intent-review"`
and mounts `panels/review/ReviewSurface` in place of `panels/changeset/ChangeSetViewer`. The
change-set viewer is therefore never mounted for a review and no change-set request is made from
one, which is the reason the variant's own declaration gives for it.

The entry that produces such a target is added **beside** the change-set actions, never in their
place. `DocChangeSetBar` renders a third `ChangeSetButton` labelled "Intent review" only when the leaf
is **live** and it holds a **subject** (`live && subject`) — the same liveness the working change-set
action is gated on (one extracted `leafIsLive` predicate, so the two entries appear and disappear
together and a subject with no live candidate offers neither). The entry carries an identity rather
than a filesystem path, because the browser never chooses the candidate: the resolution layer behind
the route does.

**Superseded 2026-09-20 (260915-KS-L45): the subject stopped being a prop, because as a prop it was
never supplied.** The L22 increment gave `DocChangeSetBar` optional `selectorKind`/`selectorId` props
and gated the entry on `live && selectorId`; no production caller supplied either, so the reviewer
takeover described above was unreachable by navigation. The props are gone. The bar now reads its
subject from `GET /api/review/intent/entries` through the `data/review.ts` client's
`intentReviewEntries(repo, master, leaf)`, carrying the whole catalogue via a `useReviewCatalogue` hook (ICR-R09: every recorded subject with per-row presence and totals, not `entries?.[0]`).
The gate is not weakened: a refusal, an empty list, a rejected promise and a non-live leaf all leave
the subject `undefined`, so **no subject means no button**. What changed is that the subject now comes
from the server's own resolution over the candidate pair rather than from a caller that never existed.

The shell did not move. The reviewer takeover inherits the change-set takeover's full-bleed body, its
`viewport` main and its back link, so it is entered and left exactly as the working and committed
views are; the discriminator is the `data-view` marker, not a new shell mode, navigation item or
store. Route-shape, takeovers and layer retention are as the L23 and CCR-R18 sections above record
them, with one more `data-view` value on the same takeover.

The surface itself is display-only and belongs to the `panels/review/` child route; its data comes
from the read-only client on the `data/` route, which mutates no store. What this route records is
the dispatch: a review is a change-set target that says it is one, so the cockpit reaches the
reviewer with no second takeover path. `260921-ICR-L3` changed nothing here — it added one child
component (`panels/review/SourceContent.tsx`, which a listed inventory row opens into) and one client
function (`reviewSourceContent`), and its own record lives in the `panels/` route overview.

- The target variant that turns the existing takeover into a review. [18]
- The declaration's own reason: the change-set viewer is never mounted for a review — the field's **presence** is what marks a review target, and an empty object is the task-context entry. [19]
- The dispatch, and the `intent-review` view marker it selects. [20]
- The surface a review target mounts in the change-set viewer's place — whose listed inventory entries, since `260921-ICR-L3`, also open into the entry's own content. [21]
- **The reviewer entry: offered for every leaf; since `260921-ICR-L47` it carries no subject (the reviewer chooses one) and shows the comparison's changed-intent counts.** [22]
- **The one predicate both gated entries share.** [23]
- The shared catalogue hook takes repository/task context and calls the existing subject catalogue client. [24]

## 260921-ICR-L2 The Task-Context Review Reaches The Surface

**Route meaning changed: the reviewer entry no longer depends on the server offering a subject.**
`panels/detail-panel/changeSetBar.tsx` gates the button on liveness alone and sends an empty review
target when the entry read answers with nothing or refuses, so the task-context target reaches the
cockpit for every live leaf; `cockpit/Cockpit.tsx`'s takeover dispatch already forwarded an optional
selector, and its review branch now records that fact in a comment. `panels/changeset/ChangeSetViewer.tsx`
widened `ChangeSetTarget.review` to carry an optional selector, where the field's **presence** still marks
a review target and an empty object is the task context. The client (`data/review.ts`) and the review
panel (`panels/review/ReviewSurface.tsx`) carry the rest: the inventory's wire types, an optional
comparison identity, and the rendering of an inventory in all three of its states.

- **The entry that is offered for every leaf; since `260921-ICR-L47` the subject catalogue is read by the reviewer on entry (not by the task entry), and never gates it.** [25]
- **The review target whose selector is optional, with presence marking a review and an empty object meaning the task context.** [26]
- **The takeover branch that mounts the surface for a target with or without a selector.** [27]
- **The client's inventory types and the request that omits the selector when there is none.** [28]
- **The panel's inventory rendering, in all three states, with byte-form rows beside the named ones — re-derived against this candidate, where the review surface's lower half moved.** [29]
- The case that measures the browser half: no subject offered, and the target is still a review. [30]

## 260921-ICR-L16 The Review Route's Refusals Reach The Reader

One change crosses this route's boundary without changing its shape: the Intent Reviewer's **read
outcomes** now reach a reader, on the entry and on the surface.

The review HTTP route answers with its typed result and maps a refusal onto a `400`/`404`/`503` status, so
a refusal lives in the **body** of a non-2xx response. The dashboard's shared client `data/files.ts` reads
only `body.status` and throws — correct for the other serving routes, and the reason a reader saw
`404 Not Found` where the route had published a missing dataset, its reason and the initialization action.
The route now has its own transport owner (`dashboard/src/data/reviewTransport.ts`) whose single GET reads
the body whatever the status and treats a body carrying this route's `state` as the answer, plus one
outcome renderer (`dashboard/src/panels/review/ReviewOutcome.tsx`) that every non-review state goes
through. `data/files.ts` is **untouched**, so this route's other clients keep their semantics.

Nothing about the cockpit's route model, takeover, or panel layout changed: the review surface is still
mounted through the change-set takeover under `data-view="intent-review"`, and the entry bar still lives on
the task-document reader. Two limits are recorded as **routed, not fixed**: an in-flight prop/question
change can still settle an earlier read under a newer header (pre-existing; **R17** with R24), and the
browser-class A01/A13 journeys are not verified here (**R25** with R24/R17).

- **The shared client this route deliberately does not change, whose throw-on-non-2xx is right for the other serving routes.** [31]
- **The review route's own decode: the body is the answer whatever the status.** [32]
- **The one renderer every non-review state goes through.** [33]

## 260921-ICR-L12 The Cockpit Hands The Review's Record To The Surface

`260921-ICR-L12` (`ICR-R12@v1`) adds one prop at the cockpit's change-set takeover:
`ReviewSurface` is mounted with `history="recorded"` when the target's review carries `historical`, and
with nothing otherwise. The browser therefore names **which record** the review is read from and adds
no resolution of its own — the subject and the record both travel from the entry, and the server owns
which comparison that record is.

**Nothing else in the cockpit changed.** The takeover's back contract, the target's subject and the
series/leaf change-set views are untouched, and the entry that produces the historical target is the
change-set bar's closed-leaf branch (see the panels route overview), which is also where the "Intent
review (recorded)" label is chosen. The mounted surface states the record it read in its own header, so
a reader never has to infer from the panes which comparison is on screen.

## 260921-ICR-L17 The Review Read Cycle, The Refresh Control And The Entry's Invalidation

`260921-ICR-L17` (`ICR-R17@v1`) changes four modules under this route and adds two, and it changes no
route, takeover dispatch or target shape:

- **`panels/review/ReviewReadCycle.ts`** (new) owns the review surface's read cycle — the question key,
  one in-flight read per question, newest-read-wins, and the refreshed read as the only one that may
  carry the displayed comparison's identity.
- **`panels/review/ReviewRefresh.tsx`** (new) owns the explicit refresh control and the generation
  notice, whose claim is rendered only when the carrying read has answered.
- **`panels/review/ReviewSurface.tsx`** delegates both and loses its inline `load`, its `useEffect`,
  `targetKeyOf` and its private page-request interface.
- **`panels/detail-panel/changeSetBar.tsx`** makes the entry's catalogue read invalidated by the
  workspace projection the store already republishes, adds the reader's own refresh control, and keeps
  the newest-read-wins guard so a previous leaf's answer cannot win.
- **`data/review.ts`** gains the ninth `intentReview` argument, the `reviewQuery` assembler and the one
  `PREVIOUS_BINDING_QUERY` spelling.

The rule a reader of this route should carry: a generation claim is only ever rendered when a read
answered for the identity it describes, and the identity belongs to exactly one question.
