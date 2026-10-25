# mcp/tests/test_curator_instruction_wording.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the Curator and coordination instruction wording that the role wording module no longer carries: the
Curator's own authoring routes, the manifest's descriptions following the coordination default, the
writer's admission for the selected runtime, and the tool grants the manifest gives each role.

## Code Commentary

### Logic

`read()` and `role_text()` open a file of the canonical skill tree (`CANONICAL`, `LIFECYCLE`) and the role
text a seat receives, with `STARTERS` naming the starter roles the manifest describes.

- **Authoring routes.** `test_current_coordination_and_curator_rules` requires the Curator's role text to
  name both authoring routes, to say no other route writes knowledge, and to write `--commit` as
  `commit: true`.
- **Manifest descriptions.** `test_manifest_descriptions_follow_the_coordination_default` keeps each
  description on the coordination default rather than a local variant.
- **Writer admission.** `test_the_curator_writer_is_admitted_for_the_selected_runtime` pins the admission in
  the role, detail and operation texts and requires the parser to refuse the removed options with exit 2.
- **Grants.** `test_the_manifest_grants_the_role_tools_to_the_roles_that_may_use_them` checks the manifest
  grants the role tools to exactly the roles allowed to use them, through `models.tools.public_roster` and
  `models.role_identity`.

### Conventions

Cases read the shipped text through `capsule_wording` rather than a copy, so a case fails on the surface a
seat actually reads.

### Invariants And Boundaries

- One authoring route writes knowledge; the Curator's text says so.
- A writer option that was removed is refused by the parser, not ignored.

## Evidence


- The Curator's role text names both authoring routes, says no other route writes knowledge, and writes `--commit` as `commit: true`. [1]

- The writer admission is pinned in the role, detail and operation texts, and the parser refuses the removed options with exit 2. [2]
