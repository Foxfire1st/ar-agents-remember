# mcp/src/agents_remember/memory/knowledge/record_envelope.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The typed record envelope's payload seam: one registry, one entry point.** The `knowledge_record`
envelope is a typed envelope rather than an unvalidated property bag, and this module is the only
place any write path decides whether a payload is admissible for the kind and schema it declares.

Before this leaf the substrate had no common envelope for a knowledge record, so every new category
of knowledge would have cost a new identity design. This module is the mechanism that makes the
envelope's "typed" half real: a shape registry, a single validation entry point, and one refusal code
covering every inadmissible payload.

**The registry now holds twenty-two `(kind, schema)` pairs across the record groups that registered through
this one seam, and every later group registered the way the one before it did.** The internal conformance
kind; the eight authored-judgment facet kinds; since `KS-R14@v1` the two mechanical-detection kinds
`detection_signal` and `detection_run`; since `KS-R19@v1` the requirement-revision kind
`requirement_revision`, which resolves to `RequirementRevisionPayload` in
`models/knowledge/requirement.py`; the citation-binding kind; the two supporting-record kinds
(`evidence_claim` and `verification_observation`); the three authored-effect member kinds with their
`semantic_change_set`; and — the registration this card's candidate records — the truth-coverage census's
three kinds, `census_inventory_row`, `census_claim` and `census_disposition`, unpacked from
`CENSUS_PAYLOAD_MODELS` in `models/knowledge/census.py`. The counts this card used to carry (12 over 12,
then 13 over 13) are superseded: the registry is **22 over 22**, and the module docstring's deferred name
`DetectionSignal` landed several leaves ago while `EvidenceClaim` landed as one of the supporting-record
pair.

