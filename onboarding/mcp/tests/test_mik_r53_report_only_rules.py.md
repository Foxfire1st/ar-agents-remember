# mcp/tests/test_mik_r53_report_only_rules.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This module checks MIK-R53 Part C's named report reasons and refusal boundaries over controlled converted-memory fixtures. A rule cannot be registered as plainly report-only; sync-merge reports and migration debt have different conditions, messages and later refusing routes.

## Code Commentary

### Logic

The registry cases reject plainly report-only registrations and rules with both named report reasons, and verify the ten-rule decision sets plus writer-reported refusing rules. Controlled fixture edits exercise governs, existing-record admission, absent carried routes, unrealized families and gone-path anchors at leaf/publication or merge boundaries.

Conversion cases verify that standalone conversion admits no base, paired code or leaf publication. Migration cases include candidate-tree overview routes, select the latest route status across censuses, distinguish carried debt from new debt, and require every route to be migrated or excluded before inherited debt becomes refusing everywhere. Per-record operation-count cases check the admission classifier without claiming a timing benchmark. Merged-row fixtures show a merge report becoming an ordinary covered-entry refusal at the next publication.

### Invariants And Boundaries

- `R13.3-governs` has neither merge nor migration-debt exemption; the four other newly refusing rules have the declared sync-merge reporting boundary.
- New migration debt refuses immediately; carried debt reports only while migration is incomplete. Once complete, sidecar-without-Markdown, unresolved-target, unassigned-route and legacy-record debt refuse at both publication and sync.
- Reports must state their reason and refusing route, and may not use unconditional never-refuse language. Command help and the c-02 skill carry the same ten-rule decisions.
- Fixtures, mock equality counters and source assertions are bounded test mechanisms, not proof that this Curator ran the suite, migrated live routes, or accepted the current memory.

## Evidence

### Repo-Internal References

- Registration rejects unnamed reporting or competing report reasons and verifies the rule sets. [1]
- Leaf/publication versus merge cases exercise existing-record, absent-route, unrealized-family and gone-path refusal boundaries. [2]
- Standalone conversion rejects bases, paired code and publication; candidate overviews join the migration population. [3]
- Admission operation counts constrain per-record classification rather than elapsed runtime. [4]
- Merge-moved rows report at merge but are refused by covered-entry validation at publication. [5]
- Messages, command help and skill text carry the named reporting and refusal decisions. [6]
- Complete-census boundary cases cover carried debt at both landing and sync with incomplete controls. [7]
