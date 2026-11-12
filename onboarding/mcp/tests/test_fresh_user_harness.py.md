# mcp/tests/test_fresh_user_harness.py

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

Past-epoch loader account:

`_load` imports a harness module by file path, since `scripts/e2e_harness/` is not a package; both
`HARNESS_ROOT` and `MCP_SRC` are inserted into `sys.path` as **strings** rather than `Path`
objects, because a non-`str` `sys.path` entry is silently ignored by the import machinery.

Current loader account: `SCRIPTS_ROOT` names the scripts directory and joins `MCP_SRC` on `sys.path` as a string. `_load` imports `e2e_harness.<module>` with `importlib.import_module`, so the scenario and test share cached module objects and fixture-class identity. No parallel file-path loader is retained.

`GOVERNED_HARNESS_MODULES` names the harness modules this suite answers for, and
`FreshUserScenarioContractTests.test_every_governed_harness_module_this_suite_answers_for_exists`
turns that list into an existence assertion — so the catalog's consumer rows and the tree cannot
drift apart silently.

The two classes and what each one defends:

| Class | Defends |
| --- | --- |
| `FreshUserFixtureShapeTests` | the **fixture shape**: the oversized fixture has exactly `fresh_user_fixture.OVERSIZED_BYTES` generated-file bytes and carries the vendored tree and the distinct spear/sprint branches; the plain fixture excludes the vendored tree and uses `main`; and the fixture owns everything under its own run root. |
| `FreshUserScenarioContractTests` | the **scenario contract**: a step that cannot run is reported as blocked by name and is never `completed`; every governed harness module this suite answers for exists; and the entry point requires `--reports` while defaulting its run root. |

### Conventions

- Size comparison uses the fixture-owned `OVERSIZED_BYTES`, not a retired citation source-index cap.
- `sizes(root)` walks real fixture files for stat-size assertions.
Past-epoch count caption: - The unit-regression module is a declared consumer of the three governed harness artifacts.

Current count: `GOVERNED_HARNESS_MODULES` names four paths: fixture, scenario, reporting and runner. The existence assertion checks all four.

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

## Evidence

### Repo-Internal References


Retained earlier caption: - A governed harness module is loaded by path, since the harness root is not a package.

Original-target custody: _load in blob 7e009d4b32c2f82a0a22371f55a3f93aaf5906d1 loaded flat harness modules by file path. Its current replacement imports the package-qualified identity through the scripts root; the historical loader sentence is detached from the live number.

- Oversized generated-file bytes equal the fixture-owned OVERSIZED_BYTES; vendored tree, ignore file and distinct main/spear/sprint branch facts are asserted.


- Plain fixture omits vendor/lib.py and uses main as its spear branch; it no longer asserts retired per-file or aggregate caps.

- The fixture owns everything under its own run root.
- A step that cannot run is blocked by name and never reported as completed.

- Every governed harness module this suite answers for exists.

- The entry point requires `--reports` and defaults the run root.
- A non-`str` `sys.path` entry would be silently ignored, so both roots are inserted as strings.
- The loader uses importlib.import_module with the e2e_harness-qualified module name. The test and scenario share cached module objects and fixture-class identity; a missing module raises rather than yielding an empty fixture.
- The report path the entry point owns.
- The entry point that drives the acceptance, removes its temporary root and exits on a failed invariant.

- The unchanged GOVERNED_HARNESS_MODULES tuple names fixture, scenario, reporting and runner; the current package-qualified loader/root account shares cached module identity, and the existence assertion checks each declared path.

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.

- The unchanged GOVERNED_HARNESS_MODULES tuple names fixture, scenario, reporting and runner; the current package-qualified loader/root account shares cached module identity, and the existence assertion checks each declared path. [12]
- Oversized generated-file bytes equal the fixture-owned OVERSIZED_BYTES; vendored tree, ignore file and distinct main/spear/sprint branch facts are asserted. [1]
- Plain fixture omits vendor/lib.py and uses main as its spear branch; it no longer asserts retired per-file or aggregate caps. [2]
- The fixture owns everything under its own run root. [3]
- A step that cannot run is blocked by name and never reported as completed. [4]
- Every governed harness module this suite answers for exists. Anchor: `test_every_governed_harness_module_this_suite_answers_for_exists` `GOVERNED_HARNESS_MODULES` [5]
- The entry point requires `--reports` and defaults the run root. [6]
- A non-`str` `sys.path` entry would be silently ignored, so both roots are inserted as strings. [7]
- The loader uses importlib.import_module with the e2e_harness-qualified module name. The test and scenario share cached module objects and fixture-class identity; a missing module raises rather than yielding an empty fixture. [8]
- The report path the entry point owns. [10]
- The entry point that drives the acceptance, removes its temporary root and exits on a failed invariant. [11]
