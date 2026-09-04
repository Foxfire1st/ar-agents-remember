# mcp/tests/test_dagger_runtime_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dagger_runtime_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the host-level shared Dagger runner/layer-store authority contract
(CCR-R12@v4, delivered by 260831-CCR-L12, commit `cfd09381`) without contacting a real engine:
every production refusal and admission decision of dagger_authority.py is forced with unit fakes,
monkeypatched docker inspection, and temporary registry roots. It is the focused proof envelope
for host-authority parsing/admission, ownership and transition, and the docker inspector, so a
change to the authority boundary is pinned here before any live Dagger evidence is produced.

## Code Commentary

### Logic

`FakeInspector` (lines 34-73) and `declaration_env` (lines 74-84) provide a deterministic engine
probe and a host declaration environment; `owner_for` (lines 85-108) builds one registered owner;
`refusal_code` (lines 109-113) extracts the typed defect code from a
`DaggerRuntimeAuthorityError`. Module-level tests cover: missing/malformed declarations and
unsupported/provisioning-capable endpoints (`test_refuses_a_missing_host_declaration_before_any_engine_contact` ...
`test_refuses_unsupported_and_provisioning_capable_endpoints`, lines 114-156), a worktree-local
declaration source (lines 147-156), a non-running engine or missing store mount (lines 157-174),
one admitted shared authority with a deterministic snapshot (lines 175-198), ambient
`DAGGER_HOST` conflict refusal (lines 199-207), two worktrees and two operation kinds reusing one
authority identity (lines 208-237), exact-owner release with stale/foreign owner refusal (lines
238-298), the typed transition barrier and zero-census activation (lines 299-350), continuation
reusing the frozen snapshot without ambient re-resolution (lines 351-403), crash reconciliation
dropping only stale owners (lines 404-442), and registry corruption refusing with a typed defect
(lines 443-453). The docker-inspector group (lines 454-652) proves the running-engine and
layer-store mount checks with `monkeypatch`, including typed defects when inspection cannot start,
mount inspection fails, mount output is unparsable or non-list, foreign or malformed mount entries
are skipped, and an endpoint that is not one engine container is refused. Parse-admission tests
(lines 653-698) pin the missing/non-object/unsupported payload refusals and the invalid
endpoint/layer-store/engine-version refusals; `_FalsyRootPath` (lines 699-705) plus the
resolve-failure tolerance case (lines 706-737) prove host-root checks survive path resolution
errors around unrelated roots. Registry tests (lines 738-927) force corrupt state/owner payloads,
owner defaults, duplicate-owner refusal, custom-liveness census, malformed-owner-cell handling,
and PID-reuse-safe liveness fingerprints; admission/continuation registry tests (lines 956-1102)
pin barrier re-admission refusal, ownerless admission/release leaving the registry untouched,
pending-barrier activation when the census reaches zero, replacement activation once the old
census reaches zero, and activation on an empty registry.

### Conventions

The suite never starts or provisions an engine; the inspector boundary is doubled with
`monkeypatch` against `docker inspect` output shapes, and every registry mutation runs on a
temporary root so no host state is touched.

### Invariants And Boundaries

- Every refusal is asserted through the typed defect code (never a bare exception message), and
  each refusal happens before any command would start.
- Owner release requires the exact owner record and matching process liveness; stale rows are
  removed only by reconciliation and never rewrite an operation result.
- A changed declaration with live owners always produces the typed transition barrier; the
  replacement activates only after the locked zero-owner census.
- Continuation always reuses the frozen snapshot digest and never re-resolves ambient state.

### Todos

None.

## Docs References

CCR-R12@v4 requires pre-admission engine/container and store verification, an immutable frozen
authority snapshot bound into operations, and a locked host-level registry with process-start
liveness, typed transition barriers, and crash reconciliation; this suite is the focused proof
envelope for those clauses (see 260903-CCR-L12-implementation-readiness, proof envelope items 1-2).

| Finding | Anchor | Source |
| --- | --- | --- |
| Host authority parsing/admission refusals and successful admission are unit-forced before any live Dagger use. | `test_refuses_a_missing_host_declaration_before_any_engine_contact`; `test_admits_one_shared_authority_and_binds_a_deterministic_snapshot` | mcp/tests/test_dagger_runtime_authority.py:114-122; mcp/tests/test_dagger_runtime_authority.py:175-198 |
| Ownership/transition, exact release, stale-owner handling, crash reconciliation, and continuation are pinned. | `test_release_only_the_exact_owner_and_reject_stale_or_foreign_owners`; `test_changed_host_declaration_enters_a_typed_barrier_and_activates_after_zero_census`; `test_continuation_reuses_the_frozen_snapshot_and_never_resolves_ambient_state` | mcp/tests/test_dagger_runtime_authority.py:238-298; mcp/tests/test_dagger_runtime_authority.py:299-350; mcp/tests/test_dagger_runtime_authority.py:351-403 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite exercises the host declaration parser, snapshot, environment, and registry directly. | `test_parse_host_declaration_refuses_missing_non_object_and_unsupported_payloads`; `test_registry_owners_default_when_absent_then_refuse_corrupt_payloads` | mcp/tests/test_dagger_runtime_authority.py:653-669; mcp/tests/test_dagger_runtime_authority.py:798-823 |
| The clean-executor authority test doubles this boundary with a probe inspector and owner registry root. | `_AuthorityProbe`; `_test_authority` | mcp/tests/test_clean_quality_executor.py:55-67; mcp/tests/test_clean_quality_executor.py:68-80 |

## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass: created this file-level
  onboarding card for the new host-authority proof suite (CCR-R12@v4) delivered in code commit
  cfd09381; anchors and ranges derived from the current worktree source and pinned to that commit.
