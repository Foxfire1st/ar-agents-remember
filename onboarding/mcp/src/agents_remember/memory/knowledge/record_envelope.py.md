# mcp/src/agents_remember/memory/knowledge/record_envelope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/record_envelope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
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

**The registry now holds four disjoint record groups, and each new one registered through the seam the
one before it established.** The internal conformance kind; the eight authored-judgment facet kinds;
since `KS-R14@v1` the two mechanical-detection kinds `detection_signal` and `detection_run`; and since
`KS-R19@v1` the requirement-revision kind `requirement_revision`, which resolves to
`RequirementRevisionPayload` in `models/knowledge/requirement.py`. The registry went from 12 kinds over
12 entries to **13 over 13** on that leaf, and it grew again the same way on the L19 change set. The
module docstring named `DetectionSignal` as a later leaf's registration point and that leaf has landed;
`EvidenceClaim` is the concrete non-facet category still outstanding.

**Four families, one seam, and the same reason each time.** None of these groups became a table or a
generation column: the frozen payload model *is* the shape, so a signal's required field set, its closed
vocabularies and its construction refusals stay declared **once**, in the model module that owns them.
A second declaration as SQL columns would be a second place for the same field set to drift, and
`REQUIREMENT_PAYLOAD_MODELS` is unpacked into `PAYLOAD_MODELS` rather than restated here for exactly
that reason — the registry and the vocabulary cannot disagree about which pairs exist.

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

### Conventions

- **One internal conformance kind, eight facet kinds, two detection kinds and the requirement kind.** `INTERNAL_CONFORMANCE_KIND`
  (`internal_conformance`) with `INTERNAL_CONFORMANCE_SCHEMA` (`internal-conformance/v1`) and its
  minimal `ConformancePayload` exist only to exercise the seam, so the typed half of the envelope has
  a mechanism rather than a promise. It is marked internal, it is **not** a knowledge category, and
  the later leaves that add the real categories (`EvidenceClaim`, …) add them
  *beside* it rather than replacing it. The detection pair was added that way:
  `(detection_signal, detection-signal/v1)` and `(detection_run, detection-run/v1)` are two ordinary
  registry entries whose models are the frozen payload models, and `DETECTION_RECORD_KINDS` is derived
  from the same declarations the entries are built from rather than restated — so the three groups are
  disjoint by construction, because a kind is one string.
- **A caller that must name what the registry holds uses the derived sets, not the mapping's keys.**
  `FACET_RECORD_KINDS`, `DETECTION_RECORD_KINDS` and `REQUIREMENT_RECORD_KINDS` are each derived from
  their own entries, and `KIND_SCHEMAS` is derived from the whole registry, so no group's membership
  can drift from the registry it is a view of. The requirement group goes one step further: its pair
  set is declared next to its payload model and merely **unpacked** here, so the registry cannot hold
  a requirement kind the vocabulary does not declare.
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

