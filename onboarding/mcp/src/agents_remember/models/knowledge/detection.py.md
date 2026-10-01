# mcp/src/agents_remember/models/knowledge/detection.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The whole vocabulary of one mechanical detection, and no SQL.** This module declares the facts a
detection signal and a detection run carry, the closed vocabularies each value comes from, and the
construction refusals that make the non-conforming shapes unrepresentable. It writes nothing, reads
nothing from a database and takes no transaction: the walk that decides which recorded facts match
which condition is `memory/knowledge/detection_walk.py`, and the record's write, read and comparison
paths are `memory/knowledge/detection.py`.

It exists because a *detection signal* is a different claim from a comparison, and the differences are
the ones that have to be unrepresentable rather than merely discouraged:

- **No semantic conclusion, by construction.** Neither a signal nor a run has a field that could hold a
  severity, an assessed priority, a conflict or compatibility verdict, a causal explanation, a
  harmlessness label or an authored finding — and the declared field set is *reviewable* against one
  closed list. The shipped comparison states the same property at `models/knowledge/diff.py:12-13`;
  this module states it as a rule rather than as an appeal to that precedent.
- **The declared input set is required, explicit and closed.** A signal states which of the three
  readings it performed, and the declaration is checked against the *recorded discriminator of the
  member it named* — never inferred from the condition, from the number of sides a request happened to
  carry, or from the running build.
- **Observed changes are typed at their recorded granularity.** The granularity is part of the fact: a
  whole-file observation recorded as a body change is refused, because a file changing is not evidence
  that an attributed span changed.
- **Versions are published twice.** The extractor and policy versions are values on the run *and* on
  every signal it produced.

## Code Commentary

### Logic

**The published identities.** `DETECTION_POLICY_VERSION` is the shipped constant idiom
(`DIFF_POLICY_VERSION`, `KNOWLEDGE_READ_POLICY_VERSION` beside it): it names the detection contract, not
a second selection rule — which records are selected is the read policy's and which union is compared
is the diff policy's, and neither is restated here. `DETECTION_EXTRACTOR_VERSION` is **authored**
rather than imported, and the module says why: the shipped anchor resolver has no symbol extractor at
all and returns `resolution="unsupported_locator"` (`memory/knowledge/read_anchors.py:132-139`), so
there is no existing constant to cite; the authored value names what this build actually extracts —
whole-path and recorded-range observations against an exact tree object. `CONDITION_VOCABULARY_VERSION`
versions the matched-condition vocabulary with the policy.

**The closed vocabularies, each declared as a `Literal` and as a tuple.** `DetectionCondition` and
`DETECTION_CONDITIONS` are the five conditions the detection policy declares — the design's own
candidate list, nothing invented beyond it; `DeclaredInputSet` and `DECLARED_INPUT_SETS` are the three
readings; `DetectionChangeGranularity` is requirement 1.3's distinct facts; `DetectionScopeStatus` is
the registered scan outcome plus the one value that says the scan did not finish; `DetectionLimitation`
and `DETECTION_LIMITATIONS` are every declareable limit. The `Literal` is what a field is validated
against and the tuple is what a caller enumerates — the shipped `ANCHOR_RESOLUTIONS` /
`AnchorResolutionState` idiom.

**The review that makes "no conclusion" checkable.** `CONCLUSION_BEARING_FIELD_NAMES` is one closed list
of conclusion concepts and `conclusion_bearing_fields` is the review: it reads a model's **declared**
field set — not an instance — and returns every field whose *name* names one of those concepts, so a
field is reported whether or not any payload populates it. Requirement 5.2's first half is that review;
its second half, refusing a payload that supplies one, is the shipped base's `extra="forbid"`.

**`declared_input_set_discriminators` derives its mapping from the closed tuple**, so it cannot name a
member the vocabulary does not declare, and the validators enforce exactly what each entry says:
`DetectionRecordedInputSet` checks the member's own recorded facts rather than counting sides. One row
per model declares the shape:

- `DetectionInputSide` — one side a run or signal read: the side name, the whole admission
  (`KnowledgeReadContext`), the selector digest and the selector policy version. Its validator refuses
  a side that names a namespace its selected knowledge snapshot does not belong to.
- `DetectionCounterpartProbe` — one union item's recorded counterpart-probe outcome in the shipped
  `DiffCoverage` vocabulary, so the probe question and its answer range are the comparison's own rather
  than a second one beside it.
