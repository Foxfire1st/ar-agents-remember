# mcp/tests/structural_seat_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/structural_seat_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T22:27+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Provides the shared real-store topology, settings, runtime configuration, harness detector, and
thread-safe fake host used by the focused canonical-seat forcing suites.

## Code Commentary

### Logic

`write_structural_topology` materializes one sprint, organizational master, and leaf with canonical
`TaskDocumentRef` values. `write_structural_settings` supplies settings-owned role launch choices.
`FakeHost` records live bindings and terminations under a lock so concurrency tests can exercise the
production spawn path without tmux.

### Conventions

Every fixture is rooted under the test-provided temporary directory. The fake substitutes only the
external terminal host; task, catalog, inbox, settings, and dispatch owners remain production code.

### Invariants And Boundaries

- The helper never touches the deployed coordination root or a real terminal session.
- Shared fixtures preserve the same task topology and host semantics across all L2 forcing modules.
- `FakeHost` protects its mutable evidence because same-seat and distinct-seat tests run concurrently.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is repository-local test support.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper writes one canonical sprint/master/leaf topology and returns its three document refs. | `write_structural_topology` | mcp/tests/structural_seat_test_support.py:30-81 |
| Settings and runtime configuration remain isolated under the supplied root. | `structural_config`; `write_structural_settings` | mcp/tests/structural_seat_test_support.py:84-101 |
| The fake host records concurrent lifecycle effects without starting tmux. | `FakeHost` | mcp/tests/structural_seat_test_support.py:108-140 |

## Cross-Repo References

No cross-repository dependency governs this test support.

## Update History

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for the shared canonical-seat forcing
  fixtures. Verification remains closeout-owned.
