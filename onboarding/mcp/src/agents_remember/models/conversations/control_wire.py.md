# mcp/src/agents_remember/models/conversations/control_wire.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/control_wire.py` (260731-EFA-L9, R2/R8) is the shared control-plane wire
vocabulary consumed by the conversation services and the harness control plane: control/activity/
acceptance state, identities, pending interactions, submission evidence, and their wire
serializers. Declaration bodies are unchanged from the pre-split module.

## Code Commentary

### Logic

The vocabulary starts with the admission limits `MAX_SUBMIT_ASSETS`/`MAX_SUBMIT_ASSET_BYTES`/
`SUBMIT_ASSET_MIME_TYPES` (cit:([`MAX_SUBMIT_ASSETS`], mcp/src/agents_remember/models/conversations/control_wire.py:43-43)) and the state/identity families
(`ControlIdentity` cit:(["class ControlIdentity"], mcp/src/agents_remember/models/conversations/control_wire.py:59-59), `AdapterSnapshot`,
`AssetReference`), through the operation timeline (`OperationTimelineItem`/`OperationTimeline`
cit:(["class OperationTimeline:"], mcp/src/agents_remember/models/conversations/control_wire.py:257-257)), submission provenance
("class SubmissionProvenance:"/"class SubmissionProvenanceBatch:" cit:(["class SubmissionProvenance:"], mcp/src/agents_remember/models/conversations/control_wire.py:268-268)),
`SubmissionAuthorityDescriptor` (cit:(["class SubmissionAuthorityDescriptor"], mcp/src/agents_remember/models/conversations/control_wire.py:288-288)), and
`ControlSubmission` (cit:(["class ControlSubmission"], mcp/src/agents_remember/models/conversations/control_wire.py:462-462), moved here from
`serving/harness_control_client.py`). The wire helpers (`interaction_question_json`,
`pending_interaction_json`, `snapshot_json`, `receipt_json`, `withdrawal_result_json`,
`asset_reference_json`, `withdrawal_recovery_json`, `interrupt_result_json`,
`operation_timeline_item_json`/`_wire_bytes`, `submission_provenance_json`,
`submission_provenance_batch_json`, `read_asset_bytes`) serialize the shared contracts.

### Invariants And Boundaries

- One declaration per shared wire contract: the control plane imports from here; conversation
  modules never import `serving.harness_control_models`/`harness_control_client` for these names
  (R8, layering rail enforced).
- The L9 delta is a one-line docstring on `SubmissionAuthorityDescriptor`; no field, alias, or
  serialization behavior changed (move ledger M13/2b).

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- Conversation control identity is declared in this shared wire owner. The deleted architecture suite no longer enforces import direction. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
