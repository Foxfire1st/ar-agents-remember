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

## Evidence

### Repo-Internal References

- The over-cap fixture really crosses the shipped per-file cap. [1]
- The plain fixture stays inside every cap. [2]
- The fixture owns everything under its own run root. [3]
- A step that cannot run is blocked by name and never reported as completed. [4]
- Every governed harness module this suite answers for exists. [5]
- The entry point requires `--reports` and defaults the run root. [6]
- A non-`str` `sys.path` entry would be silently ignored, so both roots are inserted as strings. [7]
- A governed harness module is loaded by path, since the harness root is not a package. [8]
- The per-file cap the oversize case measures against. [9]
- The report path the entry point owns. [10]
- The entry point that drives the acceptance, removes its temporary root and exits on a failed invariant. [11]

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.
