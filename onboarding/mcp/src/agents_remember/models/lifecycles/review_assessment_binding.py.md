# mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

**Currentness of one assessment's binding to the exact inputs it examined** — and the rule that
decides what a mismatch means. The module answers one question and refuses to answer a second:
whether the recorded identities still match their current values, never whether changed dependencies
are *equivalent*.

That refusal is the whole design. A resolver, a relocation, or byte-identical content at a new
location is not proof of equivalence, so this module has no notion of "equivalent" to reach for: it
compares `(algorithm, digest)` pairs for equality and reports the identities that differ.

## Code Commentary

### Logic

`disputed_dependencies` is the comparison. It walks the assessment's declared `EvidenceDependencies`
edges and returns a `BindingGap` for every edge whose `(algorithm, digest)` pair no longer equals the
observed value, carrying both the recorded and the observed state so a refusal can name them.

`AssessmentCurrentness.binding_state` carries the verdict as the two-member
`CurrentnessStatus = Literal["current", "stale"]`, and `is_stale` reads it. `assessment_currentness`
derives that state from the record's own declaration; `subject_state` derives the read-layer state a
subject is in.

**`260921-ICR-L15` (`ICR-R15@v1`) adds the measurement value the comparison above is handed.**
`AssessmentCurrentnessMeasurement` carries a `state` (`measured` / `not-measured` / `unavailable`), the
`values` it holds — whose **keys are its coverage**, which is what lets a partial measurement answer
without inventing an answer — and the `unmeasured` identities with their detail. `measured_binding_status`
is the whole rule built on it: a failed measurement is `unavailable`; a *measured disagreement* (a
declared identity the measurement holds a **different** value for, via the shipped
`disputed_dependencies`) is `stale`; a measurement that covered every declared identity and disagreed
nowhere is `current`; and **everything else — including an empty measurement, which covers nothing — is
`not-measured`**. `unmeasured_identities`, `measured_binding_statuses` (one world for a whole bundle) and
`supplied_measurement_statuses` (a caller's own per-record mapping) are the readers of it, and
`subject_state(assessments, current=None)` now takes that measurement rather than a bare mapping.
`assessment_currentness`, `disputed_dependencies` and the `require_current_*` refusals are **unchanged**:
the shipped comparison remains the one equality authority, and `AssessmentCurrentness` keeps its
two-member literal so `compose_currentness` and the refusal helpers are untouched. What this leaf removed
is the *presence* test that used to stand in for a measurement — an unmeasured assessment is no longer
reported `stale`, and an empty mapping no longer makes one `current`.

A mismatch marks the assessment **stale and leaves it readable**: its finding, rationale, author,
role and disposition stay as historical fact, and only its currentness changes. Nothing here deletes
a record, re-points an old finding at new inputs, or reinterprets the old judgment against them.

`require_current_assessment_binding` raises with the recorded digest, the observed state and the
exact identity — the three facts a caller needs — and `AssessmentBindingStaleError.response_fields`
renders them. `require_assessment_dependencies` validates that a record's declaration is
well-formed against the shipped evidence-dependency contract.

### Conventions

- **The currentness spelling is shared, deliberately.** `CurrentnessStatus` is the same two-member
  literal L14 shipped on `DetectionRunCurrentness.binding_state`. The two are separate fields on
  separate records — a detection run's currentness compares two version axes, an assessment's
  compares a whole declared input set — but a reader who has met one spelling has met both, and
  neither is free-form text.
- `SELF_REFERENTIAL_KINDS` is `frozenset({"review-record"})`, the one edge kind excluded from a
  staleness comparison. Every other kind binds an *input*; `review-record` names another
  content-addressed record, so comparing it here would ask an assessment to declare the digest of the
  record it is stored inside. The record declares that edge from its own side instead.

### Invariants And Boundaries

- **Equality, never equivalence.** A relocated or byte-identical input is a mismatch. There is no
  similarity score, no path-normalisation fallback and no "same content" shortcut.
- **A stale assessment is not reusable and is not deleted.** The stale state is reported beside the
  judgment, which remains readable.
- **The `review-record` edge is never a staleness gap.** The self-invalidating sequence is avoided
  structurally rather than by convention.
- **Refusing primitives are delivered here; the publication-time submission gate is not.** A
  submission against a stale comparison has no caller in this increment, and the consumption-side
  refusal belongs to the views and review-surface requirements.

## Evidence

### Repo-Internal References

- The equality comparison over declared-dependency identities, and the gap it reports. [1]
- The two-member currentness state and the derivation that produces it. [2]
- The refusal that names the recorded digest, the observed state and the exact identity. [3]
- The one edge kind excluded from the comparison, and why the exclusion is structural. [4]
- The shipped precedent whose exact spelling this field reuses. [5]

## KS-R15@v1 Binding Currentness

**The leaf that created this module.** `KS-R15@v1` §5 charters it: identities stored rather than
described (§5.1), identity checked and equivalence never decided (§5.2), a mismatch marking the
binding stale while leaving it readable (§5.3), and a stale assessment neither reused nor deleted
(§5.4). `KS-R15@v1` §5.4's *publication-time* refusal is the delivered-but-uncalled primitive noted
in the invariants above.

The **currentness field mapping** the packet listed as an open truth gap: this leaf mapped the
design's `binding_state=stale` onto `AssessmentCurrentness.binding_state` — the same name and the same
two-member literal as the shipped `DetectionRunCurrentness.binding_state` — rather than onto
`currentnessStatus` (the coherence authority's own free-form status, which would let a mismatch be
spelled as anything) or onto the task-leaf binding's `bindingState` (a plan's state, not a record's
currentness). The packet's audit of "no shipped `binding_state` identifier" predates L14; the mapping
was chosen against the tree as measured, not against the packet's near-miss list.
