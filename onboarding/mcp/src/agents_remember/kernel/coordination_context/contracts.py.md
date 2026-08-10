# mcp/src/agents_remember/kernel/coordination_context/contracts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/contracts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`contracts.py` loads optional `c-09-git-worktree-manager` skill worktree contract facts for the `c-08-ar-coordination-context-resolver` skill
coordination context.

## Code Commentary

### Logic

`resolve_contract(selector, coordination_root, code_repository_name)` — since 260731-EFA-L2 the
five naming arguments arrive as one frozen `EnclosureSelector` (from `models.py`) rather than as
`contract_path, task_name, parent_task, leaf_id, worktree_name`. It resolves a worktree contract in
priority order: an explicit `selector.contract_path` first, then a task-based lookup via
`find_task_contract` when `selector.task_name` is supplied (leaf-enclosure-aware through
`selector.parent_task` / `selector.leaf_id`), then a `find_worktree_contract` fallback keyed on
`selector.worktree_name` alone. Missing or unparsable contracts produce `(None, candidate_path)` so
the resolver can still report the attempted path without mutating contract state.

`find_task_contract` selects the root `series-contract.md` or a specific leaf
enclosure contract through `worktrees.task_resolver.resolve_active_task_root` and
`worktrees.leaf_refs.resolve_leaf_enclosure_contract_for_ref`, with `parent_task` used for
disambiguation. `find_worktree_contract` exists because a `worktree_name` cannot
be reversed to a `task_name` (`slugify` keeps both `-` and `_`, so the prefix
boundary is lossy); it derives the worktree-group folder name via
`worktree_group_for` and matches it against each contract's recorded
`coordination.worktree_group`, scanning `tasks/<repo>` **recursively** for the
canonical `series-contract.md` (the enclosure layout nests contracts under
master + leaf folders, so main's original flat `*/contract.md` glob no longer
suffices). Archived (`0_archive/`) contracts are skipped during the scan
(`is_archived_path`), so a retired task cannot shadow an active one that shares a
worktree-group name.

### Invariants And Boundaries

- This module reads contract facts only; `c-09-git-worktree-manager` skill owns contract creation and
  mutation.
- Contract parser failures should not fabricate worktree facts.

## Docs References

No external documentation is needed for this package-local worktree contract adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worktree contract parsing and task-root candidate logic live in the worktrees package. | `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:436-469 |
| Alias-aware leaf enclosure lookup for explicit leaf ids lives in the dedicated leaf-ref resolver. | `resolve_leaf_enclosure_contract_for_ref` | mcp/src/agents_remember/worktrees/leaf_refs.py:175-200 |
| Resolver assembly consumes the optional contract payload. | `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:148-164 |

## Cross-Repo References

No cross-repository evidence is needed for local contract fact loading.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

Contract lookup delegates task-name selection to `worktrees.task_resolver` and explicit leaf-id selection to `worktrees.leaf_refs`, first resolving active task roots outside `0_archive/` and then choosing a root series contract or alias-aware leaf enclosure contract as requested. Independently, the `worktree_name` fallback resolves a contract by its derived worktree-group folder when no task name is available; the two paths coexist (task-based selection wins, worktree-name is the fallback), and both honor the canonical `series-contract.md` filename and skip `0_archive/`.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 3 citation claims
  (Repo-Internal reference rows); scoped result 0 findings.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `resolve_contract` was re-signed from `(contract_path, coordination_root, code_repository_name,
  task_name, parent_task=None, leaf_id=None, worktree_name=None)` to `(selector,
  coordination_root, code_repository_name)`, taking the frozen `EnclosureSelector`. Priority order
  and every lookup below it are unchanged. Verification metadata pinned until closeout stamps the
  L2 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4: explicit `leaf_id` task-contract lookup now delegates to
  `worktrees.leaf_refs.resolve_leaf_enclosure_contract_for_ref`, so qualified/doc-id/legacy refs resolve
  to canonical or existing legacy enclosure contracts without adding leaf-ref policy to this package.
  Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-06-28T20:30+02:00 — Post-landing cleanup (task 260628_post-landing-cleanup): `find_worktree_contract` now skips archived (`0_archive/`) contracts via `is_archived_path` (mirroring `iter_active_series_contracts`), so a retired task can't shadow an active worktree group; its docstring was also corrected from the stale `contract.md` to the canonical `series-contract.md` nesting. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): `resolve_contract` gained a `worktree_name` fallback (MCP 2.9.3, `find_worktree_contract`) that resolves a contract by its worktree-group folder name when no task name is known, scanning `tasks/<repo>` recursively for the canonical `series-contract.md`. Reconciled onto the series' leaf-enclosure resolution (`parent_task`/`leaf_id`); task-based lookup stays first, the worktree-name match is the fallback.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: contract resolution now finds root `series-contract.md` or a specific leaf enclosure through `resolve_active_task_root` / `resolve_leaf_enclosure_contract`, with `parent_task` used only for disambiguation. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-25T20:57+02:00: Created by extracting worktree contract fact loading from the `c-08-ar-coordination-context-resolver` skill resolver.
