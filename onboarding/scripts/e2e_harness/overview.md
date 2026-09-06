# Ambient Role-Chat E2E Harness Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `scripts/e2e_harness` |
| onboardingRoute | `onboarding/scripts/e2e_harness/overview.md` |
| parentOverview | [Repository overview](../../overview.md) |
| lastUpdated | 2026-09-05T07:12+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |

## What This Area Is

This route is the clean-room, real-consumer acceptance harness for ambient and hosted Agents
Remember role spawning. It runs the pinned Codex CLI/app-server against the candidate MCP server,
uses a deterministic local Responses API only for model-side choices, creates disposable code and
coordination repositories, and proves the canonical seat and replacement-routing contracts twice
from fresh state.

## Hot Path Summary

Start with `run.py` for candidate/run ownership, `scenario.py` for checkpoints L5-C01 through
L5-C08, `codex_driver.py` for the real Codex boundary, and `responses_server.py` for deterministic
tool discovery and calls. `dispatch_sentinels.py` owns the controlled malformed-advertisement
proofs. `selection.py` validates the profile-owned applicability decision before a replication starts.

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

## Structures Found Here

The route separates candidate orchestration (`run.py`), fixture construction (`fixture.py`), real
Codex driving (`codex_driver.py`), deterministic Responses API behavior (`responses_server.py` and
`responses_sse.py`), controlled public-advertisement rejection proofs (`dispatch_sentinels.py`),
scenario flow/control/evidence/runtime modules, structured checkpoint reports, and exact dependency
selection.

## Operating Model

1. Dagger invokes `run.py` with an exact diff base, report directory and admitted source-selection artifact.
2. `run.py` proves Dagger admission before parsing arguments, creating reports, or touching tmux.
Candidate hashing uses a temporary index outside the repository and refuses an in-repository
scratch location; inspection cannot add its own index file to the candidate being measured.

3. The repository profile owns targeted dependency selection and full-mode applicability. The runner independently verifies its admitted candidate/base/mode selection and refuses a not-applicable decision; zero-start teardown proof belongs to the profile adapter.
4. Each of two fresh replications creates isolated repositories, MCP/Codex configuration, dashboard,
   tmux server, and deterministic Responses endpoint. Codex forwards the fixture `TMUX_TMPDIR` to
   its MCP child so every dispatched role occupies that same server.
5. Real Codex discovers `dispatch_agent`, builds the ambient-to-worker chain, and exercises manager
   retirement, vacancy, replacement, queued rebinding, and direct post-replacement delivery. C09
   validates success from the structured public result after strictly normalizing Codex's current
   `Wall time`/`Output` execution envelope.
6. The exact ambient dispatch is repeated once and must retain its original architect occupant;
   live schema/description mutations must fail through the shared canonical validator.
7. Each checkpoint records expected, actual, owner, and requirement before a failure is raised.
8. Teardown owns every spawned process/session and preserves secondary cleanup failures separately;
   the summary preserves exact candidate identity,
   command, run count, retry count, and per-run artifacts.

## Main Flows

### Real Ambient-To-Hosted Spawn

1. An ambient Codex thread discovers the candidate MCP server and calls `dispatch_agent`.
2. A second identity-free ambient call uses the same request and converges on that occupant.
3. The architect receives the byte-exact compiled canonical brief.
4. Architect, orchestrator, and manager seats use the same public tool to reach the worker.

### Vacancy And Replacement

1. The worker posts to the canonical master/manager seat.
2. The orchestrator retires the current manager, leaving a real vacancy.
3. A worker message persists without a private occupant address.
4. A replacement manager starts; queued and later messages resolve to that occupant without
   repointing the canonical address.

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

## Local Invariants And Traps

- The deterministic Responses server is not an MCP or Codex fake; it controls only model output.
- A targeted skip is legal only when no changed path intersects the explicit dependency surface.
- Both replications are fresh attempts; a retry after failure is forbidden and reported as zero.
- The deliberate same-seat dispatch is requirement behavior, not a retry attempt.
- Product messages use `(task_document_ref, role)` only. Runtime session ids are stimulus and
  observation data, never product addresses.
- The persisted architect brief must byte-match the canonical compiled template.
- Failure diagnostics are bounded and actionable; they must not copy secrets or complete prompts.
- Teardown is mandatory on pass and failure; a residual tmux session or structured cleanup error
  fails L5-C10 while remaining secondary to an earlier scenario failure.
- The tmux server is addressed only through a fixture-owned `TMUX_TMPDIR`; inherited `TMUX` state or
  a host invocation is rejected before any destructive server command.
- Codex's MCP whitelist must forward that dynamic `TMUX_TMPDIR`; setting it only in the outer
  scenario would create a split namespace that makes liveness and teardown inspect the wrong server.
- The summary plus both candidate-bound run reports are nested durable artifacts in the one
  immutable quality-report generation; publication cannot discard them by flattening the export.
