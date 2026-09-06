# mcp/src/agents_remember/certification/lifecycle_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/lifecycle_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3`|
| lastVerifiedCommitDate | 2026-09-03T00:47:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the CCR-R05 exact-candidate admission boundary: admit one supplied owner-produced authority
set — never discovered, scanned, or inferred — freeze it into a self-verifying lifecycle admission
manifest, and revalidate that exact manifest before any gate or write. It also carries the
prior-red corrective authority: any successor after a red gate must carry one exact corrective
disposition per failed/blocked catalog root and at least one relevant changed input.

## Code Commentary

### Logic

`compile_lifecycle_admission` (`lifecycle_admission.py:84-121`) first requires the candidate's
mutation, source, and branch authority to be `valid` and its worktree observation to be
`admissible` with an exact conflict-path shape (`_require_candidate_authority`,
`lifecycle_admission.py:150-181`), then delegates certification admission to
`compile_certification_admission` and proves the lifecycle candidate and the compiled plan name
the same repository and code tree (`_require_candidate_alignment`,
`lifecycle_admission.py:184-208`). An optional prior-red context compiles a content-addressed
disposition manifest (`_compile_prior_red_disposition`, `lifecycle_admission.py:211-272`): the
prior catalog must be the exact certifying red catalog of the prior admission
(`_require_prior_catalog_authority`, `lifecycle_admission.py:275-308`), every failed/blocked
catalog member needs exactly one disposition binding its exact rail/status/digest/owner
(`_require_result_disposition`, `lifecycle_admission.py:311-366`), a blocked dependant may cite
only a directly failed, directly repaired root, and every declared changed input must be an exact
changed semantic input of the prior and successor gate (`_require_relevant_change`,
`lifecycle_admission.py:369-405`). `validate_lifecycle_admission_currentness`
(`lifecycle_admission.py:124-147`) recompiles the exact current inputs and refuses any movement
with a typed `CertificationContractError` carrying `gateStarts: 0` (`_refuse`,
`lifecycle_admission.py:414-432`).

### Conventions

Admission is pure composition of supplied authorities; the module never executes a rail, mutates a
repository, or invents a fallback candidate.

### Invariants And Boundaries

- The candidate, profile, plan, registry, and prior-red corrective inputs are one indivisible
  ownership set; a missing member refuses.
- Zero gate starts on refusal: admission refusals emit `gateStarts: 0` and cannot elevate a
  diagnostic.
- An unchanged red candidate refuses; correctness of the successor depends on exact changed
  inputs, not on intent prose.

### Todos

Execution and repository-profile wiring are owned by later consumers, not this module.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
below close the informational gap for the exact-candidate admission CAS semantics.

CCR-R05@v3 (requirements/CCR-R05-v3-exact-candidate-admission-and-recovery.md, "Admission
Required Behavior") requires admitting one supplied owner-produced authority set without
scanning or inference: validate mutation/source/branch authority, abort only when there is no
valid candidate to examine, and require a corrective disposition for every failed/blocked
catalog root plus at least one relevant changed input after a red gate. Leaf L05
(05_exact-candidate-admission-and-recovery.md, "S2 — Implement only CCR-R05") landed the
exact-candidate admission, prior-red recovery, certificate currentness, and finalization
boundary contracts without fallback behavior.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission composes the exact supplied authorities and freezes one lifecycle manifest. | `compile_lifecycle_admission` | mcp/src/agents_remember/certification/lifecycle_admission.py:84-121 |
| Currentness re-compiles current inputs and refuses any movement before a gate or write. | `validate_lifecycle_admission_currentness` | mcp/src/agents_remember/certification/lifecycle_admission.py:124-147 |
| Candidate authority and worktree shape are mandatory, with typed refusals. | `_require_candidate_authority` | mcp/src/agents_remember/certification/lifecycle_admission.py:150-181 |
| The lifecycle candidate and the R11/R22 plan must name identical repository and code-tree authority. | `_require_candidate_alignment` | mcp/src/agents_remember/certification/lifecycle_admission.py:184-208 |
| Prior-red disposition binds the exact failed/blocked catalog and exact changed inputs. | `_compile_prior_red_disposition`; `_require_prior_catalog_authority`; `_require_relevant_change` | mcp/src/agents_remember/certification/lifecycle_admission.py:211-272; mcp/src/agents_remember/certification/lifecycle_admission.py:275-308; mcp/src/agents_remember/certification/lifecycle_admission.py:369-405 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-specific rail declarations enter through repository profiles outside this contract. | — | — |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References rows as prose (absolute ar-coordination task-artifact paths are not repo-relative citations). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 4e0ea4b3c493a2c89ca18367e89e4cb42ee8c5f3 (CCR-R05@v3/L05): created the card for the new exact-candidate admission and prior-red corrective authority module; no prior sidecar existed.
