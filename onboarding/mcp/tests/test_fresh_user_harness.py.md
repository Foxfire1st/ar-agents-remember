# mcp/tests/test_fresh_user_harness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_fresh_user_harness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:35+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Be the **consumer of record** for the fresh-user acceptance harness. `scripts/e2e_harness/**` is a
permanent evidence-support root, so every non-`test_` module under it is a governed evidence
artifact: the lifecycle catalog must carry a row for it, that row needs a real consumer and an
executable replacement node, and the artifact must not sit in the tree with no one to answer for
it. This module is that consumer.

It is deliberately small and it does **not** re-run the acceptance scenario. The scenario's own
transcript is the acceptance evidence; what is pinned here is the *shape the scenario needs*, so a
later edit to the fixtures cannot quietly stop producing it.

## Code Commentary

### Logic

`_load` imports a harness module by file path, since `scripts/e2e_harness/` is not a package; both
`HARNESS_ROOT` and `MCP_SRC` are inserted into `sys.path` as **strings** rather than `Path`
objects, because a non-`str` `sys.path` entry is silently ignored by the import machinery.

`GOVERNED_HARNESS_MODULES` names the harness modules this suite answers for, and
`FreshUserScenarioContractTests.test_every_governed_harness_module_this_suite_answers_for_exists`
turns that list into an existence assertion — so the catalog's consumer rows and the tree cannot
drift apart silently.

The two classes and what each one defends:

| Class | Defends |
| --- | --- |
| `FreshUserFixtureShapeTests` | the **fixture shape**: the over-cap fixture really crosses the shipped `MAX_SOURCE_FILE_BYTES` and carries the vendored tree and the distinct spear/sprint branches; the plain fixture stays inside every cap; and the fixture owns everything under its own run root. |
| `FreshUserScenarioContractTests` | the **scenario contract**: a step that cannot run is reported as blocked by name and is never `completed`; every governed harness module this suite answers for exists; and the entry point requires `--reports` while defaulting its run root. |

### Conventions

- Cap comparisons use the shipped `MAX_SOURCE_FILE_BYTES` / `MAX_SOURCE_BYTES` constants rather
  than literals, so a case reddens when a ruled bound moves.
- `sizes(root)` walks a fixture tree so a case can assert against real stat sizes.
- The module is registered in the `unit-regression` evidence lane and is a declared **consumer** of
  the two new `scripts/e2e_harness` catalog artifacts.

### Invariants And Boundaries

The module's own docstring states what it does **not** cover, and both exclusions are load-bearing:

- **Not the acceptance itself.** The transcript is written by running
  `scripts/e2e_harness/run_fresh_user.py`; this module never runs it, so it neither claims nor can
  claim that the chain works end to end.
- **Not the fixtures' Git behaviour.** Branch topology and `origin/HEAD` are asserted as facts
  about the repository the fixture creates, not as a claim about the product's
  integration-branch authority.

The fixtures are **disposable repositories the harness creates from nothing** under one run root.
They are not the developer's repositories, and no card may describe them as such.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The over-cap fixture really crosses the shipped per-file cap. | `test_the_over_cap_fixture_really_crosses_the_cap` | mcp/tests/test_fresh_user_harness.py:118-149 |
| The plain fixture stays inside every cap. | `test_the_plain_fixture_stays_inside_every_cap` | mcp/tests/test_fresh_user_harness.py:151-168 |
| The fixture owns everything under its own run root. | `test_the_fixture_owns_everything_under_its_own_run_root` | mcp/tests/test_fresh_user_harness.py:170-186 |
| A step that cannot run is blocked by name and never reported as completed. | `test_a_step_that_cannot_run_is_blocked_by_name_and_not_completed` | mcp/tests/test_fresh_user_harness.py:192-216 |
| Every governed harness module this suite answers for exists. | `test_every_governed_harness_module_this_suite_answers_for_exists`; `GOVERNED_HARNESS_MODULES` | mcp/tests/test_fresh_user_harness.py:218-222 |
| The entry point requires `--reports` and defaults the run root. | `test_the_entry_point_requires_reports_and_defaults_the_run_root` | mcp/tests/test_fresh_user_harness.py:224-235 |
| A non-`str` `sys.path` entry would be silently ignored, so both roots are inserted as strings. | `HARNESS_ROOT`; `MCP_SRC` | mcp/tests/test_fresh_user_harness.py:48-56 |
| A governed harness module is loaded by path, since the harness root is not a package. | `_load` | mcp/tests/test_fresh_user_harness.py:64-99 |
| The per-file cap the oversize case measures against. | `MAX_SOURCE_FILE_BYTES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:23-23 |
| The report path the entry point owns. | `REPORT_DIRECTORY` | scripts/e2e_harness/run_fresh_user.py:32-32 |
| The entry point that drives the acceptance, removes its temporary root and exits on a failed invariant. | `main` | scripts/e2e_harness/run_fresh_user.py:47-82 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T10:35+02:00 — 260915-CAPS-L14 curator: created this card for the test module the leaf adds. Records why the module exists at all (it is the **consumer of record** that makes the three new `scripts/e2e_harness` modules governed evidence artifacts with a real consumer and an executable replacement node), the two classes and what each defends, and, in its own section, the two exclusions its docstring states: it does not run the acceptance, and it does not claim the product's integration-branch authority. States plainly that the fixtures are disposable repositories created from nothing under one run root and **not** the developer's repositories. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.
