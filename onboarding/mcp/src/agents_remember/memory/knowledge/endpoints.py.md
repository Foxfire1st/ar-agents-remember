# mcp/src/agents_remember/memory/knowledge/endpoints.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/endpoints.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `4a0442d62eb842661a3dd04686c376d0f0dbc61f`|
| lastVerifiedCommitDate | 2026-09-20T14:22:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

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

**A sixth endpoint kind, and the strictest of them.** `require_facet_revision_endpoint` is the one operation `add_evidence_claim` adds to `RelationWrite`. It is deliberately stricter than the revision-table lookups beside it: a facet revision is a `record_revision` row whose *owning envelope* carries one of the eight authored-judgment kinds, so a stored revision of a detection record or of another evidence claim is not a facet revision and is refused as the missing endpoint it is — naming the kind the caller asked for and the identity it named — rather than resolving to 'some revision exists'. The module's own docstring records the vocabulary's history: the finding that closed it at two members, the facet leaf that took it to four, and this leaf's addition of `add_evidence_claim`, the one operation that resolves a claim's subject, its evidence anchor and every claimed-coverage endpoint.

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
| The closed relation-operation vocabulary a refusal may name. | "RelationWrite = Literal[" | mcp/src/agents_remember/memory/knowledge/endpoints.py:81-81 |
| The family-revision endpoint check. | `require_family_revision_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:121-135 |
| The invariant-revision endpoint check. | `require_invariant_revision_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:138-152 |
| The refusal these checks raise, with its endpoint kind and identity facts. | `missing_relation_endpoint_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:442-469 |
| The narrow ownership read that answers the family half. | `family_id_of_revision` | mcp/src/agents_remember/memory/knowledge/families.py:285-301 |
| The seal-verifying read that answers the invariant half. | `get_revision` | mcp/src/agents_remember/memory/knowledge/store.py:228-243 |
| The membership operation that calls both checks before its write. | `create_family_member` | mcp/src/agents_remember/memory/knowledge/memberships.py:88-107 |
| The realization operation that calls the invariant check before its write. | `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/realizations.py:61-83 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T11:53:49+00:00: Generated citation repair: `get_revision` repointed to mcp/src/agents_remember/memory/knowledge/store.py:228-243. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "RelationWrite = Literal[" repointed to mcp/src/agents_remember/memory/knowledge/endpoints.py:81-81. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_family_revision_endpoint` repointed to mcp/src/agents_remember/memory/knowledge/endpoints.py:121-135. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_invariant_revision_endpoint` repointed to mcp/src/agents_remember/memory/knowledge/endpoints.py:138-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "RelationWrite = Literal[" repointed to mcp/src/agents_remember/memory/knowledge/endpoints.py:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand while resolving the memory sync** — `RelationWrite`, `require_family_revision_endpoint`, `require_invariant_revision_endpoint`, `family_id_of_revision`, `create_family_member`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): re-read this card's claims against the source and re-cited the rows this leaf's additions moved: `RelationWrite` gained `create_composition` and `set_family_revision_route`, and the module gained `require_route_endpoint`, so a relation write reached directly reports a composition operation rather than borrowing a neighbouring name. The relocations are a read of each declaration's own extent, not a projection. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand** — `RelationWrite`, `require_family_revision_endpoint`, `require_invariant_revision_endpoint`, `family_id_of_revision`, `create_family_member`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the sixth endpoint kind and why it is the strictest — a facet revision is a `record_revision` row whose owning envelope carries one of the eight authored-judgment kinds, so any other stored revision is refused as the missing endpoint it is. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new shared endpoint module. It records that the module owns a question rather than a table, that both checks run inside the caller's transaction before its first write (which is why a refused relation provably writes nothing), and the boundary between existence here and pair-duplication in the relation modules. Verification metadata remains empty until closeout stamps the code commit.
