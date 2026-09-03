# mcp/src/agents_remember/certification/repository_profiles/execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Admission of one exact repository profile selection for executor use. This module stitches the
admitted canonical profile, its resolved purpose/mode selection, and the exact candidate identity
into one frozen `AdmittedRepositoryProfileExecution`: the profile bytes, the selection, the
compiled plan, the declared executor adapter, the declared result decoder, and the
published-artifact definitions relevant to the applicable gates. It is the boundary that turns
"this profile is admitted" into "this selection of that profile runs for this exact candidate",
still without naming any repository command.

## Code Commentary

`AdmittedRepositoryProfileExecution` is the frozen bundle consumed by the clean executor.
`admit_repository_profile_execution(admitted, *, purpose, mode, candidate_identity)` performs
the whole selection in one call: `resolve_repository_profile_selection` picks the sole
purpose/mode selection, `compile_repository_profile_plan` (re)validates the canonical graph and
compiles the digest-bound plan for the candidate, executor decoders and adapters are indexed by
their declared ids, and `published_artifacts` is filtered to artifacts published by at least
one gate that is applicable in this selection. A missing executor adapter or decoder id inside
the resolved selection surfaces as a `KeyError`-style admission failure during dictionary
lookup, i.e. a mis-declared selection cannot silently run a different adapter.

## Invariants And Boundaries

- One exact candidate/profile execution: the execution bundle carries profile digest, plan
  digest, selection id, adapter, and decoder together so downstream publication can bind all of
  them (see `published_manifest.py` v3 fields).
- Purpose and mode must resolve to exactly one declared selection; ambiguous or missing
  selection authority refuses at planning time.
- Execution never constructs commands itself: the adapter contract in `adapters.py` owns
  command rendering, and this module only selects which declared adapter/decoder run.
- A selection whose declared executor or decoder id is not present in the profile cannot be
  admitted; there is no default adapter substitution.

## Docs References

CCR-R22@v1 requires one admitted profile to declare explicit selections, including the canonical
local/pre-commit and closeout profiles as selections over the same rail definitions, never copied
commands; each gate certificate names the exact admitted profile and its gate-specific plan
digest. The framework owns result schema and certificate rules while the repository owns the
concrete selections.

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical local/pre-commit and closeout profiles are selections over the same rail definitions, never copied commands. | `## Required Profile Contract` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| Each gate certificate names the exact admitted profile and its gate-specific plan digest. | `## Resolution And Freeze` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| Framework owns result schema; the repository owns selections and applicability. | `## Framework and repository boundary` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/task.md |

## Repo-Internal References

`clean_executor._admit_prepared_profile` is the production consumer: it admits the execution
against the exact sandboxed candidate and writes it into the sandbox admission manifest; the
manifest then fixes the profile identity fields the published quality manifest schema v3 binds.
`_quality_evidence_fixture.py` and `test_worktree_support.publish_passing_closeout_quality`
reuse the same admission to fabricate passing evidence for tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| One-call selection/plan/executor/decoder/artifact admission for an exact candidate. | `admit_repository_profile_execution` | mcp/src/agents_remember/certification/repository_profiles/execution.py:38-81 |
| The clean executor admits against the sandboxed candidate and serializes the execution into the admission manifest. | `_admit_prepared_profile`; `_write_sandbox_manifest` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:164-176; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:220-251 |
| Fixtures admit a profile execution to publish passing gate evidence. | `publish_passing_quality_gate` | mcp/tests/_quality_evidence_fixture.py:49-80 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new exact-candidate profile-execution admission module of the repository-owned certification profile package.
