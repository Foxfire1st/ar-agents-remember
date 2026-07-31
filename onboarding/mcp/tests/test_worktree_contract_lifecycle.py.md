# test_worktree_contract_lifecycle.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/tests/test_worktree_contract_lifecycle.py`         |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-06-13T18:45+02:00                                  |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`              |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Covers the slice-2c contract lifecycle anchor: `lifecycle_id` round-trips through
`contract_to_text` / `load_contract`, and a contract written before the field
existed (no `lifecycle:` section) loads with `lifecycle_id == ""`.

## Code Commentary

### Logic

`ContractLifecycleAnchorTests` build a contract through
`default_contract(ContractTask(...), leaf=LeafIdentity(worktree_name=..., lifecycle_id=...),
code=RepoBranchPlan(...))` over a `tempfile` coordination root and assert: the default id is
`""`; `contract_to_text` emits a `lifecycle:` / `id:` section; a `write_contract` →
`load_contract` round-trip preserves the id; and a contract with the `lifecycle:`
block stripped (mimicking a pre-2c contract) loads with `lifecycle_id == ""`
(backward compatibility). The anchor the suite drives is therefore
`LeafIdentity.lifecycle_id`, not a loose `default_contract` keyword.

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom). `ContractTask(memory_mode="disabled")`
keeps the fixture free of git/memory setup so the test is a pure contract round-trip; the
module-level `_contract(root, lifecycle_id)` helper is the single place the parameter objects
are assembled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The contract module under test — the `lifecycle_id` field, the `lifecycle:` renderer, and the `_section` parser. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep. `default_contract`
  no longer takes a flat keyword list: the `_contract(...)` fixture now assembles
  `ContractTask(name/repo_name/coordination_root/workflow_kind/memory_mode)`,
  `leaf=LeafIdentity(worktree_name, lifecycle_id)`, and
  `code=RepoBranchPlan(repo_path, source_branch, work_branch, base_commit)`. Rewrote the Logic
  and Conventions paragraphs so they name the parameter objects and place the lifecycle anchor on
  `LeafIdentity.lifecycle_id` instead of describing a `default_contract(..., lifecycle_id=...)`
  keyword that no longer exists. The four assertions and the backward-compatibility case are
  unchanged.
- 2026-06-13T18:45+02:00: Created for slice 2c — contract lifecycle-anchor
  round-trip + backward-compatibility tests. Verification metadata is pinned until
  closeout stamps the 2c code commit.
