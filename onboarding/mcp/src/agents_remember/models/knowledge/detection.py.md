# mcp/src/agents_remember/models/knowledge/detection.py

## Governing Overview


[models route overview](../overview.md)

## Purpose


Carries mechanically observed detection signal values with closed conditions, recorded inputs and explicit scope limitations.

## Code Commentary


`DetectionSignalPayload` requires the condition vocabulary version, actual input set, observed changes, relationship paths, extractor/policy versions, scope manifest, unmapped paths and limitations. Its validators require the no-semantic-assessment limitation and consistency of truncation, unmapped paths and probe omissions. `detail` must equal the rendering of recorded basis; a trigger-side-only input cannot claim a two-sided comparison or counterpart absence. The canonical DetectionRun request/result/currentness/reproduction record and writer models are retired. A retained signal value is not a stored detection-run channel or a verdict.

One row per model declares the shape:

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

- `observed_basis_detail` — the one detail string a signal may hold, as a function of the recorded
  condition identity, the recorded paths and the recorded limitations.

- Every model subclasses the shipped `KnowledgeModel`, so `extra="forbid"` and frozen instances are
  inherited rather than restated, and string bounds come from the shipped `LABEL_MAX_LENGTH`,
  `PATH_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`, `SHA256_PATTERN` and `UUID_PATTERN`
  constants.

- **A field that cannot be supplied is a refusal, not an absent value.** The four collection fields a
  signal must carry are required even though three of them are frequently empty, so a signal that
  observed nothing *states* that rather than leaving the field to a default that reads the same as a
  construction that forgot it.

- **The declared input set is never inferred.** A signal whose declaration and recorded inputs disagree
  fails construction rather than being reported under the broader member.

- **A detection record carries no content address, logical digest or fingerprint field.** The observed
  digest belongs to `record_revision`; requirement 3.7 refuses a digest on the signal.

### Todos

None recorded.

## Evidence


### Repo-Internal References

- `DetectionSignalPayload` owns the current boundary described above. [30]
- `DetectionRecordedInputSet` owns the current boundary described above. [31]
- `DetectionScopeManifest` owns the current boundary described above. [32]
- `observed_basis_detail` owns the current boundary described above. [33]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

- The observed change granularities, whose whole point is that a file-level observation is not a span observation. [34]
- The registered scope status, every declareable limitation, and the one limitation both records state unconditionally. [35]
- The four manifest destinations, and the rule that only the durable publication route can back a retained report. [36]
- One side of a read as an identity: the admission, the selector and the selector policy version, with the one-namespace refusal. [37]
- The counterpart-probe outcome, in the shipped coverage vocabulary rather than a second one. [38]
- The observed change at its recorded granularity, and the refusal of a span observation no whole-path locator could have made. [39]
- The recorded relationship path, retaining every edge and the side that reached it. [40]
- The manifest reference: the retained object's own fields, the declared destination kinds, and `resolve` reporting a reference it cannot show as unresolved with what would resolve it rather than as an empty manifest. [41]
- The declared input set and the discriminator check: two sides and no probe, both sides and the probe, or one side and no probe — each refused with the member and the recorded inputs named. [42]
- The all-required signal field set, its closed-vocabulary validator and the `detail`-equals-rendering refusal that makes a verdict in prose unrepresentable. [43]
- The one detail string a signal is allowed to hold, as a rendering of its own recorded basis. [44]
- The refusal type a documented refusal would be carried on. [45]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
