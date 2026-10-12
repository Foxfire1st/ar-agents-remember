# Ambient Role-Chat E2E Harness Overview

## What This Area Is

This route contains acceptance harnesses for ambient and hosted Agents Remember role spawning and for a fresh user's initial repository workflow. The ambient harness drives real Codex CLI/app-server processes against the candidate MCP server, supplies deterministic model-side choices through a local Responses API, and constructs disposable code and coordination repositories. Its controller schedules two fresh replications to check canonical seats and replacement-aware routing; that describes the harness's intended checks, not a newly demonstrated acceptance result.

## Hot Path Summary

Start with `run.py` for candidate and replication ownership, `scenario.py` for runtime, spawn, brief, routing and discovery checkpoints, and `codex_driver.py` for the real Codex boundary. `responses_server.py` selects deterministic tool calls from advertised tools; `dispatch_sentinels.py` checks controlled malformed dispatch advertisements. `selection.py` verifies the admitted profile decision before replications start. The separate host entry point is `run_fresh_user.py`, backed by `fresh_user_fixture.py` and `fresh_user_scenario.py`.

## Construction And Operating Model

The route separates candidate orchestration, disposable fixture construction, real Codex driving, deterministic Responses behavior and SSE projection, advertisement rejection checks, scenario control and evidence, resource teardown, and structured reporting. Product spawning, seat and routing logic belongs under `mcp/src/agents_remember/`; fast regressions belong under `mcp/tests/`; quality-graph orchestration belongs under `.dagger/src/agents_remember_quality/`.

The two entry points have different admission boundaries. `run.py` requires Dagger admission before parsing arguments or creating reports. It accepts an exact diff base, report directory, mode and source-selection artifact. Candidate hashing uses a temporary index outside the repository and refuses an in-repository scratch directory. `selection.py` requires the `ambient-role-dependencies` selector, matching mode, an applicable decision, and source-selection facts matching the observed candidate tree and diff base. The standing profile contract permits targeted omission only outside the dependency surface; a not-applicable decision must not start this runner.

The ambient controller schedules exactly two fresh replications and records zero retries. Each scenario constructs disposable repositories, task topology, external memory, authority settings and Codex configuration; starts an isolated tmux namespace and dashboard; and supplies a local Responses endpoint. The Codex MCP configuration forwards `TMUX_TMPDIR`, so dispatch-created sessions share the namespace inspected by liveness and teardown. The fixture compiles the architect brief from the canonical template and rejects unresolved placeholders.

An identity-free ambient Codex call discovers `dispatch_agent` and launches the architect. After the initial brief is accepted, the same ambient dispatch is repeated once; the checks require the original architect occupant and brief row to survive. Scripted architect, orchestrator and manager calls use `dispatch_agent` to build the chain through worker. Worker initial, intermediate and later traffic uses `role_message` with the canonical master task and manager role. Live dispatch advertisements and controlled missing-brief and missing-ambient-description variants use the same canonical validator.

The scenario still contains a vacancy-and-replacement contract: initial worker delivery, manager termination with no active manager seat, an unaddressed `no-hosted-session` intermediate row, queued delivery to a different manager, and direct later delivery to that replacement. Its current stimulus disagrees with that sequence. The scripted `orchestrator-retire` action now requests `dispatch_agent` for manager B, and C05's description names replacement creation, while `_retire_manager` still waits for the old manager to terminate and for the manager seat to be empty. The card retains the vacancy contract as standing intent and discloses this source discrepancy; it does not claim that dispatch currently creates a real vacancy or that the scenario passes.

Checkpoint reporting records requirement, expected value, actual value and owner before raising a failed checkpoint. Scenario teardown runs in `finally`; cleanup errors are retained separately. The controller writes candidate-bound run reports and a summary containing candidate identity, command, replication count, retry count and report paths. The quality profile's result projection names the summary and both nested run reports. Immutable publication and complete export preservation remain the standing delivery boundary; this bounded inspection did not verify the publication implementation.

### Fresh-User Flow

The separate host invocation is:

```
python scripts/e2e_harness/run_fresh_user.py --reports <dir> [--work-root <dir>]
```

The runner uses a temporary run root unless one is supplied. The scenario recreates its two owned fixture directories: `spear-not-main`, with spear `dev`, oversized inputs and a vendored tree, and `plain-main`, with spear `main`. These are disposable fixture repositories, not the developer's repositories. Candidate package identity and the fixture authority path are checked explicitly. Fixture construction is local to its root; the overall runner also reads candidate package inputs and interpreter/environment facts and writes its transcript under the separately supplied reports directory. It therefore does not promise that all reads and writes stay beneath the run root.

