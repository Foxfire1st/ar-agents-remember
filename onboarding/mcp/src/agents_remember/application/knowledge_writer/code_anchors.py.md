# mcp/src/agents_remember/application/knowledge_writer/code_anchors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/code_anchors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57`|
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
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
  resolve. `Holder.method` is the `method` defined inside a `Holder` definition, so a same-named method
  of another class does not make it ambiguous. Since MIK-R24 the rule itself lives in the extractor as
  `extents.qualified_spans`; `_bound_spans` only calls it with the file's `extents.definitions`, so the
  curator writer and the conversion (`memory/conversion/code_objects.py`) bind symbols through one rule.
- `line_range`: the recorded lines, which must be lines the blob holds (`RangeOutsideBlobError` becomes
  `AnchorResolutionError`).
- `file`: every byte of the blob.
- Blob bytes are read on demand and cached per blob.
- **`file_subject_mismatch` (MIK-R10).** For a `no_invariant` row with a `file:<path>@<object>` subject, it
  reads the path's tree entry at C (`git rev-parse --verify --quiet <tree>:<path>`, with the metadata timeout
  `GIT_METADATA_TIMEOUT_SECONDS` since review N5) and returns why the subject names no change at C, or
  `None`. The object is a regular file's blob, a symlink's blob or a submodule's commit; `absent` means C holds
  nothing at the path. Any other subject passes. The refusal reads "names no change at C: the code candidate
  holds … (unknown subject)".

### Conventions

- Every failure is an `AnchorResolutionError` whose message the authoring step turns into a `Problem`.

### Invariants And Boundaries

- Nothing is read from `HEAD` or any other tree: a path C does not hold does not resolve.
- The writer never guesses between definitions or accepts a mention.
- `content` is computed only through `anchor_content` (architect ruling 5: one definition).

### Todos

- Reviewer R2-1 (low, non-blocking): `file_subject_mismatch` has no unit assertion for a symlink object or an
  `@absent` subject; the reviewer verified both by a probe on a scratch repository.

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
| A locator that does not resolve at C. | `AnchorResolutionError` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:45-46 |
| The captured tree C and its blobs. | `CodeSnapshot` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:49-120 |
| A `file:` row subject must name the path's object at C, or `absent` (MIK-R10). | `file_subject_mismatch` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:85-106 |
| Capture through the private-index candidate tree. | `capture` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:58-72 |
| Resolve a locator into an anchor with blob and content. | `resolve` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:108-120 |
| A symbol must bind exactly once. | `_symbol_range` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:141-162 |
| A qualified name's last part must sit inside its parents: the writer delegates to the one shared rule. | `_bound_spans`; `qualified_spans` | mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:136-139; mcp/src/agents_remember/memory_quality/style/citations/extents.py:159-178 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** A Logic bullet for `file_subject_mismatch` (the `file:` row subject checked against C's tree entry, with the review N5 timeout), a Todo recording reviewer R2-1, one row. Other rows were projected by the installed fixer. No verification stamp was advanced.
- 2026-09-30T02:33:09+00:00: Generated citation repair: `AnchorResolutionError` repointed to mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:45-46. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:33:09+00:00: Generated citation repair: `resolve` repointed to mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:108-120. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:33:09+00:00: Generated citation repair: `_symbol_range` repointed to mcp/src/agents_remember/application/knowledge_writer/code_anchors.py:141-162. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): MIK-R24 moved the qualified-name binding rule out of `_bound_spans` into `extents.qualified_spans`, which the conversion also uses. Behaviour is unchanged. The Logic bullet now names the shared rule, and the `_bound_spans` row also cites `qualified_spans` (re-measured, which folds in the fixer projection of this pass).
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
