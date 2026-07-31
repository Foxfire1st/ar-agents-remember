# mcp/src/agents_remember/worktrees/modules/start_contract.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/worktrees/modules/start_contract.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-31T00:00+02:00                                       |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                   |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

`build_start_contract(context, args)` is the public start-side entry. It wraps `_build_start_contract`
and converts `LeafRefResolutionError` into the same `WorktreeCommandResult` refusal shape that
`start_result` can return before any worktree or contract write. `_build_start_contract` asserts the
required start arguments, resolves `args.leaf_id or args.worktree_name` through `leaf_ref_start`, then
passes the resulting doc id into `default_contract`.

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
- Worktree-start contracts persist doc ids, not legacy file stems.
- Malformed task documents fail loudly during parent-series detection.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared leaf-ref validation and candidate reporting. | [../../leaf_refs.py](../../leaf_refs.py.md) |
| Start-side conversion from resolver errors into command results. | [leaf_ref_start.py](leaf_ref_start.py.md) |
| The start operation calls `build_start_contract` before preflights and writes. | [start.py](start.py.md) |

## Update History

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
