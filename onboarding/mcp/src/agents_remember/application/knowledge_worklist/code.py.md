# mcp/src/agents_remember/application/knowledge_worklist/code.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

Hunks, ranges and content identities over the two code trees of a worklist run, the base tree B and the
candidate tree C. `CodeTrees` reads both trees through one object reader and answers where an anchor's
locator lands in a blob, which lines two blobs differ in, and which file of C binds a symbol name. Tree blob maps include regular files and symlink entries
(mode `120000`); a symlink blob contains link-target bytes, not the referent's contents.

## Code Commentary

- **Hunks.** `CodeTrees.hunks(old, new)` runs `git diff` with `BLOB_DIFF_ARGS` on two blobs and parses
  the zero-context hunk headers (`parse_hunks`). Equal blobs have no hunks; a binary pair answers `None`.
  A failed diff raises `CodeReadError`. Results are cached per blob pair for the run.
- **Pinned diff options.** `BLOB_DIFF_ARGS` is `diff --no-ext-diff --no-textconv --no-color
  --diff-algorithm=myers --no-indent-heuristic --unified=0 --inter-hunk-context=0 --src-prefix=a/
  --dst-prefix=b/`. The hunks are therefore a function of the two blobs alone, whatever the user's Git
  configuration says about drivers, colour, algorithm, hunk context or prefixes; the runner also clears
  `GIT_DIFF_OPTS`, because that environment context option would override even `--unified=0`.
- **Hits.** `hits_old` and `hits_new` say whether a hunk changes a line of a range on the B or the C side.
  A side on which the hunk changes nothing hits the range only when the hunk sits strictly inside it.
- **Ranges.** `CodeTrees.resolve(path, locator, recorded_blob, blob, side="candidate")` returns the range
  and its content identity. `side="base"` selects B's symlink modes; every other value selects C's.
  A symbol on a selected-side symlink raises `CodeReadError` before extraction; file and line-range
  locators still bind entry bytes. A `file` locator is every line. A `symbol` locator is the one extent the extractor binds for
  the name (`CodeObjects.symbol_span`). A `line_range` locator is the recorded lines in the recorded blob
  and, in another blob, their image through the hunks between the two blobs (`map_range`); a range all of
  whose lines were deleted, with nothing written in its place, has no image. A recorded blob the store
  does not hold gives no mapping.
- **Read-ahead.** `CodeTrees.warm(paths)` reads the blobs that the named paths have in B and in C through
  the object reader's batched `prefetch`, so the classification and hunk steps find them in the reader's
  cache and start no `git cat-file` of their own for them. A path that is in neither tree is skipped. The
  call suppresses `CodeReadError` and `CodeObjectError`: a tree or blob that cannot be read here is read
  again, and fails, at the place that uses it. `compute_worklist` calls it with the changed text paths of
  every run.
- **Other reads.** `base()` and `candidate()` map each regular file and symlink entry of a tree to its blob; a tree the store
  does not hold raises `CodeReadError`. `has_blob` turns a Git failure into `CodeReadError` and never into
  "absent". `unique_binder(name)` returns the one path of C that binds the name exactly once, found with
  `git grep` and the extractor.
- **File-level changes.** `change_hunks` returns `None` for a change that is not text or whose type
  changed, the blob diff for a path present on both sides, and one whole-file hunk for an added or
  deleted text file with at least one line.

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
- **Resolution.** `CodeTrees.resolve(path, locator, recorded_blob, blob, side="candidate")` returns a
  `Resolved` (blob, span, content identity) or `None`. `candidate_symlinks()` and `base_symlinks()`
  cache mode-`120000` path sets independently; `_side_symlinks` turns a mode-read failure into a
  `CodeReadError` naming the tree. Symbol resolution uses the selected side's set and refuses link
  bytes before the extractor; file and line-range resolution remain entry-byte bindings:
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
- `CodeTrees.base()` and `candidate()` list regular files and symlink entries of B and C with their blobs;
  links are present entries, not `absent` and not dereferenced.
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


- The pinned options of the blob diff. [16]

- Whether a hunk hits a range on one side. [17]
- Hunk headers are parsed; a binary pair has none. [18]
- The image of a line range through a diff. [19]
- The read-ahead of both sides' blobs, with read failures suppressed. [21]

- The blob diff with its failure and cache. [22]


- The one path that binds a name once. [24]

- A changed path's hunks, or none for a file-level change. [25]

- The object reader's batched prefetch. [26]

- One batch for the changed blobs, answers from the cache afterwards, and a missing tree reported where it is used. [27]

- The blob diff carries its own prefixes, colour and driver options. [28]


### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The hunk, range, content-identity and hit rules. [29]

- The pinned zero-context blob diff. [30]
- One hunk and its document form. [31]
- The strict-inside rule for an empty side. [32]
- Binary pairs give `None`. [33]
- The image of a line range, or no mapping. [34]

- The hunks of a blob pair, cached, with a named failure. [35]


- Whether the store holds a blob; a Git failure is a `CodeReadError`, never absent (R3-2). [36]

- A line range mapped from its recorded blob; an unknown blob has no mapping. [38]
- The mechanical unique match of definition 6. 
- A changed path's hunks, shared by the gate and the lane (moved from `_path_hunks`). [40]
- The two callers: the gate's linkage and the lane's classification. [41]
- Hunk parsing and line-range mapping cases. [42]
- Line ranges map, carry and touch. [43]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one local code repository's object store
through Git.

No cross-repo boundary is crossed by this file.


- The two trees, the object reader, hunk cache and independent B/C symlink-mode caches.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/knowledge_worklist/code.py:198-402 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit e40c314ca55305f7e4334b4e8e16a10297f6f175. Retired means the anchor no longer stands, not that the cited subject was deleted [20]


- Where a locator lands in a blob; selected-side symlink symbols refuse before extraction. [23]


- Resolution by locator kind and side, with cached mode reads and named symlink-symbol refusal. [37]


- Current source delta inspected statically: Fix side-aware symlink resolution/caches and entry-blob maps; retain diff and range rules. [44]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/knowledge_worklist/code.py::unique_binder - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/knowledge_worklist/code.py:198-402 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit e40c314ca55305f7e4334b4e8e16a10297f6f175. Retired means the anchor no longer stands, not that the cited subject was deleted.