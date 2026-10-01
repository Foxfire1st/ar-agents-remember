# mcp/tests/test_pause_stop_only_end_to_end.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

The **boundary proof for the stop-only pause** added by `260831-LOCR-L37`, driven over real
temporary Git repositories through the **public** operation. Every other pause case is a unit proof
of one seam; this module measures the world before and after the stop.

The claim under test is a negative one — that pausing publishes nothing — so the fixture
**measures** it rather than asserting it: the exact branch tips, both repositories' complete object
databases, the whole coordination tree, both worktrees, the enclosure, and every task document with
its leaf rows and statuses. A ref move, a new commit object, a landing, a ledger row or a leaf
advance all show up as a difference. The activation snapshot is the pause's one legitimate write and
is measured separately, which is what makes "the pause touched nothing else" a real assertion.

It also pins what the pause must **not** report as a stop. The already-stopped success is answered
from an observed `vacant` state, and two records the pause can meet are not that: one that cannot be
read, and one whose `selectedMaster` names another master while reading `vacant`. Both refuse, and
both are asserted to leave the bytes they were refused for exactly as they were.

`worktree_checkpoint_landing` is the SEPARATE, explicitly requested publication. No case here
reaches it, and the module docstring states that as a prohibition: a test that paused a master by
landing it would be proving the defect this split exists to remove.

## Code Commentary

### Logic

`PauseStopsAnAtomicMasterTests` builds one real temporary Git world per case from
`test_closeout_queue.QueueFixture` with `atomic_a=True, atomic_b=True, memory_mode="external"`, so
**two atomic masters share one protected source pair while each holds its own contract-keyed
activation record** — the premise the isolation case depends on. `setUp` loads each master's canonical
**series** contract from the master task root and its leaf enclosure from the fixture's contract map,
and asserts the kinds and the shared source pair rather than assuming them.

The public operations:

- `_pause(series)` calls `worktree_tools.worktree_pause_tool` — the registered public entry point —
  and never `pause_result` or any inner helper.
- `_select(series)` calls `worktree_tools.worktree_sync_tool`, which is the existing public selecting
  route and therefore also the resume route.

The measurement:

- `_tree_digest(root)` — every tracked byte under a root, keyed by relative path, with `.git`
  internals excluded.
- `_git_state(repository)` — every ref (`for-each-ref`) **and** every object in the repository's
  complete object database (`cat-file --batch-all-objects --batch-check`).
- `_document_status(path)` — one task document's status, parsed through the real `TaskDocument`.
- `_world()` — the composite: both repositories' Git state, the coordination tree digest **excluding
  the activation store**, the leaf's code worktree and memory worktree digests. Excluding the
  activation store is deliberate and documented in the helper: the release writes there, and
  excluding the pause's one legitimate write is what lets everything else be asserted byte-identical.
- `_tips()` — the code work branch, the code destination/source branch, the memory work branch and
  the memory destination/source branch.
- `_documents()` — every task document under the task tree, masters, sprint and every unstarted leaf,
  admitting only objects carrying the task-document `kind` (the tree also holds non-document
  authority JSON such as the curator-coherence record, whose bytes `_world()` still covers).

Each case fails independently. Merging any two would make a failure ambiguous, which is why the
module carries ten: the no-publication measurement; the hand-back payload; the already-stopped
success a never-selected master now produces; release-idempotence; the leaf refusal; per-contract
record isolation; the record this contract does not own; the unreadable record; the record naming
another master; and resume. The last three are the refusal shapes the module keeps apart on purpose
— a leaf contract owns no selection, a record this contract does not own is someone else's
selection, and an unreadable record is not evidence of anything — and the state a master is actually
in decides which one a caller meets, so a single "refused" case would not pin them.

The two newest cases exist because the already-stopped success keys on an **observed** `vacant`
state, and two records the pause can meet also read `vacant` or must not be trusted: a record that
cannot be parsed, and a record whose `selectedMaster` names another master. The registered public
route refuses both, and the second is the shape that would be a reported stop if vacancy alone were
believed.

### Conventions

- Lane `integration` in `mcp/tests/test-evidence-lanes.toml` (line 163), and every case is
  `unittest`-style in one class with a temporary directory per case.
- The module drives public entry points only. Like `test_checkpoint_landing_end_to_end.py`, it exists
  because a seam-level suite can be fully green while the composition a caller reaches is wrong.
- Support is the existing `QueueFixture` plus this module's own measurement helpers — no new support
  module and no new shared artifact, which is the support cost recorded in the `pyproject.toml`
  integration-budget tradeoff block.
- The tampered-record case writes a foreign activation record through the production
  `AtomicSeriesActivationRecord` model rather than hand-written JSON, so the tamper is a real record
  at the wrong address.

### Invariants And Boundaries

- **Nothing moves.** `test_pausing_a_master_moves_no_ref_and_creates_no_commit` asserts equal tips,
  an equal `_world()`, equal documents, unchanged contract bytes, `integration_status ==
  "not-started"`, `closeout_status == "not-started"`, an unchanged cleanup cell, both worktrees still
  present, and the unstarted leaf's status unchanged.
