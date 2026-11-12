# mcp/tests/test_curator_instruction_wording.py

## Governing Overview

[overview](overview.md)

## Purpose

Holds the Curator and coordination instruction wording kept apart from the role wording module: the
Curator's own authoring routes, the manifest's descriptions following the coordination default, the
writer's admission for the selected runtime, and the tool grants the manifest gives each role, together with
the step-level delivery of the coordination, reviewer-intake and correct-write procedures.

## Code Commentary

### Logic

`read()` and `role_text()` open a file of the canonical skill tree (`CANONICAL`, `LIFECYCLE`) and the role
text a seat receives, with `STARTERS` naming the starter roles the manifest describes.

- **Authoring routes.** `test_current_coordination_and_curator_rules` requires the Curator's role text to
  name mounted `knowledge_write` or the admitted serving-build CLI, to write `--commit` as
  `commit: true`, and to qualify manual recovery by the failed tool and input class. The same case holds a
  per-source table of required clauses for the Architect, Orchestrator, Manager, Curator and Investigator
  roles and the coordination, curation, planning and orientation operations, deletes four of them to prove the
  check fails, and then requires the coordination routes, the Git comparison scope and the message-handover
  delivery through the shared helpers.
- **Delivered steps.** `test_coordination_detail_is_offered_at_all_eight_failed_scenario_steps`,
  `test_reviewer_waits_for_initial_mode_before_enforcing_complete_intake` and
  `test_correct_write_ladder_distinguishes_named_writes_from_other_stops` check, through
  `curator_instruction_delivery`, that each compiled step offers its own detail, that the Reviewer follows the
  delivered intake owner, and that the four affected roles receive the correct-write ladder without losing
  their hard stops; `test_foundation_intake_and_correction_keep_their_task_and_truth_boundaries` reads the
  Curator's foundation inputs and outputs through the same helper module.
- **Manifest descriptions.** `test_manifest_descriptions_follow_the_coordination_default` keeps each
  description on the coordination default rather than a local variant.
- **Writer admission.** `test_the_curator_writer_is_admitted_for_the_selected_runtime` pins the admission in
  the role, detail and operation texts and requires the parser to refuse the removed options with exit 2.
- **Grants.** `test_the_manifest_grants_the_role_tools_to_the_roles_that_may_use_them` checks the manifest
  grants the role tools to exactly the roles allowed to use them, through `models.tools.public_roster` and
  `models.role_identity`.

### Conventions

Cases read the canonical skill tree, the shipped composition corpus or the compiled capsule rather than a copy, so a case fails on the surface a
seat actually reads.

### Invariants And Boundaries

- Normal knowledge authoring uses the admitted serving writer. The wording guard also pins the narrowly scoped correct-write-refusal recovery exception.
- A retired writer option is refused by the parser, not ignored.

The foundation and correction cases require a real task/enclosure, producer handoff-check evidence and correction of every contradicted body claim. Manager publication is distinguished from organizational completion, and sentence/card scope controls remove each actual clause to prove the guard fails. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- The Curator wording guard names mounted knowledge_write or the admitted serving-build CLI, explicit file-write commit, and the scoped correct-write recovery exception; it does not assert unconditional route exclusivity.

- The writer admission is pinned in the role, serving-build detail, publication report and operation texts, and the parser refuses the removed options with exit 2 [2]

- The Curator wording guard names mounted knowledge_write or the admitted serving-build CLI, explicit file-write commit, and the scoped correct-write recovery exception; it does not assert unconditional route exclusivity. [1]

- The foundation and correction cases require a real task/enclosure, producer handoff-check evidence and correction of every contradicted body claim. Manager publication is distinguished from organizational completion, and sentence/card scope controls remove each actual clause to prove the guard fails. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [3]

- The coordination detail must be offered at each of the eight failed-scenario steps of the compiled capsules. [4]
- The compiled-capsule helper comes from the capsule-delivery proof module. [5]
