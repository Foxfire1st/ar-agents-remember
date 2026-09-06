# mcp/src/agents_remember/models/certification/base.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/certification/base.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:03:08+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Package overview](overview.md)

## Purpose

Owns the closed frozen wire primitives shared by certification-domain and lifecycle models.

## Code Commentary

### Logic

`GateId` fixes the five gate identifiers. `SemanticText` rejects blank or padded text. `FrozenContractModel` forbids extra fields and freezes model assignment; `RailIdentity` constrains its identifier and semantic version and derives the `railId@version` key.

### Conventions

These are shared value constraints. Registry, plan, result, admission and journal owners import them directly instead of maintaining parallel model bases.

### Invariants And Boundaries

- A valid rail identity does not establish registry membership, applicability or execution success.
- The module validates wire shape; semantic digests and owner currentness are established by the consuming domain owners.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate identifiers are closed to the five gates. | `GateId` | mcp/src/agents_remember/models/certification/base.py:9-9 |
| Semantic text rejects blank and padded values. | `_require_semantic_text`; `SemanticText` | mcp/src/agents_remember/models/certification/base.py:21-24; mcp/src/agents_remember/models/certification/base.py:27-27 |
| The shared model base rejects extra fields and freezes model assignment. | `FrozenContractModel` | mcp/src/agents_remember/models/certification/base.py:30-33 |
| Rail identities validate identifier/version shape and derive a stable key. | `RailIdentity` | mcp/src/agents_remember/models/certification/base.py:36-42 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:48:58+00:00 — Created from source at `c69d5171187fa1957025e393270db9f5a864ab14` for the shared wire/generation ownership split. Verification records source review, not gate execution or acceptance.
