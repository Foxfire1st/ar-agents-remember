# mcp/tests/test_repository_profile_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_profile_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

Focused path-authority tests for `certification/repository_profiles/authority.py`: proving that
certification profile resolution refuses absence, ambiguity, path escape, symlink traversal,
malformed bytes, digest mismatch, and repository-identity mismatch, and that one exact
repository-relative authority loads exactly one file. This is the cutover fingerprint test for
the R22 replacement of the fixed-wrapper authority model: the pytest scope matches the new typed
admission findings rather than wrapper discovery.

## Code Commentary

`_codes` extracts the typed finding codes from a `CertificationProfileError`; `_write_profile`
writes a valid fixture profile from `repository_profile_test_support.fixture_profile` under
`certification/profile.json`.

- `test_exact_repository_relative_authority_loads_one_file` asserts the happy path: the admitted
  source path resolves exactly and the canonical digest matches the fixture profile.
- `test_invalid_authority_refuses_before_read` parameterizes the refusal codes:
  `profile-authority-missing` (None), `profile-authority-ambiguous` (list), and
  `profile-path-invalid` for traversal/`.`/doubled-slash/trailing-slash/absolute/drive
  references, and `profile-file-unavailable` for a missing file. Every case must keep status
  `certification-profile-invalid`.
- `test_symlink_escape_is_refused` proves a symlink pointing outside the repository is refused
  as `profile-path-symlink`.
- `test_malformed_and_digest_mismatch_are_typed` proves `profile-json-invalid` for a broken
  JSON payload and `profile-digest-mismatch` for a tampered `profileDigest`.
- `test_repository_identity_mismatch_is_refused` proves a profile whose `repositoryId` does
  not match the selected repository is refused as `profile-repository-mismatch`.

## Invariants And Boundaries

- Every refused case is a typed `CertificationProfileError` with status
  `certification-profile-invalid`; no case may silently skip or fall back to a wrapper.
- The tests exercise the authority module directly with a real file on disk, not a mock of
  resolution, so the confinement rules are behaviorally proven.
- The fixture profile's repository identity (`fixture-node`) is deliberately different from the
  `agents-remember` reference profile, so repository mismatch is independently exercised.

## Docs References

CCR-R22@v1 requires missing/ambiguous/invalid/incomplete profile authority to fail during
admission with typed refusal findings (status `certification-profile-invalid`) and never
silently disable code certification or enter a compatibility/fallback route; invalid profile
resolution produces every independent schema/graph/config finding before any Gate-1 command
starts.

## Repo-Internal References

Depends on `repository_profile_test_support.fixture_profile` (same wave's test-support module)
and exercises `load_repository_profile` from the new `certification/repository_profiles`
package.

| Finding | Anchor | Source |
| --- | --- | --- |
| One-exact-file happy path and typed refusal matrix for authority resolution. | `test_exact_repository_relative_authority_loads_one_file`; `test_invalid_authority_refuses_before_read`; `test_symlink_escape_is_refused`; `test_malformed_and_digest_mismatch_are_typed`; `test_repository_identity_mismatch_is_refused` | mcp/tests/test_repository_profile_authority.py:25-107 |
| Fixture profile generator shared by authority and quality tests. | `fixture_profile` | mcp/tests/repository_profile_test_support.py:268-414 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new profile path-authority admission tests.
