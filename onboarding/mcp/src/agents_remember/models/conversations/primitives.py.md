# mcp/src/agents_remember/models/conversations/primitives.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/models/conversations/primitives.py`    |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/primitives.py` is the lowest layer of the responsibility-owned
conversation wire models (260731-EFA-L9 R1): strict immutable wire configuration and the opaque
purpose-branded token root every cursor/operation identity derives from.

## Code Commentary

### Logic

`WireModel` (cit:(["class WireModel"], mcp/src/agents_remember/models/conversations/primitives.py:15-15)) makes public DTOs immutable, camel-case on the wire, and
closed to unknown fields. `_OpaqueToken` (cit:(["class _OpaqueToken"], mcp/src/agents_remember/models/conversations/primitives.py:26-26)) is the branded
`RootModel[str]` base; `OperationFingerprint` (cit:(["class OperationFingerprint"], mcp/src/agents_remember/models/conversations/primitives.py:44-44)) is its
SHA-256 operation-identity specialization.

### Conventions

- Purpose-prefixed opaque types keep active-page, active-event, library-list, library-read,
  library-key, private native-resume, and operation identities non-interchangeable.

### Invariants And Boundaries

- This module must not import any sibling conversation module (it is the layer bottom); the armed
  layering rail and resolved-forward-reference architecture test preserve that boundary without a
  task/date snapshot.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-25T01:56+02:00 — 260824-PDLS replaced the retired split baseline reference with the
  stable architecture owner; verification remains closeout-owned.
- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the primitives layer moved from
  `serving/conversation/_models_wire.py`. Verification metadata pinned until closeout stamps the
  L9 code commit.
