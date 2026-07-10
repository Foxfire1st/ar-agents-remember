# mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-07T20:50+02:00                                      |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`                  |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

`leaf_ref_start.py` adapts the shared task-tree leaf-ref resolver to the `worktree_start` command result
surface. It keeps the policy out of `start.py` and gives start-contract construction a small helper for
canonical doc-id resolution.

## Code Commentary

`resolve_start_leaf_doc_id(context, args)` resolves `args.leaf_id or args.worktree_name` within the
current repository and requested task/parent-task scope, returning only the canonical task doc id for
contract persistence. `invalid_leaf_ref_result(error)` maps resolver failures to exit code 2 with
`state`, `summary`, `expected`, and `candidates` fields so callers get the expected
`<repo>/<master-folder>/<doc-id>` form and candidate set.

## Invariants And Boundaries

- This module is start-specific glue; the resolver owns matching, ambiguity, and candidate policy.
- The helper returns doc ids because worktree contracts persist doc ids, while terminal catalogs persist
  qualified ids.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared resolver and `LeafRefResolutionError` payload facts. | [../../leaf_refs.py](../../leaf_refs.py.md) |
| Start contract builder that calls these helpers. | [start_contract.py](start_contract.py.md) |

## Update History

- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created as the worktree-start adapter for canonical leaf-ref
  resolution and refusal payloads. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
