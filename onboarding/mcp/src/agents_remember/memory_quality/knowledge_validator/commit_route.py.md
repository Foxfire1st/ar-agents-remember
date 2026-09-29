# mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The validator as a commit route calls it: Git trees in, a refusal text out (MIK-R22 rule 8).** `GitKnowledgeValidation` implements the worktree layer's `KnowledgeValidationPort`; `application/worktree_services.build_default_worktree_services` binds it.

## Code Commentary

### Logic

- `refusal(*, memory_repository, candidate_tree, bases, code_repository, code_commit)` reads the candidate and each base with `knowledge_tree_from_git`. If `validation_applies` is false it returns `None`. Otherwise it reads the code tree with `code_tree_from_git` and calls `require_valid_commit`.
- A `KnowledgeValidationError` becomes its message, which names every violation.
- **Converted base (MIK-R24 rule 7).** `GitKnowledgeValidation` is a frozen dataclass with an optional `base_converter` (`BaseConverter`: `(memory_repository, base, *, after, code_repository, code_commit) -> KnowledgeTree`). When the candidate is converted and a converter is bound, each unconverted base tree is replaced by `base_converter(...)` before `require_valid_commit` runs, so the mechanical conversion never counts as a change. The composition binds `memory/conversion/base.GitBaseConverter`, which converts the base at its own `Code-Commit`. Without a converter such a base is still refused by rule 6 (`R22.6-base-converted`).
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
| The adapter, with its optional base converter. | `GitKnowledgeValidation`; `BaseConverter` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:31-80; mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:27-28 |
| An unconverted base of a converted candidate is replaced by its conversion before the rules run. | `refusal`; "self.base_converter" | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:61-73 |
| The converter the composition binds. | `GitBaseConverter` | mcp/src/agents_remember/memory/conversion/base.py:101-139 |
| The commit route validates against the conversion of an unconverted base. | `test_the_commit_route_validates_against_the_conversion_of_an_unconverted_base` | mcp/tests/test_knowledge_crossing.py:293-336 |
| The port it implements. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:132-148 |
| The default composition binds it. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:208-218 |
| The adapter refuses naming every violation. | `test_the_commit_route_adapter_refuses_naming_every_violation` | mcp/tests/test_knowledge_validator_routes.py:98-126 |

## Cross-Repo References

The memory repository and the code repository are separate Git repositories, but both are addressed explicitly by the caller and read through the same kernel Git runner; no external system is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Body update: the converted base (MIK-R24 rule 7).** Added a Logic bullet on the optional `base_converter` and its binding to `GitBaseConverter`, plus three rows. Re-measured the adapter, port and composition rows (the class grew and became a frozen dataclass).
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
