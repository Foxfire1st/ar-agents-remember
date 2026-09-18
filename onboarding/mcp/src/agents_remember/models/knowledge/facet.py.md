# mcp/src/agents_remember/models/knowledge/facet.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/facet.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `a066550591eb3116ae008cc0d57f3558b0af52c5`|
| lastVerifiedCommitDate | 2026-09-18T07:03:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The closed authored-judgment vocabulary: eight frozen subtypes and their authored commands.** This module
owns **one** closed list. `FACET_KINDS` is the eight subtypes the design names, and every other declaration
here is derived from it or checked against it:

- one frozen payload model per subtype, each under the shipped `KnowledgeModel` base, so an undeclared field
  is refused rather than stored and a payload is a validated shape instead of the untyped properties bag the
  storage design refuses;
- `FacetPayload`, the discriminated union whose member set is exactly `FACET_KINDS`. The discriminator is
  what makes "the vocabulary is closed" checkable: a ninth subtype has no member to resolve to, so it cannot
  be stored as a generic facet;
- `FACET_RECORD_SCHEMAS`, the `record_schema` each subtype's payload resolves to in the envelope registry.
  It is declared here, beside the models, because the pair `(kind, record_schema)` is the registry's key and
  a second spelling elsewhere could drift.

The authored commands live here too, next to the vocabulary they address, rather than in the candidate
module: the closed union in `models/knowledge/candidate.py` is the operation's whole reach and names these
members, while the *shapes* belong with the facet kinds they carry.

## Code Commentary

### Logic

- **The closed list is one tuple and one literal, and the two are asserted equal.** `FacetKind` is the
  `Literal` of the eight spellings and `FACET_KINDS` is the same eight as an ordered tuple; a case asserts the
  derived key sets equal `FACET_KINDS`, so a member cannot be added to one declaration without the other.
- **One frozen payload model per subtype.** `DecisionPayload`, `AssumptionPayload`, `IncidentPayload`,
  `FailureModePayload`, `ScenarioPayload`, `LimitationPayload`, `DiagnosticGuidancePayload` and
  `TerminologyPayload` each declare their own meanings and their own `facet_kind` literal. Two shapes are
  deliberate rather than convenient: `ScenarioPayload.preconditions` and `LimitationPayload.unsupported` are
  **nonempty tuples** (`min_length=1`), because an empty tuple would satisfy the field while omitting the
  meaning the vocabulary fixes; and prose fields are bounded by the shipped `PROSE_MAX_LENGTH` while a
  reference-shaped field (`decider`, `observed_at`) is bounded by `REFERENCE_MAX_LENGTH` and a term by
  `LABEL_MAX_LENGTH`.
- **Two properties are load-bearing and neither is incidental.** First, **no payload field can be read as,
  or substituted for, the record's provenance**: a decision's `decider` is authored *content about who
  decided*, the record's authorship is the admitted operation that recorded it, and there is no payload
  field for `actor_ref`, `authorization_ref`, `operation_id` or `recorded_at` — `extra="forbid"` is what
  refuses a payload that arrives carrying one. Second, **diagnostic guidance is guidance, not a verdict**:
  `DiagnosticGuidancePayload` carries an `interpretation` and its `interpretation_limit` as two required
  fields and no third one that could hold an assessment, a compatibility verdict, a severity or an
  endorsement.
- **The derivations are two functions and two maps.** `_FACET_MODELS` maps each kind to its frozen model,
  `FACET_RECORD_SCHEMAS` is built by comprehension over `FACET_KINDS`, `facet_record_schema` spells the
  `facet-<kind>/v1` name from the kind, `facet_payload_model` returns `None` for a kind this build does not
  declare (which is the point — an unknown or ninth subtype has no shape to validate against), and
  `facet_payload_models` returns every pair for the envelope registry to register.
