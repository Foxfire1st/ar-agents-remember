# mcp/src/agents_remember/memory/knowledge/record_envelope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/record_envelope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| lastVerifiedCommitDate | 2026-09-18T04:45:39+02:00|
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

**The registry now holds three disjoint record groups, and the third is the one this leaf's own
docstring used to defer.** The internal conformance kind, the eight authored-judgment facet kinds, and —
since `KS-R14@v1` — the two mechanical-detection kinds `detection_signal` and `detection_run`, which
resolve to the frozen payload models `models/knowledge/detection.py` declares. The docstring named
`DetectionSignal` as a later leaf's registration point; this is that leaf, so the sentence now names the
two kinds as registered rather than deferred, and `EvidenceClaim` is the category still outstanding.
Registering them here rather than as generation-4 columns is what keeps a signal's required field set,
its closed vocabularies and its construction refusals declared **once**: a second declaration as SQL
columns would be a second place for the same field set to drift.

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

- **One internal conformance kind, eight facet kinds and two detection kinds.** `INTERNAL_CONFORMANCE_KIND`
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
  `FACET_RECORD_KINDS` and `DETECTION_RECORD_KINDS` are each derived from their own entries, and
  `KIND_SCHEMAS` is derived from the whole registry, so no group's membership can drift from the
  registry it is a view of.
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

None recorded. `EvidenceClaim` and the other concrete non-facet categories remain later leaves; this card
records the seam they will register into, and the two detection kinds that have now registered through it.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point, its pair-keyed registry and the derived kind-to-schema map; three refusal paths, one code. | `validate_record_payload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:121-165 |
| The marked-internal conformance kind and the minimal frozen shape that exercises the seam. | `INTERNAL_CONFORMANCE_KIND` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:58-58 |
| **The registry the two detection payload shapes are registered in, and the derived two-kind set that names them without restating them.** | `PAYLOAD_MODELS`; `DETECTION_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:86-109 |
| The derived kind-to-schema map, which is what makes a kind unable to admit a shape the registry does not hold. | `KIND_SCHEMAS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:111-118 |
| The frozen, strict, extra-forbidding base that makes a validated payload a value. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| `invalid_payload` as a member of the shipped refusal vocabulary, and the shared refusal factory this module builds through. | `invalid_payload` | mcp/src/agents_remember/models/knowledge/result.py:82-147 |
| The envelope table this seam validates payloads for: no identity-valued column, `record_schema` alongside `kind`, a nullable governing route. | `record_schema`; `kind` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:53-72 |
| The typed-JSON payload column and the immutability triggers that seal a validated revision. | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-204 |
| The envelope and payload cases, including the five inadmissible inputs refused with `invalid_payload`. | `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-311 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read this card against the current source and recorded the change the leaf made to what it claims.** The body's "one internal conformance kind and no product kinds" convention and its Todos line both said the concrete non-facet categories were later leaves; `KS-R14@v1` registers the two mechanical-detection kinds, so both now state the registry's **three disjoint groups** (the internal conformance kind, the eight facet kinds, the two detection kinds) and name `EvidenceClaim` as the category still outstanding. The Purpose records why the detection payload shapes are registry entries rather than generation-4 columns: the frozen payload model *is* the shape, so a second declaration as SQL columns would be a second place for one field set to drift. Both stale citations were **re-cited by hand** rather than machine-projected — `validate_record_payload` moved with the inserted import block (`:69-113` → `:121-165`) and `INTERNAL_CONFORMANCE_KIND` moved with the module docstring (`:43` → `:58`) — and the **generated projection bullet that had produced the second of those ranges was removed**, because a projected range is unverified evidence and an agent has now read the declaration it points at. Two new rows record the registry and the derived kind set this leaf's entries join. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for the record envelope's payload seam. It records the pair-keyed registry and why the key is a pair rather than a schema alone, the single entry point that returns a validated value rather than a boolean, the three `invalid_payload` refusals with "no row written and the digest unchanged", the deliberately tiny internal conformance kind that keeps the product categories for later leaves, and the known gap that only a `ValidationError` is caught. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
