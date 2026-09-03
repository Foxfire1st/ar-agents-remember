# mcp/src/agents_remember/certification/repository_profiles/planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Compile immutable Gate 1-4 plan contributions from one admitted repository profile. This module
owns the concrete translation from repository-owned profile declarations into the digest-bound
per-gate plans the execution layer runs: selection resolution, plan compilation, plan admission,
and the semantic-input inventory used for dependency/invalidation bookkeeping. It never claims
the framework-owned Gate 5 (the Agents Remember memory/coherence gate).

## Code Commentary

`resolve_repository_profile_selection(canonical, *, purpose, mode)` requires exactly one
declared selection for the requested purpose/mode; zero or multiple choices are typed
`CertificationProfileError` findings (`required-profile-selection-missing` /
`ambiguous-profile-selection`).

`compile_repository_profile_plan(canonical, *, selection_id, candidate_identity)` revalidates
the canonical graph, finds the selected declaration, maps every gate's rail ids through the
profile rail catalog, and builds one `RepositoryProfilePlan` whose `planDigest` binds
schema version, profile digest, candidate identity, selection, and all gate plans. Per gate,
`_compile_gate_plan` compiles rails (ordered by order key then identity/digest), computes
execution waves via `canonical_execution_waves`, and — only for applicable gates — compiles the
semantic-input nodes (rail execution/runtime, referenced selectors, executor adapter when the
gate consumes it, referenced result decoders when the gate consumes them, publication-policy
artifacts for the gate). `admit_repository_profile_plan` requires caller-held plan bytes to
equal the sole canonical compilation for the same selection/candidate, i.e. a plan cannot be
invented or modified.

`_compile_semantic_inputs` / `_semantic_node` / `_selector_consuming_gates` build and digest
the deterministic semantic input catalog, keyed by (kind, id) with a duplicate check, so plan
identity covers every input the rails consume.

## Invariants And Boundaries

- Plans are immutable and candidate-bound: profile digest plus candidate identity plus selection
  fully determine the plan digest; admission refuses altered plan bytes.
- Gate 5 is explicitly absent: `compile_repository_profile_plan` compiles Gates 1-4 only and
  does not claim memory/coherence authority.
- A selection's gate that is typed not-applicable compiles with its reason and no semantic
  inputs; it never becomes hidden work.
- Graph validation runs at plan time against the canonical profile: an invalid profile cannot
  produce a plan, so no Gate-1 command starts from an invalid plan.

## Docs References

CCR-R22@v1 requires the profile to declare explicit applicable/not-applicable status for each of
Gates 1-4 (an empty gate is legal only as a typed not-applicable result with a repository-owned
reason and no hidden work), and framework-owned classification rules fix gate semantics and
order while repositories choose tools and populations. Each gate certificate names the exact
admitted profile and its gate-specific plan digest.

| Finding | Anchor | Source |
| --- | --- | --- |
| Explicit applicability for each of Gates 1-4; an empty gate is legal only as a typed not-applicable result with a repository-owned reason. | `## Required Profile Contract` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| Framework-owned classification rules: gate meanings and order are fixed; repositories choose tools and populations. | `## Framework-Owned Classification Rules` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| Each gate certificate names the exact admitted profile and its gate-specific plan digest. | `## Resolution And Freeze` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

`gate.py` and `clean_executor.py` consume planning through the execution admission
(`admit_repository_profile_execution`) and recovery (`recover_strict_code_quality_gate`
recompiles the expected plan digest before reusing a published generation). The generic
registry/rail/wave primitives come from `certification/models.py` and `certification/__init__.py`
(the earlier R11 foundation), and graph validation from `repository_profiles/validation.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact one-selection resolution with typed missing/ambiguous findings. | `resolve_repository_profile_selection` | mcp/src/agents_remember/certification/repository_profiles/planning.py:40-69 |
| Full profile validation + per-gate plan + wave + semantic-input compilation into one digest-bound plan. | `compile_repository_profile_plan`; `_compile_gate_plan` | mcp/src/agents_remember/certification/repository_profiles/planning.py:71-118; mcp/src/agents_remember/certification/repository_profiles/planning.py:148-197 |
| Plan admission refuses bytes that differ from the sole canonical compilation. | `admit_repository_profile_plan` | mcp/src/agents_remember/certification/repository_profiles/planning.py:120-146 |
| Recovery recompiles the expected plan digest for a candidate before reuse. | `recover_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:279-343 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Gate 1-4 plan compilation/admission module of the repository-owned certification profile package.
