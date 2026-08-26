# mcp/src/agents_remember/worktrees/modules/startup/start_contract.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/worktrees/modules/startup/start_contract.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-08-26T18:32+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb` |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

`start_contract.py` owns worktree-start contract construction after the HFX-L4 extraction from
`start.py`. It builds or recovers root series contracts, selects and reconciles an atomic master
against its protected code/external-memory source pair before leaf admission, derives leaf
source/work branches and memory bases, validates the requested leaf ref, and returns a leaf contract
whose persisted `leaf_id` is the canonical task document id.

## Code Commentary

### Logic

`build_start_contract` is the public start-side entry. It wraps
`_build_start_contract` and converts **two** failures into the same
`WorktreeCommandResult` refusal shape that `start_result` can return. `_build_start_contract` asserts
the required start arguments, resolves `args.leaf_id or args.worktree_name` through
`leaf_ref_start`, then passes the resulting doc id into `default_contract`.

The two `except` clauses are the whole of the wrapper (260731-EFA-L4 added the second):

```python
try:
    return _build_start_contract(context, args)
except LeafRefResolutionError as exc:
    return invalid_leaf_ref_result(exc)
except ContractError as exc:
    return invalid_contract_request_result(exc)
```

**The two are not the same kind of failure, and the docstring was corrected in this leaf to stop
saying they were.** It previously claimed "Both refusals are bad *arguments*"; that was false.

- `LeafRefResolutionError` **is** always a bad argument: an unresolvable leaf ref.
- `ContractError` is **not** always an argument fault. The intended case is
  `worktree_contract._task_vocabulary`, which both `default_contract` and `default_series_contract`
  funnel through: `workflow_kind` and `memory_mode` arrive at the `worktree_start` MCP signature as
  free `str`, and that helper is where a *request* is narrowed onto the persisted vocabulary. But
  the `except` wraps the **whole call**, so it also catches a `ContractError` raised by the
  `write_contract(contract.contract_path, contract)` inside `_parent_series_contract`. The helper runs
  `validate_contract` before it writes, so
  that is a **write-validation failure of the PARENT series contract** — a cell already on disk or
  already computed for the parent, not anything this caller passed.

That second path is still reported honestly rather than swallowed — `validate_contract` names the
offending cell and the file, and the message rides into the refusal summary — so returning it is
deliberate. What would have been wrong is describing it as a caller mistake when the caller may have
supplied nothing at fault.

Both refusals are **returned, not raised**, for the same reason: the `worktree_start` handler has no
`except` for either, so anything that escapes this function reaches the MCP client as a traceback.
The `ContractError` catch is not redundant with the write gate for the *vocabulary* case:
`validate_contract` also refuses those cells, but only once `write_contract` is already running,
which for the leaf contract is after the code worktree exists.

Since 260731-EFA-L2 both constructor calls are assembled from the parameter objects
`worktree_contract.py` owns: a `ContractTask` (name, repo, coordination root, workflow kind, memory
mode, parent linkage), a `LeafIdentity` (worktree name, resolved leaf id, lifecycle id — leaf
contracts only), a code-side `RepoBranchPlan`, and a memory-side `RepoBranchPlan | None`. The
series call maps its protected/integration branches onto the same plan's
`source_branch`/`work_branch`.

The local helper `_memory_plan(memory_repo, *, source_branch, work_branch, base_commit)` returns
`None` when `memory_repo is None` — **absence is the whole state**: without a repo path there is no
memory branch, no memory base and no ledger, so a plan whose repo path is missing is not a plan.
`_external_memory_value` still blanks the memory work branch for non-external modes before it
reaches the plan.

The extracted parent-series helpers are unchanged in responsibility from their old `start.py` location:
they create/load a root series contract, ensure the integration branch when needed, derive memory source
and work branches for external memory, and compute `memory_base_for_source` from the source branch tip
rather than the current memory checkout. Existing `task.json` master artifacts are parsed through
`read_task_doc` without suppressing malformed documents; only missing optional artifacts are skipped.
Standalone/light tasks are accepted through the same start builder because `leaf_ref_start` delegates to
the shared resolver, which indexes non-master `task.json` docs as leaf candidates.

**Source-pair activation replaces the old global sequential lane.** Series bootstrap still gates on
the *effective* execution nature and commanding sprint, but contract existence is durable work truth,
not scheduling ownership. Multiple non-terminal series contracts may coexist. Apply-time preflight
reads the journal-to-contract handoff under the same per-master bootstrap mutex as publication, so a
concurrent loser cannot combine a pre-publication "no contract" read with a post-retirement "no
journal" read and misclassify the winner's branch as orphaned. After recovering or
creating the requested contract, `ensure_master_series_contract` validates activation inputs and
refreshes remote evidence before taking repository integration authority. Under that authority it
finishes the per-master bootstrap journal transaction without nesting store locks, then delegates to
`reconcile_selected_series_under_authority`. The requested contract becomes the source-pair selection
in `reconciling`, logically pausing the previous selection; it is returned as implementation authority
only after exact source synchronization publishes it `active`. A retained conflict or damaged
authority returns the transaction's resolvable/refused result and `_build_start_contract` does not
construct or expose a leaf beneath it.

