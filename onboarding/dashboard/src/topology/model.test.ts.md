# dashboard/src/topology/model.test.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/model.test.ts`      |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-01T10:30+02:00                      |
| lastVerifiedCommitHash |                                             `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |                                             2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                            |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`model.test.ts` is focused Vitest coverage for the pure Topology model. It verifies provider
parenting (worktree-scoped → its enclosure, repo-scoped workspace → repo node, unmatched → workspace
core, `worktreeGroup` precedence) and, as of task 33, the active-enclosure reshape: an
`activeTopologyInputs` describe (active-only inclusion, terminal/orphan exclusion), a fold test (the
enclosure `wt` node carries its 1:1 lifecycle's id/status/sub and **no** `task`-kind node is emitted),
and a path-vs-basename provider-join test (enclosure full-path `worktreeGroup` joins a basename
provider `worktreeGroup`). A `lifecycle()` factory supplies `LifecycleProjection` fixtures.

Since 260731-EFA-L4 it also owns the **state → status grammar** coverage: a `lifecycleStatus`
describe and two `buildTopology` cases that drive the whole `LIFECYCLE_STATES` vocabulary rather than
hand-picking states. This is the file that could not see the leaf's headline defect, and the reason
is recorded in the source: it enumerated the one state it already knew about, so a classification
covering five of six states and answering `"ok"` for the sixth passed.

## Code Commentary

### Logic

The test builds minimal `EnclosureNode` and `ProviderNode` fixtures and calls `buildTopology` directly.
It then inspects the returned `ConstelNode[]` instead of rendering a canvas. The assertions cover the
intended worktree join path, the missing-worktree fallback path, the aggregate workspace-provider path,
repo-scoped workspace provider parenting, and `worktreeGroup` precedence over `repoId`.

**The `lifecycleStatus` describe (four cases).**

1. *classifies every state the vocabulary declares* — iterates `LIFECYCLE_STATES` and asserts each is
   a key of `CONSTEL_STATUS_BY_STATE`. `Record<State, ConstelStatus>` already fails `tsc -b` on a
   seventh state; this makes the same gap fail under vitest, so it is visible from either gate
   instead of only from the one someone remembered to run.
2. *classifies a state it has never heard of as the declared unclassified status* — the
   forward-compatibility case. It is pinned **to the value**, not to its negation: the comment records
   that `.not.toBe("ok")` was the whole assertion and that `undefined` satisfies it, so deleting
   `?? UNCLASSIFIED_STATUS` would leave both gates green while the `undefined` reached the renderer's
   palette. The case now asserts `CONSTEL_STATUSES` contains the answer (it is a status, not a hole),
   that it equals `UNCLASSIFIED_STATUS`, and that the declared value is `"warn"`.
3. *still classifies an unknown state when the reducer INFERRED it* — the degrade reads
   `declared === "ok"`, which is false for `undefined` as well as for `warn`, so that branch cannot
   tell "unclassified" from "classified" on its own. Pinned separately.
4. *degrades an inferred healthy state and leaves every other reading alone* — `running`+inferred →
   `warn`, `running` → `ok`, `blocked`+inferred → `crit`, `abandoned`+inferred → `idle`.

`fromANewerServer(state: string): State` is the named, single-site widening the two unknown-state
cases use. `State` is a closed union mirroring a bare `str` server-side, so the mirror is narrower
than the wire by construction; the helper exists so those two cases read as a forward-compatibility
check rather than as loose casts a reader could mistake for a banned pattern.

**Two `buildTopology` grammar cases.** *draws every state in the vocabulary with the status that state
declares* iterates `LIFECYCLE_STATES`, builds a topology per state, and asserts the `wt` node's status
equals `CONSTEL_STATUS_BY_STATE[state]` — which also pins that there is exactly one classification
path, since a second if-chain grown inside `buildTopology` would disagree with the declared grammar.
*does not render an awaiting-developer lifecycle as a healthy node* pins the reported defect by name:
`status` is not `"ok"`, is `"warn"`, and `sub` reads `build · awaiting-developer`.

### Conventions

Tests stay at the pure-model boundary because `ConstelNode.parent` is the behavior contract that the
renderer consumes. Fixture helpers accept partial overrides so each test only names the field under
test. **Iterate, never enumerate**: any assertion over the state vocabulary reads `LIFECYCLE_STATES`
rather than listing states, so a new state fails here instead of passing unnoticed. Assertions about
the unclassified answer are pinned to `UNCLASSIFIED_STATUS` by value — an assertion that only rules a
value out cannot notice the absence of a value at all.

### Invariants And Boundaries

- Tests must not depend on canvas rendering, layout timing, or browser animation state.
- No vocabulary may be hand-copied here. `LIFECYCLE_STATES` and `CONSTEL_STATUSES` are imported and
  iterated; a second local list is the failure mode this file was rewritten to remove.
- The unclassified case must assert the concrete value, not `.not.toBe("ok")`. The negation passes on
  `undefined`, which is precisely the value the fix exists to prevent.
- `fromANewerServer` is the only sanctioned widening in this file and must stay a bare token cast,
  never a shape.
- The worktree-provider test must prove `ProviderNode.worktreeGroup` joins to `EnclosureNode.worktreeGroup`.
- The fallback, workspace, repo-scoped, and precedence cases must remain explicit so backend/provider
  projection changes cannot accidentally change topology parenting semantics.

### Todos

No open file-local todos.

## Docs References

No relevant external documentation was found after checking the repository source registry; this is a
project-local unit test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This test documents the behavioral contract of the pure topology builder and, since 260731-EFA-L4,
the state → status grammar it reads from.

| Finding | Anchor | Source |
| --- | --- | --- |
| The `lifecycleStatus` describe: totality over `LIFECYCLE_STATES`, the unclassified answer pinned to `UNCLASSIFIED_STATUS` by value, the same answer under `inferred`, and the healthy-only degrade. | `lifecycleStatus`; "classifies every state the vocabulary declares" | dashboard/src/topology/model.test.ts:93-138 |
| `fromANewerServer` — the single named widening the two unknown-state cases share. | `fromANewerServer` | dashboard/src/topology/model.test.ts:52-54 |
| The two vocabulary-driven `buildTopology` cases: every state drawn with its declared status, and `awaiting-developer` explicitly not `"ok"`. | "draws every state in the vocabulary with the status that state declares"; "does not render an awaiting-developer lifecycle as a healthy node" | dashboard/src/topology/model.test.ts:155-168; dashboard/src/topology/model.test.ts:170-188 |
| The grammar under test — `CONSTEL_STATUSES`, `CONSTEL_STATUS_BY_STATE`, `UNCLASSIFIED_STATUS`, `STATUS_BY_DECLARED_STATE`, `lifecycleStatus`. | `CONSTEL_STATUSES`; `CONSTEL_STATUS_BY_STATE`; `UNCLASSIFIED_STATUS`; `STATUS_BY_DECLARED_STATE`; `lifecycleStatus` | dashboard/src/topology/model.ts:16-16; dashboard/src/topology/model.ts:48-59; dashboard/src/topology/model.ts:68-68; dashboard/src/topology/model.ts:83-83; dashboard/src/topology/model.ts:85-93 |
| The topology builder folds each enclosure's lifecycle through `lifecycleStatus` and parents providers by worktree group, repo id, or workspace core. | `lifecycleStatus` | dashboard/src/topology/model.ts:85-93 |
| `LIFECYCLE_STATES` — the imported vocabulary the assertions iterate instead of restating; composed from `LIVE_STATES` (L42) + `TERMINAL_STATES` (L48), so the range holds all six names. | `LIFECYCLE_STATES`; `LIVE_STATES`; `TERMINAL_STATES` | dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13 |
| The provider-parenting fixtures and assertions: matching worktree groups, missing groups, aggregate workspace providers, repo-scoped workspace providers, and `worktreeGroup` precedence. | "joins a worktree provider to its enclosure when worktreeGroup formats differ (path vs basename)"; "parents worktree-scoped providers to their owning worktree node"; "falls back to the workspace core when a worktree provider has no matching group"; "keeps workspace-scoped providers parented to the workspace core"; "parents repo-scoped workspace providers to their covered repo node"; "keeps worktreeGroup precedence over repoId for provider parenting" | dashboard/src/topology/model.test.ts:190-200; dashboard/src/topology/model.test.ts:202-211; dashboard/src/topology/model.test.ts:213-219; dashboard/src/topology/model.test.ts:221-231; dashboard/src/topology/model.test.ts:233-251; dashboard/src/topology/model.test.ts:253-269 |

## Cross-Repo References

No meaningful cross-repo references found. The test covers same-repository frontend model logic only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

Topology tests construct `EnclosureNode` fixtures with the new `enclosureId`, `leafId`, and `taskRoot` fields so provider-parenting expectations run against the current projection shape. Since 260703-L11 the fixture also carries the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` (defaulted `true`); the Topology itself keeps filtering on `activeWorktreeGroups`, not on these flags.

