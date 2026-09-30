# mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**Runs every registered rule over one candidate tree.** `validate_tree` is the validator itself; `validation_applies` is rule 8's applicability; `require_valid_commit` is what a commit route calls before it commits memory.

## Code Commentary

### Logic

- `validate_tree(candidate, *, bases=(), code=None, conversion=False)` builds a `ValidationContext` with `parse_tree(candidate)` and collects a `Violation` for every finding of every registered rule, stamping the rule's ID and `report_only`. It returns a sorted `ValidationReport`. `code` is required unless `conversion` is set; a conversion run checks no anchor for path existence.
- `validation_applies(candidate, bases)` is true when the candidate or any base holds the layout marker.
- **`leaf_publication` (MIK-R09, leaf 260928-MIK-L09).** `validate_tree` and `require_valid_commit` gained a defaulted `leaf_publication` keyword that they pass into the `ValidationContext`: a commit that publishes a leaf (closeout, direct landing, a leaf's recorded landing) then has MIK-R09's history-row rule read every history file not closed in a base, whatever its own `closed` flag (review R1 F1). Every other caller is unchanged.
- `require_valid_commit(candidate, *, bases, code)` returns `None` when validation does not apply, the report when the candidate passes (report-only findings included), and raises `KnowledgeValidationError` naming every refusing violation otherwise.

### Conventions

- The module imports `rules_history` (MIK-R09, since leaf 260928-MIK-L09: `R09-history-rows` and the report-only `R09-history-rows-merged`), `rules_admission` (MIK-R27, since leaf 260928-MIK-L27), `rules_decisions` (MIK-R13, since leaf 260928-MIK-L13), `rules_reconsideration` (MIK-R14, since leaf 260928-MIK-L14), `rules_census` (MIK-R20, since leaf 260928-MIK-L20), `rules_references`, `rules_routes` (MIK-R04, since leaf 260928-MIK-L04) and `rules_structure` for their registration side effect, so MIK-R27's three admission rules, MIK-R13's five decision content rules, MIK-R20's nine census rules and MIK-R04's six family route rules run wherever the validator runs. Because the admission rules are registered here, the fixture tree's every validation now carries one report-only `R27.4-legacy-unassessed` count (its Doc14 family is an export).
- With no bases every anchor is checked for path existence (a writer's or a curator's run).

### Invariants And Boundaries

- `require_valid_commit` has no parameter that skips a rule.
- `conversion=True` exists in the API only; it is deliberately not exposed on the CLI (ruling Q2), so the tool surface has no skip flag.
- Before the cutover no production tree has the marker, so no production route changes behaviour.

### Todos

L24/L37 must pass converted bases, or call `validate_tree(..., conversion=True)` for the standalone conversion (worker gap 4).

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

The three entry points.

| Finding | Anchor | Source |
| --- | --- | --- |
| The validator: every registered rule over the candidate. | `validate_tree` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:55-94 |
| Rule 8's applicability: the marker on any side. | `validation_applies` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:97-100 |
| The commit route's call: nothing, the report, or the refusal. | `require_valid_commit` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:103-122 |
| Commit routes validate only when a side has the marker. | `test_commit_routes_validate_only_when_a_side_has_the_layout_marker` | mcp/tests/test_knowledge_validator.py:526-538 |
| An unconverted base is refused, and a standalone conversion checks no path. | `test_an_unconverted_base_is_refused_and_a_standalone_conversion_checks_no_path` | mcp/tests/test_knowledge_validator.py:428-440 |
| The registering import of MIK-R09's history-row rules. | `rules_history` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:27-29 |
| A leaf publication reaches the context (MIK-R09). | "leaf_publication=leaf_publication," | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:81-81 |
| The registering import of MIK-R14's link guard. | `rules_reconsideration` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:31-31 |
| The registering import of MIK-R13's decision content rules. | `rules_decisions` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:24-26 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** Logic records the defaulted `leaf_publication` keyword on `validate_tree` and `require_valid_commit` (review R1 F1), and Conventions the registering import of `rules_history`. Two rows added; the rows below the new import were re-pointed by the installed fixer (its bullets are kept, since no claim was reworded).
- 2026-09-30T18:00:35+00:00: Generated citation repair: `validation_applies` repointed to mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:97-100. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:00:35+00:00: Generated citation repair: `rules_reconsideration` repointed to mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:31-31. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** The Conventions bullet names the registering import of `rules_reconsideration` (MIK-R14's link guard); one row added. The other rows were normalised by the installed fixer. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **body updated for MIK-R13.** The Conventions bullet now names the `rules_decisions` import, which registers MIK-R13's five decision content rules wherever the validator runs. One row was added. Rows below the import were re-pointed by the installed fixer; no claim was reworded. No verification stamp was advanced.
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — `validator.py` now imports `rules_admission`, registering MIK-R27's three admission rules.** The Conventions bullet names it and the legacy count every fixture validation now carries. The rows were re-pointed by the exact three-line shift (`validator.py`) and by the test file's own shifts, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **body update — `validator.py` now imports `rules_census`, registering MIK-R20's nine census rules.** The Conventions bullet names it. The rows were re-pointed by the exact three-line shift, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — `validator.py` now imports `rules_routes`, registering MIK-R04's family route rules.** The Conventions bullet names it. The rows were re-pointed by the exact three-line shift, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
