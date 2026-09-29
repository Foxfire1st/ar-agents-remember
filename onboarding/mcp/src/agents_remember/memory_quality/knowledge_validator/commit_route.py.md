# mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The validator as a commit route calls it: Git trees in, a refusal text out (MIK-R22 rule 8).** `GitKnowledgeValidation` implements the worktree layer's `KnowledgeValidationPort`; `application/worktree_services.build_default_worktree_services` binds it.

## Code Commentary

### Logic

- `refusal(*, memory_repository, candidate_tree, bases, code_repository, code_commit)` reads the candidate and each base with `knowledge_tree_from_git`. If `validation_applies` is false it returns `None`. Otherwise it reads the code tree with `code_tree_from_git` and calls `require_valid_commit`.
- A `KnowledgeValidationError` becomes its message, which names every violation.
- Any other `ValueError` (an unreadable tree) becomes "the knowledge validator (MIK-R22) cannot read this commit's trees: …". An unreadable tree is refused, never committed unchecked.

### Conventions

- It returns text, not an exception, because the port is a protocol the worktree layer consumes without importing `memory_quality`.

### Invariants And Boundaries

- Every failure path returns a refusal; only a passing or out-of-scope commit returns `None`.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The adapter, the port it implements and its binding.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter. | `GitKnowledgeValidation` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:26-54 |
| The port it implements. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:131-147 |
| The default composition binds it. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:206-215 |
| The adapter refuses naming every violation. | `test_the_commit_route_adapter_refuses_naming_every_violation` | mcp/tests/test_knowledge_validator_routes.py:98-126 |

## Cross-Repo References

The memory repository and the code repository are separate Git repositories, but both are addressed explicitly by the caller and read through the same kernel Git runner; no external system is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
