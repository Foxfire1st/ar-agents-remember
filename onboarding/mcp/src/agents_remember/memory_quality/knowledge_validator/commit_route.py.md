# mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The adapter, the port it implements and its binding.

- The adapter, with its optional base converter. [1]
- An unconverted base of a converted candidate is replaced by its conversion before the rules run, since MIK-R09 inside `_refusal`, which both entry points call. [2]
- The two entry points; a leaf publication checks the leaf's own history file whatever its flag; a Git failure is named (MIK-R09). [3]
- The converter the composition binds. [4]
- The commit route validates against the conversion of an unconverted base. [5]
- The port it implements. [6]
- The default composition binds it. [7]
- The adapter refuses naming every violation. [8]

### Cross-Repo References

The memory repository and the code repository are separate Git repositories, but both are addressed explicitly by the caller and read through the same kernel Git runner; no external system is involved.

No cross-repo boundary is crossed by this file.
