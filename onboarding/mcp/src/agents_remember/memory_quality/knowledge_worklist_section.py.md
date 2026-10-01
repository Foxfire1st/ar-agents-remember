# mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py

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
    (MIK-R07) and, since MIK-R09 (leaf 260928-MIK-L09), that the mandatory gate counts each item without a
    current satisfying row as one repairable finding (check `knowledge-gate`) toward `curatorActionableCount` and
    refuses closeout while any is open, then the planned-effects block (`_planned_lines`, below),
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
  since MIK-R10 `unexplained_hunk` and `unexplained_file` → `_unexplained_facts`, and since MIK-R14
  `reconsideration_candidate` → `_reconsideration_facts`); any other kind still gets
  its sorted fact keys. The `if`/`elif` ladder it replaced rendered the same text.
- **`item_facts(item)` (MIK-R09).** The public one-line form of `_item_facts`: the gate's open-item findings quote it
  as their `Facts`, so a finding names the facts a curator acts on (MIK-R09 rule 1).
- **Onboarding-trace facts (MIK-R30 items, rendered since MIK-R09, `_trace_facts`).** The changed sources a card or
  route overview traces, "sidecar unreadable: repair it through the writer" when so, and "answered by <…>" or "needs
  a counted change of its Markdown or sidecar, or a no_impact row". Before, an `onboarding_trace` item fell back to
  its sorted fact keys.
- **Family route facts (MIK-R06, `_route_facts`).** The condition and what it affects (`_route_affected`:
  the base view's routes or entry paths when the base view shows the condition, else the candidate view's;
  "no routes" for `route_unassigned`), "renamed to …" when there are rename candidates, the suggestion
  (`_route_suggestion`: "mechanical suggestion …", or "no suggestion (ambiguous rename target, or a file
  absent at C without a rename)"), "absent without a rename: …" for `unmappedLocations`, and "answered by
  <row>" or "needs a family row (rerouted, assigned, changed or retired; never no_impact) and routes that
  satisfy MIK-R04".

- **Reconsideration facts (MIK-R14, `_reconsideration_facts`).** The alternative ("`<status>` alternative `<i>`
  '`<option>`' of `<DEC-ID>`"), each changed target with the trigger that fired ("`<target key>` (`<trigger>`)"),
  and "answered by `<row>`" or "needs a reconsideration row (still_rejected with a reason, or raise)". The facts
  never evaluate `reconsider_when` (packet Exclusions).
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

- **The section counts nothing itself.** It never enters `curatorActionableCount`, the attestation or the wire
  counts. Since MIK-R09 (L09) the mandatory gate turns every item without a current satisfying row into one
  `knowledge-gate` repair finding, which the checklist does count; the gate is live at the cutover (MIK-R37).
- **Unchanged bytes for unconverted leaves.** The checklist renders the section only when a worklist
  exists, so today's checklist is byte-identical. The MIK-R11 block and column appear only inside that
  section, so they change converted checklists only (review R1 F4: every converted checklist gains the
  column and the "Planned effects" line). A `family_route_condition` row appears only in a converted
  worklist too.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Rendering only: the section itself counts nothing, and since MIK-R09 the gate turns each open item into one `knowledge-gate` repair finding. [1]
- The section heading. [2]
- The compact wire summary. [3]
- Per-kind facts, dispatched by kind; since MIK-R09 the public one-line form the gate quotes. [4]
- The stale and reached-family renderers, split out of the ladder. [5]
- A `family_route_condition` item's facts, its affected set and its suggestion text. [6]
- The kind-to-renderer table, since MIK-R10 with both unexplained kinds. [7]
- A reconsideration item's facts: the alternative, each changed target and trigger, and what answers it; its renderer entry. [8]
- An onboarding-trace item's facts and its renderer entry (MIK-R09). [9]
- An unexplained item's facts: where, coverage, delete-only, and what answers it. [10]
- A `planned_untouched` item's facts. [11]
- The planned-effects block, one line per declaration. [12]
- The section lines, the incomplete branch, the planned block and the item table with its **Plan** column. [13]
- The ambiguous-rename checklist line: no suggestion, every candidate named. [14]
- The checklist and the tool show the marks. [15]
- The checklist renders it only when a worklist exists. [16]
- The controller renders the section; since MIK-R09 its four open items count (`curatorActionableCount` 4). [17]

### Cross-Repo References

No meaningful cross-repo references found: the module renders an in-memory document.

No cross-repo boundary is crossed by this file.
