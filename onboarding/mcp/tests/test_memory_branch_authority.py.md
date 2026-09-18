# test_memory_branch_authority.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_memory_branch_authority.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T17:59+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview      | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

The shipped behavioral check for **which branch a repository's memory is founded on**, plus the two
structures the same leaf introduced: the free agent's taskless admission, and the memory-content
exclusion that keeps bootstrap scaffolding out of a memory commit.

Its leading property is stated in its own module docstring: the memory repository's initial branch
is the branch the developer names, and every seam that later compares a branch against "the memory
repository's default" reads that recorded name instead of a hard-coded one. Four seams carry it and
each one refuses if it is wrong — `memory_init` mints and records the branch, its repair path
accepts the recorded branch instead of demanding `refs/heads/main`, `_baseline_default_branch`
follows the recorded branch so the first baseline can be adopted on a repository founded on
anything, and `memory_repository_default_branch` validates the recorded name against the refs that
exist rather than against the literal `main`.

## Code Commentary

### Logic

**Twenty cases in four groups.** The module drives the real public operations
(`memory_init_tool`, `memory_baseline_adopt_tool`) on real Git repositories created under
`tmp_path`; it installs `MCP_SRC` and `MCP_TESTS` on `sys.path` so it exercises the shipped modules
rather than a copy.

*Group 1 — the memory branch is chosen, recorded and followed (12 cases).* Minting records the
named branch and validates the recorded name against a real ref; an omitted branch inherits the code
repository's checked-out branch, and the call **refuses rather than inventing `main`** when neither
source has an answer. The unborn repair path accepts the configured branch and still refuses a
repository that already carries refs; a value that is not one local branch name is refused, and a
recorded `refs/heads/` spelling is accepted and normalized. Baseline adoption follows the configured
branch, refuses a branch the memory repository does not record, and the memory default-branch
accessor validates the recorded name against its refs while still refusing a recorded name with no
ref. An absent coordination root is refused before anything is created.

*Group 2 — the free agent's shape (4 cases).* The `bootstrap` role is a free agent with no task
altitude; without a task document only the named taskless roles are admitted; the set is a named,
readable export rather than a bare literal inside a refusal; and no task altitude set in the source
names `bootstrap`. The group's own banner records the developer ruling it protects, so a later
reader cannot "fix" the seat by giving it the altitude it must not have.

*Group 3 — the reviewed round-2 findings, pinned (2 cases).* `bootstrap/` is absent from the first
baseline's commit and still on disk afterwards, asserted on `git ls-files` — the committed tree — not
on a comment; and the same exclusion holds on the helper a later memory commit uses. These are the
two cases that fail if the exclusion goes inert again.

*Group 4 — the taskless document and the manifest (2 cases).* A document supplied to a taskless role
still resolves but skips the altitude check, so a bad reference is still refused; and the manifest
declares no task altitude for the free agent while the nine task-bound roles keep theirs, which
keeps the exception scoped.

### Conventions

- Every case creates its own repository under `tmp_path` and drives the public operation; no fixture
  is shared across cases and no test reaches into a private helper to assert a private fact.
- Every comparison takes its two sides from different artifacts — the recorded config, the actual
  ref, the returned payload, and, where a refusal is the behaviour, the refusal's own text. That is
  what makes a case falsifiable rather than self-derived.
- The module is registered in `mcp/tests/test-evidence-lanes.toml` under `unit-regression`; a new
  case belongs in this module rather than in a separate ad-hoc script.
- The one production spelling the cases read is imported, not restated:
  `DEFAULT_BRANCH_CONFIG_KEY` comes from `kernel.memory_init` and `MEMORY_CONTENT_EXCLUDES` from
  `models.memory_content_excludes`, so a rename fails the case instead of silently passing.

### Invariants And Boundaries

- **The memory branch is data, never a constant.** Every comparison validates the recorded name
  against a real ref; no case may be "fixed" by reintroducing a comparison against `main`.
- **`bootstrap/` is excluded from memory-content commits, not deleted from the worktree.** The
  second half of the assertion is as load-bearing as the first: the developer's transient files stay
  on disk as untracked content.
- **The exclusion must ride the call that stages.** An exclusion applied to a bare `git add` before
  `commit_if_dirty` re-stages the worktree is inert; the case exists precisely because that was
  measured as broken.
- **The taskless set is policy, not an implementation detail.** The case asserts the export is named
  and readable, so the ruling stays legible to the next reader instead of collapsing into a literal.
- **A taskless role still resolves a supplied document.** Being exempt from the altitude check is not
  a licence to skip resolution; a bad reference stays refused.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local check.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the property, the four seams, and the two-sides rule. | "The memory repository is founded on a chosen code branch, not on" | mcp/tests/test_memory_branch_authority.py:1-1 |
