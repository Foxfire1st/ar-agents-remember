# mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
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
- **Leaf publications and Git failures (MIK-R09, leaf 260928-MIK-L09).** The body moved into `_refusal(commit, *, leaf_publication=False)` over a small `_Commit` record, and two entry points call it: `refusal(...)` as before, and the new `leaf_refusal(...)` for a commit that publishes a leaf (closeout, direct landing, a leaf's recorded landing), which passes `leaf_publication=True` to `require_valid_commit`. The history-row rule then re-anchor-checks every history file not closed in a base, whatever its own `closed` flag (review R1 F1, ruling 2026-09-30T16:07:55). A `subprocess.SubprocessError` (a Git read that failed or timed out) is now a named refusal ("… a Git call failed or timed out …"), never an escaping error (F9).

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
| The adapter, with its optional base converter. | `GitKnowledgeValidation`; `BaseConverter` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:28-28; mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:41-124 |
| An unconverted base of a converted candidate is replaced by its conversion before the rules run, since MIK-R09 inside `_refusal`, which both entry points call. | `_refusal`; "if candidate.converted and self.base_converter is not None:" | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:81-124 |
| The two entry points; a leaf publication checks the leaf's own history file whatever its flag; a Git failure is named (MIK-R09). | `_Commit`; "def leaf_refusal("; "except subprocess.SubprocessError as error:" | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:32-38; mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:65-79; mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:119-124 |
| The converter the composition binds. | `GitBaseConverter` | mcp/src/agents_remember/memory/conversion/base.py:101-139 |
| The commit route validates against the conversion of an unconverted base. | `test_the_commit_route_validates_against_the_conversion_of_an_unconverted_base` | mcp/tests/test_knowledge_crossing.py:293-336 |
| The port it implements. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:133-162 |
| The default composition binds it. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:211-224 |
| The adapter refuses naming every violation. | `test_the_commit_route_adapter_refuses_naming_every_violation` | mcp/tests/test_knowledge_validator_routes.py:103-131 |

## Cross-Repo References

The memory repository and the code repository are separate Git repositories, but both are addressed explicitly by the caller and read through the same kernel Git runner; no external system is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** A Logic bullet records `_refusal` over `_Commit`, the new `leaf_refusal` entry point that sets `leaf_publication` (review R1 F1) and the named refusal for a Git failure (F9). One row added. **Row re-measured, not shifted:** the base-converter row's `refusal` anchor already lay outside its `61-73` range at base (the method began at line 42); its body moved into `_refusal`, so it is reworded and re-anchored on `_refusal` and the converter's own line (`81-124`). The fixer normalised the other rows.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Body update: the converted base (MIK-R24 rule 7).** Added a Logic bullet on the optional `base_converter` and its binding to `GitBaseConverter`, plus three rows. Re-measured the adapter, port and composition rows (the class grew and became a frozen dataclass).
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
