# mcp/tests/test_closeout_queue_actions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_actions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns the closeout queue's public action, ambient-seat authority, barrier transition, and
caller-specific legal-operation matrices.

## Code Commentary

### Logic

The suite drives exact request fields and revisions through the queue owner, then exercises
declaration identity, immutable contract binding, atomic barrier acquire/release/abort, lifecycle
operation recovery, and legal projections for manager and orchestrator callers.

### Invariants And Boundaries

- Managers declare/admit and integrate; orchestrators grade/select and own barriers.
- A normal atomic barrier release proves the finalized master landing; abort requires canonical
  judgment evidence.
- Legal operations are state- and caller-specific rather than an overbroad union.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public request and mutation authority is exact. | `test_status_scope_and_candidate_mutation_authority_is_exact` | mcp/tests/test_closeout_queue_actions.py:86-128 |
| Barrier release and abort call their exact evidence seams. | `test_release_and_abort_barrier_require_exact_owner_and_empty_block` | mcp/tests/test_closeout_queue_actions.py:424-500 |
| Lifecycle legal operations require the exact durable owner. | `test_owned_lifecycle_operation_requires_exact_kind_contract_and_fingerprint` | mcp/tests/test_closeout_queue_actions.py:592-626 |

## Update History

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: added the successful nondefault
  admission transition and missing terminal-leaf refusal, completing the real action/declaration
  owner map without mocking production dispatch.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  action, authority, barrier, and legal-operation assertions are identical.
- 2026-08-15T13:08+02:00 — No content impact: accepted Ruff's case-sensitive private-name import
  order; the imported action owners and assertions are unchanged.
- 2026-08-15T12:53+02:00 — Created for the focused L3 action/authority suite extracted after the
  first full targeted Dagger artifact exposed insufficient branch forcing.
