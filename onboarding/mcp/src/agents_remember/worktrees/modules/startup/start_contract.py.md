# mcp/src/agents_remember/worktrees/modules/startup/start_contract.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/worktrees/modules/startup/start_contract.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-09-14T17:20+02:00|
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

`start_contract.py` owns worktree-start contract construction after the HFX-L4 extraction from
`start.py`. It builds or recovers root series contracts, selects and reconciles an atomic master in
that contract's own activation record before leaf admission, derives leaf source/work branches and
memory bases, validates the requested leaf ref, and returns a leaf contract whose persisted `leaf_id`
is the canonical task document id.

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
- A leaf under an atomic master is not admitted until its parent selection has reconciled and become
  active; neither task prose nor closeout queue state supplies that authority.
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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Master bootstrap separates durable contract creation from that contract's own disposable activation selection: it publishes that contract's own activation as reconciling without touching another master's record, then syncs the pinned source pair and reconciles it active before returning implementation authority. | `ensure_master_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:215-303 |
| The admission error type gives persisted master-edge mismatches a typed, contract-bound payload before branch-protection projection. | `MasterSeriesContractAdmissionError` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:68-78 |
| The start preflight projects a persisted master-edge refusal before protected-surface calculation. | `_existing_master_series_admission_refusal` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:931-973 |
| The start builder performs the pre-protected-surface admission check and returns its refusal result. | `_build_start_contract` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:976-1051 |
| The parent-series builder that no longer short-circuits on a command result and no longer re-checks a child-admission seal: it returns the series `ensure_master_series_contract` produced. | `_parent_series_contract`; `_parent_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:742-799 |
| The leaf-admission operation label that survives the seal removal and still names the caller's operation inside the master-series admission refusals. | `leaf_admission_operation`; "operation=leaf_admission_operation or \"worktree_start\"" | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:220-220; mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:244-244 |
| The end-to-end playthrough that proves a leaf commanded after a checkpoint landing still starts. | `LifecyclePlaythroughTests` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173 |
| Selection fetches evidence outside integration authority, re-reads the exact contract under authority, and delegates reconciliation; the focused transaction keeps the selected series reconciling until the exact current source pair is proven before active exposure. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority`; `sync_selected_atomic_series_under_authority`; `_sync_selected_atomic_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:103-121; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:134-161; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:164-226 |
| Shared leaf-ref validation and candidate reporting. | `LeafRefResolutionError`; `resolve_leaf_ref` | mcp/src/agents_remember/worktrees/leaf_refs.py:39-66; mcp/src/agents_remember/worktrees/leaf_refs.py:88-141 |
| Start-side conversion from leaf-ref resolution errors and contract-construction errors into command results. | `invalid_leaf_ref_result`; `invalid_contract_request_result` | mcp/src/agents_remember/worktrees/modules/startup/leaf_ref_start.py:26-35; mcp/src/agents_remember/worktrees/modules/startup/leaf_ref_start.py:38-53 |
| The start operation returns through `start_result`. | `start_result` | mcp/src/agents_remember/worktrees/modules/start.py:518-532 |
| `start_result` calls `build_start_contract` before existing-contract handling, preflight, and enclosure creation. | "contract = build_start_contract(context"; "existing_result = _existing_contract_result(context"; "preflighted = _preflighted_contract(context"; "return _create_start_enclosure(context" | mcp/src/agents_remember/worktrees/modules/start.py:523-523; mcp/src/agents_remember/worktrees/modules/start.py:526-526; mcp/src/agents_remember/worktrees/modules/start.py:529-529; mcp/src/agents_remember/worktrees/modules/start.py:532-532 |
| The start operation creates its enclosure through `_create_start_enclosure`. | `_create_start_enclosure`; "return _create_start_enclosure(context" | mcp/src/agents_remember/worktrees/modules/start.py:687-719; mcp/src/agents_remember/worktrees/modules/start.py:532-532 |
| `_task_vocabulary` and `validate_contract` are distinct sources of `ContractError`. | `_task_vocabulary`; `validate_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:159-176; mcp/src/agents_remember/worktrees/worktree_contract.py:766-821 |

## Cross-Repo References

