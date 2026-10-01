# mcp/tests/selected_lifecycle_test_support.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Builds the selected lifecycle fixture door through the real task, route-review, atomic-series and
door owners. The fixture keeps its authored prerequisites distinct from certification execution and
returns a declared waiting door whose declared identity is never the synthetic `test-fixture:` form.

## Code Commentary

### Logic

`declare_selected_candidate` reloads the contract and preserves an existing door. For an undeclared
leaf it resolves the actual terminal leaf document, writes fixture requirements and a completed
setup step, obtains canonical task context, and activates atomic series selection under the
integration authority lock when the master is atomic. It authors a route-review record plus fixture
judgment/priority rows and, for external memory, fixture curator evidence, then invokes the actual
door owner with the fixture manager's task identity. It requires a waiting door whose declared
identity is not the synthetic `test-fixture:` form. The authored prerequisites are test setup; this
helper does not run full memory certification.

`selected_closeout_operation_input` declares the prepared candidate before normalizing input through
the shared closeout-input owner. `selected_contract` reuses the public-entrypoint fixture, reloads
the contract and requires its live waiting door with a non-synthetic declarer. Existing doors are
never silently replaced to make later mutations current.

### Conventions

Callers install profiles and prepare candidate bytes before declaration. Scenario mutations stay in
consumer tests. Fixture actor and scheduling data belong to the isolated task world and grant no
host lifecycle authority.

### Invariants And Boundaries

- Declared fixture doors come from the actual owner; existing doors are preserved.
- The fixture never invents a synthetic declarer identity, so downstream declaration provenance
  assertions still see the real actor.
- The helpers do not replace the selected-operation guard or implement a parallel production
  closeout workflow.
- Completion bookkeeping for integration is not part of this module: the former
  `ready_selected_integration`, `finish_closeout_for_integration`,
  `completed_selected_closeout_for_integration`, `selected_successor` and
  `replace_selected_fixture_generation` helpers were deleted deliberately by commit `173bb01e`
  (2026-09-10, the detached-lifecycle-worker deletion), not lost. `git log -S
  'finish_closeout_for_integration' -- mcp/tests` names that commit.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

No configured external domain source governs this file.

### Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described
above.

- Task, route-review, series and door owners declare the prepared candidate while preserving existing doors. [1]
- Input normalization follows explicit declaration. [2]
- Public-entrypoint fixture reuse requires a live non-synthetic waiting door. [3]

### Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file
establishes no external repository or host lifecycle authority.

No cross-repository evidence is required.
