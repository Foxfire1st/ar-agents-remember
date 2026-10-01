# mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py

## Governing Overview

[Worktree modules overview](../overview.md)

## Purpose

Owns the exact immutable report-generation bindings selected by the existing gate-record journal. It connects each selected certificate to canonical stored result/certificate objects and the retained bytes they certify, without introducing a historical scan or another authority store.

## Code Commentary

### Logic

`read_gate_records` opens only `certification-records/gates.json`, enforces an 8 MiB byte bound and the exact journal schema, and treats an absent file as no selection. A valid journal with an empty gate list also returns an empty tuple. `validate_gate_records` allows at most five rows, rejects malformed/duplicate gate identities, and requires valid result/publication identities for both certificate and terminal rows.

`verify_selected_publications` loads the selected canonical objects and cross-binds row gate, result digest, candidate, registry, gate plan, admitted profile and selection. A syntactically valid publication from another authority is refused even if report bytes happen to match. `protected_certificate_generations` returns only those selected generation ids and requires their real retained directories to exist before the publisher can prune.

`publication_binding` first proves the supplied certificate/result/publication relation. For a certificate already selected, it reuses the original publication only when its result, gate and full execution authority agree; execution authority includes the full profile plan, selection, adapter, decoder and runtime digest. It then reopens every nested rail evidence/artifact through that one retained snapshot and serializes the complete snapshot into the new journal row.

`verify_result_evidence` checks each reference's declared digest and size against the snapshot inventory and delegates confined bounded physical reopening to `report_publication_paths`. Unavailable, changed or foreign bytes produce typed `CertificationContractError` findings. This owner does not mint certificates, move the current pointer or delete reports.

### Conventions

Canonical store loaders own object shape, semantic digest and exact content address. Keep physical generation/audit provenance separate from semantic execution identity, while retaining the original selected provenance when reusing an equal certificate.

### Invariants And Boundaries

- Read one bounded selected journal; never discover authority by scanning history or a current report pointer.
- Every selected certificate requires a complete publication snapshot and exact canonical result/certificate objects.
- Reuse preserves the original generation only after full execution-authority equality and physical evidence verification.
- Selected generations remain protected until their journal selection changes or the lifecycle cleanup owner reclaims the enclosure.
- Gate acceptance still belongs to the certificate compiler and its caller; these read checks alone do not complete lifecycle or Gate-5 composition.

### Todos

None recorded for this file's bounded read/retention responsibility.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository.

No external domain documentation is configured.

### Repo-Internal References

- The exact selected journal is bounded and validates certificate rows. [1]
- Cross-bind selections to their exact stored objects before publishing or pruning. [2]
- Selected certificates pin exact generations until journal replacement or cleanup. [3]
- Publication verification checks certificate, result and publication identity together. [4]
- Retain the original selected generation for a semantically identical certificate. [5]
- Execution identity excludes physical generation, report bytes and audit provenance. [6]
- Open every emitted binding through its one accepted immutable generation. [7]
- Published artifact references are opened through their accepted snapshot. [8]

### Cross-Repo References

No cross-repository implementation protocol is defined here.

No cross-repository evidence is required for these local claims.

## Current Landed Composition

Non-certifying terminal rows bind their result to an exact stored `FrozenCertificationRun`. The verifier compares registry, certification/gate plan, candidate, profile altitude, repository plan and publication identity before retaining the terminal generation. A terminal row cannot substitute for a certificate; its frozen-run reference is type-checked by the canonical object store.
