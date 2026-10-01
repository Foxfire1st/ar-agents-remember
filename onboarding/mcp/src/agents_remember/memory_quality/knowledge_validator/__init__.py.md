# mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py

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
- The module map names `rules_history` (MIK-R09's rule on history rows that are not frozen: their subjects name records and their covered entries' `after` anchors are the tree's; leaf 260928-MIK-L09). Nothing is re-exported for it; `validator.py` imports it for its registration of `R09-history-rows` and the report-only `R09-history-rows-merged`.
- The docstring states the scope boundary: the validator judges no meaning (Doc13). Whether a statement is true or a realization really enforces its invariant is the curator's and the reviewer's; whether an anchor's content still matches the code is currentness (MIK-R03), not validity.

### Conventions

- The package lives in `memory_quality` (rank 11). The worktree layer reaches it only through `worktrees.services.KnowledgeValidationPort`, bound by `application/worktree_services.py`.
- Test and route code import from this package root; `commit_route` and `trees.is_excluded_from_knowledge` are imported by module path.

### Invariants And Boundaries

- One validator, one rule registry: every caller (the sync's memory merge, the standalone command, later the writer and MIK-R09's routes) runs the same registered rules.
- There is no API that skips a rule.
- **Nothing in the installed runtime reaches a converted tree before MIK-R37.** The live memory repository has no `knowledge/layout.json`, so every route that calls the validator returns before it runs.

### Todos

None recorded. The routes that MIK-R09 owns (closeout, direct/record landing, master and checkpoint landing) now call this package (leaf 260928-MIK-L09, the carried L22 obligation: `memory_commit_refusal` at every route, and the gate's own validator run); the writer (MIK-R12) calls it too. All of it runs only on converted memory.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The re-exported API and the module map.

- The re-exported names, `writer_reported_rule_ids` included. [1]
- Importing the validator registers the rule modules, MIK-R04's route rules and MIK-R27's admission rules included. [2]
- The route adapter the composition binds. [3]
- The module map names MIK-R09's history-row rule, and importing the validator registers it. [4]
- The module map names MIK-R14's link guard, and importing the validator registers it. [5]
- The module map names MIK-R13's decision rules, and importing the validator registers them. [6]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