## Update History

- 2026-08-03T10:00+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 10 assigned citation findings (5 missing anchors and 5 malformed sources); final scoped check is clean.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the one row citing that file: `LIFECYCLE_STATES` L21-L30 → L42-L59,
  which now spans both declared halves and the composed tuple at L59. The iterate-never-enumerate claim
  is unchanged — the tuple is still what the assertions import and walk.
- 2026-08-01T09:28+02:00 — 260731-EFA-L4 curator: documented the grammar coverage this file gained.
  A `lifecycleStatus` describe (four cases: totality over `LIFECYCLE_STATES`; the unclassified answer
  pinned to `UNCLASSIFIED_STATUS` **by value** rather than by `.not.toBe("ok")`, which `undefined`
  satisfies; the same answer under `inferred`; and the healthy-only degrade), the named
  `fromANewerServer` widening helper, and two `buildTopology` cases that iterate the whole vocabulary
  — one asserting every state draws with `CONSTEL_STATUS_BY_STATE[state]`, one pinning
  `awaiting-developer` as not `"ok"`. Added the iterate-never-enumerate convention and the matching
  invariants. Replaced the two Repo-Internal rows, whose ranges (`L49-L58; L80-L124` on `model.ts`,
  `L6-L100` on this file) no longer contained the symbols they named, with seven ranges each holding
  its proving symbol. Verification metadata left pinned; closeout stamps the code commit.
- 2026-07-06T03:20+02:00 — 260703-L11: the `enclosure(...)` fixture defaults the new required
  `codeWorktreeExists`/`memoryWorktreeExists` flags to `true`, matching the projection contract; no
  assertion change — topology admission still keys on `activeWorktreeGroups`. Verification metadata
  pinned until closeout stamps the L11 commit.
- 2026-06-28T07:30+02:00 — Task 33: added an `activeTopologyInputs` describe (active-only inclusion,
  terminal/orphan exclusion), a lifecycle-fold test (enclosure node carries id/status/sub, no task-kind
  node), and a path-vs-basename provider-join test; added a `lifecycle()` fixture factory. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: topology fixtures now include `enclosureId`, `leafId`, `taskRoot`, and the leaf `series-contract.md` enclosure path required by the projection schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2: extended pure-model coverage for repo-scoped workspace provider
  parenting and `worktreeGroup` precedence over `repoId`, while preserving S1 fallback/core behavior.
  Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T15:08+02:00 — Created for task 12 S1: covers worktree-provider parenting, unmatched
  worktree fallback, and workspace-provider core parenting for `buildTopology`. Verification metadata
  will be stamped at closeout.
