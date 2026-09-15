# mcp/src/agents_remember/models/knowledge/invariant.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/invariant.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate |  2026-09-15T22:46:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

Invariant identity and the immutable invariant revision aggregate — the two identifiers that make a cited
statement impossible to rewrite in place, and the shape every stored revision is validated against.

## Code Commentary

### Logic

`InvariantDraft` is an invariant identity proposed for a namespace: `invariant_id` (UUID pattern),
`display_label` (bounded, nonblank after stripping) and `label_provenance`. `InvariantIdentity` extends the draft
with `repository_id` and a `row_digest`, which is the expected-row digest a label edit names.

`InvariantRevision` is the complete authored aggregate: `repository_id`, `invariant_id`, `revision_id` (all UUID
pattern), `display_version`, `statement`, `applicability`, `conditions`, `exclusions`, `state_at_origin`,
`acceptance_ref`, `provenance`, `predecessors` and `payload_digest` (SHA-256 pattern).

Validators: `_require_nonblank_authored_text` strips `display_version`/`statement`/`applicability` and refuses a
blank; `_require_nonblank_clauses` strips clause entries, refuses a blank and **preserves order**, because the
order is the author's and the digest covers it; `_require_unique_predecessors` refuses a repeated revision
identity; and the after-validator `_require_self_consistent_acceptance` enforces three coupled rules — an
`accepted` origin needs a nonempty `acceptance_ref`, a `proposed` origin must not carry one, and a revision must
not declare itself as its own predecessor.

`StoredInvariantRevision` wraps a `revision` with `predecessors_sorted` and an after-validator that refuses a
tuple which is not the sorted predecessor set.

### Conventions

`InvariantIdentity` is the stable subject; a revision is one authored statement of it. The friendly display
version belongs to the revision's **label**, not to its identity: two successors of one revision may both display
`v2`, and that is a supported state rather than an identity conflict.

### Invariants And Boundaries

- Immutability is by construction: the digest seals the whole semantic payload including the sorted predecessor
  set, so a stored revision identifies exactly one authored aggregate.
- `conditions`/`exclusions` are tuples whose empty value is a recorded "none", never a missing value.
- Proposal is distinct from acceptance: `state_at_origin` is authored data, and the store manufactures no
  acceptance and exposes no promotion operation.
- `InvariantRevision` is the vocabulary shape; the insert-only write path and its refusals belong to
  `memory/knowledge/store.py`, which is the only owner of that rule.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The invariant identity shape, its nonblank display label and the row digest a label edit names. | `InvariantDraft`; `InvariantIdentity` | mcp/src/agents_remember/models/knowledge/invariant.py:33-53 |
| The complete revision aggregate and its four validators, including the self-consistency rules. | `InvariantRevision`; `_require_self_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/invariant.py:56-117 |
| The read-back shape that pins the sorted predecessor set. | `StoredInvariantRevision` | mcp/src/agents_remember/models/knowledge/invariant.py:120-131 |
| The stored `invariant_revision` table this aggregate is written to, with its immutability triggers. | `invariant_revision`; `invariant_revision_no_update`; `invariant_revision_no_delete` | mcp/src/agents_remember/memory/knowledge/schema.py:135-155; mcp/src/agents_remember/memory/knowledge/schema.py:303-310 |
| The insert-only operation that seals and stores one aggregate, or refuses without any row. | `create_revision`; `_insert_revision` | mcp/src/agents_remember/memory/knowledge/store.py:212-241; mcp/src/agents_remember/memory/knowledge/store.py:279-326 |
| The requirement packet whose normative property this model encodes. | `KS-R01@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R01-v1-immutable-knowledge-identity.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new invariant identity and revision aggregate. It records the display-label-versus-identity separation and the three self-consistency rules. Verification metadata remains empty until closeout stamps the code commit.
