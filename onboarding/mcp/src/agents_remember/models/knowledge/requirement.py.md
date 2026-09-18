# mcp/src/agents_remember/models/knowledge/requirement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/requirement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:15+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Requirement *meaning* gets a database home, never a second task authority.** This module owns the
frozen payload vocabulary of the requirement-revision record group: one record identity per
requirement obligation, holding immutable revisions — which is why it adds **no** table, **no** second
envelope, **no** second revision aggregate and **no** identity mechanism of its own.

It declares the envelope's **fourth** typed kind family: `(requirement_revision,
requirement-revision/v1)` resolving to `RequirementRevisionPayload`, registered by
`record_envelope.PAYLOAD_MODELS` under the same idiom the facet kinds and the two detection kinds use.

**The quotation-degree ruling lives here, beside the shape it governs.** `KS-R19@v1`'s Open Truth Gap 3
left open how much of an obligation's own text a self-contained explanation may quote, and carried
finding `CR19-5` required a *recorded ruling before the payload schema was frozen* rather than a guess
embedded in it. The ruling is reproduced in this module's docstring: **no quotation-degree policy is
encoded in the schema.** The schema holds one attributed, nonempty `explanation` and refuses an empty
or absent one; it holds **no field that is the operative obligation**. The degree is an authoring
discipline carried by attribution plus that absence, not a schema rule, because policing the degree
would require comparing the field against the owner's packet bytes — and requirement 2.3 forbids the
substrate from treating the packet as an operand at all. The sentence an author is bound by: *the
explanation is attributed, self-contained, and never the text another system implements against.*

## Code Commentary

### Logic

- **Three components, spelled the owner's way.** `RequirementOwnerRef` (116-137) carries exactly
  `path`, `stableId` and `version` — `ApprovedRequirementPacketRef`'s own field names, so the two
  planes compare literally rather than through a translation that could disagree. `extra="forbid"` is
  what refuses a fourth addressing scheme: there is no field for a UUID or a content address to arrive
  in. **The payload does not police the reference**: it bounds the three components and does not
  confine the path to a task root, require a `.md` suffix, or read the packet's metadata rows. Those
  are the owner's refusals, and a substrate that pre-refused them would substitute its own answer for
  the owner's, which requirement 2.3 forbids in terms.
- **The version spelling is the task plane's own.** `REQUIREMENT_PACKET_VERSION_PATTERN` (90) is the
  same `^v[1-9][0-9]*$` the owner's reference declares, written once here as the same pattern rather
  than a second, wider one — two admitted spellings for one version is exactly the drift requirement
  2.2 forbids.
- **The resolution is consumed, never re-derived.** `RequirementOwnerResolution` (140-169) holds one
  outcome: `resolved` carries no refusal fields, `unresolved` carries the owner's own `refusal_code`
  and `refusal_detail` verbatim. Nothing in this record group constructs either value, so a store can
  never report an owner's refusal the owner did not give. The resolution carries **no components of
  its own** — the reference it is about is the record's one `owner` field, which is never rewritten by
  a resolution, so a resolution cannot disagree with the reference it resolves.
- **State and acceptance are the shipped pair, not a new one.** `RequirementRevisionPayload`
  (172-211) carries `state_at_origin` and `acceptance_ref` and delegates the consistency rule to the
  package's shared `require_consistent_acceptance` (193-196), so a requirement revision is checked
  exactly as a generation-1 `InvariantRevision`/`FamilyRevision` and an L11 facet envelope are.
- **The explanation refusal is by value, not by length.** `min_length=1` alone would admit a
  whitespace-only body; `_require_an_explanation_that_says_something` (198-211) refuses one that is
  empty after trimming, with the reason stated in the error: a pointer without meaning is not this
  record.
- **Currentness is derived, and a disagreement is not resolved.** `RequirementCurrentness` (232-268)
  requires `state` to equal the value derived from the two recorded pairs — asserting `aligned` against
  values that disagree raises at construction — and carries both states with their provenance rather
  than a winner.
- **The four derived views are declared here, computed in `memory/knowledge/requirement_views.py`.**
  `RequirementRevisionView`, `RequirementPredecessorChainView`, `RequirementGoverningRouteView` and
  `RequirementCurrentStateView` (271-339) are the shapes the read half returns; `RequirementRevisionScope`
  (340-360) is the one projection value. `ungoverned` is an explicit state held by
  `RequirementGoverningRouteView` (312-320), never a default.
- **The receipt is one outcome, not two nullable halves.** `RequirementRevisionResult` (389-408)
  requires a refused result to carry a refusal **and no scope**, and a served result to carry a scope
  **and no refusal**; `RequirementReferenceResolution` (409-433) requires `resolved` to name exactly
  one record, `unresolved` none and `ambiguous` more than one.

### Conventions

- `REQUIREMENT_RECORD_LIFECYCLE = "proposed"` (96) is the lifecycle every requirement revision is
  written under. A requirement revision recorded by this record group is a **record of** the owner's
  obligation, not an approval of it, so the envelope declares the proposed lifecycle exactly as an
  authored facet and a detection record do; the owner's own acceptance state travels in the payload's
  `state_at_origin`.
- `RequirementRevisionOperation` (383-386) is a **narrow local literal, not a second vocabulary**: both
  names are members of the shipped `KnowledgeOperation`, and the test suite asserts that subset
  relation rather than an exact set.
- Every model here inherits `KnowledgeModel` — strict, extra-forbidding, frozen — so a validated
  payload is a value and an undeclared field is refused by the ordinary `extra="forbid"` rule rather
  than by a named denylist. That matters for the absence claims: **there is no denylist to relax.**
- `requirement_owner_reference` (434-452) reads a stored payload's `owner` mapping and returns `None`
  rather than raising for a mapping that is absent, non-mapping or malformed.

### Invariants And Boundaries

- **No field of this payload can be an operative obligation.** The payload holds no
  `obligation_text`, `requirement_text`, `title` or `display_version`, and no registered generation
  declares a column for such a value. The absence is asserted falsifiably at both planes: the
  payload-level case parametrizes over those four names and requires `invalid_payload` with the name in
  the refusal detail, and the schema-plane case re-derives the column census over every registered
  generation.
- **No field of this payload can carry task authority.** There is no task status, seat owner, lifecycle
  gate, `implemented` or `approved_by_substrate` field, and a stored row hand-sealed with one raises
  rather than decoding.
- **No field of this payload can substitute for authorship.** Provenance rides
  `record_revision.provenance`, so `actor_ref`, `authorization_ref`, `operation_id` and `recorded_at`
  are all refused as `invalid_payload` — a payload that carried one would be a second competing author.
- **Boundary.** This module does not own the registry (`record_envelope.py`), the row codecs
  (`memory/knowledge/requirement_records.py`), the derived views' computation
  (`memory/knowledge/requirement_views.py`), the operation surface (`memory/knowledge/requirements.py`)
  or the task-plane boundary (`memory/knowledge/requirement_owner.py`).

### Todos

None recorded. `EvidenceClaim` remains the concrete non-facet category still outstanding in the
envelope registry; this module registered the fourth family and did not close that gap.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The recorded quotation-degree ruling, reproduced verbatim beside the frozen shape it governs.** | `RequirementRevisionPayload` | mcp/src/agents_remember/models/knowledge/requirement.py:172-213 |
| The one kind and the one frozen shape the record group declares in the envelope's typed vocabulary. | `REQUIREMENT_REVISION_KIND`; `REQUIREMENT_REVISION_SCHEMA` | mcp/src/agents_remember/models/knowledge/requirement.py:80-84 |
| The version spelling taken from the task plane's own pattern rather than widened into a second admitted form. | `REQUIREMENT_PACKET_VERSION_PATTERN` | mcp/src/agents_remember/models/knowledge/requirement.py:86-90 |
| The proposed lifecycle every requirement revision is written under, and why the payload's own state travels beside it. | `REQUIREMENT_RECORD_LIFECYCLE` | mcp/src/agents_remember/models/knowledge/requirement.py:92-96 |
|**The owner reference in the task plane's own three components, with `extra="forbid"` as the fourth-addressing-scheme refusal.**|`RequirementOwnerRef`| mcp/src/agents_remember/models/knowledge/requirement.py:116-139 |
|The resolution consumed rather than re-derived: one outcome, and the owner's own refusal fields verbatim.|`RequirementOwnerResolution`| mcp/src/agents_remember/models/knowledge/requirement.py:140-171 |
|**The payload's whole field set — and the absence of any operative-obligation field.**|`RequirementRevisionPayload`| mcp/src/agents_remember/models/knowledge/requirement.py:172-213 |
| The explanation refused by value, so a whitespace-only body is refused rather than admitted by `min_length=1`. | `_require_an_explanation_that_says_something` | mcp/src/agents_remember/models/knowledge/requirement.py:198-211 |
|The currentness value whose `state` must equal the value derived from the two recorded pairs.|`RequirementCurrentness`| mcp/src/agents_remember/models/knowledge/requirement.py:232-270 |
|The ungoverned route as an explicit state rather than a default.|`RequirementGoverningRouteView`| mcp/src/agents_remember/models/knowledge/requirement.py:300-322 |
| The one projection value the read half returns. | `RequirementRevisionScope` | mcp/src/agents_remember/models/knowledge/requirement.py:340-360 |
| The two-operation local literal, asserted to be a subset of the shipped vocabulary rather than a second one. | `RequirementRevisionOperation` | mcp/src/agents_remember/models/knowledge/requirement.py:383-386 |
| The receipt's one-outcome rule, and the reference resolution's 1 / 0 / at-least-2 rule. | `RequirementRevisionResult`; `RequirementReferenceResolution` | mcp/src/agents_remember/models/knowledge/requirement.py:389-408; mcp/src/agents_remember/models/knowledge/requirement.py:409-433 |
| The payload shapes declared beside the models, so the envelope registry and this vocabulary cannot drift. | `REQUIREMENT_PAYLOAD_MODELS` | mcp/src/agents_remember/models/knowledge/requirement.py:454-459; mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-103 |
|The shared state/acceptance consistency rule this payload delegates to rather than restating.|`require_consistent_acceptance`| mcp/src/agents_remember/models/knowledge/base.py:40-58 |
|The strict, extra-forbidding, frozen base that makes an undeclared field a refusal by construction — the reason the absence claims need no denylist.|`KnowledgeModel`| mcp/src/agents_remember/models/knowledge/base.py:34-39 |
|The owner's own reference shape, which this module deliberately re-spells rather than translates.|`ApprovedRequirementPacketRef`| mcp/src/agents_remember/models/task_intent/__init__.py:22-38 |
| The registry this payload shape is admitted through, and the derived kind set that names its group. | `PAYLOAD_MODELS`; `REQUIREMENT_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:148-148; mcp/src/agents_remember/memory/knowledge/record_envelope.py:150-174; mcp/src/agents_remember/memory/knowledge/record_envelope.py:149-149; mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-118; mcp/src/agents_remember/memory/knowledge/record_envelope.py:85-85 |
| **The falsifiable absence at the payload plane: four forbidden operative-obligation names, each refused with the name in the detail.** | "test_a_payload_carrying_an_operative_obligation_field_is_refused" | mcp/tests/test_knowledge_requirement_reference_contract.py:294-310 |
| The falsifiable absence at the schema plane: the re-derived column census over every registered generation, and the fact that the kind is not a table. | "test_no_registered_generation_declares_a_column_for_the_forbidden_set" | mcp/tests/test_knowledge_requirement_reference_contract.py:311-333 |
| The task-authority absence, and the hand-sealed forbidden row that cannot be decoded. | "test_a_payload_carrying_a_forbidden_task_authority_field_is_refused"; "test_a_stored_payload_carrying_a_forbidden_field_could_not_be_decoded" | mcp/tests/test_knowledge_requirement_reference_contract.py:277-293; mcp/tests/test_knowledge_requirement_reference_contract.py:334-365 |
| The three-component shape, the admitted version spelling, and the reference the payload deliberately does not police. | "test_the_owner_reference_carries_exactly_the_task_planes_three_components"; "test_a_version_outside_the_admitted_spelling_is_refused"; "test_the_payload_does_not_police_the_reference_the_owner_owns" | mcp/tests/test_knowledge_requirement_reference_contract.py:222-248; mcp/tests/test_knowledge_requirement_reference_contract.py:249-258; mcp/tests/test_knowledge_requirement_reference_contract.py:259-276 |
| The state/consistency and explanation cases, including the authorship-substitution refusals. | "test_an_accepted_origin_state_without_an_acceptance_reference_is_refused"; "test_a_proposed_origin_state_carrying_an_acceptance_reference_is_refused"; "test_an_empty_or_absent_explanation_is_refused"; "test_no_payload_field_can_substitute_for_the_revisions_authorship" | mcp/tests/test_knowledge_requirement_revisions.py:225-234; mcp/tests/test_knowledge_requirement_revisions.py:235-246; mcp/tests/test_knowledge_requirement_revisions.py:315-325; mcp/tests/test_knowledge_requirement_revisions.py:326-341 |
| The membership case that keeps the local operation literal a subset rather than a second vocabulary. | "test_the_record_group_declares_two_operations_beside_the_shipped_vocabulary" | mcp/tests/test_knowledge_requirement_revisions.py:213-224 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T04:15:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): created this one-to-one card for the requirement record group's payload vocabulary. It records the **recorded `CR19-5` quotation-degree ruling** where the finding asked for it — beside the frozen shape it governs — and states its substance rather than just its existence: no quotation-degree policy is in the schema, the degree is an authoring discipline carried by attribution plus the absence of any operative-obligation field, and the reason is that policing the degree would require comparing the field against the owner's packet bytes, the operand requirement 2.3 forbids the substrate to treat as one. It states that the payload's **whole field set is `requirement_kind`, `owner`, `owner_resolution`, `explanation`, `state_at_origin` and `acceptance_ref`** — there is no stored `obligation_text` or `requirement_text`, and the absence is falsifiable at both planes rather than merely true. It also records three boundaries a reader is likely to misread: the payload **does not police the reference** the owner owns (a path the owner would refuse is still representable, so the refusal can only come from the owner); the version spelling is the task plane's own pattern rather than a second admitted form; and `state_at_origin` / `acceptance_ref` are the **shipped** pair validated by the shared `require_consistent_acceptance`, not a new state mechanism. Verification metadata advances to the leaf's base commit `e963a01c` because the body was read against the current source; the code commit does not exist yet and closeout owns that stamp.