`dry_run` remains planning-only: it returns an existing or planned contract without fetching,
publishing the selector, writing the bootstrap journal, creating branches, or starting a sync
generation. Organizational semantics still exist only under an authored execution graph; a
graph-less master uses atomic semantics. Terminal series artifacts are replaceable stale artifacts,
not evidence that another master owns a global lane.

### Invariants And Boundaries

- `start.py` is now only the orchestration caller for contract construction; leaf-ref policy lives in
  `worktrees/leaf_refs.py` with start-specific adaptation in `leaf_ref_start.py`.
- A bad leaf ref returns `leaf-ref-not-found` or `leaf-ref-ambiguous` before any persistent start writes.
- A `workflow_kind` or `memory_mode` outside the contract vocabulary returns `invalid-request`,
  likewise before any persistent start write. `build_start_contract` is the only place either
  refusal is converted; add an `except` here rather than letting a new contract-construction error
  escape to the tool handler.
- **`invalid-request` does not imply the caller supplied something invalid.** The `except
  ContractError` covers the whole of `_build_start_contract`, and `_parent_series_contract` writes
  the parent series contract inside it, so a `validate_contract` refusal on the PARENT can
  surface under the same result state. Do not narrow the docstring or the card back to "both
  refusals are bad arguments"; when triaging an `invalid-request` from `worktree_start`, read the
  message — `validate_contract` names the offending cell and the file it belongs to, which is what
  distinguishes the two paths.
- Worktree-start contracts persist doc ids, not legacy file stems.
- Malformed task documents fail loudly during parent-series detection.
- Multiple commanded masters may have live series contracts. Exactly one is selected per normalized
  protected source pair, and selecting a different master pauses rather than deletes the prior work.
- A leaf under an atomic master is not admitted until its parent selection has reconciled and become
  active; neither task prose nor closeout queue state supplies that authority.
- Apply-time bootstrap preflight and bootstrap publication use the same per-master store lock; the
  unlocked planning-only dry run never writes lock or lifecycle state.
