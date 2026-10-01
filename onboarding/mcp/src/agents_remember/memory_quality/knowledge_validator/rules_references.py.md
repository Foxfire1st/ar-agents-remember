# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R22's cross-file rules: markers and references, record links, relations, unresolved targets, family members, and anchor paths.** Importing the module registers its eight rules in `REFERENCE_RULES`, three of them report-only. None of these rules reads a history file.

## Code Commentary

### Logic

- `R22.3-markers` (`check_markers`): every marker of an onboarding Markdown file has a reference in its sidecar, and every reference is used. Markdown without a sidecar (a record's Markdown included) holds no markers. A file sidecar without Markdown holds no references, and a route sidecar must sit beside its `overview.md`. When the paired sidecar exists but does not parse, the Markdown is skipped, because its shape violation is reported instead.
- `R22.3-sidecar-without-markdown` (**report-only**): the file sidecar itself is reported (MIK-R21 rule 5).
- `R22.3-record-links`: every ID a sidecar reference target, an entry's `invariant`, a record's `supersedes` or a record link target names must exist in `record_ids`; route targets are exempt, and a retired record still resolves.
- `R22.3-relations`: the `relation` problems found while parsing.
- `R22.3-unresolved-target` (**report-only**): each `unresolved` target.
- `R22.5-family-members`: every family member exists; the route rules are left to MIK-R04.
- `R22.6-anchor-path`: an anchor with no equal counterpart in any base must name a file in the paired code tree. For an entry the counterpart is the same entry ID; for a reference target, the same sidecar path. Skipped for a standalone conversion.
- `R22.6-carried-stale` (**report-only**): a carried anchor whose path is absent is reported as stale, never refused.

### Conventions

- `_sidecar_anchors` yields each anchor once with its sidecar, field and carried flag, and both anchor rules consume it.

### Invariants And Boundaries

- A carried anchor is never refused for a deleted path, so the stalest knowledge can still be represented and repaired.
- An added or re-anchored anchor must name an existing path.
- Report-only status comes from the registry flag, not from the check.

### Todos

`R22.6-carried-stale` surfaces the packet's "reported as stale references"; MIK-R24 rule 5 and MIK-R03 may take it over or reuse it later (worker gap 10).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The reference rules and their registration.

- Markers and references are paired both ways. [1]
- Record links, entry invariants, supersedes and family members must exist. [2]
- Added anchors must name existing paths; carried anchors at absent paths are reported. [3]
- The eight registered reference rules, three report-only. [4]
- A hand-added marker without a reference is refused. [5]
- The boundary example: one parent deleted a file the other's card cites. [6]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
