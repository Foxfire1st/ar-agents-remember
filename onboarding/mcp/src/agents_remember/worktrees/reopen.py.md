# mcp/src/agents_remember/worktrees/reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/reopen.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-05T08:46+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/ overview](../../../overview.md)

## Purpose

The `task_reopen` implementation cit:([`reopen_task`], mcp/src/agents_remember/worktrees/reopen.py:169-265): reopen a fully landed leaf task under its EXACT
same leaf id. It reopens a task by REWRITING THE LEAF'S ENCLOSURE CONTRACT, which is why
it lives in the worktrees package: it reads and amends the contract, emits a
`WorktreeCommandResult`, and renders through the worktree status payload, while the
document reset is the smaller half and goes through the `tasks` package the way every
other worktree operation does. Ranked the other way round — as a task operation that
happens to touch a contract — it made `tasks` and `worktrees` mutually dependent
(`layers.toml`): the task-document store could not be loaded without loading the whole
worktree lifecycle. Recreating worktrees stays `worktree_start`'s job.

## Code Commentary

### Logic

`reopen_task(contract_path, dry_run=False)` loads the enclosure contract and first runs
cit:([`_reopen_blockers`], mcp/src/agents_remember/worktrees/reopen.py:410-424): the contract must be `kind == "leaf"` with closeout, integration,
and cleanup all `completed`, and neither the code nor memory worktree may still exist
on disk — anything else returns a `blocked` payload (returncode 2) listing every
blocker.

On the happy path the contract rewrite is now **two nested calls, split by what the
type checker can see**:

- `dataclasses.replace(contract, ...)` clears the free-form provenance — `approved_for_commit`,
  `commit_approval_note`, the three commit hashes, `integration_strategy`, the three integrated
  hashes, `lifecycle_id`, `memory_state`.
- `amend_contract(..., ContractCells(human_review_status="pending-review",
  closeout_status="not-started", integration_status="not-started", cleanup="reopened"))` moves
  the four **vocabulary** cells.

The split is the fix, not a refactor. typeshed declares
`dataclasses.replace(obj, /, **changes: Any)`, so for as long as `cleanup="reopened"` was spelled
as a `replace` keyword it crossed the boundary **completely unchecked** — zero pyright
diagnostics against a `Literal`, measured. And `reopened` was one of the six values
`models.worktree.WorktreeSummary` then rejected, which is how the tool that writes it and the
packet that reports it disagreed about the contract this tool had just written.
`ContractCells` and `amend_contract` are the typed record and copy path that put those fields back in
front of the checker, leaving any cell they were
not handed alone. `cleanup: "reopened"` remains the tombstone marker `worktree_start`'s
existing-contract branch treats like `abandoned` (recreate fresh, never attach) — and it is now a
declared member of `CleanupStatus`, so the packet accepts it. cit:(["class ContractCells:"; "def amend_contract("; "CleanupStatus = Literal["], mcp/src/agents_remember/models/worktree.py:28-28; mcp/src/agents_remember/worktrees/worktree_contract.py:181-196; mcp/src/agents_remember/worktrees/worktree_contract.py:199-227)

`_plan_leaf_doc_reset` prepares the leaf task-document reset and publishes it only with the
contract-side reopen transaction. cit:([`_plan_leaf_doc_reset`], mcp/src/agents_remember/worktrees/reopen.py:393-436)
The paired cit:(["def _plan_master_index_reset("; "_validate_reopen_row_path(master_path"; "updated = demote_completed_master_if_unresolved(TaskDocument.model_validate(data))"], mcp/src/agents_remember/worktrees/reopen.py:580-580; mcp/src/agents_remember/worktrees/reopen.py:616-616; mcp/src/agents_remember/worktrees/reopen.py:618-618) plan applies the master's
`subTasks` row for the doc back to `planning`.

The reopen ledger-mapping proof now supplies the exact memory source commit.

### Invariants And Boundaries

- The leaf id NEVER changes across a reopen — that is the whole point; every doc,
  chat, and dashboard binding holds by construction because the identity is stable.
- Only a fully landed leaf reopens; in-flight leaves, masters/series contracts, and
  leaves with live worktrees are refused with explicit blockers.
- **A contract's vocabulary cells are moved through `ContractCells` /
  `amend_contract`, never as `dataclasses.replace` keywords.** `replace` is
  `**changes: Any` in typeshed, so a `replace` keyword is an unchecked write to a
  `Literal` field. `test_wire_vocabulary_exhaustiveness` enforces this as a rule
  across the package (`test_no_contract_cell_is_written_through_dataclasses_replace`),
  which is what stops a later edit from routing around the typed writer. The
  `replace` call that survives here is legitimate: it carries only free-form
  string/bool provenance fields, none of them a vocabulary cell.
