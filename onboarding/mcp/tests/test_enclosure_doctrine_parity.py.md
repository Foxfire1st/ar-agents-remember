# mcp/tests/test_enclosure_doctrine_parity.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the doctrine parity a scoped repair needs: the worktree-operations and closeout workflows in the kept
`w-02-light-task-workflow` skill match the current archive and no-remains routes, the packaged copies are
byte-identical to their canonical originals, and every next action a document names exists as a registered
operation.

## Code Commentary

### Logic

`C09` names `skills/w-02-light-task-workflow/workflows/worktree-operations.md` and `C12` names its
`closeout.md`; `C09_GENERATED`/`C12_GENERATED` name the packaged copies under package data, and `MCP_TOOLS`
names `docs/reference/mcp-tools.md`.

- **Archive.** `test_c12_no_retire_master_exclusivity` keeps closeout from claiming a single master archive
  operation, and `test_c12_keeps_retirement_finalization_authority` keeps individual retirement and
  finalization authority.
- **Adoption and no-remains.** `test_c09_states_bounded_no_remains_exception` requires the workflow to name the
  no-locator, no-folder, no-branch exception with why and how to retry, and
  `test_c09_keeps_adoption_and_archive_tail` keeps explicit adoption and the archive-before-destructive-tail.
- **Copies.** `test_generated_skill_copies_match_canonical` compares bytes between the packaged copy and the
  canonical source.
- **References.** `test_mcp_reference_rows_name_exception` keeps the cleanup and abandon reference rows naming
  the bounded pre-locator path, and `test_documented_next_actions_are_registered` requires every documented next
  action to exist in `public_roster`.

### Conventions

The case reads the shipped files by path rather than a copy in the test, so a moved or retired skill fails here.

### Invariants And Boundaries

- The packaged copy is the canonical text, byte for byte.
- A documented next action that is not a registered operation is a defect.

## Evidence

- Doctrine parity across the skill copies and the MCP reference is pinned. [1]
