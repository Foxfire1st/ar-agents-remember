# mcp/src/agents_remember/cli/paseo_role_tools.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Implements single-role starts, the Manager-owned leaf-set start and receipt-bound role messaging over the public launch/runtime owners.

## Code Commentary

Caller binding decides may-start pairs and sprint/master containment. Starts call launcher dispatch with native parent, and only starter or dashboard may replay a stored request. Recipients resolve through current-line receipts. Self-addresses and ambiguous/cut candidate sets refuse; a leaf seat with two live agents is ambiguous too. An unfinished start, permission prompt or unwritable running turn instead holds a message in the recipient workspace when its receipt locates that store. Native message delivery/resume/wait results keep explicit refusal and uncertain-delivery shapes; no second hosted AR seat is created here.

Closed-recipient resume calls `role_activity.resume_role_agent` with the saved receipt, publishing its identity before native resume. `_started` only builds the start answer; post-success role-facts publication was removed from it. The launch-receipt owner publishes before launch/replay. Best-effort publication does not imply host consumption, delivery or task acceptance.

Since 260928-MIK-L114 `send_role_message` carries the resolved recipient's role for the
river (`_carry_resolved_target_role`): the payload builder only sees the call, whose role
is absent for id-addressed recipients, so the durable receipt's recorded role is set on
the context variable the completed event reads. Nothing is guessed — with no role on
receipt or call the event stays literal.

## R93 refusal-remedy account — local and shared recovery owners

Four `nextAction` remedies that still leave the message transportable (`_archived`, `_resume` scope-changed, `_resume` cannot-resume, `_undelivered`) now name the parent with `role_message` on `agents-remember-task` first and the own chat only for an agent without one. The no-runtime and host-unreachable remedies keep their own-chat advice, while unavailable-recipient delivery now uses the held-store owner rather than asking the sender to repeat a message that was taken as held.

## Leaf sets and held-message admission

Only the leaf’s owning Manager may call `start_leaf_set`; the ordinary caller may-start matrix still guards each seat. `dispatch_leaf_set` prepares Worker, Reviewer and Curator as siblings, opens Worker immediately and leaves Reviewer/Curator held unless reviewer work is carried. A repeat retains the deterministic per-seat request identities. Single-role starts retain their ordinary opening, with explicit authorized replacement for an occupied leaf seat.

`send_role_message` does not let a new message overtake waiting work. A held answer names its reason, waiting ID and sender/total counts, rather than claiming acceptance by the host. `withdraw_held_message_id` withdraws only the sender’s uncommitted waiting message; a live delivery claim refuses withdrawal. Archived-recipient answers still expose the sender’s retained terminal outcomes. The host permission guard remains: holding never answers the prompt.

## Current role-message facade and recovery owner

The supported successor composition is not the Attempt-4 thin facade. `role_message_limit` reloads effective settings and `send_role_message` applies the shared text refusal. Only after recipient resolution succeeds does the ordinary prologue collect reports, locate the recipient, file the message and dispatch locally. An unfinished-start resolution instead returns through `_hold_for_unresolved` before report collection and `_file_message`; its `_MessageSend` has no filed identity, so this branch does not establish a retained body/attachment file or file/hash wake pointer. That implementation gap does not weaken the normative filing obligation.

`_deliver_or_hold` preserves held-message ordering. Its unheld branch enters facade-local `_deliver`, admits Investigator capacity before native send/resume, waits outside the lock and invokes the imported long-reply helper only when `filed` exists. `_held_then_delivered` merges `wait_for_turn` directly without that helper, so a successful held drain does not establish the ordinary character-cut/full-reply-file guarantee. The local capacity refusal is caught by the prologue and retains the filed refusal record; `role_message_delivery` holds no private delivery dispatcher to contrast it with. These are source-attribution limits for Owner/Worker disposition, not a new runtime result, waiver or CODE repair. Body/attachments travel as a file/hash line only on branches whose filed identity exists.

`role_message_delivery` is the selected shared library for file preparation/storage, links, text refusal, successor naming and long-reply filing; its remaining recipient-resolution helpers are not this public call path, and its uncalled duplicate `_deliver`/`_send` routines are gone. The prologue's shared archived answer can name a known live successor, while local resume/refusal constructors preserve their own explicit recovery boundaries. No-runtime/host-unreachable advice, actual-parent-ID questions and ordinary role/task returns remain separate; no remedy unarchives an old agent.

The Worker successor/addendum reports the composed 1835-line file breaches the 1200-line F04 rail, unlike its earlier 583-line facade. The original ONE D140 records that limitation. Architect ruling b17b9a0a permits size-named landing and assigns the later split to L68; it neither waives the rail nor repairs this file. This source-ownership account is not MEMORY acceptance or a new CODE PASS; ONE D140 is not reopened here.

## Hold-versus-send decision and the delivery answers

Before a native send, `_deliver` reads the host's own activity record through `agent_in_turn`. When that record says the recipient is in a turn the message is not sent: the refusal is `recipient-busy` with `holdReason` `recipient-in-turn`, and the caller holds it under the held-store owner. The bridge makes the second read at the moment of the send and answers `busy` for any provider it does not know to take a steer, so every such message is held rather than sent into the turn.

