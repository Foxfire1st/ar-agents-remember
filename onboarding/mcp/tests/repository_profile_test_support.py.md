# mcp/tests/repository_profile_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/repository_profile_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
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
rail specs now carry gate/wave placement and runtime image identity, `dagger_runtime_digest` recomputes the pinned Dagger module source digest, `fixture_execution_manifest` compiles the exact `repository-certification-admission/v1` execution manifest with a
fixture `dagger-runtime-authority/v1` snapshot, and `FakeContainer`/`FakeFile`/`FakeDag` double the Dagger graph so the portable profile execution functions run without a daemon.
`install_fixture_profile`/`install_agents_remember_profile` copy the fixture source or the
real profile into a temporary repository root, and `agents_remember_profile_execution` derives
the admitted execution for the real profile.

The fixture profile now declares a finite per-rail `rail-evidence/<identity>.log` publication with `application/octet-stream` media type; capture bytes need not form UTF-8 text. `FakeContainer` supplies known producer fixture files for graph interpretation, copies `FakeFile` contents into output paths and exposes actual empty stdout/stderr values. Hash reads use a detached fake container so inspecting a file does not append a hash command to the subsequent rail history. These marker files are explicitly fixture output, not live acceptance artifacts.

### Conventions

Keep repository-source literal readers visible to dependency ownership. The ambient runner path used by the producer fixture causes its importers to join the exact test-consumer closure.

### Invariants And Boundaries

- Fixture profiles are complete enough to pass validation without borrowing product behavior.
- Selector commands bind every identity placeholder the v2 contract requires (L19).
- The support module does not execute real rails; it builds profiles and records interpreter operations through explicit doubles.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tests copy the real profile into an isolated fixture repository. | `install_agents_remember_profile` | mcp/tests/repository_profile_test_support.py:67-73 |
| Portable fixture installation retains a canonical profile digest. | `install_fixture_profile` | mcp/tests/repository_profile_test_support.py:76-97 |
| Each language fixture declares source inventory, runtime and artifact identities. | `FixtureRepository` | mcp/tests/repository_profile_test_support.py:138-155 |
| The profile builder includes complete selectors, adapters, decoder and finite binary capture publications. | `fixture_profile` | mcp/tests/repository_profile_test_support.py:273-429 |
| Runtime source identity is recomputed from the actual Dagger module files. | `dagger_runtime_digest` | mcp/tests/repository_profile_test_support.py:126-134 |
| Portable execution receives an explicit test runtime-authority manifest. | `fixture_execution_manifest` | mcp/tests/repository_profile_test_support.py:447-479 |
| The SDK graph double records operations and separates detached hash output from rail execution. | `FakeContainer` | mcp/tests/repository_profile_test_support.py:579-729 |
| Known producer marker bytes are populated for interpreter tests only. | `_producer_fixture_files` | mcp/tests/repository_profile_test_support.py:652-684 |
| File operations expose the retained fixture value. | `FakeFile` | mcp/tests/repository_profile_test_support.py:732-740 |
| The fake client supplies the graph container without a daemon. | `FakeDag` | mcp/tests/repository_profile_test_support.py:806-814 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Documented binary rail captures, explicit producer marker bytes, file copying and detached hash reads; removed stale helper line locations while retaining fixture authority limits.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the gate-execution builder extensions - runtime digest helper, fixture execution manifest with runtime authority, rail gate/wave specs, and fake Dagger containers used by the portable profile execution tests.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 selector upgrade — v2 schema, version 2.0.0, empty external inputs, and the full identity
  placeholder command matching the fixture select-tests scripts. Verification is pinned to the
  owning commit.
