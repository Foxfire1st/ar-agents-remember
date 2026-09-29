# mcp/src/agents_remember/memory_quality/reference_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/reference_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

**Reference currentness over sidecars, and the mechanical reference fixer (MIK-R24 rule 5).** On a
converted memory tree the citation checker and fixer work over sidecar `references` instead of citation
tables. `application/memory_tools` routes `citation_check` and `citation_fix` here, and the memory-quality
run's converted check reports the same states.

## Code Commentary

### Logic

- `is_converted_memory(root)` holds exactly when the tree has `knowledge/layout.json`.
- `anchor_state(path, anchor, files)` reads the code working tree:
  - `current` if the file's Git blob ID (`git_blob_id`, computed without Git) equals the anchor's `blob`,
    or if the located bytes still hash to its `content` (the MIK-R03 entry rule);
  - `stale` if the content differs;
  - `stale:unresolved` if a symbol no longer binds uniquely (`located`, through `extents.qualified_spans`)
    or a range falls outside the file;
  - `stale:path-absent` if the file is gone.
- `check_references(memory_root, code_root)` walks every sidecar with `references` (`_sidecars`, skipping
  `*.index.json`) and every `code` or `test` target (`_anchor_targets`; a file sidecar's own path fills an
  anchor without one). Every non-current target is returned as a **report-only** finding
  `knowledge.references.stale`, naming the onboarding gate (MIK-R30) as the refresh route. The result is
  `ok` with `findingCount: 0`, and the counts are by state.
- `fix_references(memory_root, code_root, *, dry_run)` re-records only **mechanical** moves
  (`_refreshed`, `_refresh_document`):
  - an anchor whose located content is unchanged but whose blob moved gets the new blob;
  - a `line_range` whose exact bytes now occur exactly once elsewhere gets the new lines and blob.

  It never touches a stale anchor, a note or a target list, and it returns the remaining stale findings.

### Conventions

- Sidecars are rewritten through `canonical_text`, in the MIK-R21 canonical format.

### Invariants And Boundaries

- **A stale reference is reported, never a gate finding.** The onboarding gate (MIK-R30) is the route by
  which a curator refreshes it (rule 5).
- On the real converted copy at `cd3e943d`: 34,607 current and 476 stale references in 330 sidecars. A
  fixer dry run would refresh 1,303 mechanically moved anchors and leaves the 476 stale ones.

### Todos

None recorded.

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

The format test, the anchor states, the check and the fixer.

| Finding | Anchor | Source |
| --- | --- | --- |
| A tree is converted exactly when it has the layout marker. | `is_converted_memory` | mcp/src/agents_remember/memory_quality/reference_state.py:40-43 |
| The located bytes of a file, symbol or range locator. | `located` | mcp/src/agents_remember/memory_quality/reference_state.py:72-88 |
| An anchor's state in the working tree. | `anchor_state`; `git_blob_id` | mcp/src/agents_remember/memory_quality/reference_state.py:91-100; mcp/src/agents_remember/memory_quality/reference_state.py:46-49 |
| Stale references are report-only findings naming the onboarding gate. | `check_references`; `STALE_REFERENCE_CHECK` | mcp/src/agents_remember/memory_quality/reference_state.py:125-157; mcp/src/agents_remember/memory_quality/reference_state.py:36-36 |
| Only mechanical moves are re-recorded; a range is re-found only when its bytes occur exactly once. | `_refreshed`; `fix_references` | mcp/src/agents_remember/memory_quality/reference_state.py:160-184; mcp/src/agents_remember/memory_quality/reference_state.py:207-227 |
| References are checked, and only mechanical moves are fixed. | `test_references_are_checked_and_only_mechanical_moves_are_fixed` | mcp/tests/test_knowledge_conversion_toolchain.py:87-115 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
