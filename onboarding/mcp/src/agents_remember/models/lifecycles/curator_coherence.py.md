# mcp/src/agents_remember/models/lifecycles/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| lastVerifiedCommitDate | 2026-09-18T02:49:57+02:00|
| governingOverview | `overview.md` |

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
cit:([`CuratorQualityAttestation`, `CuratorCoherenceRecord`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:66-92; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:190-234).

## Code Commentary

### Logic

`CuratorQualityAttestation` accepts only the exact `ar-curator-memory-quality/v1` schema and checks
candidate count and uniqueness. `CuratorCoherenceRecord` keeps semantic requirement revision,
delivery attempt, and content identities in separate fields and requires the recorded judgment set
to exactly equal the source-candidate set. `CuratorCoherenceRequest` makes publication a strict
compare-and-swap shape, forbids publication-only fields on status, prepare, and validate, and — since
KS-R24@v1 — refuses by **naming** the member it is refusing on rather than by naming a category: a
`publish` refusal lists every missing publication member by its request field name, and a read action's
refusal names the publication-only field it received.

R03 binds the attestation's rendered report and inspected pair to a declared dependency
population: `memory_quality_attestation_dependencies` declares the candidate-state (pair contract
digest), exact code and memory candidate trees (git-object digests), the rendered-checklist bytes,
and both validator identities; `require_memory_quality_attestation_dependencies` rebuilds that
expected set from the attestation's current source facts and refuses
`memory-quality-attestation-dependencies-stale` on any mismatch
cit:([`memory_quality_attestation_dependencies`, `require_memory_quality_attestation_dependencies`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:95-132; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:135-158).

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
- Publication requires every expected identity and an authorized declared caller.
- One declaration states what publication requires: `PUBLICATION_MEMBERS` is the authority for the
  validator, the `publish` refusal and the `prepare` text, so no reader can name a member the others
  do not know about and an appended member needs no second edit.
- The attestation binds the exact code/memory candidate trees it inspected; a changed tree stales
  the evidence, and no filename, mtime, or marker substitutes for the typed digest edges.

### Todos

None recorded.

## Docs References

No configured external documentation applies; the schemas are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle schema has no external authority. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The quality attestation validates exact candidate count and uniqueness. | `CuratorQualityAttestation` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:66-92 |
| Immutable record validation enforces exact candidate-to-judgment coverage. | `CuratorCoherenceRecord` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:190-234 |
| The discriminated action request separates read actions from publication CAS input. | `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:370-434 |
| **The one declaration of what `publish` requires, and the per-member flag marking the two `prepare` does not derive.** | `PublicationMember`; `PUBLICATION_MEMBERS` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:260-288 |
| **The refusal that names every missing publication member by request field name, in declaration order, and calls out a missing delivery identity.** | `publication_refusal` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:309-333 |
| **The sibling refusal that names the publication-only field a read action received.** | `forbidden_publication_refusal` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:336-339 |
| **The statement of the complete publication input set, read from the declaration at call time.** | `publication_input_statement` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:342-367 |
| **Which publication fields a request supplied, `judgments` included, and the validator that refuses on it.** | `_publication_inputs_supplied`; `_action_has_one_input_shape` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:405-418; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:420-434 |
| The R03 dependency vocabulary used by this record type. | `EvidenceDependencies`, `dependency`, `require_evidence_dependencies` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98-118; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:214-223; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-273 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| These are local MCP and lifecycle records only. | — | — |

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

## Update History
- 2026-09-18T03:10+02:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read this card against the changed source and recorded the publication declaration the leaf added.** The request model now carries `PUBLICATION_MEMBERS` as the single authority for what `publish` requires, with `publication_refusal`, `forbidden_publication_refusal` and `publication_input_statement` as its three readings, and the Logic paragraph, the Purpose coordinates and the reference table were re-derived from the current file: `ValidatedCuratorCoherence` is at `:490-504`, the attestation at `:66-92`, the record at `:190-234`, and `CuratorCoherenceRequest` — which moved to `:370-434` when the declaration was inserted above it — is re-cited by this pass rather than left to the mechanical projection that had rewritten its range (that generated bullet is retired here). Five rows were added for the declaration and its three readers, and the Invariants section gained the single-declaration rule. The section states the half the packet left open rather than implying it: the two delivery identities remain **required**, and a differential probe measured 0 outcome differences over 80 request shapes. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `EvidenceDependencies`; `dependency`; `require_evidence_dependencies` repointed to mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98-118; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:214-223; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `EvidenceDependencies` in the row 82 of this card from mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-242 to mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98, the extent of the construct the claim is about (the checker named line(s) [98, 229, 233] as its live location); re-pointed `require_evidence_dependencies` in the row 82 of this card from mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98 to mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:234, the extent of the construct the claim is about (the checker named line(s) [234, 238, 345] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `EvidenceDependencies` in the row 82 of this card from mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:214-220 to mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98-99, the extent of the construct the claim is about (the checker named line(s) [98, 229, 233] as its live location); re-pointed `require_evidence_dependencies` in the row 82 of this card from mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:98-99 to mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-242, the extent of the construct the claim is about (the checker named line(s) [234, 238, 345] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `dependency` in the row 82 of this card from mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-242 to mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:214-220, the extent of the construct the claim is about (the checker named line(s) [19, 55, 80] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:214-220 in the row 82 of this card; the repetition added no pooled evidence
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/models/lifecycles/curator_coherence.py` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained the
  `ValidatedCuratorCoherence` dataclass and its imports since the recorded verification commit.
  Re-derived every cited range (+3 for the added imports; `CuratorQualityAttestation` measured at
  `:65-93`) and added the new value to the Purpose surface list. No other claim changed;
  verification metadata remains closeout-owned.
- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the typed direct-dependency declarations on the memory-quality attestation and coherence record, plus the new attestation dependency builders/currentness guards; prior pair-identity and judgment-set prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: made the exact pair mandatory acceptance evidence across
  attestation, record, and response models. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for MCAR-L02 A005's strict coherence identity, authority,
  snapshot, action, and response contracts. Verification remains closeout-owned.