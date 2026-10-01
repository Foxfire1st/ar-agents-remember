# mcp/src/agents_remember/models/knowledge/requirement.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The recorded quotation-degree ruling, reproduced verbatim beside the frozen shape it governs.** [1]
- The one kind and the one frozen shape the record group declares in the envelope's typed vocabulary. [2]
- The version spelling taken from the task plane's own pattern rather than widened into a second admitted form. [3]
- The proposed lifecycle every requirement revision is written under, and why the payload's own state travels beside it. [4]
- **The owner reference in the task plane's own three components, with `extra="forbid"` as the fourth-addressing-scheme refusal.** [5]
- The resolution consumed rather than re-derived: one outcome, and the owner's own refusal fields verbatim. [6]
- **The payload's whole field set — and the absence of any operative-obligation field.** [7]
- The explanation refused by value, so a whitespace-only body is refused rather than admitted by `min_length=1`. [8]
- The currentness value whose `state` must equal the value derived from the two recorded pairs. [9]
- The ungoverned route as an explicit state rather than a default. [10]
- The one projection value the read half returns. [11]
- The two-operation local literal, asserted to be a subset of the shipped vocabulary rather than a second one. [12]
- The receipt's one-outcome rule, and the reference resolution's 1 / 0 / at-least-2 rule. [13]
- The payload shapes declared beside the models, so the envelope registry and this vocabulary cannot drift. [14]
- The shared state/acceptance consistency rule this payload delegates to rather than restating. [15]
- The strict, extra-forbidding, frozen base that makes an undeclared field a refusal by construction — the reason the absence claims need no denylist. [16]
- The owner's own reference shape, which this module deliberately re-spells rather than translates. [17]
- The registry this payload shape is admitted through, and the derived kind set that names its group. [18]
- **The falsifiable absence at the payload plane: four forbidden operative-obligation names, each refused with the name in the detail.** [19]
- The falsifiable absence at the schema plane: the re-derived column census over every registered generation, and the fact that the kind is not a table. [20]
- The task-authority absence, and the hand-sealed forbidden row that cannot be decoded. [21]
- The three-component shape, the admitted version spelling, and the reference the payload deliberately does not police. [22]
- The state/consistency and explanation cases, including the authorship-substitution refusals. [23]
- The membership case that keeps the local operation literal a subset rather than a second vocabulary. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
