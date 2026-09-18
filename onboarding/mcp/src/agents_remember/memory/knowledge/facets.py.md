# mcp/src/agents_remember/memory/knowledge/facets.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/facets.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The authored facet write path: two entry points per write and the refusals between them.** Six authored
acts live here — record a facet, attach it to an exact endpoint, remove one attachment, author an
explanation, edit an explanation, and record a designation — and each has the shipped pair of entry
points, exactly as the label edits do:

- the **operation** (`add_facet`, `attach_facet`, `remove_facet_attachment`, `author_explanation`,
  `add_explanation_revision`, `designate_explanation`), which owns the candidate lock and one `BEGIN
  IMMEDIATE` transaction and returns a typed `FacetWriteResult`;
- the **in-transaction step** (`apply_facet_command` dispatching through `_STEPS` to the six `apply_*`
  functions), which writes inside a caller's open transaction and raises `KnowledgeRefused` so the batch
  path rolls the whole batch back.

That split is what makes "a refused facet write leaves the dataset exactly as it was" a property of the
transaction boundary rather than a promise about statement order: every refusal is raised inside the
transaction, and the reference checks run **before** the row they guard, so the order of statements is not
what protects the store.

## Code Commentary

### Logic

Four rules shape the write path:

- **The payload seam is the only payload decision point.** `apply_add_facet` calls
  `record_envelope.validate_facet_payload` and raises `KnowledgeRefused` when it returns a refusal, so an
  unknown or ninth subtype, a payload that omits a required meaning, an undeclared field and a payload
  that arrives carrying its own `actor_ref` are all the same shipped `invalid_payload` refusal, raised
  before any row exists. The validated model is what gets stored (`model_dump(mode="json")`), rather than
  the caller's mapping.
- **Provenance comes from the admission.** The `authorship` envelope is a parameter of every step and of
  `FacetWriteRequest`, never a field of a command, so no part of a submitted payload can become the
  record's author, authorization or instant. `_authority_home` reads the namespace's declared authority
  home from the store for the same reason: the envelope's `authority_home` is a fact about the destination
  the admission resolved, not something a caller authors.
- **A facet is authored as proposed origin data.** `require_proposed_origin` is a shared step rather than a
  batch-only check, because both entry points owe the same refusal: the batch refuses it in its
  preconditions before any row exists, and the standalone operation refuses it inside its transaction. The
  code is the shipped `promotion_not_supported`, and the accepted-origin consistency rule is inherited
  from the vocabulary base rather than re-implemented here.
- **Every reference is checked before the row it belongs to.** An attachment's facet revision must be
  stored as a facet revision (`_require_facet_revision`), its typed endpoint must exist
  (`endpoints.require_attachment_endpoint`), an explanation's subject must be the exact stored statement
  revision of its own kind (`require_explanation_subject`), a supersession must name a stored **decision**
  revision (`require_decision_revision`) and its graph must be acyclic
  (`require_acyclic_supersessions`), a designation must name a revision of **this** explanation, and a
  named governing route must exist (`routes.route_exists`). A dangling reference is refused rather than
  stored, and no reference is ever inferred from a name, a path or prose.

Three further behaviours are worth naming:

- **`apply_add_facet` writes the envelope and its first sealed revision, then the supersession edge when
  the command carries one**, reporting the rows it touched as `FacetWriteIdentity` values whose digests the
  store computed. `_record_supersession` inserts the edge and *then* walks the graph, so a cycle refuses
  the operation and the transaction rolls the whole write back rather than leaving a self-referential edge
  behind.
- **Removal and designation are guarded by the row's own digest.** `apply_remove_facet_attachment` refuses
  a missing row with `missing_expected_row` and a digest mismatch with `stale_precondition`, then deletes
  that attachment row and nothing else; `apply_designate_explanation` refuses a mismatch the same way and
  validates the named revision against the explanation's own revision set before writing. Both report the
  removal/write as a receipt entry, and `_written` constructs the entry with `model_construct` because
  every field was computed by the store rather than parsed from input.
- **The standalone driver refuses an operation mismatch.** `_command_matches_operation` compares the
  command's own kind against the operation the caller named and returns `invalid_reference` with the
  expected/observed pair, so a write is never reported under an operation that did not perform it; the
  driver dispatches on the command's own kind through `_STEPS` and `_OPERATION_OF_KIND`, so this is a
  naming check rather than a second dispatch.