- **The attachment endpoint set is closed at four kinds, and the route is deliberately absent from it.**
  `AttachmentEndpointKind` names `invariant_revision`, `family_revision`, `source_anchor` and
  `realization_claim`; each has its own frozen endpoint model and its own constant; `ENDPOINT_COLUMNS`
  records which column of `facet_attachment` each kind populates; and `endpoint_identity` narrows by
  explicit `isinstance` rather than `getattr`, so the identity a caller is shown is a field the endpoint
  actually carries. A route is **not** an endpoint kind because the route association is the envelope's own
  `governing_route_id` — a second route mechanism here would be the competing one the design forbids.
- **The explanation subject set is closed at two statement revisions and is a separate closed set.** The
  invariant statement and the family joint guarantee have their own typed models
  (`InvariantStatementSubject`, `FamilyJointGuaranteeSubject`), their own constants and their own
  `SUBJECT_COLUMNS` mapping. The spellings coincide with two endpoint kind names because both name the same
  canonical table, but they are separate constants on purpose: an explanation's subject set and an
  attachment's endpoint set are two closed sets that could diverge, and sharing a literal would hide that.
  `subject_identity` returns the `(identity, revision)` pair and `subject_revision_id` the revision alone.
- **Six authored commands, one per distinct act**, each frozen and extra-forbidding: `AddFacet` records a
  facet as one envelope plus its first sealed revision; `AttachFacet` attaches one exact facet revision to
  one exact typed endpoint; `RemoveFacetAttachment` removes one attachment by identity and expected row
  digest; `AuthorExplanation` authors the first revision of a separable explanation; `AddExplanationRevision`
  edits by authoring a successor that names its exact predecessor; `DesignateExplanation` records which
  revision is designated, guarded by the expected row digest.
- **`AddFacet` carries its payload as a mapping on purpose.** The payload is validated at the **envelope
  seam**, which is the one place any write path decides admissibility; pre-validating it here would be a
  second decision point and would turn an unknown or ninth subtype into a parse error instead of the typed
  `invalid_payload` refusal a caller branches on. What the command fixes is the pair the seam resolves with —
  the declared subtype and the revision the payload is written under — so a refusal can name both.
  `AddFacet` also carries `supersedes_revision_id`, and its validator refuses that field on any kind other
  than `decision`, because a supersession edge is that record kind's own statement.
- **The receipt and the request are the operation's shapes.** `FacetWriteRequest` is one namespace, one
  command and the admitted `provenance` envelope (carried on the request exactly as the realization-claim
  request carries it, so the envelope comes from the admission rather than from any authored payload);
  `FacetWriteIdentity` is one row a write touched, with the digest the store computed and a
  `written`/`removed` state; `FacetWriteResult` is the factual receipt whose validator refuses a refused
  result that reports a written row, an applied result that carries a refusal, and an applied result with no
  row at all.

### Conventions

- **Every value model inherits `KnowledgeModel`**, so the whole vocabulary is frozen, strict and
  extra-forbidding by construction rather than per model.
- **Closed sets are declared as a `Literal` type, an ordered tuple and a name constant per member**, and the
  maps (models, record schemas, endpoint columns, subject columns) are derived from the tuple rather than
  restated.
- **The command union is declared here and named by the candidate module.** `FacetCommand` is the
  discriminated union of the six commands and `FACET_COMMAND_KINDS` is the same six as a tuple; the union
  the operation publishes (`ProposedCommand`) is where they join the shipped twelve.
- **The tables a facet command writes are declared here too.** `FACET_WRITABLE_TABLES` and the
  `FacetRecordTable` literal name the six canonical tables, and the candidate module's `MutableRecordTable`
  is folded from them so an expectation may name a facet row; a case asserts the two declarations agree
  rather than assuming they do.

### Invariants And Boundaries

- **The vocabulary is closed by structure, not by a check.** A ninth subtype has no payload model, no union
  member and no record schema, and `facet_payload_model` returns `None` rather than a default.
- **No field of any model here carries provenance, an assessment or an identity fingerprint.** The only
  identity-bearing fields are the opaque UUIDs a caller authors, and the `row_digest`/`content_digest`
  values live on the read models rather than here.
