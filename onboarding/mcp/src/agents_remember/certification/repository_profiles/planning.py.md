# mcp/src/agents_remember/certification/repository_profiles/planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:39:50+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
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
identity covers every input the rails consume. `_compile_adapter_inputs` supplies the selected executor, consumed result decoders, and this gate's publication policies; `_compile_semantic_inputs` retains the duplicate-identity check and canonical sorting after combining those nodes with rail and selector inputs.

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

CCR-R22@v1 (requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md,
"## Required Profile Contract") requires explicit applicability for each of Gates 1-4, an
empty gate being legal only as a typed not-applicable result with a repository-owned reason;
framework-owned classification rules fix gate meanings and order while repositories choose
tools and populations ("## Framework-Owned Classification Rules"); each gate certificate
names the exact admitted profile and its gate-specific plan digest ("## Resolution And
Freeze").


## Repo-Internal References

`gate.py` and `clean_executor.py` consume planning through the execution admission
(`admit_repository_profile_execution`). Recovery renders the exact journal-selected certification through `render_selected_code_certification`, which reopens the frozen run and checks current candidate identity before validating original terminal evidence. The generic
registry/rail/wave primitives come from `certification/models.py` and `certification/__init__.py`
(the earlier R11 foundation), and graph validation from `repository_profiles/validation.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact one-selection resolution with typed missing/ambiguous findings. | `resolve_repository_profile_selection` | mcp/src/agents_remember/certification/repository_profiles/planning.py:55-83 |
| Compile exact Gates 1-4 without claiming the framework-owned Gate 5. | "def compile_repository_profile_plan" | mcp/src/agents_remember/certification/repository_profiles/planning.py:86-167 |
| Gate compilation binds applicable rails, artifacts and semantic inputs. | "def _compile_gate_plan" | mcp/src/agents_remember/certification/repository_profiles/planning.py:199-269 |
| Plan admission refuses bytes that differ from the sole canonical compilation. | `admit_repository_profile_plan` | mcp/src/agents_remember/certification/repository_profiles/planning.py:170-196 |
| Render an exact journal selection after full original-object and artifact readback. | "def render_selected_code_certification" | mcp/src/agents_remember/worktrees/modules/quality/gate.py:364-395 |

## Update History

- 2026-09-06T21:39:50+00:00 — Reconciled the landed validation/helper extraction against IAS d3610903; retained ownership and refusal semantics and refreshed same-file evidence ranges. Verification stamps and final acceptance were not advanced.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References rows as prose.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Gate 1-4 plan compilation/admission module of the repository-owned certification profile package.