- **The hand-back is the result's whole next-move contribution.**
  `test_a_paused_master_hands_the_turn_back_with_no_next_call` asserts `state` and `status` are
  `"paused"`, `paused is True`, `operation == "worktree_pause"`, that `nextTool`, `nextArgs` and
  `nextOperation` are **absent** at both the top level and inside `nextStep`, that the summary says
  "Nothing was published", and that `observe_atomic_series(...).state == "vacant"` with the released
  record echoed in `atomicSeriesActivation`.
- **Refusals are inert, and the one non-refusal is inert too.** The never-selected case **succeeds**:
  a master holding no selection is already stopped, so `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`
  asserts `ok`, `state` and `status` both `atomic-series-already-vacant`, `paused is True`,
  `atomicSeriesActivation.state == "vacant"`, and no `nextTool`/`nextArgs`/`nextOperation` at either
  level; the success is also asserted to be **explicit and unmistakable** — the state is not the
  released `"paused"`, the summary names that no selection was held and that nothing was published,
  `nextStep` carries exactly `summary`, and the observation carries **no** `record` where a released
  pause carries the record its own release wrote — and then asserted **inert**: no activation record
  was created, and the branch tips, `_world()`, every task document and the ledger bytes are
  unchanged. That is the byte-level form of "nothing was written to say so". A leaf contract refuses
  with `pause-requires-atomic-master` and leaves the parent master's own selection untouched; a
  record this contract does not own (an **active** foreign record) refuses with
  `atomic-series-activation-release-unreadable` and is neither repaired nor released; an
  **unreadable** record refuses with the same `atomic-series-activation-release-unreadable` and has
  its bytes compared before and after; and a **vacant** foreign record — fingerprint and path of
  this contract, `selectedMaster` naming the other master, so the observation itself reads `vacant`
  — refuses with `atomic-series-activation-selected-contract-mismatch`, is never released, and leaves
  the master it names still `active`. The case asserts that `vacant` premise through
  `observe_atomic_series` before pausing, which is what makes it a proof rather than an outcome
  check. (Before this change set the never-selected case asserted the
  `atomic-series-activation-selection-missing` refusal; the pause now answers that status itself.)
- **The foreign-record shape decides which guard a caller meets.** An *active* foreign record is
  refused one step earlier, inside the observation's `_load_selected_contract`
  (`atomic-series-activation-master-mismatch` → observation `unreadable`), so it surfaces as
  `atomic-series-activation-release-unreadable`; only a *vacant* foreign record reaches the release's
  own exact-owner guard and its `selected-contract-mismatch`. Both are refusals and both are inert,
  but a case written against the active shape cannot reach the guard the vacant shape reaches — the
  two cases are not interchangeable.
- **Per-contract isolation.** The two masters' `activation_path`s differ and their records name
  different masters; pausing A leaves B's record bytes identical, B's state `active`, and B able to
  select again through the public route. Neither master is a waiting reason for the other, and the
  retired cross-master vocabulary (`paused-by`, `not-selected`) appears nowhere in the result.
- **Idempotent and reversible.** A second pause reports the same stopped master and leaves the
  released record bytes unchanged. Resume through `worktree_sync` restores `active` and the pause
  works again afterwards; stop and resume together leave tips, object databases, coordination tree
  and contract bytes as they were.
- The module must never be extended to pause a master by landing it. That is the regression this
  whole split exists to prevent.

### Todos

None recorded. Verification metadata on this card remains closeout-owned.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The measurement helpers: byte digest of a tree, one repository's full ref and object state, and a task document's status. [1]
- The one-world-per-case fixture: two atomic masters on one shared source pair, each with its own contract-keyed record. [2]
- The public pause and the public select/resume route the module drives instead of inner helpers. [3]
- The measurement composite, the branch tips, the task-document walk, and the per-contract record read that make "nothing else moved" assertable. [4]
- The ten cases and the distinct protection each one buys. The never-selected case asserts the already-vacant SUCCESS, its explicitness (state is not `paused`, the summary names that nothing was held, the observation carries no `record`) and its inertness; before this change set it asserted the missing-selection refusal. The last three cases are the three refusal shapes: a leaf contract, an active foreign record (`…release-unreadable`) and an unreadable record (`…release-unreadable`), and a vacant foreign record (`…selected-contract-mismatch`), the one shape that reads `vacant`. [5]
- The public operation under test and the release it performs, including the already-stopped branch the never-selected case now reaches. [6]
- The per-contract address and the observation the cases read to prove the released state is the existing `vacant`. [7]
- The observation's own guard the *active* foreign record meets before the release's exact-owner guard, which is why the two foreign-record cases produce different refusal statuses. [8]
- The exact-owner guard the *vacant* foreign record reaches, and the release that refuses it as a contract mismatch. [9]
- The shared closeout fixture this module builds its real Git world from, and the Git helper it measures with. [10]
- The lane this module is registered in. [11]
- The shared closeout fixture this module builds its real Git world from, and the Git helper it measures with. [12]
- The lane this module is registered in. [13]
- The shared-support artifact whose exact consumer list carries this module (its entry is at `:369` in the block). [14]
- The separate publication no case here reaches. [15]
- The integration-case budget this module's membership is accounted against. [16]
- The end-to-end playthrough that exercises pause and resume in lifecycle order and proves the master a pause stops still admits a leaf. [17]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned boundary proof.
