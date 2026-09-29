# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R20's nine census rules in the validator's one registry (MIK-R22 rule 9).** Importing the module
registers one `ValidationRule` per entry of `knowledge_census.checks.CENSUS_RULES`, all refusing; `validator.py`
imports it next to the other rule modules, so every place the validator runs (`validate_tree`,
`require_valid_commit`, the managed sync, `knowledge-validate`) runs the census rules too.

## Code Commentary

### Logic

- `_findings(context)` runs `check_censuses` once per validation over the candidate, the bases and the
  validator's `record_ids`, and caches the findings; each registered rule (`_rule_check`) yields only its
  own rule's findings as registry `Finding`s.
- The cache is `_FINDINGS: dict[id(context), (weakref.ref(context), findings)]`, read with one `dict.get`,
  and each entry is removed by `weakref.finalize` when its context is collected (review R1 finding 3).

### Conventions

- No rule is report-only and none is writer-reported; `parsed.py` is not forked.

### Invariants And Boundaries

- The cache holds only findings, never a tree, so no tree outlives its validation.
- A reused `id()` cannot hit a stale entry: the weak-reference identity check fails.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cache and the registration.

| Finding | Anchor | Source |
| --- | --- | --- |
| One check per validation, cached by context identity with a weak reference. | `_FINDINGS`; `_findings` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py:28-42 |
| Each rule yields its own findings. | `_rule_check` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py:45-51 |
| The registration, one rule per census rule. | `CENSUS_VALIDATION_RULES` | mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py:54-57 |
| The census rules are registered and refusing. | `test_census_rules_are_registered_and_refusing` | mcp/tests/test_knowledge_census_files.py:308-312 |
| The cache keeps no tree after validation. | `test_the_census_rule_cache_keeps_no_tree_after_validation` | mcp/tests/test_knowledge_census_files.py:585-589 |

## Cross-Repo References

No meaningful cross-repo references found: the rules read the validation context's memory trees only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
