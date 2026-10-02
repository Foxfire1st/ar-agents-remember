# mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md

## Governing Overview

[mcp route overview](../../../../../../../overview.md)

## Purpose

**The c-05 skill's workflow for converted memory: how a curator creates and maintains a card once the memory tree
holds `knowledge/layout.json` (L37).** It replaces `file-level-onboarding-workflow.md` on converted
trees. This is the packaged copy that `runtime_install` ships; the canonical source is
`skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md`, and the harness starter
copies are generated from it by `scripts/sync-skills.py`. All copies are byte-identical.

## Code Commentary

### Logic

The workflow states, in order:

- **What a converted card is.** Two files at the mirrored path: the Markdown (title, governing overview, purpose,
  commentary, evidence) and the sidecar (references, and the `realizes` and `proves` entries). The Markdown has no
  metadata table, no Update History and no citation tables. Evidence is `- <finding> [n]` lines; `[n]` names
  `references["n"]`. Target kinds are `code`, `test`, `requirement`, `external` and `unresolved`; anchor locators
  are `symbol`, `line_range` and `file`.
- **Create a card for a new source file.** Write the Markdown with a citation table (`| Finding | Anchor |
  Source |`), then run the fixer on that one card (`memory-citations --fix --document <card>`, or `citation_fix`
  with `document`); on converted memory `--document` needs no `--expected-snapshot`. Read the `authoring` block:
  `authoredReferences`, `createdSidecars`, `unresolvedTargets`, `refused`, `unreadableSidecars`. The refusal reasons
  include two tables with no blank line between them when either is a citation table: a delimiter row (every cell
  three dashes or more) inside a table; the reason names the line, and a blank line above the second header fixes it.
- **Refresh a card after the code changed.** Prose is edited directly. One reference is re-authored by replacing
  its `- <finding> [n]` line with a one-row table whose finding ends in `[n]`; a leftover line with the same number
  refuses the card. Mechanically moved anchors are re-recorded by the same run and never count as a change.
- **Remove a reference**: delete its line and run the fixer on that card; a tree-wide run never removes one.
- **A source file moved or was deleted**: entries first, through the writer (`moved` rows with the new path, or
  covers with `remove: true`), then the card and the old sidecar, then the other cards that cite the file.
- **When the card needs no change**: an `onboarding:<path>` or `onboarding:<route>/overview` row with disposition
  `no_impact`, written through `knowledge-ingest`.
- **Never on converted memory**: a metadata table, an Update History entry, `lastVerifiedCommit*`, a citation table
  left after the fixer ran, hand-written sidecar anchors or reference numbers, and `memory_carryover_apply`.

### Conventions

- The workflow is instruction text only; the behaviour it describes is `memory/conversion/card_authoring.py` (the
  authoring), `memory_quality/reference_state.py` (the re-recording) and the writer (`knowledge-ingest`).

### Invariants And Boundaries

- **Never write sidecar JSON by hand.** The fixer authors `references`; the writer authors `realizes` and
  `proves`.
- The tree-wide fixer run re-records moved anchors across the whole tree, so a curator names one document at a
  time.
- The statement "Numbers are not reused" has one known exception: a removed highest number is reused by a later
  run.
- With a document named, the fixer's result lists that document's stale references only, and the MCP
  `citation_fix` response caps every list at 50 entries with its full count.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the L37 decisions of 2026-10-01T10:06:02 and 11:12:11 in `37_cutover-to-text-storage.json`, with `MIK-R21@v1`, `MIK-R24@v1` rule 5 and `MIK-R30@v1`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- What a converted card is, and that sidecar JSON is never written by hand. [1]

- Creating a card for a new source file: the Markdown, the citation table, one fixer run and the refusal reasons. [2]

- Refreshing a card: prose, re-authoring one reference by its number, and mechanical moves. [3]
- Removing a reference, and the moved-source and deleted-source procedures. [4]
- The no-change trace rows, and what never belongs on converted memory. [5]
- The c-05 skill routes converted memory to this workflow. [6]
- The authoring the workflow drives. [7]

- The refusal for two tables with no blank line between them. [8]

### Cross-Repo References

No meaningful cross-repo references found: the workflow is repository-local instruction text.

No cross-repo boundary is crossed by this file.
