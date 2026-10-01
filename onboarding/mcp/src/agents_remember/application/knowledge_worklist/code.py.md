# mcp/src/agents_remember/application/knowledge_worklist/code.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Hunks, ranges and content identities over the code trees B and C (MIK-R08 definitions 2 and 3).** This
module reads the zero-context hunks between two blobs of one path, maps a recorded line range onto another
blob of the same path, resolves an anchor's locator to a range in a blob, computes the range's content
identity, and finds the mechanical unique match of definition 6. Everything else in the worklist, and the
writer's carry-forward (`knowledge_writer/carry.py`), reads code through `CodeTrees`.

**Since MIK-L32 it also owns a changed path's hunks, `change_hunks` (definition 2).** It was moved verbatim out of
`compute._Run._path_hunks`, which now calls it, so the gate's linkage and the reviewer's unexplained-changes lane
(`application/review_lane_classification.py`, MIK-R32) take a path's hunks from one function and never disagree about
what a hunk is.

## Code Commentary

### Logic

- **Hunks.** `CodeTrees.hunks(old, new)` runs `git diff` on two blobs with `BLOB_DIFF_ARGS`: `--unified=0`,
  `--diff-algorithm=myers`, `--no-indent-heuristic`, `--no-ext-diff`, `--no-textconv`, `--no-color`, so the
  hunks are a function of the two blobs alone (rule 6). `parse_hunks` reads the `@@` headers into `Hunk`
  values (`old_start`, `old_count`, `new_start`, `new_count`; a missing count means 1) and returns `None`
  for a binary pair ("Binary files"), never "no change". Identical blobs give `()`, and results are cached
  per blob pair.
- **Hits.** `hits_old` and `hits_new` test one side of a hunk against a span. A side with changed lines
  hits when it overlaps the span. A side that changes nothing (a pure insertion seen from B, a pure deletion
  seen from C) hits only when it sits **strictly inside** the span, never at its edge (`_hits`).
- **Line-range mapping.** `map_range(hunks, span)` is the image of the old lines in the new blob: every
  surviving line (`_map_line` shifts it by the preceding hunks' deltas, or drops a deleted line) plus every
  line a hunk inside the range wrote. A range whose lines were all deleted with nothing written in their
  place has no image (`None`), which is "its line range has no mapping" (definition 4).
- **Resolution.** `CodeTrees.resolve(path, locator, recorded_blob, blob)` returns a `Resolved` (blob, span,
  content identity) or `None`:
  - `file`: every line, with the whole blob's content identity;
  - `symbol`: `CodeObjects.symbol_span`, the one extent the shipped extractor binds uniquely for the name
    (the rule the writer and the conversion bind with); a name bound twice or nowhere does not resolve;
  - `line_range`: the recorded lines in the anchor's own blob, otherwise mapped through the diff from the
    recorded blob (`_mapped_lines`). A recorded blob the store does not hold gives no mapping, not an error; since
    MIK-R09 a Git failure asking for it is a `CodeReadError` (below), never "not held".
  - The content identity is `content_identity(range_bytes(...))` from `models/knowledge_files/anchor_content`.
    A range outside the blob does not resolve.
- **Unique match.** `unique_binder(name)` prefilters C with `git grep -l -z -F` on the name's last segment,
  then counts, for each candidate path with a grammar, how many constructs `extents.qualified_spans` binds to
  the name. It returns a path only when exactly one path binds the name, exactly once.
- `CodeTrees.base()` and `candidate()` list each regular file of B and C with its blob.
- **A changed path's hunks (`change_hunks`, MIK-L32).** For a `TreeChange` of the landed change inventory and the
  path's blobs on B and C: `None` when the content is not text or the type changed (a non-text change, linked at file
  level, definition 8); the blob pair's hunks when both sides exist; one whole-file hunk (`Hunk(1, n, 0, 0)` or
  `Hunk(0, 0, 1, n)`) for a deleted or added text file; and `None` for an empty added or deleted file.

### Conventions

- Every read failure is a `CodeReadError` that names the tree, blob, pair or grammar; the run turns it into
  an `incomplete` worklist (MIK-R08 rule 4). A tree the store does not hold is never read as an empty tree.
- **`CodeTrees.has_blob` (MIK-R09, L09 review R3-2, ruling 2026-09-30T19:16:07).** It asks
  `CodeObjects.has_blob`, which now tells Git's documented not-found answer (`False`) from a Git failure
  (`CodeObjectError`, naming Git's stderr); the failure is re-raised as `CodeReadError`. A Git failure is therefore
  never read as a missing object: the worklist makes the run `incomplete`, and `observe_entry` marks the entry
  `read_failed`, so the gate reports an unreadable input and never memoises it.
- `CodeTrees.open(repository, base_tree, candidate_tree)` wraps one `CodeObjects` store; the writer's carry
  builds one with the same tree on both sides.

### Invariants And Boundaries

- **Deterministic diffs.** No configurable diff setting is left to the machine.
- **A binary pair is never "no change"**; it is `None`, which the classifier treats as a whole change and
  the linkage as a file-level fact.
- **One hunk definition (MIK-L32).** The gate (`compute._Run._path_hunks`) and the reviewer's lane
  (`review_lane_classification.TreeLane.classify`) both call `change_hunks`; this is part of the candidate invariant
  "the reviewer classifies changed files and hunks through MIK-R08's definitions only" recorded on
  `review_lane_classification.py.md`.
- **One symbol rule.** Symbol ranges come from the same extractor rule the writer and conversion use, so
  the worklist and the recorded anchors agree on what a name binds.

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

- The hunk, range, content-identity and hit rules. [1]
- The pinned zero-context blob diff. [2]
- One hunk and its document form. [3]
- The strict-inside rule for an empty side. [4]
- Binary pairs give `None`. [5]
- The image of a line range, or no mapping. [6]
- The hunks of a blob pair, cached, with a named failure. [7]
- Whether the store holds a blob; a Git failure is a `CodeReadError`, never absent (R3-2). [8]
- Resolution by locator kind. [9]
- A line range mapped from its recorded blob; an unknown blob has no mapping. [10]
- The mechanical unique match of definition 6. [11]
- A changed path's hunks, shared by the gate and the lane (moved from `_path_hunks`). [12]
- The two callers: the gate's linkage and the lane's classification. [13]
- Hunk parsing and line-range mapping cases. [14]
- Line ranges map, carry and touch. [15]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one local code repository's object store
through Git.

No cross-repo boundary is crossed by this file.