**Every family, one seam, and the same reason each time.** None of these groups became a table or a
generation column: the frozen payload model *is* the shape, so a signal's required field set, its closed
vocabularies and its construction refusals stay declared **once**, in the model module that owns them.
A second declaration as SQL columns would be a second place for the same field set to drift, and every
family whose pair set is declared beside its own model — `REQUIREMENT_PAYLOAD_MODELS`, the supporting-record
and authored-effect mappings, and now `CENSUS_PAYLOAD_MODELS` — is **unpacked** into `PAYLOAD_MODELS` rather
than restated here for exactly that reason: the registry and the vocabulary cannot disagree about which pairs
exist. The census group shows the rule at its clearest, because its three shapes carry closed vocabularies of
their own (an inventory row's parse outcome, a claim's claim-kind and applicability, a disposition's kind)
that the seam enforces without this module naming a value of any of them.

## Code Commentary

### Logic

- Two values select a payload's shape, and they are not interchangeable. `record_schema` names the
  **frozen Pydantic shape** the revision was written against and selects it; `kind` constrains **which
  shapes are admissible** for that kind. `PAYLOAD_MODELS` is keyed by the `(kind, record_schema)`
  pair for exactly that reason — a schema that is valid for one kind is not automatically valid for
  another.
- `KIND_SCHEMAS` is **derived** from `PAYLOAD_MODELS` rather than restated, so a kind cannot admit a
  shape the registry does not hold. A restated map would be a second source of truth for the same
  fact, and the two could diverge silently.
- `validate_record_payload(kind, record_schema, payload, *, operation=…, record_id=None)` is the one
  entry point. It returns the **validated model instance**, not a boolean, so a caller stores what was
  validated instead of re-deriving it — and it returns a **refusal** rather than raising, because an
  inadmissible payload is an expected failure a caller branches on.
- Three paths refuse, all with the shipped code `invalid_payload`: an unregistered `kind`; a
  `record_schema` that is not admissible for that kind; and a payload that does not validate against
  the resolved model. Each refusal names the operation the caller passed, the `record_revision` table,
  the kind's admitted schemas or the schema itself as `expected`, the observed value, and the same
  next action: correct the payload or declare the registered schema the shape belongs to, and nothing
  was written.
- `_render_validation_error` bounds the rendered detail to the **first four** validation errors and
  names each by its position, so a refusal stays readable when a large payload is malformed
  throughout.
- The registry maps to **frozen** models: `ConformancePayload` inherits the package's `KnowledgeModel`
  base, which is strict, extra-forbidding and frozen. A validated payload is therefore a value, and a
  caller cannot mutate what it validated into something the registry would not have accepted.

**The two kinds that complete the deferred set are registered.** `(evidence_claim, evidence-claim/v1)` and `(verification_observation, verification-observation/v1)` resolve to the frozen payload models the supporting-record vocabulary declares, so both record groups reach the typed seam every other record passes through rather than a second decision point beside it — and a field that is not declared has nowhere to be stored. `EVIDENCE_RECORD_KINDS` is derived from those declarations beside `FACET_RECORD_KINDS` and `DETECTION_RECORD_KINDS`, so a caller naming what the registry holds names four groups whose disjointness is a property of a kind being one string. **The claim's subject and its claimed coverage are deliberately not payload fields.** They are resolved relations, so they live in generation 5's typed join tables, where endpoint-kind compatibility is a constraint of the schema rather than a value this seam validates at runtime.

**The truth-coverage census's three kinds are the newest registration, and they arrive the same way.** `CENSUS_PAYLOAD_MODELS` is unpacked into `PAYLOAD_MODELS` as the last entry of the mapping, so `(census_inventory_row, census-inventory-row/v1)`, `(census_claim, census-claim/v1)` and `(census_disposition, census-disposition/v1)` resolve through this seam rather than through a second decision point beside it. **Nothing in those three shapes can hold a semantic verdict.** The inventory row carries its parse outcome, the claim its closed claim-kind and applicability vocabularies, the disposition its kind and its links — so a category, a status derived from import success or a mismatch class is not a value this registry could store *and* not a value it could refuse for the wrong reason: every one of them is simply "this payload does not validate", because no field of these three shapes could carry one. The census's own record group reads the seam's answer the same way every group does: it resolves the payload through this call, writes the envelope row and its one sealed revision from what came back, and keeps what the envelope cannot express — the record's own identity column and the relations a claim or a disposition declares — in its own tables, written only as part of the aggregate that owns them.

### Conventions

- **The internal conformance kind, the eight facet kinds, the two detection kinds, and one entry set per later family — the requirement revision, the citation binding, the supporting-record pair, the authored-effect kinds and the census's three.** `INTERNAL_CONFORMANCE_KIND`
  (`internal_conformance`) with `INTERNAL_CONFORMANCE_SCHEMA` (`internal-conformance/v1`) and its
  minimal `ConformancePayload` exist only to exercise the seam, so the typed half of the envelope has
  a mechanism rather than a promise. It is marked internal, it is **not** a knowledge category, and
  the later leaves that add the real categories (`EvidenceClaim`, …) add them
  *beside* it rather than replacing it — `EvidenceClaim` has since landed as one of the supporting-record
  pair. The detection pair was added that way:
  `(detection_signal, detection-signal/v1)` and `(detection_run, detection-run/v1)` are two ordinary
  registry entries whose models are the frozen payload models, and `DETECTION_RECORD_KINDS` is derived
  from the same declarations the entries are built from rather than restated — so the groups are
  disjoint by construction, because a kind is one string. The census's three kinds joined by that
  route: one unpacked mapping, three ordinary entries, and no value of the vocabularies they carry
  named anywhere in this module.
- **A caller that must name what the registry holds reads `PAYLOAD_MODELS`, and the derived sets are the group-local views.** The membership is stated **once** — in that mapping and in this module's docstring — because the per-set comments had drifted: each of the five derived group constants used to restate *its own incomplete list* of groups ("names every group — the internal conformance kind, the eight facet kinds, the two detection kinds …"), and the lists contradicted each other and the registry. `FACET_RECORD_KINDS`, `DETECTION_RECORD_KINDS`, `REQUIREMENT_RECORD_KINDS`, `EVIDENCE_RECORD_KINDS` and `CITATION_BINDING_RECORD_KINDS` are each derived from their own entries, and `KIND_SCHEMAS` is derived from the whole registry, so no group's membership can drift from the registry it is a view of; the derived sets are disjoint by construction, because a kind is one string. Every group whose pair set is declared next to its own payload model goes one step further: it is merely **unpacked** here, so the registry cannot hold a kind that vocabulary does not declare — the requirement revision, the supporting-record pair, the authored-effect family and, newest, the census's `CENSUS_PAYLOAD_MODELS`.
- The refusal is built through the package's shared `refusal(...)` factory with `RefusalFacts`, so
  this module contributes a code, a detail, facts and a next action — never a bespoke error shape.
- The module performs **no storage I/O at all**: it imports no connection type and takes no
  connection parameter, so it cannot write a row on any path.

### Invariants And Boundaries

- **Refusal means nothing was written and the digest did not move.** `invalid_payload` is a returned
  value with no row written and the before/after logical digest unchanged; a payload that fails
  validation never reaches the revision table.
- **`record_schema` is not a fingerprint.** It names which frozen shape the revision was written
  against. The envelope itself carries no content address, no logical digest and no fingerprint
  column, so nothing in it can be mistaken for a competing identity of the dataset or of a revision —
  and this module mints, derives and overrides no identity.
- **The registry is the only admissibility authority.** A write path that decided payload
  admissibility anywhere else would be a second definition of the same rule; the call site stores
  what this function returned instead.
- **Boundary.** This module does not own the envelope's *columns* (`schema_v2.py` declares them), does
  not own the record or revision operations that call it, does not own the governed-route association
  (`routes.py`), and does not decide which generation a dataset is (`schema_generations.py`).
  Endpoint-kind compatibility stays enforced by the typed join tables, not here: this module never
  becomes a registry that could make an unrestricted polymorphic edge possible.
- **Known gap, recorded rather than implied.** Only `ValidationError` is caught. A non-mapping
  `payload` raises `TypeError` from `dict(payload)`, and a non-string or unhashable `kind` raises
  `TypeError` at the registry lookup rather than returning a refusal. The declared contract is that
  inadmissible input yields `invalid_payload`; a caller passing a non-mapping payload is outside that
  contract today.

### Todos

None recorded. `EvidenceClaim` is no longer outstanding — it registered as one of the supporting-record
pair — and the registry now holds **22** `(kind, schema)` pairs over the families that have passed through
this seam: the internal conformance kind, the eight facet kinds, the two detection kinds, the
requirement-revision kind, the citation-binding kind, the evidence-claim and observation pair, the
authored-effect member kinds with their change set, and the census's inventory row, claim and disposition.
The standing open item is the refusal's known gap above, not a missing family.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one entry point, its pair-keyed registry and the derived kind-to-schema map; three refusal paths, one code. [1]
- The marked-internal conformance kind and the minimal frozen shape that exercises the seam. [2]
- **The registry every typed payload shape is registered in — the internal kind, the eight facet kinds, the detection pair, the requirement revision, the citation binding, the supporting-record pair, the authored-effect family and, newest, the census's three kinds unpacked from `CENSUS_PAYLOAD_MODELS`. Twenty-two pairs in all.** [3]
- The derived two-kind set that names the detection group without restating it. [4]
- The derived requirement-kind set, derived from the same declarations its registry entry is built from. [5]
- The requirement kind and its frozen shape, declared once in the vocabulary module the registry unpacks. [6]
- The derived kind-to-schema map, which is what makes a kind unable to admit a shape the registry does not hold. [7]
- The one entry point, its pair-keyed registry and the derived kind-to-schema map; three refusal paths, one code. [8]
- The marked-internal conformance kind and the minimal frozen shape that exercises the seam. [9]
- **The registry the two detection payload shapes are registered in, and the derived two-kind set that names them without restating them.** [10]
- The derived kind-to-schema map, which is what makes a kind unable to admit a shape the registry does not hold. [11]
- The frozen, strict, extra-forbidding base that makes a validated payload a value. [12]
- The requirement family this registry gained, its own declaration of the pair, and the payload model the pair resolves to. [13]
- The case that pins the registry as the union of all the declared groups, so a group the registry does not declare cannot be admitted without that line changing. [14]
- `invalid_payload` as a member of the shipped refusal vocabulary, and the shared refusal factory this module builds through. [15]
- The envelope table this seam validates payloads for: no identity-valued column, `record_schema` alongside `kind`, a nullable governing route. [16]
- The typed-JSON payload column and the immutability triggers that seal a validated revision. [17]
- The envelope and payload cases, including the five inadmissible inputs refused with `invalid_payload`. [18]
- **The census mapping the registry unpacks as its last entry — three `(kind, schema)` pairs declared beside the census's commands and payload models, so the registry cannot hold a census kind that vocabulary does not declare.** [19]
- **The site in this module where the census's three kinds join the one payload seam, with no value of their closed vocabularies named here.** [20]
- **The three frozen census payload shapes the census pairs resolve to, each declared once in the vocabulary module the registry unpacks.** [21]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
- **The registry the detection and citation-binding payload shapes are registered in, and the two derived sets that name them without restating them.** [22]
- **The citation-binding payload model this seam resolves the new kind to, and the binding facts that are payload rather than columns.** [23]
- **The case that measures the seam's membership after this leaf's registration: the kind union named in the seam registry, and its second additive re-scope that names this leaf's own group constant instead of trimming the expectation back.** [24]
