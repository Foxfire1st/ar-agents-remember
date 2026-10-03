# mcp/src/agents_remember/worktrees/modules/startup/start_contract.py

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

`start_contract.py` owns worktree-start contract construction after the HFX-L4 extraction from
`start.py`. It builds or recovers root series contracts, selects and reconciles an atomic master in
that contract's own activation record before leaf admission, derives leaf source/work branches and
memory bases, validates the requested leaf ref, and returns a request-scoped `StartContractPlan` whose leaf contract persists the canonical task document id as `leaf_id`. The same owner-validated parent is carried only for preview.

## Request-scoped preview authority

`build_start_contract` now returns `StartContractPlan` or the existing refusal. `_build_start_contract` derives the leaf through the same canonical/task/source owner and retains that owner's actual parent object only for `args.dry_run`; apply stores `preview_parent=None`. The internal wrapper is not a new constructor, public request/result field, durable contract or activation.

`ensure_master_series_contract` remains the one bootstrap/planning owner: planning observes canonical topology, source/ref and journal facts without publication, while actual apply keeps its per-master transaction and exact current activation/source revalidation. Only actual implementation exposure requires reconciled active authority; an admitted preview does not claim activity.


- The existing builder returns a leaf plus its same-request preview-only parent. [18]
- The public start-side adapter preserves existing typed refusals. [19]

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

**Contract-keyed activation replaces the old global sequential lane.** Series bootstrap still gates on
the *effective* execution nature and commanding sprint, but contract existence is durable work truth,
not scheduling ownership. Multiple non-terminal series contracts may coexist. Apply-time preflight
reads the journal-to-contract handoff under the same per-master bootstrap mutex as publication, so a
concurrent loser cannot combine a pre-publication "no contract" read with a post-retirement "no
journal" read and misclassify the winner's branch as orphaned. After recovering or
creating the requested contract, `ensure_master_series_contract` validates activation inputs and
refreshes remote evidence before taking repository integration authority. Under that authority it
finishes the per-master bootstrap journal transaction without nesting store locks, then delegates to
`reconcile_selected_series_under_authority`. The requested contract becomes the selection in its OWN
activation record — keyed per series contract rather than per protected source pair — and no other
master is named, selected, or logically paused, because a foreign master's record can never be
adopted (`atomic-series-activation-contract-mismatch`). The contract is returned as implementation
authority only after exact source synchronization publishes it `active`; the only surviving
activation waiting reason is `atomic-series-reconciling`. A retained conflict or damaged
authority returns the transaction's resolvable/refused result and `_build_start_contract` does not
construct or expose a leaf beneath it.

**No lifecycle cell seals leaf admission (260831-LOCR child-admission seal removal).** The seal that
used to stand at this boundary — `worktrees/atomic_series_seal.py::require_series_accepting_leaves`,
called from `ensure_master_series_contract` in both the dry-run and the locked apply arm and again
from `_parent_series_contract` — is deleted, together with its module. It refused a new or reopened
atomic child leaf whenever the parent series' `(closeout_status, integration_status, cleanup)` was
not `("not-started", "not-started", "pending")`; once `checkpointed` joined the integration
vocabulary the same predicate also sealed every master that took a checkpoint landing, so a master
could never admit another leaf after its first landing. The developer ruled the guard out rather than
narrowing it: a master is meant to be paused and resumed, never locked by its own landing. This
module's three call sites are gone and no replacement admission predicate was added.

What survives here:

- `leaf_admission_operation` (parameter at code line 220) still labels the master-series admission
  refusals with the operation the caller performed
  (`operation=leaf_admission_operation or "worktree_start"` at 244, 261 and 291). Only the seal call
  was removed, not the operation label.
- `_parent_series_contract` (code lines 742-799) still builds or recovers the leaf's parent series
  through `ensure_master_series_contract`, but now returns it directly. The former
  `isinstance(series, WorktreeCommandResult)` short-circuit and the follow-up seal check are gone, so
  a `WorktreeCommandResult` the parent builder returns is no longer filtered here.
- Leaf admission still requires the parent's contract-keyed activation to have reconciled and become
  `active`. That is activation authority, not a lifecycle-cell seal, and it is unchanged.

`mcp/tests/test_lifecycle_playthrough_end_to_end.py` is the regression proof for the removal: it
plays the whole lifecycle in order on one real temporary Git world — master open, leaf commanded and
started, leaf closed out, leaf landed through the public `worktree_integrate`, unfinished master
checkpointed through the public `worktree_checkpoint_landing`, master paused, master resumed through
the ordinary attach route — and then starts a leaf commanded *after* that landing.

`dry_run` remains planning-only: it returns an existing or planned contract without fetching,
publishing the selector, writing the bootstrap journal, creating branches, or starting a sync
generation. Organizational semantics still exist only under an authored execution graph; a
graph-less master uses atomic semantics. Terminal series artifacts are replaceable stale artifacts,
not evidence that another master owns a global lane.

CCR-R25 gives persisted master-edge failures a typed admission path. `_existing_master_series_contract`
now raises `MasterSeriesContractAdmissionError` with a stable status plus expected/observed task,
repository, memory, and branch edges for unreadable, wrong-kind, or mismatched contracts. Both the
dry-run preflight and the locked apply preflight convert that error through the shared atomic-series
admission projection. Before protected-branch surface calculation, `_build_start_contract` performs
the same read-only edge check so a persisted mismatch cannot escape as an unstructured
`RuntimeError`; the response advertises the exact `worktree_status` address and leaves repair to
the existing recovery authority.