- The tool mutates only coordination state: the enclosure contract, task docs, and the frozen
  landing-final observation it clears before reopening. cit:([`_clear_frozen_landing`], mcp/src/agents_remember/worktrees/reopen.py:391-407)
- `nextOperation` is always `worktree_start`: edit steps via `task_doc`, then start
  the same leaf id.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The doc lookup and lifecycle restamp helpers this module shares with worktree start. | `find_leaf_doc`; `plan_leaf_doc_lifecycle_restamp`; `restamp_leaf_doc_lifecycle` | mcp/src/agents_remember/tasks/leaf_doc.py:56-70; mcp/src/agents_remember/tasks/leaf_doc.py:161-175; mcp/src/agents_remember/tasks/leaf_doc.py:178-197 |
| The recreate-fresh branch admits `cleanup: reopened`. | "existing.cleanup in (\"abandoned\", \"reopened\")" | mcp/src/agents_remember/worktrees/modules/start.py:508-508 |
| Reopen publishes the frozen-landing clear, task resets, and contract rewrite under one task-fact CAS and reports projection refresh separately. | `publish_task_fact_mutation`; `_publish_reopen_transition` | mcp/src/agents_remember/worktrees/reopen.py:471-493 |
| The application entry point exposing this as the `task_reopen` MCP tool beside `task_doc`. | `task_reopen_tool` | mcp/src/agents_remember/application/task_docs/task_reopen.py:20-41 |
| The cleanup vocabulary includes abandoned and reopened as declared terminal/reopen states. | "CleanupStatus = Literal[" | mcp/src/agents_remember/models/worktree.py:28-28 |
| The typed contract amendment record holds the six optional vocabulary cells. | "class ContractCells:" | mcp/src/agents_remember/worktrees/worktree_contract.py:181-196 |
| The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. | "def amend_contract(" | mcp/src/agents_remember/worktrees/worktree_contract.py:199-227 |
| The wire model that reports `cleanup` and accepts `reopened` through `CleanupStatus`. | `WorktreeSummary` | mcp/src/agents_remember/models/worktree.py:148-198 |
| `test_no_contract_cell_is_written_through_dataclasses.replace` and `test_every_writable_cleanup_value_validates_at_the_wire_boundary` pin both halves of this. | `test_no_contract_cell_is_written_through_dataclasses_replace`; `test_every_writable_cleanup_value_validates_at_the_wire_boundary` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:302-306; mcp/tests/test_wire_vocabulary_exhaustiveness.py:669-677 |

## 260718-CHATS-L5I Current Delta

Task reopening now clears the persisted landing-final observation as part of returning a contract to active work and reports any clearing failure explicitly. A reopened task must not retain an old completed landing projection as current fact.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## L23 Thematic Master Reopen Boundary

Reopen first proves that the leaf's master contains its super-integration
source. If that parent edge is stale or unavailable, the operation returns the
shared lineage block/recovery payload before rewriting contract cells, leaf
state, or the master index. The intended recovery is to synchronize the
existing thematic master, not create a replacement master.

## 260815-DAG-L3 Publication History, Superseded By CLIVE

The earlier sprint-queue publisher no longer governs reopen. The current operation keeps frozen
landing clear, leaf/master task writes, and contract rewrite in one rollback-safe task-CAS batch;
projection invalidation/rebuild happens afterward and cannot roll that batch back.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers,
and active atomic-series refs are censused across code and external memory. CLIVE retains the exact
terminal predecessor, source-tip, ledger, and lineage proofs but removes queue state from the reopen
publication boundary.

Reopen proves a terminal leaf against its exact recorded landing, not its necessarily older start
base: code source must equal `integrated_code_commit`, and external-memory source must equal
`integrated_ledger_commit`, before task facts are reset.

The apply publication repeats that whole proof inside the task-CAS publication it uses for the
reset. It reloads and requires the exact preflighted terminal contract, rechecks current protected
source tips, and for external memory proves the recorded ledger maps the landed code commit to the
landed memory-content commit and reaches that content. A contract or ref race therefore returns a
blocked result without clearing frozen landing or rewriting task facts. The leaf/master reset plan
is rebuilt inside the same callback, so a concurrent task-doc edit is never overwritten by stale
prepared models.

## 260815-DAG Master Full-Gate Repair

