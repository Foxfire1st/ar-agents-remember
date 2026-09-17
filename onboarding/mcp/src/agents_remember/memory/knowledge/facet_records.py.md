# mcp/src/agents_remember/memory/knowledge/facet_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/facet_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890`|
| lastVerifiedCommitDate | 2026-09-18T01:58:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Row codecs between the facet vocabulary and generation 3's declared columns.** Every conversion in both
directions lives here — the four drafts, the encoders that produce a column tuple, the decoders that
produce a served value, the digest functions each row's identity is computed from, and the one-row
lookups the write path and the guards ask — so the column order, the canonical JSON text form of a typed
column, and the digest recomputation have exactly one owner per table.

The module exists because a facet spans six tables at once. A facet record is an envelope row plus a
revision row; an attachment is a row whose *endpoint* is spread across four nullable columns; an
explanation is an identity row whose subject is spread across four more; and each of those has a digest
some guard or expectation has to be able to name. Scattering the conversions across the write path, the
read path and the batch checks would give the same row three definitions, and the first one to drift would
be invisible until a removal refused a row that had not changed.

## Code Commentary

### Logic

- **Two seals are recomputed on the way *out* rather than trusted.** `decode_facet_revision_row`
  re-derives a facet revision's `content_digest` from the stored payload, and
  `decode_explanation_revision_row` re-derives an explanation revision's `payload_digest` from the stored
  body. A mismatch raises `KnowledgeStorageError` and the message tells the caller what to do with the
  store ("treat the store as damaged and recover the revision from an intact snapshot"). The rule is the
  shipped one: a row whose text was rewritten behind its identity must not be served as the revision that
  identity names.
- **The mutable-field digests are the other half of the same idea.** A facet attachment and an explanation
  identity row are not sealed revisions — one may be explicitly removed, the other carries the recorded
  designation — so an operation that names one of them by digest computes that digest from the row as it
  stands. `attachment_row_digest` and `explanation_row_digest` are what those guards compare against.
- **The identity inputs are the stored identity's own fields.** The record-envelope digest covers the
  `record_schema` the kind must store and the provenance the admission supplied; the revision seal covers
  the payload and the exact predecessor and excludes only itself; the attachment digest covers the endpoint
  kind **and** the endpoint identity (`endpoint_identity`) so the digest is a fact about the endpoint and
  not about which column happens to hold it; the supersession digest covers both endpoint revisions; an
  explanation row's digest covers the subject kind, the subject's identity revision **and** the recorded
  designation, so every designation names the row it expects including the designation it replaces; and an
  explanation revision's seal covers the body and the exact predecessor.
- **`facet_record_schema_of` is the one place a kind is resolved to its schema, and it refuses.** An
  undecoded kind raises `KnowledgeStorageError` rather than returning a default, so a row carrying a kind
  this build does not declare is a damaged store rather than a facet with a missing schema. The same shape
  is used by `decode_attachment_endpoint` (a kind outside the four raises, and a kind whose column is null
  raises because the table's own constraint was bypassed) and by `decode_explanation_subject` (same two
  refusals for the two subject kinds, with `_required_subject_part` naming which half of the key was
  missing).
- **Encoding fills every column explicitly.** `attachment_endpoint_columns` and `subject_columns` build all
  four columns and set the three the kind does not declare to `None`, so a row's shape never depends on a
  default, and the `CHECK` in the DDL is satisfied by construction rather than by omission.
- **The stored-value readers answer the same question the read projection exposes.** `facet_record_digest`,
  `record_revision_content_digest`, `attachment_endpoint_digest`, `supersession_digest`,
  `explanation_record_digest` and `explanation_revision_payload_digest` each return the digest the read
  path serves for that row, or `None` when the row is not stored — so a caller carries an expectation
  straight from a read instead of deriving a second identity scheme.
- **Two values are versioned rather than inferred.** `RECORD_REVISION_PAYLOAD_VERSION` and
  `EXPLANATION_REVISION_PAYLOAD_VERSION` are inside their seals, so a change to the sealed field set is a
  different identity computation recorded in a constant rather than deduced from which fields are present.

### Conventions

- **The drafts are frozen dataclasses, not column tuples.** `FacetEnvelopeDraft`, `RecordRevisionDraft` and
  `AttachmentDraft` carry one authored row each as a value, which is why a digest function and its row
  encoder take the same object rather than six positional arguments that could be passed in the wrong
  order.
- **Decoders take a row sequence and return a model**, and each decoder computes the row's digest from the
  values it just decoded rather than reading a stored digest column — except where the column *is* the
  seal (`record_revision.content_digest`, `explanation_revision.payload_digest`), which is verified against
  the recomputation instead.
- **The one-row lookups are declared beside the readers that use them** (`ATTACHMENT_BY_ID`,
  `RECORD_BY_ID`, `REVISION_BY_ID`, `SUPERSESSION_BY_SUPERSEDING`, `EXPLANATION_BY_ID`,
  `EXPLANATION_REVISION_BY_ID`), each naming one canonical table and its own key, so a lookup is not
  spelled twice with two parameter orders.
- **The module writes nothing.** It performs no insert, no update and no delete; every function here is a
  conversion or a read, and the write path is `facets.py`.

### Invariants And Boundaries

- **A digest is computed the same way wherever it is needed.** The removal guard, the designation guard,
  the batch's expectation machinery and the read projection all consume these functions, so "the row I
  expected" means one thing in this package.
