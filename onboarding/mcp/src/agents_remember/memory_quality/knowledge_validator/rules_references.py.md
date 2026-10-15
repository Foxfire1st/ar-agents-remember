# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_references.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R22's cross-file rules: markers and references, record links, relations, unresolved targets, family members, and anchor paths.** Importing the module registers its eight rules in `REFERENCE_RULES`: two carry `migration_debt`, one carries `merge_reports` with writer reporting, and the others refuse. None of these rules reads a history file.

## Code Commentary

### Logic

- `R22.3-markers` (`check_markers`): every marker of an onboarding Markdown file has a reference in its sidecar, and every reference is used. Markdown without a sidecar (a record's Markdown included) holds no markers. A file sidecar without Markdown holds no references, and a route sidecar must sit beside its `overview.md`. When the paired sidecar exists but does not parse, the Markdown is skipped, because its shape violation is reported instead.
- `R22.3-sidecar-without-markdown` (**migration_debt**): the file sidecar is a repair finding
  (MIK-R21 rule 5), carried only when a base already lacks its Markdown at that sidecar path.
- `R22.3-record-links`: every ID a sidecar reference target, an entry's `invariant`, a record's `supersedes` or a record link target names must exist in `record_ids`; route targets are exempt, and a retired record still resolves.
- `R22.3-relations`: the `relation` problems found while parsing.
- `R22.3-unresolved-target` (**migration_debt**): each `unresolved` target, carried only when a base
  holds the same `(sidecar path, target text)` finding. Both debt rules report at standalone
  conversion, or for carried debt while migration is incomplete; new debt refuses immediately
  elsewhere, and carried debt refuses once every onboarding route is migrated/excluded.
- `R22.5-family-members`: every family member exists; the route rules are left to MIK-R04.
- `R22.6-anchor-path`: an anchor with no equal counterpart in any base must name a file in the paired code tree. For an entry the counterpart is the same entry ID; for a reference target, the same sidecar path. Skipped for a standalone conversion.
- `R22.6-carried-stale` (**merge_reports**, writer-reported): a carried anchor at an absent code path
  refuses commit/landing, reports at sync/standalone conversion, and is reported by the writer for
  repair. No code tree means no path check; this does not make every content-stale reference refusing.

### Conventions

- `_sidecar_anchors` yields each anchor once with its sidecar, field and carried flag, and both anchor rules consume it.

### Invariants And Boundaries

- A carried deleted-path anchor can be merged and repaired under `merge_reports`; it must be repaired
  before the next refusing publication/landing. Equal-anchor carry still distinguishes it from a
  newly written absent-path anchor.
- An added or re-anchored anchor must name an existing path.
- Route disposition comes from the registry's named reason and current migration/base facts, not
  a permanent report-only flag. Writer reporting is a repair affordance, not publication permission.

### Todos

The historical worker gap 10 anticipated MIK-R24/MIK-R03 stale-reference maintenance. The current
absent-path finding already carries MIK-R53's merge_reports reason and names repair before the next
refusing publication/landing; other content-only staleness keeps its separate currentness treatment.

Literal text that is not a marker receives three recovery choices in `_ESCAPE_HINT`: escaped bracket spelling, a fenced code block, or a code span. The hint changes presentation, not marker grammar or the separate absent-path/reporting rules.

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
- A hand-added marker without a reference is refused. [5]
- The boundary example: one parent deleted a file the other's card cites. [6]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.

- Added anchors must name existing paths; carried absent-path anchors refuse off merge and report for sync/conversion or writer repair. [3]
- Eight reference rules: two migration_debt, one merge_reports/writer-reported, no permanent report-only waiver. [4]
- Current source delta inspected statically: Repair debt keys and carried-anchor route disposition throughout prose/captions; retain carry and currentness scope. [7]

- Literal-markup recovery names escapes, fenced blocks and code spans. [8]
