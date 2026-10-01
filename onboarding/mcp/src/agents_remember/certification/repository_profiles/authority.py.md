# mcp/src/agents_remember/certification/repository_profiles/authority.py

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Confined resolution and admission of one explicit repository profile authority. This module
resolves the single repository-relative `certificationProfile` reference configured per
repository, reads exactly that one real regular file inside the selected repository, and admits
it through schema parsing, digest canonicalization, repository-identity binding, and full graph
validation before any Gate 1-4 command can start. It is the fail-closed front gate of the
CCR-R22 repository-owned profile model: missing, ambiguous, invalid, or incomplete authority is a
typed `certification-profile-invalid` admission failure, never a silent skip, never a discovery
fallback.

The module is the direct replacement for the old fixed-wrapper authority model. Before this
commit a single hardcoded `mcp/test_support/agents_remember_test_support/code_quality/check.py`
wrapper path and repository-name policy decided gate applicability; `authority.py` moves that
decision into one explicit per-repository settings reference plus the admitted profile bytes.

## Code Commentary

`AdmittedRepositoryProfile` is the frozen result record: repository id, resolved repository
root, the exact resolved source path, its SHA-256, and the canonical profile identity.

`load_repository_profile(repository_id, repository_root, configured_reference)` is the single
admission entry point. It (1) resolves one real file below the repository,
(2) reads and JSON-parses exactly those bytes with an 8 MiB budget,
(3) parses the schema via `RepositoryCertificationProfile.model_validate_json`,
(4) canonicalizes and requires the declared digest,
(5) requires `repositoryId` to equal the selected repository, and
(6) runs `validate_repository_profile` over the canonical graph. Every refusal raises
`CertificationProfileError` with typed findings; no finding stops the report early.

`resolve_repository_profile_path(repository_root, configured_reference)` owns the confinement
rules. It refuses `None` (missing authority), a non-string reference (ambiguous), absolute
paths, Windows-drive paths, backslashes, empty/`.`/`..` parts, and any reference that is not
its own canonical POSIX form. It resolves strictly inside the repository root, refuses symlink
components during traversal, and requires a real regular file. `_reject_symlink_components`
walks each reference part and refuses a symbolic link before it can escape the root.

`_read_profile_bytes` enforces the 8 MiB admission budget, parses JSON eagerly, and converts
OS/Unicode/JSON failures into a typed `profile-json-invalid` finding. `_validation_finding` /
`_finding` shape pydantic and semantic findings into `RegistryValidationFinding` records so
the typed error carries every independent finding.

## Invariants And Boundaries

- Exactly one authority: zero references (`profile-authority-missing`) or multiple
  (`profile-authority-ambiguous`) both refuse; there is no multi-profile or default profile.
- The reference must be canonical, relative, traversal-free, and resolve to one real regular
  file inside the repository; symlink traversal and path escape refuse.
- Admission is complete before execution: parse, digest, repository identity, and graph
  validation all pass before any rail can start. No Gate-1 command begins on an invalid profile.
- This module reads only the profile file; it never scans, discovers by convention, searches
  newest files, or imports repository commands.
- `CertificationProfileError` (status `certification-profile-invalid`) is the single typed
  failure surface, carrying the complete findings list.

## Evidence

### Docs References

CCR-R22@v1 requires exactly one authoritative profile resolved through the repository
context/settings contract; zero or multiple authorities refuse; invalid profile resolution
produces the typed admission failure `certification-profile-invalid` with every independent
schema/graph/config finding before any Gate-1 command starts. The master task.md boundary section
assigns the trusted host runtime-launch boundary to the framework exactly as this module's
confinement rules implement it.

CCR-R22@v1 (requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md) requires
resolving one authoritative profile through the repository context/settings contract
("## Resolution And Freeze") with zero or multiple authorities refusing; invalid resolution
produces the typed admission failure certification-profile-invalid carrying every independent
schema/graph/config finding before any Gate 1 command starts ("## Failure And Recovery").
No auto-discovery by newest file, filename convention, executable presence, or historical
success exists, and no built-in default certifies an unconfigured code repository
("## Exclusions And Forbidden Overreach"). The master task boundary (task.md,
"## Framework and repository boundary") assigns the trusted host runtime-launch boundary to
the framework; a repository profile never owns or overrides Dagger runner/engine/session/
layer-store authority.


### Repo-Internal References

The configured reference arrives through `RepositoryScope.certification_profile` parsed by
`runtime_config._optional_repository_profile_reference` (same commit); the lifecycle worker and
worktree tools pass it into `WorktreeArgs.certification_profile`. Consumers such as
`worktrees/modules/quality/gate.py` and `clean_executor.py` call `load_repository_profile`
against the exact candidate checkout so the profile bytes admitted are the candidate's own.

- Resolution/read/canonicalize/validate before any rail: the complete admission sequence. [1]
- Confined one-file resolution with symlink and escape refusal. [2]
- 8 MiB budget and eager JSON parse for the admitted bytes. [3]
- Settings parsing binds one canonical relative path per repository. [4]
- The gate admits the repository profile selection from its declared authority. [5]
- The sandbox admits the profile execution against its prepared candidate tree. [6]