Imports updated to the moved queue/integration packages; the contract review/closeout/integration reset was extracted into the `_reopened_contract` helper used by `reopen_task`.

## 260821-CLIVE Terminal Predecessor And Task Publication

Reopen requires the exact terminal lifecycle predecessor rather than inferring authority from a
missing or deleted enclosure. Its prepared contract/task reset publishes under the task CAS, with
exact original-source validation and rollback-safe document writes. Accepted task truth remains
authoritative; dry-run and apply report the same affected projection scopes/effects, and a rebuild
failure does not undo the reopen batch.

## Update History

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 2 declined citation claims against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated cleanup vocabulary from the typed amendment record and helper. Kept the prose claim and repaired its precise definitions and cleanup literal. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged exact terminal-predecessor proof, task-CAS publication, and independent projection refresh into reopen. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: imports updated to the moved packages; contract reset extracted into `_reopened_contract`. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored the `task_reopen_tool` citation to its current re-export line (task_doc_tools.py:87) and advanced the card verification stamp to the L16 tree; card source (worktrees/reopen.py) itself is unchanged by L16.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved the `task_reopen_tool` facade re-export within `task_doc_tools.py`; re-pointed the citation to `task_doc_tools.py:83-85`. Verification metadata unchanged.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: reopen now passes `memory_source_commit` to the external-ledger mapping proof. Verification remains closeout-owned.

- 2026-08-16T07:15+02:00 — L4 review repair: moved leaf/master reset planning into the locked publication so concurrent task-doc edits cannot be overwritten by stale preflight models.
- 2026-08-16T07:05+02:00 — L4 review repair: moved the exact terminal contract, source-tip, and external-ledger proof into the locked reopen publication boundary before any evidence is erased.

- 2026-08-16T06:15+02:00 — Dagger repair: terminal reopen now validates the current source pair against the leaf's exact landed commits, preserving own-atomic reopen without admitting source drift.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: replaced the retired direct restamp/publication
  claim with the queue-governed reopen transaction and preserved rollback semantics; verification
  remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: replaced the deleted `_reset_leaf_doc` account with the
  atomic `_plan_leaf_doc_reset` planning boundary. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented parent-lineage admission before reopen mutation and thematic-master recovery; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: split recreate-fresh admission, contract write, and lifecycle restamp onto their frozen-source owners; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-02T01:05+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/tasks/reopen.py` became `mcp/src/agents_remember/worktrees/reopen.py`, so this sidecar moved with it; `path`, the H1, and `governingOverview` (now `../../../overview.md`, matching the five sibling cards in this route — `worktrees/` has no route-local overview) follow. **The Purpose's stated rationale was inverted, not just re-pathed.** It read "it lives in the tasks package ... because the thing being reopened is the task"; the module now says the opposite and gives the reason: reopen rewrites the leaf's ENCLOSURE CONTRACT, emits a `WorktreeCommandResult` and renders through the worktree status payload, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent (`layers.toml`) — the task-document store could not be loaded without the whole worktree lifecycle. Behavior is unchanged; only the home and the justification are. Every self-citation was re-derived against the file at its new path rather than shifted by arithmetic — the module docstring was rewritten in the move, so all of them moved: `reopen_task` L45-L112 → L53-L120, `_reopen_blockers` L137-L151 → L145-L159, the split contract rewrite L63-L88 → L71-L96, the vocabulary cells L82-L87 → L90-L95, `_reset_leaf_doc` L154-L187 → L162-L195, `_reset_master_index` L190-L208 → L198-L216. The `worktree_contract.py` cross-file anchors also moved and were re-derived: `CleanupStatus` L55 → L67, `ContractCells` L171 → L183, `amend_contract` L188 → L200. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T10:12+02:00 — 260731-EFA-L4 curator: body corrected. The card now records that free-form
  provenance uses `dataclasses.replace`, vocabulary cells use `amend_contract(..., ContractCells(...))`,
  and `CleanupStatus` admits `reopened`; the current reference rows bind those claims to the frozen
  source. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. Purpose cited
  the `task_reopen` implementation at L11, which is now a line inside the module docstring; the
  entry point is `reopen_task` at L43-L102 (the module docstring grew to L1-L22 and the
  landing-freeze imports/helper landed after it). Named the function explicitly so the anchor is
  self-checking. Claim unchanged.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-03T00:30+02:00 — Created for L11 (leaf reopen semantics): `reopen_task` resets a completed
  leaf's contract and doc back to planning under its original leaf id, replacing the suffixed `-rN`
  reopen workaround. Verification metadata pinned until closeout stamps the code commit.