None recorded. `EvidenceClaim` remains the concrete non-facet category still outstanding; this card
records the seam a later leaf will register it into, and the four families that have registered through
it so far (the internal conformance kind, the eight facet kinds, the two detection kinds and the
requirement-revision kind).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point, its pair-keyed registry and the derived kind-to-schema map; three refusal paths, one code. | `validate_record_payload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:144-190 |
| The marked-internal conformance kind and the minimal frozen shape that exercises the seam. | `INTERNAL_CONFORMANCE_KIND`; `ConformancePayload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:71-78; mcp/src/agents_remember/memory/knowledge/record_envelope.py:82-82; mcp/src/agents_remember/memory/knowledge/record_envelope.py:81-81 |
| **The registry every typed payload shape is registered in — four families now, with the requirement pair unpacked from its own module rather than restated here.** | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-103 |
| The derived two-kind set that names the detection group without restating it. | `DETECTION_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:142-142; |
| The derived requirement-kind set, derived from the same declarations its registry entry is built from. | `REQUIREMENT_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:148-150 |
| The requirement kind and its frozen shape, declared once in the vocabulary module the registry unpacks. | `REQUIREMENT_REVISION_KIND`; `REQUIREMENT_REVISION_SCHEMA` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84 |
| The derived kind-to-schema map, which is what makes a kind unable to admit a shape the registry does not hold. | `KIND_SCHEMAS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:160-165 |
| The frozen, strict, extra-forbidding base that makes a validated payload a value. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The requirement family this registry gained, its own declaration of the pair, and the payload model the pair resolves to. | `RequirementRevisionPayload`; `REQUIREMENT_REVISION_KIND` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84; mcp/src/agents_remember/models/knowledge/requirement.py:172-213 |
| The case that pins the registry as the union of all four groups, so a group the registry does not declare cannot be admitted without that line changing. | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes" | mcp/tests/test_knowledge_facets.py:183-247 |
| `invalid_payload` as a member of the shipped refusal vocabulary, and the shared refusal factory this module builds through. | `invalid_payload` | mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| The envelope table this seam validates payloads for: no identity-valued column, `record_schema` alongside `kind`, a nullable governing route. | `record_schema`; `kind` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:53-72 |
| The typed-JSON payload column and the immutability triggers that seal a validated revision. | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-204 |
| The envelope and payload cases, including the five inadmissible inputs refused with `invalid_payload`. | `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-311 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
| **The registry the detection and citation-binding payload shapes are registered in, and the two derived sets that name them without restating them.** | `PAYLOAD_MODELS`; `DETECTION_RECORD_KINDS`; `CITATION_BINDING_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:155-155; mcp/src/agents_remember/memory/knowledge/record_envelope.py:144-144; mcp/src/agents_remember/memory/knowledge/record_envelope.py:157-157; mcp/src/agents_remember/memory/knowledge/record_envelope.py:156-156; mcp/src/agents_remember/memory/knowledge/record_envelope.py:143-143; mcp/src/agents_remember/memory/knowledge/record_envelope.py:142-142; mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-103 |
| **The citation-binding payload model this seam resolves the new kind to, and the binding facts that are payload rather than columns.** | `CitationBindingPayload`; `BINDING_RECORD_KIND`; `BINDING_RECORD_SCHEMA` | mcp/src/agents_remember/models/knowledge/citation.py:353-374; mcp/src/agents_remember/models/knowledge/citation.py:127-128 |
| **The case that measures the seam's membership after this leaf's registration: the kind union named in the seam registry, and its second additive re-scope that names this leaf's own group constant instead of trimming the expectation back.** | `test_the_seam_registry_is_exactly_the_eight_declared_subtypes` | mcp/tests/test_knowledge_facets.py:183-246 |

## Update History
- 2026-09-18T06:09:03+00:00: Generated citation repair: `REQUIREMENT_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:148-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 014df62463362d92ea768ade7d81f0ca0b615347d5c6feed94e130d80244a24d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:09:03+00:00: Generated citation repair: `KIND_SCHEMAS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:160-165. No content impact: mechanical anchor-range projection bound to citation source snapshot 014df62463362d92ea768ade7d81f0ca0b615347d5c6feed94e130d80244a24d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:50+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `a0665505`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the range now recorded in the row above is the one that holds its anchor. Claims re-read (by their full anchor sets): `CITATION_BINDING_RECORD_KINDS`; `DETECTION_RECORD_KINDS`; `PAYLOAD_MODELS`. No claim wording changed; verification metadata advances to the landed base because the claims were re-read against the current source.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `REQUIREMENT_RECORD_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:149-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `KIND_SCHEMAS` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:161-166. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:30+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **re-read this card against the current source and recorded the fourth family the registry gained, then retired the generated projection bullets by hand.** The body said the registry holds *three* disjoint groups and named only the detection pair as this leaf's own addition; `KS-R19@v1` registers `(requirement_revision, requirement-revision/v1)` resolving to `RequirementRevisionPayload`, so the Purpose and the group convention now state **four** families and record the general rule the middle two share — the unpacked pair set means the registry cannot hold a requirement kind the vocabulary does not declare, and no family became a table or a generation column. The retired bullets are replaced by rows an agent has actually read: `INTERNAL_CONFORMANCE_KIND` is re-cited at its own declaration (`:65`, and the earlier projection to `:65` was the one range the tool got right while its neighbours were stale), `PAYLOAD_MODELS` is now one anchor at `:93-113` instead of a pair sharing a projected range, `DETECTION_RECORD_KINDS` is narrowed to `:124`, and `REQUIREMENT_RECORD_KINDS` with `REQUIREMENT_PAYLOAD_MODELS` is a new row. `KIND_SCHEMAS` and `validate_record_payload` were **re-derived rather than carried**: the module grew its import block and its registry, so the entry point moved to `:144-190` and the derived map to `:136-141`. A row for the registry case that pins the union of all four groups is added, since that case is what makes a fifth group unable to be admitted silently. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read this card against the current source and recorded the fourth record group the leaf registered.** `KS-R18@v1` adds `(citation_binding, citation-binding/v1)` to the one payload seam, so the Purpose, the Conventions bullet, the derived-sets bullet and the Todos line all now state the registry's **four** disjoint groups (the internal conformance kind, the eight facet kinds, the two detection kinds, the citation-binding kind) and name `EvidenceClaim` as the one category still deferred. The Purpose additionally records the pattern the leaf makes explicit — a record group registers its payload shape at this seam and appends to a generation only what the envelope cannot express — because `memory/knowledge/` now holds two groups that follow it (the detection pair from `KS-R14@v1` and the binding here), and the binding is the clearest case: its three authored record facts are payload while its identity pair and governing route are columns. Three stale citation ranges were **re-cited by hand** rather than machine-projected (`validate_record_payload` `:121-165` → `:145-190`, `KIND_SCHEMAS` `:111-137` → `:137-143`, and the registry row re-split so the detection and binding sets are cited separately), and one new row records the payload model the new kind resolves to plus the seam-membership case that names it. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read this card against the current source and recorded the change the leaf made to what it claims.** The body's "one internal conformance kind and no product kinds" convention and its Todos line both said the concrete non-facet categories were later leaves; `KS-R14@v1` registers the two mechanical-detection kinds, so both now state the registry's **three disjoint groups** (the internal conformance kind, the eight facet kinds, the two detection kinds) and name `EvidenceClaim` as the category still outstanding. The Purpose records why the detection payload shapes are registry entries rather than generation-4 columns: the frozen payload model *is* the shape, so a second declaration as SQL columns would be a second place for one field set to drift. Both stale citations were **re-cited by hand** rather than machine-projected — `validate_record_payload` moved with the inserted import block (`:69-113` → `:121-165`) and `INTERNAL_CONFORMANCE_KIND` moved with the module docstring (`:43` → `:58`) — and the **generated projection bullet that had produced the second of those ranges was removed**, because a projected range is unverified evidence and an agent has now read the declaration it points at. Two new rows record the registry and the derived kind set this leaf's entries join. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for the record envelope's payload seam. It records the pair-keyed registry and why the key is a pair rather than a schema alone, the single entry point that returns a validated value rather than a boolean, the three `invalid_payload` refusals with "no row written and the digest unchanged", the deliberately tiny internal conformance kind that keeps the product categories for later leaves, and the known gap that only a `ValidationError` is caught. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
