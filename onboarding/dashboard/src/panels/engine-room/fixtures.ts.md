# dashboard/src/panels/engine-room/fixtures.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/fixtures.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T15:10+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[engine-room overview](overview.md)

## 260731-EFA-L8 Change

The file was trimmed to 1,197 physical lines in the fix round (FL1): the transient
`edgeState` extraction was reverted to the `state ?? fallback` write path and three
comment/blank lines were removed, closing the 1,202-line physical breach against the
L7 detector's `wc -l` semantics. Scenario content is unchanged.

## Purpose

Provides the scenario fixtures for the enclosure-centered Engine Room process map (slice 5e, 05e §11). Each `EngineRoomScenario` is a set of server-shaped `EngineProcessNode`s plus the official/workspace provider stack, so the dev gallery and component tests can render the map without a live projection. The set covers the discrete boot/lifecycle states (bootstrap, setup running, GrepAI failure, CGC fallback, memory blocked, sync needed, cleanup pending) and a step-through of one enclosure being assembled after `worktree_start`.

## Code Commentary

### Logic

cit:([`EngineRoomScenario`], dashboard/src/panels/engine-room/fixtures.ts:19-23) names a `{ name, processes, workspace }` triple; `ENGINE_ROOM_SCENARIOS` cit:([`ENGINE_ROOM_SCENARIOS`], dashboard/src/panels/engine-room/fixtures.ts:721-1197) is the exported array consumed downstream. Node shaping is factory-driven: cit:([`wsEngine`], dashboard/src/panels/engine-room/fixtures.ts:26-35) builds a ready workspace `ProviderNode` (role inferred from id — memory/grepai → `memory`, else `code`), and cit:([`WORKSPACE`], dashboard/src/panels/engine-room/fixtures.ts:37-37) is the shared `[codegraphcontext-code, grepai-memory]` stack reused by every scenario. cit:([`ref`], dashboard/src/panels/engine-room/fixtures.ts:108-110) wraps a `CommitRefNode` defaulting `factState: "observed"`; cit:([`boot`], dashboard/src/panels/engine-room/fixtures.ts:112-119) builds a `ProviderBootNode` for the code/memory role; `edges` cit:([`edges`], dashboard/src/panels/engine-room/fixtures.ts:141-212) emits the `EngineProcessEdge[]` graph (worktree-add, cgc-seed, and — when `external` — ledger-map + grepai-clone, plus an optional sync edge), each edge state overridable via cit:([`EdgeStates`], dashboard/src/panels/engine-room/fixtures.ts:131-138). `engineProcess` cit:([`engineProcess`], dashboard/src/panels/engine-room/fixtures.ts:214-268) is the core builder: it derives the worktree group path from `repoName`/`id`, fills a nominal `worktree-started` enclosure (leaf id, commit refs, external memory, provider boots, completed phases, source files), then spreads `over` last so each scenario overrides only the fields it varies. `bootStages` are the six `engine-boot-*` build-up frames, **renumbered B0→B5 in slice 5i** to match the
scenario-player beats: `engine-boot-0-main-only` (the official line at rest — worktree refs `planned`, no
providers, every edge planned, no `missingFacts`: a not-yet-created enclosure is not an alarm) →
`-1-code-worktree` (code worktree forks in; `worktree-add` complete) → `-2-memory-contract` (memory copies
in, the coupler binds; `ledger-map` complete) → `-3-providers-dim` (the runtime deploys, engines materialise
`configured`/dim, clone conduits begin) → `-4-seeding` (CGC seeds + GrepAI clones, engines charge cyan) →
`-5-nominal` (the idle constellation), spread into the export tail. The discrete scenarios include `engine-fleet` (a five-process mixed fleet), the single-state cards, and (5g G5) `engine-integration-conflict` (`phase: integration-blocked` + an `integration` edge `state: blocked` — the t14c terminal STOP) and `engine-abandoned` (`phase: abandoned` — the t18 dissolve). The `edges()` emitter gained an optional `integration` edge (worktree → official-line) alongside `sync`, and (2026-06-21) a companion `integration-mem` edge (`fromNode: "memory-worktree"` → `toNode: "memory-source"`, `kind: "integration-mem"`) that mirrors the code `integration` edge on the **memory lane** — the memory worktree integrates ff-only back into the feat SOURCE before the carryover (feat → main mem). It is emitted only with `external` memory and is **skipped when `states.integration === "blocked"`**, so the all-or-nothing integration conflict keeps a single code-lane STOP (no second gate duplicated onto the memory lane). Slice 5h adds the `landingRef` helper and two successful-landing scenarios — `engine-landing-ffonly` (T14: `integrationStrategy: "ff-only"`, source pushed + PR open, memory carryover planned) and `engine-landing-merged` (T14b/T16: replay, PR merged + memory carried over, cleanup pending) — plus a default `landing: []` on `engineProcess` so every prior fixture satisfies the new required field. 5h H2 adds a third landing scenario, `engine-landing-closeout` (`phase: closeout-pending`), so the T13 closeout train has a fixture. The 5h cleanup pass drops the unused `engine-empty` scenario (the bench gallery separately filters the `engine-boot-*` build-up frames out of its tab strip — see `dev/fixtures.ts` — while the component tests still import them from here). The 5h ledger popover adds the `LEDGER_ROWS` window (25 served rows, the newest mapping `08e9221a ⇄ d60a0511` so the popover highlights it) + `LEDGER_TOTAL` and the exported `OFFICIAL_LEDGER` (`LedgerNode`); the default `engineProcess` factory now carries `ledgerRows: LEDGER_ROWS` + `ledgerRowCount` (so every external-memory worktree coupler is live), while the no-real-worktree fixtures (`engine-memory-blocked`, `engine-precontract-blocked`) override `ledgerRows: []` (fact-honest — a blocked start has no ledger mapping). **5h Tier 2** enriches each `LEDGER_ROWS` entry with the per-side `codeSubject`/`codeDate`/`memorySubject`/`memoryDate` — the 4 real 5h commits get real messages + dates, the 21 generated rows get stepped synthetic ones — so the expanded bench popover's 6 columns read complete (the honest no-metadata fallback is asserted in a render test, not the fixture). **5h H4** gives `engine-cleanup-pending` a settled `landing[]` (origin-feat/PR `merged`, `origin-main` `tip`, `origin-mem-main` `pushed`) + `integrationStrategy: "ff-only"`, so the cleanup teardown's "back into main" seam + historical chip have data to read. **Slice 5i** turns these landing fixtures into the D2→D6 tear-down beats the scenario player walks: `engine-landing-merged` is re-typed `phase: "integration-pending"` (D4 — the enclosure is INTACT, the de-materialise is the *next* beat), `engine-cleanup-pending` becomes the **D5 de-materialise** (its `codeWorktree`/`memoryWorktree` go `factState: "planned"` / `(detaching)` and `providers: []` so the worktree side fades + the engines power down while main stays solid), and a new **`engine-retired`** fixture is the **D6 stack removed** (worktree refs `(removed)`/`planned`, `landing: []`, `providers: []`, `cleanup: "done"` — only the official line + a dim historical chip remain). The boot edges now carry the `worktree-add` lane state through B0→B2. **Slice 05k** then **splits the previously-collapsed D2·D3 beat** by adding a new **`engine-landing-pushed`** scenario (appended to the export tail, before `...bootStages`): the **D3 "code lands"** frame — `phase: "integration-pending"`, `integrationStrategy: "ff-only"`, with a `landing[]` of `origin-feat` (`pushed`), `pr` (`merged`), `origin-main` (`tip`, advanced) and **`origin-mem-main` still `planned`** ("after carryover"). It sits between D2 (`engine-landing-ffonly`, integrate / push / PR-open) and D4 (`engine-landing-merged`, memory carryover) so the code-lands-then-memory-carries order is fact-honest in its own beat; the dev scenario player wires it into the tear-down timeline. **Slice 05o** adds a small `memoryBlockStages` array (spread into the export tail after `...bootStages`) holding **two `boot-demo`-identity** frames for the T3B memory/ledger-block arc — `engine-boot-memory-verify` (`phase: code-worktree`, `edges({ worktreeAdd: "complete", ledger: "running", … })` with the memory worktree still `factState: "planned"`, so the code lane is solid while the ledger-map lane is being verified — this is the frame that drives the cyan scan-ring) and `engine-boot-memory-blocked` (`phase: worktree-started`, `health: "blocked"`, `edges({ ledger: "blocked", … })`, the memory worktree `factState: "missing"`, `ledgerRows: []`, `nextAction: "reconciliation"` — the gate + ghosted-lane beat). They are deliberately the **same `boot-demo` enclosure** as the boot stages so the memory-block scenario's recover reuses `engine-boot-2/3/4/5` and animates as ONE enclosure (no remount); the existing `engine-memory-blocked` (a different `v12-feature` identity) stays the static GALLERY card. Named `engine-boot-*` so the bench gallery hides them (scenario-player frames only). **Slice 05o T1B** then adds a parallel `staleBaseStages` array (spread into the export tail after `...memoryBlockStages`) holding **two more `boot-demo`-identity** frames for the stale-base preflight arc — `engine-boot-stale-verify` (`phase: code-worktree`, `edges({ worktreeAdd: "running", … })` with the **code worktree still `factState: "planned"`** so it drives the code-lane preflight scan; the base staleness is not decided yet — this is the cyan scan-ring beat) and `engine-boot-stale-blocked` (`phase: worktree-started`, `health: "blocked"`, `codeSource.behindSource: 3`, both worktrees `planned`, **all edges `planned`**, `actions` `fast-forward`/`proceed-stale`, `nextAction: "fast-forward"`, and `missingFacts` carrying a contract-not-yet-written fact so it reads as a **FLEETING born-blocked enclosure with the main code node pruned/dormant**). Same `boot-demo` identity as the boot stages so the stale-base scenario's recover reuses the boot/clone frames and animates as one enclosure. **Slice 05o** then rounds out the six remaining failure-mode arcs, all reusing the `engineProcess`/`edges` builders (no new node types): The refuse-and-reroute beat is expressed with a plain `EdgeStates.cgc` state, not a bespoke flag: an earlier `cgcRefused: "amber" | "red"` field made the `cgc-seed` edge emit `state: "refused"` plus a `refusedPolarity`, and BOTH were fictions — `EngineProcessEdge` (`extra="forbid"`) declares no `refusedPolarity`, its documented state vocabulary never listed `refused`, and no reducer path has ever emitted it. The lane now carries `cgc: "stale"`, which `_seed_edge_state` really does return, and the renderer derives the amber polarity from it. The new fixtures are `engine-boot-abandoned` (T18, appended inside `bootStages` — the live `boot-demo` enclosure DISSOLVES with no landing: `phase: "abandoned"`, `health: "skipped"`, providers/landing `[]`, worktree refs `(detaching)`/`planned` — terminal, no recover tail); `providerBlockStages` (T7B — the provider-PLAN verify → block beats: `engine-boot-provider-verify` `setupState: "running"` with both worktrees observed so the scan anchors AT the worktree engine, then `engine-boot-provider-blocked` `setupState: "blocked"` with the engines never lighting); `seedFaultStages` (T9B — `engine-boot-seed-fault` flashes the `grepai-clone` `failed` + the GrepAI engine `down` while CGC stays `indexing`, then `engine-boot-seed-retry` re-seeds); `engine-cgc-seed-refused` (T9C — a discrete `device-mgmt`-identity card where the `cgc-seed` conduit flashes AMBER because the lane is `edges({ cgc: "stale", … })` and `refusedPolarityOf` maps `stale`→amber; `seedFallback: true` drives the center-out reindex pulse, SOFT so `health` stays `running`, no gate. The scenario keeps its `-refused` name — "refused" is the beat's name, not the edge's state — and its `currentPhase`/`summary` now read "seed stale — reroute"); `liveSyncStages` (T12B — a `live-sync` enclosure: `engine-sync-moved` (memory `behindSource: 2`, a soft notification) → `engine-sync-memory-blocked` (`health: "blocked"`, `ledger: "blocked"` so only the memory lane gates) → `engine-sync-recovered` (the default rest state after the ff)); and `engine-integration-conflict-flash` (T14C — a `boot-audio`-identity transient CONFLICT FLASH: `edges({ integration: "failed" })`, which (since the builder only suppresses `integration-mem` when `state === "blocked"`) emits BOTH return lanes in `failed` so the refused-conduit RED flash fires on both, before the next frame flips to the steady `engine-integration-conflict` STOP). The three stage arrays are spread into the export tail as `...providerBlockStages`, `...seedFaultStages`, `...liveSyncStages` (after `...staleBaseStages`), while `engine-cgc-seed-refused` and `engine-integration-conflict-flash` sit inline among the discrete scenarios.

