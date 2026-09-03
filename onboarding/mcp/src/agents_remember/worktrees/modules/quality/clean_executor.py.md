# mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

This module runs the exact repository-profile-declared Dagger adapter over a clean, exact staged
candidate and publishes the certified report generation into the worktree enclosure. Since
CCR-R22@v1 (L22, commit `685f83c44055`) it executes only the admitted profile's selected
executor adapter and result decoder; it no longer recognizes a fixed Agents Remember report
inventory, a hardcoded wrapper path, or repository commands. The module materializes an isolated
sandbox clone of the exact candidate (HEAD plus the staged overlay), admits the candidate's own
profile from inside that sandbox, runs the declared adapter, and publishes an immutable generation
whose manifest binds the candidate tree, profile identity, plan digest, and files.

## Code Commentary

`CleanQualityRequest` carries the code worktree, worktree group, `repository_id`,
`profile_reference`, mode, diff base, optional memory cap, and optional attestation.
`CleanQualityOutcome` wraps the process result with governed evidence and the published manifest.

`run_clean_quality(request)` validates mode and Windows-interop, prepares the sandbox
(`_prepare_sandbox` clones `--no-local --no-checkout`, checks out the detached HEAD, applies
the staged overlay, resolves the candidate tree, and bundles ancestry), admits the exact profile
execution (`_admit_prepared_profile` -> `load_repository_profile` +
`admit_repository_profile_execution`), writes the sandbox admission manifest
(`_write_sandbox_manifest`, schema `repository-certification-admission/v1`), resolves the
declared executable through the native platform boundary (`_resolve_executor`), and runs the
declared Dagger adapter via `DaggerModuleExecutorAdapter().command(...)`. A non-zero exported
pipeline result returns the outcome with no evidence; a start failure raises a typed
`CertificationExecutorPrerequisiteError` bound to the earliest affected gate and corrective
owners.

`_publish_executor_outcome` publishes reports (`_publish_reports`), re-validates the
generation manifest, decodes the authoritative terminal result through the declared
`JsonExitStatusDecoder`, mints `CertifyingTestEvidence` only for a passed pipeline, and writes
`quality-progress.json` status.

`_publish_reports` writes one immutable generation directory and atomically advances the
`quality-report-set.json` pointer: it validates the export inventory against the profile-declared
published artifacts (no unexpected names/directories/irregular entries, size limits enforced for
each declared artifact), requires pass-only required publications, computes the generation digest
from candidate tree + profile identity + files + dependencies, stages and validates the generation,
prunes stale generations (protecting the prior live generation), removes the legacy report
projection, and only then writes the manifest. Publication and recovery share the strict
`published_manifest.py` v3 reader.

Helper boundaries: `published_report_path_from_manifest`, `published_generation_root`,
`published_quality_attestation`, `certifying_evidence_from_published_manifest`, and
`require_published_quality_evidence` resolve artifacts and evidence only from one immutable
manifest snapshot. `_stream_dagger` streams bounded progress/result output to the enclosure
`dagger-progress.log` and `quality-progress.json`.

### Conventions

The certified adapter comes entirely from the repository profile: executable, function name,
arguments, reports field, export destination, decoder, published artifacts, and result decoder are
declared profile data. The framework adds only the exact candidate source, bundle, manifest, mode,
diff base, export root, and optional memory cap.

### Invariants And Boundaries

- The executed command is built only from the admitted profile bytes; host-quality execution is
  never a fallback (`gate.py` refuses the host diagnostic route).
- The profile is admitted from inside the sandboxed candidate, so the bytes certified are the
  candidate's own profile, not the host checkout's.
- Candidate Git identity must match before and after publication (`gate.py` re-verifies the
  write-tree); sandbox materialization preserves the exact staged overlay.
- Reports are atomically replaced as one immutable generation, never accumulated per run; the
  manifest is schema `3.0` with profile identity fields (see `published_manifest.py`).
- Only declared published artifacts may be exported; unexpected names/directories/irregular
  entries and oversized artifacts fail closed.
- A passed pipeline is required to publish a manifest; `gate.py` refuses a pass with no published
  manifest.
- Recovery callers pass one immutable manifest snapshot through every artifact lookup; a pointer
  rotation cannot mix generations.

### Todos

None.

## Docs References

