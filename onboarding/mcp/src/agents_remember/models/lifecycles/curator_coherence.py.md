# mcp/src/agents_remember/models/lifecycles/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:53+02:00 |
| lastVerifiedCommitHash | `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| lastVerifiedCommitDate | 2026-09-18T15:05:30+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l3-ar` uncommitted source (`mcp/src/agents_remember/models/lifecycles/curator_coherence.py` **385 → 398 lines**, `_action_has_one_input_shape` only); base `a12c511f6e76bd1188719cad0a9104d78d46920c` |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

Defines the strict structured contracts for curator source candidates, agent-owned judgments,
immutable coherence generations, the sole live authority manifest, optional attempt snapshots, the
four-action public request/response API, and — since the closeout plane was cut away — the frozen
`ValidatedCuratorCoherence` value (`:372-385`) that carries one validated authority with its record,
its two paths, its digest and its evidence. Under CCR-R03@v1 the memory-quality attestation and
immutable coherence record additionally carry a typed direct-dependency declaration so evidence is
a content-addressed consumer of exactly its declared inputs
cit:([`CuratorQualityAttestation`, `CuratorCoherenceRecord`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:65-92; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:189-233).

## Code Commentary

### Logic

`CuratorQualityAttestation` accepts only the exact `ar-curator-memory-quality/v1` schema and checks
candidate count and uniqueness. `CuratorCoherenceRecord` keeps semantic requirement revision,
delivery attempt, and content identities in separate fields and requires the recorded judgment set
to exactly equal the source-candidate set. `CuratorCoherenceRequest` makes publication a strict
compare-and-swap shape while forbidding publication-only fields on status, prepare, and validate.

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
cit:([`memory_quality_attestation_dependencies`, `require_memory_quality_attestation_dependencies`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:94-133; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:134-159).

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
| The quality attestation validates exact candidate count and uniqueness. | `CuratorQualityAttestation` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:65-91 |
| Immutable record validation enforces exact candidate-to-judgment coverage. | `CuratorCoherenceRecord` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:189-235 |
| The discriminated action request separates read actions from publication CAS input, and names the publication fields it is missing. | `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:259-330 |
| The R03 dependency vocabulary used by this record type. | `EvidenceDependencies`, `dependency`, `require_evidence_dependencies` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:99-122; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:216-227; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:240-277; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:238-273 |

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

## Update History

- 2026-09-18T14:53+02:00 — 260918-TSIP-L3 curator (uncommitted change set on `ar/260918-tsip-l3-ar`,
  base `a12c511f`): this source is one of the leaf's five changed paths, so the card gained a **body**
  update, not a restamp. `_action_has_one_input_shape` now carries `(name, value)` pairs and its
  `publish` refusal appends `missing: <fields>` (the sibling branch says `supplied: <fields>`), which
  is the repair of `T50`'s second half — the first half is the registered description in
  `mcp/registration/tasks.py`. Recorded in `Logic` that the diagnosis has to live in the message
  because a model-level validator reports `loc: ()` and the JSON schema cannot carry the requirement
  (`required == ["action","contract_path"]`); the same sentence was added to `Invariants And
  Boundaries`. Evidence for the reading is the leaf's own pin in `mcp/tests/test_tools.py`
  (`CuratorCoherencePublishContractTests`, one `publish` omission per field, positive control first).
  Two citations into this file were re-derived against the new bytes: the `CuratorCoherenceRequest`
  row moved `:259-317 → :259-330` (the change is an insertion inside that range), and the eight rows
  that end below `:296` were re-read and are **unchanged**, which is why they are not restamped.
  `lastUpdated` advances with this body edit; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are
  deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real
  code commit.
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