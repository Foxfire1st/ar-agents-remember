# mcp/src/agents_remember/certification/repository_profiles/execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T22:25+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
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

### Logic

`AdmittedRepositoryProfileExecution` is the frozen bundle consumed by the clean executor.
`admit_repository_profile_execution(admitted, *, purpose, mode, candidate_identity, source_selection=None)` performs
the whole selection in one call: `resolve_repository_profile_selection` picks the sole
purpose/mode selection, `compile_repository_profile_plan` (re)validates the canonical graph and
compiles the digest-bound plan for the candidate, executor decoders and adapters are indexed by
their declared ids, and `published_artifacts` is filtered to artifacts published by at least
one gate that is applicable in this selection. A missing executor adapter or decoder id inside
the resolved selection surfaces as a `KeyError`-style admission failure during dictionary
lookup, i.e. a mis-declared selection cannot silently run a different adapter.

### Conventions

Selection and declared-id lookup use the admitted canonical profile; this module does not select
ambient executors or render commands.

### Invariants And Boundaries

- One exact candidate/profile execution: the execution bundle carries profile digest, plan
  digest, selection id, adapter, and decoder together so downstream publication can bind all of
  them (see `published_manifest.py` v3 fields).
- Purpose and mode must resolve to exactly one declared selection; ambiguous or missing
  selection authority refuses at planning time.
- Execution never constructs commands itself: the adapter contract in `adapters.py` owns
  command rendering, and this module only selects which declared adapter/decoder run.
- A selection whose declared executor or decoder id is not present in the profile cannot be
  admitted; there is no default adapter substitution.

### Todos

No task-independent follow-up was identified in this profile-selection adapter.

### Current source-selection contract

Execution admission accepts optional CandidateSourceSelection and passes it unchanged into compile_repository_profile_plan, binding the selected source applicability into the resulting exact candidate plan. Executor and decoder lookup remain profile-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| `admit_repository_profile_execution` carries the current contract described above. | "def admit_repository_profile_execution" | mcp/src/agents_remember/certification/repository_profiles/execution.py:41-81 |

## Docs References

CCR-R22@v1 requires one admitted profile to declare explicit selections, including the canonical
local/pre-commit and closeout profiles as selections over the same rail definitions, never copied
commands; each gate certificate names the exact admitted profile and its gate-specific plan
digest. The framework owns result schema and certificate rules while the repository owns the
concrete selections.

CCR-R22@v1 (requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md,
"## Required Profile Contract") requires the canonical local/pre-commit and closeout
profiles to be selections over the same rail definitions, never copied commands; each gate
certificate names the exact admitted profile and its gate-specific plan digest
("## Resolution And Freeze"). The master task boundary (task.md,
"## Framework and repository boundary") assigns result schema to the framework while the
repository owns the concrete selections and applicability.


| Finding | Anchor | Source |
| --- | --- | --- |
| No Domain Documentation source is configured; the requirement context above is background, while executable behavior is cited below. | — | — |

## Repo-Internal References

`clean_executor._admit_prepared_profile` is the production consumer: it admits the execution
against the exact sandboxed candidate. `_write_sandbox_manifest` serializes the admitted profile
source digest, full plan, executor/decoder definitions, runtime-authority snapshot, and published
artifact definitions; the profile and plan identity therefore remain tied to that sandbox.


| Finding | Anchor | Source |
| --- | --- | --- |
| One-call selection/plan/executor/decoder/artifact admission for an exact candidate. | `admit_repository_profile_execution` | mcp/src/agents_remember/certification/repository_profiles/execution.py:38-76 |
| The sandbox admits the profile execution against its prepared candidate tree. | "def _admit_prepared_profile" | mcp/src/agents_remember/worktrees/modules/quality/execution/sandbox.py:42-66 |
| The sandbox manifest records profile execution and frozen runtime authority. | "def _write_sandbox_manifest" | mcp/src/agents_remember/worktrees/modules/quality/execution/sandbox.py:121-169 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this profile-selection adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |


## Update History

- 2026-09-07T01:15:32+02:00 — Timestamp-format repair of the earlier 2026-09-07 event (original exact time unrecorded): Reconciled current source-selection and ownership semantics against the retained verification baseline; prior pins and history remain unchanged.


- 2026-09-05T22:25+00:00 — L30 incoming-reference review: projected the retained source-backed claim to its current owner extent; preserved this unchanged source file's genuine verification hash/date.


- 2026-09-05T08:27+02:00 — L31 native curator: Retained exact-candidate profile admission after reading the clean-executor consumer; documented the serialized runtime-authority snapshot and regenerated exact admission/manifest evidence. Reviewed against frozen code `ea35964985f30080488270e71ac81657ac40682b`; this records source verification, not gate acceptance.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References rows as prose.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new exact-candidate profile-execution admission module of the repository-owned certification profile package.
