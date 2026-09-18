# mcp/src/agents_remember/models/knowledge/detection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/detection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

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
- Verified policy relations are stated in the docstring with the file and line that carries them
  (`models/knowledge/diff.py:12-13`, `models/knowledge/read.py:112-130`,
  `memory/knowledge/read_anchors.py:132-139`), so a reader can check the precedent rather than trust it.
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The three published identities: the detection policy (a named contract, not a second selection rule), the authored extractor version, and the condition vocabulary's version.** | `DETECTION_POLICY_VERSION`; `DETECTION_EXTRACTOR_VERSION`; `CONDITION_VOCABULARY_VERSION` | mcp/src/agents_remember/models/knowledge/detection.py:96-134 |
| The five declared conditions, as the validated type and as the ordered value the walk emits in. | `DetectionCondition`; `DETECTION_CONDITIONS` | mcp/src/agents_remember/models/knowledge/detection.py:111-132 |
| **The three declared input sets, and the discriminator each member records, derived from the closed tuple so it cannot name an undeclared member.** | `DeclaredInputSet`; `DECLARED_INPUT_SETS`; `declared_input_set_discriminators` | mcp/src/agents_remember/models/knowledge/detection.py:136-149; mcp/src/agents_remember/models/knowledge/detection.py:286-303 |
| The observed change granularities, whose whole point is that a file-level observation is not a span observation. | `DetectionChangeGranularity`; `_WHOLE_PATH_LOCATOR_KINDS` | mcp/src/agents_remember/models/knowledge/detection.py:156-170 |
| The registered scope status, every declareable limitation, and the one limitation both records state unconditionally. | `DetectionScopeStatus`; `DETECTION_LIMITATIONS`; `NO_SEMANTIC_ASSESSMENT_LIMITATION` | mcp/src/agents_remember/models/knowledge/detection.py:172-215 |
| **The closed conclusion-name list and the review that makes requirement 5.2's first half mechanical: it reads the declared field set and reports a conclusion-bearing name whatever its type.** | `CONCLUSION_BEARING_FIELD_NAMES`; `conclusion_bearing_fields` | mcp/src/agents_remember/models/knowledge/detection.py:217-283 |
| The four manifest destinations, and the rule that only the durable publication route can back a retained report. | `MANIFEST_DESTINATION_KINDS` | mcp/src/agents_remember/models/knowledge/detection.py:250-258 |
| The envelope registry key pair for each record kind, declared once here rather than spelled a second time. | `DETECTION_SIGNAL_KIND`; `DETECTION_RUN_KIND` | mcp/src/agents_remember/models/knowledge/detection.py:260-265 |
| One side of a read as an identity: the admission, the selector and the selector policy version, with the one-namespace refusal. | `DetectionInputSide` | mcp/src/agents_remember/models/knowledge/detection.py:306-327 |
| The counterpart-probe outcome, in the shipped coverage vocabulary rather than a second one. | `DetectionCounterpartProbe` | mcp/src/agents_remember/models/knowledge/detection.py:330-340 |
| **The observed change at its recorded granularity, and the refusal of a span observation no whole-path locator could have made.** | `DetectionObservedChange` | mcp/src/agents_remember/models/knowledge/detection.py:343-379 |
| The recorded relationship path, retaining every edge and the side that reached it. | `DetectionRelationshipPath` | mcp/src/agents_remember/models/knowledge/detection.py:382-398 |
| **The manifest reference: the retained object's own fields, the declared destination kinds, and `resolve` reporting a reference it cannot show as unresolved with what would resolve it rather than as an empty manifest.** | `DetectionScopeManifest`; `DetectionManifestResolution` | mcp/src/agents_remember/models/knowledge/detection.py:401-543 |
| **The declared input set and the discriminator check: two sides and no probe, both sides and the probe, or one side and no probe — each refused with the member and the recorded inputs named.** | `DetectionRecordedInputSet` | mcp/src/agents_remember/models/knowledge/detection.py:546-632 |
| **The all-required signal field set, its closed-vocabulary validator and the `detail`-equals-rendering refusal that makes a verdict in prose unrepresentable.** | `DetectionSignalPayload`; `ordered_changes` | mcp/src/agents_remember/models/knowledge/detection.py:635-753 |
| **The run payload: the two published versions, the per-signal members not collapsed into a run-level default, and the declared total order over signal identity.** | `DetectionRunPayload` | mcp/src/agents_remember/models/knowledge/detection.py:756-827 |
| The run-basis rendering the run's `detail` must equal. | `_run_basis_detail` | mcp/src/agents_remember/models/knowledge/detection.py:830-837 |
| The signals one run produced, returned in the run's recorded order rather than a query's order. | `DetectionSignalSet` | mcp/src/agents_remember/models/knowledge/detection.py:840-854 |
| The request shape, carrying the assessed databases requirement 7.1 refuses to write into. | `DetectionRunRequest` | mcp/src/agents_remember/models/knowledge/detection.py:857-868 |
| **The reproduction as two identities, two ordered sequences and the differences, with one verdict that must follow from them.** | `DetectionRunReproduction`; `DetectionRunInputDifference` | mcp/src/agents_remember/models/knowledge/detection.py:871-930 |
| **The currentness answer that carries the recorded versions beside the current ones and cannot hold a re-interpreted signal.** | `DetectionRunCurrentness` | mcp/src/agents_remember/models/knowledge/detection.py:942-987 |
| The one typed outcome per detection operation, with the served signals in the recorded order. | `DetectionRunResult` | mcp/src/agents_remember/models/knowledge/detection.py:990-1014 |
| The one detail string a signal is allowed to hold, as a rendering of its own recorded basis. | `observed_basis_detail` | mcp/src/agents_remember/models/knowledge/detection.py:1017-1033 |
| The envelope registry these payload models are registered in, which is why the field set is declared once here. | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-132 |
| The comparison the walk reads, and the shipped statement that a comparison is not a conclusion. | `KnowledgeDiffResult`; `KnowledgeDiffItem` | mcp/src/agents_remember/models/knowledge/diff.py:501-520; mcp/src/agents_remember/models/knowledge/diff.py:318-340 |
| The refusal type a documented refusal would be carried on. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:207-217 |
| **The anchor resolution state that carries `unsupported_locator`, which is why the extractor version is authored here rather than imported.** | `AnchorResolutionState` | mcp/src/agents_remember/models/knowledge/read.py:112-120 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:06:32+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:207-217. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `a0665505`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the range recorded in the row above is the one that now holds its anchor. The anchors concerned: `PAYLOAD_MODELS`. No claim wording changed, and the verification metadata advances to the landed base because the claims were re-read against the current source.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:190-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): created this one-to-one card for the detection vocabulary module. It records the three published identities and, for the extractor version, that it is **authored** because the shipped resolver has no symbol extractor to cite; the closed vocabularies each declared as a validated `Literal` beside the tuple a caller enumerates; the conclusion-name list plus `conclusion_bearing_fields` as the mechanical review that makes "a conclusion must not be representable" checkable rather than asserted; the per-member discriminator contract of `DetectionRecordedInputSet` (two sides without a probe, both sides with one, one side with none) and why counting sides is not the check; the granularity refusal that makes a whole-file observation recorded as a span change unrepresentable; the `detail`-equals-rendering rule that refuses a verdict written into prose exactly as it refuses a verdict field; the manifest resolution that reports `unresolved` with what would resolve it and never as an empty manifest; and the currentness shape that carries recorded and current versions beside the state and no signal at all. Verification metadata is the leaf's base commit `4264dcc9`: the code commit does not exist yet and closeout owns that stamp.
