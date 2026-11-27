# mcp/src/agents_remember/cli/role_launch_routes.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Registers role launcher options/dispatch/result/frame APIs and serializes preparation/retry/revive.

## Code Commentary

After the Manager owns its starting receipt, the route records an Architect address when it can identify one. For an Orchestrator starter, identifying that address requires both a corroborated Orchestrator launch receipt whose `agentId` matches `started_by.agent_id` and an Architect launch receipt for that receipt's `parentAgentId`. Launch proceeds if the lookup finds no address or the write fails.

### Current Contract

Launch preparation and receipt records retain their internal identity and task-copy metadata. Missing requirement sources are reported as `missingCopies` in handover/index/receipt and a warning rather than failing a start solely for that absence; later canonical task publication refreshes copies when sources exist. Ordinary delivered `role_start` success carries the compact agent ID and handover fields. The starting receipt keeps any `briefsProblem` from workspace preparation, and the start answer can carry it in the warning alongside a product notice report. The launcher invokes its notice handler after a successful dispatch response, using the stored receipt to recognize an opened leaf Reviewer or Curator.

`_start_execution` wraps `role_start_execution.start_execution`, which reconciles a matching receipt before recompiling and rejects reused request identity or another starter through the retained route seams. `_launch_prepared_role_session` writes artifacts and the complete starting receipt before the saved runtime call. Leaf Revive (`_revive_execution`) checks recorded/current grant-aware task scope before any bridge operation. Register these APIs through serving injection before static mount alongside the read-only report route (`role_report.register_role_report_route`). Both handover files are published before the start is sent, settling the request's own locator before the first write and refusing a collision or retarget before either file exists. When a non-held launch carries a direct `opening_message` exceeding `settings.role_message_limit` (resolved once at launch preparation from the selection repository), `_launch_prepared_role_session` bounds it via `role_opening_offload.prepare_direct_opening_message`, preflights `<report_stem>.opening-message.md` before `publish_handover_files`, writes it read-only before `build_launch_call`, and records `openingMessageArtifact` in the starting receipt so replay stays immutable if settings change later and write failures refuse before host `agent-create`. When applicable, `acp_launch_instruction` appends after `bounded_opening` before handover publication.

## Leaf-set preparation and replacement

`dispatch_leaf_set` serializes one set using the existing dispatch lock. `seat_request_id` derives each seat UUID from the set request and role, so a repeated set completes missing seats without a fourth agent or waking an already held seat. Each seat retains ordinary role settings and preparation. Failure of one seat is returned on that seat and leaves the others standing.

The prepared start writes each held seat's handover, saved `replayRequest`, and `heldOpeningPrompt` onto its receipt (`status: "held"`, `hostAgentExists: false`) without calling host `agent-create`, deferring host creation until the first addressed message opens the seat. Worker opens at once; optional direct `opening_message` (such as Reviewer work on a non-held seat) is bounded by `role_message_limit` and offloaded to `.opening-message.md` when over limit. A successor's handover names the prior report paths. Same-request replay, exclusive receipt publication, source-scope checks and leaf-closing archival debt remain with their existing owners.

`dispatch_leaf_set` branches on whether the leaf carries `consolidationList`: consolidation leaves prepare Consolidator (opened) and Reviewer (held) with no Worker or Curator, while ordinary leaves prepare Worker, Reviewer, and Curator.

## Grant-backed leaf preparation and revival

Dashboard leaf Revive uses the shared grant-aware scope verifier before native bridge revival. It compares the saved canonical leaf and contract against the current pair: readable direct grant plus master series contract, or ordinary leaf enclosure. Stored direct-looking context is not permission. Receipt UUID/reconciliation, capacity, launch-before-runtime and report ownership remain with their existing owners.

## Step-up, catalog questions, progress, and dispatch admission

`_reserve_message_binding_projection` passes the prepared step-up marker to occupancy reconciliation and binds `step-up.from` to the actual predecessor receipt's applied/session choices before storing predecessor reports. `_launch_prepared_role_session` delegates successor prompt assembly to `role_step_up_runtime`, keeps selected `stepUp`, `requestedStepUp`, and `stepUpArtifact` on the starting receipt, and includes `stepUpArtifact` in `bindingDigest` before the saved host call. Missing-copy warnings are composed with step-up warnings without dropping either.

The options and dispatch endpoints share a `launcher_catalog_question` context. Options checks the dispatch lock before host access; requests without a provider/model pair return catalogue metadata and receipt data, paired requests read features for that pair, and `GET /api/role-launch/saved-catalog` reads the durable snapshot without querying Paseo.

Route registration mounts `/api/role-launch/progress/{request_id}`, `register_document_chat_route`, and `POST /api/role-launch/document-chats/tree` (`register_document_chat_tree_route`), claiming progress notices on dispatch and reclaiming them in `finally`, with the dispatch answer carrying `enclosurePreparation`. Investigator dispatch uses the existing selection admission lock; options expose per-request executions and omitted display rows for selected tasks.

The dispatch endpoint takes `_DISPATCH_LOCK` first, runs `role_launch_admission.admit` and `prepare_first_run_for` inside the lock, binds `with_caller_harness` after preparation, preserves completed stages on `refuse_after_preparation`, and records `firstRun` on the starting receipt. Missing-copy warnings and bridge status mapping live in `cli.role_launch_request_rules`.

## Evidence

- Before workspace-open and agent-create, the observer sees the starting receipt, its saved agent ID and the stored artifact. [5]
- Interrupts between receipt and call and checks retry retains one agent identity. [6]

- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [7]

- Races publication and checks one persisted winner; competing request cannot issue another launch. [8]
- Changed/missing saved scope refuses with both pairs, no bridge/write/enclosure creation. [11]
- The existing route delegates preparation/reconciliation to the new owner. [16]
- Occupancy receives the step-up marker and actual predecessor facts. [17]
- The launch-warning builder puts missing requirement filenames before the step-up notice. [19]
- The dispatch endpoint that admits, prepares, binds and refuses in one locked order. [20]
- Cold preparation runs under the dispatch lock, and a later refusal keeps the preparation it made. [21]

- The route registrar mounts the saved catalogue, frame, options, dispatch, result and progress endpoints alongside the document-chat and report readers. [1]
- `_start_execution` wraps `role_start_execution.start_execution` while retaining route seams. [2]

- `_launch_prepared_role_session` bounds direct `opening_message` via `role_opening_offload`, preflights/writes `.opening-message.md` and both handover files, records `openingMessageArtifact` and `stepUpArtifact` in the starting receipt, and builds the saved host call. [3]

- `_revive_execution` verifies grant-aware leaf scope before native bridge revival. [4]
- Checks path, bytes, digest, read-only mode, exact reuse and conflicting-content refusal. [9]
- Checks size limit and refuses links without changing their target. [10]
- The route registrar mounts the document-chat tree beside the selected read and report routes. The tree handler uses one live-agent census for its receipt-derived answer. [14]
- The starting receipt carries task-copy metadata and warns of missing requirement copies ahead of step-up advice; later canonical task publication refreshes copies; the start answer projects identity and handover addresses while whole `role_start` can carry `productMessage`. [15]

- Frozen takeover and requested reason are recorded before the host call. [18]

- The Manager records an Architect address when available; an Orchestrator starter's parent receipt determines whether the address can be recorded; launch proceeds on lookup/write failure. [22]
- The launcher invokes the notice owner after a successful dispatch response. [28]

- The starting receipt retains the workspace brief advisory in preparation, and the role start answer can carry it in the warning. [29]
