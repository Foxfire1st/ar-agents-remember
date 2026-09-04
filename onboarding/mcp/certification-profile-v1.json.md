# mcp/certification-profile-v1.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/certification-profile-v1.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b`|
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](overview.md)

## Purpose

The checked-in canonical repository certification profile for Agents Remember
(schema `repository-certification-profile/v1`, semantic revision `1.0.0`, profile id
`agents-remember-certification`): three selections (`closeout-full`, `closeout-targeted`,
`local-targeted`), the complete repository rail catalog with runtime identities and content
digests, and the certified digest authorities that admission, selector, and runtime validation
recompute before a gate may start.

## Code Commentary

### Logic

The profile binds every rail to its gate, class, prerequisites, required artifacts, runtime inputs
(cpython-3.13.15 / node-playwright image identities and their toolchain, lock, environment, and
secret-policy digests), evidence contracts, output artifacts, and execution adapter contract
(container command, environment whitelist, timeout, resource policy, success/skip exit codes,
clean-room and teardown policy). Each of the two closeout selections and the local pre-commit
selection restates the applicable gate populations.

At the root-owned bootstrap repair (commit eb05a8727801) the profile was regenerated after a
Dagger source change split the installer from the runtime-directory/symlink exec node; that
history is preserved below the current state. CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`)
regenerated the profile after the Dagger module
cutover to cost-ordered five-gate execution with the shared runtime authority: `profileDigest`
`34858daa...` (line 6) and adapter `runtimeDigest` `4cf0e133...` (line 2793) moved with the changed
module bytes, while the selector `configurationDigest` `8ceb5c1d...` (line 2733) is unchanged. Every
rail now declares explicit `successExitCodes` / `skippedExitCodes` arrays (the ambient-role-chat
E2E rail keeps 0 and 78; every other rail declares [0] and []), and `consumingGates` arrays are
declared for the gate scheduler instead of relying on defaults.

### Conventions

Digests are authoritative and regenerated, never hand-edited: a profile whose digests fail
recomputation is refused at admission, and the file is produced by the repository's canonical
profile tooling against the exact source state.

### Invariants And Boundaries

- The profile is repository-owned data consumed by universal certification contracts (CCR-R22);
  the framework never teaches itself about Agents Remember rails.
- Every rail's runtime identity and digest must match the pinned toolchain; a drift refuses the
  plan.
- The profile advances no requirement leaf; the bootstrap repair only restored the authoritative
  verifier so frozen leaves could rebind.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts
below document the regenerated digests and the repair scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| The regenerated canonical authority after CCR-R12@v4 binds profileDigest 34858daa..., selector configurationDigest 8ceb5c1d..., and adapter runtimeDigest 4cf0e133.... | `profileDigest`; `configurationDigest`; `runtimeDigest` | mcp/certification-profile-v1.json:6-6; mcp/certification-profile-v1.json:2733-2733; mcp/certification-profile-v1.json:2793-2793 |
| The 2026-09-03T06:20:00+02:00 master decision landed the bootstrap repair; it advances no requirement leaf and does not satisfy L12. | `## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the profile regeneration for the five-gate/authority cutover - `profileDigest` `34858daa...` and adapter `runtimeDigest` `4cf0e133...` moved with the changed Dagger module bytes, every rail now declares explicit `successExitCodes`/`skippedExitCodes` arrays, and digest anchor lines were re-pointed (2733/2793).
` | onboarding/mcp/certification-profile-v1.json.md:93-95 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The regenerated profile digest after the CCR-R12@v4 five-gate/authority profile cutover. | `profileDigest` | mcp/certification-profile-v1.json:6 |
| The unchanged selector configuration digest. | `configurationDigest` | mcp/certification-profile-v1.json:2733 |
| The regenerated adapter runtime digest after the Dagger module byte change. | `runtimeDigest` | mcp/certification-profile-v1.json:2793 |
| The profile's literal consumer ownership names the gate-certificate authority test. | `REPOSITORY_TEST_INPUT_CONSUMERS` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:50-104 |
| Repository-profile admission/canonicalization consume this authority at plan compile time. | `compile_repository_profile_plan`; `canonicalize_repository_profile` | mcp/src/agents_remember/certification/repository_profiles/planning.py:71-119; mcp/src/agents_remember/certification/repository_profiles/canonical.py:13-27 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The framework is repository-neutral; this file is the Agents Remember profile data, not framework code. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): created the card for the checked-in canonical certification profile and recorded the three regenerated digest authorities (`profileDigest`, selector `configurationDigest`, adapter `runtimeDigest`); no prior sidecar existed.
