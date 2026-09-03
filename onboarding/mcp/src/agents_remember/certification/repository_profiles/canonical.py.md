# mcp/src/agents_remember/certification/repository_profiles/canonical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/canonical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification overview](../overview.md)

## Purpose

Canonical bytes and digest authority for repository certification profiles. This module is the
narrow entry point that turns one user-authored `RepositoryCertificationProfile` into a normalized
`CanonicalRepositoryCertificationProfile` whose declared `profileDigest` provably authorizes the
canonical content. It exists so that every later consumer (admission, planning, execution,
publication) can rely on one digest-stamped semantic identity instead of trusting raw profile
bytes.

It is one of the new `certification/repository_profiles/` modules introduced by CCR-R22@v1
(L22, commit `685f83c44055`): `models.py`/`validation.py` carry the data contract and graph
validation, `authority.py` resolves exactly one real profile file, `canonical.py` normalizes and
digest-stamps it, `planning.py` compiles immutable Gate 1-4 plans, `adapters.py` declares the
repository-neutral executor/decoder interfaces, and `execution.py` admits one exact
candidate/profile execution. This module deliberately contains no repository commands, no
discovery, and no fallback path: it is pure canonicalization.

## Code Commentary

`canonicalize_repository_profile(profile)` first calls `_normalize_repository_profile(profile)`
(from `models.py`) to produce normalized semantic bytes, then computes
`repository_profile_digest(normalized)` over exactly those bytes. If the profile's declared
`profileDigest` does not equal that computed digest, it raises `ValueError` -- the caller
(`authority.load_repository_profile`) converts that into a typed `profile-digest-mismatch`
admission finding. On success it returns an immutable `CanonicalRepositoryProfile` carrying both
the normalized profile and its digest, so no later stage can see a digest that does not match the
profile it describes.

The module re-exports `repository_profile_digest` in `__all__` so programming against a profile's
canonical identity does not require importing the private models helpers directly.

The digest is computed in `models.py` (over the normalized canonical payload, sorted JSON with
compact separators); this module only enforces that the declared digest authorizes the bytes.

## Invariants And Boundaries

- One profile has exactly one canonical identity: digest mismatch always refuses before any
  repository rail can start; there is no digest repair, override, or compatibility path.
- This module never reads files, settings, or the repository; it operates only on the parsed
  `RepositoryCertificationProfile` value handed to it.
- Normalization lives in `models.py`; this module is the enforcement boundary that binds the
  declared digest to normalized content. Do not add discovery or a second digest rule here.
- A `ValueError` here is the deliberate contract with `authority.py`, which owns converting it
  into a typed `CertificationProfileError` finding.

## Docs References

The governing requirement is CCR-R22@v1 (Repository-Owned Certification Gate Profiles). The
normative profile-digest/freeze contract is stated there: the framework freezes one profile
digest and every directly consumed configuration/runtime identity into the admission manifest. The
leaf `22_repository-owned-certification-gate-profiles.md` and master `task.md`
"Framework and repository boundary" section confirm the framework/repository split this module
implements (framework owns schema/digest rules; repository owns profile bytes).

CCR-R22@v1 (requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md,
"## Normative Requirement") has one explicit versioned repository-owned profile compile
Gates 1-4 while the framework owns gate meanings, order, dependency legality, result schema,
and certificate rules; the framework freezes the profile digest and every directly consumed
configuration/runtime identity into the admission manifest, and profile bytes changes
invalidate the certificate dependency closure ("## Resolution And Freeze" /
"## Invalidation Boundaries"). The master task boundary (task.md,
"## Framework and repository boundary") assigns fixed gate meanings, order, and typed
schemas to the MCP while each repository owns one explicit versioned Gate 1-4 profile.


## Repo-Internal References

`canonicalize_repository_profile` (this file) is invoked by `authority.load_repository_profile`
after schema validation and before graph validation, so the digest check runs exactly once per
admission. The normalized-profile model and digest helper it depends on live in
`certification/repository_profiles/models.py` (owned by the L19 test-ownership wave). Validation
of the canonical graph (`validate_repository_profile`) lives in
`certification/repository_profiles/validation.py`; planning consumes the canonical profile for
plan digest compilation.

| Finding | Anchor | Source |
| --- | --- | --- |
| `canonicalize_repository_profile` normalizes one profile and refuses a declared digest that does not match canonical content. | `canonicalize_repository_profile` | mcp/src/agents_remember/certification/repository_profiles/canonical.py:13-24 |
| The digest is computed by `repository_profile_digest` over normalized content in models. | `repository_profile_digest` | mcp/src/agents_remember/certification/repository_profiles/models.py:308-312 |
| `load_repository_profile` calls canonicalization and converts digest refusal into a typed `profile-digest-mismatch` finding. | `load_repository_profile` | mcp/src/agents_remember/certification/repository_profiles/authority.py:42-92 |
| The canonical profile is what planning digests into immutable per-gate plans. | `compile_repository_profile_plan` | mcp/src/agents_remember/certification/repository_profiles/planning.py:71-118 |

## Update History

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References rows as prose.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new canonicalization/digest-entry module of the repository-owned certification profile package.
