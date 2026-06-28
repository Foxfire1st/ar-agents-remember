# dashboard/src/dev/scenarios.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/scenarios.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T23:58+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Slice 5i — Vitest coverage of the scenario MODEL (`scenarios.ts`). It asserts the authored timelines
exist with the right shape, that every frame carries a valid projection, and that the old gallery states
folded in as single-frame resting scenarios — guarding the dev-bench substrate without rendering.

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
`refused` `cgc-seed` edge with `refusedPolarity === "amber"` + `seedFallback === true`, never a `blocked`
health (soft reroute), with the refuse→reindex-settle pair asserted as a same-`worktreeGroup` prop diff;
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

### Invariants And Boundaries

Pure model test — no DOM, no store, no timers (the transport is exercised separately/by hand). It is
coupled to the authored captions + the tear-down's `cleanup-pending` phase, so it is the guard that keeps
those load-bearing strings/phases from silently drifting. Asserts real shape, not theater: a missing
timeline or an empty frame fails.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Asserts the `build-up`/`tear-down` timelines + frame validity. | L10-L37 | [scenarios.test.ts](scenarios.test.ts) |
| The `SCENARIOS` model under test. | — | [scenarios.ts](scenarios.ts) |

## Update History

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
