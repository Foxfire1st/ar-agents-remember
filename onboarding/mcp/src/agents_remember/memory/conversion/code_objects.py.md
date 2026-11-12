# mcp/src/agents_remember/memory/conversion/code_objects.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The only door to the code objects a conversion resolves in (MIK-R24 rules 2 and 6).** `CodeObjects`
reads commits, trees and blobs from one code repository's object store by exact identity, never from a
working tree, so the same objects give the same answer on every machine and every line. It binds symbols
through the shipped extractor.

## Code Commentary

### Logic

- `commit(name)` returns the full commit ID `rev-parse --verify <name>^{commit}` resolves, or `None`
  (cached).
- `commits_with_prefix(prefix)` lists **every** object whose ID starts with the prefix
  (`rev-parse --disambiguate`) and keeps the commits (`cat-file --batch-check`). An abbreviated commit is
  therefore seen as ambiguous as the store grows, never silently read as missing (review R1 finding 3).
- `tree(commit)` maps regular files (`100644`/`100755`) and symlinks (`120000`) to their entry blobs. Cached tree modes, `tree_modes` and `link_paths` preserve mode identity; an extant link has target-text bytes, not absence or its referent contents. Symbol resolution receives the selected tree's symlink set and rejects a named link before extraction; file/line-range locators still read entry bytes.

- `tree_entry_mode(tree, path)` observes the exact raw candidate entry with bounded, nonrecursive `git ls-tree -z <tree> -- <path>`. Unlike recursive leaf inventory it sees an empty tree or a tree of empty subtrees. It returns the mode or `None` for true absence; a failed Git read raises `CodeObjectError`. Generated-copy declaration admission uses this observation before filtered blob lookup; the shared recursive inventory remains leaf-oriented.



- Tree inventory and mode snapshots retain symlink entry blobs, with link_paths supplying explicit symbol-extraction context.



- Symbol and content locators use explicit symlink context.

- `prefetch(blob_ids)` reads uncached blobs in batches of 1,500 through `read_git_blobs_bytes`, and wraps
  any failure as `CodeObjectError`. `blob` and `has_blob` read single objects; `line_count` reuses the instance's blob-keyed split-line representation.
- **`has_blob(blob_id)` tells a missing object from a Git failure (MIK-R09, L09 review R3-2, ruling
  2026-09-30T19:16:07).** An already cached blob returns `True`; for uncached objects it asks `git cat-file -e` first: Git's documented not-found exit (`_GIT_NOT_FOUND`, 1, with
  no error) is `False`; for an object that exists it asks `cat-file -t` for the type (`blob` is `True`); any other
  failure raises `CodeObjectError` naming Git's stderr ("the object store cannot say whether it holds …"), and a
  timeout still raises `subprocess.TimeoutExpired`. Before, any non-zero exit read as "absent". Callers:
  `CodeTrees.has_blob` (the worklist and `observe_entry`, where the failure is a `CodeReadError`, `read_failed`,
  `incomplete` at the gate and never memoised), the reviewer's cards read (`review_tree_entries._unsupported`,
  `unavailable`), and the conversion's `legacy_db`, which now refuses on such a failure (`knowledge-convert` already
  catches `CodeObjectError`) instead of silently treating the blob as absent. This is one of L09's stated exceptions
  to "inert until the cutover": it is not behind a marker probe.
- `symbol_span(path, blob, name, *, top_level=False)` returns the one extent the extractor binds.
  Definitions are parsed once per (blob, grammar, path) (`extents.definitions`, then `extents.qualified_spans`), so filename-dependent test-case eligibility cannot leak between paths sharing a blob.
  A file without a grammar never binds. `top_level` is the export's reading of a recorded claim whose
  name binds more than once (a module-level `def run` and a local `run = …`): if exactly one span is nested
  in no other definition of the file (`_outermost`), that span is the claim's construct.
- `content(blob, locator, path)` is the anchor `content` for a `file`, `symbol` or `line_range` locator
  (`anchor_content.content_identity` over `range_from_lines` for a resolved range), or `None` when it does not resolve there. Whole-file content hashes the original blob without splitting it.
- `_blob_lines` keeps the LF-only byte lines once per blob ID per `CodeObjects` instance. Repeated line counts and symbol/range content requests reuse those same lines across source paths. This is instance-local conversion reuse, not a persistent parsed-file store or a worklist/verdict cache.
- The raw blob in `_blobs` and its split representation in `_lines` coexist for the instance lifetime. The split byte values, list and per-line objects add memory cost; the incremental cost and final-cut peak/RSS are unmeasured. No memory reduction or 1 GB claim follows from this optimization.

### Conventions

- Every Git call goes through the kernel runner with the metadata timeout.

### Invariants And Boundaries

- **The extractor is pinned by the conversion-format version.** A change to `qualified_spans`,
  `extents.definitions` or a grammar that alters conversion output must ship as a new version (see
  `convert.py`).
- A missing grammar is a `CodeObjectError`, never a silent `line_range` fallback.
- **A Git failure is never read as a missing object** (`has_blob`, since MIK-R09). Proved by
  `test_a_recorded_blob_the_store_lacks_is_named_at_its_real_raise_site` (a missing blob: the worklist stays complete
  and the item names it) and `test_a_git_failure_asking_for_a_recorded_blob_is_incomplete_and_never_kept`
  (`cat-file -e` exits 128: incomplete, never kept), in `test_knowledge_gate_routes.py`.

### Todos

The `top_level` reading is accepted by the architect (ruling 5) for the one real claim it applies to,
`cli/knowledge_bootstrap.py::run`, which the report lists. MIK-R03 still reads that claim as a
non-unique symbol, that is, stale.

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

The object store's read-only surface.


- The read-only class retains raw blobs and instance-local blob-keyed split lines; no persistent worklist is stored. 



- A commit by exact name. [2]


- Every commit with a prefix, so ambiguity is seen. [3]



- A commit's regular-file and symlink blob map remains read-only and mode-aware. [4]



- Git's not-found exit, and a Git failure named rather than read as absent (R3-2).

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory/conversion/code_objects.py:176-201 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 8b0254263c6998b1d4814b2e97c1bd231d39350f. Retired means the anchor no longer stands, not that the cited subject was deleted [5]


- Batched blob reads. [6]

- Symbol extraction is cached by blob, grammar and path, preserves the selected symlink context, and supports the explicit top-level reading for recorded claims.

- Exact nonrecursive entry-mode observation distinguishes present empty trees from absence without broadening recursive source inventory. [12]


- Whole-file content hashes the blob; symbol and line-range content reuse the instance's split lines through the inclusive-range helper. [8]


- The shared binding rule preserves qualified symbol extents and unique binding. [9]


### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.


Anchor: `CodeObjects` [1]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory/conversion/code_objects.py:219-260 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 8b0254263c6998b1d4814b2e97c1bd231d39350f; mcp/src/agents_remember/memory/conversion/code_objects.py:203-244 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c052b2593b85d9baf425cc1d5c46f384b13fc9ea; mcp/src/agents_remember/memory/conversion/code_objects.py::CodeObjects - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/memory/conversion/code_objects.py:176-201 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 8b0254263c6998b1d4814b2e97c1bd231d39350f. Retired means the anchor no longer stands, not that the cited subject was deleted.