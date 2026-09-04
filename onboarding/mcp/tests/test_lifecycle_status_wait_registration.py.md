# {S}mcp/tests/test_lifecycle_status_wait_registration.py{S}

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | {S}mcp/tests/test_lifecycle_status_wait_registration.py{S} |
| doc_type | {S}file-level-onboarding{S} |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | {S}e375f2ebdc87f6843bc76168b646d606fa79caec{S} |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | {S}overview.md{S} |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Self-contained CCR-R15 wait-tool registration test: the `worktree_status_wait` `server.tool` closure in `mcp/registration/worktrees.py` must hand its flat public arguments to the application payload builder as one typed `LifecycleStatusWaitRequest` and return the builder's result untouched, mirroring the family-wide registration wiring pattern.

## Code Commentary

### Logic

The module creates the MCP server through `create_server`, stands in for the payload builder with a recorder that remembers the one call it received, and asserts the closure converts `contract_path` / `operation_kind` / `expected_generation` / `after_revision` / `timeout_seconds` into the typed request before dispatch.

### Invariants And Boundaries

- Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support
  module.
- Asserts public behavior through the typed outcome vocabulary and the store's dual-revision
  contract, never through private operation identity.

## Docs References

No configured external Domain Documentation source governs this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs these tests. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closure delegates flat args as one typed request. | registration recorder assertions | mcp/tests/test_lifecycle_status_wait_registration.py:1-118 |
| The registration closure under test. | `worktree_status_wait` | mcp/src/agents_remember/mcp/registration/worktrees.py:202-233 |

## 260831-CCR-L15 Status-Wait Test Module

Created with the lifecycle status-change waiting tool (CCR-R15).

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new status-wait test module.