### Invariants And Boundaries

Fixtures are presentation data only: they encode the wire shape (camelCase, `exclude_none` optionals) and carry no behavior. They must stay in lockstep with the imported node types in [types/projection.ts](../../types/projection.ts) — fields like `factState`, `health`, edge `state`, and `phase` use the unions defined there. cit:([`SOURCE_BRANCH`], dashboard/src/panels/engine-room/fixtures.ts:25-25) and the hard-coded commits (`08e9221a`, `d60a0511`) are illustrative, not live. Health/setup/edge state strings must remain valid members of `ProcessHealth` and the edge-state vocabulary so the map renders honestly — and "valid" means the SERVER's vocabulary, not the renderer's tolerance. `EngineProcessEdge` is `extra="forbid"`, so a fixture inventing a field (`refusedPolarity`) or a state (`refused`) that the reducer cannot produce describes a payload the server would reject; the scenario then exercises a branch no user can ever reach. Every fixture edge state must be one `_seed_edge_state`/`_materialize_edge_state` can actually return. `seedFallback: true` in `engine-cgc-fallback` cit:([`ENGINE_ROOM_SCENARIOS`], dashboard/src/panels/engine-room/fixtures.ts:721-1197) models a reroute-to-reindex, not a failure; `retryArgs` appears only on failed-setup scenarios. The active provider `runtimeState` is kept consistent with the running conduit (5g G4) — the engine being seeded/cloned is `indexing`, the done engine `nominal` — so the charging engine lines up with the flowing conduit (e.g. GrepAI cloning ⇒ `[boot("code"), boot("memory", "indexing")]`).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Node/edge types this file shapes — the import list here, resolving to the mirror there. | `EngineProcessEdge` | dashboard/src/types/projection.ts:162-170 |
| `EngineProcessEdge` server model — `extra="forbid"`, no `refusedPolarity`, no `refused` in the state comment. | `EngineProcessEdge` | mcp/src/agents_remember/observer/projection.py:791-810 |
| `_seed_edge_state` returns `stale` for the reroute case — the state this fixture now carries. | "def _seed_edge_state(" | mcp/src/agents_remember/observer/reducer_impl/_processes.py:634-634 |
| `EngineRoomScenario` interface + exported `ENGINE_ROOM_SCENARIOS` | `EngineRoomScenario`, `ENGINE_ROOM_SCENARIOS` | dashboard/src/panels/engine-room/fixtures.ts:19-23; dashboard/src/panels/engine-room/fixtures.ts:721-1197 |
| `engineProcess` core builder (override-last spread) | `engineProcess` | dashboard/src/panels/engine-room/fixtures.ts:214-268 |
| `edges` / `EdgeStates` graph emitter (incl. the `integration` + memory-lane `integration-mem` edges); `EdgeStates` no longer carries a `cgcRefused` flag and the `cgc-seed` lane takes `states.cgc` straight through. | `edges`, `EdgeStates` | dashboard/src/panels/engine-room/fixtures.ts:132-139; dashboard/src/panels/engine-room/fixtures.ts:141-212 |
| `engine-cgc-seed-refused` — the T9C scenario, now `edges({ cgc: "stale", … })` with `seedFallback: true`. | "engine-cgc-seed-refused" | dashboard/src/panels/engine-room/fixtures.ts:834-834 |
| `bootStages` six-frame build-up (B0 main-only → B5 nominal, 5i), spread into the export tail | `bootStages` | dashboard/src/panels/engine-room/fixtures.ts:275-417 |
| `engine-retired` (D6 stack-removed) + the D4/D5 split (`engine-landing-merged` integration-pending, `engine-cleanup-pending` de-materialise) | "engine-retired" | dashboard/src/panels/engine-room/fixtures.ts:991-991 |
| `engine-landing-pushed` (05k, D3 "code lands": feat `pushed` · PR `merged` · origin/main `tip` · origin/mem-main still `planned`) — the D2·D3 split | "engine-landing-pushed" | dashboard/src/panels/engine-room/fixtures.ts:1165-1165 |

