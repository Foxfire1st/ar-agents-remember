# mcp/src/agents_remember/memory_quality/reference_state.py

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
- **One sidecar, and unreadable sidecars (L37 fix round P1b, review R3-3).** `fix_references(memory_root,
  code_root, *, dry_run=False, only=None)`: with `only` (a memory-root-relative sidecar path) no other sidecar is
  read or rewritten, which is how `citation_fix` with one `document` stays on that card. `_sidecars` names a
  sidecar that is not valid JSON in `unreadableSidecars` and skips it; a sidecar that is not shaped as one
  (`_MALFORMED`) is named the same way by `check_references` and `fix_references`. Neither raises on it: the
  knowledge validator refuses it by its own rule. An unreadable sidecar makes the fix not `ok`; the others are
  still fixed. `check_references(memory_root, code_root, *, only=None)` takes the same `only`, and `fix_references`
  passes it on, so with `only` the result's `stale` list holds that one document's stale references and nothing
  else.

### Conventions

- Sidecars are rewritten through `canonical_text`, in the MIK-R21 canonical format.

### Invariants And Boundaries

- **A stale reference is reported, never a gate finding.** The onboarding gate (MIK-R30) is the route by
  which a curator refreshes it (rule 5).
- On the real converted copy at `cd3e943d`: 34,607 current and 476 stale references in 330 sidecars. A
  fixer dry run would refresh 1,303 mechanically moved anchors and leaves the 476 stale ones.

### Todos

None recorded.

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

The format test, the anchor states, the check and the fixer.

- A tree is converted exactly when it has the layout marker. [1]
- The located bytes of a file, symbol or range locator. [2]
- An anchor's state in the working tree. [3]

- Stale references are report-only findings naming the onboarding gate. [4]
- Only mechanical moves are re-recorded; a range is re-found only when its bytes occur exactly once. [5]

- References are checked, and only mechanical moves are fixed. [6]

- The fixer can be scoped to one sidecar, and names unreadable sidecars. [7]

- A sidecar that is not valid JSON is named and skipped. [8]

- The reference check scoped to one sidecar. [9]
- One document's fix lists its own stale references. [10]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
