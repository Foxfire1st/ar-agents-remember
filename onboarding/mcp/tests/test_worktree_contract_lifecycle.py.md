# test_worktree_contract_lifecycle.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/tests/test_worktree_contract_lifecycle.py`         |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-06-13T18:45+02:00                                  |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`              |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Covers the slice-2c contract lifecycle anchor: `lifecycle_id` round-trips through
`contract_to_text` / `load_contract`, and a contract written before the field
existed (no `lifecycle:` section) loads with `lifecycle_id == ""`.

## Code Commentary

### Logic

`ContractLifecycleAnchorTests` build a `default_contract(..., lifecycle_id=...)`
over a `tempfile` coordination root and assert: the default id is `""`;
`contract_to_text` emits a `lifecycle:` / `id:` section; a `write_contract` →
`load_contract` round-trip preserves the id; and a contract with the `lifecycle:`
block stripped (mimicking a pre-2c contract) loads with `lifecycle_id == ""`
(backward compatibility).

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom). `memory_mode="disabled"` keeps
the fixture free of git/memory setup so the test is a pure contract round-trip.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The contract module under test — the `lifecycle_id` field, the `lifecycle:` renderer, and the `_section` parser. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-06-13T18:45+02:00: Created for slice 2c — contract lifecycle-anchor
  round-trip + backward-compatibility tests. Verification metadata is pinned until
  closeout stamps the 2c code commit.
