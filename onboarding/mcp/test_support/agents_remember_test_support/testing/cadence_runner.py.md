# mcp/test_support/agents_remember_test_support/testing/cadence_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/cadence_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Runs scheduled stress, provider-bump, and migration-window evidence in the pinned Dagger
environment without creating a second acceptance route.

## Code Commentary

### Logic

`run_cadence_evidence` requires Dagger admission, validates the lifecycle catalog, selects one
closed trigger expression, forces serial pytest, and writes a structured non-accepting result plus
phase/event artifacts. The result binds exact candidate/machine provenance, selected population,
topology, command, phase definitions, repetitions, limitations, and content-addressed artifacts.
An empty migration population produces a loud not-applicable result with provenance but does not
claim execution.
If pytest omits the phase report or writes an unusable one, the runner emits a content-addressed
failure artifact and returns a failing route result. Missing evidence can never be serialized as a
successful cadence execution.

### Conventions

The Dagger module owns container construction; this module owns only the in-container cadence
command and result schema.

### Invariants And Boundaries

- Host execution refuses before inventory or pytest.
- Release and diagnostic triggers are rejected so this cannot shadow full quality or the direct
  exact-node route.
- Every result says `acceptanceEligible=false` and `certifying=false`.

### Todos

None.

## Docs References

No external domain documentation governs the local cadence command.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Only scheduled, provider-bump, and migration triggers can execute. | `run_cadence_evidence` | mcp/test_support/agents_remember_test_support/testing/cadence_runner.py:23-113 |
| The Dagger public route remains explicitly non-accepting. | `cadence_evidence` | .dagger/src/agents_remember_quality/main.py:448-517 |
| Focused tests force host refusal, serial stress, provider selection, and not-applicable migration. | `test_host_process_is_refused_before_inventory_or_execution` | mcp/tests/test_cadence_runner.py:36-119 |

## Cross-Repo References

No cross-repository cadence authority is owned here.

## Update History

- 2026-08-28T11:32+02:00 — Made missing or unusable phase evidence an explicit artifact-backed
  route failure instead of allowing a successful result with absent proof.

- 2026-08-28T04:37+02:00 — Bound cadence evidence to exact candidate, machine, population,
  topology, command, raw artifact hashes, and explicit limitations.
- 2026-08-25T01:56+02:00 — Created for separated stress/provider/migration evidence cadence.