No meaningful cross-repository reference applies beyond the configured external-memory pair that
the contract records explicitly.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260815-DAG-L4 Integration-Authority Impact

Task-derived integration refs remain mechanically non-ordinary: repository defaults, sprint supers,
and atomic-series refs are censused across code and external memory. Leaf publication still uses the
exact configured locator and task CAS, while contract-keyed activation
selection/reconciliation uses repository integration authority. No mutable queue lane participates in
start admission.

## 260821-CLIVE-L2 Current Contract

The current source seams include `memory_base_for_source`, `memory_mode_for_repository`, `MasterSeriesContractSpec`. New enclosures publish the strict root manifest, canonical journal directory, and locked address-only locator before exposure or operation admission. Pre-existing readable enclosures require the explicit adoption route; start never infers or falls back.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes the source-branch memory base helper at this ownership boundary. | `memory_base_for_source` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:131-140 |
| The startup admission module owns memory-mode selection for a code/memory pair. | `memory_mode_for_repository` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:81-88 |
| The current module defines the strict master-series contract specification. | `MasterSeriesContractSpec` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:200-212 |

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

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_existing_master_series_admission_refusal` repointed to mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:931-973. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_build_start_contract` repointed to mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:976-1051. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `start_result` repointed to mcp/src/agents_remember/worktrees/modules/start.py:518-532. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `_task_vocabulary`; `validate_contract` repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:159-176; mcp/src/agents_remember/worktrees/worktree_contract.py:766-821. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `validate_contract` in the row 220 of this card from mcp/src/agents_remember/worktrees/worktree_contract.py:766-767 to mcp/src/agents_remember/worktrees/worktree_contract.py:129, the extent of the construct the claim is about (the checker named line(s) [129, 471, 479] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `validate_contract` in the row 220 of this card from mcp/src/agents_remember/worktrees/worktree_contract.py:159-160 to mcp/src/agents_remember/worktrees/worktree_contract.py:766-767, the extent of the construct the claim is about (the checker named line(s) [129, 471, 479] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_task_vocabulary` in the row 220 of this card from mcp/src/agents_remember/worktrees/worktree_contract.py:766-767 to mcp/src/agents_remember/worktrees/worktree_contract.py:159-160, the extent of the construct the claim is about (the checker named line(s) [159, 346, 399] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/worktrees/worktree_contract.py:159-160 in the row 220 of this card; the repetition added no pooled evidence
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (residue citation pass): re-derived the source
  range of 3 claim(s) whose anchor no longer sat in its cited range and normalised 0 further
  range(s) from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`). No claim wording was changed to fit an anchor; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): `_require_bootstrap_ref` now hands the runner one `GitRunnerOptions(input_text=...)`
  object for `git update-ref --stdin` instead of an `input_text=` keyword, and the module's import
  block gained one line. No content impact: this card stated no `run_git` call form, so the contract
  construction and refusal-conversion behavior documented above is unchanged. The three-line growth
  moved citations that were also already behind the source, so each was re-derived against the current
  file: `ensure_master_series_contract` 215-307 → 215-303 (its
  `reconcile_selected_series_under_authority(...)` return now closes at 303, not 307),
  `_existing_master_series_admission_refusal` 940-984 → 935-979, `_build_start_contract`
  987-1062 → 982-1057, `_parent_series_contract` 739-796 → 742-799 and its prose reference,
  `leaf_admission_operation` 219-219/243-243 → 220-220/244-244 and the operation-label usages
  (243, 260, 290 → 244, 261, 291), the docstring range 227-232 → 229-233, the lock-order comment
  279 → 276-277, and the playthrough citation 62-169 → 62-173. The `memory_base_for_source`
  (131-140) and `MasterSeriesContractSpec` (200-212) rows still match the current file; verification
  metadata remains closeout-owned.
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): recorded that
  `worktrees/atomic_series_seal.py::require_series_accepting_leaves` is deleted and that this module's
  three call sites — the dry-run arm, the locked apply arm of `ensure_master_series_contract`, and
  `_parent_series_contract` — are gone, together with the `isinstance(series, WorktreeCommandResult)`
  short-circuit that preceded the third. Recorded why: the predicate read closeout/integration/cleanup
  cells as a seal, so once `checkpointed` existed it also refused every master that took a checkpoint
  landing, and a master is meant to be paused and resumed rather than locked by its own landing. Kept
  `leaf_admission_operation` in the card because it survives as the refusal label (code line 219, used
  at 243, 260 and 290), re-cited `_parent_series_contract` at 739-796, and added the invariant that no
  serial-lifecycle cell refuses a leaf plus the playthrough module as the proof. Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T15:03:18+02:00 — Removed the round-1 source-side wording-debt section: the frozen `start_contract.py` was corrected this round, so the card now records the corrected source instead of flagging it. Verified in the code worktree that `ensure_master_series_contract`'s docstring reads "it publishes that contract's own activation as reconciling (no other master's record is touched), syncs its pinned source pair, and publishes it active before returning implementation authority" (lines 227-232) and that the lock-order comment now names "the per-contract activation store" (line 279); the retired "exact protected source pair ... logically pausing the previous selection" and "source-pair activation store" phrasings no longer occur in the module. Re-worded the `ensure_master_series_contract` reference claim to that contract's-own-activation behavior and re-cited its exact range 215-307 (declaration at 215, `reconcile_selected_series_under_authority(...)` return at 304-307). Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T15:03:18+02:00 — Curator verification of the mechanically repointed `ensure_master_series_contract` claim, clearing its reopened-citation finding; this entry takes the place of the auto-generated mechanical repair line for that claim, and the provenance it carried is preserved in prose here. Mechanical provenance retained in prose: the ccr-r10@v1 anchor-range projection bound the claim to mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:215-307 against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830 with claim bytes unchanged at that time. I re-read the construct at that exact range — `def ensure_master_series_contract(` at 215 through its `reconcile_selected_series_under_authority(...)` return at 304-307 — and its docstring and body support the claim's own words: durable contract creation is separate from that contract's own disposable activation selection, which is published as `reconciling` for that contract alone ("no other master's record is touched"), refreshed and committed after repository integration authority, and returned only through reconciliation. The claim is curator-verified as current, not merely mechanically repointed.
- 2026-09-13T14:21:11+02:00 — 260831-LOCR-L36: corrected this card to the contract-keyed activation runtime. Purpose, the "Source-pair activation replaces the old global sequential lane" heading, the `reconcile_selected_series_under_authority` paragraph, the protected-source-pair invariant, the DAG-L4 sentence, and the `ensure_master_series_contract` reference row no longer describe one selection per protected source pair or a logically paused previous selection; they now state that each series contract owns its record, that a foreign master's record can never be adopted (`atomic-series-activation-contract-mismatch`), and that the only surviving activation waiting reason is `atomic-series-reconciling`. Added a section recording the source-side wording debt this re-keying left in the FROZEN file: `ensure_master_series_contract`'s docstring still says "the exact protected source pair ... logically pausing the previous selection" (lines 231-232) and the lock comment still says "the source-pair activation store" (line 279). The code file was not edited by this pass and no reference row was changed for it. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_existing_master_series_admission_refusal` repointed to mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:940-984. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_build_start_contract` repointed to mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:987-1062. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `start_result` repointed to mcp/src/agents_remember/worktrees/modules/start.py:544-555. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `memory_base_for_source` repointed to mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:131-140. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-08T19:29:21+02:00 — Repaired the inherited claim-reopen citation by rereading the current activation transaction: fetch/re-read authority, reconciling transition, exact sync, source-pair completeness, and active publication now point to their current behavioral ranges. Verification pins remain unchanged; no acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ04 preparation reconciled the authoritative second master-contract read, typed parser/edge refusal, and pre-protected-surface admission seam. Source remains uncommitted; verification remains closeout-owned with no acceptance claim.
- 2026-09-08T17:47:39+02:00 — CCR-L38 source-grounded preparation split the moved admission symbols and rebound the master-series builder, memory helpers, and contract specification to their current owners and ranges. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T16:24:06+02:00 — CCR-L38 preparation range refresh: regenerated start-result and contract-admission seam coordinates after the frozen additions. This is a mechanical source-range correction; verification metadata remains closeout-owned.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded typed master-edge admission evidence and the pre-protected-surface refusal seam. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

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
