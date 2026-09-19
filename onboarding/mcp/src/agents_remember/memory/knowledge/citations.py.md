# mcp/src/agents_remember/memory/knowledge/citations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/citations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The authored citation-binding write path: the binding's own rows, and every refusal between them.
One authored act lives here — record that this citation key, in this exact revision of this prose
document, denotes this knowledge record at this locator.

## Code Commentary

### Logic

The module carries the shipped pair of entry points, exactly as the facet and detection writes do:
`author_citation_binding` owns the candidate lock and one `BEGIN IMMEDIATE` transaction and returns a
typed `CitationBindingResult`; `apply_citation_binding` writes inside a caller's open transaction and
raises `KnowledgeRefused`, so a batch path rolls the whole batch back. That split is what makes "a
refused binding write leaves the dataset exactly as it was" a property of the transaction boundary
rather than a promise about statement order. `_apply_binding_write` and `_write_binding_rows` write the
envelope row, the sealed revision and the binding row together, so a binding whose sealed revision is
missing cannot exist.

`_validated_payload` routes the payload through `validate_record_payload` at the one envelope seam, so
an unregistered kind, a schema inadmissible for its kind, a payload that omits a required fact and a
payload carrying an undeclared field are all the same shipped `invalid_payload` refusal, raised before
any row exists.

`require_target_reference` is the reference check: the target record must be stored in this namespace,
a named revision must be a revision *of that record*, and the record's **recorded kind must be the
kind the reference declares** — a wrong-kind reference is refused at this boundary. `_require_governing_route`
refuses a named route that is not authored here, while `None` is the explicit **ungoverned** state.
`require_binding_generation` is the gate: a dataset whose recorded generation predates
`REQUIRED_BINDING_GENERATION` is refused with the observed generation as a fact, never migrated,
widened or written through.

`binding_row` derives the canonical column tuple, `local_key_text` renders the recorded key (or
`None` for a form this increment does not read), `binding_row_digest` is the row's own digest over its
*recorded* columns, and `load_binding_ids` is the ordered identity listing the read path uses.

### Invariants And Boundaries

- **The binding is authored, not inferred.** Nothing here derives a target from a path prefix, a
  folder name, a symbol string, a display label or a prose mention, and nothing searches for a nearest
  plausible record. A wrong-kind reference is a *write* refusal, which is why the read path's
  `target_kind_mismatch` can only arise from a store changed after the write.
- **Scope is never inferred.** `governing_route_id` is a parameter and is never derived from the
  document path, the target's path, the key's written source or the repository root.
- **Every reference is checked before the row it belongs to**, so a dangling reference is refused
  rather than stored and the read path never has to guess what an absent reference meant.
- **A rewritten key is a different key**, which is why the key is recorded as form plus exact text and
  the `UNIQUE` constraint makes "one owner revision records one key once" a table fact.
- This module writes no Markdown, re-parses no corpus and imports nothing from
  `memory_quality/style/citations/**`: the one citation authority stays where it is.

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
| **The two entry points and the transaction split that makes a refused write leave nothing behind.** | `author_citation_binding`; `apply_citation_binding` | mcp/src/agents_remember/memory/knowledge/citations.py:126-144; mcp/src/agents_remember/memory/knowledge/citations.py:146-160 |
| **The one payload decision point, and the reference check that refuses a wrong-kind or absent target before any row exists.** | `_validated_payload`; `require_target_reference`; `_require_target_revision` | mcp/src/agents_remember/memory/knowledge/citations.py:162-177; mcp/src/agents_remember/memory/knowledge/citations.py:199-242; mcp/src/agents_remember/memory/knowledge/citations.py:244-271 |
| **The governing-route check: a named route that is not authored here is refused, and `None` is the explicit ungoverned state.** | `_require_governing_route` | mcp/src/agents_remember/memory/knowledge/citations.py:273-291 |
| **The generation gate: a dataset that predates the binding table is refused with the observed generation as a fact.** | `require_binding_generation`; `REQUIRED_BINDING_GENERATION` | mcp/src/agents_remember/memory/knowledge/citations.py:293-314; mcp/src/agents_remember/memory/knowledge/citations.py:88-88 |
| The row codec, the canonical key text and the row digest over the recorded columns. | `binding_row`; `local_key_text`; `binding_row_digest` | mcp/src/agents_remember/memory/knowledge/citations.py:382-405; mcp/src/agents_remember/memory/knowledge/citations.py:407-417; mcp/src/agents_remember/memory/knowledge/citations.py:443-469 |
| The ordered binding identities the read path enumerates. | `load_binding_ids` | mcp/src/agents_remember/memory/knowledge/citations.py:471-482 |
| The one envelope seam this write path validates through, and the registry its decision reads. | `validate_record_payload`; `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:236-280; mcp/src/agents_remember/memory/knowledge/record_envelope.py:132-178 |
| The revision-row helper the sealed revision is written with, and the draft it takes. | `RecordRevisionDraft`; `record_revision_row`; `record_revision_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:86-118; mcp/src/agents_remember/memory/knowledge/facet_records.py:193-207; mcp/src/agents_remember/memory/knowledge/facet_records.py:209-232 |
| The two operation members this write path and its read partner register. | `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-49 |
| **The boundary cases that measure the write refusals: a wrong-kind target, a target the namespace does not hold, and a dangling governing route beside an accepted ungoverned binding.** | `test_a_wrong_kind_target_is_refused_at_the_write_boundary`; `test_a_target_record_the_namespace_does_not_hold_is_refused`; `test_a_dangling_governing_route_is_refused_and_an_ungoverned_binding_is_not` | mcp/tests/test_knowledge_citation_boundaries.py:401-431; mcp/tests/test_knowledge_citation_boundaries.py:434-456; mcp/tests/test_knowledge_citation_boundaries.py:459-513 |
| The boundary case that proves the store itself refuses two bindings claiming one key in one owner revision. | `test_two_bindings_claiming_one_key_in_one_owner_revision_are_refused_by_the_store` | mcp/tests/test_knowledge_citation_boundaries.py:516-543 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A binding records a fact about one memory
document and one knowledge record in the same namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_a_wrong_kind_target_is_refused_at_the_write_boundary`; `test_a_target_record_the_namespace_does_not_hold_is_refused`; `test_a_dangling_governing_route_is_refused_and_an_ungoverned_binding_is_not` repointed to mcp/tests/test_knowledge_citation_boundaries.py:401-431; mcp/tests/test_knowledge_citation_boundaries.py:434-456; mcp/tests/test_knowledge_citation_boundaries.py:459-513. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_two_bindings_claiming_one_key_in_one_owner_revision_are_refused_by_the_store` repointed to mcp/tests/test_knowledge_citation_boundaries.py:516-543. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the authored binding write path. It records the four rules that shape it, because each is a refusal a future leaf must not relax. **The payload seam is the only payload decision point**, so an unregistered kind, an inadmissible schema, a missing fact and an undeclared field are one shipped `invalid_payload` raised before any row exists. **The binding is authored, not inferred** — a wrong-kind reference is a *write* refusal, which is what makes the read path's `target_kind_mismatch` reachable only from a store changed after the write. **Every reference is checked before the row it belongs to**, so a dangling target or governing route is refused rather than stored. And **scope is never inferred**: `None` is the explicit ungoverned state and is never defaulted to a route that happens to exist. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
