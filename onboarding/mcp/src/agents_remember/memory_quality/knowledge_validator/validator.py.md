# mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**Runs every registered rule over one candidate tree.** `validate_tree` is the validator itself; `validation_applies` is rule 8's applicability; `require_valid_commit` is what a commit route calls before it commits memory.

## Code Commentary

### Logic

- `validate_tree(candidate, *, bases=(), code=None, conversion=False)` builds a `ValidationContext` with `parse_tree(candidate)` and collects a `Violation` for every finding of every registered rule, stamping the rule's ID and `report_only`. It returns a sorted `ValidationReport`. `code` is required unless `conversion` is set; a conversion run checks no anchor for path existence.
- `validation_applies(candidate, bases)` is true when the candidate or any base holds the layout marker.
- `require_valid_commit(candidate, *, bases, code)` returns `None` when validation does not apply, the report when the candidate passes (report-only findings included), and raises `KnowledgeValidationError` naming every refusing violation otherwise.

### Conventions

- The module imports `rules_references`, `rules_routes` (MIK-R04, since leaf 260928-MIK-L04) and `rules_structure` for their registration side effect, so MIK-R04's six family route rules run wherever the validator runs.
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
| The validator: every registered rule over the candidate. | `validate_tree` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:40-76 |
| Rule 8's applicability: the marker on any side. | `validation_applies` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:79-82 |
| The commit route's call: nothing, the report, or the refusal. | `require_valid_commit` | mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py:85-100 |
| Commit routes validate only when a side has the marker. | `test_commit_routes_validate_only_when_a_side_has_the_layout_marker` | mcp/tests/test_knowledge_validator.py:505-517 |
| An unconverted base is refused, and a standalone conversion checks no path. | `test_an_unconverted_base_is_refused_and_a_standalone_conversion_checks_no_path` | mcp/tests/test_knowledge_validator.py:417-429 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — `validator.py` now imports `rules_routes`, registering MIK-R04's family route rules.** The Conventions bullet names it. The rows were re-pointed by the exact three-line shift, their claims unchanged. No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