The executor contract is CCR-R22@v1's repository-owned adapter boundary: the MCP must execute
only the exact admitted profile bytes through the declared sandbox adapter, and an executor that
was valid at admission but unavailable at execution produces a typed executor prerequisite
failure owned by the affected gate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The MCP executes only the exact admitted bytes through the declared sandbox adapter; configuration cannot inject host execution outside the admitted executor boundary. | `## Required Profile Contract` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |
| An executor valid at admission but unavailable at execution produces a typed executor prerequisite failure owned by the affected gate. | `## Failure And Recovery` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The executor prepares the exact candidate sandbox, admits the profile execution, runs the declared adapter, and publishes the certified generation. | `run_clean_quality`; `_prepare_sandbox`; `_admit_prepared_profile`; `_write_sandbox_manifest`; `_publish_executor_outcome` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:90-144; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:246-308; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:164-176; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:220-251; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:198-219 |
| Profile-bound publication: inventory validated against declared artifacts, generation digest binds candidate + profile identity, atomic pointer advance. | `_publish_reports`; `_validated_export_inventory`; `_generation_digest`; `_profile_identity` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:311-383; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:413-443; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:560-586; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:445-462 |
| Manifest/artifact/evidence helpers consume one strict snapshot. | `published_report_path_from_manifest`; `certifying_evidence_from_published_manifest`; `require_published_quality_evidence` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:655-668; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:683-706; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:708-714 |
| The strict gate admits the same profile and enforces candidate identity around the run. | `run_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:235-278 |
| The generic decoder replaces the deleted hardcoded result-inventory validator. | (deleted) `validate_result_artifact_references` | mcp/src/agents_remember/worktrees/modules/quality/result_artifacts.py (removed at this commit) |

## Cross-Repo References

The only external boundary is the pinned Dagger container/tool runtime resolved through the
profile-declared executable; for a consuming repository that executable is that repository's own
declared adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared executable is resolved through the native platform boundary, then run by the Dagger adapter. | `_resolve_executor`; `_executor_command`; `_stream_dagger` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:928-929; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:178-196; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:802-866 |

## 260821-DAGQC-L2 And 260824-PDLS Historical Notes

The strict schema-based manifest and one-snapshot recovery model introduced by those waves remain
in force but are now profile-bound: the manifest schema advanced to `3.0` with profile identity
fields, and evidence is minted only from a digest-verified passed generation.

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): rewrote the card for the repository-profile executor cutover. `CleanQualityRequest` now carries `repository_id`/`profile_reference`/mode; the module admits the candidate's own profile, runs the profile-declared Dagger adapter and decoder, and publishes a schema-v3 manifest with profile identity; the fixed report-inventory/constants model (EXPORTED_REPORT_NAMES, CODEX_VERSION, base/venv runtime proofs, `_resolve_dagger`) was replaced by declared published artifacts and `_resolve_executor`.

- 2026-08-31T08:05+02:00 -- 260821-ARSPAWN-L5 A004 correction: recorded strict prior-pointer resolution, pre-pointer historical-generation validation/pruning with prior-live protection, and the invariant that atomic pointer replacement is the final publication operation.

- 2026-08-31T04:50+02:00 -- 260821-ARSPAWN-L5 independent-review repair: documented recursive, allowlisted publication of the ambient E2E directory and staged-generation validation that prevents nested evidence from being silently discarded. Verification remains closeout-owned.

- 2026-08-30T21:25+02:00 -- 260821-ARSPAWN-L5 refreshed the executor's exact Codex admission pin from 0.147.0 to 0.151.0 in lockstep with the certifying Dagger graph. Verification remains closeout-owned.

- 2026-08-29T16:27+02:00 -- Added both canonical Python runtime proofs to the immutable recognized quality-report generation.

- 2026-08-25T08:16+02:00 -- 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 -- 260824-PDLS added phase export and the sole certifying evidence factory at verified publication altitude.
- 2026-08-24T14:19+02:00 -- 260821-DAGQC-L2: unified report publication and recovery on the strict schema-1.0 manifest and one-snapshot artifact lookup. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-17T12:30+02:00 -- 260815-DAG-L5: report publication now carries an attestation; added `published_quality_attestation`. Verification remains closeout-owned.

- 2026-08-14T06:36+02:00 -- L23 final candidate review: the Dagger executor starts a fresh attempt, makes two report projections share one authoritative result, bounds live output, prunes stale predecessor reports, and fails closed on status reads; no local runner remains.

- 2026-08-13T08:40+02:00 -- L23 integration-gate repair: recorded that report promotion now routes through `kernel.atomic_write.atomic_replace` instead of calling `os.replace` directly. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 -- Created for L23's pinned, observable Dagger quality executor; verification provenance remains closeout-owned.