- **The generation gate is read from the open store, not from the build.**
  `require_facet_generation` compares `store.generation.user_version` against `REQUIRED_FACET_GENERATION`
  (`GENERATION_3`) and returns `unsupported_schema` with both numbers as facts. Nothing is migrated,
  widened or written through, and the dataset is still served as what it is.

### Conventions

- **`pending` is the batch's declared identity set, and the standalone path passes the empty set.** A
  reference that resolves against `pending` is left to the batch's own completed-graph preconditions, which
  is the same split the shipped lineage checks use: the preconditions decide what the batch *declares*, and
  this step decides what is already stored. A reference that is not pending must be stored.
- **Each step returns the rows it really wrote.** A step whose requested effect was already stored writes
  nothing and reports nothing, and `_apply_facet_command` is where that empty tuple becomes a
  `FacetWriteResult`; the batch path receives the tuple itself.
- **Refusals are built through the shipped factories** — `scope_refusal`, `missing_expected_row_refusal`,
  `missing_relation_endpoint_refusal`, `stale_expected_row_refusal`,
  `facet_promotion_not_supported_refusal`, `facet_supersession_cycle_refusal`, `explanation_revision_refusal`
  and `generation_mismatch_refusal` — so this module contributes facts and a next action rather than a
  bespoke error shape.
- **The dispatch table is declared after the steps it names**, so the two cannot disagree about what a
  command kind maps to, and two adapters (`_step_taking_authorship`, `_step_ignoring_authorship`) give the
  table one uniform signature for removal and designation, which need neither the envelope nor the pending
  set.
- **Every statement is a module constant** (`_RECORD_INSERT`, `_REVISION_INSERT`, `_SUPERSESSION_INSERT`,
  `_ATTACHMENT_INSERT`, `_EXPLANATION_INSERT`, `_EXPLANATION_REVISION_INSERT`, `_ATTACHMENT_DELETE`,
  `_EXPLANATION_DESIGNATE`, plus the three lookups), so a statement is not spelled twice.

### Invariants And Boundaries

- **Refusal means nothing was written.** Every refusal is raised inside the caller's transaction; the batch
  path converts it into a rolled-back batch, and the standalone operation converts it into a `refused`
  receipt carrying the refusal and no written row.
- **An explanation edit is append-only in practice, not only in intent.** The predecessor must already be
  stored **for this** explanation, so a revision can only name a revision that exists: two revisions
  authored in one transaction cannot name each other and no predecessor cycle is constructible.
- **The supersession graph is the shared rule, not a second one.** `require_acyclic_supersessions` builds
  the graph from `lineage.supersession_edges` and asks `lineage.cycle_vertices`, so the third lineage graph
  is judged by the same strongly-connected-component rule as the two predecessor graphs.
- **Boundary.** This module does not declare the tables (`schema_v3.py` does), does not convert rows
  (`facet_records.py` does), does not decide payload admissibility (`record_envelope.py` does), does not
  validate an endpoint's kind compatibility (`schema_v3.py`'s `CHECK` does), and does not select anything
  (`facet_read.py` and `application/knowledge_facets.py` do).
- **Recorded detail, measured rather than assumed.** `_apply_facet_command` constructs a
  `FacetWriteResult` with `state="no_change"` for the empty-write case, while `models/knowledge/facet.py`'s
  receipt declares `state: Literal["applied", "refused"]`. The two statements do not agree, and the
  mismatch is reachable only through an empty write, which the digest-guarded designation (`stale_precondition`)
  and the pre-write reference checks make unreachable on every path the leaf's cases drive. It is recorded
  here rather than softened: a future leaf that makes an empty write reachable meets a `ValidationError`,
  not a third state.
- **Not admissible, recorded so it is not re-proposed:** a promotion or acceptance operation for a facet.
  `promotion_not_supported` is the shipped answer, and the lifecycle stays data.

### Todos

- The `state="no_change"` path above is a real divergence between the operation and its receipt model, and
  it has no producer today. Deciding it — either by making the receipt declare the third state or by
  making the empty write impossible by construction — belongs to a later leaf; this card records it so the
  next reader does not have to rediscover it.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The six standalone operations, each naming the act it performs so a refusal is reported under the operation the caller asked for.** | `add_facet`; `attach_facet`; `remove_facet_attachment`; `author_explanation`; `add_explanation_revision`; `designate_explanation` | mcp/src/agents_remember/memory/knowledge/facets.py:153-192 |
