# mcp/certification-profile-v1.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/certification-profile-v1.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `eb05a872780112640359232063168639d20fa87b`|
| lastVerifiedCommitDate | 2026-09-03T06:19:25+02:00|
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

At the root-owned bootstrap repair (commit eb05a8727801) the profile was regenerated after the
Dagger source change split the installer from the runtime-directory/symlink exec node and the
selector-ownership change added the gate-certificate authority test consumer. Three digest
authorities moved and are now self-consistent with the regenerated sources
(`certification-profile-v1.json:6`, line 2583, line 2643): `profileDigest`
`87142fc2...`, selector `configurationDigest` `8ceb5c1d...`, adapter `runtimeDigest`
`32b57c79...`. Per the bootstrap handover, canonicalization, selector authority, and the
candidate module digest agreed before the accepted run (candidate tree 3e984eb0...).

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
| The root-owned repair "Regenerates the canonical authority after the Dagger-source and selector-ownership changes," binding profileDigest 87142fc2..., selector configurationDigest 8ceb5c1d..., and adapter runtimeDigest 32b57c79.... | "Changed surfaces and behavior"; "The regenerated profile binds" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/notes/reports/l09-gate-evidence/runtime-bootstrap-unblocker-handover/260903-runtime-bootstrap-unblocker-worker-handover.md |
| The 2026-09-03T06:20:00+02:00 master decision landed the bootstrap repair; it advances no requirement leaf and does not satisfy L12. | Decision record | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/task.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The regenerated profile digest after the bootstrap repair. | `profileDigest` | mcp/certification-profile-v1.json:6 |
| The regenerated selector configuration digest. | `configurationDigest` | mcp/certification-profile-v1.json:2583 |
| The regenerated adapter runtime digest. | `runtimeDigest` | mcp/certification-profile-v1.json:2643 |
| The profile's literal consumer ownership names the gate-certificate authority test. | `REPOSITORY_TEST_INPUT_CONSUMERS` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:50-104 |
| Repository-profile admission/canonicalization consume this authority at plan compile time. | `compile_repository_profile_plan`; `canonicalize_repository_profile` | mcp/src/agents_remember/certification/repository_profiles/planning.py; mcp/src/agents_remember/certification/repository_profiles/canonical.py |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The framework is repository-neutral; this file is the Agents Remember profile data, not framework code. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): created the card for the checked-in canonical certification profile and recorded the three regenerated digest authorities (`profileDigest`, selector `configurationDigest`, adapter `runtimeDigest`); no prior sidecar existed.
