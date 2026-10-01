# mcp/src/agents_remember/models/lifecycles/ — Lifecycle Models

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/lifecycles/` |

## Governing Overview

[models overview](../overview.md)

## Hot Path Summary

Operation recovery and integration authority carry code and memory-content commits only. `mutation_evidence.py` keeps the actual `head`/`headTree` and adds `contentHeadTree` for memory comparisons with root `memory.md` excluded. Prepared state admits the ordered code/content prefix and separately proves the certified content tree when an existing raw memory output still contains a legacy cache.

This route is the strict vocabulary for root-journal operations: generations, closeout-door and successor publication, worker termination, direct landing, legacy migration proof, and public legal controls.

Use `responses.py` for lifecycle signal vocabularies and tool responses, `finalize.py` for the
terminal finalizer response, and `operation.py` for asynchronous closeout/integration inputs,
durable records, and public projections. The operation record separately retains closeout selection,
integration selection, and completed organizational certification. `certification.py` and
`integration_certification.py` own those selected-reference vocabularies; execution and physical
publication readback remain outside the model layer.

## What Belongs Here

Strict lifecycle wire and durable-operation models. Lifecycle behavior, persistence, status
projection, and tool payload assembly remain in observer, worktree, application, and MCP layers.

## Operating Model

The package centralizes related model definitions without introducing a package facade.
`responses.py` owns the lifecycle state/phase vocabularies consumed by observer code;
`operation.py` separates private durable execution identity from the task-addressed public view.

## Local Invariants And Traps

- One module owns each vocabulary; consumers import it rather than copying literal sets.
- AR-owned response and operation records reject unexpected fields.
- Operation keys, worker PIDs, fingerprints, and candidate trees remain private record state.
- Selected certification belongs to one exact operation key/generation. Completed integration binds
  the same original frozen run and G1–4 references, completion fingerprint, comparison base, memory
  cap, and admitted integration code commit.
- Selection advances meaningful state; model validity alone does not prove stored publication bytes.

## File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`responses.py.md`](responses.py.md) — lifecycle signal vocabularies and responses.
- [`finalize.py.md`](finalize.py.md) — terminal task-finalization response.
- [`operation.py.md`](operation.py.md) — asynchronous lifecycle operation inputs, record, and projection.

- [`certification.py.md`](certification.py.md) — exact closeout selection, retained memory observations and append-only original terminal history.
- [`integration_certification.py.md`](integration_certification.py.md) — full integration selection, original completion identity and retained interrupted terminals.

## Child Overviews

None.

## Evidence

### Repo-Internal References

- Lifecycle response vocabularies and models are owned together. [1]
- Finalization exposes edge proof and completion-seat result sets. [2]
- Asynchronous operation records keep private identity out of the public projection. [3]

Current working-candidate evidence for this route:

- Recovery records have two output commits. [4]
- A filtered content head does not replace actual Git head/tree facts. [5]
- Prepared state has an ordered two-leg prefix. [6]

### Docs References

No Domain Documentation source is configured.

### Cross-Repo References

No cross-repository implementation dependency governs this route.

### MCAR-L03 Pair-Bound Lifecycle Evidence

`CuratorQualityAttestation` and `CuratorCoherenceRecord` now require the complete frozen
`MemoryCandidatePairIdentity`, not merely independent code and memory tree strings. The public
coherence response carries that same pair on prepared, published, valid, and typed-refusal paths;
`pairField`, `expected`, `observed`, and `nextArgs` preserve exact mismatch and recovery facts
without exposing a second authority. This makes a record from another otherwise-valid checkout,
base, branch, onboarding root or contract structurally ineligible for the current leaf. The consumer cache path is excluded from candidate identity.

## How To Use This Area

Read the focused model card first, then its producer/consumer references. Use the parent models
overview for registry-wide response conventions.

## L23 Final Candidate Route Disposition

This route owns the validated durable-operation record, including accepted candidate and monotonic
recovery-commit evidence. Agent-facing lifecycle responses remain task-addressed and deliberately
exclude operation keys, PIDs, leases, and resume tokens.

## 260815-DAG-L4 L4 Integration Journal Schema

Lifecycle operation records bind integration to canonical contract and repository identities, exact source and target refs, accepted commits, conflict provenance, irreversible recovery facts, and worker ownership. Legacy or incomplete integration authority fails closed rather than being synthesized.

## 260821-CLIVE-L1 Evidence And Strict Schema

Closeout lifecycle records are strict schema 3.0 and carry normalized effective input plus per-leg mutation evidence. `mutation_evidence.py` defines pre-mutation, mutation-intent, reconciled-unchanged, and commit-proven states over exact Git snapshots. Recovery cells are a derived projection, and the exact finalized-contract publication hash retains verified-existing/no-op generations without inventing Git mutation evidence. Compatibility readers and runtime bypasses are intentionally absent.

## 260821-CLIVE-L2 Current Architecture

The journal record is the durable authority after scheduling claim transfer. Retry preserves accepted input; recovery reconciles the same generation; cancellation requires exact Git/process evidence; revision publishes one linked successor. Direct landing has its own accepted input and memory-content mutation evidence; the ledger intent is retired. Schema-1 proof is isolated and removable.

### Reconciled Source Evidence

- Closeout and integrate inputs retain their kind-specific accepted decisions. [7]
- Organizational completion proof requires original full-prefix references and the exact selected integration authority. [8]
- Enclosure address models. [9]
- Worker termination evidence. [10]

## 260821-CLIVE Final Door, Journal, And Enclosure Models

`door.py` is canonical scheduling intent with exactly waiting/deferred/withdrawn/claimed
dispositions and immutable task/repository/provenance identity. The public join result
`door_response.py` was deleted with the closeout-door tool entry point (commit `6982c6a7`); no door
response model remains on this route. `operation.py`
owns the durable lifecycle after claim: running state, source-journal identity, commits,
certification, integration, cancellation, retirement, and supersession survive queue invalidation.

`enclosure.py` owns the terminal archive, external receipt, locator progression, and exact terminal
predecessor required for successor-enclosure publication. The former `successor.py` standalone
intent model is deleted: missing enclosure state and standalone successor WALs are not authority.
Cleanup may remove the enclosure root only after canonical entries have been externally archived,
receipted, and read back; a successor must cite that exact terminal predecessor.

## 260824-PDLS Final Lifecycle-Model Reconciliation

Operation and enclosure validation is split into named single-purpose checks for commit legs,
irreversible boundaries, recovery, legacy proof, mutation history, and worker authority. The split
preserves one strict journal-owned model surface; it does not add permissive readers, fallback
state, or queue-derived lifecycle evidence.

## 2026-08-26 Shared Operation And Control Vocabulary

`operation_kinds.py` is the single model owner for both `LifecycleOperationKind` and the closed `LifecycleControlAction` set. Worktree request DTOs, lifecycle controls, and public projections consume those types rather than declaring action literals at an effect layer. This keeps exhaustive request/response typing beside the lifecycle model vocabulary.

## MCAR-L02 Curator-Coherence Records

`curator_coherence.py` defines frozen strict source-candidate, judgment, recorded-evidence,
generation, stable-authority, snapshot, action-request, and response models. Requirement revision,
delivery attempt, candidate trees, attestation digest, record digest, and predecessor-authority
digest are different cells. Exact set validation prevents a report from silently covering eight
candidates while the current attestation contains ten.

## KS-R24@v1 The Publication Set Is One Declaration

`curator_coherence.py` now declares what `publish` requires **once**. `PUBLICATION_MEMBERS` is a tuple
of `PublicationMember` beside the request model, in the request model's own field order, each entry
carrying its caller-written field name and whether `prepare` derives it; `JUDGMENTS_MEMBER` names
`judgments`, a publication input that is not one of the nine the `None` check covers. The validator,
the `publish` refusal (`publication_refusal`) and the `prepare` text (`publication_input_statement`) all
read that declaration, so a member appended to it is checked, named and stated with no second edit —
the drift the single list removes. `forbidden_publication_refusal` names the publication-only field a
`status`/`prepare`/`validate` call received, in model order, with the `freeze_snapshot` branch keeping
its own message. The messages are the requirement: the shipped refusal named three prose categories
("identity, predecessor, and caller") while the two members that actually caused it
(`semantic_requirement_revision`, `delivery_attempt`) belonged to none of them, which is how two leaves
of this master recorded an unpublished coherence authority as an impassable tool defect
(`notes/DISCLOSURES.md` D-11). No member became optional, none became required, and a differential
probe over 80 request shapes measured 0 accept/refuse changes. File-level detail is in the sidecar, and
the `prepare` half lives on the closeout route.
## 260918-TSIP-L3 The Publish Refusal Names The Field (`T50`)

`CuratorCoherenceRequest._action_has_one_input_shape` requires nine non-null fields for `publish` and
forbids them on `status`/`prepare`/`validate`. Its predicate tests each field against `None`, so the
entries now carry the request field's own name beside the value: the `publish` refusal appends
`missing: <every absent field>` and the sibling branch names what it received. **That message is the
caller's only route to the field** — pydantic attaches a model-level validator error to nothing
(`loc: ()`) — and the JSON schema cannot carry the requirement, because it is conditional on
`action == "publish"`. The predicate itself is unchanged: a refusal's text, not its behaviour, was the
defect, which is why the repair is pinned through the **real registered tool** in
`mcp/tests/test_tools.py` and not only at the model boundary.

## CCR-R18@v1 Generation-Coherent Projection Contracts

260831-CCR-L18 added `models/lifecycles/operation_projection.py` to this route: the closed state matrix (status/phase/worker-state/result-class/control-action cells, versioned `lifecycle-operation-state-matrix/v1`) and the revision-bound public `LifecycleOperationProjection` envelope (identity, component bindings, worker/approval/recommendation cells). `operation_kinds.py` now centralizes `LifecycleOperationStatus` and `LifecycleOperationPhase`; `operation.py` gained the monotonic `recordRevision` field and re-exports the envelope. File-level detail lives in the three sidecars.

## Observation Cursor Contract

`operation_wait.py` declares the status-change wait vocabulary. `operation.py` retains both
`recordRevision` for durable writes and `meaningfulRevision` for meaningful state changes;
`operation_projection.py` carries the optional public wait cursor in the versioned coherent
envelope. These revisions have different purposes and must not be substituted for one another.

- The durable record owns both revisions; its meaningful subset includes both selected certification cells. [11]
- The public envelope carries the wait cursor beside versioned identity and component bindings. [12]

## L34 Preparation Ownership

The L34 private-output vocabulary is owned by [preparation.py](preparation.py.md), [preparation_state.py](preparation_state.py.md) and [prepared_memory.py](prepared_memory.py.md). Intent and raw-output identity, append-only command evidence and physical/logical execution views remain separate. None of these models makes a private commit a published mutation.


## Integrated IAS Recovery Contract

`preparation_state.py` separates output-command validation and command-terminal observation into focused helpers. An output still requires its original observed commit command; command history cannot be removed or restarted, and late terminal observation requires the original worker authority. The model remains a validator of selected journal facts, not a producer of Git proof.

## CCR-R12@v5 Current Model Boundary

The lifecycle model route records typed transaction inputs, explicit approval/gate-policy snapshots,
candidate/source identity, mutation evidence, recovery facts, and terminal results. Retained
certification and quality fields remain strict vocabulary for explicit or historical callers, but
normal closeout/integration workers do not select, populate, or require them. Model presence is not
normal transaction acceptance evidence.

## 260915-KS-L15 The Assessment Collection Beside Judgments

`models/lifecycles/` gains three modules and one field on the existing authority, and the reason the
field is a **second collection** rather than an extension of `judgments` is the load-bearing fact of
this change. A judgment's identity is the `(sourceFile, onboardingFile, classification)` triple and
`_judgments_cover_candidates_exactly` refuses a record whose judgment set is not exactly its
source-candidate set; a knowledge review's subject is a knowledge record, a family, an invariant
revision or a comparison, and none of those is a source-file pair. Appending one to `judgments` would
therefore either break exact coverage or fabricate a source-candidate tuple for a family, which the
design forbids outright — so `CuratorCoherenceRecord.assessments` is its own typed collection,
bounded by `MAX_CURATOR_REVIEW_ASSESSMENTS = 256` and validated only for its own identity uniqueness.

`review_assessment.py` owns the record and the four-state read projection; `review_assessment_binding.py`
owns currentness and the rule that a mismatch marks a binding **stale while leaving the judgment
readable**; `review_assessment_store.py` builds the exact-input declaration under a new
`review-assessment/v1` evidence-dependency policy and declares the record's own `review-record` edge
per assessment. The binding deliberately does not declare the record it lives in — the edge runs from
the record to the assessment only — which is what keeps it out of the self-invalidating sequence.
`evidence_dependencies.py` gained that policy and one *permission* on `curator-coherence/v1`, widening
no kind vocabulary.

## 260921-ICR-L15 Measured assessment currentness

This route's assessment vocabulary now separates **what a measurement established** from **what the
stored records assert**, and it is a vocabulary change rather than a new read: no invariant of the
binding rule moved, and the shipped comparison stays the one equality authority.

`review_assessment.py` (502 → 620 lines) declares the per-record state as the four-member
`AssessmentBindingStatus` — `not-measured`, `current`, `stale`, `unavailable` — published once as
`ASSESSMENT_BINDING_STATUSES` and reused as `CURRENTNESS_STATES`. `AssessmentEntry.currentness` carries
it, so a projection reports the state a *measurement* put a binding in rather than a label derived from
whether a mapping was supplied. `SubjectAssessmentStatus` gained `not-measured` and `unavailable` beside
the `none-recorded` that stays the *unassessed* subject's own state, because a subject nobody assessed,
a subject whose records nobody measured and a subject whose measurement failed are three different
answers. `SubjectAssessmentState` gained `notMeasuredCount`/`unavailableCount` and the validator
(`_counts_describe_the_records_that_exist`, `_require_the_counts_to_partition_the_records`,
`_status_of_records`) that derives the currentness counts from the entries and refuses a status its own
records contradict. `assessment_state_for(assessments, *, statuses=None)` reports `not-measured` for an
assessment nobody measured, and its signature has no argument that means "assume current" or "assume
stale"; the subject status follows the precedence `stale` → `unavailable` → `unresolved` →
`not-measured` → `current`.

`review_assessment_binding.py` (276 → 497 lines) owns the measurement half. The new
`AssessmentCurrentnessMeasurement` carries `state`, the `values` a world was read to hold, a `detail`,
and the `unmeasured` identities with their own reason; `CurrentnessMeasurementState` declares the three
measurement states, and `measured_currentness`, `no_currentness_measurement` and
`unavailable_currentness_measurement` are the ways to build one. `measured_binding_status` states the
whole rule: a failed measurement is `unavailable`; a measured disagreement is `stale`, decided by the
shipped `disputed_dependencies` comparison over the measured values; a completed measurement that
covered every declared identity and disagreed nowhere is `current`; and everything else — including the
empty measurement, which is measured and covers nothing — is `not-measured`. Presence of a mapping is
never the decision. `unmeasured_identities`, `measured_binding_statuses`,
`supplied_measurement_statuses` and `subject_state(assessments, current=None)` carry that rule into the
per-record and per-subject shapes the composition and the read projection use. `assessment_currentness`,
`disputed_dependencies` and the `require_current_*` refusals are **unchanged**: a measured movement is
still the only thing that can call a binding stale, and nothing here decides equivalence.

Three facts a reader of this route should carry:

- **An unmeasured binding is neither current nor stale.** It is `not-measured`, and reporting it as
  either would publish a fact the store never held.
- **A measured zero is not a failure.** An empty measurement is a measurement that covered nothing; a
  failed one is `unavailable`. The two are different facts.
- **The summary cannot disagree with its records.** The counts partition the entries and the status is
  re-derived from them, so a `current` subject holding an entry nothing measured is unrepresentable.

## Retained curator generation and judgment custody

The existing recorded judgment may carry owner-stamped path/SHA/size custody under the existing curator artifact root. Original authored citation/hash remain unchanged, caller judgment inputs cannot provide replacement custody, and canonical omission preserves older sealed records. A typed ValidatedCuratorCoherenceGeneration represents durable integrity separately from live authority/currentness.
