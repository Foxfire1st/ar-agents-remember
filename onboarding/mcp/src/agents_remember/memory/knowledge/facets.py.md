# mcp/src/agents_remember/memory/knowledge/facets.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The six standalone operations, each naming the act it performs so a refusal is reported under the operation the caller asked for.** [1]
- **The one dispatch the batch path and the standalone driver share, and the alias that documents the split.** [2]
- **The payload seam as the only payload decision point, and the envelope-plus-first-revision write.** [3]
- **The payload seam as the only payload decision point, and the envelope-plus-first-revision write.** [4]
- **Proposed origin only, refused at both entry points with the shipped code.** [5]
- **The recorded supersession edge and the shared cycle rule applied to it.** [6]
- The exact earlier decision revision the edge requires, refused by name before any row is written. [7]
- The typed attachment write, with the facet revision and the typed endpoint both checked first. [8]
- **The removal that names its row and deletes that row only, and the designation guarded by the expected row digest.** [9]
- **The explanation pair: the first revision with no designation, and the successor that must name a stored revision of its own explanation.** [10]
- The subject check that keeps a family subject from being satisfied by an invariant revision. [11]
- The dispatch table over the six command kinds and the two uniform-signature adapters. [12]
- **The standalone boundary: lock, one immediate transaction, scope and generation checks, and the receipt for a refusal.** [13]
- The operation-name check that refuses a command presented to another operation's entry point. [14]
- **The generation gate read from the dataset's own recorded version rather than the build's.** [15]
- The authority home a facet envelope inherits from the namespace it was written into. [16]
- The governing-route reference check, with the ungoverned state never refused. [17]
- The shipped factories this module reports through, including the four the facet leaf added. [18]
- The shared graph rule the third lineage graph is judged by. [19]
- The pre-write endpoint existence check the attachment reaches. [20]
- **The cases that hold the two entry points, the cycle rollback, the sealed rows and the generation refusal.** [21]
- The pre-write endpoint existence check the attachment reaches. [22]
- **The cases that hold the two entry points, the cycle rollback, the sealed rows and the generation refusal.** [23]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
