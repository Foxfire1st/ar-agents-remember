# mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The public face of the mandatory knowledge validator (MIK-R22): integrity checked at the memory commit boundary, because text files are the source of truth for knowledge (D18).** The package docstring maps each module to its job, and this module re-exports the API that callers and later packets use: the registry (`ValidationRule`, `register_rule`, `registered_rules`, `ValidationContext`, `Finding`), the report (`Violation`, `ValidationReport`, `KnowledgeValidationError`), the tree inputs and readers, and `validate_tree`, `validation_applies` and `require_valid_commit`.

## Code Commentary

### Logic

- It imports only; there is no logic here. Importing `validator` (which the re-export does) imports `rules_structure` and `rules_references`, and that registers MIK-R22's 16 rules; since MIK-R04 (leaf 260928-MIK-L04) it also imports `rules_routes`, which registers MIK-R04's six family route rules; since MIK-R27 (leaf 260928-MIK-L27) it also imports `rules_admission`, which registers MIK-R27's three admission rules. Since MIK-R13 (leaf 260928-MIK-L13) it also imports `rules_decisions`, which registers MIK-R13's five decision content rules (four refusing, one report-only).
- The module map names `family_routes` and `rules_routes` (MIK-R04's Coverage, Non-empty, the reported states and the mechanical suggestion), and the re-exports gain `writer_reported_rule_ids`, the IDs of the refusing rules a writer reports instead of refusing.
- The module map names `rules_admission` (MIK-R27's admission rule: refused on a new record, reported on an existing one, and the count of records still `legacy-unassessed`). Nothing is re-exported for it: its rules reach callers through the one registry.
- The module map names `rules_decisions` (MIK-R13's decision content rules: alternatives, `reconsider_when`, `superseded` never stored, `reconsider_on` indexes, and the governs links reported). Nothing is re-exported for it either.
- The module map names `rules_reconsideration` (MIK-R14's guard `R14.1-linked-alternative-order`: an alternative a `reconsider_on` link addresses keeps its index, so a reorder never silently retargets the link). Nothing is re-exported for it; `validator.py` imports it for its registration.
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
| The re-exported names, `writer_reported_rule_ids` included. | `__all__` | mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py:58-78 |
| Importing the validator registers the rule modules, MIK-R04's route rules and MIK-R27's admission rules included. | `rules_admission`; `rules_references`; `rules_routes`; `rules_structure` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:19-19; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:31-31; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:34-34; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:37-37 |
| The route adapter the composition binds. | `GitKnowledgeValidation` | mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:31-80 |
| The module map names MIK-R14's link guard, and importing the validator registers it. | "MIK-R14's guard: an alternative a"; "registers MIK-R14's link guard" | mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py:17-18; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:27-29 |
| The module map names MIK-R13's decision rules, and importing the validator registers them. | `rules_decisions` | mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py:15-16; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:24-26 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** A Logic bullet records that the module map names `rules_reconsideration` (the `R14.1-linked-alternative-order` guard; nothing re-exported). One row added. The rows the fixer declined were re-pointed by the exact line shift of this leaf's diff; the others were normalised by the installed fixer. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **body updated for MIK-R13.** Logic records the `rules_decisions` module-map entry and its registration through `validator.py` (five decision content rules). One row was added; the existing import row the fixer re-pointed was not reworded. No verification stamp was advanced.
- 2026-09-30T01:08:26+00:00: Generated citation repair: `rules_admission`; `rules_references`; `rules_routes`; `rules_structure` repointed to mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:19-19; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:28-28; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:31-31; mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:34-34. No content impact: mechanical anchor-range projection bound to citation source snapshot 8a187177fd97aa785f74b03e4a26914c71c4a09b0afe5ab323208b62b13057b0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — the module map names MIK-R27's `rules_admission`, which `validator.py` imports for its registration.** Logic states both; the import row was reworded and re-measured (`validator.py:18-32`), and the `__all__` row re-pointed by the exact +2 shift (`:54-74`). No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — the module map names MIK-R04's `family_routes` and `rules_routes`, and `writer_reported_rule_ids` is re-exported.** Logic states both; two rows reworded and re-pointed by the exact line shift (`__all__` now `:52-72`). No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
