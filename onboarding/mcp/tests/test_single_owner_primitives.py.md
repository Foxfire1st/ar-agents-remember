# mcp/tests/test_single_owner_primitives.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_single_owner_primitives.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Uses small Python input programs to exercise single-writer detectors. It follows import aliases and constant program names, reads the program word from shell command strings, distinguishes gh from git, recognizes module and direct-import calls, and avoids confusing dataclasses.replace or unrelated names with the protected writer. It is detector behavior, not a repeated repository census.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| An import alias is followed to the name it binds | `test_an_import_alias_is_followed_to_the_name_it_binds` | mcp/tests/test_single_owner_primitives.py:47-49 |
| A program name hidden behind a constant is resolved | `test_a_program_name_hidden_behind_a_constant_is_resolved` | mcp/tests/test_single_owner_primitives.py:51-57 |
| A shell command string is read down to its program word | `test_a_shell_command_string_is_read_down_to_its_program_word` | mcp/tests/test_single_owner_primitives.py:59-61 |
| Gh is not git | `test_gh_is_not_git` | mcp/tests/test_single_owner_primitives.py:68-79 |
| The module attribute form is caught | `test_the_module_attribute_form_is_caught` | mcp/tests/test_single_owner_primitives.py:86-87 |
| A bare replace from dataclasses is not the one from os | `test_a_bare_replace_from_dataclasses_is_not_the_one_from_os` | mcp/tests/test_single_owner_primitives.py:94-98 |
| Direct imports and aliases are caught | `test_direct_imports_and_aliases_are_caught` | mcp/tests/test_single_owner_primitives.py:104-123 |
| Reexport without a call and unrelated local names are not callers | `test_reexport_without_a_call_and_unrelated_local_names_are_not_callers` | mcp/tests/test_single_owner_primitives.py:125-129 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-28T06:40+02:00 — No content impact: moved the single-owner verification import into
  `agents_remember_test_support`; the primitive ownership census remains unchanged.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: added direct-import, module-alias,
  and relative-import forcing cases for `write_task_doc_batch`, so an unreviewed batch publisher
  cannot evade the task-document single-owner census.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
