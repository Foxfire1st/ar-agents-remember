# mcp/test_support/agents_remember_test_support/testing/manifest_step_derivation.py

## Governing Overview

[overview](overview.md)

## Purpose

The module derives actions and role audiences for classified Markdown references in the composition manifest and reports disagreement with their composed declarations.

## Code Commentary

First-message texts are a role's role file, the role-addressed passages of its operation files, the `SKILL.md` of each listed skill and `core/every-role.md` when listed; fenced code is skipped. A pointer is a Markdown link resolving to an `l-01-agent-lifecycles` file (relative, `{{detail:F}}` or the served `skill://` form). Its action is the sentence's opening "Before/When/For" clause up to the last top-level comma before the link; a pointer without one is reported, not counted. A file with no first-message pointer takes its step and roles from pointers in the manifest's other reference files. A declared `rolesReason` widens the expected roles by the roles it names. Readers are the unique-detail-pointer, wording-pin and link-integrity tests and `pointer_uniqueness.py`, which reuses `LINK`, `action_of` and `sentence_start`.

`manifest_mismatches` composes the manifest before comparing declarations with pointer-derived facts. A step-set mismatch or a role-list mismatch, including roles widened by a nonempty rolesReason, ends its finding with `; run mcp/.venv/bin/python scripts/renew-instructions.py`. The separate no-action and empty-rolesReason findings do not add that suffix. [3]

## Evidence

- A pointer's action is its table-row trigger (`row: <cell>`), its sentence's opening Before/When/For clause, or none. [1]


- Actions and roles are derived for references with a step_detail classification and a Markdown source. [2]

### Repo-Internal References (renewed)

- Composed declarations are compared with pointer-derived steps and roles; ordinary references without a declared step skip the step comparison, and a nonempty rolesReason controls role widening. Step-set and role-list mismatch findings end with `; run mcp/.venv/bin/python scripts/renew-instructions.py`; no-action and empty-rolesReason findings retain their separate messages. [3]
