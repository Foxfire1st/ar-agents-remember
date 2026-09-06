# mcp/tests/test_worktree_quality_gate_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_quality_gate_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks that direct host execution cannot run a certification profile and that an interrupted gate preserves the previous completed test report. This refusal concerns the certification wrapper, not ordinary supported host pytest development feedback.

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
| Host quality execution refuses before running a profile | `test_host_quality_execution_refuses_before_running_a_profile` | mcp/tests/test_worktree_quality_gate_runner.py:17-21 |
| Interrupted gate keeps the previous completed test report | `test_interrupted_gate_keeps_the_previous_completed_test_report` | mcp/tests/test_worktree_quality_gate_runner.py:24-44 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-06T15:11:59+00:00 — L33 pending candidate curation: Re-read the prepared source, reconciled profile-required planning and shared fixture ownership, preserved report/cap/host-refusal contracts, and replaced obsolete wrapper/local-builder claims with their current tests. Verification names the real prepared source commit c69d5171187fa1957025e393270db9f5a864ab14; this entry does not claim CCR acceptance.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-target cutover of the quality gate runner tests.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the quality gate and clean executor package relocations; runner outcome and evidence assertions are unchanged.
- 2026-08-24T21:23+02:00 — Replaced zero-exit-only fakes with candidate-bound certifying outcomes.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded builder-level non-Dagger refusal and aligned
  missing-wrapper wording. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: reconciled the test card with self-policy, immediate host
  refusal, and the simplified Dagger-only adapter. Verification remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: quality-runner tests require Dagger-only
  execution, explicit mode/diff base, exact candidate materialization, fail-closed status, and no
  host or direct-Docker compatibility path.
- 2026-08-12T20:10+02:00 — L23 curator: documented short native temp-root propagation through the quality runner; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 replaced a platform branch in the test expectation with an equivalent lookup; host-managed and explicit-cap runtime behavior is unchanged.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  host-managed full command/report proofs and resource-policy payload coverage;
  retained explicit-cap failure proofs. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from `CodeQualityGateTests` in the
  closeout quality-gate suite; retained shared helpers and separated runner policy from closeout
  mutation while bringing both files below the hard size gate.
