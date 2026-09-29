# mcp/tests/test_knowledge_validator.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_validator.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R22 rules 1–9 at unit level, over converted fixture trees.** Each test changes one thing in the fixture tree and checks that exactly the owning rule answers, with its rendered file, field and rule (`_only`). Registered in the `unit-regression` lane; 37 collected cases.

## Code Commentary

### Logic

- **Baseline:** the fixture tree passes every rule; the report-only set is pinned to `R22.3-sidecar-without-markdown`, `R22.3-unresolved-target` and `R22.6-carried-stale`.
- **Rule 1:** a bad field, a non-canonical file (naming the formatter), a file outside the layout, and a misplaced sidecar.
- **Rule 2:** the filename prefix, duplicate IDs after a merge (`merge conflict:` naming both files), the packet's conforming parallel-mint example, and duplicate entry IDs across sidecars.
- **Rule 3:** the packet's non-conforming hand-added `[4]`, an unused reference, Markdown without a sidecar, a file sidecar without Markdown (reported; holds no references), record links, a retired record, an unresolved target (reported), a disallowed relation by field, and a dot-named card with its sidecar.
- **Rules 4 and 5:** an invariant that lists its realizations; a missing family member.
- **Rule 6:** an added anchor at a missing path, a carried anchor at a deleted path (reported stale), the packet's boundary merge example, re-anchored and moved entries, locator and content rules, and an unconverted base with the standalone conversion.
- **Rule 7:** a closed history file is frozen (edited, deleted, closed in one merge parent); an open one may change; history is shape-only (the packet's rename boundary example).
- **Rules 8 and 9:** applicability by the marker; a later packet's rule runs everywhere and a report-only rule never refuses.
- **Markers:** the grammar table and the invalid-number message.

### Conventions

- The rule-9 test registers two test rules and removes them from `registry._REGISTRY` in a `finally` block.

### Invariants And Boundaries

- Every packet example (conforming, non-conforming and boundary) is covered at this level.

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

Representative cases; the full list is in the module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture tree passes, and the report-only set is pinned. | `test_converted_fixture_tree_passes_every_rule` | mcp/tests/test_knowledge_validator.py:87-98 |
| Merge duplicates are conflicts naming both files; parallel mints merge cleanly. | `test_duplicate_ids_after_a_merge_are_a_conflict_naming_both_files`; `test_parallel_leaves_minting_different_ids_merge_cleanly` | mcp/tests/test_knowledge_validator.py:149-162; mcp/tests/test_knowledge_validator.py:165-172 |
| The hand-added marker is refused. | `test_a_hand_added_marker_without_a_reference_is_refused` | mcp/tests/test_knowledge_validator.py:192-200 |
| A dot-named card and its sidecar are validated. | `test_a_dot_named_card_and_its_sidecar_are_validated` | mcp/tests/test_knowledge_validator.py:292-312 |
| The boundary merge: three rows, passes, three stale reports. | `test_merge_where_one_parent_deleted_a_file_the_other_parents_card_cites` | mcp/tests/test_knowledge_validator.py:364-380 |
| A closed history file is frozen. | `test_a_closed_history_file_is_frozen` | mcp/tests/test_knowledge_validator.py:454-469 |
| A later rule runs everywhere; report-only never refuses. | `test_a_later_packets_rule_runs_everywhere_and_report_only_never_refuses` | mcp/tests/test_knowledge_validator.py:520-537 |

## Cross-Repo References

No meaningful cross-repo references found: the cases run over in-memory trees.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
