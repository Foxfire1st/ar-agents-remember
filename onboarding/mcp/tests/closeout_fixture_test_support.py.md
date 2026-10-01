# mcp/tests/closeout_fixture_test_support.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides the one waiting-door fixture the closeout boundary suites still consume. The module
constructs a queued fixture for a requested memory mode and declares the master; it grants no
operation, commit, admission, or certification authority.

## Current Fixture Boundary

Closeout and integration are synchronous. The queued-operation fixtures that used to live here
drove the detached worker through `OperationRuntime`; commit `173bb01e` (2026-09-10, "Delete the
detached lifecycle worker and drive every fixture on the synchronous path") deleted that worker and
removed the fixtures with the driving tests that had already been rewritten on the public tool
surface. Only the waiting-door fixture kept a consumer, so this module now holds a single helper and
re-exports nothing. The removal was deliberate, not a lost file: `git log -S '_PendingMemory' --
mcp/tests` names the same commit.

## Code Commentary

### Logic

`selected_fixture` builds a `QueueFixture` from `test_closeout_queue` for the requested memory mode
and declares `MASTER_A`, returning the fixture. Selection therefore comes from the queue fixture's
own door/projection truth rather than from a retained queue lifecycle row, and the helper neither
claims nor starts a closeout operation.

### Conventions

Call the fixture when a test genuinely needs waiting-door source state. Scenario-specific mutations
stay in callers; this module implements no production behavior and adds no shortcut around the
public admission, review, or gate-acceptance owners.

### Invariants And Boundaries

- Waiting-door selection alone grants no operation, commit, or certification authority.
- The fixture reaches production behavior only through `QueueFixture`; this module composes
  nothing on top of it.
- The removed queued-operation fixtures are not replaced here: a test that needs public
  selected-operation behavior drives the public tools directly.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.
The retained history records the fixture's earlier scheduling-only role.

No configured external domain source governs this helper.

### Repo-Internal References

- The waiting-door fixture builds a queue fixture for the requested memory mode and declares the master. [1]

### Cross-Repo References

No independent cross-repository protocol is established here. Temporary external-memory fixtures
exercise the repository's own contract and ledger writers.

No separate cross-repository evidence is required.

## Current Contract

`selected_fixture` derives selection from current door and projection truth rather than a retained
queue lifecycle row, and it returns a `QueueFixture` whose only declared input is `MASTER_A`.

### Current Invariants

- `selected_fixture` creates waiting-door source state for the requested memory mode without
  granting claim, operation, commit or certification authority.
- The module no longer exposes pending-memory doubles, public-apply wrappers, or component writer
  helpers: those fixtures were removed with the detached-worker tests they served.
