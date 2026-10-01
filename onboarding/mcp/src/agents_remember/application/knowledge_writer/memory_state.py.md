# mcp/src/agents_remember/application/knowledge_writer/memory_state.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The memory tree one writer operation reads and edits, and the base it compares against.** The
candidate K_C is every file under `knowledge/` and `onboarding/`, read once as bytes
(`knowledge_tree_from_directory`). The operation edits parsed copies of the JSON documents it touches;
nothing reaches disk until `MemoryState.write` is called with the validated result.

## Code Commentary

### Logic

- `Owner(task, kind, id)`: the task and the leaf, wave or crossing that owns the history file. A `crossing` owner
  (L37) is a master line's crossing sync: its rows go into the `<task-id>-crossing-<n>.json` file the sync opened. `origin()` is
  `{task, leaf|wave}`; `authored(document, handoff_entry)` says whether a record's or entry's origin names
  this owner and this hand-off entry (entries carry only `leaf`, so a wave's entries carry the wave ID in
  `leaf`, architect ruling 2).
- **The base** is the memory worktree's `HEAD`, or `HEAD`'s conversion when `HEAD` is unconverted and the
  candidate is converted (L37, MIK-R24 rule 7): `MemoryState.load(root, *, code=None)` takes it from
  `base_side.writer_bases`, and `code` (a `BaseCode`) names the code the conversion reads, its fallback commit
  and the shared converted-base cache. A base that cannot be built is kept as `base_problem`, and the writer
  refuses with it. The old raw-`HEAD` reader `read_base` is gone. A root that is not a Git work tree has no
  base. It answers a record's revision before this leaf (`base_record`) and an entry's anchor before this
  leaf (`base_entry_anchor`, a history row's `before`). The exact K_B resolver of MIK-R07 rule 0 is the
  gate's (MIK-R08/R09).
- `known_ids` is every record ID, minted ID, sidecar entry ID and history row ID of every history file, so
  minting never collides.
- `record_by_origin` and `entries_by_origin` find what this owner wrote from a hand-off entry, which is how
  a rerun reuses IDs.
- `put_record` keeps a record's file name unless a new slug renames it, carrying the paired `.md` along.
- `file_sidecar` creates an empty sidecar for a source file that has none.
- `write` writes each changed file through a temporary sibling and `replace`, then unlinks removed files.
- **`history_target(owner)` (L37 reopen ruling)** returns the history file the owner writes and its attempt. A
  wave or a crossing has one file. A leaf writes its latest attempt, and the next attempt once the latest is closed
  **in the base**: the leaf closed out and was reopened on a line that holds its frozen file. A file closed only
  in the candidate is still the target, and the write refuses it by name (MIK-R07 rule 7).
- **`merged_sides_revision(record_id)` (L37, MIK-R24 rule 8 step 4)** returns the higher of the two sides'
  revisions of a record a merge left unmerged, else `None`. `_unmerged_stages` reads `git ls-files -u` for the
  record's path; with stages 2 and 3 present, `_side_revisions` reads both blobs. `MergeStageError` is raised when
  Git cannot list the stages or a side names no integer revision.

### Conventions

- `deep_copy` and `canonical_equal` (sorted-key JSON equality) are the helpers `authoring.py` uses.

### Invariants And Boundaries

- A refused operation leaves every file exactly as it was, because edits live only in `documents` until
  `write`.
- The file writer writes only a converted tree: `converted` is the layout-marker test over the candidate
  files.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The candidate, the owner, the base and the write.

- Who authors the operation, and whether a document names it. [1]
- The base is the memory worktree's `HEAD`, or its conversion when the candidate is converted and `HEAD` is not; a base that cannot be built is a named problem. [2]
- Every ID the tree holds, including history row IDs. [3]
- Rerun ID reuse by origin. [4]
- A record keeps its file unless a new slug renames it. [5]
- Entries this owner wrote for an invariant from a hand-off entry. [6]
- A record as the base holds it. [7]
- An entry's anchor as the base holds it. [8]
- The atomic per-file write and the removals. [9]

- The history file an owner writes: a leaf's latest attempt, or the next once the latest is closed in the base. [10]
- The higher side's revision of a record a merge left unmerged. [11]
- A reopened leaf writes its next attempt, and its history is every file. [12]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