- Tool-result normalization recognizes only direct structured JSON or the exact current Codex
  execution envelope; unknown wrappers fail C09 instead of being searched for a favorable field.

## Repo-Internal References

The Dagger quality graph owns invocation, while this route owns only the real-consumer scenario and
its candidate-bound evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The controller runs exactly two fresh, retry-free replications and emits a candidate-bound summary. | `main` | scripts/e2e_harness/run.py:21-75; scripts/e2e_harness/run.py:107-203 |
| The scenario proves the live spawn chain and replacement-routing sequence through named checkpoints. | `run_scenario` | scripts/e2e_harness/scenario.py:141-194; scripts/e2e_harness/scenario.py:368-531 |
| The deterministic provider discovers tools from the real request and validates the public dispatch schema. | `ScriptedResponses` | scripts/e2e_harness/responses_server.py:47-127; scripts/e2e_harness/responses_server.py:329-381 |
| Controlled malformed advertisements must fail through the same canonical validator as the live advertisement. | `dispatch_rejection_sentinels` | scripts/e2e_harness/dispatch_sentinels.py:23-95 |

## Cross-Repo References

No cross-repository implementation dependency governs this route. The disposable coordination and
code repositories are fixture-owned representations of this repository's public contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external repository supplies implementation logic to this harness. | `create_fixture` | scripts/e2e_harness/fixture.py:43-112 |

## Docs References

No Domain Documentation source is configured for this repository. The Codex version/protocol claim
is verified at runtime by the real installed client rather than copied from an external prose source.

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime evidence records the negotiated Codex client/app-server boundary used by the scenario. | `_run_ambient_codex` | scripts/e2e_harness/codex_driver.py:100-194; scripts/e2e_harness/codex_driver.py:221-252 |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `README.md` | [README.md.md](README.md.md) | covered | Security, provider, version, and run semantics |
| `codex_driver.py` | [codex_driver.py.md](codex_driver.py.md) | covered | Real Codex boundary |
| `dispatch_sentinels.py` | [dispatch_sentinels.py.md](dispatch_sentinels.py.md) | covered | Canonical negative-advertisement proofs |
| `fixture.py` | [fixture.py.md](fixture.py.md) | covered | Clean-room topology and configuration |
| `reporting.py` | [reporting.py.md](reporting.py.md) | covered | Structured checkpoint evidence |
| `responses_server.py` | [responses_server.py.md](responses_server.py.md) | covered | Deterministic tool-driving server |
| `responses_sse.py` | [responses_sse.py.md](responses_sse.py.md) | covered | Responses SSE wire projection |
| `run.py` | [run.py.md](run.py.md) | covered | Candidate and replication controller |
| `scenario.py` | [scenario.py.md](scenario.py.md) | covered | End-to-end flow and assertions |
| `scenario_control.py` | [scenario_control.py.md](scenario_control.py.md) | covered | Bounded public control stimulus |
| `scenario_evidence.py` | [scenario_evidence.py.md](scenario_evidence.py.md) | covered | Failure and routing evidence |
| `scenario_runtime.py` | [scenario_runtime.py.md](scenario_runtime.py.md) | covered | Resource preparation and teardown |
| `selection.py` | [selection.py.md](selection.py.md) | covered | Exact targeted dependency surface |

## Child Overviews

No child route currently needs a separate overview.

## How To Use This Area

When changing this route, first decide whether the change affects candidate ownership, real Codex
driving, scripted provider behavior, scenario semantics, evidence, or teardown. Preserve the split,
update the exact dependency surface when adding a load-bearing input, and keep the one certifying
execution owned by the lifecycle Dagger gate.

## Needs Verification

None.

## Update History

- 2026-09-05T07:12+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Documented external temporary candidate-index ownership and preserved twice-fresh no-retry scenario semantics. Verification records source review, not execution or acceptance.

- 2026-08-31T10:33+02:00 — 260821-ARSPAWN-L5 closeout repair: documented the strict Codex
  execution-envelope normalization required for C09 to read the successful public dispatch results
  observed in generation 6. Verification remains closeout-owned.

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: recorded the cross-process tmux
  namespace contract and the Codex MCP whitelist that preserves it. Verification remains
  closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded pre-side-effect
  Dagger admission, exact fixture-owned tmux isolation, and recursive immutable publication of all
  three E2E evidence files. Verification remains closeout-owned.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T22:11:35+02:00 — 260821-ARSPAWN-L5: separated controlled malformed
  advertisement proofs from the deterministic provider and reduced acceptance evidence to small,
  independently readable predicates. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: recorded identity-free same-seat
  convergence, canonical live-advertisement sentinels, positive tool results, and non-suppressing
  cleanup evidence. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created the route overview for the real Codex 0.151.0 ambient/hosted spawn and replacement-routing acceptance harness. Verification metadata remains closeout-owned.
