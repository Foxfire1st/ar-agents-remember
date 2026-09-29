# mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The public face of the mandatory knowledge validator (MIK-R22): integrity checked at the memory commit boundary, because text files are the source of truth for knowledge (D18).** The package docstring maps each module to its job, and this module re-exports the API that callers and later packets use: the registry (`ValidationRule`, `register_rule`, `registered_rules`, `ValidationContext`, `Finding`), the report (`Violation`, `ValidationReport`, `KnowledgeValidationError`), the tree inputs and readers, and `validate_tree`, `validation_applies` and `require_valid_commit`.

## Code Commentary

### Logic

- It imports only; there is no logic here. Importing `validator` (which the re-export does) imports `rules_structure` and `rules_references`, and that registers MIK-R22's 16 rules.
- The docstring states the scope boundary: the validator judges no meaning (Doc13). Whether a statement is true or a realization really enforces its invariant is the curator's and the reviewer's; whether an anchor's content still matches the code is currentness (MIK-R03), not validity.

### Conventions

- The package lives in `memory_quality` (rank 11). The worktree layer reaches it only through `worktrees.services.KnowledgeValidationPort`, bound by `application/worktree_services.py`.
- Test and route code import from this package root; `commit_route` and `trees.is_excluded_from_knowledge` are imported by module path.

### Invariants And Boundaries

- One validator, one rule registry: every caller (the sync's memory merge, the standalone command, later the writer and MIK-R09's routes) runs the same registered rules.
- There is no API that skips a rule.
- **Nothing in the installed runtime reaches a converted tree before MIK-R37.** The live memory repository has no `knowledge/layout.json`, so every route that calls the validator returns before it runs.

### Todos

None recorded. The routes that MIK-R09 owns (closeout, direct/record landing, master and checkpoint landing) and the writer (MIK-R12) will call this package; they are not wired yet.

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

The re-exported API and the module map.

| Finding | Anchor | Source |
| --- | --- | --- |
| The re-exported names. | `__all__` | mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py:49-68 |
| Importing the validator registers the rule modules. | `rules_references`; `rules_structure` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:18-23 |
| The route adapter the composition binds. | `GitKnowledgeValidation` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:26-54 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
