# mcp/src/agents_remember/worktrees/modules/start_contract.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/worktrees/modules/start_contract.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-01T10:45+02:00                                       |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`                   |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

`start_contract.py` owns worktree-start contract construction after the HFX-L4 extraction from
`start.py`. It builds root series contracts for master tasks, derives source/work branches and memory
bases, validates the requested leaf ref, and returns a leaf contract whose persisted `leaf_id` is the
canonical task document id.

## Code Commentary

### Logic

`build_start_contract(context, args)` (L187-L206) is the public start-side entry. It wraps
`_build_start_contract` (L209-L261) and converts **two** failures into the same
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
  `write_contract(contract.contract_path, contract)` inside `_parent_series_contract` (the call is
  at L176; the helper is L112-L184). `write_contract` runs `validate_contract` before it writes, so
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
  the parent series contract inside it (L176), so a `validate_contract` refusal on the PARENT can
  surface under the same result state. Do not narrow the docstring or the card back to "both
  refusals are bad arguments"; when triaging an `invalid-request` from `worktree_start`, read the
  message — `validate_contract` names the offending cell and the file it belongs to, which is what
  distinguishes the two paths.
- Worktree-start contracts persist doc ids, not legacy file stems.
- Malformed task documents fail loudly during parent-series detection.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared leaf-ref validation and candidate reporting. | [../../leaf_refs.py](../../leaf_refs.py.md) |
| Start-side conversion from resolver errors into command results. | [leaf_ref_start.py](leaf_ref_start.py.md) — `invalid_contract_request_result` L38-L54 |
| The start operation calls `build_start_contract` before preflights and writes. | [start.py](start.py.md) |
| `_task_vocabulary` L150-L167 (the request-narrowing both constructors funnel through) and `write_contract` L461-L465, which runs `validate_contract` L750 before it writes — the second, non-caller source of the `ContractError` this module catches. | [../worktree_contract.py](../worktree_contract.py.md) |

## Update History

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): `build_start_contract`
  gained a docstring after the 09:17 entry below, and it corrects a claim this card had inherited.
  The docstring previously would have said (and the card implied) that **both** refusals are bad
  *arguments*. That is false for `ContractError`: the `except` wraps the whole call, so besides the
  intended vocabulary case it also catches a `ContractError` raised by the `write_contract` inside
  `_parent_series_contract` — verified in the source, the call is at L176 inside the helper at
  L112-L184, and `write_contract` (`worktree_contract.py` L461-L465) runs `validate_contract`
  (L750) before writing. That is a write-validation failure of the **parent series contract**, not
  anything the caller passed. Recorded the corrected scope in Code Commentary, split the two
  `except` clauses by kind rather than treating them as one class of failure, and added an invariant
  saying `invalid-request` does not imply a caller fault and naming what distinguishes the two paths
  when triaging (`validate_contract` names the offending cell and file). Pinned the two wrapper
  functions to their current ranges (`build_start_contract` L187-L206, `_build_start_contract`
  L209-L261) and gave the two reference rows real citations. Verification metadata pinned until
  closeout stamps the L4 commit.
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
