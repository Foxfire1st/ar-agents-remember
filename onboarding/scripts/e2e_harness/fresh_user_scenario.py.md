# scripts/e2e_harness/fresh_user_scenario.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/e2e_harness/fresh_user_scenario.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:50+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[scripts/e2e_harness/overview.md](overview.md)

## Purpose

Drive the **fresh-user end-to-end acceptance**: one clean-room repository's first hour, per step,
through the product's own entry points, recorded as one transcript.

The packet's flow, in order, against the fixtures `fresh_user_fixture` creates:

```
install runtime -> memory_init (with the spear-branch choice) -> thin bootstrap (c-03)
-> exclusion review -> baseline adoption -> first worktree task (light leaf)
-> citation_fix + memory_quality_check + closeout validation
```

Every step runs the product's own entry point, records the exact call it made and the real result
it got, and **never summarises**: a sentence like "the bootstrap succeeded" is not evidence, the
transcript is. A step that cannot run in this environment is recorded as `blocked` with the exact
reason and with what evidence would have been required.

## Code Commentary

### Logic

`run_fixture_scenario` drives the ordered steps for one fixture and `run_fresh_user_acceptance`
runs both fixtures, collects the invariants and checkpoints, and returns the transcript document.
`StepRecord` is the unit of evidence — one call, one real result, one status.

`_assert_candidate_source()` runs **before the first product call** and the transcript records
`packageSource` per step. This is load-bearing, not decorative: `MCP_SRC` must be inserted into
`sys.path` as a **string**, because a non-`str` `sys.path` entry is silently ignored by the import
machinery — the interpreter's editable install would then answer every import from the primary
checkout while every line of this module still looked right.

The steps:

| Step | What it does |
| --- | --- |
| `install-runtime` | the product's runtime install entry point |
| `memory-init` | `initialize_memory` with the fixture's spear-branch choice |
| `thin-bootstrap-c03` | the `c-03` thin bootstrap, recorded as `emulated-outcome` and stated as such |
| `exclusion-review` | persists the exclusion register (status `persisted`) |
| `baseline-adoption` | memory baseline adoption, plus the first ledger row |
| `fixture-memory-series-branch` | the **declared fixture setup** that makes the memory series branch exist |
| `first-worktree-task` | the ordered worktree starts, through `worktree_start_tool` |
| `citation-fix` | a **real `citation_fix` call** (`dryRun: true`) once the enclosure contract exists; when it does not, `citation_fix_blocked` records the step `blocked` **by name** rather than `completed` |
| `memory-quality-check` | the closeout gate's own declared check group over the fixture's memory root |
| `closeout-validation` | closeout validation over the produced state |
| `free-agent-bootstrap-seat` | a **free agent** opened the way a user opens it — the product's registered `POST /api/terminal/{session}` with `role='bootstrap'` and **no task document** |

### The free-agent step reads the capsule from the consumer side

`free_agent_acceptance` opens the seat through the product's own route and reads the capsule back
**from the artifact that launch produced**: the encoded launch token the child process is started
with, parsed by the product's own `parse_runner_config`. The expected side is the same application
entry point the route itself calls (`compile_launch_capsule` with a `LaunchCapsuleRequest`), so
**neither side is hand-supplied**. The step records `routeStatus`, `instructionMode`,
`equalsCompilerResult`, `routeDigestEqualsSessionDigest`, and a `sessionReceived` block carrying
the byte count and the digest the session actually received.

This is what closes the standing rule: *a delivery claim is closed by a production path from
producer to consumer, with the artifact read from the consumer's side — never a seam plus a
caller-supplied value.*

### The blocked entry is derived from the run's own records

`first_worktree_task_blocked(records, chains)` builds `result.refusals` by reading the
`StepRecord`s the run already wrote — every `first-worktree-task` record whose status is `failed`
or `refused` — so the entry and the transcript's `steps` **can only agree**. Nothing is asserted
about attempts the transcript does not carry. It fires only when not every chain's work branch
exists; at a clean run it adds nothing.

### Invariants And Boundaries

`INVARIANTS` asserts four readings **per fixture**: no bootstrap content in the first memory
commit, no confidence tags in durable onboarding, the first ledger row, and a working first
worktree task.

The module's `WHAT THIS SCENARIO DOES AND DOES NOT CERTIFY` section states the boundary, and the
divergence between that section and the code is a recorded finding, not a claim this card makes:

- It certifies the **chain** over disposable fixtures created by the harness: two repositories from
  nothing, the register persisted, the baseline adopted, the invariants asserted.
- The module docstring still says it "does not certify the free-agent bootstrap seat, because at
  this base nothing delivers a compiled capsule into an opened session … and the scenario records
  it as blocked". **The code no longer matches that sentence.** Since this leaf synced onto the
  wiring leaf's landing, `free_agent_acceptance` opens the seat through the product's route and
  reads the capsule back from the launched token, and the delivered transcript records the step as
  `completed` with the digest agreement asserted. The docstring is stale source text; the code is
  the conduct. This is recorded for the owning seat and is not repaired here — this seat writes
  memory, never code.

