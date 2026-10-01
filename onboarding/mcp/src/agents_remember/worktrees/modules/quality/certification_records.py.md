# mcp/src/agents_remember/worktrees/modules/quality/certification_records.py

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Connects the profile-backed quality gate to R21 admission, terminal result manifests and certificates. It consumes verified published generation data and records refusals when the supplied rail evidence cannot support certification.

## Code Commentary

### Logic

`prepare_certification_records` admits the supplied repository profile and bound memory registry for every repository; unsupported or unbound authority refuses. It loads the exact profile, compiles the repository plan against the supplied candidate tree, obtains memory rails through the bound service port, and persists admission under the enclosure's certification-records directory before execution.

`record_published_generation` first requires equality of candidate tree, profile digest, full repository plan digest and selection. It processes the decoder's gate catalog in order with the accumulated predecessor certificates. The catalog parser requires actual terminal records. Red and interrupted catalogs retain typed result manifests and publication bindings without certificates; green entries require every planned rail and observed evidence. Reused entries must consume exactly the supplied retained prefix, with duplicate or unreported retained gates refused.

Before storing a result, `_publish_gate_result` reopens every nested evidence and artifact through the exact immutable publication. Green results produce content-addressed certificates and a journal row containing the complete accepted publication snapshot. `publication_binding` preserves a previously selected generation for a semantically identical certificate. A publication-binding mismatch preserves the existing selection journal and returns a typed refusal; other invalid outcomes are journaled. `journal_gate_records` validates the bounded population and cross-binds selected rows to real store objects before atomic replacement.

Reusing admission or certificate identities reopens the original object through the canonical store, retaining its genuine provenance. It does not suppress an arbitrary collision error: malformed objects, invalid semantic digests and wrong content addresses still refuse. `load_execution_records` returns `None` for absent, unreadable or wrong-schema admission data; callers must separately establish exact currentness.

### Conventions

Keep memory-domain imports behind `CertificationMemoryRailsPort`. Executor bytes and canonical object loaders supply observations; never fabricate bindings or creation provenance.

### Invariants And Boundaries

- Published candidate, profile, full plan and selection must match admission before any gate recording.
- Green disposition does not excuse missing or changed evidence bytes.
- Invalid/non-green outcomes publish no reusable certificate; the ordinary gate caller now propagates returned certification refusals.
- Selected certificate rows retain complete immutable publication identities, and only the canonical store validates existing semantic objects.
- This module does not call typed lifecycle admission/finalization, durable telemetry or the final Gate-5 executor.
- Ordinary failed runs still raise before this helper in `gate.py`; complete red/interrupted result publication remains a production composition obligation.

### Todos

Complete typed lifecycle composition and all-terminal-outcome publication in their owning recovery leaves. L30 supplies retained report evidence and refusal propagation; it does not establish those later protocols.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

- Freeze the complete profile and registered memory authority before Gate 1. [1]
- Admission persistence preserves the stored admission provenance. [2]
- Published candidate and complete profile plan must agree before recording. [3]
- The selected journal is bounded and validated before atomic replacement. [4]
- Result and certificate publication reopens nested evidence and original objects. [5]
- Map a terminal gate catalog into typed rail results (payload-bound). [6]
- Memory rails are read through the bound certification-memory owner. [7]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.

## Current Landed Composition

`PreparedCertificationRun` carries the complete frozen run. `prepared_from_frozen_run` revalidates the supplied model and exact original store reference, avoiding profile or journal rediscovery. Result recording returns `RecordedCertificationGeneration` with actual terminals and presentation rows; a missing green certificate is never replaced with a manufactured pass.
