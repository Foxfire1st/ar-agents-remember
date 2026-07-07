# mcp/src/agents_remember/worktrees/worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T23:45+02:00                     |
| lastVerifiedCommitHash | `52911a15091de8d065afc6cbc0f8d6ac34690039` |
| lastVerifiedCommitDate | 2026-07-07T22:29:35+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`worktree_contract.py` reads, writes, validates, and renders the `c-09-git-worktree-manager` skill
`series-contract.md` files. A root series contract records a master task's integration branch; a leaf
enclosure contract records one concrete worktree under `enclosures/<leaf-id>/series-contract.md`, with
new writes persisting the canonical task document id as `coordination.leaf_id` when the task tree can
prove the leaf mapping.

## Code Commentary

### Logic

The module defines the single `ar-series-contract/v1` schema, supported memory modes, valid contract
`kind`s (`series` or `leaf`), the `WorktreeContract` dataclass, deterministic worktree folder helpers,
root/leaf default constructors, markdown front-matter serialization, validation, limited YAML-like parsing,
and conversion from parsed front matter back into a typed contract object. Contract rendering is split into
small section renderers for memory, sync, human review, closeout, integration, and body content. Task-folder
lookup is delegated to `worktrees/task_resolver.py`; leaf-id normalization is delegated to
`worktrees/leaf_refs.py`; this module no longer owns active-task lookup or leaf-ref policy.

Leaf contract reads and writes run through `normalize_contract_leaf_id()`. That helper asks the shared
leaf-ref resolver to map legacy stem-shaped `coordination.leaf_id` values to canonical task doc ids when
the task tree can prove a unique match. On `load_contract`, unproven task-root resolution failures keep the
contract unchanged instead of crashing a read path; write paths still surface non-leaf-ref task-resolution
failures. `default_contract` therefore accepts a caller-supplied doc id without slugifying it, while still
slugifying the worktree name only when no explicit leaf id is available.

`lifecycle_id` (slice 2c) remains the observable-lifecycle enclosure anchor for leaf contracts, rendered as
a `lifecycle:` front-matter section and parsed back through `_section(data, "lifecycle")`. Root series
contracts represent integration branches and do not require a lifecycle id.

`sync_log` (issue #54 sub-task D) records each `worktree_sync` base-pair
advance as a tuple of dict entries. It is a real dataclass field because the
closeout/contract rewrite regenerates the document from the model — freeform
contract prose does not survive. It serializes as one compact JSON scalar
(`sync:` / `  log: [...]`) so the limited front-matter parser (scalar one-level
sections only) round-trips it; an absent or unparseable value loads as `()`,
keeping pre-#54 contracts loadable.

### Conventions

The contract parser intentionally supports only the subset written by the
workflow: scalar top-level fields and one-level nested sections. This keeps
contract files human-readable without introducing a general YAML dependency.

### Invariants And Boundaries

- External-memory leaf contracts must include memory repo, memory worktree, and
  ledger paths; root series contracts can point at the memory repo ledger without a leaf memory worktree.
- Contract serialization must preserve closeout and integration state.
- Worktree contracts persist leaf document ids going forward; legacy stem-shaped ids remain readable when
  resolver evidence is missing, ambiguous, or the read path cannot prove the active task root.
- Leaf worktree folders use slugified names with legacy `-ar` support only where the resolver needs to find
  existing work; task-root lookup lives in `worktrees/task_resolver.py`.
- `ContractError` subclasses the shared `AgentsRememberError` (imported from
  `agents_remember.errors`); since that base itself derives from `ValueError`,
  existing `except ValueError` callers still catch contract failures while the
  error now also participates in the domain error hierarchy.

## Docs References

No external documentation is needed for this local contract format.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the local worktree contract parser. | n/a | n/a |

## Repo-Internal References

Same-repository source defines the contract format and `c-09-git-worktree-manager` skill uses it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines the contract schema, valid memory modes, the `ContractError` type (now subclassing `AgentsRememberError` from `agents_remember.errors`), and the full `WorktreeContract` state record. | L16-L60 | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Folder naming and default contract helpers derive task roots, worktree groups, and external-memory ledger paths. | L61-L151 | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Contract load/write paths normalize legacy leaf ids to canonical doc ids when the leaf-ref resolver can prove the mapping. | normalize_contract_leaf_id | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Dedicated leaf-ref resolver supplies canonical doc ids and legacy alias policy. | n/a | [leaf_refs.py](agents-remember/mcp/src/agents_remember/worktrees/leaf_refs.py) |
| Load/write/render helpers parse front matter, validate contracts, and render closeout/integration state back to markdown. | L154-L289 | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Validation and limited YAML parsing enforce required fields and external-memory path requirements. | L292-L387 | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The worktree lifecycle modules import contract helpers and record closeout/integration commit state through these contract objects. | n/a | [modules/overview.md](agents-remember/mcp/src/agents_remember/worktrees/modules/overview.md) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here; the contract points at
external memory paths, but the parser and renderer are same-repository code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: `load_contract` now asks
  `normalize_contract_leaf_id(..., keep_unresolved=True)`, so base task-resolution failures during legacy
  id mapping leave the read contract unchanged while write/start paths remain loud for non-leaf-ref
  resolution failures. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: contract load/write now normalizes proven legacy
  stem-shaped leaf ids to canonical task doc ids while leaving unresolved legacy contracts readable;
  `default_contract` preserves explicit doc ids for future writes. Verification metadata pinned until
  closeout stamps the 260707-HFX-L4 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `worktree_contract.py` now owns the single `ar-series-contract/v1` schema with `kind` (`series` or `leaf`), root `series-contract.md` integration contracts, leaf `enclosures/<leaf-id>/series-contract.md` contracts, parent linkage fields, and parser compatibility only for path key names inside that schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: added the additive `lifecycle_id` field (the observable-lifecycle enclosure anchor, design §1.1) on the unchanged `v1` schema — rendered as a `lifecycle:` front-matter section, parsed back via `_section`, defaulting to "" for pre-2c contracts. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T09:56+02:00 — Added the `sync_log` field + `sync:` section (compact JSON scalar, backward-compatible empty default) for issue #54 sub-task D worktree_sync bookkeeping.
- 2026-05-31T12:50+02:00 — `ContractError` re-based from `ValueError` to the shared `AgentsRememberError` (imported from `agents_remember.errors`); corrected the error-type prose in Invariants And Boundaries and Repo-Internal References to name the new domain base while noting `except ValueError` callers still catch it (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Updated after contract rendering was split into section helpers during worktree package refactoring.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
