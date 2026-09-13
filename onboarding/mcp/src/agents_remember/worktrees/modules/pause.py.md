# mcp/src/agents_remember/worktrees/modules/pause.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/pause.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T19:02+02:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[modules route overview](overview.md)

## Purpose

`pause.py` is the **entire stop-only pause route** for an atomic master, added by
`260831-LOCR-L37`. It owns one public-shape operation: release the master's atomic-series
activation selection, publish nothing, and hand the turn back to the developer.

Its boundary **is** the feature. A caller who wants to stop a master must not be able to move a
ref, create a commit, land anything or write a ledger row by reaching for the stop, so this
module imports and calls none of the integration, landing, closeout or ledger planes and runs no
Git at all. The activation snapshot it writes while releasing is the one legitimate write, and
that write is not a publication: it records that this contract is no longer the selected master.

`worktree_checkpoint_landing` is the SEPARATE, explicitly requested **publication** that lands an
unfinished master's accumulated line. It is deliberately unreachable from here, and the split
exists so that the two can never be one verb again.

## Code Commentary

### Logic

`pause_result(args, current_contract)` is the whole entry point. It refuses to run against a
contract that is not the one it was addressed with (`args.contract_path.resolve()` must equal
`current_contract.contract_path.resolve()`), then splits three ways:

- **Not a series contract.** `contract.kind != "series"` refuses with
  `pause-requires-atomic-master`. An ordinary leaf owns no atomic-series selection — its parent
  master's selection is what exposes its work — so a leaf pause must refuse rather than release
  the master's selection on the leaf's behalf or invent a record for it.
- **Release refused.** `release_atomic_series_selection(contract)` raises
  `AtomicSeriesActivationError`; the module returns the release authority's own `status` and
  explains it in the pause's terms through `_RELEASE_REFUSAL_DETAIL`. The three explained
  statuses are `atomic-series-activation-selected-contract-mismatch` (the addressed record names
  another master), `atomic-series-activation-selection-missing` (nothing to stop) and
  `atomic-series-activation-release-unreadable`. The guard itself stays in the release
  authority; this module never suppresses, repairs or re-implements it.
- **Released.** `_paused_payload(contract, released.source_fact())` reports the stop: `state` and
  `status` are both `"paused"`, `paused` is `True`, `atomicSeriesActivation` carries the released
  record's source fact, and `nextStep` is `_PAUSE_NEXT_STEP` — a `summary` and **no**
  `nextTool`/`nextArgs`/`nextOperation`.

`_PAUSE_NEXT_STEP` is the stop's whole next-move contribution and it is deliberately the
smallest possible one: the result proposes no continued execution and no call to make, so
control is the developer's until they ask for the master again. Resuming is the existing public
`worktree_sync`/attach route, not a pause verb.

`_refusal_payload(...)` mirrors that shape on the refusal side: `paused` is `False`, the status is
the refusal status, and no next call is proposed either.

### Conventions

- The module owns its caller-facing vocabulary (`_PAUSED_SUMMARY`, `_PAUSE_NEXT_STEP`,
  `_RELEASE_REFUSAL_DETAIL`) as module constants; `_paused_payload` copies `_PAUSE_NEXT_STEP`
  with `dict(...)` so a caller cannot mutate the module's own step.
- Both payload shapes report `contractPath`/`enclosurePath` (success) or `contract_path`
  (refusal) from the resolved contract, so a stop is always addressed by the contract it stopped.
- The delegation is one call: the pause introduces **no second scheduling, release or publication
  authority**. Sync cancellation, terminal cleanup and the pause all release through the same
  `release_atomic_series_selection`.

### Invariants And Boundaries

- **The pause publishes nothing.** It moves no ref, creates no commit, lands nothing, writes no
  ledger row, and advances no unstarted leaf. The master keeps its code and memory work branches,
  its worktrees, its enclosure and every unstarted leaf byte-identically, and the destination
  (protected source) branch is untouched.
- **The release is what makes the stop real.** The activation selection is the durable fact that
  says this master is the one exposing implementation work, so releasing it is the stop; marking
  the master without releasing it would stop nothing. The paused master's observed state is the
  existing released state (`vacant`) — there is no parallel paused state and no second authority.
- **Per-contract keying is what isolates the stop.** The activation record is addressed by
  `activation_path(...)` derived from this contract's fingerprint, so releasing one master leaves
  every other master's record byte-identical and cannot make a sibling ineligible. The retired
  cross-master waiting vocabulary is gone from the live read and must not be re-introduced here.
- **No publication module is reachable.** `mcp/tests/test_pause_is_not_publication.py` builds this
  module's static source-level import graph and asserts it is disjoint from every ref-moving, landing,
  ledger-writing and closeout module. Publication is excluded structurally, by what the route can call
  at all. Measured on the frozen candidate: the closure holds **60** modules including the root, this
  module's **5** direct imports, **54** modules beyond them, and **0 of 12** publication modules. The
  case also asserts the closure is deep enough for the disjointness claim to mean anything — three
  non-vacuity checks including two named witnesses, one of which
  (`agents_remember.worktrees.scheduling_mode`) is provably not a direct import — so a walker that
  stopped at the direct imports would fail rather than pass.
- The guard's method limits are real and are stated by the test itself: it reads a static AST graph
  (function-local imports counted, `TYPE_CHECKING` branches excluded), it does not follow dynamic
  imports such as `importlib.import_module`, and it measures per-module reachability rather than a
  process-wide `sys.modules` reading — deliberately, because a session-wide reading would see
  publication modules other tests imported. Separately measured, importing this module in the real
  interpreter loads 125 `agents_remember` modules; that is a runtime observation, not what the guard
  asserts. See that test's card for both readings.
