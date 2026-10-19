# mcp/src/agents_remember/application/knowledge_reader/marks.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The two record kinds whose state is read off the code (MIK-R118, MIK-R124 rule 3).** A weakness is read
as it was written and its anchor is observed at the read's own code tree: `current` when the recorded
content still stands at the symbol, `stale` when it moved or the symbol no longer resolves, `unverifiable`
when no tree could be resolved, with the reason named. A dependent's staleness is derived on every read
and never stored: a link has moved when an anchor link's content no longer stands, when a whole-file
link's blob differs, when the file is gone, or when a record link's stored revision differs from the one
recorded. A document is stale when at least one link moved, current when none did, and unverifiable when a
link cannot be observed at all. No read writes, and no byte of a record changes when its document becomes
stale.

## Code Commentary

### Logic

- **`weakness_list`** filters by folder, by kind and by open state, and each row names the id, the file,
  the kind, the sentence, the state and, where it has one, the measurement and the closure. With
  `include_closed` unset only open weaknesses are returned.
- **`open_weakness_counts`** is the one line a card's read adds: how many open weaknesses sit on each file.
- **`dependent_movement`** is the single derivation, shared by a mounted read and by a landing: it walks
  the links in recorded order, skips the ones that still stand, and keeps the moved ones with what was
  recorded and what was observed. A record link moves in the memory tree, so its row says that no code
  commit made the change.
- **`_moving_commit` and `_anchor_moving_commit`** attribute the movement to the commit that made it. A
  commit that edits an unrelated constant in the same file is not the mover of an anchor whose bytes it
  left alone, and a commit that deleted the file is named as the mover rather than described as an
  uncommitted change. A hash is named only when that commit's recorded value is the value this read
  observed; otherwise the row says the change is uncommitted or comes from another line.
- **`_selected_commit`** accepts a tree's own commit, or HEAD only when HEAD's whole tree is the selected
  tree. A captured dirty tree, or a historical tree without its commit, is not attributed through later
  history.
- **`dependent_list`** returns all dependents, those under a folder of documents, the stale ones, or those
  that stand on a named code path, with each moved link and its attribution.
- **`dependent_counts`** is the card line for the other direction: how many documents stand on each file.

### Conventions

- Observations are cached per anchor within one read, so a file with many rows does not resolve the same
  anchor twice.
- A record its own model cannot read is the validator's finding, not a row: the list skips it rather than
  failing the read.

### Invariants And Boundaries

- **A stale anchor is marked, never refused.** A weakness whose code moved stays a readable row.
- **Staleness is derived and not stored.** No function in this module writes, and the record file is
  byte-identical before and after a document becomes stale.
- **A card's read carries a count, never the text.** The weakness sentence and the document's text stay
  out of the card line.

### Todos

- None.

## Evidence

- The two record kinds' rows and the derived state are read through the existing knowledge read tool.
