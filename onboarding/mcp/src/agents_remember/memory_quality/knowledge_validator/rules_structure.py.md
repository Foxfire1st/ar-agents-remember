# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R22's per-file and cross-tree structure rules: shape, identity, single owner, locators and content, converted bases, and history freezing.** Importing the module registers its eight rules in `STRUCTURE_RULES`.

## Code Commentary

### Logic

- `R22.1-shape` (`check_shape`): the candidate keeps `knowledge/layout.json`, plus every `shape` problem.
- `R22.1-canonical`: every `canonical` problem, whose message names the formatter command.
- `R22.2-identity` (`check_identity`): `identity` problems; record IDs and realization/proof entry IDs share one uniqueness space, and a duplicate names every file that holds it. With more than one base (a merge) the message starts `merge conflict:`. A record's Markdown must sit beside its JSON record.
- `R22.4-single-owner`: an undeclared record field is a relationship recorded on the wrong side (Doc14 §2), such as an invariant that lists its realizations.
- `R22.6-locator` and `R22.6-content`: the locator kind and the `content` hash format problems.
- `R22.6-base-converted` (`check_bases_converted`): a comparison base without the marker is refused, naming its conversion (MIK-R24 rules 7 and 8) and the crossing sync; skipped for a standalone conversion.
- `R22.7-history-frozen` (`check_history_frozen`): over every history path in any base or the candidate, L07's `frozen_history_violation` decides; a closed file changed or deleted is refused.

### Conventions

- Each rule filters `ParsedTree.problems` by category (`_problems`) or computes a tree-level check; none re-parses a file.

### Invariants And Boundaries

- Rule 4 is enforced at shape level: the models' `extra="forbid"` makes a second owner unrepresentable, and this rule attributes it.
- History row IDs are outside ID uniqueness, because two frozen files that collided could never be repaired.
- A closed history file is byte-identical in the candidate; deletion counts as a change.

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

The structure rules and their registration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Shape keeps the layout marker; canonical formatting is its own rule. | `check_shape`; `check_canonical` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:44-51; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:54-55 |
| Unique IDs across records and entries; a merge duplicate is a conflict naming both files. | `check_identity` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:58-80 |
| A relationship on the wrong side is a rule-4 refusal. | `check_single_owner` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:83-90 |
| An unconverted base is refused unless this is a standalone conversion. | `check_bases_converted` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:101-111 |
| A closed history file is frozen. | `check_history_frozen` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:114-131 |
| The eight registered structure rules. | `STRUCTURE_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py:134-163 |
| Duplicate IDs after a merge are a conflict naming both files. | `test_duplicate_ids_after_a_merge_are_a_conflict_naming_both_files` | mcp/tests/test_knowledge_validator.py:149-162 |
| A closed history file is frozen, including deletion and closure in one merge parent. | `test_a_closed_history_file_is_frozen` | mcp/tests/test_knowledge_validator.py:454-469 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