The ordered flow invokes runtime installation, memory initialization, baseline adoption and worktree start through imported product entry points. Thin bootstrap is explicitly recorded as `emulated-outcome`: it writes the minimum artifact rather than executing the LLM-driven c-03 procedure. Exclusion review is represented by persistence of the register and recorded as `persisted`, not by execution of the judgment itself. Citation fixing is attempted when a leaf contract is available; otherwise a named blocked record is added. Memory-quality checks exercise the closeout citation-check function, while the full closeout transaction is explicitly outside this flow. Product-call records distinguish completed, refused and failed results; blocked records are used for specifically unreachable operations.

The bootstrap capsule check calls the registered `POST /api/terminal/{session}` route with role `bootstrap` and no task document, using a recording terminal-host boundary double. It parses the token in the recorded launch specification with the product's `parse_runner_config` and compares trusted instructions and semantic digest against `compile_launch_capsule`. This verifies the launch artifact produced by the route; it does not start a real child process or prove that a child received the capsule.

The runner writes `<reports>/fresh-user-acceptance/run.json`, prints the transcript location and counts, then prints any failed and blocked records. Its exit code is non-zero when an invariant or checkpoint is not passed. That exit predicate does not independently reject every failed or blocked step record.

## Local Invariants And Boundaries

- The ambient Responses server controls model output; it does not replace the MCP server or Codex process. The fresh-user terminal opening has a separately declared boundary double.
- Two planned fresh ambient replications and zero retries are controller behavior. The same-seat ambient repeat checks idempotency rather than retrying a failure.
- Canonical manager-message checks require the task document and role, with no agent or lifecycle address. Runtime session identifiers are used for control stimulus and delivery observation.
- The accepted architect brief must byte-match the compiled canonical template.
- Teardown must run on success and scenario failure. Residual-session and cleanup checks contribute L5-C10 failure; cleanup diagnostics must remain visible alongside an earlier failure.
- Destructive tmux commands require the fixture-owned `TMUX_TMPDIR` and reject inherited `TMUX`. Preparation clears inherited `TMUX` and configures the isolated server before role sessions are created.
- Codex's MCP environment whitelist must forward the dynamic `TMUX_TMPDIR`; outer-process configuration alone would leave namespace ownership inconsistent.
- Diagnostics are intended to be bounded and exclude secrets and complete prompts. Current failure evidence includes full event, catalog and inbox collections, and the controller records exception tracebacks; this inspection does not establish that all diagnostic output satisfies that intent.
- C09 requires successful dispatch-result evidence. Its normalizer recognizes JSON and the specific `Wall time`/`Output` envelope, but recursively searches mappings and lists for an `ok` boolean. The former promise that unknown wrappers are never searched is stronger than the implementation.
- Keep the candidate-bound summary and both run reports together in the durable quality-report generation. Source inspection is not test execution, native-host acceptance, whole-build certification, landing approval or memory acceptance.

## Lifecycle And Coverage Metadata

These retained metadata tables describe the card's recorded routes and coverage labels. They are outside operative acceptance promises; `covered` does not mean a test was executed in this review.

| Field | Value |
|---|---|
| sourceRoute | `scripts/e2e_harness` |
| onboardingRoute | `onboarding/scripts/e2e_harness/overview.md` |
| parentOverview | [Repository overview](../../overview.md) |

## What Belongs Here

| Path | Role |
|---|---|
| `scripts/e2e_harness/README.md` | Operator-facing boundary and invocation contract |
| `scripts/e2e_harness/*.py` | Candidate-bound, process-level acceptance fixtures for public ambient/hosted spawning |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
|---|---|
| Product spawning, seat, or routing logic | `mcp/src/agents_remember/` |
| Fast unit and contract regressions | `mcp/tests/` |
| Quality-graph orchestration and container construction | `.dagger/src/agents_remember_quality/` |

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `run.py` | acceptance controller | Owns exact candidate, two fresh runs, no retry, reports, and residual-session proof | covered |
| `fixture.py` | clean-room constructor | Builds disposable repositories, task topology, canonical brief, and Codex/MCP configuration | covered |
| `codex_driver.py` | real consumer boundary | Starts Codex 0.151.0 app-server and observes normal MCP registration/discovery | covered |
| `responses_server.py` | deterministic provider | Drives only model-side tool choices while validating real advertised schemas | covered |
| `dispatch_sentinels.py` | negative contract evidence | Mutates the live advertisement and requires canonical-validator rejection at the expected boundary | covered |
| `scenario.py` | acceptance state flow | Executes and records the spawn, canonical routing, vacancy, and replacement assertions | covered |
| `scenario_runtime.py` | resource owner | Tears down tmux, dashboard, and response fixtures even on failure | covered |
| `run_fresh_user.py` | fresh-user acceptance entry point | Host-run (no Dagger admission by design); writes the one transcript and exits non-zero on any failed invariant or checkpoint | covered |

