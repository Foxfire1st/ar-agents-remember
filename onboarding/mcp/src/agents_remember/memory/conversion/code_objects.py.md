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
- `tree(commit)` maps each regular file of the commit's tree to its blob ID (`read_git_tree_bytes`,
  modes `100644`/`100755`).
- `prefetch(blob_ids)` reads uncached blobs in batches of 1,500 through `read_git_blobs_bytes`, and wraps
  any failure as `CodeObjectError`. `blob`, `has_blob` and `line_count` read single objects.
- **`has_blob(blob_id)` tells a missing object from a Git failure (MIK-R09, L09 review R3-2, ruling
  2026-09-30T19:16:07).** It asks `git cat-file -e` first: Git's documented not-found exit (`_GIT_NOT_FOUND`, 1, with
  no error) is `False`; for an object that exists it asks `cat-file -t` for the type (`blob` is `True`); any other
  failure raises `CodeObjectError` naming Git's stderr ("the object store cannot say whether it holds …"), and a
  timeout still raises `subprocess.TimeoutExpired`. Before, any non-zero exit read as "absent". Callers:
  `CodeTrees.has_blob` (the worklist and `observe_entry`, where the failure is a `CodeReadError`, `read_failed`,
  `incomplete` at the gate and never memoised), the reviewer's cards read (`review_tree_entries._unsupported`,
  `unavailable`), and the conversion's `legacy_db`, which now refuses on such a failure (`knowledge-convert` already
  catches `CodeObjectError`) instead of silently treating the blob as absent. This is one of L09's stated exceptions
  to "inert until the cutover": it is not behind a marker probe.
- `symbol_span(path, blob, name, *, top_level=False)` returns the one extent the extractor binds.
  Definitions are parsed once per (blob, grammar) (`extents.definitions`, then `extents.qualified_spans`),
  and a file without a grammar never binds. `top_level` is the export's reading of a recorded claim whose
  name binds more than once (a module-level `def run` and a local `run = …`): if exactly one span is nested
  in no other definition of the file (`_outermost`), that span is the claim's construct.
- `content(blob, locator, path)` is the anchor `content` for a `file`, `symbol` or `line_range` locator
  (`anchor_content.content_identity` over `range_bytes`), or `None` when it does not resolve there.

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

- The class and its caches. [1]
- A commit by exact name. [2]
- Every commit with a prefix, so ambiguity is seen. [3]
- A commit's file-to-blob map. [4]
- Git's not-found exit, and a Git failure named rather than read as absent (R3-2). [5]
- Batched blob reads. [6]
- One symbol extent per (blob, grammar); the top-level reading for recorded claims. [7]
- An anchor's content in a blob. [8]
- The shared binding rule. [9]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
