# test_resolver_parity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_resolver_parity.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:59+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_resolver_parity.py` protects the package resolver CLI output shape for
external, internal, and contract-backed contexts.

## Code Commentary

### Logic

The tests create temporary code, adjacent, coordination, and memory roots, write
minimal settings, and execute `agents_remember.kernel.coordination_context_resolver`
as a package module. Assertions check the complete context key set for external
memory, internal memory, and worktree contract resolution, including worktree
contract path and group fields.

### Invariants And Boundaries

The resolver must keep the `c-08-ar-coordination-context-resolver` skill JSON shape stable after moving out of the skill
tree. Tests should exercise the package route directly rather than loading a
deleted runtime skill script.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package resolver module provides the tested CLI. | `main` | mcp/src/agents_remember/kernel/coordination_context_resolver.py:1-11 |
| Worktree contracts supply the contract-backed fixture. | `default_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:345-395; mcp/src/agents_remember/worktrees/worktree_contract.py:398-404 |

## Series-Contract Notes

Resolver parity tests now pin task-name lookup over active roots, nested parent disambiguation, leaf-id selection, archive exclusion, and parity between source API and MCP wrapper arguments.

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 2 citation rows
  (`main` re-export at coordination_context_resolver.py 1-11; the contract fixture builders at
  worktree_contract.py 345-395 and 398-404). Zero findings remain.

- 2026-08-01T09:59+02:00 — 260731-EFA-L4 curator: No content impact: three fixture values moved
  onto the narrowed `WorkflowKind` (`Literal["chat-task", "light-task"]`,
  `worktrees/worktree_contract.py` L50) — `"light"` to `"light-task"` in
  `test_worktree_contract_resolution_reports_expected_context`, and `"master-series"` to
  `"light-task"` in the two `default_series_contract` fixtures inside
  `test_parent_task_disambiguates_nested_task_roots` and
  `test_active_series_discovery_excludes_archive`. Checked the one thing that could have made that
  consequential and it did not: series-ness is set by `default_series_contract` itself
  (`contract.kind == "series"`), not by the workflow kind, so the nested-parent case still raises
  `TaskResolutionError` on "multiple active tasks" and still disambiguates via `--parent-task`, and
  the archive case still excludes `0_archive/`. Re-read every claim in the card against the current
  396-line file: 5 tests in `ResolverCliTests`, the external / internal / contract-backed context
  key sets asserted through `assert_context_shape`, `--contract-path` reporting
  `contract_path`/`worktree_group`/`code_worktree`, and `--leaf-id` selection at L149-L153. Both
  reference paths resolve. The card names no workflow kind.

- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 rewrote only the contract-fixture call
  sites. `default_contract` and `default_series_contract` now take the `ContractTask`,
  `LeafIdentity` and `RepoBranchPlan` parameter objects instead of a dozen loose keywords
  (`protected_branch`/`integration_branch` are now `RepoBranchPlan.source_branch`/`work_branch`),
  and one stray closing paren was re-indented. No test was added, removed or renamed and no
  assertion changed; this card claims the resolver CLI's context key set plus the task-name,
  nested-parent, leaf-id, archive-exclusion and API/wrapper-parity coverage, and names none of the
  keywords that moved.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: resolver parity coverage now includes active task-name lookup, nested parent disambiguation, leaf enclosure resolution, archive exclusion, and source API/MCP wrapper parity for the new resolver arguments. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after resolver parity tests stopped comparing against the deleted old script.
