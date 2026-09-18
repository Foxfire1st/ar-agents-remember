# mcp/tests/test_pause_stop_only_end_to_end.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pause_stop_only_end_to_end.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:18+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The measurement helpers: byte digest of a tree, one repository's full ref and object state, and a task document's status. | `_tree_digest`; `_git_state`; `_document_status` | mcp/tests/test_pause_stop_only_end_to_end.py:59-69; mcp/tests/test_pause_stop_only_end_to_end.py:72-82; mcp/tests/test_pause_stop_only_end_to_end.py:85-86 |
| The one-world-per-case fixture: two atomic masters on one shared source pair, each with its own contract-keyed record. | `PauseStopsAnAtomicMasterTests` | mcp/tests/test_pause_stop_only_end_to_end.py:86-556 |
| The public pause and the public select/resume route the module drives instead of inner helpers. | `_pause`; `_select` | mcp/tests/test_pause_stop_only_end_to_end.py:120-126; mcp/tests/test_pause_stop_only_end_to_end.py:128-137 |
| The measurement composite, the branch tips, the task-document walk, and the per-contract record read that make "nothing else moved" assertable. | `_world`; `_tips`; `_documents`; `_activation_bytes`; `_record_bytes` | mcp/tests/test_pause_stop_only_end_to_end.py:153-171; mcp/tests/test_pause_stop_only_end_to_end.py:173-184; mcp/tests/test_pause_stop_only_end_to_end.py:183-201; mcp/tests/test_pause_stop_only_end_to_end.py:142-144; mcp/tests/test_pause_stop_only_end_to_end.py:146-151 |
| The ten cases and the distinct protection each one buys. The never-selected case asserts the already-vacant SUCCESS, its explicitness (state is not `paused`, the summary names that nothing was held, the observation carries no `record`) and its inertness; before this change set it asserted the missing-selection refusal. The last three cases are the three refusal shapes: a leaf contract, an active foreign record (`…release-unreadable`) and an unreadable record (`…release-unreadable`), and a vacant foreign record (`…selected-contract-mismatch`), the one shape that reads `vacant`. | `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`; `test_pausing_an_already_released_master_is_idempotent`; `test_pausing_a_leaf_contract_is_refused`; `test_pausing_one_master_leaves_the_other_masters_record_byte_identical`; `test_a_record_this_contract_does_not_own_is_refused_not_released`; `test_an_unreadable_record_is_refused_not_reported_stopped`; `test_a_record_naming_another_master_is_refused_not_released`; `test_resuming_a_paused_master_restores_work_with_nothing_published` | mcp/tests/test_pause_stop_only_end_to_end.py:206-237; mcp/tests/test_pause_stop_only_end_to_end.py:239-266; mcp/tests/test_pause_stop_only_end_to_end.py:268-320; mcp/tests/test_pause_stop_only_end_to_end.py:322-336; mcp/tests/test_pause_stop_only_end_to_end.py:338-363; mcp/tests/test_pause_stop_only_end_to_end.py:365-407; mcp/tests/test_pause_stop_only_end_to_end.py:409-446; mcp/tests/test_pause_stop_only_end_to_end.py:448-474; mcp/tests/test_pause_stop_only_end_to_end.py:473-526; mcp/tests/test_pause_stop_only_end_to_end.py:565-589 |
| The public operation under test and the release it performs, including the already-stopped branch the never-selected case now reaches. | "def worktree_pause_tool("; "def pause_result("; `_already_stopped_result`; `_already_vacant_payload` | mcp/src/agents_remember/application/worktree_tools.py:466-495; mcp/src/agents_remember/worktrees/modules/pause.py:79-82; mcp/src/agents_remember/worktrees/modules/pause.py:80-128; mcp/src/agents_remember/worktrees/modules/pause.py:130-149 |
| The per-contract address and the observation the cases read to prove the released state is the existing `vacant`. | `contract_fingerprint`; `activation_path`; `observe_atomic_series`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-287 |
| The observation's own guard the *active* foreign record meets before the release's exact-owner guard, which is why the two foreign-record cases produce different refusal statuses. | `_observation_from_record`; `_load_selected_contract` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:338-357; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:375-401 |
| The exact-owner guard the *vacant* foreign record reaches, and the release that refuses it as a contract mismatch. | `_record_selects_contract`; `release_atomic_series_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:79-88; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:23-53 |
| The shared closeout fixture this module builds its real Git world from, and the Git helper it measures with. | "class QueueFixture:"; "MASTER_A = TaskDocumentRef("; "MASTER_B = TaskDocumentRef("; "def git(repo: Path, *args: str) -> str:" | mcp/tests/test_closeout_queue.py:184-694; mcp/tests/test_closeout_queue.py:56-56; mcp/tests/test_closeout_queue.py:57-57; mcp/tests/test_worktree_support.py:79-79 |
| The lane this module is registered in. | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:235-235 |
| The shared closeout fixture this module builds its real Git world from, and the Git helper it measures with. | "class QueueFixture:"; "MASTER_A = TaskDocumentRef("; "MASTER_B = TaskDocumentRef("; "def git(repo: Path, *args: str) -> str:" | mcp/tests/test_closeout_queue.py:177-184; mcp/tests/test_closeout_queue.py:56-56; mcp/tests/test_closeout_queue.py:57-57; mcp/tests/test_worktree_support.py:79-79 |
| The lane this module is registered in. | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:235-235 |
| The shared-support artifact whose exact consumer list carries this module (its entry is at `:369` in the block). | "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:329-389 |
| The separate publication no case here reaches. | `worktree_checkpoint_landing` | mcp/src/agents_remember/mcp/registration/closeout.py:173-201 |
| The integration-case budget this module's membership is accounted against. | `integration_case_budget` | pyproject.toml:176-215 |
| The end-to-end playthrough that exercises pause and resume in lifecycle order and proves the master a pause stops still admits a leaf. | `LifecyclePlaythroughTests` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned boundary proof.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:211-211. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:323-323. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_pause_stop_only_end_to_end.py`, `_tree_digest`, `_git_state`, `_document_status`, `_world`, `_tips`, `_documents`, `_activation_bytes` and 11 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand** — `mcp/tests/test_pause_stop_only_end_to_end.py`, `_tree_digest`, `_git_state`, `_document_status`, `_world`, `_tips`, `_documents`, `_activation_bytes` and 11 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_pause_stop_only_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:204-204`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:202-202` -> `mcp/tests/test-evidence-lanes.toml:203-203`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T01:52:52+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:40:00+00:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read the one row whose range the mechanical projection had rewritten, and re-cited it by hand.** The row asserts that `integration_case_budget` is the budget this module's membership is accounted against; the identifier's own declaration moved from `:287` to `:305` when this candidate raised the pair, so the row cites `pyproject.toml:305-305` — the extent the engine resolves for it, and the only line in that file that carries the identifier at all (the surrounding comments spell the raises as "300 -> 340" prose, not as the key). The claim itself is unchanged and still true: this module is registered in the `integration` lane and that key is the cap its membership is accounted against. Nothing else in this card was re-read in this pass. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:166-166. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `integration_case_budget` at pyproject.toml:287-287.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `pause_result` in the row 173 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:131-150 to mcp/src/agents_remember/worktrees/modules/pause.py:79, the extent of the construct the claim is about (the checker named line(s) [79] as its live location); re-pointed `_activation_bytes` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:173-174 to mcp/tests/test_pause_stop_only_end_to_end.py:142, the extent of the construct the claim is about (the checker named line(s) [142, 279, 316] as its live location); re-pointed `_document_status` in the row 168 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:72-73 to mcp/tests/test_pause_stop_only_end_to_end.py:85, the extent of the construct the claim is about (the checker named line(s) [85, 232, 235] as its live location); re-pointed `_documents` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:142 to mcp/tests/test_pause_stop_only_end_to_end.py:186, the extent of the construct the claim is about (the checker named line(s) [186, 212, 222] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `pause_result` in the row 173 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:130-133 to mcp/src/agents_remember/worktrees/modules/pause.py:79-82, the extent of the construct the claim is about (the checker named line(s) [79] as its live location); re-pointed `_activation_bytes` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:153-154 to mcp/tests/test_pause_stop_only_end_to_end.py:142-143, the extent of the construct the claim is about (the checker named line(s) [142, 279, 316] as its live location); re-pointed `_document_status` in the row 168 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:59-60 to mcp/tests/test_pause_stop_only_end_to_end.py:85-86, the extent of the construct the claim is about (the checker named line(s) [85, 232, 235] as its live location); re-pointed `_documents` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:142-143 to mcp/tests/test_pause_stop_only_end_to_end.py:186-187, the extent of the construct the claim is about (the checker named line(s) [186, 212, 222] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_activation_bytes` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:173-174 to mcp/tests/test_pause_stop_only_end_to_end.py:142-143, the extent of the construct the claim is about (the checker named line(s) [142, 279, 316] as its live location); re-pointed `_already_stopped_result` in the row 173 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:79-82 to mcp/src/agents_remember/worktrees/modules/pause.py:130-133, the extent of the construct the claim is about (the checker named line(s) [116, 130] as its live location); re-pointed `_document_status` in the row 168 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:72-73 to mcp/tests/test_pause_stop_only_end_to_end.py:85-86, the extent of the construct the claim is about (the checker named line(s) [85, 232, 235] as its live location); re-pointed `_documents` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:142-143 to mcp/tests/test_pause_stop_only_end_to_end.py:186-187, the extent of the construct the claim is about (the checker named line(s) [186, 212, 222] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 181 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `pause_result` in the row 173 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:80-128 to mcp/src/agents_remember/worktrees/modules/pause.py:79-82, the extent of the construct the claim is about (the checker named line(s) [79] as its live location); re-pointed `_activation_bytes` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:153-154 to mcp/tests/test_pause_stop_only_end_to_end.py:142-143, the extent of the construct the claim is about (the checker named line(s) [142, 279, 316] as its live location); re-pointed `_document_status` in the row 168 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:59-60 to mcp/tests/test_pause_stop_only_end_to_end.py:85-86, the extent of the construct the claim is about (the checker named line(s) [85, 232, 235] as its live location); re-pointed `_documents` in the row 171 of this card from mcp/tests/test_pause_stop_only_end_to_end.py:142-143 to mcp/tests/test_pause_stop_only_end_to_end.py:186-187, the extent of the construct the claim is about (the checker named line(s) [186, 212, 222] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_pause_stop_only_end_to_end.py:153-154 in the row 171 of this card; the repetition added no pooled evidence; kept one copy of the repeated citation mcp/tests/test_pause_stop_only_end_to_end.py:365-366 in the row 172 of this card; the repetition added no pooled evidence; kept one copy of the repeated citation mcp/tests/test_pause_stop_only_end_to_end.py:59-60 in the row 168 of this card; the repetition added no pooled evidence

- 2026-09-15T11:18:00+00:00 — 260831-LOCR-L38 verification envelope (uncommitted change set on
  `ar/260831-locr-l38`, base `67b21aeb`): the module went from eight cases to **ten** and the
  at-HEAD already-vacant behaviour was proved rather than changed (`mcp/src/**` is byte-identical to
  HEAD; the delivered change is this module plus the `test_tools.py` pin). Added
  `test_an_unreadable_record_is_refused_not_reported_stopped` (unparseable bytes at this master's own
  per-contract address refuse with `atomic-series-activation-release-unreadable`, `paused: False`,
  bytes neither repaired nor released) and
  `test_a_record_naming_another_master_is_refused_not_released` (a **vacant** foreign record — this
  contract's fingerprint and path, another master's `selectedMaster`, so the observation itself reads
  `vacant` — refuses with `atomic-series-activation-selected-contract-mismatch` and is never
  released). Extended the never-selected case with the explicitness half (state is not the released
  `"paused"`, the summary names that no selection was held and that nothing was published, `nextStep`
  is exactly `{"summary"}`, the observation carries no `record`) and the inertness half (branch tips,
  coordination tree, both worktrees, every task document and the ledger bytes unchanged), and
  recorded the guard-order fact the second new case exists to reach: an *active* foreign record is
  refused one step earlier inside `_load_selected_contract` and surfaces as
  `atomic-series-activation-release-unreadable`, so only the *vacant* shape reaches the release's
  exact-owner guard. Re-derived every case range after the extension (cases are now
  `203-234`, `236-263`, `265-317`, `319-333`, `335-360`, `362-404`, `406-443`, `445-471`, `473-526`,
  `528-556`) and the helper ranges, repointed `worktree_pause_tool` to
  `application/worktree_tools.py:466-495`, corrected three activation helper ranges
  (`contract_fingerprint` `130-134`, `activation_waiting_reason` `275-287`), repaired two findings the
  scoped check returned on this card (the `QueueFixture` citation `test_closeout_queue.py:186-727` ran
  31 lines past EOF and its four anchors had drifted off their declarations, now fully re-derived —
  `class QueueFixture:` `184-696`, `MASTER_A` `:56`, `MASTER_B` `:57`, `def git(`
  `test_worktree_support.py:79`; and the `worktree_checkpoint_landing` claim, whose evidence
  changed since `bb65a207` — re-read against the current construct and repointed from
  `registration/closeout.py:180-209` to `:173-201`, wording unchanged), replaced the stale
  two-block `evidence-lifecycle.toml` row with the one block that now carries this module
  (`329-389`, entry at `:369`), and corrected the lane line in Conventions to `:163`. Verification
  metadata remains closeout-owned; no verification stamp advanced and no acceptance claim.

- 2026-09-14T18:00:00+00:00 — 260913-LCA-L12 curator (drift re-verification): the rewritten
  never-selected case is the change, and the earlier entries record it. Re-checked all eight case
  ranges, the helper ranges and the two manifest rows: they hold. No wording changed. Verification
  metadata remains closeout-owned.

- 2026-09-14T18:00:00+00:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 5 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 2 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.

- 2026-09-13T18:42:00+00:00 — 260831-LOCR-L38 (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): recorded the renamed and re-asserted never-selected
  case. `test_pausing_a_master_that_was_never_selected_is_refused_and_writes_nothing` is now
  `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing` and asserts the
  already-vacant SUCCESS (`ok`, `state == "atomic-series-already-vacant"`, `paused is True`,
  `atomicSeriesActivation.state == "vacant"`, no `nextTool`) plus the same inertness: no activation
  record created and `_world()` unchanged. The Purpose, the eight-case list, the refusal invariant and
  every reference row were re-derived against the current module (the never-selected case grew from 14
  to 22 lines, so five later case ranges shifted), the `pause_result` citation was repointed to
  `pause.py:80-128` after the pause module grew to 209 lines, the lane row was corrected to
  `test-evidence-lanes.toml:159`, the two evidence-lifecycle artifact blocks were re-cited as
  `282-336` and `338-392` with this module's consumer entries at `:319` and `:375`, and the playthrough
  module was added as the lifecycle-level companion. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-13T17:02:00+00:00 — 260831-LOCR-L37 curator: created the card for the new integration boundary
  proof. Recorded the public-operation-only discipline (`worktree_pause_tool`, `worktree_sync_tool`),
  the two-masters-one-source-pair fixture that makes per-contract isolation testable, the measurement
  composite and why the activation store is the one excluded write, the eight independently-failing
  cases and the distinct protection each buys, the refusal statuses, and the prohibition on ever
  pausing a master by landing it. Verification metadata remains closeout-owned; no acceptance claim.
