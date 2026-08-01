# dashboard/src/dev/scenarios.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/scenarios.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:40+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Slice 5i — Vitest coverage of the scenario MODEL (`scenarios.ts`). It asserts the authored timelines
exist with the right shape, that every frame carries a valid projection, and that the old gallery states
folded in as single-frame resting scenarios — guarding the dev-bench substrate without rendering.

Since 260731-EFA-L4 it also **pins the engine-edge state vocabulary**. These fixtures are the only
thing that ever "produces" an engine-process edge on this side of the wire, so an author can invent a
state the reducer cannot emit — and then a renderer branch gets written to match it and ships
permanently dead. That is exactly how `refused` and its `refusedPolarity` companion field got in.

## Code Commentary

### Logic

Five `it` cases over `SCENARIOS`: (1) `build-up` has 6 frames opening on a `worktree_start` caption and
ending on the `idle constellation`; (2) `tear-down` has ≥6 frames (idle → `removed`/`stack`) and its
frames' `engineProcesses` phases include `cleanup-pending` (the de-materialise beat — proven via a
`flatMap` over each frame's `analytics.engineProcesses[].phase`); (3) every scenario has ≥1 frame and
each frame is a full `WorkspaceProjection` (`version === 2`, `analytics.engineProcesses` is an array, a
string caption); (4) a folded-in gallery state (`engine-cleanup-pending`) is a single-frame scenario; (5)
**(05o)** the `memory-block` T3B arc has verify/block/reconcile captions, a frame whose `engineProcesses`
`health` includes `blocked`, a frame driving a **running `cgc-seed`/`grepai-clone` edge** (so the recover's
copy-arrow clone beat can't be silently dropped again), and a single `worktreeGroup` across all frames (the
one-enclosure recover); (6) **(05o T1B)** the `stale-base` arc has preflight/block/fast-forward captions, a
`blocked`-health frame whose `codeSource.behindSource` is `> 0` and whose `missingFacts` include a
`contract not yet written` entry (the fleeting born-blocked beat), a frame driving a **running
`cgc-seed`/`grepai-clone` edge** (the recover's copy-arrow clone beat, so it can't regress to a teleport), and
a single `worktreeGroup` across all frames (one enclosure). **(05o)** Six further `it` cases pin one arc
per remaining failure mode, each asserting the choreography off the projection rather than off captions:
(7) **`seed-fault` (T9B)** — the fault frame drives a `failed`-health node with a `failed` `grepai-clone`
edge, the `memory`-role provider `runtimeState === "down"` while the `code` provider is NOT down, and a
re-running `grepai-clone` AFTER the fault (re-seed, not a teleport); (8) **`reindex-reroute` (T9C)** — a
**`stale`** `cgc-seed` edge plus `seedFallback === true`, never a `blocked`
health (soft reroute), with the reroute→reindex-settle pair asserted as a same-`worktreeGroup` prop diff.
Two things changed here in 260731-EFA-L4: the caption match moved from `/refused/i` to `/reroute/i`, and
the `refusedPolarity === "amber"` assertion was **deleted** — the edge carries no polarity field of its
own, and the amber flash polarity is derived from the edge state by the renderer
(`EnclosureCanvas.tsx::refusedPolarityOf`);
(9) **`provider-block` (T7B)** — a `blocked`-health node with `setupState === "blocked"`, zero `providers`
(engines never light), `missingFacts` carrying both a `contract not yet written` and a provider-plan/setup
entry, and the recover running the seed/clone copy-arrows; (10) **`live-sync` (T12B)** — a `blocked` node
with a `blocked` `ledger-map` edge (but NOT a `worktree-add` block), `memorySource.behindSource > 0`, an
existing `memoryWorktree`, NO clone/seed beat (the recover is a ff/ref diff since the engines never go
down), and a final frame that is unblocked with `memorySource.behindSource === 0`; (11)
**`integration-conflict` (T14C)** — a transient flash frame with a `failed` `integration`/`integration-mem`
return-lane, a TERMINAL last frame in phase `integration-blocked` with no clone tail (no recover), and the
flash→STOP pair sharing one `worktreeGroup`; (12) **`abandon` (T18)** — exactly 4 frames whose phases go
nominal then `abandoned`×3, no `landing` refs on any abandon frame (never lands), `durMs === 1300` on the
held dissolve beat, and a single `boot-demo` node `id` across all frames (one continuous identity). Across
the recoverable modes the recover re-runs the clone beats, and each failure beat shares one enclosure
identity with its resolving neighbour.

