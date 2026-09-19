# mcp/src/agents_remember/models/knowledge/facet_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/facet_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate | 2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The facet-specific selection's declared contract: seeds, stored values, items, counts, page and result.**
`KS-R07@v1` owns the recorded-scope selection over paths, invariant revisions, family revisions,
memberships and realizations, and its declared set, counts, cursor contract and finite family frontier are
unchanged by this leaf. Facets are reached by this **separate** selection instead: its own seed kinds, its
own item kinds, its own counts and its own declared policy name. Nothing here is reachable from a shipped
seed, and a shipped seed's page is therefore byte-identical to what it was before this leaf — not by a
guard, but because no code path is shared.

Two decisions are recorded here and both are the reason the module exists:

- **The selection is complete or it refuses.** One seed selects one bounded aggregate, and a selection that
  reaches `FACET_SELECTION_ITEM_LIMIT` refuses with the shipped `selection_incomplete` rather than serving a
  page that reads as the whole set. There is no cursor: a continuation contract is a second declared policy
  surface, and this selection does not need one to be honest about what it selected.
- **Nothing here derives currency.** Every retained facet revision is served as its own item with its exact
  revision identity, its provenance and its stored lifecycle, in an order fixed by stable identifiers. The
  only statement about which explanation revision matters is the explanation record's own
  `current_revision_id`, which is a *recorded designation*: it is reported verbatim, never computed, and no
  field here could be read as "newest".

## Code Commentary

### Logic

- **Six stored-value models, one per shape a canonical row serves.** `FacetRecord` is the envelope (its kind,
  schema, lifecycle, authority home, optional governing route and provenance, plus the `row_digest` the read
  exposes); `FacetRevision` is one sealed revision with its payload exactly as validated and stored and the
  `content_digest` of the revision aggregate — explicitly **not** a digest on the record, which mints no
  identity of its own; `FacetAttachment` names the exact facet revision and the exact typed endpoint;
  `DecisionSupersession` is one recorded edge and asserts nothing else; `ExplanationRecord` carries the
  exact subject and the stored designation, with `None` as a fact ("no designation recorded") rather than a
  fallback to the newest revision; and `ExplanationRevision` is one append-only body with its exact
  predecessor and its `payload_digest`.
- **Two seed kinds, because the selection answers two questions**: `FacetRecordSeed` (what is this facet
  record made of, addressed by its exact record identity) and `ExplanationSubjectSeed` (which explanations
  explain this exact statement revision). `FacetReadSeed` is their discriminated union, and
  `facet_seed_digest` seals one seed the way the shipped read seals a selector.
- **Six item kinds, one model each**, so an item carries exactly the fields its kind has and a page cannot
  grow an optional bag that means different things per kind. `FacetReadItem` is their discriminated union
  and `FacetReadItemKind` the same six spellings.
- **The declared order is a fixed order over item kinds and then over stable identifiers.**
  `_FACET_KIND_ORDER` numbers the six kinds and `facet_item_sort_key` returns
  `(kind order, first identifier, second identifier)`, with `_facet_item_identifiers` narrowing per kind
  (a record orders by its own id twice, a revision by record then revision, an attachment by facet revision
  then attachment id, an edge by superseding then superseded, an explanation by its id twice). `facet_item_id`
  renders the identity an item is addressed by inside its selection as `kind:first/second`.
- **The counts are the selection's own arithmetic.** `FacetReadCounts` carries one non-negative integer per
  item kind and an `items_total` property that adds them; there is no `has_more` and no remaining count,
  because a selection that does not fit whole is refused rather than paged.
- **The page's completeness is not a flag a builder can set to `False`.** `FacetReadPage.enumeration_complete`
  is `Literal[True] = True`, and its validator refuses a page whose counts disagree with the items it
  carries and a page whose items are not in the declared order — "an order derived from insertion time or an
  authored label is not this selection's".
- **The result is a page or a refusal and its validator refuses both or neither.** `FacetReadResult` declares
  `state: Literal["page", "refused"]`, the operation literal `read_facet_scope`, the repository, the
  snapshot, the context digest, the seed and its digest, the manifest digest, the policy version, the page
  and the refusal; a refused result must carry its refusal and no page, and a served one must carry its page.

### Conventions

- **Every value model is frozen and extra-forbidden under the shipped vocabulary base**, so a page cannot be
  extended with a field that carries a verdict, a confidence or a severity: there is nowhere for one to go.
- **The policy name is its own.** `FACET_SELECTION_POLICY_VERSION` is `authored-judgment-facets/v1` rather
  than the shipped recorded-scope name, because a policy name is a claim about which selection produced a
  page and two selections that select different things are two policies whatever module they live in.
- **The execution bound is a bound on enumeration, not a page size**, and both the bound and the reason
  (`FACET_ITEM_LIMIT_REASON`) are declared beside each other so a refusal can name the bound it reached.
- **Stored values carry the digests the read operations expose**, so a caller carries an expectation
  straight from a read instead of deriving a second identity scheme.