## Series-Contract Notes

Engine Room scenario factories now emit leaf enclosure contract paths (`tasks/<repo>/<task>/enclosures/<leaf-id>/series-contract.md`) in both `enclosure` and `sourceFiles`, and seed `leafId` from the fixture id by default. This keeps fixture source traces and rendered labels aligned with the backend resolver.

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the FL1 trim to 1,197 physical lines. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: removed duplicated Source ranges
  from the `ENGINE_ROOM_SCENARIOS` and `edges`/`EdgeStates` rows; exact non-fixing check returns
  zero findings.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 24 citation findings (8 rows plus prose); scoped recheck clean.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations — the reference row and the restatement in the 10:56 entry
  below. `EngineProcessEdge` cit:([`EngineProcessEdge`], mcp/src/agents_remember/observer/projection.py:791-810)
  is the class with the `extra="forbid"` model and the documented state vocabulary. No body claim changed.

- 2026-08-01T10:56+02:00 — 260731-EFA-L4 curator: corrected the T9C fixture description. `EdgeStates`
  no longer has a `cgcRefused: "amber" | "red"` flag, and the `cgc-seed` lane no longer emits
  `state: "refused"` with a `refusedPolarity` — both were shapes the server cannot send. Verified
  against `observer/projection.py` L762-L781 (`EngineProcessEdge` is `extra="forbid"`, declares no
  `refusedPolarity`, and its state comment lists nominal|running|blocked|failed|stale|skipped|complete|
  planned|unknown) and `git log --all -S 'state="refused"'` (zero commits ever). The scenario now seeds
  `edges({ cgc: "stale", … })` — a state `_seed_edge_state` really returns — and the renderer derives
  the amber polarity from it; its `currentPhase`/`summary` read "seed stale — reroute". The scenario
  name `engine-cgc-seed-refused` is deliberately unchanged, so the body now says why: "refused" names
  the visual beat, not the edge state. Added the fixture-honesty invariant (an `extra="forbid"` model
  means an invented field or state is a payload the server would reject, and a branch no user reaches).
  Repaired four citations: the projection-types row L61-L285 → L143-L154;L521-L608 (the old range
  contained none of the five named types), `ENGINE_ROOM_SCENARIOS` L724 → L722, `engineProcess`
  L216-L270 → L214-L268, and the `edges` row L132-L214 → L132-L212 (L214 is `engineProcess`).

