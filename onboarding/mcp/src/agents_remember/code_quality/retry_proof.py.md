# mcp/src/agents_remember/code_quality/retry_proof.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/retry_proof.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`retry_proof.py` owns fail-closed reuse of a passed pytest/branch-coverage proof inside a
nonce-attested Dagger retry after a later coverage-derived rail refuses. It stores no proof in the
worktree and admits only an exact repository retry or a selected-test-only delta after the shared
Dagger environment guard has authorized the wrapper process.

## Code Commentary

### Logic

`prepare` builds a fresh run plan from a complete tracked-file snapshot and a compatibility key.
The key binds the resolved diff base, measurement scope and thresholds, Python/platform and
coverage, pytest, pytest-cov, and pytest-xdist tool versions, plus a digest of the invocation
environment. The manifest and both
coverage artifacts carry SHA-256 integrity checks. An exact match restores coverage JSON and skips
pytest. Otherwise the canonical `DependencyOwnershipGraph` resolves every changed product, test,
support, plugin, and governed fixture path to affected consumers. Only a complete, non-global
impact wholly inside the prior selected population may run as a delta.

Tracked symlinks are fingerprinted as Git stores them: the link-target text, tagged as a symlink,
not bytes reached by following the link. This matters for the repository's tracked
`dashboard/node_modules` directory link; following it made the first production retry fail with
`IsADirectoryError` and silently fall back to another full suite.

`_filtered_coverage_data` removes every affected test's runtime contexts and the empty
collection/import context from the old branch data before those consumers append fresh data. The
retained aggregate is therefore a conservative subset: it may be insufficient and trigger a
conclusive full rerun, but it cannot pass from stale evidence attributable to a changed dependency.
Global input, incomplete ownership, affected consumers outside the prior population, missing
contexts, changed environment, corrupt artifacts, and CI all select a fresh run.

Only a fresh full pytest pass followed by a later rail failure publishes a new manifest. A passing
wrapper removes the proof; a delta failure retains the original full proof rather than chaining an
already-filtered aggregate.

### Invariants And Boundaries

- Cache location is the worktree-specific directory below Git's common directory, so it neither
  dirties nor enters the commit.
- The manifest stores only the environment digest, never environment values or secrets.
- The repository snapshot hashes tracked symlink identity without reading an external target tree.
- Context filtering requires branch arcs and at least one pytest runtime context.
- Delta eligibility is dependency-owned: all affected consumers must be known, non-global, and
  inside the prior selected population. Support and governed fixture changes may qualify only when
  their complete consumer set is proven; ambiguous/unowned input runs fresh.
- `AR_QUALITY_NO_RETRY` disables reuse. `prepare` requires a typed capability minted only by
  `testing.dagger_admission`; this module cannot turn host or diagnostic execution into an accepted
  retry.

### Todos

None.

## Docs References

No Domain Documentation entries are configured for this repository; this is a repository-local
quality-proof policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain contract governs this local retry cache. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper prepares, consumes, and finalizes retry plans around its fixed and coverage-derived rails. | `execute_quality_rails`; `prepare_retry_plan` | mcp/src/agents_remember/code_quality/check.py:535-584; mcp/src/agents_remember/code_quality/check.py:879-912 |
| Retry pytest commands record per-test contexts and append only in delta mode. | `_pytest_step`; `quality_steps` | mcp/src/agents_remember/code_quality/check.py:301-340; mcp/src/agents_remember/code_quality/check.py:378-428 |
| Focused tests prove dependency-owned filtering, global/incomplete invalidation, exact reuse, conclusive full fallback, and tracked directory-symlink snapshotting. | `test_changed_test_contexts_and_collection_context_are_removed`; `test_repository_snapshot_hashes_symlink_identity_without_following_it` | mcp/tests/test_quality_retry_proof.py:32-55; mcp/tests/test_quality_retry_proof.py:359-383 |
| The compatibility key includes pytest-xdist alongside the other coverage/pytest tool versions, so executor changes invalidate reuse. | `_compatibility_key` | mcp/src/agents_remember/code_quality/retry_proof.py:360-381 |
| Retry planning validates the certifying capability before reading or publishing any cached proof. | `prepare`; `require_dagger_admission_capability` | mcp/src/agents_remember/code_quality/retry_proof.py:157-181; mcp/src/agents_remember/testing/dagger_admission.py:93-101 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The proof remains local to the repository/worktree Git common directory. | — | — |

## 260824-PDLS — Admission-Gated Retry Proof

Retry-proof preparation now requires a verified `DaggerAdmission` capability. A diagnostic runner
cannot publish or restore retry proof, and a matching diagnostic candidate digest is not a
certifying reuse key. Existing content-addressed compatibility checks remain inside the Dagger
quality route.

## Update History

- 2026-08-25T01:56+02:00 — Replaced changed-test-only retry eligibility with the shared
  dependency-owned impact graph; support and fixture deltas are allowed only with complete consumer
  proof, and stale affected contexts are removed before append.
- 2026-08-24T21:23+02:00 — 260824-PDLS added the typed admission boundary and closed diagnostic
  reachability.

- 2026-08-14T11:24+02:00 — R39 curator: removed the obsolete local/CI retry interpretation.
  Proof reuse is now documented solely as a nonce-attested Dagger optimization behind the shared
  before-planning guard. Verification remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T23:56+02:00 — Added pytest-xdist to the documented retry-proof compatibility
  fingerprint; changing the parallel executor version now invalidates cached proof reuse.
  Verification metadata remains pinned until closeout.

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged retry-proof implementation; the existing sidecar remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-10T12:20+02:00 — Made tracked symlink snapshotting Git-faithful after the live retry
  exposed `dashboard/node_modules` as a directory symlink that disabled proof reuse.
- 2026-08-10T07:30+02:00 — Created for the developer-approved cheap-first and content-addressed
  retry pipeline. Verification metadata remains blank until closeout stamps the code commit.
