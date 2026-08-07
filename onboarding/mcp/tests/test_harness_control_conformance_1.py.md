# mcp/tests/test_harness_control_conformance_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_conformance_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

First half of the post-restructure harness-control conformance family (260731-EFA-L7; the 2,131-line `test_harness_control.py` was split into this 612-line module and `test_harness_control_conformance_2.py`). Carries the fake-adapter conformance cases — handshake/ordered terminal acceptance, setter truth-table, FIFO queue ordering, cancellation safety, retained/idempotent duplicates, known-receipt reconciliation, exact-session IPC, durable-inbox convergence, and the multiplexed sub-agent approval cases (R6). L8's deterministic receipt-before-release rewrite of `test_cancelled_setter_late_completion_does_not_kill_command_queue` is applied verbatim here.

## Code Commentary

- `HarnessControlConformanceTests1` — the family's first `unittest.IsolatedAsyncioTestCase` class; the module-level helpers (`_FakeAdapter`, `_BlockingSubmitAdapter`, `_BlockingSetAdapter`, `_catalog_entry`, `_launch`, `_identity`, `_settle_events`) are imported from `test_harness_control` to keep one shared fake.

## Invariants And Boundaries

- Behavior is shared with `test_harness_control.py` and the sibling `test_harness_control_conformance_2.py`; the split preserves every assertion (name sets reconciled item for item).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared fake adapter this family imports. | `_FakeAdapter` | mcp/tests/test_harness_control.py:113-287 |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the conformance-family split module. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
