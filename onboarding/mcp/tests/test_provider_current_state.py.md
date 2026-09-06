# mcp/tests/test_provider_current_state.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_current_state.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks that provider status describes current runtime truth rather than setup history. Fixtures distinguish per-repository CGC degradation, GrepAI restart recovery without a workspace, disabled providers excluded from aggregate readiness, and a restarting watcher that is not ready.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Current state is current truth not setup history | `test_current_state_is_current_truth_not_setup_history` | mcp/tests/test_provider_current_state.py:24-67 |
| Current state reports per repo cgc degradation | `test_current_state_reports_per_repo_cgc_degradation` | mcp/tests/test_provider_current_state.py:69-98 |
| Provider status reports restart recovery for grepai no workspace | `test_provider_status_reports_restart_recovery_for_grepai_no_workspace` | mcp/tests/test_provider_current_state.py:100-126 |
| Current state ignores disabled providers for aggregate readiness | `test_current_state_ignores_disabled_providers_for_aggregate_readiness` | mcp/tests/test_provider_current_state.py:128-147 |
| Restarting watcher is not ready | `test_restarting_watcher_is_not_ready` | mcp/tests/test_provider_current_state.py:149-171 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints the tool response registry to its moved `models.tools` package. Verified at code commit `1d446724`.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 9 table citations and 2 Update History citations; no unresolved Tier-3 claims.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `providers/current_state.py`. The module is 348 lines and the old `L16-L325` stopped short of the
  helpers the claim covers, cutting off `cgc_indexing_state` cit:([`cgc_indexing_state`], mcp/src/agents_remember/providers/current_state.py:336-342) and `_result_list` cit:([`_result_list`], mcp/src/agents_remember/providers/current_state.py:345-348).
  Widened to L16-L348 — `build_current_provider_state` through the last helper — and read both ends
  to confirm the range spans the whole projection-and-persistence body (`write_current_provider_state`
  L39, `current_state_path` L52, `grepai_current_state` L136, `cgc_current_state` L179,
  `aggregate_state` L285, `grepai_indexing_state` L317).
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): documented `test_provider_status_summarizes_structured_cgc_last_refresh` (MCP 2.9.x), which pins flattening a structured CGC `lastRefresh` object to the human-readable summary string. Grafted onto the series' task-12 `targetRepos` content.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: the current-truth regression now asserts GrepAI
  `targetRepos` are persisted from configured repository memory roots, protecting the observer's
  repo-scoped memory-provider projection. Verification metadata will be stamped at closeout.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-10T06:20+02:00 — Body-quality pass: merged the 2.5.0/2.5.1 readiness coverage (content-gated ok, indexing busy list, restarting watcher, scan markers) into Logic (documentation only).
- 2026-06-10T05:30+02:00 — Added tests: restarting (crash-looping) watcher is not ready and degrades the provider/global ok; GrepAI `initialScan` markers map to indexing/indexed/unknown without degrading readiness; GrepAI indexing feeds the summary busy list.
- 2026-06-09T22:10+02:00 — Added tests for empty-graph degradation (repo target, provider, aggregate, and global packet `ok`/`partial`), the `indexing` transient staying ready at every level, the CGC per-repo restart recovery action, and the summary `indexing` busy-target list.
- 2026-06-04T22:15+02:00: Documented the provider-status regression that returns restart/rebind recovery guidance for GrepAI `noWorkspace` from both compact status and diagnostics.
- 2026-06-02T16:24+02:00: Added the `test_current_state_reports_grepai_no_workspace_as_degraded` regression (GrepAI reports `degraded` / `indexingState: noWorkspace` when the watcher has no searchable workspace) and noted that the ready fixture now includes a healthy `workspaceStatus`; reflected both in the Logic narrative and repo-internal references.
- 2026-05-28T19:52+02:00: Updated after provider current-state integration tests moved full current-state payload assertions to provider diagnostics.
- 2026-05-28T12:32+02:00: Created for provider current-state unit coverage.
