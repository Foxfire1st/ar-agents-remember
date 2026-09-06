# mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
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
whose manifest binds the candidate tree, profile identity, plan digest, files, and - since
CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`) - the frozen host-level shared Dagger authority
snapshot digest. `run_clean_quality` admits the shared authority (or reuses an explicitly passed frozen
one for retry/recovery) before any Dagger command starts, launches through the deterministic
authority environment (dagger_authority.py), and releases the exact registered owner on
terminalization; the published quality manifest advanced to schema 3.1 with `runtimeAuthorityDigest`.

## Code Commentary

`CleanQualityRequest` carries the code worktree, worktree group, `repository_id`,
`profile_reference`, mode, diff base, optional memory cap, and optional attestation.
`CleanQualityOutcome` wraps the process result with governed evidence and the published manifest.

`run_clean_quality(request, *, authority=...)` validates mode and Windows-interop, admits the host-level
shared Dagger authority when none is passed (registering one exact live owner), prepares the sandbox
(`_prepare_sandbox` clones `--no-local --no-checkout`, checks out the detached HEAD, applies
the staged overlay, resolves the candidate tree, and bundles ancestry), admits the exact profile
execution (`_admit_prepared_profile` -> `load_repository_profile` +
`admit_repository_profile_execution`), writes the sandbox admission manifest
(`_write_sandbox_manifest`, schema `repository-certification-admission/v1`), resolves the
declared executable through the native platform boundary (`_resolve_executor`), and runs the
declared Dagger adapter via `DaggerModuleExecutorAdapter().command(...)`, then releases the exact
authority owner in a `finally` once the run terminalizes. A non-zero exported
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
prunes stale generations (protecting the prior live generation and every exact generation selected by a validated certificate journal), removes the legacy report
projection, and only then writes the manifest. Publication and recovery share the strict
`published_manifest.py` v3 reader.

The existing report reader and historical pruner now live in `report_publication_paths.py`.
`certification_evidence.protected_certificate_generations` validates selected rows against the existing content-addressed store before supplying their exact retention pins. Malformed selected authority or missing/irregular selected generation roots refuse publication before pruning or pointer replacement. Nested report bytes are reopened when a certificate is recorded or reused; obtaining pruning pins does not repeat that byte verification.

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
  manifest is schema `3.1` with profile identity and runtime authority fields (see `published_manifest.py`).
- Only declared published artifacts may be exported; unexpected names/directories/irregular
  entries and oversized artifacts fail closed.
- A completed export may publish a failed pipeline generation for diagnostics; only a passed decoded pipeline mints certifying evidence, and `gate.py` refuses a pass without a published manifest.
- Recovery callers pass one immutable manifest snapshot through every artifact lookup; a pointer
  rotation cannot mix generations.
- Every Dagger launch crosses the shared authority boundary: the admitted snapshot digest is bound
  into the sandbox manifest and the published schema-v3.1 manifest, and only the exact registered
  owner is released at terminalization (an explicitly passed frozen authority is never re-admitted
  or released here).

### Todos

None.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| Only the admitted executable is resolved for the profile adapter. | `_resolve_executor`; `_executor_command` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:965-966; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:253-284 |
| An unavailable admitted executor produces a typed prerequisite failure. | `_executor_prerequisite_failure` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:951-978 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The executor admits authority, materializes the candidate and executes the profile adapter. | `run_clean_quality`; `_prepare_sandbox`; `_admit_prepared_profile`; `_write_sandbox_manifest` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:146-233; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:340-381; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:236-250; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:384-417 |
| Exported decoder bytes determine the pipeline result and whether certifying evidence exists. | `_publish_executor_outcome`; `_exported_pipeline_exit` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:287-337; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:424-437 |
| Publish one immutable evidence generation, then atomically point readers at it. | "def _publish_reports" | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:437-532 |
| Export inventory validation checks the declared report members before publication. | "def _validated_export_inventory" | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:535-556 |
| Immutable generation identity includes the exported report inventory. | "def _generation_digest" | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:596-611 |
| Mint from one caller-held immutable generation snapshot. | "def certifying_evidence_from_published_manifest" | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:733-764 |
| One serialized acceptance firewall shared by lifecycle consumers. | "def require_published_quality_evidence" | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:767-779 |
| The single report reader and pruner implementation live in the path owner. | `published_report_path_from_manifest`; `_prune_report_generations` | mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py:86-116; mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py:119-138 |

## Cross-Repo References

The external execution boundary is the profile-declared Dagger runtime; its declaration is resolved through the native platform boundary. This file does not define a separate cross-repository protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact admitted executor and frozen authority determine the launch command. | `_executor_command` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:253-284 |

## 260821-DAGQC-L2 And 260824-PDLS Historical Notes

The strict schema-based manifest and one-snapshot recovery model introduced by those waves remain
in force but are now profile-bound: the manifest schema advanced to `3.0` with profile identity
fields, and evidence is minted only from a digest-verified passed generation.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_executor_prerequisite_failure` repointed to mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:951-978. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:19+00:00 — L30 source review at `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Preserved selected certificate generations during publication, moved the shared reader/pruner ownership, corrected failed-generation versus certifying-evidence wording and refreshed source extents.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the authority-bound executor cutover - `run_clean_quality` admits or reuses the host-level shared Dagger authority, writes the snapshot into the sandbox manifest, launches through the deterministic authority environment, releases the exact owner on terminalization, and publishes schema-v3.1 manifests carrying `runtimeAuthorityDigest`; re-anchored reference ranges to the current 1030-line layout.


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
