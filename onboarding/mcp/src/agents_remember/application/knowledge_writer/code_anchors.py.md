# mcp/src/agents_remember/application/knowledge_writer/code_anchors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/code_anchors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Anchor resolution at the leaf's code candidate tree C (MIK-R12 rule 2, MIK-R07 rule 0).**
`CodeSnapshot.capture` captures the code worktree, committed and uncommitted, as a tree through the shipped
private-index capture (`worktrees/modules/git.worktree_candidate_tree`) and lists every regular file's blob.
`CodeSnapshot.resolve` turns a locator into an `Anchor{locator, blob, content}`, hashing the located bytes
through `models/knowledge_files/anchor_content.py`.

## Code Commentary

### Logic

- `symbol`: the one extent the shipped citation extractor (`memory_quality/style/citations/extents`) binds
  for the name. A name bound nowhere, bound more than once, or in a language with no grammar does not
  resolve. `Holder.method` is the `method` defined inside a `Holder` definition (`_bound_spans`), so a
  same-named method of another class does not make it ambiguous.
- `line_range`: the recorded lines, which must be lines the blob holds (`RangeOutsideBlobError` becomes
  `AnchorResolutionError`).
- `file`: every byte of the blob.
- Blob bytes are read on demand and cached per blob.

### Conventions

- Every failure is an `AnchorResolutionError` whose message the authoring step turns into a `Problem`.

### Invariants And Boundaries

- Nothing is read from `HEAD` or any other tree: a path C does not hold does not resolve.
- The writer never guesses between definitions or accepts a mention.
- `content` is computed only through `anchor_content` (architect ruling 5: one definition).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

Capture and resolution.

| Finding | Anchor | Source |
| --- | --- | --- |
| A locator that does not resolve at C. | `AnchorResolutionError` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:39-40 |
| The captured tree C and its blobs. | `CodeSnapshot` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:43-91 |
| Capture through the private-index candidate tree. | `capture` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:52-66 |
| Resolve a locator into an anchor with blob and content. | `resolve` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:79-91 |
| A symbol must bind exactly once. | `_symbol_range` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:112-133 |
| A qualified name's last part must sit inside its parents. | `_bound_spans` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:136-155 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