- **Boundary.** This module declares shapes and nothing else: it performs no validation of a payload against
  the registry (the envelope seam does), writes no row (the write path does), selects nothing (the read
  models do), and does not decide which facet kinds a dataset may hold (the schema generation does).
- **Precision worth stating, because the union makes the closure look stronger than the command does:**
  `AddFacet.facet_kind` is a length-bounded `str` rather than the `FacetKind` literal, so the *command*
  accepts any nonempty kind name and the closure is enforced one seam later, where an unknown kind is the
  typed `invalid_payload` refusal. That is the deliberate trade the docstring records, not an oversight —
  but a reader should not conclude that `AddFacet(facet_kind="retrospective", …)` is unconstructible.

### Todos

None recorded. The eight subtypes are the whole vocabulary this leaf was asked for; widening it is a
vocabulary change with its own packet rather than an edit here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one closed list, as a literal and as an ordered tuple, with the schema derivation that keeps them in step.** | `FACET_KINDS`; `FacetKind`; `facet_record_schema` | mcp/src/agents_remember/models/knowledge/facet.py:57-88 |
| **The eight frozen payload models, one per subtype, each carrying its own `facet_kind` literal and its own minimum meanings.** | `DecisionPayload`; `AssumptionPayload`; `IncidentPayload`; `FailureModePayload`; `ScenarioPayload`; `LimitationPayload`; `DiagnosticGuidancePayload`; `TerminologyPayload` | mcp/src/agents_remember/models/knowledge/facet.py:91-177 |
| **The discriminator whose member set is exactly the eight subtypes.** | `FacetPayload` | mcp/src/agents_remember/models/knowledge/facet.py:183-193 |
| The kind-to-schema map, the kind-to-model map and the two accessors, including the `None` an undeclared kind earns. | `FACET_RECORD_SCHEMAS`; `facet_payload_model`; `facet_payload_models` | mcp/src/agents_remember/models/knowledge/facet.py:198-230 |
| **The four closed endpoint kinds, their four frozen models, the column each populates, and the route's deliberate absence.** | `AttachmentEndpointKind`; `InvariantRevisionEndpoint`; `FamilyRevisionEndpoint`; `SourceAnchorEndpoint`; `RealizationClaimEndpoint`; `ENDPOINT_COLUMNS`; `endpoint_identity` | mcp/src/agents_remember/models/knowledge/facet.py:238-320 |
| **The two closed subject kinds, their typed models and the separate constants that keep the two sets from being confused.** | `ExplanationSubjectKind`; `InvariantStatementSubject`; `FamilyJointGuaranteeSubject`; `SUBJECT_COLUMNS`; `subject_identity` | mcp/src/agents_remember/models/knowledge/facet.py:329-382 |
| **The six authored commands, including `AddFacet`'s mapping payload and the validator that confines supersession to a decision.** | `AddFacet`; `AttachFacet`; `RemoveFacetAttachment`; `AuthorExplanation`; `AddExplanationRevision`; `DesignateExplanation` | mcp/src/agents_remember/models/knowledge/facet.py:391-486 |
| The command union and its kind tuple, named here and joined to the operation's reach in the candidate module. | `FacetCommand`; `FACET_COMMAND_KINDS` | mcp/src/agents_remember/models/knowledge/facet.py:492-509 |
| **The standalone request, the touched-row identity and the receipt whose validator makes a refusal and a write mutually exclusive.** | `FacetWriteRequest`; `FacetWriteIdentity`; `FacetWriteResult` | mcp/src/agents_remember/models/knowledge/facet.py:512-585 |
| The six canonical tables a facet command writes, and the candidate module's table vocabulary they fold into. | `FACET_WRITABLE_TABLES`; "MutableRecordTable = Literal[" | mcp/src/agents_remember/models/knowledge/facet.py:532-548; mcp/src/agents_remember/models/knowledge/candidate.py:122-134 |
| The sealed, extra-forbidding base every model here inherits. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The facet-specific entry point that resolves the `(kind, record_schema)` pair and refuses an unknown kind. | `validate_facet_payload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:191-220 |
| **The registry those models are registered in — which since `KS-R19@v1` holds four groups (the internal conformance kind, these eight facet kinds, the two detection kinds and the requirement-revision kind).** | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:93-113 |
| The facet kind set derived from those entries rather than restated. | `FACET_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:118-118 |
| The requirement family the registry gained, derived from the entries it unpacks. | `REQUIREMENT_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:130-132 |
| The requirement kind and its frozen shape, declared in the vocabulary module rather than restated in the registry. | `REQUIREMENT_REVISION_KIND`; `REQUIREMENT_REVISION_SCHEMA` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84 |
| **The case that keeps this closure a measurement: the union of all four groups, so a ninth subtype cannot be admitted without that line changing.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes" | mcp/tests/test_knowledge_facets.py:183-247 |
| The closed union these six commands join, and the dispatch tables that must cover every member. | `ProposedCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:372-392 |
| **The cases that hold the closed vocabulary, the per-subtype refusals and the receipt's absent verdict fields.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes"; "test_every_subtype_refuses_a_bad_shape_a_missing_meaning_and_its_own_provenance"; "test_a_facets_authorship_lifecycle_and_receipt_are_stored_data_with_no_verdict" | mcp/tests/test_knowledge_facets.py:181-227; mcp/tests/test_knowledge_facets.py:229-280; mcp/tests/test_knowledge_facets.py:306-343 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-18T06:45+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **re-read the envelope-seam rows and recorded the fourth group this registry gained, then retired the card's generated projection bullet by hand.** The registry row named **three** groups because that was the fact when it was written; `KS-R19@v1` registers the requirement-revision kind, so the row now states **four** and the derived-set rows name `REQUIREMENT_RECORD_KINDS` beside `FACET_RECORD_KINDS`. The citation was **re-derived rather than shifted**: the registry moved to `:93-113` with the requirement pair unpacked at `:112`, `FACET_RECORD_KINDS` to `:118`, and the new derived set to `:130-132`. Nothing about this module's own eight-kind vocabulary changed, and this leaf did not modify `models/knowledge/facet.py`, so **no verification stamp is advanced** on this card — the reviewed candidate is recorded only where the body was actually re-read against a file this leaf changed. A row for the seam-registry case was added, because that case is what makes the closure a measurement: it asserts the union of all four groups, so a fifth group cannot be admitted without that line changing.
- 2026-09-18T06:35+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``FACET_RECORD_KINDS`` → `mcp/src/agents_remember/memory/knowledge/record_envelope.py:118-118`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read the envelope-seam row and re-cited it by hand, and recorded what the seam now holds.** The row named three anchors across three ranges that no longer held them, so it is now one anchor per row at each declaration's current range, and the registry row states the fact `KS-R14@v1` changed: `PAYLOAD_MODELS` holds **three groups** — the internal conformance kind, these eight facet kinds, and the two mechanical-detection kinds — with `FACET_RECORD_KINDS` still derived from its own entries rather than restated. Nothing about this module's own vocabulary changed, and no verification stamp is advanced for a file this leaf did not modify.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the closed authored-judgment vocabulary. It records the one closed list and the three declarations derived from it, the eight frozen payload models with the two nonempty-tuple meanings that keep an empty value from satisfying a field, the **two load-bearing properties** (no payload field can be read as provenance, and guidance carries an interpretation plus its limit rather than a verdict), the four closed endpoint kinds with the route's **deliberate absence** from them, the two closed subject sets kept as separate declarations rather than a shared literal, the six authored commands, and `AddFacet`'s mapping payload validated at the envelope seam so an unknown subtype is the typed `invalid_payload` refusal rather than a parse error. It also states the precision that the *command* accepts any nonempty kind name while the closure is enforced one seam later, so a reader does not conclude the ninth subtype is unconstructible. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
