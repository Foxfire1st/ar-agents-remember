# mcp/src/agents_remember/worktrees/modules/pause.py

## Governing Overview

[modules route overview](overview.md)

## Purpose

`pause.py` is the **entire stop-only pause route** for an atomic master, added by
`260831-LOCR-L37`. It owns one public-shape operation: release the master's atomic-series
activation selection — or, when the master holds none, report that it is already stopped —
publish nothing, and hand the turn back to the developer.

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

`pause_result(args, current_contract)` is the whole entry point (code lines 80-128). It refuses to
run against a contract that is not the one it was addressed with (`args.contract_path.resolve()` must
equal `current_contract.contract_path.resolve()`), then splits into four outcomes:

- **Not a series contract.** `contract.kind != "series"` refuses with
  `pause-requires-atomic-master`. An ordinary leaf owns no atomic-series selection — its parent
  master's selection is what exposes its work — so a leaf pause must refuse rather than release
  the master's selection on the leaf's behalf or invent a record for it.
- **Release refused, and the master is genuinely not vacant.** `release_atomic_series_selection(contract)`
  raises `AtomicSeriesActivationError`. `_already_stopped_result` (code lines 131-151) answers the one
  status the pause owns — `_SELECTION_MISSING`, `"atomic-series-activation-selection-missing"` — by
  **re-observing** the record with `observe_atomic_series(contract)`: only an observation of `vacant`
  becomes the already-stopped success below, so a record that appeared or became unreadable between
  the two reads still refuses instead of reporting a stop. Every other status, and every observation
  that is not `vacant`, returns the release authority's own `status` explained in the pause's terms
  through `_RELEASE_REFUSAL_DETAIL`. The explained refusals are
  `atomic-series-activation-selected-contract-mismatch` (the addressed record names another master)
  and `atomic-series-activation-release-unreadable`. The two are reached by **different record
  shapes**, which is worth knowing before writing or reading a case against them: an *active* record
  naming another master never reaches the release's owner guard at all — the observation's
  `_load_selected_contract` refuses it first (`atomic-series-activation-master-mismatch`, reported as
  `unreadable`) — so `selected-contract-mismatch` is reachable only through a record that reads
  `vacant` while naming another master. The guard itself stays in the release authority;
  this module never suppresses, repairs or re-implements it.
- **Already stopped.** `_already_vacant_payload` (code lines 153-171) reports the success: `state`
  and `status` are both `"atomic-series-already-vacant"`, `paused` is `True`,
  `atomicSeriesActivation` carries the observed vacant source fact, and `nextStep` is the same
  `_PAUSE_NEXT_STEP` a released pause returns — a `summary` and **no**
  `nextTool`/`nextArgs`/`nextOperation`. `_ALREADY_VACANT_SUMMARY` states explicitly that no selection
  was held, so a caller can tell this apart from a real release.
- **Released.** `_paused_payload(contract, released.source_fact())` (code lines 173-191) reports the
  stop: `state` and `status` are both `"paused"`, `paused` is `True`, `atomicSeriesActivation` carries
  the released record's source fact, and `nextStep` is `_PAUSE_NEXT_STEP`.

`_PAUSE_NEXT_STEP` (code lines 50-55) is the stop's whole next-move contribution and it is
deliberately the smallest possible one: the result proposes no continued execution and no call to
make, so control is the developer's until they ask for the master again. Both success payloads carry
it unchanged. Resuming is the existing public `worktree_sync`/attach route, not a pause verb.

`_refusal_payload(...)` (code lines 193-209) mirrors that shape on the refusal side: `paused` is
`False`, the status is the refusal status, and no next call is proposed either.

### Conventions

- The module owns its caller-facing vocabulary as module constants — `_ALREADY_VACANT_STATE`,
  `_ALREADY_VACANT_SUMMARY`, `_SELECTION_MISSING`, `_PAUSED_SUMMARY`, `_PAUSE_NEXT_STEP` and
  `_RELEASE_REFUSAL_DETAIL`; every payload builder copies `_PAUSE_NEXT_STEP` with `dict(...)` so a
  caller cannot mutate the module's own step.
