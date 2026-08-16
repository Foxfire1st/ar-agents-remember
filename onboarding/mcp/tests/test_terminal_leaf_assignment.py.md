# mcp/tests/test_terminal_leaf_assignment.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_leaf_assignment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T04:06+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Despite its historical filename, this suite now covers structural terminal task assignment. It
tests the shared assignment helper, trusted MCP payload wrapper, and HTTP boundary against real
temporary task-document topology without spawning or controlling a terminal process.

## Code Commentary

Assignments use `TaskDocumentRef` plus role, validate that the role is legal at the document's
altitude, and arbitrate the live pair before mutation. Different roles may occupy one leaf; the
same document+role pair refuses without mutating the requester. Hand-opened harnesses require an
explicit structural role, while spawn provenance can supply a compatible role to the trusted path.

The HTTP case asserts the same seat-conflict behavior. Runtime session id remains private
administrative correlation, never the structural task address.

The suite also directly pins the legacy display-name suffix parser for the three supported
separators, case normalization, missing leaf bases, and unknown roles. This is compatibility
recognition at the serving boundary; it does not make the suffix an agent-facing identity.

## Invariants And Boundaries

- Canonical document+role is the binding identity.
- Altitude/role mismatch fails closed.
- Same-pair conflict never mutates either binding.
- Tests do not exercise tmux, model-facing MCP registration, or task-message delivery.

## Docs References

No external domain source governs this repository-local test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is focused structural assignment coverage. | `TerminalTaskAssignmentTests` | mcp/tests/test_terminal_leaf_assignment.py:131-280 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Assignment moves between valid seats and preserves same-pair no-mutation. | `test_assignment_moves_one_session_between_valid_leaf_role_seats`; `test_same_document_and_role_is_seat_taken_without_mutation` | mcp/tests/test_terminal_leaf_assignment.py:140-159; mcp/tests/test_terminal_leaf_assignment.py:187-207 |
| Role altitude is validated against real task topology. | `test_role_altitude_mismatch_fails_closed` | mcp/tests/test_terminal_leaf_assignment.py:230-259 |
| The trusted payload carries canonical document identity and compatible role provenance. | `test_payload_uses_canonical_task_reference_and_spawn_role` | mcp/tests/test_terminal_leaf_assignment.py:261-279 |
| The shared implementation performs topology validation and pair arbitration. | `assign_terminal_session_to_task` | mcp/src/agents_remember/serving/terminal_task_assignment.py:96-170 |

## L23 Assignment No-Mutation Regression

Task topology now includes current contracts, and a dedicated stale-super case
advances the exact task-derived `super` ref before returning the ambient checkout to `main`.
It proves the blocked projection is returned while the terminal retains its previous unbound
task state.

## Update History

- 2026-08-16T04:06+02:00 — Dagger fixture repair: terminal-assignment stale-lineage forcing advances the task-derived super ref and leaves the ambient checkout on main.
- 2026-08-12T20:10+02:00 — L23 curator: documented fail-closed assignment without seat mutation; verification remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 added direct boundary coverage for `role_suffixed_leaf_base`, clearing the master CRAP finding without changing production behavior.
- 2026-08-11T12:15+02:00 — Reconciled the historical sidecar with its current task-document/role
  assignment coverage. Verification remains pinned pending governed closeout.
- 2026-07-02T17:04+02:00 — Through 2026-08-08, earlier coverage established reassignment, pair conflicts,
  role resolution, and no-mutation behavior under the predecessor leaf-addressing design.
