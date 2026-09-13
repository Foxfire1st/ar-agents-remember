# mcp/tests/test_pause_stop_only_end_to_end.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pause_stop_only_end_to_end.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T19:02+02:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `overview.md` |

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
module carries eight: the no-publication measurement; the hand-back payload; the selection-missing
refusal; leave-idempotence; the leaf refusal; per-contract record isolation; the tampered-record
refusal; and resume.

### Conventions

- Lane `integration` in `mcp/tests/test-evidence-lanes.toml` (line 158), and every case is
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
- **Refusals are inert.** A never-selected master refuses with
  `atomic-series-activation-selection-missing` and writes no activation record and no coordination
  byte; a leaf contract refuses with `pause-requires-atomic-master` and leaves the parent master's own
  selection untouched; a record naming another contract refuses with
  `atomic-series-activation-release-unreadable` and is neither repaired nor released.
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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The measurement helpers: byte digest of a tree, one repository's full ref and object state, and a task document's status. | `_tree_digest`; `_git_state`; `_document_status` | mcp/tests/test_pause_stop_only_end_to_end.py:54-65; mcp/tests/test_pause_stop_only_end_to_end.py:67-78; mcp/tests/test_pause_stop_only_end_to_end.py:80-81 |
| The one-world-per-case fixture: two atomic masters on one shared source pair, each with its own contract-keyed record. | `PauseStopsAnAtomicMasterTests` | mcp/tests/test_pause_stop_only_end_to_end.py:84-116 |
| The public pause and the public select/resume route the module drives instead of inner helpers. | `_pause`; `_select` | mcp/tests/test_pause_stop_only_end_to_end.py:118-124; mcp/tests/test_pause_stop_only_end_to_end.py:126-133 |
| The measurement composite, the branch tips, the task-document walk, and the per-contract record read that make "nothing else moved" assertable. | `_world`; `_tips`; `_documents`; `_activation_bytes`; `_record_bytes` | mcp/tests/test_pause_stop_only_end_to_end.py:148-166; mcp/tests/test_pause_stop_only_end_to_end.py:168-179; mcp/tests/test_pause_stop_only_end_to_end.py:181-197; mcp/tests/test_pause_stop_only_end_to_end.py:137-139; mcp/tests/test_pause_stop_only_end_to_end.py:141-146 |
| The eight cases and the distinct protection each one buys. | `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_is_refused_and_writes_nothing`; `test_pausing_an_already_released_master_is_idempotent`; `test_pausing_a_leaf_contract_is_refused`; `test_pausing_one_master_leaves_the_other_masters_record_byte_identical`; `test_a_record_this_contract_does_not_own_is_refused_not_released`; `test_resuming_a_paused_master_restores_work_with_nothing_published` | mcp/tests/test_pause_stop_only_end_to_end.py:201-232; mcp/tests/test_pause_stop_only_end_to_end.py:234-261; mcp/tests/test_pause_stop_only_end_to_end.py:263-276; mcp/tests/test_pause_stop_only_end_to_end.py:278-292; mcp/tests/test_pause_stop_only_end_to_end.py:294-319; mcp/tests/test_pause_stop_only_end_to_end.py:321-363; mcp/tests/test_pause_stop_only_end_to_end.py:365-402; mcp/tests/test_pause_stop_only_end_to_end.py:404-428 |
| The public operation under test and the release it performs. | "def worktree_pause_tool("; "def pause_result(" | mcp/src/agents_remember/application/worktree_tools.py:470-499; mcp/src/agents_remember/worktrees/modules/pause.py:66-109 |
| The per-contract address and the observation the cases read to prove the released state is the existing `vacant`. | `contract_fingerprint`; `activation_path`; `observe_atomic_series`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-143; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-288 |
| The shared closeout fixture this module builds its real Git world from, and the Git helper it measures with. | `QueueFixture`; `MASTER_A`; `MASTER_B`; `git` | mcp/tests/test_closeout_queue.py:57-58; mcp/tests/test_closeout_queue.py:181-181; mcp/tests/test_worktree_support.py:83-83 |
| The lane this module is registered in. | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:155-158 |
| The two shared-support artifacts whose exact consumer lists carry this module (its entry sits inside each artifact block). | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:283-334; mcp/tests/evidence-lifecycle.toml:338-388 |
| The separate publication no case here reaches. | `worktree_checkpoint_landing` | mcp/src/agents_remember/mcp/registration/closeout.py:180-209 |
| The integration-case budget this module's membership is accounted against. | `integration_case_budget` | pyproject.toml:149-150 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned boundary proof.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: created the card for the new integration boundary
  proof. Recorded the public-operation-only discipline (`worktree_pause_tool`, `worktree_sync_tool`),
  the two-masters-one-source-pair fixture that makes per-contract isolation testable, the measurement
  composite and why the activation store is the one excluded write, the eight independently-failing
  cases and the distinct protection each buys, the refusal statuses, and the prohibition on ever
  pausing a master by landing it. Verification metadata remains closeout-owned; no acceptance claim.