**(13) The vocabulary guard (260731-EFA-L4).** A final `it` — *never authors an engine edge state the
reducer cannot emit* — flattens every `scenario.frames[].projection.analytics.engineProcesses[].edges[]`
into a `Set` of states, asserts the set is non-empty (so the test cannot pass vacuously on a broken
traversal), and asserts every member is in the module-local `SERVED_EDGE_STATES` set:
`nominal | running | blocked | failed | stale | skipped | complete | planned | unknown` — the vocabulary
`observer/projection.py::EngineProcessEdge.state` documents on an `extra="forbid"` model. The failure
message names the offending state.

### Conventions

Arc assertions read the **projection**, not the captions, wherever the projection carries the fact —
health, edge state, `seedFallback`, `worktreeGroup` identity. Captions are matched only where the
caption itself is the artefact under test. `SERVED_EDGE_STATES` is a deliberate hand-kept mirror of a
Python-side comment: there is no generated vocabulary to import here, so the set is written out and
cited rather than inferred.

### Invariants And Boundaries

Pure model test — no DOM, no store, no timers (the transport is exercised separately/by hand). It is
coupled to the authored captions + the tear-down's `cleanup-pending` phase, so it is the guard that keeps
those load-bearing strings/phases from silently drifting. Asserts real shape, not theater: a missing
timeline or an empty frame fails.

- No assertion may pin a fixture-only field. `refusedPolarity` was asserted here against a field the
  fixture set itself, on a server model that is `extra="forbid"` — the shape this suite now guards
  against for every edge state.
- `SERVED_EDGE_STATES` must stay in step with `EngineProcessEdge.state`. It is the one place this file
  restates a server vocabulary, and drift makes the guard silently narrower or wrongly noisy.
- The vocabulary guard must keep asserting `seen.size > 0`; without it a traversal that stops finding
  edges passes.

### Todos

No open file-local todos.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source, the model under test, and the
server-side model the vocabulary mirrors.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The T9C `reindex-reroute` case: `/reroute/i` caption, `stale` `cgc-seed` edge, `seedFallback`, never `blocked`, same-`worktreeGroup` prop diff. | L131-L161 | [scenarios.test.ts](scenarios.test.ts) |
| `SERVED_EDGE_STATES` and the guard that no authored edge state falls outside it. | L279-L313 | [scenarios.test.ts](scenarios.test.ts) |
| Asserts the `build-up`/`tear-down` timelines + frame validity. | L10-L37 | [scenarios.test.ts](scenarios.test.ts) |
| The `SCENARIOS` model under test, including the `reindexReroute` timeline whose R4 caption this case matches. | L90-L102; L258-L271 | [scenarios.ts](scenarios.ts) |
| `EngineProcessEdge.state` — the served vocabulary `SERVED_EDGE_STATES` mirrors, on an `extra="forbid"` model. | L762-L781 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| `_seed_edge_state` — the reducer function that actually emits `stale`; `refused` is not among its answers. | L1588-L1611 | [reducer.py](../../../mcp/src/agents_remember/observer/reducer.py) |
| `refusedPolarityOf` derives the amber flash from the edge STATE in the renderer, which is why the edge needs no polarity field and the deleted assertion was fixture-only. | L231-L241 | [engine-room/EnclosureCanvas.tsx](../panels/engine-room/EnclosureCanvas.tsx) |

