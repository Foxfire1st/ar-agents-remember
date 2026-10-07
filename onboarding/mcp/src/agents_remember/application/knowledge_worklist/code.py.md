# mcp/src/agents_remember/application/knowledge_worklist/code.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

Hunks, ranges and content identities over the two code trees of a worklist run, the base tree B and the
candidate tree C. `CodeTrees` reads both trees through one object reader and answers where an anchor's
locator lands in a blob, which lines two blobs differ in, and which file of C binds a symbol name.

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
- **Ranges.** `CodeTrees.resolve(path, locator, recorded_blob, blob)` returns the range and its content
  identity. A `file` locator is every line. A `symbol` locator is the one extent the extractor binds for
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
- **Other reads.** `base()` and `candidate()` map each regular file of a tree to its blob; a tree the store
  does not hold raises `CodeReadError`. `has_blob` turns a Git failure into `CodeReadError` and never into
  "absent". `unique_binder(name)` returns the one path of C that binds the name exactly once, found with
  `git grep` and the extractor.
- **File-level changes.** `change_hunks` returns `None` for a change that is not text or whose type
  changed, the blob diff for a path present on both sides, and one whole-file hunk for an added or
  deleted text file with at least one line.

## Evidence

- The pinned options of the blob diff. [16]
- Whether a hunk hits a range on one side. [17]
- Hunk headers are parsed; a binary pair has none. [18]
- The image of a line range through a diff. [19]
- The two trees, the object reader and the hunk cache. [20]
- The read-ahead of both sides' blobs, with read failures suppressed. [21]
- The blob diff with its failure and cache. [22]
- Where a locator lands in a blob. [23]
- The one path that binds a name once. [24]
- A changed path's hunks, or none for a file-level change. [25]
- The object reader's batched prefetch. [26]
- One batch for the changed blobs, answers from the cache afterwards, and a missing tree reported where it is used. [27]
- The blob diff carries its own prefixes, colour and driver options. [28]
