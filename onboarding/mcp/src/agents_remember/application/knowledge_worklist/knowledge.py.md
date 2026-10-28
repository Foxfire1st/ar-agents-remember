# mcp/src/agents_remember/application/knowledge_worklist/knowledge.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The knowledge sides K_B and K_C, read through the derived index's parser (MIK-R08 definition 7).** Each
side is one memory tree parsed by `memory.knowledge_index.parse_tree`, the MIK-R23 index builder's own
parse of the MIK-R21/R07 models. The worklist compares the two sides over those parsed relationships and
over the exact bytes of each record file.

## Code Commentary

### Logic

- `KnowledgeSide` holds a side's `label` (`K_B` or `K_C`), its tree `key`, whether it is `converted` (the
  parsed layout marker), the `ParsedTree` and the indexed files' bytes.
- `from_snapshot(label, snapshot)` parses a `MemoryTreeSnapshot`. **Any parse problem raises
  `KnowledgeSideUnreadable`**, naming every failing file (the first five in the message, then a count).
- `from_tree(label, key, tree)` builds a side from the validator's `KnowledgeTree`, retaining indexed
  JSON and their Markdown prose companions through `with_prose_companions`; the leaf uses it for
  the converted base of MIK-R24 rule 7. Markdown remains exact comparison bytes, not parsed records.
- Derived views, each sorted: `invariants` and `families` (records by ID), `entries` (realization and proof
  entries by ID, each with the source path whose sidecar holds it), `entries_by_invariant`,
  `entries_by_path`, `families_of` (each invariant's families by the families' `members`), and `linked_from`
  (each record ID that another record's `links` name, used only as context).
- `record_file(record_id)` returns the record's location and exact bytes, so "its record file differs" means
  the bytes or the location differ. `history(owner_id)` reads an owner's history file. `anchor_document(anchor,
  path)` is an entry's anchor with its source path filled in.
- `revision(record_id)` answers the stored `revision` of **any** record kind, through the derived index's
  parsed record and its document, not only for invariants and families. It answers `None` only for an
  unknown ID or a record whose `revision` is not an integer. Reading a dependent's revision is what MIK-R124
  rule 5 needs: a `None` there would skip a comparison, so a changed row could stand in for a real
  confirmation.

### Conventions

- Nothing is inferred from a name: identity is the parsed ID, and change is byte or location difference.

### Invariants And Boundaries

- **A side that does not parse whole is unreadable input.** Its index would be `partial`, and a worklist
  built over it could miss an entry, so the run is `incomplete` naming each file (MIK-R08 rule 4; the
  worker's filled-in choice, accepted by the architect).
- **In-memory comparison (architect ruling 2).** The knowledge-side comparison over the index builder's
  parse is the derived index MIK-R23 defines, used in memory; no per-side SQLite file is built, and the
  database-era `registered_scope` is not used for text trees.

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

- Sides are parsed by the index builder; a side that does not parse whole is unreadable input. [1]
- The unreadable-side error naming each failing file. [2]
- An entry's anchor with its source path. [3]
- Parsing a snapshot, refusing any problem. 

- A side from the validator's tree retains indexed JSON and unparsed Markdown companions for exact worklist comparison.

- Entries grouped by invariant and by path. [6]
- Each invariant's families by membership. [7]
- A record's file: location and exact bytes. [8]
- The `links` context. [9]
- An unparseable K_C makes the run incomplete. [10]

### Cross-Repo References

No meaningful cross-repo references found: the module parses memory trees handed to it as snapshots.

No cross-repo boundary is crossed by this file.

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/knowledge_worklist/knowledge.py:75-81 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit e40c314ca55305f7e4334b4e8e16a10297f6f175; mcp/src/agents_remember/application/knowledge_worklist/knowledge.py::from_snapshot - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
