# mcp/src/agents_remember/cli/role_launch_receipts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns durable current-line launch receipts, immutable saved-call replay, report binding and public projection.

## Code Commentary

Receipt-directory addressing is defined by `controlplane/held_store_discovery.py`; this module imports `receipt_holder` and uses it to address role receipts and message bindings.

Receipt creation is exclusive and complete before native launch. `_execute_prepared_launch` republishes receipt-bound role facts before the native launch/replay call; this best-effort publication and host execution are separate boundaries, not one atomic transaction; unknown outcomes retain replayRequest with original UUID/prompt/options. Resolved ordinary receipts drop replayRequest. An eligible rejected step-up with a settled predecessor and no lost successor retains its saved call for same-request retry. A saved native Antigravity Retry whose agent is absent settles as rejected and drops its saved call, including on a step-up. A deferred held seat is instead reserved on disk via `role_deferred_held.defer_held_launch` (`status: "held"`, `hostAgentExists: false`, `execution: {}`) without creating a host agent, retaining its saved `replayRequest` and `heldOpeningPrompt` until its first message opens it. Public projection names an eligible leaf holder for the launcher (including deferred held seats via `role_deferred_held.apply_leaf_holder`); closing-mark refusals still override retry/revive/start affordances without erasing archival debt, and `_refuse_closing_launch` accepts `retried_agent_id` to archive retried agents on concurrent close. Taskless canonical storage/migration remains bounded to exact receipt identities; old schema at current address refuses, previous host receipts are not execution authority. Public execution whitelists lifecycle fields and requested/observed tier disclosure, never task acceptance.

`_read_receipt` and `read_enumerated_receipt` are implemented in `cli/role_receipt_files.py` and re-exported here alongside `RECEIPT_SCHEMA`, `_archive_receipt`, `_create_receipt`, and `_now_iso`. `_read_receipt` distinguishes a missing receipt from an unreadable or malformed one: non-regular paths refuse, decoding/JSON/value-conversion/depth failures return HTTP 409 with reconcile advice, and non-object/wrong-schema records are malformed. The document reader adds shared chat-shape validation; none of these refusals rewrites a receipt or starts/replays a launch. Ordinary Retry invokes restoration when the receipt carries a `handoverArtifact` dictionary or a `handoverFile` key. Restoration checks a missing or malformed companion reference. Held-seat opening calls the helper even when neither reference is recorded, so it checks saved instruction details directly in that case.

`read_enumerated_receipt` is the reader for enumerating mixed report folders: valid JSON that is not a receipt of this line returns `None`; unreadable JSON retains the ordinary receipt refusal. The direct `_read_receipt` path keeps its strict schema check.

## Closing mark and archive settlement (MIK-R76)

`_execute_prepared_launch` reads the leaf closing mark before replaying a saved call and re-checks it
under the receipt lock after creation, so a retired start is refused instead of publishing a running
receipt. `_write_receipt` serializes short metadata publication under the existing lock, applies
`preserve_held_closure` and (when `prior_generation is None`) `preserve_retirement`, merges the same
request's closing marker, archive debt and refusal facts when a stale ordinary writer publishes, and
persists via `role_receipt_files._replace_receipt_bytes`. The existing request-ID reconciliation and
saved-call replay semantics are otherwise unchanged.

## Predecessor reports, observed choices and public fields

