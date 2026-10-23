# mcp/src/agents_remember/cli/role_launch_receipts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns durable current-line launch receipts, immutable saved-call replay, report binding and public projection.

## Code Commentary

Receipt-directory vocabulary is defined by `controlplane/held_store_discovery.py`; this module imports `EXECUTIONS_DIRECTORY` and keeps that existing public name.

Receipt creation is exclusive and complete before native launch. `_execute_prepared_launch` republishes receipt-bound role facts before the native launch/replay call; this best-effort publication and host execution are separate boundaries, not one atomic transaction; unknown outcomes retain replayRequest with original UUID/prompt/options. Resolved ordinary receipts drop replayRequest. A rejected step-up with a settled predecessor and no lost successor instead retains its saved call for same-request retry; other rejections remain closed. A created held seat instead keeps its saved call and opening handover, reports `held`, and restores the artifact from `heldOpeningPrompt` on retry without inventing a first message. Public projection names an eligible leaf holder for the launcher; closing-mark refusals still override retry/revive/start affordances without erasing archival debt. Taskless canonical storage/migration remains bounded to exact receipt identities; old schema at current address refuses, previous host receipts are not execution authority. Public execution whitelists lifecycle fields and requested/observed tier disclosure, never task acceptance.

`_read_receipt` distinguishes a missing receipt from an unreadable or malformed one: non-regular paths refuse, decoding/JSON/value-conversion/depth failures return HTTP 409 with reconcile advice, and non-object/wrong-schema records are malformed. The document reader adds shared chat-shape validation; none of these refusals rewrites a receipt or starts/replays a launch. A retry restores both hand-over files through `role_handover_restore.py` before it sends, and a receipt without the second file's reference keeps the text file's rules alone.

## Closing mark and archive settlement (MIK-R76)

`_execute_prepared_launch` reads the leaf closing mark before replaying a saved call and re-checks it
under the receipt lock after creation, so a retired start is refused instead of publishing a running
receipt. `_write_receipt` serializes short metadata publication under the existing lock and merges
the same request's closing marker, archive debt and refusal facts when a stale ordinary writer
publishes, so a concurrent settlement is not erased. The existing request-ID reconciliation and
saved-call replay semantics are otherwise unchanged.

## Predecessor reports, observed choices and public fields

`_execute_prepared_launch` collects predecessor reports before running and settles them after the host answers; a settlement failure keeps the host's actual result and records the collection error instead of misreporting. The imported compatibility name `_observe_launch_choices` delegates to `role_launch_choices.observe_launch_choices`: it records requested/observed model, effort, mode and feature facts, updates a step-up’s displayed model while retaining requestedModel, and warns on stated mode/feature mismatches. The former local implementation no longer exists here. `_public_execution` additionally exposes `choices`, `instructionComposition`, `taskDocumentFiles`, `assignmentReadGrant`, `predecessorCollectionError` and `reportCollection`. `_request_digest` drops an empty feature map so old requests keep their digest, and `_archived_receipt_for_selection` returns the archived receipt so the dispatch route can record predecessor reports.

## Current Contract — Scoped Launch And Settings Changes

_execute_prepared_launch honors closing barriers, reconciles the task step-up decision before execution, restores/verifies saved artifacts, collects predecessor reports and renews step-up predecessor liveness before the native call. After publishing a nonclosing host outcome it reconciles observed choices into the same task decision; a failed acknowledgment keeps receipt facts for same-request recovery, not a second launch.

_restore_launch_handover rebinds report access and hands the saved targets to `restore_launch_files`, which rebuilds a lost request locator, validates every frozen detail and restores or verifies the primary, takeover and complete-hand-over files before the first message is sent. Missing detail bytes require original snapshots, never current-corpus regeneration, and a receipt that records no artifact pair keeps the detail validation alone. A detail-free legacy composition remains permitted.

Outcome publication and observed choice bookkeeping move to role_launch_outcome and role_launch_choices; this file keeps compatibility seams. Rejected settled empty step-up receipts retain replayRequest, while ordinary resolved launches drop it and held seats retain their opening call.

_request_digest includes stepUp only when explicitly present, keeping absence-compatible digests. _public_execution exposes stepUp and permits rejected-stepUp retry only with a saved call; retryPayload includes the original requested reason and overrides. This projection is not a new review verdict or unconditional permission to start.

Existing schema/read refusals, exclusive receipt creation, canonical taskless identity, closing/archive debt and predecessor report custody remain in force.

## Evidence


- Frozen implementation of _create_receipt supporting the stated file behavior. [2]
- Frozen implementation of _read_receipt supporting the stated file behavior. [3]


- Interrupts between receipt and call and checks retry retains one agent identity. [6]

- Races publication and checks one persisted winner; competing request cannot issue another launch. [8]

- Checks unresolved/rejected receipts returned unchanged without host read. [10]
- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [11]


## MIK-R95 Preparation Receipt

A successful launch receipt records the public open outcome it observed: `receipt.preparation.workspace` is `created`, `found` or `opened` when the outcome names one, and the enclosure's own `created`/`found`/`not-applicable` value is carried beside it. `_public_execution` exposes the `preparation` block to the role-start answer.

## Investigator scope and request identity

Selected-task Investigator receipts are per request rather than singleton selections. Read normalization exposes the canonical role with the one notice while keeping original stored role, labels, request/agent IDs and report paths. Same-request replay still answers from the recorded call; a new source tree is never a reason to rewrite the first assignment. Task ownership and complete-set capacity are delegated to investigator_receipts, with no second receipt writer.


- The current source implements this file’s stated Investigator boundary. [14]


## Refreshed current evidence

- Frozen implementation of _execute_prepared_launch supporting the stated file behavior. [1]
- Frozen implementation of _public_execution supporting the stated file behavior. [4]
- The launch observer checks complete receipt, stable UUID and stored call before runtime launch. [5]
- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [7]
- Through leaf/taskless routes checks restoration/refusal, exact advice and unchanged receipt/foreign link target. [9]
- Pins delivered worker doctrine: one parent role_message after report, none for dashboard-started worker, and a finished turn is not AR acceptance. [12]
- Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation. [13]

## Current contract evidence

- `_read_receipt` distinguishes a missing receipt from an unreadable or malformed one: non-regular paths refuse, decoding/JSON/value-conversion/depth failures return HTTP 409 with reconcile advice, and non-object/wrong-schema records are malformed. The document reader adds shared chat-shape validation; none of these refusals rewrites a receipt or starts/replays a launch. [15]

- Decision, artifacts, predecessor liveness and outcome reconciliation preserve saved identity. [16]

- Replay validation binds primary/detail/takeover artifacts. [17]

- Optional reason enters request identity without altering absent requests. [18]

- Conditional retry payload preserves original selection/reason. [19]

- Test source checks validator refusal before host replay. [20]
