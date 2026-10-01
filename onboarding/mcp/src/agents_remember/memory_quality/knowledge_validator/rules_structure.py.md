# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_structure.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R22's per-file and cross-tree structure rules: shape, identity, single owner, locators and content, converted bases, and history freezing.** Importing the module registers its eight rules in `STRUCTURE_RULES`.

## Code Commentary

### Logic

- `R22.1-shape` (`check_shape`): the candidate keeps `knowledge/layout.json`, plus every `shape` problem.
- `R22.1-canonical`: every `canonical` problem, whose message names the formatter command.
- `R22.2-identity` (`check_identity`): `identity` problems; record IDs and realization/proof entry IDs share one uniqueness space, and a duplicate names every file that holds it. With more than one base (a merge) the message starts `merge conflict:`. A record's Markdown must sit beside its JSON record.
- `R22.4-single-owner`: an undeclared record field is a relationship recorded on the wrong side (Doc14 §2), such as an invariant that lists its realizations.
- `R22.6-locator` and `R22.6-content`: the locator kind and the `content` hash format problems.
- `R22.6-base-converted` (`check_bases_converted`): a comparison base without the marker is refused, naming its conversion (MIK-R24 rules 7 and 8) and the crossing sync; skipped for a standalone conversion.
- `R22.7-history-frozen` (`check_history_frozen`): over every history path in any base or the candidate, L07's `frozen_history_violation` decides; a closed file changed or deleted is refused.

### Conventions

- Each rule filters `ParsedTree.problems` by category (`_problems`) or computes a tree-level check; none re-parses a file.

### Invariants And Boundaries

- Rule 4 is enforced at shape level: the models' `extra="forbid"` makes a second owner unrepresentable, and this rule attributes it.
- History row IDs are outside ID uniqueness, because two frozen files that collided could never be repaired.
- A closed history file is byte-identical in the candidate; deletion counts as a change.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The structure rules and their registration.

- Shape keeps the layout marker; canonical formatting is its own rule. [1]
- Unique IDs across records and entries; a merge duplicate is a conflict naming both files. [2]
- A relationship on the wrong side is a rule-4 refusal. [3]
- An unconverted base is refused unless this is a standalone conversion. [4]
- A closed history file is frozen. [5]
- The eight registered structure rules. [6]
- Duplicate IDs after a merge are a conflict naming both files. [7]
- A closed history file is frozen, including deletion and closure in one merge parent; since MIK-R09 its trees keep the retired subject `INV-RET1R3` (records are never deleted, rule 3), assertions unchanged. [8]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
