# mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py

## Governing Overview

[lifecycles overview](overview.md)
## Purpose

Measures a stored assessment's dependency binding against the exact identities supplied by its current read.
## Code Commentary

Recorded and measured identity maps remain distinct. `measured_binding_status` returns unavailable for unread dependencies, not-measured for absent coverage, stale for an observed disagreement, and current only when the required identities are fully measured and equal. Separate semantic freshness reasons are carried without rewriting the stored assessment. The removed _subject_state helper is not the current measurement owner; absence of evidence cannot be reported as current.
### Logic

`disputed_dependencies` is the comparison. It walks the assessment's declared `EvidenceDependencies`
edges and returns a `BindingGap` for every edge whose `(algorithm, digest)` pair no longer equals the
observed value, carrying both the recorded and the observed state so a refusal can name them.

`AssessmentCurrentness.binding_state` carries the verdict as the two-member
`CurrentnessStatus = Literal["current", "stale"]`, and `is_stale` reads it. `assessment_currentness`
derives that state from the record's own declaration; the former `subject_state` read-layer derivation is removed (see below).

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
`subject_state` is removed (see above); `measured_binding_status`
is the measurement owner.
`assessment_currentness`, `disputed_dependencies` and the `require_current_*` refusals are **unchanged**:
the shipped comparison remains the one equality authority, and `AssessmentCurrentness` keeps its
two-member literal so the refusal helpers are untouched; `compose_currentness` is removed. What this leaf removed
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

- **The currentness spelling stands alone.** `CurrentnessStatus` is the two-member literal this module
  declares; `models/knowledge/detection.py` carries no `DetectionRunCurrentness` declaration, so the old
  L14 shipped-precedent note is retired. An assessment's currentness compares a whole declared input
  set, and the spelling is never free-form text.
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

- `measured_binding_status` owns the current boundary described above. [6]
- `assessment_currentness` owns the current boundary described above. [7]
- `require_assessment_dependencies` owns the current boundary described above. [8]
- The equality comparison over declared-dependency identities, and the gap it reports. [9]
- The two-member currentness state and the derivation that produces it. [10]
- The refusal that names the recorded digest, the observed state and the exact identity. [11]
- The one edge kind excluded from the comparison, and why the exclusion is structural. [12]
- The two-member spelling is declared module-locally; no shipped `DetectionRunCurrentness` precedent exists in the tree. [13]
## KS-R15@v1 Binding Currentness

**The leaf that created this module.** `KS-R15@v1` §5 charters it: identities stored rather than
described (§5.1), identity checked and equivalence never decided (§5.2), a mismatch marking the
binding stale while leaving it readable (§5.3), and a stale assessment neither reused nor deleted
(§5.4). `KS-R15@v1` §5.4's *publication-time* refusal is the delivered-but-uncalled primitive noted
in the invariants above.

The **currentness field mapping** the packet listed as an open truth gap: this leaf mapped the
design's `binding_state=stale` onto `AssessmentCurrentness.binding_state` rather than onto
`currentnessStatus` (the coherence authority's own free-form status, which would let a mismatch be
spelled as anything) or onto the task-leaf binding's `bindingState` (a plan's state, not a record's
currentness). The old L14 note claiming a shipped `DetectionRunCurrentness.binding_state` precedent is
retired: no such declaration exists in the tree as measured.
