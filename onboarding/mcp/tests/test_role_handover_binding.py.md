# mcp/tests/test_role_handover_binding.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Binds a compiled handover to its role and its task: leaf roles compile their contract and repository
identity with scoped context and reports, a taskless Architect plans without inventing a task or a
repository, and a repeat runs the stored call after the leaf document changed. It also isolates report
paths per request and keeps the folder and grant preparation bounded.

## Code Commentary

### Logic

`_projection()` and `_check_projection()` read the projection the compiled first message carries
(MIK-R193 rule 1) and require it to name the complete hand-over while holding only the permitted fields.
`_bridge_whose_first_creation_gets_no_answer()` stands in for `bridge_call` with a catalog, a workspace
and one timed-out creation.

- **Scoped capsules.** `RoleScopedCapsuleBindingTests` compiles a leaf role with its contract and
  repository identity, scoped context and reports; a taskless Architect handover uses planning without
  inventing a task or a repository, and the taskless prompt carries the composed instructions rather
  than the baseline.
- **Repeats.** `RepeatAfterDocumentEditTests.test_a_repeat_runs_the_stored_call_after_the_leaf_document_was_edited`
  runs the stored call after the document changed instead of recompiling.
- **Enclosure binding.** `test_missing_leaf_enclosure_passes_selected_sprint_to_worktree_owner` keeps the
  selected sprint with the worktree owner when the leaf enclosure is missing.
- **Report paths.** `RoleReportPathIsolationTests` keeps manager reports master-local and request-unique,
  and leaf reports task-local with one file per request.
- **Folder and grant.** `R71FolderAndGrantTests` grants only the supported Claude route and refuses an
  external link before creating any child.

### Conventions

Cases compile the real handover and stand in only for the bridge, so what a seat receives is the
production compilation rather than a fixture string.

### Invariants And Boundaries

- A taskless Architect never invents a task or a repository.
- A repeat replays the stored call; it does not rebuild the handover.


Reusing an enclosure reports its resolved `referenceRoot`; failure to copy an agreed-reference source is returned as a `referenceWarning` naming that leaf file, while the existing enclosure is still reused and no new start is called. The fixture deliberately has no leaf file, so the test checks a named warning rather than claiming a successful copy.

## Evidence


- Scoped compilation, taskless planning, repeats, enclosure binding, report isolation and folder/grant preparation are asserted here. [1]



- Taskless Architect planning passes `role=architect` to the resolver and keeps the existing binding, no-invented-task and no-invented-repository assertions. [2]


- Reusing an enclosure reports its resolved `referenceRoot`; failure to copy an agreed-reference source is returned as a `referenceWarning` naming that leaf file, while the existing enclosure is still reused and no new start is called. The fixture deliberately has no leaf file, so the test checks a named warning rather than claiming a successful copy. [3]
