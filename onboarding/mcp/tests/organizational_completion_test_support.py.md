# mcp/tests/organizational_completion_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/organizational_completion_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Provide current door/journal fixtures for organizational-completion tests.


CCR-R22@v1 (L22, commit `685f83c44055`): the full-gate fixture memory policy literal changed to
`processPolicy: "profile-adapter-owned"` and fixture `WorktreeArgs` now carry
`certification_profile=Path("mcp/certification-profile-v1.json")`.

## Code Commentary

### Logic

The fixture builds a real queue/task/worktree setup, starts a closeout operation, publishes finalization evidence, and exposes helpers used by completion, integration, and repair tests.

Its `_full_gate` helper now returns a callback with the production quality-gate call shape. The
callback uses `publish_passing_quality_gate` to publish exact candidate-bound passing evidence and
returns that published payload; it does not hand completion tests an invented static success map.


### Invariants And Boundaries

- Tests share current door/journal authority rather than obsolete queue lifecycle fixtures.
- The fixture uses real task and operation stores for recovery-sensitive assertions.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The support module imports current lifecycle, task, and queue fixtures. | "from agents_remember.application.lifecycle import lifecycle_operation_worker"; "from agents_remember.tasks import read_task_doc, write_task_doc"; "from test_closeout_queue import MASTER_A, QueueFixture" | mcp/tests/organizational_completion_test_support.py:11-11; mcp/tests/organizational_completion_test_support.py:13-13; mcp/tests/organizational_completion_test_support.py:29-29 |
| The fixture class assembles organizational-completion test state. | `OrganizationalCompletionFixture` | mcp/tests/organizational_completion_test_support.py:76-149 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the processPolicy literal and certification_profile args in organizational completion fixtures.


- 2026-08-26T10:44:52+02:00 — Reconciled organizational-completion fixtures with candidate-aware quality callbacks that publish exact passing evidence through the canonical test helper.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.