- `_already_stopped_result` narrows on the release authority's own status constant
  (`error.status != _SELECTION_MISSING` returns `None`) and then asks the activation plane directly
  through `observe_atomic_series`, rather than inferring vacancy from the error alone. It introduces
  no second vacancy authority: the state it reports is the existing observed `vacant` state.
- Both payload shapes report `contractPath`/`enclosurePath` (success) or `contract_path`
  (refusal) from the resolved contract, so a stop is always addressed by the contract it stopped.
- The delegation is one call: the pause introduces **no second scheduling, release or publication
  authority**. Sync cancellation, terminal cleanup and the pause all release through the same
  `release_atomic_series_selection`.

### Invariants And Boundaries

- **The pause publishes nothing.** It moves no ref, creates no commit, lands nothing, writes no
  ledger row, and advances no unstarted leaf. The master keeps its code and memory work branches,
  its worktrees, its enclosure and every unstarted leaf byte-identically, and the destination
  (protected source) branch is untouched. The already-stopped success is inert in exactly the same
  way — it writes no record to say so, which is what makes it a report rather than a write.
- **A master holding no selection is already stopped, and the pause says so.** This is the ordinary
  state of a master between landings, so the verb succeeds with `state`/`status`
  `atomic-series-already-vacant`, `paused: true` and the same stop next step, instead of failing an
  intent it has just satisfied. The success is explicit, never silent: `_ALREADY_VACANT_SUMMARY` names
  that no selection was held, so a caller can tell it apart from a real release.
- **Only vacancy is answered that way.** An unreadable record and a record naming another master stay
  refusals, because neither proves the master is inactive; `release_atomic_series_selection` itself is
  unchanged, because explicit sync cancellation still requires an existing exact selection. The
  260831-LOCR-L38 verification envelope proved each shape through the registered public route and left
  the blast radius stated rather than assumed: unparseable bytes at this master's own address refuse
  with `atomic-series-activation-release-unreadable` and are neither repaired nor released, and the
  dangerous shape — a **vacant** foreign record, which is the only foreign shape that reads `vacant`,
  exactly the state the already-stopped success keys on — refuses with
  `atomic-series-activation-selected-contract-mismatch` and leaves the master it names still `active`.
  The discriminator is the **release's status**, not the observation: a missing record is the only
  outcome that reaches `_already_stopped_result` at all, and a record that exists produces the
  exact-owner mismatch instead.
- **The release is what makes the stop real.** When a selection *is* held, the activation selection is
  the durable fact that says this master is the one exposing implementation work, so releasing it is
  the stop; marking the master without releasing it would stop nothing. The paused master's observed
  state is the existing released state (`vacant`) — there is no parallel paused state and no second
  authority.
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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The stop-only route: contract identity check, the series-only refusal, the release delegation, the already-stopped decision, both success payloads and the refusal payload. [1]
- The already-vacant vocabulary: the one release status the pause answers itself and the explicit already-stopped result, so a caller can tell "nothing was held" from a real release. [2]
- The hand-back: a `nextStep` carrying a summary and no `nextTool`/`nextArgs`, so the result proposes no continued execution. Both success payloads carry it unchanged. [3]
- The release authority the pause delegates to — strict explicit cancellation release, exact-owner proof, per-contract address, and the refusal statuses the pause explains (a missing selection is deliberately no longer among them). [4]
- The observation the already-stopped decision takes rather than assumes: absence is `vacant`, and a record that is not this exact contract refuses instead of being read as inactive. Its `_load_selected_contract` is the earlier guard an **active** foreign record meets, which is why only a **vacant** foreign record reaches the release's `selected-contract-mismatch`. [5]
- The activation record's contract-derived address is what makes one master's release leave another master's record alone. [6]
- The public tool the pause is reached through, and the payload builder it is reached by. [7]
- The facade re-export that keeps the public `git_worktree_manager` import path for the pause. [8]
- The response model that declares `paused` as the route's own claim. [9]
- The executable specification of the boundary: the pause's runtime-import closure is disjoint from every publication module. [10]
- The boundary proof: the public pause over real temporary Git repositories, measuring refs, object databases, coordination tree, worktrees and task documents before and after. The never-selected case asserts the already-vacant SUCCESS (it was a refusal before this change set), and the module's ten cases keep the four refusal shapes apart — a leaf contract, a record this contract does not own, an unreadable record, and a vacant record naming another master. [11]
- The end-to-end playthrough that proves the master a pause stops can still admit a leaf after its landing. [12]
- The separate publication the pause must never be reached as or described as. [13]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned stop route.

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
| `worktree_pause` | stops the master — releasing its activation selection, or reporting `atomic-series-already-vacant` when it holds none — and hands the turn back | nothing |
| `worktree_checkpoint_landing` | the explicitly requested partial PUBLICATION of a partial master | refs, ledger, `checkpointed` integration cell |
| `worktree_sync` / `worktree_attach` | the existing resume route for a paused master | nothing beyond ordinary selection/sync |

