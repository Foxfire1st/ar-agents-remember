# mcp/src/agents_remember/worktrees/modules/quality/certification_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/certification_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Connects the profile-backed quality gate to R21 admission, terminal result manifests and certificates. It consumes verified published generation data and records refusals when the supplied rail evidence cannot support certification.

## Code Commentary

### Logic

`prepare_certification_records` currently registers memory rails only for repository id `agents-remember`. It loads the exact profile, compiles the repository plan against the supplied candidate tree, obtains memory rails through the bound service port, and persists admission under the enclosure's certification-records directory before execution.

`record_published_generation` first requires equality of candidate tree, profile digest, full repository plan digest and selection. It processes the decoder's gate catalog in order with the accumulated predecessor certificates. A missing catalog produces an empty selection journal. Non-green catalog entries retain terminal status without a result manifest at this branch; green entries must contain every planned rail and valid observed evidence/artifact bindings.

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

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission freezes the exact repository lane and preserves original stored provenance. | `prepare_certification_records`; `_persist_admission` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:165-200; mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:535-549 |
| Published candidate and complete profile plan must agree before recording. | `_require_publication_admission`; `record_published_generation` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:256-274; mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:209-253 |
| The selected journal is bounded and validated before atomic replacement. | `journal_gate_records` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:289-308 |
| Result and certificate publication reopens nested evidence and original objects. | `_record_gate`; `_publish_gate_result` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:311-339; mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:342-394 |
| Rail observations and the memory catalog come from their declared owners. | `_terminal_results`; `_bound_memory_rails` | mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:413-463; mcp/src/agents_remember/worktrees/modules/quality/certification_records.py:493-507 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:19+00:00 — L30 source review at `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Recorded exact publication retention, canonical object reopening, and propagated refusals; preserved the remaining red-run and lifecycle integration boundaries.

- 2026-09-05T06:14:14+00:00 — Created the exact production record-consumer account, including refusal journaling and unresolved composition/propagation boundaries.
