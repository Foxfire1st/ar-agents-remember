# mcp/src/agents_remember/memory_quality/knowledge_validator/__init__.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The public face of the mandatory knowledge validator (MIK-R22): integrity checked at the memory commit boundary, because text files are the source of truth for knowledge (D18).** The package docstring maps each module to its job, and this module re-exports the API that callers and later packets use: the registry (`ValidationRule`, `register_rule`, `registered_rules`, `ValidationContext`, `Finding`), the report (`Violation`, `ValidationReport`, `KnowledgeValidationError`), the tree inputs and readers, and `validate_tree`, `validation_applies` and `require_valid_commit`.

## Code Commentary

### Logic

- It imports only; there is no logic here. Importing `validator` (which the re-export does) imports `rules_structure` and `rules_references`, and that registers MIK-R22's 16 rules; since MIK-R04 (leaf 260928-MIK-L04) it also imports `rules_routes`, which registers MIK-R04's six family route rules; since MIK-R27 (leaf 260928-MIK-L27) it also imports `rules_admission`, which registers MIK-R27's three admission rules. Since MIK-R13 (leaf 260928-MIK-L13) it also imports `rules_decisions`, which registers five decision content rules; governs links now refuse commit/landing publication and are writer-reported for repair, not permanently report-only.
- The module map names `family_routes` and `rules_routes` (MIK-R04's Coverage, Non-empty, the reported states and the mechanical suggestion), and the re-exports gain `writer_reported_rule_ids`, the IDs of the refusing rules a writer reports instead of refusing.
- The module map names `rules_admission`: new-record admission refuses; unsupported existing-record
  criteria carry `merge_reports` (report at sync/standalone conversion, refuse commit/landing,
  writer-report for repair). The live `legacy-unassessed` count carries `migration_debt`: base-carried
  live debt reports while migration is incomplete, new debt refuses outside standalone conversion,
  and carried debt refuses once every route is migrated/excluded. Nothing is re-exported for it: its
  rules reach callers through the one registry, not an admission-maintenance exemption.
- The module map names `rules_decisions` (MIK-R13's decision content rules: alternatives, `reconsider_when`, `superseded` never stored, `reconsider_on` indexes, and the governs links refused at commit/landing publication (writer-reported for repair)). Nothing is re-exported for it either.
- The module map names `rules_reconsideration` (MIK-R14's guard `R14.1-linked-alternative-order`: an alternative a `reconsider_on` link addresses keeps its index, so a reorder never silently retargets the link). Nothing is re-exported for it; `validator.py` imports it for its registration.
- The module map names `rules_history` (MIK-R09's rule on history rows that are not frozen: their subjects name records and their covered entries' `after` anchors are the tree's; leaf 260928-MIK-L09). Nothing is re-exported for it; `validator.py` imports it for its registration of `R09-history-rows` and `R09-history-rows-merged` with `merge_reports`: report at sync/standalone conversion, repair before the next refusing leaf publication/landing.
- The docstring states the scope boundary: the validator judges no meaning (Doc13). Whether a statement is true or a realization really enforces its invariant is the curator's and the reviewer's; whether an anchor's content still matches the code is currentness (MIK-R03), not validity.
- The module map names `rules_overviews`: R80's fixed purpose-first heading, prohibition of leaf/date-named sections, and terminal citation region. Importing the re-exported validator registers those checks through its `rules_overviews` import. No second registry or rule-skipping facade is introduced; see [the overview-rule card](rules_overviews.py.md) for the exact parser and leaf-publication/conversion-context boundary.

### Conventions

- The package lives in `memory_quality` (rank 11). The worktree layer reaches it only through `worktrees.services.KnowledgeValidationPort`, bound by `application/worktree_services.py`.
- Test and route code import from this package root; `commit_route` and `trees.is_excluded_from_knowledge` are imported by module path.

### Invariants And Boundaries

- One validator, one rule registry: every caller (the sync's memory merge, the standalone command, later the writer and MIK-R09's routes) runs the same registered rules.
- There is no API that skips a rule. Plain `report_only=True` registration is refused; reporting
  requires a named `merge_reports` or `migration_debt` reason, not a permanent waiver.
- Applicability is a property of the supplied trees: commit validation runs when the candidate or any comparison base has the layout marker. An unconverted pair returns without validation; this is not a claim that current live memory has no marker.

### Todos

None recorded. The routes that MIK-R09 owns (closeout, direct/record landing, master and checkpoint landing) now call this package (leaf 260928-MIK-L09, the carried L22 obligation: `memory_commit_refusal` at every route, and the gate's own validator run); the writer (MIK-R12) calls it too. All of it runs only on converted memory.

## The Family-Judgment Rule Registration (MIK-R48)

The module docstring names MIK-R48's rule beside the history-row rule: at a
leaf's publication a new or edited changed family row records its effect and own
revision. Registration itself is unchanged; one module still owns the registry.


- The validator package's module map names the family-judgment publication rule.


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


- The module map names MIK-R14's link guard, and importing the validator registers it. [5]

- The public module map documents overview order; the exported validator registers its checks through the common registry. [8]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.

- Overview-order rules activate at leaf publication, not conversion or ordinary adoption/census/writer validation. [9]

- The module map names history-row rules; importing the validator registers the refusing rule and the merged-row rule with merge_reports. [4]
- The module map names decision rules, including governs links refused at commit/landing publication; the validator registers them. [6]
- Current source delta inspected statically: Replace permanent reporting summaries with named reasons and governs refusal; retain common registry and meaning/currentness boundary. [10]