| Group 1 — minting, inheriting and refusing to invent a branch. | `test_memory_init_mints_and_records_the_named_initial_branch`; `test_memory_init_inherits_the_code_repositorys_current_branch_by_default`; `test_memory_init_refuses_rather_than_inventing_a_branch_when_it_has_no_answer` | mcp/tests/test_memory_branch_authority.py:109-125; mcp/tests/test_memory_branch_authority.py:127-144; mcp/tests/test_memory_branch_authority.py:146-164 |
| Group 1 — the repair path, the name narrowing, and the recorded spelling. | `test_the_unborn_repair_path_accepts_the_configured_branch_instead_of_main`; `test_the_unborn_repair_path_still_refuses_a_repository_that_already_has_refs`; `test_an_initial_branch_that_is_not_one_local_branch_name_is_refused`; `test_the_recorded_refs_heads_spelling_is_accepted_and_normalized` | mcp/tests/test_memory_branch_authority.py:166-185; mcp/tests/test_memory_branch_authority.py:187-204; mcp/tests/test_memory_branch_authority.py:206-215; mcp/tests/test_memory_branch_authority.py:217-228 |
| Group 1 — adoption follows the recorded branch, and the default-branch accessor validates it. | `test_baseline_adoption_follows_the_configured_branch`; `test_baseline_adoption_refuses_a_branch_the_memory_repository_does_not_record`; `test_the_memory_default_branch_validates_the_recorded_name_against_its_refs`; `test_the_memory_default_branch_still_refuses_a_recorded_name_with_no_ref` | mcp/tests/test_memory_branch_authority.py:230-261; mcp/tests/test_memory_branch_authority.py:263-283; mcp/tests/test_memory_branch_authority.py:285-300; mcp/tests/test_memory_branch_authority.py:302-316 |
| Group 2 — the free agent's shape, with the ruling the group protects. | `test_the_bootstrap_role_is_a_free_agent_and_has_no_task_altitude`; `test_without_a_task_document_only_the_taskless_seat_roles_are_admitted`; `test_the_free_agent_set_is_named_and_readable_not_a_bare_literal`; `test_no_task_altitude_set_in_the_source_names_bootstrap` | mcp/tests/test_memory_branch_authority.py:337-364; mcp/tests/test_memory_branch_authority.py:366-394; mcp/tests/test_memory_branch_authority.py:396-419; mcp/tests/test_memory_branch_authority.py:421-446 |
| Group 3 — the exclusion, pinned on the commit tree. | `test_the_first_baseline_never_commits_bootstrap_scaffolding`; `test_no_memory_content_commit_stages_bootstrap_scaffolding` | mcp/tests/test_memory_branch_authority.py:448-493; mcp/tests/test_memory_branch_authority.py:495-512 |
| Group 4 — a supplied document still resolves, and the manifest exception stays scoped. | `test_a_document_supplied_to_a_taskless_role_still_resolves_but_skips_the_altitude_check`; `test_the_manifest_declares_no_task_altitude_for_the_free_agent` | mcp/tests/test_memory_branch_authority.py:514-590; mcp/tests/test_memory_branch_authority.py:592-618 |
| The branch authority the first group drives. | `_git_init_result`; `_repair_unborn_memory_repository`; `_resolved_initial_branch`; `DEFAULT_BRANCH_CONFIG_KEY` | mcp/src/agents_remember/kernel/memory_init.py:140-192; mcp/src/agents_remember/kernel/memory_init.py:103-137; mcp/src/agents_remember/kernel/memory_init.py:49-59; mcp/src/agents_remember/kernel/memory_init.py:13-13 |
| The adoption seam whose hard-coded `main` the first group replaced. | `_baseline_default_branch` | mcp/src/agents_remember/memory/baseline.py:149-192 |
| The recorded-name validation the first group holds, and its malformed-name refusal. | `memory_repository_default_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:51-87 |
| The taskless admission the second and fourth groups hold. | `TASKLESS_SEAT_ROLES`; `_binding_refusal` | mcp/src/agents_remember/serving/task_binding.py:60-83; mcp/src/agents_remember/serving/task_binding.py:126-152 |
| The exclusion policy the third group pins. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/models/memory_content_excludes.py:32-35 |
| The staging helper the third group's failure mode lives in. | `_excluded_pathspec`; `stage_worktree_content`; `commit_if_dirty` | mcp/src/agents_remember/worktrees/modules/git.py:34-35; mcp/src/agents_remember/worktrees/modules/git.py:191-198; mcp/src/agents_remember/worktrees/modules/git.py:200-208 |
| The lane row that keeps the fail-closed evidence registry loading clean. | "test_memory_branch_authority.py" | mcp/tests/test-evidence-lanes.toml:113-113 |

## Cross-Repo References

No sibling-repository contract defines this check.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_memory_branch_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: created this card for the module the leaf added
  (`CAPS-R13@v1`, discharging the absorbed `260820` runtime-correctness scope). It records the four
  groups and their twenty cases, the two-sides rule that makes each case falsifiable, the property
  that the memory branch is data rather than a constant, the exclusion's
  excluded-not-deleted boundary, and the lane row this module carries in the fail-closed evidence
  registry. Verification metadata is left at the leaf base commit because the source is uncommitted —
  the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
