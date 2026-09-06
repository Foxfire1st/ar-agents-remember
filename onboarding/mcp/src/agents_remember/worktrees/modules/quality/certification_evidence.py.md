# mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain documentation is configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact selected journal is bounded and validates certificate rows. | `read_gate_records`; `validate_gate_records` | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:31-56; mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:59-81 |
| Cross-bind selections to their exact stored objects before publishing or pruning. | "def verify_selected_publications" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:101-124 |
| Selected certificates pin exact generations until journal replacement or cleanup. | "def protected_certificate_generations" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:86-98 |
| Publication verification checks certificate, result and publication identity together. | "def verify_publication_authority" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:152-183 |
| Retain the original selected generation for a semantically identical certificate. | "def publication_binding" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:127-149 |
| Execution identity excludes physical generation, report bytes and audit provenance. | "def _execution_authority" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:268-278 |
| Open every emitted binding through its one accepted immutable generation. | "def verify_result_evidence" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:281-295 |
| Published artifact references are opened through their accepted snapshot. | "def _verify_reference" | mcp/src/agents_remember/worktrees/modules/quality/certification_evidence.py:298-309 |

## Cross-Repo References

No cross-repository implementation protocol is defined here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these local claims. | N/A | N/A |

## Current Landed Composition

Non-certifying terminal rows bind their result to an exact stored `FrozenCertificationRun`. The verifier compares registry, certification/gate plan, candidate, profile altitude, repository plan and publication identity before retaining the terminal generation. A terminal row cannot substitute for a certificate; its frozen-run reference is type-checked by the canonical object store.

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:19+00:00 — L30 source review at `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Created the exact selected-journal, semantic cross-binding, retained-generation and physical-evidence account from the prepared code object.