### Conventions

- One `StepRecord` per call; the transcript, not prose, is the evidence.
- Fixtures are **disposable repositories the harness creates from nothing** under one run root.
  They are **not** the developer's repositories.
- `memory-quality-check` on a fresh card reports `ok:false` **with findings**. That is the honest
  `checked` state of a brand-new memory layer, not a run failure; the step's own status is
  `refused`, and the transcript states it that way.
- The scenario is a **governed evidence artifact** with an `[[artifact]]` row in
  `mcp/tests/evidence-lifecycle.toml` (`owner: fresh-user-acceptance`,
  `introduced_by: 260915-CAPS-L14`).

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one step record: the call made and the real result it returned. | `StepRecord` | scripts/e2e_harness/fresh_user_scenario.py:172-194 |
| Why `MCP_SRC` must be a **string** in `sys.path`: the import machinery silently ignores a `Path`. | `MCP_SRC` | scripts/e2e_harness/fresh_user_scenario.py:47-47 |
| The candidate-source assertion that runs before the first product call, and the per-step provenance it records. | `_assert_candidate_source`; `package_source` | scripts/e2e_harness/fresh_user_scenario.py:207-214; scripts/e2e_harness/fresh_user_scenario.py:217-226 |
| The ordered steps for one fixture. | `run_fixture_scenario` | scripts/e2e_harness/fresh_user_scenario.py:579-807 |
| The two-fixture acceptance, its invariants and its transcript. | `run_fresh_user_acceptance` | scripts/e2e_harness/fresh_user_scenario.py:1099-1183 |
| The free agent's capsule, read back from the launch token the session was actually started with. | `free_agent_acceptance` | scripts/e2e_harness/fresh_user_scenario.py:936-1039 |
| The citation step is a real `citation_fix` call once the enclosure contract exists. | `_citation_fix` | scripts/e2e_harness/fresh_user_scenario.py:828-840 |
| The citation step when no enclosure contract exists: blocked by name, never completed. | `citation_fix_blocked` | scripts/e2e_harness/fresh_user_scenario.py:843-863 |
| The blocked entry is built from the run's own step records, so it cannot disagree with them. | `first_worktree_task_blocked` | scripts/e2e_harness/fresh_user_scenario.py:1042-1096 |
| The ordered worktree starts the product's authority requires. | `_worktree_topology`; `_start_leaf_worktree` | scripts/e2e_harness/fresh_user_scenario.py:335-405; scripts/e2e_harness/fresh_user_scenario.py:408-436 |
| The declared fixture setup that creates the memory series branch. | `_declare_memory_series_branch` | scripts/e2e_harness/fresh_user_scenario.py:473-500 |
| The four per-fixture invariants. | `_invariant` | scripts/e2e_harness/fresh_user_scenario.py:1186-1200 |
| The register the citation and memory-quality steps honour. | `write_exclusion_register` | scripts/e2e_harness/fresh_user_fixture.py:180-207 |
| The step that must never be `completed` when it could not run. | `test_a_step_that_cannot_run_is_blocked_by_name_and_not_completed` | mcp/tests/test_fresh_user_harness.py:192-216 |
| The delivered transcript these ranges are read against. | `REPORT_DIRECTORY` | scripts/e2e_harness/run_fresh_user.py:32-32 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `MCP_SRC` repointed to scripts/e2e_harness/fresh_user_scenario.py:47-47. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_assert_candidate_source`; `package_source` repointed to scripts/e2e_harness/fresh_user_scenario.py:217-226; scripts/e2e_harness/fresh_user_scenario.py:207-214. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `run_fresh_user_acceptance` repointed to scripts/e2e_harness/fresh_user_scenario.py:1099-1183. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `free_agent_acceptance` repointed to scripts/e2e_harness/fresh_user_scenario.py:936-1039. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `first_worktree_task_blocked` repointed to scripts/e2e_harness/fresh_user_scenario.py:1042-1096. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_invariant` repointed to scripts/e2e_harness/fresh_user_scenario.py:1186-1200. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T10:50+02:00 — 260915-CAPS-L14 curator: created this card for the scenario the leaf adds. Records the ordered flow, the `StepRecord`-per-call evidence rule, why `MCP_SRC` must be a **string** in `sys.path` (a `Path` is silently ignored and the editable install answers from the primary checkout), the register/baseline/worktree/citation/quality steps, the free-agent step reading the capsule **from the launch token the session was actually started with** with the expected side taken from the same application entry point the route calls, and the blocked entry being derived from the run's own records. Adds a section recording that the module docstring's "does not certify the free-agent bootstrap seat … records it as blocked" sentence is **stale source text contradicted by the code since this leaf synced onto the wiring landing** — reported to the owning seat, not repaired here. States the fixtures are disposable and **not** the developer's repositories. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.
