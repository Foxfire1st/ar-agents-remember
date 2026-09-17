# mcp/src/agents_remember/memory/knowledge/endpoints.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/endpoints.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../../overview.md)

## Purpose

The endpoint-existence checks shared by the two relation writes. A membership and a realization claim
both name an exact revision, and both must refuse a missing endpoint **with the offending identity
named** before any row is written. One module answers that question so the two operations cannot drift
into reporting different codes for the same failure, and so "the endpoint does not exist" stays a
single definition per endpoint kind.

This module owns no table. It is a two-function contract owner: the shared *question* the relation
modules ask, and the `RelationWrite` vocabulary that names which operation is asking.

## Code Commentary

### Logic

- `require_family_revision_endpoint` asks `families.family_id_of_revision` whether the named family
  revision exists in the bound namespace; when it does not, it raises `KnowledgeRefused` carrying
  `missing_relation_endpoint_refusal`.
- `require_invariant_revision_endpoint` asks `store.get_revision` the same question for the invariant
  half.
- Both refusals carry `endpoint_kind` as the human-readable kind ("family revision", "invariant
  revision"), the declared table, the relation identity and the endpoint identity, so a caller is sent
  to the exact row rather than to the relation in general.
- `RelationWrite` is a closed literal of the two relation operations. It exists so a refusal cannot
  name an operation that does not write relations.

### Conventions

- The functions take the opened store as their first argument, exactly like the operations that call
  them, and they never open a transaction of their own — they are called *inside* the caller's
  immediate transaction, before its first write.
- They raise `KnowledgeRefused` rather than returning a result. That is the package's internal
  control-flow signal: the calling operation catches it and converts it into its own typed refusal
  result, so the public surface never exposes an exception.

### Invariants And Boundaries

- **Checks come before any DML.** Both callers run these checks before their first `INSERT`, which is
  what makes "a refused relation writes nothing" true by ordering rather than by rollback.
- **The endpoint kinds are not interchangeable.** A family revision is resolved through the family
  module and an invariant revision through the store; neither can be substituted for the other, and
  the separate functions make that structurally visible.
- **One definition per failure.** The two relation modules do not carry their own "not found" wording
  or their own codes; a change here changes both relations at once, which is the point.
- **Boundary.** This module decides existence, not legality. Whether the *pair* is already related is
  the relation module's own duplicate check, and whether the row matches what the caller expected is
  the removal path's stale-precondition check.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one-definition-per-endpoint-kind rationale this module exists for. | "the endpoint does not exist" | mcp/src/agents_remember/memory/knowledge/endpoints.py:5-6 |
| The closed relation-operation vocabulary a refusal may name. | `RelationWrite` | mcp/src/agents_remember/memory/knowledge/endpoints.py:22-22 |
| The family-revision endpoint check. | `require_family_revision_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:25-40 |
| The invariant-revision endpoint check. | `require_invariant_revision_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:42-56 |
| The refusal these checks raise, with its endpoint kind and identity facts. | `missing_relation_endpoint_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:442-469 |
| The narrow ownership read that answers the family half. | `family_id_of_revision` | mcp/src/agents_remember/memory/knowledge/families.py:285-301 |
| The seal-verifying read that answers the invariant half. | `get_revision` | mcp/src/agents_remember/memory/knowledge/store.py:161-177 |
| The membership operation that calls both checks before its write. | `create_family_member` | mcp/src/agents_remember/memory/knowledge/memberships.py:88-107 |
| The realization operation that calls the invariant check before its write. | `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/realizations.py:61-83 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `family_id_of_revision` repointed to mcp/src/agents_remember/memory/knowledge/families.py:285-301. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `create_family_member` repointed to mcp/src/agents_remember/memory/knowledge/memberships.py:88-107. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new shared endpoint module. It records that the module owns a question rather than a table, that both checks run inside the caller's transaction before its first write (which is why a refused relation provably writes nothing), and the boundary between existence here and pair-duplication in the relation modules. Verification metadata remains empty until closeout stamps the code commit.
