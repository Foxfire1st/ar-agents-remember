# mcp/src/agents_remember/models/lifecycles/preparation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/preparation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Memory reuse binds exact raw HEAD/tree plus certified content and cannot simultaneously request a new write. | L26-L26; L43-L69; L171-L192 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| `_canonical_preparation_path` owns the corresponding behavior described above. | L30-L40 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| `ExistingMemoryPreparationProof` owns the corresponding behavior described above. | L43-L69 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| `_one_header` owns the corresponding behavior described above. | L331-L338 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| `_identity_date` owns the corresponding behavior described above. | L341-L354 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| `_require_output_headers` owns the corresponding behavior described above. | L357-L377 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |
| `require_prepared_output_matches_intent` owns the corresponding behavior described above. | L380-L414 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Replaced ledger-mapping reuse proof with exact historical HEAD/tree and separately certified memory content. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