| **The one dispatch the batch path and the standalone driver share, and the alias that documents the split.** | `apply_facet_command`; `PendingIdentities` | mcp/src/agents_remember/memory/knowledge/facets.py:201-215; mcp/src/agents_remember/memory/knowledge/facets.py:667-670 |
| **The payload seam as the only payload decision point, and the envelope-plus-first-revision write.** | `apply_add_facet`; "def validate_facet_payload(" | mcp/src/agents_remember/memory/knowledge/facets.py:218-272; mcp/src/agents_remember/memory/knowledge/record_envelope.py:215-215; mcp/src/agents_remember/memory/knowledge/record_envelope.py:216-249; mcp/src/agents_remember/memory/knowledge/record_envelope.py:249-249; mcp/src/agents_remember/memory/knowledge/record_envelope.py:276-283 |
| **The payload seam as the only payload decision point, and the envelope-plus-first-revision write.** | `apply_add_facet`; "def validate_facet_payload(" | mcp/src/agents_remember/memory/knowledge/facets.py:218-272; mcp/src/agents_remember/memory/knowledge/record_envelope.py:283-283 |
| **Proposed origin only, refused at both entry points with the shipped code.** | `require_proposed_origin` | mcp/src/agents_remember/memory/knowledge/facets.py:275-285 |
| **The recorded supersession edge and the shared cycle rule applied to it.** | `_record_supersession`; `require_acyclic_supersessions` | mcp/src/agents_remember/memory/knowledge/facets.py:288-312; mcp/src/agents_remember/memory/knowledge/facets.py:349-364 |
| The exact earlier decision revision the edge requires, refused by name before any row is written. | `require_decision_revision` | mcp/src/agents_remember/memory/knowledge/facets.py:315-337 |
| The typed attachment write, with the facet revision and the typed endpoint both checked first. | `apply_attach_facet`; `_require_facet_revision` | mcp/src/agents_remember/memory/knowledge/facets.py:375-398; mcp/src/agents_remember/memory/knowledge/facets.py:401-416 |
| **The removal that names its row and deletes that row only, and the designation guarded by the expected row digest.** | `apply_remove_facet_attachment`; `apply_designate_explanation` | mcp/src/agents_remember/memory/knowledge/facets.py:419-457; mcp/src/agents_remember/memory/knowledge/facets.py:589-639 |
| **The explanation pair: the first revision with no designation, and the successor that must name a stored revision of its own explanation.** | `apply_author_explanation`; `apply_add_explanation_revision` | mcp/src/agents_remember/memory/knowledge/facets.py:460-497; mcp/src/agents_remember/memory/knowledge/facets.py:535-586 |
| The subject check that keeps a family subject from being satisfied by an invariant revision. | `require_explanation_subject` | mcp/src/agents_remember/memory/knowledge/facets.py:500-532 |
| The dispatch table over the six command kinds and the two uniform-signature adapters. | `_STEPS` | mcp/src/agents_remember/memory/knowledge/facets.py:673-694 |
| **The standalone boundary: lock, one immediate transaction, scope and generation checks, and the receipt for a refusal.** | `_facet_operation`; `_refused_result` | mcp/src/agents_remember/memory/knowledge/facets.py:697-720; mcp/src/agents_remember/memory/knowledge/facets.py:733-742; mcp/src/agents_remember/memory/knowledge/facets.py:771-772 |
| The operation-name check that refuses a command presented to another operation's entry point. | `_command_matches_operation` | mcp/src/agents_remember/memory/knowledge/facets.py:745-781 |
| **The generation gate read from the dataset's own recorded version rather than the build's.** | `require_facet_generation` | mcp/src/agents_remember/memory/knowledge/facets.py:832-852 |
| The authority home a facet envelope inherits from the namespace it was written into. | `_authority_home` | mcp/src/agents_remember/memory/knowledge/facets.py:859-871 |
| The governing-route reference check, with the ungoverned state never refused. | `_require_governing_route`; "def route_exists(" | mcp/src/agents_remember/memory/knowledge/facets.py:874-887; mcp/src/agents_remember/memory/knowledge/routes.py:233-233 |
| The shipped factories this module reports through, including the four the facet leaf added. | `facet_promotion_not_supported_refusal`; `facet_supersession_cycle_refusal`; `generation_mismatch_refusal`; `explanation_revision_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:1051-1073; mcp/src/agents_remember/memory/knowledge/refusals.py:1074-1130; mcp/src/agents_remember/memory/knowledge/refusals.py:1131-1164; mcp/src/agents_remember/memory/knowledge/refusals.py:1165-1196 |
| The shared graph rule the third lineage graph is judged by. | `supersession_edges`; `cycle_vertices` | mcp/src/agents_remember/memory/knowledge/lineage.py:83-95; mcp/src/agents_remember/memory/knowledge/lineage.py:207-228 |
| The pre-write endpoint existence check the attachment reaches. | `require_attachment_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:226-257 |
| **The cases that hold the two entry points, the cycle rollback, the sealed rows and the generation refusal.** | "test_the_two_entry_points_agree_and_a_refused_write_writes_nothing"; "test_accepted_origin_data_is_refused_at_both_entry_points"; "test_a_supersession_cycle_rolls_back_and_a_sealed_decision_cannot_be_rewritten"; "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write" | mcp/tests/test_knowledge_facets.py:840-875; mcp/tests/test_knowledge_facets.py:363-458; mcp/tests/test_knowledge_facets.py:606-700; mcp/tests/test_knowledge_facets.py:985-1035; mcp/tests/test_knowledge_facets.py:958-965; mcp/tests/test_knowledge_facets.py:1135-1142 |
| The pre-write endpoint existence check the attachment reaches. | `require_attachment_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:226-257 |
| **The cases that hold the two entry points, the cycle rollback, the sealed rows and the generation refusal.** | "test_accepted_origin_data_is_refused_at_both_entry_points"; "test_a_supersession_cycle_rolls_back_and_a_sealed_decision_cannot_be_rewritten"; "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write"; "test_the_two_entry_points_agree_and_a_refused_write_writes_nothing" | mcp/tests/test_knowledge_facets.py:346-382; mcp/tests/test_knowledge_facets.py:589-671; mcp/tests/test_knowledge_facets.py:935-1017; mcp/tests/test_knowledge_facets.py:809-875; mcp/tests/test_knowledge_facets.py:448-455; mcp/tests/test_knowledge_facets.py:691-698; mcp/tests/test_knowledge_facets.py:1135-1142 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: `require_facet_generation` repointed to mcp/src/agents_remember/memory/knowledge/facets.py:832-852. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_authority_home` repointed to mcp/src/agents_remember/memory/knowledge/facets.py:859-871. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_require_governing_route`; "def route_exists(" repointed to mcp/src/agents_remember/memory/knowledge/facets.py:874-887; mcp/src/agents_remember/memory/knowledge/routes.py:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `apply_add_facet`; "def validate_facet_payload(" repointed to mcp/src/agents_remember/memory/knowledge/facets.py:218-272; mcp/src/agents_remember/memory/knowledge/record_envelope.py:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_attachment_endpoint` repointed to mcp/src/agents_remember/memory/knowledge/endpoints.py:226-257. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_attachment_endpoint` repointed to mcp/src/agents_remember/memory/knowledge/endpoints.py:226-257. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: `apply_add_facet`; "def validate_facet_payload(" repointed to mcp/src/agents_remember/memory/knowledge/facets.py:218-272; mcp/src/agents_remember/memory/knowledge/record_envelope.py:249-249. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand while resolving the memory sync** — `apply_add_facet`, `def validate_facet_payload(`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand** — `apply_add_facet`, `def validate_facet_payload(`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``apply_add_facet`; "def validate_facet_payload("` → `mcp/src/agents_remember/memory/knowledge/facets.py:218-272; mcp/src/agents_remember/memory/knowledge/record_envelope.py:191-191`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-17T22:25:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the authored facet write path. It records the **two entry points per write** and why the split makes "a refused write leaves the dataset exactly as it was" a property of the transaction boundary, the payload seam as the only payload decision point (so an unknown subtype is the typed `invalid_payload` refusal rather than a parse error), provenance and `authority_home` taken from the admission and the namespace rather than from a command, proposed-origin-only with the shipped `promotion_not_supported` at both entry points, the **check-every-reference-before-the-row-it-belongs-to** rule across attachments, supersessions, subjects, designations and governing routes, the cycle walk as the shared lineage rule over the third graph, the `pending` split between what a batch declares and what is stored, the operation-name check that refuses an act performed under another name, and the generation gate read from the dataset's own recorded version. It also records a measured divergence rather than leaving it: `_apply_facet_command` constructs `state="no_change"` while the receipt declares only `applied`/`refused`, unreachable on every path the leaf's cases drive and carried as a todo. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
