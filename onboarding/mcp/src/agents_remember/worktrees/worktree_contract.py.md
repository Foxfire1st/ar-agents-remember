# mcp/src/agents_remember/worktrees/worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`worktree_contract.py` reads, writes, validates, and renders the `c-09-git-worktree-manager` skill
`series-contract.md` files. A root series contract records a master task's integration branch; a leaf
enclosure contract records one concrete worktree under `enclosures/<leaf-id>/series-contract.md`, with
new writes persisting the canonical task document id as `coordination.leaf_id` when the task tree can
prove the leaf mapping. Since 260712-PTS-L1 the module also owns `heal_contract_leaf_ids`, the explicit
one-shot migration that rewrites legacy stem-shaped leaf ids to doc ids on disk — reads themselves never
normalize.

## Code Commentary

### Logic

The module defines the single `ar-series-contract/v1` schema, supported memory modes, valid contract
`kind`s (`series` or `leaf`), the `WorktreeContract` dataclass, deterministic worktree folder helpers,
root/leaf default constructors, markdown front-matter serialization, validation, limited YAML-like parsing,
and conversion from parsed front matter back into a typed contract object. Contract rendering is split into
small section renderers for memory, sync, human review, closeout, integration, and body content. Task-folder
lookup is delegated to `worktrees/task_resolver.py`; leaf-id normalization is delegated to
`worktrees/leaf_refs.py`; this module no longer owns active-task lookup or leaf-ref policy.

**The constructor parameter objects (260731-EFA-L2).** `default_contract` and
`default_series_contract` are now signed on three frozen dataclasses this module also owns and
exports:

- **`RepoBranchPlan(repo_path, source_branch="", work_branch="", base_commit="")`** — one
  repository's branch plan for a worktree pair. The contract's `code:` and `memory:` sections carry
  exactly these four facts and `start_contract` derives them per side as a unit. **On the series
  contract the pair used to read `protected_branch`/`integration_branch`** — those were only other
  names for the same fork point and landing branch, so `default_series_contract` now takes
  `code=RepoBranchPlan(source_branch=<protected>, work_branch=<integration>, …)` and still writes
  them to `code_source_branch`/`code_work_branch` as before.
- **`ContractTask(name, repo_name, coordination_root, workflow_kind, memory_mode,
  parent_task_name="", parent_contract_path=None)`** — the task a contract speaks for: its name,
  the repository it changes, the coordination tree that holds it, how it is run, and the contract
  one level up (a leaf's series, a series' enclosing task).
- **`LeafIdentity(worktree_name, leaf_id=None, lifecycle_id="")`** — which leaf a leaf-enclosure
  contract is for. `leaf_id=None` still means "derive from the worktree name": the *reference* used
  for the enclosure path is `leaf_id or worktree_name`, while the *persisted* `leaf_id` is
  `leaf_id or slugify(worktree_name)` — the same two-value rule as before.

Current signatures: `default_contract(task, *, leaf, code, memory=None)` and
`default_series_contract(task, *, code, memory=None, task_root=None)`. **`memory=None` is the whole
absent-memory state**: without a repo path there is no memory branch, no memory base and no
ledger, so the constructors expand `None` to `memory_repo_path=None` and empty branch/commit
strings rather than accepting a half-populated memory plan. `start_contract._memory_plan` is the
helper that builds it or returns `None`. Every emitted `WorktreeContract` field is unchanged.

Since 260712-PTS-L1, `load_contract` is read + parse + validate ONLY: one file read, zero tasks-tree
traversal — no leaf-ref resolution, no series-contract iteration, no glob. A legacy stem-shaped
`coordination.leaf_id` is returned verbatim. Normalization is a write-time concern: `write_contract`
paths still run `normalize_contract_leaf_id()`, which asks the shared leaf-ref resolver to map legacy
stem-shaped ids to canonical task doc ids when the task tree can prove a unique match, and write paths
still surface non-leaf-ref task-resolution failures. `default_contract` accepts a caller-supplied doc id
without slugifying it, while still slugifying the worktree name only when no explicit leaf id is
available. (Motivation: a 2026-07-12 py-spy daemon sample put the hidden per-read resolution walk at
~9.7s of a 15s sample; the master 260712-PTS decision is that normalization is
write-time/migration-only.)

