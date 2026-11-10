# mcp/test_support/agents_remember_test_support/testing/manifest_step_derivation.py

## Governing Overview

[overview](overview.md)

## Purpose

The module derives each composition-manifest reference's step and role audience from the actual pointers to its file, and reports entries whose declared `step` or `roles` differ.

## Code Commentary

First-message texts are a role's role file, the role-addressed passages of its operation files, the `SKILL.md` of each listed skill and `core/every-role.md` when listed; fenced code is skipped. A pointer is a Markdown link resolving to an `l-01-agent-lifecycles` file (relative, `{{detail:F}}` or the served `skill://` form). Its action is the sentence's opening "Before/When/For" clause up to the last top-level comma before the link; a pointer without one is reported, not counted. A file with no first-message pointer takes its step and roles from pointers in the manifest's other reference files. A declared `rolesReason` widens the expected roles by the roles it names. Readers are the unique-detail-pointer, wording-pin and link-integrity tests and `pointer_uniqueness.py`, which reuses `LINK`, `action_of` and `sentence_start`.

## Evidence

- A pointer's action is its sentence's opening Before/When/For clause, or none. [1]
- Step and roles are derived for every manifest reference that declares a step. [2]
- Declared step and roles must equal the derived ones, widened only by a nonempty roles reason. [3]
