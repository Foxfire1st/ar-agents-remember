# mcp/src/agents_remember/models/knowledge/invariant.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/invariant.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash |  `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate |  2026-09-16T08:41:27+02:00|
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
identity; and the after-validator `_require_self_consistent_acceptance` enforces the self-predecessor rule and
delegates the accepted/proposed rule to `base.require_consistent_acceptance` — an `accepted` origin needs a
nonempty `acceptance_ref`, and a `proposed` origin must not carry one. The two `ValueError` messages are unchanged
by the extraction; the rule moved so the family revision aggregate applies one owner's version instead of a
second copy.

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
- **The accepted/proposed rule is shared, not owned here.** It lives in `base.py` because both revision
  aggregates apply it at construction; a third revision kind must call it rather than restate it.
- **No change to this model's behaviour was made by the graph leaf.** The extraction is behaviour-preserving, and
  the revision's field set, validators and digest participation are unchanged.

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
| The invariant identity shape, its nonblank display label and the row digest a label edit names. | `InvariantDraft`; `InvariantIdentity` | mcp/src/agents_remember/models/knowledge/invariant.py:33-48; mcp/src/agents_remember/models/knowledge/invariant.py:49-55 |
| The complete revision aggregate and its validators, including the self-predecessor rule. | `InvariantRevision`; `_require_self_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/invariant.py:56-115 |
| The shared accepted/proposed rule this validator now delegates to. | `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/base.py:40-56 |
| The read-back shape that pins the sorted predecessor set. | `StoredInvariantRevision` | mcp/src/agents_remember/models/knowledge/invariant.py:116-127 |
| The stored `invariant_revision` table this aggregate is written to, with its immutability triggers. | `invariant_revision`; `invariant_revision_no_update`; `invariant_revision_no_delete` | mcp/src/agents_remember/memory/knowledge/schema.py:136-156; mcp/src/agents_remember/memory/knowledge/schema.py:304-311 |
| The insert-only operation that seals and stores one aggregate, or refuses without any row. | `create_revision`; `_insert_revision` | mcp/src/agents_remember/memory/knowledge/store.py:224-259; mcp/src/agents_remember/memory/knowledge/store.py:296-344 |
| The requirement packet whose normative property this model encodes. | `KS-R01@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R01-v1-immutable-knowledge-identity.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): reviewed-no-impact body correction with a semantic note. The only change to this file is that its accepted/proposed validator now delegates to `base.require_consistent_acceptance` instead of inlining the same two checks, so the new family revision aggregate applies one owner's rule rather than a second copy. The field set, the validators, the two `ValueError` messages, the digest participation and the stored shape are unchanged; the card's validator description and reference ranges were corrected to match. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new invariant identity and revision aggregate. It records the display-label-versus-identity separation and the three self-consistency rules. Verification metadata remains empty until closeout stamps the code commit.