`heal_contract_leaf_ids(coordination_root, *, dry_run=False)` is the explicit, one-shot successor to the
per-read normalization `load_contract` used to run. It walks `tasks/` once via
`iter_leaf_enclosure_contracts` — the exact population the projection readers consume — maps each legacy
`leaf_id` through `normalize_contract_leaf_id(..., keep_unresolved=True)` (the same mapping the read path
used to apply), and rewrites only the contracts whose id actually changes. It is idempotent and cheap on
re-run: a contract whose `leaf_id` already is a doc id of the task root its enclosure PHYSICALLY lives in
(derived from the `enclosures/<leaf>/series-contract.md` path, never the recorded root, so a stale
recorded root degrades to the slow path instead of a wrong skip) is skipped through a per-root
`leaf_refs.canonical_leaf_doc_ids` index without any resolution walk. It is loud by report: every rewrite
logs one line and lands in the returned report (`healed` / `canonical` / `unchanged` / `errors` /
`dryRun`), and an unresolvable or malformed entry is reported, never fatal to the sweep. Nothing invokes
it implicitly from a read path — reach it through the `heal-leaf-ids` CLI subcommand
(`worktrees/modules/cli.py`) or a direct call (e.g. once at daemon startup).

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
- Contract reads cost O(one file): `load_contract` must never traverse the tasks tree. Consumers of
  loaded contracts must therefore tolerate RAW legacy stem-shaped `leaf_id` values until
  `heal_contract_leaf_ids` (or any `write_contract` rewrite, e.g. closeout/sync bookkeeping) heals the
  file on disk — do not assume a doc-id-shaped `leaf_id` on an unhealed tree.
- The heal rewrite regenerates the whole contract file from the parsed model: unknown front-matter keys
  and hand-added prose do not survive it. This is pre-existing `write_contract` semantics (same as
  closeout rewrites), not a heal-specific behavior.
- `heal_contract_leaf_ids` is idempotent, dry-runnable, and never fatal on a malformed entry; it is only
  ever invoked explicitly (CLI `heal-leaf-ids` or a direct call), never as a read side effect.
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
| Contract WRITE paths normalize legacy leaf ids to canonical doc ids when the leaf-ref resolver can prove the mapping; `load_contract` performs no normalization at all. | load_contract, normalize_contract_leaf_id | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| `heal_contract_leaf_ids` sweeps the active leaf-enclosure population once, cheap-skips canonical ids via a per-root doc-id index, rewrites only changed contracts, and reports every rewrite and error. | heal_contract_leaf_ids | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Dedicated leaf-ref resolver supplies canonical doc ids, legacy alias policy, and the heal's bounded per-task-root doc-id index (`canonical_leaf_doc_ids`). | n/a | [leaf_refs.py](agents-remember/mcp/src/agents_remember/worktrees/leaf_refs.py) |
| The `heal-leaf-ids` CLI subcommand (`--coordination-root`, `--dry-run`) is the deliberate invocation seam for the heal. | command_heal_leaf_ids | [modules/cli.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cli.py) |
| Walk-free load tripwires, heal parity with the removed read-time normalization, idempotence, dry-run, error tolerance, and the CLI seam are pinned by the resolver test suite. | n/a | [test_leaf_ref_resolution.py](agents-remember/mcp/tests/test_leaf_ref_resolution.py) |
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

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `RepoBranchPlan`, `ContractTask` and `LeafIdentity`, and re-signed both
  constructors — `default_contract(task, *, leaf, code, memory=None)` and
  `default_series_contract(task, *, code, memory=None, task_root=None)`. The series contract's
  `protected_branch`/`integration_branch` keywords became the code plan's
  `source_branch`/`work_branch` (the same two facts under their general names), and `memory=None`
  now expresses the whole absent-memory state. Every emitted `WorktreeContract` field, including
  the `leaf_id or worktree_name` reference and the `leaf_id or slugify(worktree_name)` persisted
  id, is unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1: `load_contract` is now read+parse+validate ONLY — the
  per-read `normalize_contract_leaf_id` call and its hidden whole-tasks-tree resolution walk are gone
  (py-spy 2026-07-12 measured that walk at ~9.7s of a 15s daemon sample; master 260712-PTS decision:
  normalization is write-time/migration-only). Added `heal_contract_leaf_ids(coordination_root,
  dry_run)`, the explicit, idempotent, loud-by-report one-shot sweep that rewrites legacy stem-shaped
  leaf ids to doc ids across the active enclosure population, cheap-skipping canonical contracts via
  `leaf_refs.canonical_leaf_doc_ids`. Legacy ids now surface RAW from reads until the heal or a
  `write_contract` rewrite heals them; the heal rewrite regenerates the whole contract file (unknown
  front-matter keys / hand prose do not survive — pre-existing `write_contract` semantics). Adversarial
  review confirmed post-heal parity for doc-id changeset lookups, enclosure lifecycle joins, and reopen.
  Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
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