- `DetectionObservedChange` — one observed change at its recorded granularity, with the item, the path,
  the recorded and observed identities and the locator kind. Its validator refuses
  `attributed_span_changed` against a whole-path locator kind (`file`, `directory`).
- `DetectionRelationshipPath` — one followed path: the snapshot side, every recorded edge in order, the
  item the last edge reached and the realization role. A path is *recorded* rather than derived, so a
  link the candidate removed is still reported with the side that still holds it.
- `ManifestDestinationObservation` — what one destination check observed: the destination kind and
  reference, whether it resolved, and a detail. Nothing here publishes or archives.
- `DetectionScopeManifest` and `DetectionManifestResolution` — the retained, addressable object a signal
  references, and its answer. `resolve` reports a reference as `retained` only for a resolved
  `durable_publication` destination with a recorded identity, and otherwise `unresolved` **with what
  would resolve it** — never as an empty manifest. Its validator refuses a destination kind outside the
  declared four and a required retention at the durable route with no destination identity.
- `DetectionRecordedInputSet` — the declared member and the recorded discriminator that must agree with
  it: `both_sides_declared` needs exactly the two sides and no probe; `union_of_both_sides` needs both
  sides *and* the probe's recorded outcome per item; `trigger_side_only` needs exactly one side and no
  probe at all. Each refusal names the member, what was recorded and the failure shape.
- `DetectionSignalPayload` — requirement 1.1's all-required field set. Beyond the closed vocabularies it
  enforces three things: the unconditional `no_semantic_assessment_performed` limitation is always
  present; an omitted item and its declared limitation cannot disagree in either direction; and
  `detail` must **equal** `observed_basis_detail`, so a rendered judgment written into the prose field
  is refused as the same defect a verdict field would be. A `trigger_side_only` signal that asserts
  something about the unread side gets its own refusal naming what it did not read.
- `DetectionRunPayload` — one execution of one policy: the run's own identity, the namespace it was
  recorded into and the namespace it assessed, its governing route, the two published versions, the
  vocabulary version, the sides it read, the members its signals declared, the conditions they recorded,
  the declared deterministic total order over signal identity, and the declared limits. Its validators
  require the unconditional limitation, refuse a repeated identity in the order, refuse a declared order
  whose length differs from the recorded conditions, and require `detail` to equal the run-basis
  rendering.
- `DetectionSignalSet`, `DetectionRunRequest`, `DetectionRunInputDifference`, `DetectionRunReproduction`,
  `DetectionRunDifference`, `DetectionRunCurrentness`, `DetectionRunResult` — the served shapes. The
  reproduction carries **both** run identities, the two ordered sequences, the differences and one
  verdict, and its validator refuses a verdict that disagrees with the facts it carries.
  `DetectionRunCurrentness` carries the recorded and current versions beside the state but **no signal
  at all**: its `signals_unchanged` field is the literal `True`, which is the type saying that this
  operation cannot rewrite what it read. `DetectionRunResult` requires exactly one outcome, and
  `ordered_signal_ids` returns the served signals in the run's recorded order.
- `observed_basis_detail` — the one detail string a signal may hold, as a function of the recorded
  condition identity, the recorded paths and the recorded limitations.

### Conventions

- Every model subclasses the shipped `KnowledgeModel`, so `extra="forbid"` and frozen instances are
  inherited rather than restated, and string bounds come from the shipped `LABEL_MAX_LENGTH`,
  `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`, `SHA256_PATTERN` and `UUID_PATTERN`
  constants.
- **A field that cannot be supplied is a refusal, not an absent value.** The four collection fields a
  signal must carry are required even though three of them are frequently empty, so a signal that
  observed nothing *states* that rather than leaving the field to a default that reads the same as a
  construction that forgot it.
- Verified policy relations are stated in comments that name the precedent, so a reader can check it
  rather than trust it. The two read-vocabulary precedents are now named by module and symbol rather than
  by line number: `read.KNOWLEDGE_READ_POLICY_VERSION` in `models/knowledge/read.py`, and
  `read_anchor.AnchorResolutionState` (beside `ANCHOR_RESOLUTIONS`) in `models/knowledge/read_anchor.py`,
  where the anchor vocabulary now lives. The `DIFF_POLICY_VERSION` pointer still names
  `models/knowledge/diff.py:98` (the constant is now declared a few lines lower), and the `DETECTION_EXTRACTOR_VERSION` comment still cites
  `memory/knowledge/read_anchors.py:132-139` and says the resolver has no symbol extractor. That last
  statement no longer describes the resolver, which resolves symbol locators through the shipped extractor
  (`_observed_symbol`); treat the comment as the version's origin note, not as a current fact.
