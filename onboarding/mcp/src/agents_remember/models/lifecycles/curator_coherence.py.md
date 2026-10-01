# mcp/src/agents_remember/models/lifecycles/curator_coherence.py

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

Defines the strict structured contracts for curator source candidates, agent-owned judgments,
immutable coherence generations, the sole live authority manifest, optional attempt snapshots, the
four-action public request/response API, and — since the closeout plane was cut away — the frozen
`ValidatedCuratorCoherence` value (`:490-504`) that carries one validated authority with its record,
its two paths, its digest and its evidence. Under CCR-R03@v1 the memory-quality attestation and
immutable coherence record additionally carry a typed direct-dependency declaration so evidence is
a content-addressed consumer of exactly its declared inputs
cit:([`CuratorQualityAttestation`, `CuratorCoherenceRecord`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:83-109; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:226-307).

## Code Commentary

### Logic

`CuratorCoherenceRecordedJudgment.evidenceArtifact` is an optional owner-stamped existing path/SHA/size value; its digest must equal the originally recorded judgment hash. It is absent from caller judgment inputs and omitted canonically when absent, so old record seals stay intact. `ValidatedCuratorCoherenceGeneration` carries a digest-addressed integrity result without a live authority claim; `ValidatedCuratorCoherence` remains the live selected authority result. `CuratorCoherencePaths.judgment_evidence` derives custody under the existing artifact root.

`CuratorQualityAttestation` accepts only the exact `ar-curator-memory-quality/v1` schema and checks
candidate count and uniqueness. `CuratorCoherenceRecord` keeps semantic requirement revision,
delivery attempt, and content identities in separate fields and requires the recorded judgment set
to exactly equal the source-candidate set. `CuratorCoherenceRequest` makes publication a strict
compare-and-swap shape, forbids publication-only fields on status, prepare, and validate, and — since
KS-R24@v1 — refuses by **naming** the member it is refusing on rather than by naming a category: a
`publish` refusal lists every missing publication member by its request field name, and a read action's
refusal names the publication-only field it received.

**The refusal is the whole diagnosis, because pydantic reports a model-level validator with
`loc: ()` (260918-TSIP-L3, `T50`).** `_action_has_one_input_shape` requires **nine** non-null fields
for `publish`; a bare `any(value is None …)` over that tuple named a *class* of absent fields and
none of them, so a caller who had supplied every field the tool description named could not learn
which one it wanted. Each entry is now a `(request-field name, value)` pair, and the `publish`
refusal appends `missing: <every absent field by request name>`; the sibling branch states
`supplied: <what it received>` instead. The predicate itself is unchanged, and the JSON schema
cannot carry the requirement — `required` is `["action", "contract_path"]` because the constraint is
conditional on `action == "publish"` — which is why the description and the message are the
load-bearing surfaces.

R03 binds the attestation's rendered report and inspected pair to a declared dependency
population: `memory_quality_attestation_dependencies` declares the candidate-state (pair contract
digest), exact code and memory candidate trees (git-object digests), the rendered-checklist bytes,
and both validator identities; `require_memory_quality_attestation_dependencies` rebuilds that
expected set from the attestation's current source facts and refuses
`memory-quality-attestation-dependencies-stale` on any mismatch
cit:([`memory_quality_attestation_dependencies`, `require_memory_quality_attestation_dependencies`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:112-149; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:152-175).

### Conventions

All authority models are frozen and reject extra fields. Caller judgments omit lifecycle-owned
evidence digests; publication creates the recorded judgment form after reading the cited bytes.
Dependency declarations are built from the same canonical edge encoding shared by every record
type, never hand-written per domain.

### Invariants And Boundaries

- A requirement revision is not a delivery attempt or an evidence digest.
- Exactly one judgment exists for each `(sourceFile, onboardingFile, classification)` tuple.
- Markdown is not represented as an input model; it is projection output only.
- The stable manifest points to one content-addressed generation.
- Publication requires every expected identity and an authorized declared caller, and a refusal
  names each absent field by request name rather than the class of them (`T50`).
- One declaration states what publication requires: `PUBLICATION_MEMBERS` is the authority for the
  validator, the `publish` refusal and the `prepare` text, so no reader can name a member the others
  do not know about and an appended member needs no second edit.
- The attestation binds the exact code/memory candidate trees it inspected; a changed tree stales
  the evidence, and no filename, mtime, or marker substitutes for the typed digest edges.

### Todos

None recorded.

## Evidence

### Docs References

No configured external documentation applies; the schemas are repository-owned.

The lifecycle schema has no external authority.

### Repo-Internal References

- The quality attestation validates exact candidate count and uniqueness. [1]
- Immutable record validation enforces exact candidate-to-judgment coverage. [2]
- The discriminated action request separates read actions from publication CAS input, and names the publication fields it is missing. [3]
- **The one declaration of what `publish` requires, and the per-member flag marking the two `prepare` does not derive.** [4]
- **The refusal that names every missing publication member by request field name, in declaration order, and calls out a missing delivery identity.** [5]
- **The sibling refusal that names the publication-only field a read action received.** [6]
- **The statement of the complete publication input set, read from the declaration at call time.** [7]
- **Which publication fields a request supplied, `judgments` included, and the validator that refuses on it.** [8]
- The R03 dependency vocabulary used by this record type. [9]

The following declarations carry the changed boundary.

- Owner custody preserves original judgment bytes and old encoding. [10]
- A durable generation integrity result makes no live readiness claim. [11]

### Cross-Repo References

No meaningful cross-repository reference applies.

These are local MCP and lifecycle records only.

## MCAR-L03 Acceptance Identity

Both the source memory-quality attestation and immutable curator-coherence record require
`pairIdentity`. Public coherence responses expose the pair and typed pair-refusal field/repair
arguments. Missing pair data is invalid rather than being read through a compatibility path.

## 260831-CCR-R03 Declared Attestation Dependencies

The source attestation now carries `dependencies`; the coherence observer and publication owner
recompute the exact dependency set from the candidate pair, code/memory candidate trees, and
rendered-checklist digest at currentness time, so the memory-quality evidence cannot be rebound to
another candidate or report (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## KS-R24@v1 The Publication Set States Itself

The nine members `publish` requires are now **one declaration** — `PUBLICATION_MEMBERS`, a tuple of
`PublicationMember` beside the request model, in the request model's own field order, each entry
carrying its caller-written field name and whether `prepare` derives it. The inline `publication_fields`
tuple the validator used to build is gone: the validator reads the declaration through `getattr`, so a
member appended there is checked, named and stated with no second edit. `JUDGMENTS_MEMBER` names
`judgments`, which is a publication input too but not one of the nine the `None` check covers — a leaf
with no source candidates publishes with an empty judgment list.

The three readings of that declaration are the requirement:

- `publication_refusal` keeps the shipped opening sentence — `publish requires every identity,
  predecessor, and caller field` — and appends the missing members by request field name in declaration
  order. Only the **missing** members that are the caller's own delivery identities are called out, as
  `semantic_requirement_revision` and `delivery_attempt` are the two `prepare` does not derive; naming a
  member the caller did supply would reproduce the defect this text exists to remove.
- `forbidden_publication_refusal` names the publication-only request fields a `status`/`prepare`/
  `validate` call actually carried, in the request model's own field order, so `judgments` is named in
  its real position between `delivery_attempt` and the `expected_*` members. The `freeze_snapshot`
  branch keeps its own message byte-identically.
- `publication_input_statement` is what the `prepare` response carries (see the publication card on the
  closeout route): it names the per-candidate judgments and every declared member, and marks the two it
  does not derive. It reads the declaration at call time, so an extended declaration reaches the text
  with no edit — the drift the requirement exists to remove.

Nothing else moved: no member became optional, none became required, the canonical record schema, the
publication fingerprint, the predecessor rule and the idempotent replay are untouched, and a
differential probe over 80 request shapes measured **0** accept/refuse outcome differences against the
base revision. The out-of-scope half is stated rather than implied: the two delivery identities remain
**required**, and a later ruling may decide otherwise.

## KS-R15@v1 Typed Assessment Collection

This authority now carries a **second typed collection beside `judgments`**, and the separation is the
point rather than an implementation detail. A judgment's identity is the `(sourceFile, onboardingFile,
classification)` triple, and `_judgments_cover_candidates_exactly` refuses a record whose judgment set
is not exactly its source-candidate set. A knowledge review's subject is a family, an invariant
revision or a comparison — none of which is a source-file pair — so appending one to `judgments` would
either break exact coverage or fabricate a source-candidate tuple for a family, which the design
forbids outright.

`CuratorCoherenceRecord.assessments` is that separate collection, bounded by
`MAX_CURATOR_REVIEW_ASSESSMENTS = 256`. The bound is deliberately far below the candidate bound: an
assessment is an authored act a human writes, not a machine-produced row per changed file, so a
thousand of them on one leaf is a defect rather than a workload. Its own validator,
`_assessments_are_uniquely_identified`, refuses a repeated assessment identity and says nothing about
source candidates, which keeps `_judgments_cover_candidates_exactly` the only rule relating judgments
to candidates. The field defaults to empty, so every already-published generation stays valid: an
assessment is optional content and its **absence** is reported as the `none-recorded` state rather
than as an empty favourable disposition.

`CuratorCoherenceRequest.review_assessments` is the submission-side input, named by
`REVIEW_ASSESSMENTS_MEMBER`. It is deliberately **not** a member of `PUBLICATION_MEMBERS`: every one
of those nine is an identity `publish` must be told, while this one is content a leaf may legitimately
have none of, and making it required would force every existing caller to supply an empty list to say
so. Like `judgments` it is refused on `status`/`prepare`/`validate` by the shape validator, so the four
actions keep one input shape each.

## KS-R23@v1 The Record Carries A Durable Attestation Copy

`CuratorCoherenceRecord.attestationCopyPath` (`:221`, optional, `None` when absent) is the model half of
`260915-KS-L23` item 18's **second** measurement: the record's `attestationPath` names a file inside the
leaf's own **enclosure**, and `lifecycle_finalize_task`'s automatic cleanup reclaims that enclosure —
`os.path.exists` is False for it on every landed leaf, so each authority's `attestationSha256` committed
to bytes recoverable nowhere, and a reader could no longer tell a candidate-empty publication from one
whose attestation listed candidates. The publication now copies those exact bytes into the surviving task
tree beside the record, content-addressed by the attestation's own digest, and records the
task-root-relative path here.

The field is deliberately optional rather than required: authorities published before it existed carry
no copy, and that absence has to be distinguishable from a copy that was written. It adds no new record
validity rule — it is the durable address of bytes the record already commits to — and the publication
refuses (`curator-coherence-attestation-stale`, `curator-coherence-content-address-collision`) rather
than recording a path whose bytes do not match `attestationSha256` (see the publication card on the
closeout route).