- **A rewritten row is a damaged store, not a served value.** Every seal mismatch raises rather than
  returning a value the caller could write back, and the read path converts that into a typed
  `snapshot_unavailable` refusal rather than serving content that is not the identity it names.
- **Boundary.** This module does not own the tables' declarations (`schema_v3.py` does), does not decide
  whether a write is admissible (`record_envelope.py` and `facets.py` do), does not decide which generation
  a dataset is (`schema_generations.py` does), and does not shape a page (`models/knowledge/facet_read.py`
  does). It converts rows and computes digests.
- **Naming detail worth stating, because two modules share a name.** `EXPLANATION_BY_ID` here and
  `EXPLANATION_BY_ID` in `facets.py` are two separately declared statements with the same text and the
  same purpose; neither imports the other, and each is used only inside its own module. They are local
  constants rather than one shared declaration, which is a deliberate non-coupling rather than a second
  definition of a rule.
- **Known asymmetry, recorded rather than implied:** the readers return `None` for a row that is not
  stored, so a caller that does not check gets `None` rather than a refusal. The write path is the caller
  that turns that into a typed refusal (`missing_expected_row`), and the read path never uses these
  readers.

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
| **The recomputed-on-the-way-out seals and the damaged-store rule they enforce.** | `decode_facet_revision_row`; `decode_explanation_revision_row` | mcp/src/agents_remember/memory/knowledge/facet_records.py:227-271; mcp/src/agents_remember/memory/knowledge/facet_records.py:630-655 |
| **The two mutable-field digests the guards compare against.** | `attachment_row_digest`; `explanation_row_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:356-371; mcp/src/agents_remember/memory/knowledge/facet_records.py:534-558 |
| The versioned payload constants that make a change to the sealed field set a recorded decision. | `RECORD_REVISION_PAYLOAD_VERSION`; `EXPLANATION_REVISION_PAYLOAD_VERSION` | mcp/src/agents_remember/memory/knowledge/facet_records.py:67-68 |
| The three drafts that make one authored row a value rather than six positional arguments. | `FacetEnvelopeDraft`; `RecordRevisionDraft`; `AttachmentDraft` | mcp/src/agents_remember/memory/knowledge/facet_records.py:74-101 |
| The record-envelope encoder and the schema resolution that refuses an undeclared kind. | `facet_record_row`; `facet_record_schema_of` | mcp/src/agents_remember/memory/knowledge/facet_records.py:104-130 |
| The revision seal that excludes only itself, and the digest a served record row carries. | `record_revision_digest`; `facet_record_row_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:209-224; mcp/src/agents_remember/memory/knowledge/facet_records.py:133-154 |
| **The four endpoint columns filled explicitly, and the decoder's two refusals for an unknown kind and a bypassed constraint.** | `attachment_endpoint_columns`; `decode_attachment_endpoint` | mcp/src/agents_remember/memory/knowledge/facet_records.py:277-301; mcp/src/agents_remember/memory/knowledge/facet_records.py:304-337 |
| The supersession edge's encoder, digest and decoder. | `supersession_row_digest`; `decode_supersession_row` | mcp/src/agents_remember/memory/knowledge/facet_records.py:410-426; mcp/src/agents_remember/memory/knowledge/facet_records.py:429-441 |
| **The explanation's checked subject group, its decoder's refusals, and the designation inside the row digest.** | `subject_columns`; `decode_explanation_subject`; `explanation_row_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:447-462; mcp/src/agents_remember/memory/knowledge/facet_records.py:465-501; mcp/src/agents_remember/memory/knowledge/facet_records.py:534-558 |
| The explanation revision's seal and the encoder that stores it. | `explanation_revision_digest`; `explanation_revision_row` | mcp/src/agents_remember/memory/knowledge/facet_records.py:611-627; mcp/src/agents_remember/memory/knowledge/facet_records.py:588-608 |
| **The six stored-value readers a caller's expectation comes straight from a read through.** | `attachment_endpoint_digest`; `record_revision_content_digest`; `explanation_record_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:680-688; mcp/src/agents_remember/memory/knowledge/facet_records.py:698-702; mcp/src/agents_remember/memory/knowledge/facet_records.py:716-720 |
| The write path that owns every statement this module converts rows for. | `apply_remove_facet_attachment`; `apply_designate_explanation` | mcp/src/agents_remember/memory/knowledge/facets.py:419-457; mcp/src/agents_remember/memory/knowledge/facets.py:589-639 |
| **The cases that hold the removal guard, the recomputed seal and the damaged-store refusal.** | "test_removing_an_attachment_names_its_row_and_deletes_that_row_only"; "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" | mcp/tests/test_knowledge_facets.py:455-491; mcp/tests/test_knowledge_facets.py:1037-1141 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the facet row codecs. It records the two **recomputed-on-the-way-out** seals and the damaged-store rule they enforce, the two **mutable-field digests** the removal and designation guards compare against, what each digest covers (the endpoint *identity* rather than the column that holds it; the subject identity **and** the recorded designation; the payload and exact predecessor), the versioned payload constants, the explicit filling of all four endpoint and subject columns so the DDL's `CHECK` is satisfied by construction, the six stored-value readers that let a caller carry an expectation straight from a read, and the one-row lookups declared beside their readers. It records the shared local constant name `EXPLANATION_BY_ID` as a deliberate non-coupling rather than a second definition of a rule, and the asymmetry that these readers return `None` for an absent row while the write path is what turns that into a typed refusal. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