## 260831-LOCR-L38 The Already-Vacant Stop

A master between landings holds no activation record, and that is the ordinary state of a master the
developer wants parked rather than an error. The pause used to refuse that state with
`atomic-series-activation-selection-missing`, which meant the verb failed an intent it had just
satisfied — observed on LOCR itself, immediately after its checkpoint landing into IAS on 2026-09-13.
The developer's ruling: the verb succeeds, names the already-vacant fact explicitly rather than
silently, publishes nothing, and carries the same stop next step.

The change is local to this module and is one branch:

- `_already_stopped_result` answers exactly one release status, `_SELECTION_MISSING`, and only after
  re-observing the record through `observe_atomic_series` reports `vacant`. It therefore cannot
  convert a record that appeared, became unreadable, or names another master into a reported stop.
- `_RELEASE_REFUSAL_DETAIL` deliberately no longer carries a `selection-missing` entry: that is the
  one release outcome the pause answers itself, because the state it names is the state a pause
  produces.
- `release_atomic_series_selection` is unchanged. Explicit sync cancellation still requires an exact
  existing selection, so the release authority keeps refusing a missing one; the pause is the caller
  that reinterprets that specific status, not a second authority.
- The already-vacant payload carries the same `_PAUSE_NEXT_STEP` as a released pause, so the hand-back
  is identical in both success shapes.

`mcp/tests/test_lifecycle_playthrough_end_to_end.py` is the companion proof at the lifecycle level.

**The verification envelope (260831-LOCR-L38, 2026-09-15) proved this behaviour without changing a
production byte.** The leaf's own task document still narrates the defect as live; that narrative was
written 2026-09-13T20:13 and the fix landed at 21:02 in the master's checkpoint commit `9026c29e`,
which is an ancestor of the leaf's base `67b21aeb`. The leaf was therefore executed as a
**preservation** leaf: `mcp/src/**` is byte-identical to HEAD and the delivery is the boundary proof —
two records the already-stopped success must never be taken from, plus the registered-description pin
in `mcp/tests/test_tools.py`. Two things a later reader should not have to rediscover:

- The already-stopped success and the released pause are distinguishable in the payload, not only in
  the summary: the released path reports `state`/`status` `paused` and carries the record its own
  release wrote, while the already-stopped path reports `atomic-series-already-vacant` with an
  observation carrying **no** `record`, and both carry the same `_PAUSE_NEXT_STEP`.
- `selected-contract-mismatch` and `release-unreadable` are not two names for one situation. Only a
  **vacant** foreign record reaches the release's exact-owner guard; an **active** foreign record is
  refused earlier, by the observation's `_load_selected_contract`, and reports as `unreadable`. A case
  written against the active shape therefore proves nothing about the guard the vacant shape reaches.
