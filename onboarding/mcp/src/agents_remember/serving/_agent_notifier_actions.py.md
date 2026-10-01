# mcp/src/agents_remember/serving/_agent_notifier_actions.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Applies one evaluated agent-notifier finding through durable inbox transitions, structural owner
rebinding, shared delivery, and observer evidence.

## Code Commentary

Expiry batching first requires a source id and a still-pending row. Rebind expiry resolves the current structural owner and refuses a missing task address; a changed owner returns to ordinary re-evaluation rather than expiring the stale recipient. Seat/routing ambiguity is caught per finding before transition batching, so unrelated expiries and their ordered results continue. The ordinary pending-TTL expiry retains its own direct terminal transition. cit:([`act_on_findings`, `_prepare_known_expiry`, `_prepare_pending_expiry`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:722-849).

L23 batches independent inbox expiry transitions through one durable `transition_many` write while preserving per-finding order, event emission, readdressing, and skip results.

State-signal emission revalidates the current finding, derives its structural owner at action time from the subject's current task-document binding, and refuses a role/document-only address when no current occupant has an agent id. The source remains eligible for a later sweep in that case. `TaskDocumentRefError` is contained at both ordinary action and expiry-preparation boundaries so malformed topology fences only that subject. The emitted marker is no longer a post-return write: `_emit_state_signal` supplies `OwnerSignalOptions.after_persist`, so `record_state_signal_emitted` runs after the row is durable and on the sweep fold and strictly before the delivery attempt. Delivery eligibility is then re-checked at the shared action by `_state_signal_awaits_marker`, a guard clause at the top of `_redeliver` that `_drain_boundary` inherits by delegation. cit:([`_emit_state_signal`, `_state_signal_awaits_marker`, `act_on_finding`, `act_on_findings`], mcp/src/agents_remember/serving/_agent_notifier_actions.py:489-561; mcp/src/agents_remember/serving/_agent_notifier_actions.py:98-122; mcp/src/agents_remember/serving/_agent_notifier_actions.py:736-763; mcp/src/agents_remember/serving/_agent_notifier_actions.py:766-822).

### Logic

`_rebind_due` rewrites a pending row's structural address/owner to the current qualified occupant
before delivery. Expiry and unresolved paths write explicit terminal snapshots. State-signal,
compound-idle, and non-reaction actions use the same structural routing and shared whole-message
delivery; boundary drain records adapter acknowledgement.
`act_on_finding` contains typed occupancy/routing/task-document failure to the one finding as a skipped result.
`act_on_findings` applies the same containment before expiry batching, so an ambiguous expiry
mailbox cannot abort preparation or prevent unrelated expiry transitions and the sweep heartbeat.

`_state_signal_awaits_marker` is the action-time half of the state-signal recovery contract, and it
exists because predicate-side filtering cannot guarantee the durable order: `evaluate_predicates`
already excludes a held state-signal row from the *generic* redelivery finder, but
`evaluate_boundary_drain_findings` dispatches the same row to `_drain_boundary` and therefore into
`_redeliver` without that filter. While the row's own seat still reports the exact evidence the row
carries and its `state_signal_emitted_for` is not stamped, the guard returns
`("skipped", "state-signal source marker not stamped")` before any delivery or delivery-state
mutation, leaving state-signal recovery as the only path that may renew the row, stamp the marker,
and then deliver. The identity it compares is the row's normalized ask against
`state_signals.state_signal_ask` for the catalog's current outcome/evidence — one derivation shared
with the emitter, never a second key or a landed-row scan.

### Conventions

Actions re-check the current fold before mutation so a stale sweep snapshot cannot reverse a newer
terminal outcome.

### Invariants And Boundaries

- Ordinary pending rows can follow replacement; dispatch briefs never rebind.
- Rebinding and owner stamps change together.
- For a state signal the durable order is row persisted → marker stamped → delivery attempted, and
  the marker is stamped from inside `_post_owner_signal` (`after_persist`), not after the action
  returns. A marker write that raises therefore makes zero adapter submissions and leaves one
  pending unmarked row for the next sweep to renew.
- That row is fenced at the shared action, not by predicate order: a precomputed generic
  redelivery or boundary-drain finding for the exact unmarked source makes no delivery mutation.
  A marked row, a row naming an older evidence identity, and every non-state-signal kind keep the
  ordinary path, and an unresolvable seat or a missing evidence id fails open to that path rather
  than stalling it.
- The fence trades "deliver an unmarked row" for "hold the row until its source can be stamped",
  so a subject that permanently loses a routable document holds one pending row indefinitely.
  That is a monotonic stall, not row loss: the state-signal producer owns the retry, and the row is
  never deleted or silently completed.
- No action treats model consume or completion as acknowledgement.
- Structural ambiguity or malformed routing skips only the affected finding; no alternate owner is
  selected and valid work in the same sweep continues.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Due rebinding updates and redelivers the current structural owner. [1]
- The action-time state-signal marker guard: the shared delivery action refuses a pending row whose own seat still reports that row's evidence unmarked. [2]
- The shared redelivery action carrying that guard first, before admission and delivery-state mutation. [3]
- State-signal action revalidates, posts through the current structural owner, and supplies the post-persistence marker callback. [4]
- Boundary drain inherits the same guard by delegating to the shared delivery action. [5]
- Ordinary action-time structural and task-document failures become a skipped result for that finding only. [6]
- Expiry preparation contains an ambiguous or malformed route before batching other valid transitions. [7]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
