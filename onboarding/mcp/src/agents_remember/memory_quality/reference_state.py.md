# mcp/src/agents_remember/memory_quality/reference_state.py

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

**Reference currentness over sidecars, and the mechanical reference fixer (MIK-R24 rule 5).** On a
converted memory tree the citation checker and fixer work over sidecar `references` instead of citation
tables. `application/memory_tools` routes `citation_check` and `citation_fix` here. The converted reference census has its own current and stale counts. The validator's `R198.1-reference-anchor` rule refuses a non-current anchor at publication.

## Code Commentary

### Logic

- `is_converted_memory(root)` holds exactly when the tree has `knowledge/layout.json`.
- `anchor_state(path, anchor, files)` reads the code working tree:
  - `unverifiable` if a requested Lean key has uncertain scope, including on a matching blob. The report offers a line range.
  - Otherwise, `current` if the file's Git blob ID (`git_blob_id`, computed without Git) equals the anchor's `blob`,
    or if the located bytes still hash to its `content` (the MIK-R03 entry rule);
  - `stale` if the content differs;
  - `stale:unresolved` if a symbol no longer binds uniquely (`located`, through `extents.qualified_spans`)
    or a range falls outside the file;
  - `stale:path-absent` if the file is gone.
- `check_references(memory_root, code_root)` walks every sidecar with `references` (`_sidecars`, skipping
  `*.index.json`) and every `code` or `test` target (`_anchor_targets`; a file sidecar's own path fills an
  anchor without one). Non-current targets are report-only. Uncertain Lean scope has its own `unverifiable` state and line-range remedy. Stale anchors name the onboarding gate as their refresh route. The result is
  `ok` with `findingCount: 0`, and the counts are by state.
- `sidecarCount` counts successfully inspected sidecars with nonempty reference maps, including
  sidecars with only non-code targets. `states` counts the observed code and test targets by state.
  The checker skips empty maps. JSON parse and reference inspection failures appear separately in
  `unreadableSidecars`, and those sidecars contribute to neither count. Each count describes only
  the population it measures.
- `fix_references(memory_root, code_root, *, dry_run)` refreshes anchors through `refreshed_anchor`
  and `_refresh_document`. It re-records a changed blob when the existing locator finds the recorded
  bytes. If a line range moved, it re-records the lines and blob when exactly one range of the
  original length matches those bytes. It preserves notes and target lists. The working-tree check
  can report a repairable move as stale at its old lines. The strict paired-tree census identifies
  blob refreshes and unique range moves as `stale:blob` and `moved:range`. Cases that remain unresolved
  after mechanical repair, including uncertain Lean scope, require Curator judgment.
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
- `fix_references` accepts an explicit memory-relative sidecar exclusion set. The converted fixer passes cards refused by authoring through that set, so the later mechanical stage does not rewrite them. The ordinary one-document scope, stale-reference reporting and successful-sibling behavior remain separate from that no-write boundary.

### Invariants And Boundaries

- The working-tree check reports non-current references. At publication and in the full quality
  run, `R198.1-reference-anchor` requires the paired blob and matching locator content.
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
- The working-tree citation check reports an uncertain Lean key as unverifiable before considering an equal blob. [3]


- The fixer refreshes a changed blob when the locator still resolves to the recorded bytes. It re-records a moved range when exactly one range of the original length matches those bytes. Cases that remain unresolved after mechanical repair, including uncertain Lean scope, require Curator judgment. [5]



- References are checked, and only mechanical moves are fixed. Anchor: `test_references_are_checked_and_only_mechanical_moves_are_fixed` [6]


- The mechanical fixer scopes one sidecar, names unreadable sidecars, and skips the explicit authoring-refused exclusion set before refresh or write. [7]



- Only sidecars holding references are counted or observed; empty maps are skipped, malformed ones unreadable. [11]

- The named-document test checks that each fix lists only that card’s stale references. The compact reply delivers the first ten status rows with full counts and the detailed result retains the complete lists. [10]


### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.

- A stale reference is reported to the curator and refused at publication by the validator's anchor guard. [4]

- A sidecar that is not valid JSON is named and skipped. [8]
- The reference check scoped to one sidecar. [9]
