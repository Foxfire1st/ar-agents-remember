# mcp/tests/test_mcp_registration_wiring_tests_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_mcp_registration_wiring_tests_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`                                        |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_mcp_registration_wiring_tests_2.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `RegistrationWiringTests2`

### 260713-TES-L4 Poll And Supersede Wiring

`test_operator_inbox_poll_*` now asserts the `include_terminal: False` default is forwarded to
the application poll (N11), and `test_operator_inbox_supersede_forwards_entry_reason_and_
attribution` pins the new declaration: `operator_inbox_supersede` forwards
`entry_id`/`reason`/`superseded_by` to the payload builder (R11).

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_mcp_registration_wiring_tests_2.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `include_terminal` poll kwarg
  pin (N11) and the `operator_inbox_supersede` wiring test (R11). Verification metadata pinned
  until closeout stamps the 260713-TES-L4 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