- The `Literal` and its tuple are declared **twice on purpose** and a case asserts they agree.

### Invariants And Boundaries

- **No field of either record can carry a conclusion**, and the absence is declared rather than left to
  be inferred from a missing field: `no_semantic_assessment_performed` is unconditional on both records.
- **The declared input set is never inferred.** A signal whose declaration and recorded inputs disagree
  fails construction rather than being reported under the broader member.
- **A detection record carries no content address, logical digest or fingerprint field.** The observed
  digest belongs to `record_revision`; requirement 3.7 refuses a digest on the signal.
- **`governing_route_id` is a required validated field on both records.** It is an identity, not a
  reference to the envelope's `knowledge_record.governing_route_id` association — see
  `memory/knowledge/detection.py` for why the association is left unset for this record group.
- **Boundary.** This module is vocabulary and validation: it holds no SQL, imports no store, mints no
  gate and writes no row. Its one behavioural function, `conclusion_bearing_fields`, answers a question
  about a *type* and touches no instance.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The three published identities: the detection policy (a named contract, not a second selection rule), the authored extractor version, and the condition vocabulary's version.** [1]
- The five declared conditions, as the validated type and as the ordered value the walk emits in. [2]
- **The three declared input sets, and the discriminator each member records, derived from the closed tuple so it cannot name an undeclared member.** [3]
- The observed change granularities, whose whole point is that a file-level observation is not a span observation. [4]
- The registered scope status, every declareable limitation, and the one limitation both records state unconditionally. [5]
- **The closed conclusion-name list and the review that makes requirement 5.2's first half mechanical: it reads the declared field set and reports a conclusion-bearing name whatever its type.** [6]
- The four manifest destinations, and the rule that only the durable publication route can back a retained report. [7]
- The envelope registry key pair for each record kind, declared once here rather than spelled a second time. [8]
- One side of a read as an identity: the admission, the selector and the selector policy version, with the one-namespace refusal. [9]
- The counterpart-probe outcome, in the shipped coverage vocabulary rather than a second one. [10]
- **The observed change at its recorded granularity, and the refusal of a span observation no whole-path locator could have made.** [11]
- The recorded relationship path, retaining every edge and the side that reached it. [12]
- **The manifest reference: the retained object's own fields, the declared destination kinds, and `resolve` reporting a reference it cannot show as unresolved with what would resolve it rather than as an empty manifest.** [13]
- **The declared input set and the discriminator check: two sides and no probe, both sides and the probe, or one side and no probe — each refused with the member and the recorded inputs named.** [14]
- **The all-required signal field set, its closed-vocabulary validator and the `detail`-equals-rendering refusal that makes a verdict in prose unrepresentable.** [15]
- **The run payload: the two published versions, the per-signal members not collapsed into a run-level default, and the declared total order over signal identity.** [16]
- The run-basis rendering the run's `detail` must equal. [17]
- The signals one run produced, returned in the run's recorded order rather than a query's order. [18]
- The request shape, carrying the assessed databases requirement 7.1 refuses to write into. [19]
- **The reproduction as two identities, two ordered sequences and the differences, with one verdict that must follow from them.** [20]
- **The currentness answer that carries the recorded versions beside the current ones and cannot hold a re-interpreted signal.** [21]
- The one typed outcome per detection operation, with the served signals in the recorded order. [22]
- The one detail string a signal is allowed to hold, as a rendering of its own recorded basis. [23]
- The envelope registry these payload models are registered in, which is why the field set is declared once here. [24]
- The comparison the walk reads, and the shipped statement that a comparison is not a conclusion. [25]
- The refusal type a documented refusal would be carried on. [26]
- **The anchor resolution state that carries `unsupported_locator`, which is why the extractor version is authored here rather than imported.** [27]
- The precedent comments naming the read-vocabulary constants by module and symbol rather than by line. [28]
- The extractor-version origin note, whose claim that the resolver has no symbol extractor predates the resolver's symbol path. [29]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