- Integration authority and the per-master bootstrap store lock do not nest with another store lock.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Master bootstrap separates durable contract creation from disposable source-pair selection, refreshes before integration authority, and reconciles before returning. | `ensure_master_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:221-288 |
| Selection and exact sync-before-exposure are owned by the focused activation transaction. | `activate_atomic_series_contract`; `sync_selected_atomic_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:41-79; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:113-136 |
| Shared leaf-ref validation and candidate reporting. | `LeafRefResolutionError`; `resolve_leaf_ref` | mcp/src/agents_remember/worktrees/leaf_refs.py:39-66; mcp/src/agents_remember/worktrees/leaf_refs.py:88-141 |
| Start-side conversion from leaf-ref resolution errors and contract-construction errors into command results. | `invalid_leaf_ref_result`; `invalid_contract_request_result` | mcp/src/agents_remember/worktrees/modules/startup/leaf_ref_start.py:26-35; mcp/src/agents_remember/worktrees/modules/startup/leaf_ref_start.py:38-53 |
| The start operation returns through `start_result`. | `start_result` | mcp/src/agents_remember/worktrees/modules/start.py:482-493 |
| `start_result` calls `build_start_contract` before existing-contract handling, preflight, and enclosure creation. | "contract = build_start_contract(context"; "existing_result = _existing_contract_result(context"; "preflighted = _preflighted_contract(context"; "return _create_start_enclosure(context" | mcp/src/agents_remember/worktrees/modules/start.py:484-484; mcp/src/agents_remember/worktrees/modules/start.py:487-487; mcp/src/agents_remember/worktrees/modules/start.py:490-490; mcp/src/agents_remember/worktrees/modules/start.py:493-493 |
| The start operation creates its enclosure through `_create_start_enclosure`. | `_create_start_enclosure`; "return _create_start_enclosure(context" | mcp/src/agents_remember/worktrees/modules/start.py:493-493; mcp/src/agents_remember/worktrees/modules/start.py:620-682 |
| `_task_vocabulary` and `validate_contract` are distinct sources of `ContractError`. | `_task_vocabulary`; `validate_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:162-179; mcp/src/agents_remember/worktrees/worktree_contract.py:795-850 |

## Cross-Repo References

No meaningful cross-repository reference applies beyond the configured external-memory pair that
the contract records explicitly.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260815-DAG-L4 Integration-Authority Impact

Task-derived integration refs remain mechanically non-ordinary: repository defaults, sprint supers,
and atomic-series refs are censused across code and external memory. Leaf publication still uses the
exact configured locator and task CAS, while source-pair selection/reconciliation uses repository
integration authority. No mutable queue lane participates in start admission.

## 260821-CLIVE-L2 Current Contract

The current source seams include `memory_base_for_source`, `memory_mode_for_repository`, `MasterSeriesContractSpec`. New enclosures publish the strict root manifest, canonical journal directory, and locked address-only locator before exposure or operation admission. Pre-existing readable enclosures require the explicit adoption route; start never infers or falls back.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `memory_base_for_source`, `memory_mode_for_repository`, `MasterSeriesContractSpec` at this ownership boundary. | `memory_base_for_source`; `memory_mode_for_repository`; `MasterSeriesContractSpec` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:127-136; mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:196-203; mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:206-218 |

## Update History

- 2026-08-26T18:32+02:00 — Bound apply-time bootstrap preflight to the existing per-master journal
  mutex, closing the contract/journal handoff race that could reject a concurrent winner's protected
  branch as orphaned. Dry-run remains read-only and verification remains closeout-owned.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for this changed
  startup-contract card.

- 2026-08-26T03:37+02:00 — Replaced the obsolete single-in-flight sequential-lane contract with
  source-pair activation: multiple live series are normal, selection pauses the previous master,
  bootstrap and selector stores never nest, and reconciliation must reach active before leaf
  admission. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/modules/startup/start_contract.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: series bootstrap gates on the effective execution
  nature (nature-less legacy masters resolve atomic), the atomic-sequential lane block returns a
  `sequential-lane-owned` blocked result naming the owner and legal next operations (fails closed
  on resolution errors), organizational semantics apply only under an authored graph, and terminal
  series artifacts are ignored with a `staleSeriesArtifact` fact. Verification remains
  closeout-owned.

- 2026-08-19T04:05+02:00 — No content impact: 260815-DAG-L10 re-pointed the internal
  `_same_master_task_edge` idempotence comparison at `worktree_group_for(...)`; the contract
  construction and refusal-conversion behavior this card documents is unchanged. Verification
  metadata stamped at the landed code commit `e41ea31d`.
- 2026-08-16T06:15+02:00 — No behavior change: split task-derived source selection and exact code/external-memory base reads out of `_build_start_contract`; the builder retains one canonical construction path and no compatibility fallback.
- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:36+02:00 — L23 final candidate review: contract preparation derives canonical
  sprint/master/leaf code and external-memory ancestry, compares Git common-directory identity, and
  fails closed with task-addressed sync guidance before process creation.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: split resolver-result, start-operation, and
  contract-validation ownership; bound start ordering/caller flow to exact implementation anchors and
  rewrote stale line references.

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator: corrected the ContractError scope, separated
  vocabulary refusal from parent-series write validation, and pinned the wrapper ownership. The
  current table above supersedes the old line-specific references.
- 2026-08-01T09:17+02:00 — 260731-EFA-L4 curator: the Code Commentary said `build_start_contract`
  converts `LeafRefResolutionError`; it now converts two failures. Added the second `except
  ContractError as exc: return invalid_contract_request_result(exc)` clause, the new
  `invalid_contract_request_result` import from `leaf_ref_start`, and where the error comes from —
  `worktree_contract._task_vocabulary`, which both `default_contract` and
  `default_series_contract` now funnel through and which is where a free-`str` `workflow_kind` /
  `memory_mode` request is narrowed onto the persisted vocabulary. Recorded that this catch is not
  redundant with `validate_contract`'s write gate (that one fires inside `write_contract`, after the
  code worktree exists) and added the matching invariant. The L2 parameter-object description,
  `_memory_plan`, and the parent-series helpers were re-read against the current file and are
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  both `default_series_contract` and `default_contract` calls were re-assembled onto the
  `ContractTask` / `LeafIdentity` / `RepoBranchPlan` parameter objects, and the local
  `_memory_plan(...)` helper was added (returns `None` when there is no memory repository). The
  built contracts are identical. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: exported `memory_base_for_source` as the public helper used
  by `start.py` and tests, and documented that default light-task starts now resolve through the shared
  non-master `task.json` candidate path. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created by extracting start contract construction and
  leaf-ref normalization out of `start.py`, keeping the large start module from growing while making
  canonical doc-id persistence the start contract path. Verification metadata pinned until closeout
  stamps the 260707-HFX-L4 commit.