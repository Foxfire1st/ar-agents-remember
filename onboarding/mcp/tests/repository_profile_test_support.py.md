# mcp/tests/repository_profile_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/repository_profile_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | cfd0938103b1392e471144b6997c51a41591ad2b |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

One typed builder for repository-profile contract tests and their fixture repositories: it
materializes Node and Rust fixture roots, installs the Agents Remember certification profile and
fixture profiles, and composes complete `RepositoryCertificationProfile` instances with the
exact selector, executor, decoder, rail, and artifact declarations the profile validator requires.

## Code Commentary

### Logic

`FixtureRepository` declares the language root, locked image reference, and rail specs;
`NODE_FIXTURE`/`RUST_FIXTURE` carry the two non-Python fixtures. `fixture_profile`
builds a complete profile with four gate selections and the repository-test selector. L19 upgraded
that selector to `schemaVersion="repository-selector-result/v2"`, version `2.0.0`, an empty
declared `externalInputs` tuple, and a command that consumes
`{selector-output}`, `{selection-mode}`, `{diff-base}`, `{candidate-kind}`,
`{candidate-value}`, `{selector-id}`, `{selector-version}`, and
`{selector-configuration-digest}` — matching the v2 fixture scripts.


CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`) extends the builders for five-gate execution tests:
rail specs now carry gate/wave placement and runtime image identity, `dagger_runtime_digest` (lines
126-134) recomputes the pinned Dagger module source digest, `fixture_execution_manifest` (lines
434-466) compiles the exact `repository-certification-admission/v1` execution manifest with a
fixture `dagger-runtime-authority/v1` snapshot, and `FakeContainer`/`FakeFile`/`FakeDag` (lines
566-755) double the Dagger graph so the portable profile execution functions run without a daemon.
`install_fixture_profile`/`install_agents_remember_profile` copy the fixture source or the
real profile into a temporary repository root, and `agents_remember_profile_execution` derives
the admitted execution for the real profile.

### Invariants And Boundaries

- Fixture profiles are complete enough to pass validation without borrowing product behavior.
- Selector commands bind every identity placeholder the v2 contract requires (L19).
- The support module never executes rails; it only builds and installs profiles.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is test-only support.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture roots and installation helpers. | `FixtureRepository`; `install_fixture_profile`; `install_agents_remember_profile` | mcp/tests/repository_profile_test_support.py:133-153; mcp/tests/repository_profile_test_support.py:71-94; mcp/tests/repository_profile_test_support.py:62-69 |
| The complete profile builder now declares the v2 selector authority with identity binding. | `fixture_profile`; `RepositorySelectorAuthority` | mcp/tests/repository_profile_test_support.py:268-410; mcp/tests/repository_profile_test_support.py:331-358 |

## Cross-Repo References

None; the fixture data is repository-local.

## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the gate-execution builder extensions - runtime digest helper, fixture execution manifest with runtime authority, rail gate/wave specs, and fake Dagger containers used by the portable profile execution tests.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 selector upgrade — v2 schema, version 2.0.0, empty external inputs, and the full identity
  placeholder command matching the fixture select-tests scripts. Verification is pinned to the
  owning commit.
