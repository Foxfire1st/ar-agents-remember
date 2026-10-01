# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_census.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cache and the registration.

- One check per validation, cached by context identity with a weak reference. [1]
- Each rule yields its own findings. [2]
- The registration, one rule per census rule. [3]
- The census rules are registered and refusing. [4]
- The cache keeps no tree after validation. [5]

### Cross-Repo References

No meaningful cross-repo references found: the rules read the validation context's memory trees only.

No cross-repo boundary is crossed by this file.
