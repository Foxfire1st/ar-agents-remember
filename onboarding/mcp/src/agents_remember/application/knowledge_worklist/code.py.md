# mcp/src/agents_remember/application/knowledge_worklist/code.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/code.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Hunks, ranges and content identities over the code trees B and C (MIK-R08 definitions 2 and 3).** This
module reads the zero-context hunks between two blobs of one path, maps a recorded line range onto another
blob of the same path, resolves an anchor's locator to a range in a blob, computes the range's content
identity, and finds the mechanical unique match of definition 6. Everything else in the worklist, and the
writer's carry-forward (`knowledge_writer/carry.py`), reads code through `CodeTrees`.

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
    recorded blob (`_mapped_lines`). A recorded blob the store does not hold gives no mapping, not an error.
  - The content identity is `content_identity(range_bytes(...))` from `models/knowledge_files/anchor_content`.
    A range outside the blob does not resolve.
- **Unique match.** `unique_binder(name)` prefilters C with `git grep -l -z -F` on the name's last segment,
  then counts, for each candidate path with a grammar, how many constructs `extents.qualified_spans` binds to
  the name. It returns a path only when exactly one path binds the name, exactly once.
- `CodeTrees.base()` and `candidate()` list each regular file of B and C with its blob.

### Conventions

- Every read failure is a `CodeReadError` that names the tree, blob, pair or grammar; the run turns it into
  an `incomplete` worklist (MIK-R08 rule 4). A tree the store does not hold is never read as an empty tree.
- `CodeTrees.open(repository, base_tree, candidate_tree)` wraps one `CodeObjects` store; the writer's carry
  builds one with the same tree on both sides.

### Invariants And Boundaries

- **Deterministic diffs.** No configurable diff setting is left to the machine.
- **A binary pair is never "no change"**; it is `None`, which the classifier treats as a whole change and
  the linkage as a file-level fact.
- **One symbol rule.** Symbol ranges come from the same extractor rule the writer and conversion use, so
  the worklist and the recorded anchors agree on what a name binds.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The hunk, range, content-identity and hit rules. | "never when it sits at the range's edge" | mcp/src/agents_remember/application/knowledge_worklist/code.py:1-25 |
| The pinned zero-context blob diff. | `BLOB_DIFF_ARGS` | mcp/src/agents_remember/application/knowledge_worklist/code.py:65-73 |
| One hunk and its document form. | `Hunk` | mcp/src/agents_remember/application/knowledge_worklist/code.py:84-101 |
| The strict-inside rule for an empty side. | `_hits`; `hits_old`; `hits_new` | mcp/src/agents_remember/application/knowledge_worklist/code.py:104-108; mcp/src/agents_remember/application/knowledge_worklist/code.py:111-114; mcp/src/agents_remember/application/knowledge_worklist/code.py:117-120 |
| Binary pairs give `None`. | `parse_hunks` | mcp/src/agents_remember/application/knowledge_worklist/code.py:123-142 |
| The image of a line range, or no mapping. | `_map_line`; `map_range` | mcp/src/agents_remember/application/knowledge_worklist/code.py:145-158; mcp/src/agents_remember/application/knowledge_worklist/code.py:161-176 |
| The hunks of a blob pair, cached, with a named failure. | `hunks` | mcp/src/agents_remember/application/knowledge_worklist/code.py:224-242 |
| Resolution by locator kind. | `resolve`; `symbol_span` | mcp/src/agents_remember/application/knowledge_worklist/code.py:247-268 |
| A line range mapped from its recorded blob; an unknown blob has no mapping. | `_mapped_lines` | mcp/src/agents_remember/application/knowledge_worklist/code.py:270-279 |
| The mechanical unique match of definition 6. | `unique_binder`; `qualified_spans` | mcp/src/agents_remember/application/knowledge_worklist/code.py:290-332 |
| Hunk parsing and line-range mapping cases. | `test_hunks_parse_and_line_ranges_map_through_the_zero_context_diff` | mcp/tests/test_knowledge_worklist.py:300-319 |
| Line ranges map, carry and touch. | `test_line_ranges_map_carry_and_touch` | mcp/tests/test_knowledge_worklist.py:411-420 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one local code repository's object store
through Git.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