- **The pause is not the checkpoint, and the checkpoint is not the pause.**
  `worktree_checkpoint_landing` is an explicitly requested publication with its own approval; the
  pause must never be routed through it, and no pause surface may describe it as the pause.
- The stop is idempotent: replaying an already-vacant exact record releases nothing new and
  reports the same stopped master.

### Todos

None recorded. Verification metadata on this card remains closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stop-only route: contract identity check, the series-only refusal, the release delegation, the paused payload and the refusal payload. | `pause_result`; `_paused_payload`; `_refusal_payload` | mcp/src/agents_remember/worktrees/modules/pause.py:66-109; mcp/src/agents_remember/worktrees/modules/pause.py:112-129; mcp/src/agents_remember/worktrees/modules/pause.py:132-148 |
| The hand-back: a `nextStep` carrying a summary and no `nextTool`/`nextArgs`, so the result proposes no continued execution. | `_PAUSE_NEXT_STEP` | mcp/src/agents_remember/worktrees/modules/pause.py:31-39 |
| The release authority the pause delegates to — strict explicit cancellation release, exact-owner proof, per-contract address, and the three refusal statuses the pause explains. | `release_atomic_series_selection`; `_record_selects_contract` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:23-54; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:79-88 |
| The activation record's contract-derived address is what makes one master's release leave another master's record alone. | `activation_path`; "def contract_fingerprint(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-142 |
| The public tool the pause is reached through, and the payload builder it is reached by. | "def worktree_pause("; "def worktree_pause_payload("; "def worktree_pause_tool(" | mcp/src/agents_remember/mcp/registration/worktrees.py:199-219; mcp/src/agents_remember/mcp/tools/worktree.py:88-95; mcp/src/agents_remember/application/worktree_tools.py:470-499 |
| The facade re-export that keeps the public `git_worktree_manager` import path for the pause. | "from agents_remember.worktrees.modules.pause import pause_result"; "\"pause_result\"," | mcp/src/agents_remember/worktrees/git_worktree_manager.py:86-86; mcp/src/agents_remember/worktrees/git_worktree_manager.py:154-154 |
| The response model that declares `paused` as the route's own claim. | `WorktreePauseResponse` | mcp/src/agents_remember/models/worktree.py:467-476 |
| The executable specification of the boundary: the pause's runtime-import closure is disjoint from every publication module. | `PUBLICATION_MODULES`; `test_the_pause_cannot_reach_any_publication_module` | mcp/tests/test_pause_is_not_publication.py:37-52; mcp/tests/test_pause_is_not_publication.py:165-202 |
| The boundary proof: the public pause over real temporary Git repositories, measuring refs, object databases, coordination tree, worktrees and task documents before and after. | `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_is_refused_and_writes_nothing`; `test_pausing_an_already_released_master_is_idempotent`; `test_pausing_a_leaf_contract_is_refused`; `test_pausing_one_master_leaves_the_other_masters_record_byte_identical`; `test_a_record_this_contract_does_not_own_is_refused_not_released`; `test_resuming_a_paused_master_restores_work_with_nothing_published` | mcp/tests/test_pause_stop_only_end_to_end.py:201-232; mcp/tests/test_pause_stop_only_end_to_end.py:234-261; mcp/tests/test_pause_stop_only_end_to_end.py:263-276; mcp/tests/test_pause_stop_only_end_to_end.py:278-292; mcp/tests/test_pause_stop_only_end_to_end.py:294-319; mcp/tests/test_pause_stop_only_end_to_end.py:321-363; mcp/tests/test_pause_stop_only_end_to_end.py:365-402; mcp/tests/test_pause_stop_only_end_to_end.py:404-428 |
| The separate publication the pause must never be reached as or described as. | `worktree_checkpoint_landing` | mcp/src/agents_remember/mcp/registration/closeout.py:180-209 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned stop route.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260831-LOCR-L37 Pause/Publication Split

The split is the point of the module. Before L37 the repository had a PUBLICATION under the name
an agent reaches for when it wants to stop a master: `worktree_checkpoint_landing` lands the
master's committed code and memory refs onto its super branch, where every other master sees
them, under an explicitly required developer approval. L36 corrected that tool's registered
description to say it is a publication and deny being the pause, but no stop existed. L37 adds
the stop as its own verb and its own route, and proves structurally that the stop cannot become
the publication.

The three surfaces an agent meets are deliberately distinct:

| Surface | What it does | What it moves |
| --- | --- | --- |
| `worktree_pause` | stops the master, releases its activation selection, hands the turn back | nothing |
| `worktree_checkpoint_landing` | the explicitly requested partial PUBLICATION of a partial master | refs, ledger, `checkpointed` integration cell |
| `worktree_sync` / `worktree_attach` | the existing resume route for a paused master | nothing beyond ordinary selection/sync |

## Update History
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: created the card for the new stop-only pause
  module. Recorded the delegation to the existing `release_atomic_series_selection` authority (no
  second scheduling or publication authority), the three-way split in `pause_result` (contract
  identity, series-only refusal, release delegation), the paused payload's `state`/`status`/
  `paused`/`atomicSeriesActivation` and its `nextStep` carrying a summary and no next call, the
  contract-keyed isolation that leaves a sibling master's record byte-identical, and the structural
  exclusion of publication through the module's runtime-import closure. Verification metadata
  remains closeout-owned; no acceptance claim.
