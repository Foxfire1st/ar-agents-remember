# mcp/src/agents_remember/models/lifecycles/ — Lifecycle Models

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/lifecycles/` |

## Governing Overview

[models overview](../overview.md)

## Purpose

This directory defines strict transaction models for task-addressed closeout, integration and direct landing. The former agent-session lifecycle signal response/vocabulary in responses.py is removed; transaction package naming does not restore that API. It describes accepted inputs, durable operation records, public observations, preparation, certification, cancellation and enclosure identity. It also defines curator-coherence generations and the separate knowledge-review assessment collection.

Execution, persistence, physical publication readback and tool payload assembly belong to the consuming observer, worktree, application and MCP layers. A model accepting a record establishes its structural validity; it does not establish that Git mutation, certification execution or publication occurred.

## Hot Path Summary

Use `finalize.py` for terminal finalization responses and `operation.py` for accepted transaction inputs and durable records. Native task stage/activity/eventAt belongs to observer/projection.py and its task-entry producer, not the removed responses.py session State/Phase domain. `operation_projection.py` owns the versioned public envelope, re-exported by `operation.py`; `operation_kinds.py` centralizes operation kinds, statuses, phases and control actions.

Recovery output fields distinguish the code commit from the memory-content commit. `mutation_evidence.py` retains actual Git `head` and `headTree` alongside optional `contentHeadTree`. Preparation retains the ordered code/memory-content prefix and keeps private output selection separate from published mutation authority.

For curator publication, read `curator_coherence.py` with `memory_candidate.py`. For assessment currentness, read `review_assessment.py` with `review_assessment_binding.py`: an unmeasured binding is neither current nor stale.

## Construction

DirectLandingOperationInput retains canonical leafTaskDocumentRef, optional codeBefore and codeCommitMessage to distinguish create from verify-existing. The journal owns accepted input/policy snapshots and code/memory mutation/output proof, not a full pre-code check verdict; raw output/lifecycle state is not interchangeable with top-level response state.

### Signal and transaction models

The package marker introduces no facade. The former responses.py session state/phase vocabulary and lifecycle-id signal response are historical only. The retained asynchronous transaction-operation vocabulary belongs to operation_kinds.py; native task state is a separate model, not a rename of the deleted signal response.

`CloseoutOperationInput` retains normalized effective input, approval note, gate-policy snapshots and corrective dispositions. `IntegrateOperationInput` retains strategy, gate-policy snapshots and the completion-seat choice. Their discriminated union also admits the separate direct-landing input.

`LifecycleOperationRecord` is the strict schema-3.0 internal snapshot. It retains accepted identity, generation, revisions, worker ownership, mutation evidence, recovery commits, cancellation and termination evidence, legacy migration proof, preparation, door publication and optional certification selections. The public `LifecycleOperationProjection` is a coherent task-addressed envelope with versioned identity and component bindings, worker and approval observations, recommendations, legal controls and an optional meaningful-state cursor. Its declared fields omit raw operation keys, worker PIDs, leases and process fingerprints; this is not a blanket secrecy guarantee for every nested result value or identity digest.

`LifecycleFinalizeTaskResponse` declares terminal task facts, blockers, cleanup and archive results, projection effects and atomic-series activation facts. `outsideScratch` names the root a completed-cleanup retry removed, and `outsideScratchReconcile` carries the sweep that runs beside every ending answer. It declares neither completion-seat result sets nor edge proof; the producer emits cleanup/archive/projection and activation facts. Its `agentArchive` defaults to an empty mapping; finalization forwards an archive report when the cleanup or abandon result supplies one.

### Scheduling, enclosure and private preparation

`door.py` defines waiting, deferred, withdrawn and claimed scheduling dispositions, publication evidence and task/provenance identity vocabulary. `enclosure.py` defines reserved, manifest-proven, addressable and terminal-archived address states and the exact terminal predecessor link, including archive and receipt paths. These structures describe scheduling and enclosure evidence; they do not themselves perform queue transfer, external archival or cleanup.

The standing enclosure contract is that cleanup follows external archival, receipt and readback, and successor publication cites the exact terminal predecessor. Verification of the executing cleanup and successor owners remains an uncertainty of this bounded review.

`preparation.py`, `preparation_state.py` and `prepared_memory.py` separate intent and raw output identity, retained command observations, and logical versus physical execution views. `OperationPreparationState` admits only the ordered code/memory-content prefix. Command kinds form an ordered create/materialize/commit prefix; earlier commands must have succeeded before later commands are admitted. The output-command check requires an observed original commit command when the selection carries command history. It does not impose that condition on an output with an empty command tuple.

Transition validation preserves selected identity and prior commands, refuses clearing or restarting command history, and permits late terminal observation only under the original worker or proved-exit authority. A prepared-code execution view binds its references and digest while leaving actual repository and Git readback to its owner. None of these models turns a private commit into a published mutation.

### Certification and curator generations

`certification.py` and `integration_certification.py` own retained selected-reference vocabulary. The operation record separately retains closeout selection, integration selection and completed organizational quality certification. When completion certification is present, validation requires the original frozen run and four original gate certificates, exact selected integration references, completion identity and admitted integration code commit. The retained fields describe explicit or historical certification authority; their presence alone does not show that ordinary transaction workers select or require them.

`CuratorQualityAttestation` and `CuratorCoherenceRecord` carry `MemoryCandidatePairIdentity`, whose cells distinguish repository, contract, roots, branches, bases and onboarding root. The model documents the cache location as informational and excluded from the contract-digest projection. The public coherence response declares pair identity and typed mismatch/recovery fields (`pairField`, `expected`, `observed`, `nextArgs`); pair identity is optional in that response shape, so model declarations alone do not prove that every prepared, published, valid or refused response populates it.

Curator source candidates and judgments use the `(sourceFile, onboardingFile, classification)` identity. Record validation requires unique candidates, unique judgments and exact set equality. Requirement revision, delivery attempt, candidate trees, attestation digests, record digest and predecessor-authority digest remain separate cells.

`PUBLICATION_MEMBERS` declares the nine non-null publication inputs in request order, including the semantic requirement revision, delivery attempt and expected task intent. `JUDGMENTS_MEMBER` names the separate judgment content input; review assessments are another optional content collection. The publish validator, missing-field refusal and prepare input statement consume the declaration. Non-publish actions refuse supplied publication-only fields, and `freeze_snapshot` has its own refusal. The current refusal says `missing ` followed by field names; it does not use the former prose's `missing:` spelling. Prepare's direct caller uses `publication_input_statement()`.

Recorded judgments may additionally retain evidence custody. The serializer omits absent custody to preserve older record encoding, and supplied custody must retain the original evidence SHA. Caller judgment inputs have no replacement-custody field. `ValidatedCuratorCoherenceGeneration` represents integrity-checked durable content separately from a live authority pointer.

### Knowledge-review assessments

`CuratorCoherenceRecord.assessments` is a separate typed collection, bounded at 256 and checked for assessment-ID uniqueness. It is not added to source-candidate judgment coverage: knowledge subjects and source-file pairs have different identities.

`review_assessment.py` owns assessment records and read projections; `review_assessment_binding.py` compares recorded dependencies with measured values; `review_assessment_store.py` builds and checks collection bindings without deciding semantic equivalence or endorsing a disposition. The dependency builder uses `review-assessment/v1`; its policy requires candidate-state, code-tree, task-intent, semantic-topology, evidence-bytes and validator edges, with memory-tree, predecessor-record and review-record optional. The coherence record declares one `review-record` edge per stored assessment; an assessment does not declare the containing record as its own dependency. Those different directions avoid the self-referential binding described by the existing contract.

The measurement vocabulary distinguishes not-measured, measured and unavailable observations. A binding reports `unavailable` when measurement failed, `stale` when a measured value disagrees, `not-measured` when declared identities remain uncovered, and otherwise `current`. An empty mapping is a completed measurement with no values, not a measurement failure; coverage of the assessment's declared identities still decides its binding state. The comparison does not decide equivalence, and stale judgments remain readable.

Subject projections distinguish `none-recorded` from `not-measured` and `unavailable`. Currentness counts must describe and partition the entries. Independently, unresolvedCount must equal the number of entries whose disposition is unresolved, not merely be bounded by assessmentCount. Their status follows stale, unavailable, unresolved, not-measured, then current precedence. `assessment_state_for` accepts explicit statuses rather than an instruction to assume currentness.

Direct operation input carries optional leafId as retry identity while old journals default it to None. Shared evidence-dependency capacity follows from bounded record populations, including coherence judgments and assessments; valid unrelated evidence need not be coarsened to a bare historical count. Model bounds still refuse before artifact writes.

### Retained comparison availability, not the live judgment pane

`comparison_records.py` defines ComparisonAssessmentAvailability for immutable comparison manifests.
An answered collection requires its recorded count; none_recorded requires zero, recorded requires a
positive count, and unanswered states carry no count plus a recovery action. These guards constrain
supplied values; they do not independently measure the collection or authenticate artifact bytes.
Retaining this descriptor does not restore the removed observation/evidence/assessment reviewer pane.
The current live review has its separate judgment/proof contract. Read its concrete model card for
manifest-versus-physical-artifact validation ownership.

## Invariants and boundaries

- Consumers should import the owning vocabulary rather than duplicate literal sets. This is a standing ownership rule, not proof that every consumer conforms.
- Response and operation models retain strict unexpected-field rejection. Strictness does not mean all compatibility decoding is absent: both operation and curator records decode legacy missing task intent into the explicit `missing-intent` state. The former blanket absence promise conflicts with these deciding predicates.
- Actual Git head/tree facts are distinct from filtered content-tree facts. The mutation snapshot owner excludes root `memory.md` from its isolated content, index and candidate trees when memory-cache filtering is selected, while retaining actual head/tree facts. The surviving kernel `ExistingGitPreparationBinding` explicitly separates immutable Git `tree` from optional `memory_content_tree` in the admitted memory-cache domain. The old prepared-memory reuse/new-output consumers are removed, not the actual-versus-filtered model distinction. These are consumer-source predicates, not effects performed by the model or execution evidence from this account.
- Selected certification belongs to its exact operation key and generation. Completed integration certification must bind the original selection and admitted code commit; structurally valid references do not prove stored publication bytes.
- `recordRevision` and `meaningfulRevision` have different purposes. The meaningful-state subset includes both certification selection cells; the store's transition checks require meaningful revision to advance precisely when that subset changes. The public envelope carries the meaningful cursor separately from its record-bound identity.
- Worker exit requires an observation timestamp. Cancellation evidence requires nonempty expected facts and exact observed equality. Its `workerExitProven` field is a boolean declaration; this model's own validator does not require it to be true. Executing cancellation authority requires separate verification.
- Accepted input, source/target authority, mutation history, irreversible boundaries and worker facts belong to durable operation state rather than being inferred from queue presence. The original retry/recovery/successor and legacy fail-closed behavioral promises are retained as contracts requiring their executing owners' confirmation.
- Assessment currentness must report what was measured. Missing measurement is not favorable evidence, a failed measurement is not an empty successful measurement, and a summary cannot contradict its entries.

## Authority uncertainties

No lifecycle authority or task-status record was assigned to this review. Historical leaf names and dates are not current status or acceptance evidence. No test, differential probe, installation or product validation was executed. The earlier 80-shape probe and registered-tool regression claim are historical assertions whose evidence was not examined.

The original claim that normal closeout/integration workers do not select, populate or require retained certification fields is not established by model optionality or the examined generation constructor alone. Confirmation belongs to the executing workers. Likewise, deletion provenance for `door_response.py`, `successor.py` and the retired ledger intent, schema-1 removability, queue-invalidation survival, and the complete integration/refusal behavior remain outside the deciding source excerpts examined here. These uncertainties do not assign a new lifecycle status or change standing intent.

## File-Level Onboarding Map

- [comparison_records.py](comparison_records.py.md) — retained manifest availability, not a live pane.
- [review_assessment.py](review_assessment.py.md) — stored assessment/count/currentness projection.

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`finalize.py.md`](finalize.py.md) — terminal task-finalization response.
- [`operation.py.md`](operation.py.md) — asynchronous lifecycle operation inputs, record, and projection re-export.
- [`certification.py.md`](certification.py.md) — exact closeout selection, retained memory observations and append-only original terminal history.
- [`integration_certification.py.md`](integration_certification.py.md) — full integration selection, original completion identity and retained interrupted terminals.
- [preparation.py](preparation.py.md), [preparation_state.py](preparation_state.py.md) and [prepared_memory.py](prepared_memory.py.md) — private preparation vocabulary and logical/physical execution views.

## Child Overviews

None.

## How To Use This Area

Read the focused model card, then its producer and consumer references. Use the governing models overview for registry-wide response conventions.

## Evidence



- Native task stage/activity/eventAt is declared separately; the removed session response/state vocabulary is not an operative model in this route. [1]
- Finalization declares terminal facts, cleanup/archive and activation facts; it declares neither edge proof nor completion-seat result sets. [2]
- Asynchronous operation records keep private execution identity out of the declared public projection fields. [3]
- Recovery records have code and memory-content output-commit fields. [4]
- A filtered content head does not replace actual Git head/tree facts. [5]
- Prepared state has an ordered two-leg prefix. [6]
- Closeout and integrate inputs retain their kind-specific accepted decisions. [7]
- Organizational completion proof requires original full-prefix references and the exact selected integration authority. [8]
- Enclosure address models. [9]
- Worker termination evidence. [10]
- The durable record owns both revisions; its meaningful subset includes both selected certification cells. [11]
- The public envelope carries the wait cursor beside versioned identity and component bindings. [12]
- Strict operation decoding explicitly represents missing legacy task intent. [13]
- Publication inputs, refusal text, record coverage and evidence custody have deciding predicates. [14]
- Prepare consumes the shared publication input statement. [15]
- Preparation output-command requirements are conditional on retained command history; transitions preserve original observations. [16]
- Measured binding status separates failure, disagreement and incomplete coverage. [17]

- Finalization forwards supplied agent archive reports. [19]

- The exact assessment dependency policy and record-to-assessment edge are separately constructed. [20]
- The memory mutation snapshot preserves actual Git head and headTree while computing cache-excluded contentHeadTree, indexTree, candidateTree and status; removed prepared-memory reuse/output consumers are not current callers. [21]

- Currentness partitions entries while unresolvedCount independently equals their unresolved dispositions; status follows the actual recorded population. [18]
- ComparisonAssessmentAvailability is a retained manifest descriptor, not a current reviewer channel: answered counts and recovery requirements are structurally checked, not independently measured or semantically endorsed. [22]
