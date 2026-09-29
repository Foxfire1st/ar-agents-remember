# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R22's cross-file rules: markers and references, record links, relations, unresolved targets, family members, and anchor paths.** Importing the module registers its eight rules in `REFERENCE_RULES`, three of them report-only. None of these rules reads a history file.

## Code Commentary

### Logic

- `R22.3-markers` (`check_markers`): every marker of an onboarding Markdown file has a reference in its sidecar, and every reference is used. Markdown without a sidecar (a record's Markdown included) holds no markers. A file sidecar without Markdown holds no references, and a route sidecar must sit beside its `overview.md`. When the paired sidecar exists but does not parse, the Markdown is skipped, because its shape violation is reported instead.
- `R22.3-sidecar-without-markdown` (**report-only**): the file sidecar itself is reported (MIK-R21 rule 5).
- `R22.3-record-links`: every ID a sidecar reference target, an entry's `invariant`, a record's `supersedes` or a record link target names must exist in `record_ids`; route targets are exempt, and a retired record still resolves.
- `R22.3-relations`: the `relation` problems found while parsing.
- `R22.3-unresolved-target` (**report-only**): each `unresolved` target.
- `R22.5-family-members`: every family member exists; the route rules are left to MIK-R04.
- `R22.6-anchor-path`: an anchor with no equal counterpart in any base must name a file in the paired code tree. For an entry the counterpart is the same entry ID; for a reference target, the same sidecar path. Skipped for a standalone conversion.
- `R22.6-carried-stale` (**report-only**): a carried anchor whose path is absent is reported as stale, never refused.

### Conventions

- `_sidecar_anchors` yields each anchor once with its sidecar, field and carried flag, and both anchor rules consume it.

### Invariants And Boundaries

- A carried anchor is never refused for a deleted path, so the stalest knowledge can still be represented and repaired.
- An added or re-anchored anchor must name an existing path.
- Report-only status comes from the registry flag, not from the check.

### Todos

`R22.6-carried-stale` surfaces the packet's "reported as stale references"; MIK-R24 rule 5 and MIK-R03 may take it over or reuse it later (worker gap 10).

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

The reference rules and their registration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Markers and references are paired both ways. | `check_markers`; `_markdown_findings` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:73-96; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:58-70 |
| Record links, entry invariants, supersedes and family members must exist. | `check_record_links`; `check_family_members` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:136-140; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:163-166 |
| Added anchors must name existing paths; carried anchors at absent paths are reported. | `check_anchor_paths`; `check_carried_stale` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:202-212; mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:215-226 |
| The eight registered reference rules, three report-only. | `REFERENCE_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py:229-269 |
| A hand-added marker without a reference is refused. | `test_a_hand_added_marker_without_a_reference_is_refused` | mcp/tests/test_knowledge_validator.py:192-200 |
| The boundary example: one parent deleted a file the other's card cites. | `test_merge_where_one_parent_deleted_a_file_the_other_parents_card_cites` | mcp/tests/test_knowledge_validator.py:364-380 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
