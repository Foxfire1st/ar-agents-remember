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

The model assertions cover `SCENARIOS` without mounting a component. `build-up` has four frames,
opening on a `worktree_start` caption and ending on the `idle constellation`; its two provider beats
are gone. `tear-down` has at least six frames, begins idle, ends removed/stack, and includes a
`cleanup-pending` process phase. Every scenario has at least one frame, and each frame has
`version === 2`, an engine-process array and a string caption. The folded-in
`engine-cleanup-pending` gallery state remains a single-frame scenario.

The `memory-block` arc retains verify/block/reconcile captions, a blocked-health beat, a ledger-map
edge, and one `worktreeGroup` across its frames. The `stale-base` arc retains
preflight/block/fast-forward captions, a blocked pre-contract process whose base is behind upstream,
a worktree-add edge, and one worktree group. Both cases explicitly reject `cgc-seed` and
`grepai-clone` edge kinds; recovery no longer reruns provider copy-arrow beats.

The `live-sync` case pins a blocked ledger-map edge without a blocked worktree-add edge, an existing
memory worktree behind its source, no seed/clone kinds, and a final unblocked process back in sync.
`integration-conflict` retains the failed integration return-lane flash, terminal
`integration-blocked` last frame, absence of seed/clone kinds, and shared flash-to-STOP worktree
identity. `abandon` retains exactly four frames, nominal then three abandoned phases, no landing refs
on its abandoned frames, a 1300 ms dissolve hold, and one `boot-demo` identity.

The former `seed-fault`, `reindex-reroute` and `provider-block` test cases are removed. A replacement
case checks all three names are absent from `SCENARIOS` and every encountered edge kind belongs to
`worktree-add`, `ledger-map`, `sync`, `integration` or `integration-mem`. It requires a nonempty set of
encountered kinds so an empty traversal cannot pass. These are authored assertions, not a test run.

**The vocabulary guard (260731-EFA-L4).** A final `it` — *never authors an engine edge state the
reducer cannot emit* — flattens every `scenario.frames[].projection.analytics.engineProcesses[].edges[]`
into a `Set` of states, asserts the set is non-empty (so the test cannot pass vacuously on a broken
traversal), and asserts every member is in the module-local `SERVED_EDGE_STATES` set:
`nominal | running | blocked | failed | stale | skipped | complete | planned | unknown` — the vocabulary
`observer/projection.py::EngineProcessEdge.state` documents on an `extra="forbid"` model. The failure
message names the offending state.

### Conventions

Arc assertions read the **projection**, not the captions, wherever the projection carries the fact —
health, edge state/kind and `worktreeGroup` identity. Captions are matched only where the
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

- The replacement provider-retirement case asserts the three provider arc names are absent and all encountered edge kinds belong to the five retained enclosure lanes, with a nonempty traversal. [1]

- `SERVED_EDGE_STATES` and the guard that no authored edge state falls outside it. [2]
- Asserts the `build-up`/`tear-down` timelines + frame validity. [3]

- SCENARIOS registers build-up, tear-down, memory-block, stale-base, live-sync, integration-conflict and abandon before the resting frames; the three provider arcs are removed. [4]

- `EngineProcessEdge.state` — the served vocabulary `SERVED_EDGE_STATES` mirrors, on an `extra="forbid"` model. [5]

- The surviving state guard lists nine accepted edge states, including stale, and rejects any encountered state outside that set after requiring a nonempty traversal. It does not claim a removed seed-edge reducer still emits them. [6]

- `refusedPolarityOf` derives the amber flash from the edge STATE in the renderer, which is why the edge needs no polarity field and the deleted assertion was fixture-only. [7]

### Cross-Repo References

No meaningful cross-repo references found. The served vocabulary this file mirrors lives in the same
repository, under `mcp/src/agents_remember/observer/`.

No meaningful cross-repo references found.
