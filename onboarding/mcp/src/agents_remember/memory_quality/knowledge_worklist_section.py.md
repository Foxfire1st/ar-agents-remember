# mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57`|
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
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
- **Dispatch table (L06, review R3-N1).** `_item_facts` looks the kind up in `_FACT_RENDERERS`
  (`touched_invariant` → `_entry_facts`, `stale_invariant` → `_stale_facts`, `reached_family` →
  `_family_facts`, `planned_untouched` → `_planned_facts`, `family_route_condition` → `_route_facts`, and
  since MIK-R10 `unexplained_hunk` and `unexplained_file` → `_unexplained_facts`); any other kind still gets
  its sorted fact keys. The `if`/`elif` ladder it replaced rendered the same text.
- **Family route facts (MIK-R06, `_route_facts`).** The condition and what it affects (`_route_affected`:
  the base view's routes or entry paths when the base view shows the condition, else the candidate view's;
  "no routes" for `route_unassigned`), "renamed to …" when there are rename candidates, the suggestion
  (`_route_suggestion`: "mechanical suggestion …", or "no suggestion (ambiguous rename target, or a file
  absent at C without a rename)"), "absent without a rename: …" for `unmappedLocations`, and "answered by
  <row>" or "needs a family row (rerouted, assigned, changed or retired; never no_impact) and routes that
  satisfy MIK-R04".

- **Unexplained-change facts (MIK-R10, `_unexplained_facts`).** The path and where the change is (each hunk
  as `-<start>,<count> +<start>,<count>`, or a file change's content and status), the coverage (state,
  realization-entry count, governing route and its status), "delete-only: only no_invariant" for a
  delete-only hunk, then "answered by <row or counted-change>", or for an open item either "needs attach/author
  or a no_invariant row `hunk:…`" (covered) or "needs the onboarding trace `onboarding:<path>`" (uncovered).
  It is one pair of table entries; no branch was added to `_item_facts` (the L06 sync).

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
  column and the "Planned effects" line). A `family_route_condition` row appears only in a converted
  worklist too.

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
| Per-kind facts, dispatched by kind. | `_entry_facts`; `_item_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:41-52; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:64-68 |
| The stale and reached-family renderers, split out of the ladder. | `_stale_facts`; `_family_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:55-56; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:59-61 |
| A `family_route_condition` item's facts, its affected set and its suggestion text. | `_route_facts`; `_route_affected`; `_route_suggestion` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:144-160; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:163-168; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:171-174 |
| The kind-to-renderer table, since MIK-R10 with both unexplained kinds. | "_FACT_RENDERERS: Final["; "\"unexplained_hunk\": _unexplained_facts," | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:177-187 |
| An unexplained item's facts: where, coverage, delete-only, and what answers it. | `_unexplained_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:84-112 |
| A `planned_untouched` item's facts. | `_planned_facts` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:71-81 |
| The planned-effects block, one line per declaration. | `_planned_lines`; "Planned effects (MIK-R11)" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:115-141 |
| The section lines, the incomplete branch, the planned block and the item table with its **Plan** column. | `knowledge_worklist_lines`; "Plan" | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:194-242 |
| The ambiguous-rename checklist line: no suggestion, every candidate named. | `test_an_ambiguous_rename_target_lists_every_candidate_and_suggests_nothing` | mcp/tests/test_family_route_conditions.py:426-450 |
| The checklist and the tool show the marks. | `test_a_leaf_reads_its_declaration_and_the_checklist_and_tool_show_the_marks` | mcp/tests/test_planned_knowledge_effects.py:530-587 |
| The checklist renders it only when a worklist exists. | `knowledge_worklist`; `knowledge_worklist_lines` | mcp/src/agents_remember/memory_quality/curator_checklist.py:69-69; mcp/src/agents_remember/memory_quality/curator_checklist.py:289-289 |
| The controller renders the section and keeps the count at 0. | `test_the_memory_quality_controller_persists_the_worklist_and_renders_it_in_the_checklist` | mcp/tests/test_knowledge_worklist_leaf.py:577-669 |

## Cross-Repo References

No meaningful cross-repo references found: the module renders an in-memory document.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** The dispatch-table bullet names the two unexplained kinds; a Logic bullet for `_unexplained_facts`; one row added. **Reopened claim reworded:** the `_FACT_RENDERERS` row (the table gained two entries) is re-anchored on the line-exact quote "_FACT_RENDERERS: Final[" and names the new entry; this pass's fixer bullet for it was removed. Other rows were projected or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T02:33:21+00:00: Generated citation repair: `_route_facts`; `_route_affected`; `_route_suggestion` repointed to mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:144-160; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:163-168; mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:171-174. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **body updated for MIK-R06.** Logic records the `_FACT_RENDERERS` dispatch table (review R3-N1; the rendered text is unchanged) and the `family_route_condition` facts (`_route_facts`, `_route_affected`, `_route_suggestion`); the byte-identity boundary names the new row. Four rows added; the planned-block and section rows re-measured by hand (the code moved unevenly). The fixer's one bullet above covers `_planned_facts`, whose claim was not reworded, so it is kept. No verification stamp was advanced.
- 2026-09-29T23:15:54+00:00: Generated citation repair: `_planned_facts` repointed to mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:71-81. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Logic now records the planned-effects block (`_planned_lines`), the **Plan** column and the `planned_untouched` facts (`_planned_facts`); the byte-identity boundary notes that only converted checklists change (review R1 F4, carried to L09 by ruling 22:35:34). Three rows added, two reworded and re-measured. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