## Cross-Repo References

No meaningful cross-repo references found. The served vocabulary this file mirrors lives in the same
repository, under `mcp/src/agents_remember/observer/`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the `projection.py`
  citation after a worker inserted ten lines above it. `EngineProcessEdge` L752-L771 → L762-L781:
  the class opens at L762, `model_config = ConfigDict(extra="forbid")` is L770, and the nine-state
  vocabulary comment plus `state: str` are L778-L779. No body text changed.
- 2026-08-01T10:04+02:00 — 260731-EFA-L4 curator: corrected the T9C description and documented the new
  vocabulary guard. The `reindex-reroute` case now matches `/reroute/i` instead of `/refused/i`,
  looks for a **`stale`** `cgc-seed` edge instead of a `refused` one, and **no longer asserts
  `refusedPolarity === "amber"`** — that field existed on no server model, was set by the fixture the
  assertion then read, and the amber flash is derived from the edge state by
  `EnclosureCanvas.tsx::refusedPolarityOf`. Added case (13), the `SERVED_EDGE_STATES` guard that pins
  every authored edge state to the nine `EngineProcessEdge.state` documents, plus `Conventions`,
  `Todos`, `Docs References` and `Cross-Repo References`, which the card lacked. Replaced the `—`
  citation with ranges proving `SERVED_EDGE_STATES`, the T9C case, `_seed_edge_state`,
  `EngineProcessEdge.state` and `refusedPolarityOf`. Verification metadata left pinned; closeout
  stamps the code commit.
- 2026-06-22T11:00 — slice 05o: added six arc `it` cases, one per remaining failure mode — `seed-fault`
  (T9B: failed `grepai-clone` + memory engine down, CGC unaffected, re-seed after the fault),
  `reindex-reroute` (T9C: refused amber `cgc-seed` + `seedFallback`, soft/never blocked),
  `provider-block` (T7B: `blocked` `setupState`, zero providers, provider-plan + pre-contract
  `missingFacts`), `live-sync` (T12B: `blocked` `ledger-map`, behind-source memory, ff/ref recover with
  no clone beat), `integration-conflict` (T14C: failed integration return-lane, terminal
  `integration-blocked` STOP, no recover tail), and `abandon` (T18: 4 frames, abandoned×3, no landing,
  one `boot-demo` identity). Each asserts the choreography off the projection (health/edge-state/polarity),
  recoverable modes re-run the clone beats, and the failure beat shares one enclosure identity with its
  resolving neighbour. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T10:45 — slice 05o T1B: added a sixth `it` pinning the `stale-base` arc — preflight/block/fast-forward
  captions, a `blocked`-health frame whose `codeSource.behindSource > 0` and whose `missingFacts` carry a
  `contract not yet written` entry (the fleeting born-blocked beat), a **running `cgc-seed`/`grepai-clone`**
  beat (the recover's copy-arrow clone, so it can't regress to a teleport), and a single `worktreeGroup` across
  the frames (one enclosure). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B: added a fifth `it` pinning the `memory-block` arc — verify/block/
  reconcile captions, a `blocked`-health frame, a **running `cgc-seed`/`grepai-clone`** beat (locks in the
  recover's copy-arrow clone beats so they can't regress to a teleport), and a single `worktreeGroup` across the
  frames. Broadened the verify caption match to `/verif/i`. Verification metadata pinned until closeout stamps
  the 05o code commit.
- 2026-06-19T23:58+02:00 — Created for slice 5i: tests for the scenario model — build-up (6 frames) /
  tear-down (≥6, with a `cleanup-pending` de-materialise frame) timelines, every frame a valid v2
  projection + caption, and the gallery states folded in as single-frame resting scenarios. Verification
  metadata pinned until closeout stamps the code commit.