`_run_prepared_launch` collects predecessor reports before running, routes held launches without a prompt to `role_deferred_held.defer_held_launch` (which archives a live predecessor first, settles it via `finish_replacing_predecessor`, or keeps `pendingArchiveAgentId` debt without reserving on archive/write failure), and for non-held launches delegates confirmed predecessor retirement and folder closure to `role_retirement_receipt.finish_replacing_predecessor` (also settling the predecessor's held store when `settled.predecessor_settled`). The imported compatibility name `_observe_launch_choices` delegates to `role_launch_choices.observe_launch_choices`: it records requested/observed model, effort, mode and feature facts, updates a step-up’s displayed model while retaining requestedModel, and warns on stated mode/feature mismatches.  `_public_execution` additionally exposes `choices`, `instructionComposition`, `taskDocumentFiles`, `assignmentReadGrant`, `predecessorCollectionError` and `reportCollection`, delegating leaf holder and closing-mark projection to `role_deferred_held`. `_request_digest` drops an empty feature map so old requests keep their digest, and `_archived_receipt_for_selection` returns the archived receipt so the dispatch route can record predecessor reports.

## Current Contract — Scoped Launch And Settings Changes

_execute_prepared_launch honors closing barriers, reconciles the task step-up decision before execution, restores or verifies saved artifacts and collects predecessor reports. For a step-up receipt whose saved call names an `archiveAgentId`, the executor rechecks the predecessor before the native call. After publishing a nonclosing host outcome it reconciles observed choices into the same task decision; a failed acknowledgment keeps receipt facts for same-request recovery, not a second launch.

_restore_launch_handover rebinds report access and hands the saved targets to `restore_launch_files`, which rebuilds a lost request locator, validates every frozen detail and restores or verifies the primary, takeover and complete-hand-over files before the first message is sent. Missing detail bytes require the original snapshots. Held-seat opening without either recorded artifact reference validates the saved details directly. A detail-free legacy composition remains permitted.

Outcome publication, deferred held reservation, and observed choice bookkeeping delegate to `role_launch_outcome`, `role_deferred_held`, and `role_launch_choices`; this file keeps their imported and forwarding names. `_execute_prepared_launch` passes `LaunchExecutionPolicy(mode="create", on_retry_agent=...)` so a binding-confirmation retry immediately re-publishes `role-agents.json` for the retried agent ID, and `_public_execution` exposes `bindingConfirmation` when recorded on the receipt. An eligible rejected empty step-up retains `replayRequest` when the predecessor settled and the outcome reports no lost agent. If saved native Antigravity Retry finds its recorded agent absent, the HTTP 409 refusal settles the request and drops `replayRequest`. Other resolved ordinary launches drop it, and held seats retain their opening call.

_request_digest includes stepUp only when explicitly present, keeping absence-compatible digests. _public_execution exposes stepUp and permits rejected-stepUp retry only with a saved call; retryPayload includes the original requested reason and overrides. This projection is not a new review verdict or unconditional permission to start.

Existing schema/read refusals, exclusive receipt creation, canonical taskless identity, closing/archive debt and predecessor report custody remain in force.

## Evidence



- Frozen implementation of `_create_receipt` (extracted to `role_receipt_files.py` and re-exported here) supporting exclusive initial receipt creation. [2]


- The receipt reader (defined in `role_receipt_files.py` and re-exported here) distinguishes absence, unreadable bytes, invalid JSON and wrong or non-object receipt schemas. [3]





- Interrupts between receipt and call and checks retry retains one agent identity. [6]





- Races publication and checks one persisted winner; competing request cannot issue another launch. Anchor: `RepeatAndConflictTests.test_a_task_bound_receipt_is_created_exclusively` [8]



- Checks unresolved/rejected receipts returned unchanged without host read. [10]

- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [11]



## MIK-R95 Preparation Receipt

A successful launch receipt records the public open outcome it observed: `receipt.preparation.workspace` is `created`, `found` or `opened` when the outcome names one, and the enclosure's own `created`/`found`/`not-applicable` value is carried beside it. `_public_execution` exposes the `preparation` block to the role-start answer.

## Investigator scope and request identity

Selected-task Investigator receipts are per request rather than singleton selections. Read normalization exposes the canonical role with the one notice while keeping original stored role, labels, request/agent IDs and report paths. Same-request replay still answers from the recorded call; a new source tree is never a reason to rewrite the first assignment. Task ownership and complete-set capacity are delegated to investigator_receipts, with no second receipt writer.




An Investigator receipt address requires its exact request UUID.




## Refreshed current evidence








- The public execution whitelist includes request identity, status, observed choices and eligible Result, Retry or Revive information drawn from the same receipt. [4]









- Before workspace-open and agent-create, the observer sees the starting receipt, its saved agent ID and the stored artifact. [5]








- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [7]




- Through leaf/taskless routes checks restoration/refusal, exact advice and unchanged receipt/foreign link target. [9]




Past-epoch account (retained wording): - Pins delivered worker doctrine: freeze the candidate and hand it directly to the leaf's Reviewer; the Manager receives no routine report notice. A dashboard-started Worker has no parent, and a finished turn is not AR acceptance.

Custody: the preceding sentence is detached from live reference 12; its original target blob(s) were `74a051a27a76bfa2d21ab404b581911d5e391701`. The current clause below is separately bound.

- The Worker handover test requires a first freeze notice to the Manager to start the Reviewer, followed by direct complete freeze handover to that Reviewer; the Manager does not relay it or receive routine report notices. It also checks parentless Worker and turn-end-versus-acceptance wording, with mutation cases for every required route clause.
Past-epoch account (retained wording): - Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation.

Custody: the preceding sentence is detached from live reference 13; original target blob(s): `74a051a27a76bfa2d21ab404b581911d5e391701`.

- The test joins the shipped Architect/review, Manager/coordination and Orchestrator/coordination source texts, checks their candidate-evidence and owner-acceptance clauses, and detects removal of Manager inspection. This checks that source composition’s wording; it runs no capsule admission/compilation and proves no runtime no-mutation property.

## Current contract evidence



A receipt moved by Start between inspection and reading is treated as absent.





- Decision, artifacts, predecessor liveness, predecessor replacement settlement, deferred held routing, and outcome reconciliation preserve saved identity. [16]





- Ordinary Retry enters restoration for a recorded artifact reference. The restore path checks its targets and validates frozen detail references before writing. [17]




- Request identity includes a supplied step-up value and normalizes an override with an empty feature map. [18]




- Conditional retry payload preserves original selection/reason. [19]



- Test source checks validator refusal before host replay. [20]

## The message-binding address admission reads

`message_binding_projection_path` is the public name of the binding-file address; the request-id refusal and the discard path use it too. Admission reads the same file a preparation wrote, which is how a retry whose receipt never landed returns to the seat it prepared instead of preparing the root again. Receipt creation, replay and projection semantics are unchanged.

- The one binding-file address, read by admission and written by preparation.

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/cli/role_launch_receipts.py::message_binding_projection_path - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The Worker handover test requires a first freeze notice to the Manager to start the Reviewer, followed by direct complete freeze handover to that Reviewer; the Manager does not relay it or receive routine report notices. It also checks parentless Worker and turn-end-versus-acceptance wording, with mutation cases for every required route clause. [12]


- The test joins the shipped Architect/review, Manager/coordination and Orchestrator/coordination source texts, checks their candidate-evidence and owner-acceptance clauses, and detects removal of Manager inspection. This checks that source composition’s wording; it runs no capsule admission/compilation and proves no runtime no-mutation property. [13]



- The receipt executor restores stored launch artifacts when present, runs the same saved launch call (or delegates deferred held starts), settles confirmed predecessor replacements, and publishes the observed outcome. [1]


- `_read_receipt` (in `role_receipt_files.py`, re-exported here) distinguishes a missing receipt from an unreadable or malformed one: non-regular paths refuse, decoding/JSON/value-conversion/depth failures return HTTP 409 with reconcile advice, and non-object/wrong-schema records are malformed. The document reader adds shared chat-shape validation; none of these refusals rewrites a receipt or starts/replays a launch. [15]



- The current source implements this file’s stated Investigator boundary. [14]
