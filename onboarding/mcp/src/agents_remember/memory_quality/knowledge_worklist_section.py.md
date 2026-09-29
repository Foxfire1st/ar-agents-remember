# mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
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
    (MIK-R07) and that the gate is MIK-R09's, then the planned-effects block (`_planned_lines`, below),
    then either "No item: the change reaches no recorded knowledge." or a `| Kind | Subject | Plan | Item |
    Facts |` table. Since MIK-R11 the **Plan** column shows each item's `planning` mark (`-` for a kind with
    none), and the subject cell is escaped by `_cell`.
  - **Planned effects (MIK-R11 rule 7, `_planned_lines`).** With no declaration: one line, "none declared in
    the task document, so every item is `unplanned`". Otherwise one line per declaration: its planned key and
    `requirementRef`, then "matched by `<row or invariant>`", or **unmatched** with the reason and either
    "answered by `<row>`" or "needs a planned row".
- `_item_facts` summarizes each kind: a touched invariant's entries with their classes, added, retired and
  re-anchored IDs and a changed record's revisions (`_entry_facts`); a stale invariant's stale entries; a
  reached family's member count and `reachedBy` reasons; since MIK-R11 a `planned_untouched` item's
  declaring `requirementRef`, its unmatched reason, each row about the declared record marked "(does not
  deliver it)", and "answered by <row>" or "needs a planned row" (`_planned_facts`). `_cell` escapes pipes
  and newlines.

### Conventions

- The module is pure rendering; it imports nothing from the application layer, so `leaf.py` and
  `surface.py` import `worklist_summary` from here.

### Invariants And Boundaries

- **Information, never a count.** The section does not count toward `curatorActionableCount`, the
  attestation or the wire counts; what an open item blocks is the closeout gate's (MIK-R09), live at the
  cutover (MIK-R37).
- **Unchanged bytes for unconverted leaves.** The checklist renders the section only when a worklist
  exists, so today's checklist is byte-identical. The MIK-R11 block and column appear only inside that
  section, so they change converted checklists only (review R1 F4: every converted checklist gains the
  column and the "Planned effects" line).

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
| Per-kind facts. | `_entry_facts`; `_item_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:41-52; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:55-69 |
| A `planned_untouched` item's facts. | `_planned_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:72-82 |
| The planned-effects block, one line per declaration. | `_planned_lines`; "Planned effects (MIK-R11)" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:85-111 |
| The section lines, the incomplete branch, the planned block and the item table with its **Plan** column. | `knowledge_worklist_lines`; "Plan" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:118-166 |
| The checklist and the tool show the marks. | `test_a_leaf_reads_its_declaration_and_the_checklist_and_tool_show_the_marks` | mcp/tests/test_planned_knowledge_effects.py:530-587 |
| The checklist renders it only when a worklist exists. | `knowledge_worklist`; `knowledge_worklist_lines` | mcp/src/agents_remember/memory_quality/curator_checklist.py:69-69; mcp/src/agents_remember/memory_quality/curator_checklist.py:289-289 |
| The controller renders the section and keeps the count at 0. | `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` | mcp/tests/test_knowledge_worklist_leaf.py:577-669 |

## Cross-Repo References

No meaningful cross-repo references found: the module renders an in-memory document.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Logic now records the planned-effects block (`_planned_lines`), the **Plan** column and the `planned_untouched` facts (`_planned_facts`); the byte-identity boundary notes that only converted checklists change (review R1 F4, carried to L09 by ruling 22:35:34). Three rows added, two reworded and re-measured. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
