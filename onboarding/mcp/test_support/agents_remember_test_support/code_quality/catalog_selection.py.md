# mcp/test_support/agents_remember_test_support/code_quality/catalog_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/catalog_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:52:19+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Quality verification overview](overview.md)

## Purpose

Narrows explicit lifecycle catalog consumer-list edits while retaining consumers removed by the change.

## Code Commentary

### Logic

`changed_catalog_consumers` parses both TOML versions. Only matching outer configuration and matching ordered artifact declarations can narrow selection. Each artifact must retain all fields other than its consumer list. Consumer lists must contain nonempty strings. A changed list contributes the union of old and new consumer paths, so deleting a consumer does not erase its impact.

### Conventions

An empty frozenset represents no changed consumer population. `None` means broader catalog semantics changed or its shape cannot safely narrow. Invalid TOML raises; it is not converted into an empty declaration.

### Invariants And Boundaries

Schema, scope, contract, artifact addition/removal and lifecycle-policy changes retain global invalidation through the caller. This helper returns dependency information; it neither runs tests nor grants certification authority.

### Todos

No source-local TODO is asserted.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pure old/new consumer comparison preserves removed consumers and refuses broader narrowing. | `changed_catalog_consumers` | mcp/test_support/agents_remember_test_support/code_quality/catalog_selection.py:9-40 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository authority is used. | N/A | N/A |

## Update History

- 2026-09-06T21:52:19+00:00 — Created from landed IAS source during missing-baseline recovery. Verification metadata remains unset; no execution or acceptance is claimed.