- 2026-07-31T18:05+02:00 — 260731-EFA-L2 curator: re-derived 10 stale self-citations after the file
  grew to 1198 lines. The whole factory block moved down past the `LEDGER_ROWS`/`LEDGER_TOTAL`/
  `OFFICIAL_LEDGER` window and the `landingRef` helper: `SOURCE_BRANCH` L21→L25,
  `wsEngine` L23-L32→L27-L36, `WORKSPACE` L34→L38, `ref` L36-L38→L109-L111,
  `boot` L40-L47→L113-L120, `EdgeStates` L49-L55→L132-L140, `edges` L57-L105→L142-L214,
  `engineProcess` L107-L156→L216-L270, `EngineRoomScenario` L15-L19→L19-L23, and
  `ENGINE_ROOM_SCENARIOS` L288-L623→L724-L1198 (the export tail now ends at the six spread stage
  arrays). The same three ranges were re-stamped in the Repo-Internal References table. No claim
  text changed; every range was read back against the current source.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: the `engineProcess` fixture helper seeds `leafId` so bench/gallery projections exercise the same leaf-label contract as live series-contract projections. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: engine-room fixtures now point `enclosure` and `sourceFiles` at `<task>/enclosures/<leaf-id>/series-contract.md` instead of a task-root `contract.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-22T11:00 — slice 05o: added the fixtures for the six remaining failure modes (all reusing the
  `engineProcess`/`edges` builders). `EdgeStates` gains a `cgcRefused` flag so the `cgc-seed` edge can emit
  `state: "refused"` (+ `refusedPolarity`). New: `engine-boot-abandoned` (T18, in `bootStages` — the
  `boot-demo` enclosure dissolves with no landing); `providerBlockStages` (T7B provider-plan verify + block);
  `seedFaultStages` (T9B GrepAI seed-fault + seed-retry); `engine-cgc-seed-refused` (T9C — the amber SOFT
  reroute, `health` stays `running`); `liveSyncStages` (T12B — `engine-sync-moved` + `-memory-blocked` +
  `-recovered`, memory lane only); and `engine-integration-conflict-flash` (T14C — `integration: "failed"`
  flashes BOTH return lanes red before the steady STOP). The three stage arrays spread into
  `ENGINE_ROOM_SCENARIOS` (after `...staleBaseStages`); the two `device-mgmt`/`boot-audio` cards sit inline.
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T10:45 — slice 05o T1B: added the `staleBaseStages` array (spread after `...memoryBlockStages`)
  with two `boot-demo`-identity frames — `engine-boot-stale-verify` (`phase: code-worktree`,
  `worktreeAdd: "running"` with the code worktree still `planned`: the code-lane preflight scan-ring beat,
  base staleness not yet decided) and `engine-boot-stale-blocked` (`health: "blocked"`,
  `codeSource.behindSource: 3`, both worktrees `planned`, all edges `planned`, actions
  `fast-forward`/`proceed-stale`, `nextAction: "fast-forward"`, a contract-not-yet-written `missingFact`:
  a FLEETING born-blocked enclosure with the main code node pruned). Same `boot-demo` enclosure as the boot
  stages so the stale-base scenario's recover reuses the boot/clone frames. Verification metadata pinned
  until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B: added the `memoryBlockStages` array (spread after `...bootStages`)
  with two `boot-demo`-identity frames — `engine-boot-memory-verify` (`ledger: "running"` + memory worktree
  `planned`: code lane solid, the ledger-verify scan-ring beat) and `engine-boot-memory-blocked`
  (`ledger: "blocked"`, memory worktree `missing`, `health: "blocked"`, `nextAction: "reconciliation"`,
  `ledgerRows: []`: the gate + ghosted-lane beat). Same `boot-demo` enclosure as the boot stages so the
  `memory-block` scenario's recover reuses `engine-boot-2/3/4/5` and animates as one enclosure; the existing
  `engine-memory-blocked` (`v12-feature`) stays the static GALLERY card. Verification metadata pinned until
  closeout stamps the 05o code commit.
- 2026-06-21T23:35 — added the memory-lane `integration-mem` edge to `edges()`: when integration runs it now
  also pushes an `integration-mem` edge (`memory-worktree → memory-source`, mirroring the code `integration`
  edge) so the memory worktree's ff-only integration back into the feat SOURCE is visible before carryover.
  Emitted only with `external` memory and **skipped when `states.integration === "blocked"`**, so the
  all-or-nothing integration conflict keeps a single code-lane STOP (no duplicate memory-lane gate).
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T02:27+02:00 — slice 05k: added the `engine-landing-pushed` scenario (D3 "code lands" —
  `integration-pending`, `ff-only`, `landing[]` = origin-feat `pushed` / PR `merged` / origin-main `tip` /
  origin-mem-main `planned`), splitting the previously-collapsed D2·D3 tear-down beat (D2 = `engine-landing-ffonly`
  integrate/push/PR-open, D4 = `engine-landing-merged` memory carryover). Appended before `...bootStages`.
  Verification metadata pinned until closeout stamps the 05k code commit.
- 2026-06-19T23:58+02:00 — slice 5i: renumbered the boot stages B0→B5 (added `engine-boot-0-main-only`,
  renamed the rest to the build-up beats — providers-dim / seeding / nominal); added `engine-retired` (D6
  stack-removed); re-typed `engine-landing-merged` to `integration-pending` (D4 intact) and turned
  `engine-cleanup-pending` into the D5 de-materialise (detaching worktree refs + `providers: []`); boot edges
  carry the `worktree-add` lane state. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27 — Dev-bench tab trim (mirrors task 5's `b3f2491`): removed the unused `engine-empty` scenario (empty `processes`) — no consumer (the dev gallery dropped it; the `EnclosureProcessMap` render tests reference only named live scenarios). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: `LEDGER_ROWS` rows now carry `codeSubject`/`codeDate`/`memorySubject`/`memoryDate` (real on the 4 real commits, stepped synthetic on the 21 generated) so the bench popover's 6 columns read complete. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: added `LEDGER_ROWS` (25-row served window) + `LEDGER_TOTAL` + the exported `OFFICIAL_LEDGER`; the default `engineProcess` factory now carries `ledgerRows`/`ledgerRowCount` (live worktree coupler everywhere), and the no-worktree blocked fixtures override `ledgerRows: []`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): dropped the unused `engine-empty` scenario; refreshed the now-stale line-number citations (the landing additions shifted the file). The `engine-boot-*` frames stay here for the component tests; only the bench gallery filters them (`dev/fixtures.ts`). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — slice 5h H2: added the `engine-landing-closeout` scenario (`phase: closeout-pending`) so the T13 closeout train has a fixture. Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: added the `landingRef` helper + the `engine-landing-ffonly` / `engine-landing-merged` scenarios (the successful-landing arc surface for H2) and a default `landing: []` on `engineProcess`. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-17T16:15 — slice 5g G5: added the `engine-integration-conflict` (t14c, `integration-blocked` + a
  blocked `integration` edge) and `engine-abandoned` (t18, `abandoned`) scenarios + an optional `integration`
  edge in `EdgeStates`/`edges()`. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T15:00 — slice 5g G4: made the boot/cloning fixtures' provider `runtimeState` consistent with the
  running conduit — CGC-seeding gets `[boot("code", "indexing")]`; the GrepAI-cloning frames
  (`engine-boot-4`, `engine-fleet` device-mgmt, `engine-setup-running`) get `[boot("code"), boot("memory",
  "indexing")]` so the charging engine matches the flowing conduit. Verification metadata pinned until
  closeout stamps the G4 code commit.
- 2026-06-15T19:35 — Created for slice 5e: scenario fixtures (05e §11): bootstrap/running/failed/fallback/blocked/sync/cleanup + boot build-up stages. Verification metadata pinned until closeout stamps the 5e code commit.
