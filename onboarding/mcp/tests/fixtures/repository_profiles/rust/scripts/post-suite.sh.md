# mcp/tests/fixtures/repository_profiles/rust/scripts/post-suite.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/scripts/post-suite.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-3 post-suite quality rail of the Rust repository-profile fixture: it consumes the Gate-2
proof artifact and requires the declared suite-result and verification claims to be present. It
exists so the Rust fixture profile has a real suite-dependent quality consumer (Gate 3 must
consume a green Gate-2 certificate or its declared artifacts).

## Code Commentary

`set -eu`; takes `proof_path` and greps the proof artifact for
`"suiteResult":"rust-suite.json"` and `"verified":true`; exits non-zero (via `set -e`) when
either is absent.

## Invariants And Boundaries

- Gate-3 input discipline: consumes only the Gate-2 declared proof artifact.
- Deterministic fixture check: passes exactly when the proof is present and verified.

## Docs References

CCR-R22@v1: Gate 3 contains only checks that consume a green Gate-2 certificate or its declared
artifacts.

Gate 3 contains only checks that consume a green Gate-2 certificate or its declared artifacts.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture post-suite proof consumer over the suite artifact. | `suiteResult` | mcp/tests/fixtures/repository_profiles/rust/scripts/post-suite.sh:1-5; mcp/tests/fixtures/repository_profiles/rust/scripts/run-suite.sh:1-9 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Rust fixture post-suite rail.
