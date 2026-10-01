# dashboard/src/dev/scenarios.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source, the model under test, and the
server-side model the vocabulary mirrors.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The T9C `reindex-reroute` case: `/reroute/i` caption, `stale` `cgc-seed` edge, `seedFallback`, never `blocked`, same-`worktreeGroup` prop diff. [1]
- `SERVED_EDGE_STATES` and the guard that no authored edge state falls outside it. [2]
- Asserts the `build-up`/`tear-down` timelines + frame validity. [3]
- The `SCENARIOS` model under test, including the `reindexReroute` timeline whose R4 caption this case matches. [4]
- `EngineProcessEdge.state` — the served vocabulary `SERVED_EDGE_STATES` mirrors, on an `extra="forbid"` model. [5]
- `_seed_edge_state` — the reducer function that actually emits `stale`; `refused` is not among its answers. [6]
- `refusedPolarityOf` derives the amber flash from the edge STATE in the renderer, which is why the edge needs no polarity field and the deleted assertion was fixture-only. [7]

### Cross-Repo References

No meaningful cross-repo references found. The served vocabulary this file mirrors lives in the same
repository, under `mcp/src/agents_remember/observer/`.

No meaningful cross-repo references found.
