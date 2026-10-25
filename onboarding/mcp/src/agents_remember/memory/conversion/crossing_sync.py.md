# mcp/src/agents_remember/memory/conversion/crossing_sync.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Plans a converted/unconverted memory crossing from the actual three input trees before the transaction applies it.

## Code Commentary

`cross` classifies the three sides by their markers. Three converted sides use structural merge without a conversion; mixed sides use pinned conversion and marker/history ownership before merge and validation. Three unconverted sides do not enter this crossing route. The plan carries files, conflicts and counts; since MIK-R66 its result also carries the alignment counts (aligned cards, renumbered references, kept evidence lines, skipped cards). The transaction owner applies and stages it. The removed is_crossing helper is not a current classifier or alternate writer. This module's plan is not an acceptance or a grant to mutate a repository.

### Logic

- `_pinned_version` refuses an all-unconverted merge or converted sides that do not share exactly one
  version. Three converted sides sharing one version remain eligible for structural merge without conversion.

- **Step 1, markers first.** For a leaf owner whose own tree is unconverted,
  `marker_rows(base, own, *, code_blobs)`
  collects the Update History lines that leaf added (`kernel/onboarding_doc.new_history_lines`) matching
  the no-impact marker pattern. Each card with such lines becomes one `onboarding_trace` row:
  - `subject`: `onboarding:<path>`, `onboarding:<route>/overview`, or `onboarding:overview`;
  - `disposition`: `no_impact`;
  - `reason`: the fixed `MARKER_ROW_REASON`;
  - `markers`: one entry per marker line (architect ruling N1). `marker_pieces` splits a line longer than
    the text limit into consecutive pieces at the limit, deterministically and losslessly;
  - `sources`: `_marker_sources` binds the own side's paired code commit. A file card records its
    source blob or `absent`; an overview records every tracked file beneath its route (all tracked
    files for the root overview). This is historical marker provenance, not an exact answer to a
    future changed-source set: the future gate compares only changed files and the row must be judged
    again there;
  - `items`: `[]`, and a minted `ROW-` ID.

  `cross` reads `objects.tree(own_paired_commit)` before conversion and passes it as `code_blobs`.
  Any paired-code read exception raises `CrossingError` with step `markers`; it cannot silently
  convert with unbound provenance.

  `with_markers` adds the rows to the leaf's history file after the own side is converted. A subject that
  already has a row is not moved: the authored row is left alone, and the marker is returned as
  `markersNotMoved` for the report, never dropped silently (review R1 finding 9).
- **Step 2, convert** every tree with the pinned version, and the own side's paired code commit for
  fallback cards (`_convert_sides`). A converted tree converts to itself.
- **Step 3, merge** (`crossing.merge_trees`).
- **Step 4, conflicts.** They are returned with their converted base, own and incoming bytes. The report
  names `recordConflictHistoryOwner`: the leaf's own ID, or on a master line `next_crossing_owner`, the
  `<task-id>-crossing-<n>` one past any existing crossing file of the task on any side. For a master line
  with a conflicted record, the plan also opens that history file (`{crossing, closed: false, rows: []}`).
  `worktrees/knowledge_crossing.close_crossing_history` closes it in the merge commit. The row itself is
  the curator's, written while resolving the record conflict.
- **Step 5, validate**, is enforced where the merge is committed, not here. The managed sync's commit step
  runs `memory_commit_refusal` over the staged merge, with `GitBaseConverter` replacing the unconverted
  parent (review R1 finding 7).
- The report holds the version, the converted sides, marker rows moved and not moved, files taken per
  side, cards per side (`_card_counts`: unchanged, from own, from incoming, merged cleanly, conflicted)
  and every conflict.

### Conventions

- `HistoryOwner` is `{kind: leaf | master, id}`. The managed sync passes the leaf, or the master line's
  task ID.

### Invariants And Boundaries

- **A crossing conflict is never committed silently:** every conflicted path goes back to the curator
  with its three converted versions.
- **The markers list carries the moved text in full.** On the real ONT fork, 15 rows carry 97 marker
  entries (81 of them for one card, `test-evidence-lanes.toml`), the longest 376 characters, and the history
  file validates. A single `reason` would have held 29,351 characters, over the 20,000-character limit
  (review R2, N1).
- Rule 2 fallback cards use the own side's code tree on every side, which differs from
  `GitBaseConverter` (see `base.py`).

### Todos

None recorded. L37 corrected the module docstring's step 1: the marker text goes in `markers`, one entry per
moved line, and `reason` is the fixed summary `MARKER_ROW_REASON` (ruling N1). It was a docstring change only.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The crossing result carries the alignment counts beside conflicts and cards. [14]


- `_convert_sides` owns the current boundary described above. [12]
- `next_crossing_owner` owns the current boundary described above. [13]

The steps and their helpers.

- - A step failure names the step. [15]
- - The pinned version refuses all-unconverted inputs or version disagreement; all-converted inputs sharing one version remain eligible. [16]
- - Markers go into the leaf's history file; a subject with a row is reported, not dropped. [18]
- - The master-line crossing history file's name. [19]
- - Cards counted by side. [21]

- - The markers move, each side converts, and the trees merge. [22]


- - Many long markers fit one valid row. [23]

- - A master-line record conflict opens a crossing history file, closed at commit. [24]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.

- - Step 1: the leaf's added no-impact markers become onboarding_trace rows, with full text in `markers` and sources bound to the own side's paired code commit; file and overview provenance have different source sets. [17]
- - Steps 1-4 and the report: paired-code blobs are read before marker conversion; unreadable paired code raises the named `markers` failure rather than dropping source provenance. [20]
- Current source delta inspected statically: Require paired-code marker provenance, distinguish overview history from future changed sets, and name fail-closed markers-step errors. [25]
