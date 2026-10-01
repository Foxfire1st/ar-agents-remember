# mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py

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

## Evidence

### Docs References

- Only the admitted executable is resolved for the profile adapter. [1]
- An unavailable admitted executor produces a typed prerequisite failure. [2]

### Repo-Internal References

- The executor admits authority, materializes the candidate and executes the profile adapter. [3]
- Exported decoder bytes determine the pipeline result and whether certifying evidence exists. [4]
- Publish one immutable evidence generation, then atomically point readers at it. [5]
- Export inventory validation checks the declared report members before publication. [6]
- Immutable generation identity includes the exported report inventory. [7]
- Mint from one caller-held immutable generation snapshot. [8]
- One serialized acceptance firewall shared by lifecycle consumers. [9]
- The single report reader and pruner implementation live in the path owner. [10]

### Cross-Repo References

The external execution boundary is the profile-declared Dagger runtime; its declaration is resolved through the native platform boundary. This file does not define a separate cross-repository protocol.

- The exact admitted executor and frozen authority determine the launch command. [11]

## 260821-DAGQC-L2 And 260824-PDLS Historical Notes

The strict schema-based manifest and one-snapshot recovery model introduced by those waves remain
in force but are now profile-bound: the manifest schema advanced to `3.0` with profile identity
fields, and evidence is minted only from a digest-verified passed generation.

## Current Landed Composition

Selected execution carries `CodeCertificationExecution`, a current launch-authority callback and a selected-generation protection callback. It validates the explicit comparison base, reconstructs retained report transport for a suffix, and reopens launch authority only after sandbox/profile/manifest preparation completes. Selected execution without a launch callback refuses. Publication reobserves the selected generation set before pruning and validates that it is a frozen set of full generation digests. Sandbox profile/manifest helpers now live in `quality/execution/sandbox.py`.
