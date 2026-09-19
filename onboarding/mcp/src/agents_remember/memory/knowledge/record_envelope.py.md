# mcp/src/agents_remember/memory/knowledge/record_envelope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/record_envelope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate |  2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point, its pair-keyed registry and the derived kind-to-schema map; three refusal paths, one code. | `validate_record_payload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:245-289 |
| The marked-internal conformance kind and the minimal frozen shape that exercises the seam. | `INTERNAL_CONFORMANCE_KIND`; `ConformancePayload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:110-110; mcp/src/agents_remember/memory/knowledge/record_envelope.py:111-118 |
| **The registry every typed payload shape is registered in — the internal kind, the eight facet kinds, the detection pair, the requirement revision, the citation binding, the supporting-record pair, the authored-effect family and, newest, the census's three kinds unpacked from `CENSUS_PAYLOAD_MODELS`. Twenty-two pairs in all.** | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:131-192 |
| The derived two-kind set that names the detection group without restating it. | `DETECTION_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:204-204 |
| The derived requirement-kind set, derived from the same declarations its registry entry is built from. | `REQUIREMENT_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:211-213 |
| The requirement kind and its frozen shape, declared once in the vocabulary module the registry unpacks. | `REQUIREMENT_REVISION_KIND`; `REQUIREMENT_REVISION_SCHEMA` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84 |
| The derived kind-to-schema map, which is what makes a kind unable to admit a shape the registry does not hold. | `KIND_SCHEMAS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:245-250 |
| The one entry point, its pair-keyed registry and the derived kind-to-schema map; three refusal paths, one code. | `validate_record_payload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:245-289 |
|The marked-internal conformance kind and the minimal frozen shape that exercises the seam.|`INTERNAL_CONFORMANCE_KIND`| mcp/src/agents_remember/memory/knowledge/record_envelope.py:110-118 |
| **The registry the two detection payload shapes are registered in, and the derived two-kind set that names them without restating them.** | `PAYLOAD_MODELS`; `DETECTION_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:131-192; mcp/src/agents_remember/memory/knowledge/record_envelope.py:204-204 |
| The derived kind-to-schema map, which is what makes a kind unable to admit a shape the registry does not hold. | `KIND_SCHEMAS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:245-250 |
| The frozen, strict, extra-forbidding base that makes a validated payload a value. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The requirement family this registry gained, its own declaration of the pair, and the payload model the pair resolves to. | `RequirementRevisionPayload`; `REQUIREMENT_REVISION_KIND` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84; mcp/src/agents_remember/models/knowledge/requirement.py:172-213 |
| The case that pins the registry as the union of all the declared groups, so a group the registry does not declare cannot be admitted without that line changing. | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes" | mcp/tests/test_knowledge_facets.py:183-247 |
| `invalid_payload` as a member of the shipped refusal vocabulary, and the shared refusal factory this module builds through. | `invalid_payload` | mcp/src/agents_remember/models/knowledge/result.py:162-162 |
| The envelope table this seam validates payloads for: no identity-valued column, `record_schema` alongside `kind`, a nullable governing route. | `record_schema`; `kind` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:53-72 |
| The typed-JSON payload column and the immutability triggers that seal a validated revision. | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-204 |
| The envelope and payload cases, including the five inadmissible inputs refused with `invalid_payload`. | `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-311 |
| **The census mapping the registry unpacks as its last entry — three `(kind, schema)` pairs declared beside the census's commands and payload models, so the registry cannot hold a census kind that vocabulary does not declare.** | `CENSUS_PAYLOAD_MODELS` | mcp/src/agents_remember/models/knowledge/census.py:346-350 |
| **The site in this module where the census's three kinds join the one payload seam, with no value of their closed vocabularies named here.** | `CENSUS_PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:191-191 |
| **The three frozen census payload shapes the census pairs resolve to, each declared once in the vocabulary module the registry unpacks.** | `CensusInventoryRowPayload`; `CensusClaimPayload`; `CensusDispositionPayload` | mcp/src/agents_remember/models/knowledge/census.py:147-192; mcp/src/agents_remember/models/knowledge/census.py:195-219; mcp/src/agents_remember/models/knowledge/census.py:222-236 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
| **The registry the detection and citation-binding payload shapes are registered in, and the two derived sets that name them without restating them.** | `PAYLOAD_MODELS`; `DETECTION_RECORD_KINDS`; `CITATION_BINDING_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:131-192; mcp/src/agents_remember/memory/knowledge/record_envelope.py:204-204; mcp/src/agents_remember/memory/knowledge/record_envelope.py:219-219 |
| **The citation-binding payload model this seam resolves the new kind to, and the binding facts that are payload rather than columns.** | `CitationBindingPayload`; `BINDING_RECORD_KIND`; `BINDING_RECORD_SCHEMA` | mcp/src/agents_remember/models/knowledge/citation.py:353-374; mcp/src/agents_remember/models/knowledge/citation.py:127-128 |
| **The case that measures the seam's membership after this leaf's registration: the kind union named in the seam registry, and its second additive re-scope that names this leaf's own group constant instead of trimming the expectation back.** | `test_the_seam_registry_is_exactly_the_eight_declared_subtypes` | mcp/tests/test_knowledge_facets.py:183-246 |

## Update History
- 2026-09-18T17:54:55+00:00: 260915-KS-L23 residue clearance (seat A): `INTERNAL_CONFORMANCE_KIND` repointed from `record_envelope.py:105-105` to `record_envelope.py:110-110` (and its second copy from `:105-118` to `:110-118`) — the new range holds `INTERNAL_CONFORMANCE_KIND = "internal_conformance"` and the frozen `ConformancePayload` it resolves to, instead of the docstring lines above them; `PAYLOAD_MODELS` repointed from `record_envelope.py:133-187` to `record_envelope.py:131-192` in all three rows — the new range is the whole pair-keyed registry, from its first comment line through the closing brace after `**CENSUS_PAYLOAD_MODELS`, and it holds the anchor the stale range stopped short of; `DETECTION_RECORD_KINDS` repointed from `:198-198` to `:204-204` in two rows — the new range holds the derived two-kind set itself rather than the comment above it; `CITATION_BINDING_RECORD_KINDS` repointed from `:211-211` to `:219-219` — the new range holds the derived binding-kind set rather than the earlier group's set; `CENSUS_PAYLOAD_MODELS` repointed from `:179-186` to `:191-191` — the new range holds the `**CENSUS_PAYLOAD_MODELS` unpacking line where the census's three kinds join the seam, rather than the comment block above it. Claim re-read against each construct, wording unchanged. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `DETECTION_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `REQUIREMENT_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:211-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `KIND_SCHEMAS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:245-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `KIND_SCHEMAS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:245-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:30+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **corrected the derived-sets convention to what the module’s comments now say.** The five comments above the derived kind sets (`record_envelope.py:198-238`) each used to restate a *different, incomplete* list of the groups the registry holds — the last of them still missed the supporting-record pair, the effect kinds, the change set and the census — and all five now read that a caller naming the registry's membership reads `PAYLOAD_MODELS` above, while keeping the fact they were there for (the derived sets are disjoint by construction because a kind is one string). The card's Conventions bullet said the opposite ("uses the derived sets, not the mapping's keys"), so it was rewritten to the mapping-as-membership-authority rule with the drift that motivated it, and the unpacking half is retained verbatim. The module docstring's own membership headline ("twenty-two kind/schema pairs", the nine blocks by name, nothing deferred) was corrected by `260915-KS-L21` and the card already states it, so nothing else in the body moved. No row, citation or range was added or rewritten, and no verification stamp advanced (the source is uncommitted and closeout owns the stamp).
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): **re-read every citation this card carries against the staged working candidate and recorded the census record group's registration at the payload seam.** The leaf unpacks `**CENSUS_PAYLOAD_MODELS` into `PAYLOAD_MODELS` as the mapping's last entry, so the registry now holds **twenty-two** `(kind, schema)` pairs rather than the "13 over 13" and "four families" this card still stated; the Purpose registry paragraph, the "four families, one seam" paragraph, the group convention and the Todos line were each **rewritten to the current families by name** — the internal conformance kind, the eight facet kinds, the detection pair, the requirement revision, the citation binding, the supporting-record pair, the authored-effect family and the census's three — and the stale claim that `EvidenceClaim` is still outstanding was corrected, since it registered as one of the supporting-record pair. A new Logic paragraph records what the census registration buys: the three pairs resolve to `CensusInventoryRowPayload`, `CensusClaimPayload` and `CensusDispositionPayload`, and no value of their closed vocabularies (a parse outcome, a claim kind, an applicability, a disposition kind) is named in this module, so a category or an import-derived status is not something the seam could store *or* refuse for the wrong reason. The derived-sets convention now names all five group constants plus `KIND_SCHEMAS`, and the unpacking rule is stated for every family that declares its pair set beside its own model rather than for the requirement group alone. Nine rows whose cited ranges this leaf's import line and registry entry had moved were **re-cited by hand to each construct's declaration extent** — `validate_record_payload` (both copies), `INTERNAL_CONFORMANCE_KIND`/`ConformancePayload`, `PAYLOAD_MODELS` (three rows), `DETECTION_RECORD_KINDS`, `REQUIREMENT_RECORD_KINDS` and `KIND_SCHEMAS` — and three rows were added for the census mapping, this module's registration site and the three frozen census payload shapes. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T12:07:24+00:00: Generated citation repair: `invalid_payload` repointed to mcp/src/agents_remember/models/knowledge/result.py:162-162. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `validate_record_payload` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:236-280. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `DETECTION_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:189-189. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `REQUIREMENT_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:195-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `KIND_SCHEMAS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:228-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `validate_record_payload` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:236-280. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `INTERNAL_CONFORMANCE_KIND` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:104-104. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `KIND_SCHEMAS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:228-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `invalid_payload` repointed to mcp/src/agents_remember/models/knowledge/result.py:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 2 claim(s) here (2 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `PAYLOAD_MODELS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:118-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand while resolving the memory sync** — `REQUIREMENT_RECORD_KINDS`, `KIND_SCHEMAS`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:50:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `a0665505`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the range now recorded in the row above is the one that holds its anchor. Claims re-read (by their full anchor sets): `CITATION_BINDING_RECORD_KINDS`; `DETECTION_RECORD_KINDS`; `PAYLOAD_MODELS`. No claim wording changed; verification metadata advances to the landed base because the claims were re-read against the current source.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the two kinds that complete the deferred set, the derived `EVIDENCE_RECORD_KINDS`, and why a claim's subject and coverage are relations rather than payload fields. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T04:30:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **re-read this card against the current source and recorded the fourth family the registry gained, then retired the generated projection bullets by hand.** The body said the registry holds *three* disjoint groups and named only the detection pair as this leaf's own addition; `KS-R19@v1` registers `(requirement_revision, requirement-revision/v1)` resolving to `RequirementRevisionPayload`, so the Purpose and the group convention now state **four** families and record the general rule the middle two share — the unpacked pair set means the registry cannot hold a requirement kind the vocabulary does not declare, and no family became a table or a generation column. The retired bullets are replaced by rows an agent has actually read: `INTERNAL_CONFORMANCE_KIND` is re-cited at its own declaration (`:65`, and the earlier projection to `:65` was the one range the tool got right while its neighbours were stale), `PAYLOAD_MODELS` is now one anchor at `:93-113` instead of a pair sharing a projected range, `DETECTION_RECORD_KINDS` is narrowed to `:124`, and `REQUIREMENT_RECORD_KINDS` with `REQUIREMENT_PAYLOAD_MODELS` is a new row. `KIND_SCHEMAS` and `validate_record_payload` were **re-derived rather than carried**: the module grew its import block and its registry, so the entry point moved to `:144-190` and the derived map to `:136-141`. A row for the registry case that pins the union of all four groups is added, since that case is what makes a fifth group unable to be admitted silently. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read this card against the current source and recorded the fourth record group the leaf registered.** `KS-R18@v1` adds `(citation_binding, citation-binding/v1)` to the one payload seam, so the Purpose, the Conventions bullet, the derived-sets bullet and the Todos line all now state the registry's **four** disjoint groups (the internal conformance kind, the eight facet kinds, the two detection kinds, the citation-binding kind) and name `EvidenceClaim` as the one category still deferred. The Purpose additionally records the pattern the leaf makes explicit — a record group registers its payload shape at this seam and appends to a generation only what the envelope cannot express — because `memory/knowledge/` now holds two groups that follow it (the detection pair from `KS-R14@v1` and the binding here), and the binding is the clearest case: its three authored record facts are payload while its identity pair and governing route are columns. Three stale citation ranges were **re-cited by hand** rather than machine-projected (`validate_record_payload` `:121-165` → `:145-190`, `KIND_SCHEMAS` `:111-137` → `:137-143`, and the registry row re-split so the detection and binding sets are cited separately), and one new row records the payload model the new kind resolves to plus the seam-membership case that names it. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read this card against the current source and recorded the change the leaf made to what it claims.** The body's "one internal conformance kind and no product kinds" convention and its Todos line both said the concrete non-facet categories were later leaves; `KS-R14@v1` registers the two mechanical-detection kinds, so both now state the registry's **three disjoint groups** (the internal conformance kind, the eight facet kinds, the two detection kinds) and name `EvidenceClaim` as the category still outstanding. The Purpose records why the detection payload shapes are registry entries rather than generation-4 columns: the frozen payload model *is* the shape, so a second declaration as SQL columns would be a second place for one field set to drift. Both stale citations were **re-cited by hand** rather than machine-projected — `validate_record_payload` moved with the inserted import block (`:69-113` → `:121-165`) and `INTERNAL_CONFORMANCE_KIND` moved with the module docstring (`:43` → `:58`) — and the **generated projection bullet that had produced the second of those ranges was removed**, because a projected range is unverified evidence and an agent has now read the declaration it points at. Two new rows record the registry and the derived kind set this leaf's entries join. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for the record envelope's payload seam. It records the pair-keyed registry and why the key is a pair rather than a schema alone, the single entry point that returns a validated value rather than a boolean, the three `invalid_payload` refusals with "no row written and the digest unchanged", the deliberately tiny internal conformance kind that keeps the product categories for later leaves, and the known gap that only a `ValidationError` is caught. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