### Invariants And Boundaries

- **The shipped selection does not move.** This module declares no seed, no item, no count and no policy
  name that the recorded-scope read can reach, and `KNOWLEDGE_READ_POLICY_VERSION`'s declared set and
  constants are untouched.
- **No field here can carry a verdict, a ranking, a currency or an endorsement.** That absence is how the
  requirement's forbidden overreach is enforced structurally rather than by discipline.
- **Boundary.** This module declares shapes and nothing else: it executes no selection
  (`memory/knowledge/facet_read.py` does), verifies no snapshot (`application/knowledge_facets.py` does),
  and declares neither the facet vocabulary nor the attachment endpoints it reuses from
  `models/knowledge/facet.py`.
- **One deliberate non-change worth recording:** this vocabulary is **not** re-exported from
  `models/knowledge/__init__.py` — a consumer names `agents_remember.models.knowledge.facet_read`, exactly
  as the portable, merge and comparison vocabularies are named by their own modules.

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
| **The declared policy name, the enumeration bound and its reason — this selection's own policy rather than the shipped one.** | `FACET_SELECTION_POLICY_VERSION`; `FACET_SELECTION_ITEM_LIMIT`; `FACET_ITEM_LIMIT_REASON` | mcp/src/agents_remember/models/knowledge/facet_read.py:56-63 |
| **The six stored-value models, including the absent designation reported as absent.** | `FacetRecord`; `FacetRevision`; `FacetAttachment`; `DecisionSupersession`; `ExplanationRecord`; `ExplanationRevision` | mcp/src/agents_remember/models/knowledge/facet_read.py:71-160 |
| The two seed kinds, their union and the seed digest. | `FacetRecordSeed`; `ExplanationSubjectSeed`; `FacetReadSeed`; `facet_seed_digest` | mcp/src/agents_remember/models/knowledge/facet_read.py:168-191 |
| The six item kinds, one model each, and the union they form. | `FacetRecordItem`; `FacetRevisionItem`; `FacetAttachmentItem`; `DecisionSupersessionItem`; `ExplanationItem`; `ExplanationRevisionItem`; `FacetReadItem` | mcp/src/agents_remember/models/knowledge/facet_read.py:199-258 |
| **The declared order over item kinds and stable identifiers, and the identity an item is addressed by.** | `facet_item_sort_key`; `facet_item_id` | mcp/src/agents_remember/models/knowledge/facet_read.py:273-299 |
| **The counts that are the selection's own arithmetic, with no `has_more` and no remaining count.** | `FacetReadCounts` | mcp/src/agents_remember/models/knowledge/facet_read.py:302-329 |
| **The page whose completeness is not a settable flag, and whose validator refuses a count/order disagreement.** | `FacetReadPage` | mcp/src/agents_remember/models/knowledge/facet_read.py:332-354 |
| The request and the page-or-refusal result, with the validator that keeps the two exclusive. | `FacetReadRequest`; `FacetReadResult` | mcp/src/agents_remember/models/knowledge/facet_read.py:357-390 |
| The attachment endpoint and explanation subject shapes this module reuses rather than redeclaring. | `AttachmentEndpoint`; `ExplanationSubject` | mcp/src/agents_remember/models/knowledge/facet.py:288-294; mcp/src/agents_remember/models/knowledge/facet.py:365-368 |
| The shipped recorded-scope policy this selection deliberately does not share. | `KNOWLEDGE_READ_POLICY_VERSION` | mcp/src/agents_remember/models/knowledge/read.py:87-87 |
| The frozen, strict, extra-forbidding base that makes every page a value. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The selection that executes these declarations and the application seam that serves them. | "def select_facet_scope("; `read_facet_scope` | mcp/src/agents_remember/memory/knowledge/facet_read.py:109-129; mcp/src/agents_remember/application/knowledge_facets.py:71-121 |
| **The cases that hold the declared order, the counts' arithmetic, the empty-but-real page and the own-policy result.** | "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact"; "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" | mcp/tests/test_knowledge_facets.py:1104-1119; mcp/tests/test_knowledge_facets.py:1053-1068; mcp/tests/test_knowledge_facets.py:1119-1119; mcp/tests/test_knowledge_facets.py:1239-1246; mcp/tests/test_knowledge_facets.py:1187-1194; mcp/tests/test_knowledge_facets.py:1266-1266; mcp/tests/test_knowledge_facets.py:1214-1214 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the facet selection's declared vocabulary. It records the **two decisions the module exists for** (complete-or-refused with no cursor, and nothing deriving currency with the stored designation reported verbatim), the six stored-value models with the absent designation as a fact rather than a fallback, the two seed kinds and six item kinds as closed discriminated unions, the declared order over item kinds and stable identifiers, the counts as the selection's own arithmetic with no `has_more`, the page whose completeness is `Literal[True]` and whose validator refuses a count or order disagreement, the page-or-refusal result validator, the own policy name rather than the shipped one, and the deliberate non-change that the facade does not re-export this vocabulary. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
