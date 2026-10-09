# mcp/src/agents_remember/memory/conversion/crossing.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The structural three-way merge of a crossing sync (MIK-R24 rule 8 steps 3 and 4), with reference-number
alignment first (MIK-R66).** Once every unconverted side is converted, the three converted trees merge file
by file. A card both sides changed has its reference numbers aligned before the merge when it is eligible under rule 7, so numbering shifts no longer conflict for aligned cards. A rule-7-skipped card merges without alignment exactly as before with its reason recorded, and a true authored conflict stays one item at the incoming number. Markdown merges by line, sidecars and records by key, and mechanical anchor fields never
cause a conflict.

## Code Commentary

### Logic

- `merge_trees(base, ours, theirs, *, repository)` goes path by path. A card both sides changed is aligned
  first (`_align_cards`): its reference numbers are paired and remapped, and own's and the base's Markdown
  markers move with the same map. Then the merge runs as before: a file only one side changed is taken from
  that side (a deletion included, counted `own`, `incoming` or `same`). A JSON file both sides changed is
  merged by key (`_merge_json_file`), and any other file three-way by line (`_merge_text_file`, through
  `kernel/git_command.merge_file_bytes`). A text file deleted on one side and changed on the other
  is a `(file)` conflict.
- **Alignment (`_align_card`).** Base pairs with incoming and base with own, each by unique content (a),
  then same number (b), then the singleton between the same two paired neighbours (c); partnerless own and
  incoming pair by content only. Incoming keeps every number; a base or own reference with an incoming partner
  takes the partner's number; every other group takes one fresh number above all three sides' highest, own's
  groups first in own order, then base-only groups in base order. The maps are verified injective per side.
  The merge is a pure function of the three trees: two runs give the same bytes.
- **No guessing.** The card merges without alignment, exactly as before, when the pairing would give one
  number to two references of a side, or when a side that would be renumbered has a marker without a
  reference or a reference without a marker. The reason is recorded for the report.
- **Evidence lines both sides added.** A conflict region with an empty base part whose differing lines are
  all real trailing-marker evidence lines is not a conflict: incoming's lines are kept first, then own's,
  judged per side in that side's full-document grammar with shared context kept once.
- **Keys (`_merge_json`, `_merge_collection`).** `references` merge by aligned number, `realizes` and `proves` by
  entry `id`, and every other field by name.
- **Items (`merge_item`).** A reference, an entry or a record field is one item. Its mechanical fields are
  an anchor's `blob`, `content` and line numbers (`authored` strips them), and everything else is authored.
  - An item only one side changed is taken from that side, whole.
  - If one side changed authored fields and the other only mechanical ones, the authored side's item is
    taken, whole.
  - If both sides changed only mechanical fields, the incoming side's item is taken.
  - An item deleted on one side and changed only mechanically on the other is deleted.
  - Authored fields changed differently on both sides are a **conflict**. So is an item added on both
    sides with different authored content. A reference both lines really changed differently is still one
    conflict item, at the incoming number. The old `renumber one side` reason survives only for a card that
    merged without alignment under rule 7.
- **Conflict markers (`CONFLICT_MARKER`, `_conflicted`).** A conflicted JSON item, or a whole JSON file,
  is written as an explicit `{"crossing-conflict": {item, reason, base, own, incoming}}` marker. No
  knowledge-file model admits that key, so the validator refuses the file until the curator replaces the
  marker. Markdown conflicts keep Git's conflict hunks.
- `Conflict.to_document` gives each conflict's path, item, reason and the three sides' values for the
  crossing report.

### Conventions

- Merged JSON is written in the canonical format (`canonical_text`).

### Invariants And Boundaries

- **Mechanical anchor fields never conflict in a crossing** (rule 8 step 3).
- **A conflicted item is never committed as a silent "ours"** (review R1 finding 1, resolved by the
  markers).
- **An aligned both-changed card conflicts only where both lines changed the same reference or the same prose
  (MIK-R66).** Numbering shifts from inserted rows pair by content and take the incoming number; only new
  references take fresh numbers. A card skipped under rule 7 is not aligned: it merges by the pre-R66 rules with its reason recorded, and a true authored conflict stays one item at the incoming number. Before MIK-R66 the same merge reported a conflict item for every reference
  after an inserted row (on the real ONT fork, 615 items in 32 cards, 503 of them renumbering effects).
- **No anchor is re-resolved.** Staleness is reported later by MIK-R03 wherever the knowledge is read.
- An aligned merged card passes the validator's marker rule (`R22.3-markers`): every marker has its reference and
  every reference its marker. A rule-7-skipped card keeps the legacy merge, whose references.2 renumber conflict the marker-incomplete witness retains.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`), the requirement packet `MIK-R66@v1` of the same task (with the
owner cold interpretation and erratum in the leaf document
`66_the-structural-merge-aligns-reference-numbers.json`), and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The alignment, the merge, and the report counts.

- One card's numbers are paired, allocated, and its prose remapped, or the card merges as today with its reason. [9]
- Pairing runs unique content, then same number, then the singleton gap, each at most once. [10]
- Gap intervals count and locate live numbers in a Fenwick index instead of scanning paired populations. [11]
- Partnerless own and incoming pair by unique content only. [12]
- Incoming-kept numbers, partner numbers, then fresh numbers above every maximum in own-then-base order. [13]
- A non-injective map fails the card closed into a rule-7 skip. [14]
- A side that would be renumbered but holds a marker without a reference, or the reverse, skips with its reason. [15]
- Empty-base regions of only real trailing-marker evidence lines resolve incoming-first, then own. [16]
- References merge by aligned number, entries by id, fields by name. [17]
- Authored beats mechanical; a doubly-changed reference stays one item at the incoming number. [18]
- The explicit conflict marker the validator refuses. [19]
- The report counts aligned cards, renumbered references, kept evidence lines, and skipped cards. [20]
- The prose remap moves exactly the markers the shared grammar reports. [21]

- Both sides added one reference each: alignment gives each its number, no conflict. [22]
- A reference both lines changed differently stays one item at the incoming number. [23]
- Evidence lines both sides added are kept incoming-first, then own. [24]
- The same three trees merge to identical bytes twice. [25]
- Fresh numbers follow own order, then base order, above every maximum. [26]
- A repeated number refuses alignment instead of writing duplicates. [27]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
