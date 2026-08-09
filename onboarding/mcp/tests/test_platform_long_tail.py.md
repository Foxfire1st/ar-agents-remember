# mcp/tests/test_platform_long_tail.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_platform_long_tail.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-09T06:48+02:00                     |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Refusals, defaults and degraded paths across the platform's **small helpers**. None is big
enough to earn a module of its own, and every one is a guard: the argument shape a tool
refuses, the settings key it rejects by name, the already-aborted operation it reports
instead of raising, the inbox row it renews without losing fields the caller did not
restate.

They are collected here rather than scattered because they share a shape — a specific bad or
unusual input, and the exact verdict it produces — and because **a guard nobody exercises is
a guard nobody can show is right**.

## Classes

| Class | Guard |
| --- | --- |
| `DecisionRoleTests` | Decision role handling. |
| `ReadFilesRangeTests` | `read_ar_files` line ranges are caller-supplied JSON, so each field is checked. |
| `CarryoverRequestTests` | Carryover request validation. |
| `NudgeTargetTests` | Nudge target resolution. |
| `ReducerPausedTests` | The paused-reducer arm. |
| `ProviderStateCacheTests` | The projection's pre-read provider refresh is **best-effort by design** — a failed refresh must not fail the projection. |
| `EntityFingerprintValidationTests` | Entity fingerprint validation. |
| `MemoryBaselineParserTests` | Memory baseline parsing. |
| `EscalationSettingsTests` | `orchestration.escalation` timings, read from developer-owned settings text. |
| `InboxRenewalTests` | Renewing a pending row bumps its date **without dropping what it already carried**. |
| `RequestedHarnessTests` | A caller-named harness must be both a known id **and** actually installed. |
| `OpenTerminalRefusalTests` | Terminal-open outcomes translated into the spawn tool's public statuses. |
| `SkillsInstallRequestTests` | The skills install validates its own request before touching the harness root. |
| `CopySkillTreeCollisionTests` | What happens to a skill directory that is already installed. |
| `ProviderDependencyInstallTests` | Settings that enable no provider mean there is no dependency install to run. |
| `DashboardReloadServerTests` | `--reload` hands its knobs to the re-imported app **through the environment**. |
| `BenchmarkBatchExecutionTests` | Parallel benchmark task execution collects failures instead of aborting the run. |
| `BenchmarkMcpRegistrationTests` | The benchmark MCP registration insists on the layout its settings hard-code. |

## Invariants And Boundaries

- Each test names one specific bad or unusual input and the exact verdict it produces —
  the message or status a caller acts on, not merely "an error".
- Best-effort paths (provider state refresh, parallel benchmark execution) must degrade,
  never propagate.
- Renewal and update paths must preserve fields the caller did not restate.

**260713-TES-L4:** `InboxRenewalTests.test_a_row_that_is_no_longer_pending_is_returned_untouched`
now seeds the terminal state via `mark_landed` (the `consumed` fixture is gone with the N16
consume demotion) and asserts the landed row is returned untouched — a re-firing condition
appends nothing and the caller sees the terminal row back.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sibling refusal collection for provider/seed/dispatch paths. | `CgcBackendPortsTests` | mcp/tests/test_platform_edge_refusals.py:76-123 |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the renewal fixture swap to the
  formal `landed` terminal (mark_landed; the consumed fixture is gone with the N16 consume
  demotion). Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` row with an exact
  anchor (deleting the unresolvable directory row); exact non-fixing check returns zero findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  long-tail guard suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
