# mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

**The curator checklist's knowledge-worklist section, and the worklist's wire summary (MIK-R08 rule 7).**
The application layer computes the worklist and hands the checklist its persisted `knowledge-worklist/v1`
document; this module only renders it. `worklist_summary` is also the compact summary the memory-quality
response, the managed-sync response and `knowledge_integrity_check` carry.

## Code Commentary

### Logic

- `worklist_summary(document, path)` returns `state`, `path`, `digest`, `itemCount`, `itemsByKind` (sorted
  counts) and `incomplete` (the unreadable inputs).
- `knowledge_worklist_lines(document, path)` renders `## Knowledge worklist (MIK-R08)`
  (`WORKLIST_SECTION_HEADING`): the state, the file, the digest, and the pairing (B, K_B with
  "(converted base)" when it applies, the C tree and the K_C tree, shortened by `_short`).
  - An `incomplete` run lists each unreadable input and its detail and stops: no item list exists.
  - Otherwise it explains that each item needs a row about its subject in the leaf's history file
    (MIK-R07) and that the gate is MIK-R09's, then either "No item: the change reaches no recorded
    knowledge." or a `| Kind | Subject | Item | Facts |` table.
- `_item_facts` summarizes each kind: a touched invariant's entries with their classes, added, retired and
  re-anchored IDs and a changed record's revisions (`_entry_facts`); a stale invariant's stale entries; a
  reached family's member count and `reachedBy` reasons. `_cell` escapes pipes and newlines.

### Conventions

- The module is pure rendering; it imports nothing from the application layer, so `leaf.py` and
  `surface.py` import `worklist_summary` from here.

### Invariants And Boundaries

- **Information, never a count.** The section does not count toward `curatorActionableCount`, the
  attestation or the wire counts; what an open item blocks is the closeout gate's (MIK-R09), live at the
  cutover (MIK-R37).
- **Unchanged bytes for unconverted leaves.** The checklist renders the section only when a worklist
  exists, so today's checklist is byte-identical.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rendering only; never counted toward `curatorActionableCount`. | "It does not count toward" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:1-8 |
| The section heading. | `WORKLIST_SECTION_HEADING` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:18-18 |
| The compact wire summary. | `worklist_summary` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:27-38 |
| Per-kind facts. | `_entry_facts`; `_item_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:41-52; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:55-67 |
| The section lines, the incomplete branch and the item table. | `knowledge_worklist_lines` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:74-121 |
| The checklist renders it only when a worklist exists. | `knowledge_worklist`; `knowledge_worklist_lines` | mcp/src/agents_remember/memory_quality/curator_checklist.py:69-69; mcp/src/agents_remember/memory_quality/curator_checklist.py:289-289 |
| The controller renders the section and keeps the count at 0. | `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` | mcp/tests/test_knowledge_worklist_leaf.py:572-660 |

## Cross-Repo References

No meaningful cross-repo references found: the module renders an in-memory document.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