The lifecycle catalog contains permanent shared-support rows for the three fresh-user modules, naming owner `fresh-user-acceptance`, exact-source consumers and replacement test nodes. `test_fresh_user_harness.py` actually loads those modules and its retained existence test checks that their paths exist. That test alone does not validate every lifecycle-row property. These catalog declarations are not fresh lifecycle approval or acceptance evidence.

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `README.md` | [README.md.md](README.md.md) | covered | Security, provider, version, and run semantics |
| `codex_driver.py` | [codex_driver.py.md](codex_driver.py.md) | covered | Real Codex boundary |
| `dispatch_sentinels.py` | [dispatch_sentinels.py.md](dispatch_sentinels.py.md) | covered | Canonical negative-advertisement proofs |
| `fixture.py` | [fixture.py.md](fixture.py.md) | covered | Clean-room topology and configuration |
| `fresh_user_fixture.py` | [fresh_user_fixture.py.md](fresh_user_fixture.py.md) | covered | Fresh-user disposable fixtures (260915-CAPS-L14) |
| `fresh_user_scenario.py` | [fresh_user_scenario.py.md](fresh_user_scenario.py.md) | covered | Fresh-user end-to-end acceptance flow (260915-CAPS-L14) |
| `reporting.py` | [reporting.py.md](reporting.py.md) | covered | Structured checkpoint evidence |
| `responses_server.py` | [responses_server.py.md](responses_server.py.md) | covered | Deterministic tool-driving server |
| `responses_sse.py` | [responses_sse.py.md](responses_sse.py.md) | covered | Responses SSE wire projection |
| `run.py` | [run.py.md](run.py.md) | covered | Candidate and replication controller |
| `run_fresh_user.py` | [run_fresh_user.py.md](run_fresh_user.py.md) | covered | Fresh-user acceptance entry point (260915-CAPS-L14) |
| `scenario.py` | [scenario.py.md](scenario.py.md) | covered | End-to-end flow and assertions |
| `scenario_control.py` | [scenario_control.py.md](scenario_control.py.md) | covered | Bounded public control stimulus |
| `scenario_evidence.py` | [scenario_evidence.py.md](scenario_evidence.py.md) | covered | Failure and routing evidence |
| `scenario_runtime.py` | [scenario_runtime.py.md](scenario_runtime.py.md) | covered | Resource preparation and teardown |
| `selection.py` | [selection.py.md](selection.py.md) | covered | Exact targeted dependency surface |

## Child Overviews

No child route currently needs a separate overview.

## How To Use This Area

When changing this route, identify whether candidate ownership, real Codex driving, scripted provider behavior, scenario semantics, evidence or teardown is affected. Preserve those ownership boundaries and update the dependency surface for a load-bearing input. Keep certifying execution under the lifecycle Dagger gate; the separately admitted host flow supplies local-composition evidence rather than the same ambient certification.

## Needs Verification

The replacement stimulus and vacancy predicates disagree. Recorded verification metadata from the original card remains "None."; it is not a fresh verdict. Complete diagnostic bounds, profile invocation and immutable publication were not verified in this bounded inspection. No execution or new acceptance is claimed. The external requirement rationale for host admission was not independently checked; the source establishes that the two entry points have different admissions, not that they have equivalent certification authority.

## Evidence


- The controller schedules two fresh replications, zero retries and candidate-bound reports. Retained controller co-targets. Admission, replication and candidate-index predicates. [1]
- The scenario owns spawn and routing checks, including the disclosed vacancy discrepancy. Retained scenario co-target. Current checkpoint ownership, flow and replacement checks. [2]
- The deterministic provider validates live dispatch advertisements and selects dispatch and role-message actions. Retained provider discovery co-target. [3]
- Controlled malformed advertisements use the canonical validator. Rejection must occur with the expected canonical failure. [4]
- Fresh-user fixture construction owns disposable repository paths. [5]
- The fresh-user flow distinguishes product calls, emulated bootstrap, persisted review outcome and partial closeout checks. Both fresh-user fixtures and their invariant report are assembled here. Retained fresh-user flow co-targets. Product-call record status and candidate authority checks. [6]
- Bootstrap capsule comparison reads a recorded launch token. The terminal-host boundary records specifications without starting a child. [7]
- The fresh-user entry point writes a transcript and derives its exit code from invariants and checkpoints. The transcript directory constant. [8]
- The retained consumer test checks module-path existence. Actual module loading and exact-path consumer declarations. Catalog declarations for the three fresh-user support modules. [9]
- Disposable ambient repositories represent the contract rather than supplying external implementation logic. [10]
- Ambient Codex results record client version, MCP readiness and turn evidence. Retained Codex protocol-summary co-target. [11]
- Canonical brief construction and tmux environment forwarding. [12]
- Selection requires an applicable matching observed candidate decision. [13]
- Teardown preserves cleanup errors and protects destructive tmux commands. [14]
- Checkpoint values are recorded before failure is raised. [15]
- Result normalization recursively searches JSON children; failure evidence collects full collections. [16]
- Quality result projection names nested summary and replication reports. [17]
