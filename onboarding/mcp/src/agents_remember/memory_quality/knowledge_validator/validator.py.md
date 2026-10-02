# mcp/src/agents_remember/memory_quality/knowledge_validator/validator.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**Runs every registered rule over one candidate tree.** `validate_tree` is the validator itself; `validation_applies` is rule 8's applicability; `require_valid_commit` is what a commit route calls before it commits memory.

## Code Commentary

### Logic

- `validate_tree(candidate, *, bases=(), code=None, conversion=False)` builds a `ValidationContext` with `parse_tree(candidate)` and collects a `Violation` for every finding of every registered rule, stamping the rule's ID and `report_only`. It returns a sorted `ValidationReport`. `code` is required unless `conversion` is set; a conversion run checks no anchor for path existence.
- `validation_applies(candidate, bases)` is true when the candidate or any base holds the layout marker.
- **`leaf_publication` (MIK-R09, leaf 260928-MIK-L09).** `validate_tree` and `require_valid_commit` gained a defaulted `leaf_publication` keyword that they pass into the `ValidationContext`: a commit that publishes a leaf (closeout, direct landing, a leaf's recorded landing) then has MIK-R09's history-row rule read every history file not closed in a base, whatever its own `closed` flag (review R1 F1). Every other caller is unchanged.
- `require_valid_commit(candidate, *, bases, code)` returns `None` when validation does not apply, the report when the candidate passes (report-only findings included), and raises `KnowledgeValidationError` naming every refusing violation otherwise.
- **`LeafCommit` (L37).** `leaf_publication` is `False`, `True` or a `LeafCommit(frozen)`. A `LeafCommit` marks a
  leaf publication and also hands in the history files of the commit(s) the candidate sits on when they are not
  bases; `validate_tree` puts them into `ValidationContext.frozen`. A history file closed there is frozen like
  one closed in a base.

### Conventions

- The module imports `rules_history` (MIK-R09, since leaf 260928-MIK-L09: `R09-history-rows` and the report-only `R09-history-rows-merged`), `rules_admission` (MIK-R27, since leaf 260928-MIK-L27), `rules_decisions` (MIK-R13, since leaf 260928-MIK-L13), `rules_reconsideration` (MIK-R14, since leaf 260928-MIK-L14), `rules_census` (MIK-R20, since leaf 260928-MIK-L20), `rules_references`, `rules_routes` (MIK-R04, since leaf 260928-MIK-L04) and `rules_structure` for their registration side effect, so MIK-R27's three admission rules, MIK-R13's five decision content rules, MIK-R20's nine census rules and MIK-R04's six family route rules run wherever the validator runs. Because the admission rules are registered here, the fixture tree's every validation now carries one report-only `R27.4-legacy-unassessed` count (its Doc14 family is an export).
- With no bases every anchor is checked for path existence (a writer's or a curator's run).

### Invariants And Boundaries

- `require_valid_commit` has no parameter that skips a rule.
- `conversion=True` exists in the API only; it is deliberately not exposed on the CLI (ruling Q2), so the tool surface has no skip flag.
- Before the cutover no production tree has the marker, so no production route changes behaviour.

### Todos

L24/L37 must pass converted bases, or call `validate_tree(..., conversion=True)` for the standalone conversion (worker gap 4).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The three entry points.

- The validator: every registered rule over the candidate. [1]

- Rule 8's applicability: the marker on any side. [2]

- The commit route's call: nothing, the report, or the refusal. [3]

- Commit routes validate only when a side has the marker. [4]
- An unconverted base is refused, and a standalone conversion checks no path. [5]
- The registering import of MIK-R09's history-row rules. [6]

- A leaf publication, and the frozen history files of a `LeafCommit`, reach the context (MIK-R09). [7]

- The registering import of MIK-R14's link guard. [8]
- The registering import of MIK-R13's decision content rules. [9]

- A commit that publishes a leaf, with the history files of the commit it sits on. [10]
- The frozen trees reach the validation context. [11]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
