# mcp/src/agents_remember/models/lifecycles/preparation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/preparation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Closed preparation intent, genuine existing memory proof and raw commit output vocabulary.

## Code Commentary

### Logic

`PreparationLeg` is `code` or `memory-content`. Existing memory reuse binds the exact
`logicalHeadCommit` and raw `logicalHeadTree`, plus a separate `certifiedContentTree` for the
cache-free memory view. It requires no ledger blob or code-to-memory cache row. A reused intent
must retain that exact historical HEAD/tree and cannot also enable a new write.

Intents bind one operation/generation/leg to logical roots, common repository, expected-old and preparation-parent identities, admitted tree, observed configuration/hooks and original frozen-run/candidate/certificate references. Enabled writes require a real private path and message. Existing code forbids invented private inputs. Existing memory reuse requires an exact HEAD/tree and certified-content proof. Memory intents require a Gate-5 certificate reference, whose actual authority is checked above the model layer. The raw-byte factory derives commit/tree/parents/identity/date/message/signature-presence digests and validates their exact intent relationship. Signature presence is not signature verification; private existence is not delivery or certification.

### Conventions

Use the named source owners directly. The original source was introduced in commit `245057ab16e19afdaabd5c188c9576b22e0c0870`; the current uncommitted LCA-L9 candidate changes its reuse proof. Historical verification metadata remains distinct from that candidate review.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Memory reuse binds exact raw HEAD/tree plus certified content and cannot simultaneously request a new write. | `PreparationLeg` | mcp/src/agents_remember/models/lifecycles/preparation.py:26 |
| `_canonical_preparation_path` owns the corresponding behavior described above. | `_canonical_preparation_path` | mcp/src/agents_remember/models/lifecycles/preparation.py:30-31 |
| `ExistingMemoryPreparationProof` owns the corresponding behavior described above. | `ExistingMemoryPreparationProof` | mcp/src/agents_remember/models/lifecycles/preparation.py:43-44 |
| `_one_header` owns the corresponding behavior described above. | `_one_header` | mcp/src/agents_remember/models/lifecycles/preparation.py:331-332 |
| `_identity_date` owns the corresponding behavior described above. | `_identity_date` | mcp/src/agents_remember/models/lifecycles/preparation.py:341-342 |
| `_require_output_headers` owns the corresponding behavior described above. | `_require_output_headers` | mcp/src/agents_remember/models/lifecycles/preparation.py:357-359 |
| `require_prepared_output_matches_intent` owns the corresponding behavior described above. | `require_prepared_output_matches_intent` | mcp/src/agents_remember/models/lifecycles/preparation.py:380-382 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | — | — |

## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Replaced ledger-mapping reuse proof with exact historical HEAD/tree and separately certified memory content. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
