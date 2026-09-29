# mcp/src/agents_remember/memory/conversion/code_objects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/code_objects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

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

### Todos

The `top_level` reading is accepted by the architect (ruling 5) for the one real claim it applies to,
`cli/knowledge_bootstrap.py::run`, which the report lists. MIK-R03 still reads that claim as a
non-unique symbol, that is, stale.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The object store's read-only surface.

| Finding | Anchor | Source |
| --- | --- | --- |
| The class and its caches. | `CodeObjects` | mcp/src/agents_remember/memory/conversion/code_objects.py:46-205 |
| A commit by exact name. | `commit` | mcp/src/agents_remember/memory/conversion/code_objects.py:61-72 |
| Every commit with a prefix, so ambiguity is seen. | `commits_with_prefix` | mcp/src/agents_remember/memory/conversion/code_objects.py:74-104 |
| A commit's file-to-blob map. | `tree` | mcp/src/agents_remember/memory/conversion/code_objects.py:106-119 |
| Batched blob reads. | `prefetch`; `CodeObjectError` | mcp/src/agents_remember/memory/conversion/code_objects.py:121-131; mcp/src/agents_remember/memory/conversion/code_objects.py:42-43 |
| One symbol extent per (blob, grammar); the top-level reading for recorded claims. | `symbol_span`; `_outermost` | mcp/src/agents_remember/memory/conversion/code_objects.py:150-176; mcp/src/agents_remember/memory/conversion/code_objects.py:208-220 |
| An anchor's content in a blob. | `content` | mcp/src/agents_remember/memory/conversion/code_objects.py:181-205 |
| The shared binding rule. | `qualified_spans` | mcp/src/agents_remember/memory_quality/style/citations/extents.py:159-178 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
