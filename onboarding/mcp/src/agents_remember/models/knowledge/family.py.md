# mcp/src/agents_remember/models/knowledge/family.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/family.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

Family identity and the immutable family revision aggregate — the vocabulary half of the family graph.
A family is a stable subject whose revision carries an authored **joint guarantee**: a statement about
a set of invariant revisions that hold together. The guarantee is the family's own text and is never
assembled from its members; a member keeps its exact own obligation, and the two are separate authored
claims a reader must not derive from one another.

This module defines values, not rows. It performs no I/O, owns no table and raises no refusal: the
storage owner is `memory/knowledge/families.py`.

## Code Commentary

### Logic

- `FamilyDraft` is the identity a caller proposes — `family_id`, `display_label` and the label's own
  `Authorship` — with a non-blank label validator.
- `FamilyIdentity` adds `repository_id` and the expected `row_digest`, so a stored identity can be
  compared against what a caller remembered.
- `FamilyRevisionDraft` is the authored aggregate before sealing: `family_id`, `revision_id`,
  `display_version`, `joint_guarantee`, `predecessors`, `state_at_origin`, `acceptance_ref` and
  `provenance`. **The digest is absent by design**: the store recomputes and stores it, so a caller
  cannot present a payload whose seal belongs to different content.
- `FamilyRevision` adds `repository_id` and the `payload_digest`; `StoredFamilyRevision` carries the
  decoded `predecessors_sorted` set alongside the revision.
- Two authored-value rules are refused at construction rather than at the storage boundary:
  `require_consistent_acceptance` (an accepted origin needs a non-blank acceptance reference, and a
  proposed one must not carry one) and the self-predecessor rule (a revision must not declare itself
  as its own predecessor). `predecessors` additionally refuses a repeated identity.

### Conventions

- Separating `FamilyRevisionDraft` from `FamilyRevision` is what keeps the seal out of a caller's
  hands, exactly as `RevisionDraft`/`InvariantRevision` do on the invariant side.
- `StoredFamilyRevision._require_sorted_predecessors` asserts that the decoded set equals the sorted
  predecessor tuple, so a reader cannot present an unsorted or partial lineage view.
- Length bounds come from `base.py` (`LABEL_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`)
  rather than being re-spelled here, so both revision aggregates share one set of limits.

### Invariants And Boundaries

- **Immutability is structural, not advisory.** The `payload_digest` seals the whole authored payload
  *including the sorted predecessor set*, so a stored family revision identifies exactly one authored
  aggregate: changing the guarantee means authoring a separately identified successor, and an earlier
  membership citing the original still resolves the original text.
- **The guarantee is never derived from members.** Nothing in this vocabulary has a field a reader
  could fill from a member's obligation.
- **`unclassified`-style honesty applies here too.** A draft with an unknown role of its own is
  refused at construction rather than defaulted.
- **Boundary.** This module declares no operation, no table, no SQL and no refusal code; it must not
  grow a validation rule whose only enforcement point is storage, because both revision aggregates are
  validated where they are authored.
- **Not this module's job.** The relation vocabulary (`graph.py`), the payload-digest computation
  (`digest.py`) and the storage operations (`memory/knowledge/families.py`).

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
| The separation between the family guarantee and its members' obligations. | "a member keeps its exact own obligation, and the two are separate authored claims" | mcp/src/agents_remember/models/knowledge/family.py:4-6 |
| The identity draft and its stored, digest-carrying form. | `FamilyDraft`; `FamilyIdentity` | mcp/src/agents_remember/models/knowledge/family.py:35-48; mcp/src/agents_remember/models/knowledge/family.py:51-55 |
| The authored aggregate before sealing, with its digest deliberately absent. | `FamilyRevisionDraft` | mcp/src/agents_remember/models/knowledge/family.py:58-102 |
| The sealed revision and its stored read shape. | `FamilyRevision`; `StoredFamilyRevision` | mcp/src/agents_remember/models/knowledge/family.py:105-109; mcp/src/agents_remember/models/knowledge/family.py:112-123 |
| The shared accepted/proposed rule this aggregate applies at construction. | `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/base.py:40-56 |
| The payload this revision's digest seals, including the sorted predecessor set. | `canonical_family_revision_payload`; `family_revision_payload_digest` | mcp/src/agents_remember/models/knowledge/digest.py:71-92; mcp/src/agents_remember/models/knowledge/digest.py:93-96 |
| The row codec and seal-verifying decode that turn these values into stored rows. | `family_revision_row`; `decode_family_revision_row`; `sealed_family_revision_from_draft` | mcp/src/agents_remember/memory/knowledge/records.py:287-302; mcp/src/agents_remember/memory/knowledge/records.py:327-356; mcp/src/agents_remember/memory/knowledge/records.py:303-326 |
| The storage owner that writes and reads these values. | `create_family`; `create_family_revision`; `get_family_revision` | mcp/src/agents_remember/memory/knowledge/families.py:78-95; mcp/src/agents_remember/memory/knowledge/families.py:112-141; mcp/src/agents_remember/memory/knowledge/families.py:215-232 |
| The declared `family` and `family_revision` tables these values map onto. | `family`; `family_revision` | mcp/src/agents_remember/memory/knowledge/schema.py:173-183; mcp/src/agents_remember/memory/knowledge/schema.py:184-201 |
| The requirement this vocabulary's first delivered slice belongs to. | `KS-R02@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R02-v1-registered-family-and-realization-graph.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new family vocabulary. It records that the guarantee is the family's own text and never assembled from members, that a family revision is immutable by construction with its sorted predecessor set inside the seal, and that the accepted/proposed and self-predecessor rules are authored-value rules refused at construction rather than at the storage boundary. Verification metadata remains empty until closeout stamps the code commit.