A delivery that carried held messages answers `ok` with `status` `accepted` and carries no `turnId`; `RoleMessageResponse` validates it, and the turn id stays available to a caller that waits. A send the host did not answer is held with `host-unreachable` and the answer says the message is held, not lost. `_name_replacement` reports a replaced running turn on both answer paths: `taken` is `replaced` and the warning states plainly that the runtime replaced the recipient's turn to take the message, and that the turn did not continue because it was cancelled.

## Feature passthrough, choice metadata and message-time collection

`_agent_override` passes speed `featureValues` through even without an agent/model/effort override, and still refuses a model or effort without its agent. The start answer carries launch-choice metadata, task-document files and any warning beside preparation. `send_role_message` collects the sender's own execution reports before delivery when its receipt matches the bound agent; a collection failure is recorded and returned alongside the delivered message rather than blocking it.

## Grant-backed leaf preparation and revival

Message-time leaf resume uses the same call-time grant-aware scope verifier as dashboard Revive before native resume. The saved canonical leaf and master series contract must equal the current granted pair; an ordinary leaf retains its enclosure comparison. Receipt evidence never replaces the live grant. Recipient identity, parent-first remedies, uncertain delivery, report collection and role containment remain separate contracts.

## Current Contract — Scoped Launch And Settings Changes

_start_role carries call.step_up into the typed RoleDispatchRequest beside unchanged selection, override, replacement and chat-start facts. It does not manufacture a settings alternative or bypass the caller/start matrix.

_started delegates receipt-based answer projection to role_start_answer.started_answer. Running/held/unknown/refused meanings and report paths remain receipt-derived; the extracted answer adds observed step-up disclosure and conditional same-request recovery advice for an empty retryable successor. Plugin role-facts publication is not an answer-side effect: the receipt-aware launch/resume owners publish before their host call, best effort and separately from host execution.

The role-message facade, native held ordering, recipient identity, parent containment, scope-sensitive revival and report collection are unchanged by this extraction. This module is not an independent review or task-acceptance owner.

## Evidence



- Frozen implementation of _start_role supporting the stated file behavior. [2]
- Frozen implementation of _resolve_recipient supporting the stated file behavior. [3]


- Checks foreign IDs and self-addresses are refused. [6]
- Checks live taskless-role ambiguity reports IDs and sends no message. [7]
- Exceeding 24 reads refuses and discloses list cut rather than selecting newest agent. [8]

## MIK-R95 Preparation Answer

A `RolePreparationError` cause is projected into the `launch-refused` answer with its exact owner status, detail and next action, and `preparationStatus`; a successful answer carries the receipt's `preparation` block and appends `_projects_preparation_note`, which states that a masterless Projects workspace was opened and that the host reports no creation outcome. Nothing infers the outcome from timing or a pre-call list.
## 260928-MIK-L96 Host remedy texts

The role-start host remedies now name the install step where the host is not installed and the one start where it is down, so an agent started by a dashboard without a reachable host is told the same thing the dashboard line says.

- The host-unreachable remedy that names the install step and the one start. [9]

## Investigator scope and request identity

Architect, Orchestrator and Manager may start Investigator only within their admitted Projects/sprint/master containment; Investigator, Worker, Reviewer and Curator start no role. A role-addressed selected Investigator is resolved against the complete open request set, with exact IDs in an ambiguity refusal. A message that would start a new turn on a completed selected-task Investigator enters the shared selection capacity owner before send/resume; steering an already open execution keeps its slot. Host wait remains outside that short admission operation.


- The current source implements this file’s stated Investigator boundary. [10]


## Refreshed current evidence

- Frozen implementation of start_rule_violation supporting the stated file behavior. [1]



## Refreshed current evidence

- Checks all 49 caller/target pairs against exact table. [4]
- Checks own orchestrator sprint and manager sprint/master binding containment. [5]

## Supported successor's operative seams

- Public message call uses local resolution, report collection, prologue filing and held/native dispatch rather than the retained delivery-module dispatcher. [11]
- After ordinary recipient resolution succeeds, the prologue constructs the filed identity from shared attachment/link/store primitives before that resolved-recipient delivery; unfinished-start holding returns through _hold_for_unresolved before _file_message and has no filed identity. [12]
- Unheld native dispatch owns capacity/send/resume and invokes shared long-reply filing after its wait. [13]
- Upstream held-message ordering is decided before native send; permission holding never answers a prompt. [14]

- Leaf revival compares current grant-sensitive canonical task/contract scope before bridge use. [11]

- Typed public start conversion includes stepUp. [15]

- Projection now delegates to the extracted answer owner. [16]

- Readback, provenance and retry advice are extracted without changing receipt identity. [17]


- On valid saved receipt context, role-facts publication belongs to pre-launch/replay and receipt-aware resume, not to the post-answer projection; filesystem/runtime publication is best effort, not host execution or plugin-consumption evidence. [18]