CQ04 closes the reread gap after upstream refresh: `ensure_master_series_contract` catches only the
known `MasterSeriesContractAdmissionError` from its authoritative second contract read and routes
that typed edge or parser refusal through the existing admission projection. `_build_start_contract`
performs the same read-only preflight before protected-branch calculation, preserving the concrete
observed evidence and contract-bound status action without rewriting the persisted contract.

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
- Multiple commanded masters may have live series contracts, including two that share one sprint's
  code and memory source branches. Each is selected in its own contract-keyed activation record;
  selecting one never rewrites, pauses, or names another's record, and a foreign master's state is
  never this contract's reason to wait.
- Actual leaf materialization/implementation under an atomic master requires its parent selection to reconcile active; a read-only preview may carry the existing owner's validated plan without claiming activation. Neither task prose nor queue state supplies durable implementation authority.
- **No serial-lifecycle cell refuses a leaf.** Closeout, integration and cleanup cells do not gate
  leaf admission. The `atomic_series_seal.py` predicate that read them as a seal is deleted, so a
  master that took a checkpoint landing (`integration_status="checkpointed"`) still admits the next
  leaf; `mcp/tests/test_lifecycle_playthrough_end_to_end.py` proves it end to end. Do not reintroduce
  a lifecycle-cell admission predicate here or in the parent-series helpers.
- Apply-time bootstrap preflight and bootstrap publication use the same per-master store lock; the
  unlocked planning-only dry run never writes lock or lifecycle state.
- Integration authority and the per-master bootstrap store lock do not nest with another store lock.
- Master-edge admission reports observed evidence without rewriting the persisted contract or
  bypassing contract-keyed activation.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Master bootstrap separates durable contract creation from that contract's own disposable activation selection: it publishes that contract's own activation as reconciling without touching another master's record, then syncs the pinned source pair and reconciles it active before returning implementation authority. [1]
- The admission error type gives persisted master-edge mismatches a typed, contract-bound payload before branch-protection projection. [2]
- The start preflight projects a persisted master-edge refusal before protected-surface calculation. [3]
- The start builder performs the pre-protected-surface admission check and returns its refusal result. [4]
- The parent-series builder that no longer short-circuits on a command result and no longer re-checks a child-admission seal: it returns the series `ensure_master_series_contract` produced. [5]
- The leaf-admission operation label that survives the seal removal and still names the caller's operation inside the master-series admission refusals. [6]
- The end-to-end playthrough that proves a leaf commanded after a checkpoint landing still starts. [7]
- Selection fetches evidence outside integration authority, re-reads the exact contract under authority, and delegates reconciliation; the focused transaction keeps the selected series reconciling until the exact current source pair is proven before active exposure. [8]
- Shared leaf-ref validation and candidate reporting. [9]
- Start-side conversion from leaf-ref resolution errors and contract-construction errors into command results. [10]
- The start operation returns through `start_result`. [11]
- start_result consumes StartContractPlan before existing-contract handling, preflight and enclosure planning, forwarding its preview parent only through the explicit dry-run request. [12]
- The start operation creates its enclosure through `_create_start_enclosure`. [13]
- `_task_vocabulary` and `validate_contract` are distinct sources of `ContractError`. [14]

### Cross-Repo References

No meaningful cross-repository reference applies beyond the configured external-memory pair that
the contract records explicitly.

## 260815-DAG-L4 Integration-Authority Impact

Task-derived integration refs remain mechanically non-ordinary: repository defaults, sprint supers,
and atomic-series refs are censused across code and external memory. Leaf publication still uses the
exact configured locator and task CAS, while contract-keyed activation
selection/reconciliation uses repository integration authority. No mutable queue lane participates in
start admission.

## 260821-CLIVE-L2 Current Contract

The current source seams include `memory_base_for_source`, `memory_mode_for_repository`, `MasterSeriesContractSpec`. New enclosures publish the strict root manifest, canonical journal directory, and locked address-only locator before exposure or operation admission. Pre-existing readable enclosures require the explicit adoption route; start never infers or falls back.

### Reconciled Source Evidence

- The current module exposes the source-branch memory base helper at this ownership boundary. [15]
- The startup admission module owns memory-mode selection for a code/memory pair. [16]
- The current module defines the strict master-series contract specification. [17]

## 260831-LOCR-L36 Contract-Keyed Activation (Source Wording Now Corrected)

The runtime is keyed per series contract: `ensure_master_series_contract` selects the requested
master in that contract's own activation record, and no other master is paused, adopted, or named as
a waiting reason. The module's own frozen source now says so, so this card no longer carries a
source-side debt note.

- `ensure_master_series_contract`'s docstring (code lines 229-233) reads: "Contract presence proves
  durable work exists; it does not own scheduling. Once this operation has recovered or created the
  requested contract, it publishes that contract's own activation as reconciling (no other master's
  record is touched), syncs its pinned source pair, and publishes it active before returning
  implementation authority." The retired "selects that master for the exact protected source pair,
  marks it reconciling (logically pausing the previous selection)" phrasing no longer occurs.
- The lock-order comment guarding the second mutex (code lines 276-277) now names "the per-contract
  activation store" instead of the former source-pair store.

Read the docstring for the mechanism it describes; it is now the same per-contract rule this card
documents.
