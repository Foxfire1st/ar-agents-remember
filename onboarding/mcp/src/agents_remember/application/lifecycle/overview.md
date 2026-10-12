# Application Lifecycle Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/lifecycle` |

## Governing Overview

[Application overview](../overview.md)

## What This Area Is

Application adapters for admitting configured contracts, locating durable lifecycle operations, resolving caller authority, and exposing the direct-landing route. They translate configuration and caller context into worktree-domain requests and public refusals; journal transition policy belongs to the worktree lifecycle domain.

The directory also retains an internal ambient-lifecycle block builder and a typed terminal rail-failure projector. Their presence does not establish a public tool registration or an active execution caller.

## Hot Path Summary

Use `configured_contract_admission.py` for configured-contract admission and refusal projection, `direct_landing.py` for the public direct route, and `lifecycle_operation_location.py` for exact configured operation locations and retained-journal observations. `certification_refusal.py` renders complete typed certification findings; `lifecycle_control_authority.py` resolves caller identity and completed-disposition authority.

Public closeout and integration run synchronously through `application/worktree_tools.py` and the worktree module owners. The former detached-worker, public status-wait, legacy-bridge, and enclosure application entry-point files are absent. `terminal_rail_failure.py` retains its envelope-building functions, but no current production caller of `terminal_worker_failure_result` was found.

## How It Is Built

The direct-landing boundary selects a canonical granted leaf and preserves the durable generation recovery owner. Verify-existing and exact-pair create are explicit modes, not fallback closeout; typed refusal retains nextAction and interrupted pair evidence.

Configured admission confines the contract address to coordination authority, resolves its durable location, reads the contract, checks configured repositories, and verifies that the contract matches the location. Candidate-worktree identity is checked by default. Closeout explicitly delegates that check downstream; configured repository authority and contract-location matching remain at admission. Its publication owner checks ordinary worktree repository and branch identity and revalidates the admitted candidate before committing.

`direct_landing.py` checks the direct-execution policy, admits the configured contract, invokes the worktree direct-landing owner, and projects input, journal, and domain refusals. Direct landing is a distinct branch-addressed route, not an implicit fallback from closeout. Its domain owner requires a series contract, an intent note, and an exact code commit; it retains a synchronous durable generation and recovery controls for memory publication.

[`certification_refusal.py`](certification_refusal.py.md) renders every typed admission finding, including nested byte evidence. Its `gateStarts: 0` refusal field reports the admission boundary; the renderer itself neither observes processes nor changes journal state. A typed `routeReview` finding adds the shared route-review refusal projection while preserving the complete findings list. Exact contract-bound next-step arguments are added when a contract is available. This projection does not record a review or mutate task state.

`lifecycle_operation_location.py` binds a confined contract path to its configured task-owned location. If contract bytes become unreadable, it projects retained strict journals; when no retained operation exists, it preserves the proven initial-contract publication loss as a developer-decision refusal. `lifecycle_control_authority.py` resolves a hosted caller or an explicit declaration and derives completed-disposition ownership from live task topology.

`lifecycle_tools.py` retains the internal ambient-lifecycle block builder and its response adapter. Its source documents the removal of the six model-invoked lifecycle signal tools; the retained builder is not evidence that those tools are registered.

The read-only wait implementation survives in the worktree observation domain. It validates a positive revision cursor, polls the addressed generation with a bounded deadline, and returns change, unchanged timeout, or typed journal/generation outcomes. No current production caller of `wait_for_lifecycle_change` was found; it is not a public status-wait surface.

`terminal_rail_failure.py` constructs bounded typed envelopes from a validated published rail report or from the supplied error. It distinguishes `gate-result`, `terminal-rail-result-unavailable`, and `worker-execution-unclassified`, preserving candidate identity and bounded evidence rather than inventing a rail outcome. Its retained implementation does not establish an active detached-worker failure boundary.

### File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `certification_refusal.py` | [certification_refusal.py.md](certification_refusal.py.md) | covered |
| `configured_contract_admission.py` | [configured_contract_admission.py.md](configured_contract_admission.py.md) | covered |
| `direct_landing.py` | [direct_landing.py.md](direct_landing.py.md) | covered |
| `lifecycle_control_authority.py` | [lifecycle_control_authority.py.md](lifecycle_control_authority.py.md) | covered |
| `lifecycle_operation_location.py` | [lifecycle_operation_location.py.md](lifecycle_operation_location.py.md) | covered |
| `lifecycle_tools.py` | [lifecycle_tools.py.md](lifecycle_tools.py.md) | covered |
| `terminal_rail_failure.py` | [terminal_rail_failure.py.md](terminal_rail_failure.py.md) | covered |

The preserved table statuses are onboarding metadata, not operative lifecycle promises. No external Domain Documentation source is configured; the inspected boundaries are between repository-owned application and worktree owners.


## Invariants And Boundaries

- Application adapters project lower-level failure families at their boundary; callers should consume those public projections rather than duplicate the exception vocabulary.
- Delegating candidate identity does not waive configured repository or contract-location authority. The downstream publication owner must still validate the candidate it commits.
- Retained strict journal and enclosure evidence governs unreadable-contract observations; a task projection is not replacement authority.
- Direct landing remains distinct from ordinary closeout and integration. The synchronous ordinary route has no detached worker lease or worker composition root.
- Closeout preserves approval, source-lineage, candidate, and publication checks. Integration preserves approval, contract authority, source ancestry, and ref safety. Neither synchronous call is itself an invocation of a full test suite or an independent review.
- Absence of automatic full-suite execution does not mean absence of memory enforcement. Converted leaf closeout checks the mandatory invariant gate before claiming approval or committing code, and validates the exact memory output before its publication. Recovered converted memory output is checked too. Direct landing also retains converted-memory gate and validation checks.
- `worktrees/modules/onboarding.py::validate_memory_refresh_attestations` composes independent sidecar and governing-route body/history checks. Curator memory preparation calls it on the unconverted-tree branch; converted trees use the onboarding-trace gate. Current closeout refreshes sidecar and route metadata through their refresh owners rather than calling this shared validator directly.


## Evidence

- The bounded read-only observer validates the cursor, polls the exact generation, and returns change or timeout. [1]

- Configured admission checks repository and contract-location authority while permitting only an explicit candidate-identity delegation. [2]
- Ordinary converted-leaf closeout checks its mandatory gate before approval or code publication and validates its exact memory output and recovered output before memory publication. [3]
- Typed admission findings are projected completely; rail-failure and status-wait construction remains retained capability rather than a registered detached execution route. [4]
- Unreadable contract observations prefer retained strict journals and otherwise preserve proven initial publication loss as a developer-decision refusal. [5]
