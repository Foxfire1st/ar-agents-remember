# mcp/src/agents_remember/serving/_agent_notifier_actions.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_actions.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-15T13:15+02:00 |
| lastVerifiedCommitHash | `52bee42965e9437b3692325954ca1dcac92813e6`|
| lastVerifiedCommitDate | 2026-09-15T13:39:30+02:00|
| governingOverview      | `overview.md`                                          |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Due rebinding updates and redelivers the current structural owner. | `_rebind_due` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:214-257 |
| The action-time state-signal marker guard: the shared delivery action refuses a pending row whose own seat still reports that row's evidence unmarked. | `_state_signal_awaits_marker` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:98-122 |
| The shared redelivery action carrying that guard first, before admission and delivery-state mutation. | `_redeliver` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:126-181 |
| State-signal action revalidates, posts through the current structural owner, and supplies the post-persistence marker callback. | `_emit_state_signal` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:489-561 |
| Boundary drain inherits the same guard by delegating to the shared delivery action. | `_drain_boundary` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:705-714 |
| Ordinary action-time structural and task-document failures become a skipped result for that finding only. | `act_on_finding` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:736-763 |
| Expiry preparation contains an ambiguous or malformed route before batching other valid transitions. | `act_on_findings` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:766-822 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-09-15T13:15+02:00 — 260831-LOCR-L10 curator: recorded the state-signal recovery contract on this action surface. `_emit_state_signal` no longer writes its marker after the post returns; it supplies `OwnerSignalOptions.after_persist`, so the marker is durable between the row write and the delivery attempt and a failing marker write makes zero adapter submissions. The new `_state_signal_awaits_marker` guard clause at the top of the shared `_redeliver` refuses a pending state-signal row whose exact source seat still reports that row's evidence unmarked, and `_drain_boundary` inherits it by delegation — that is the concrete reachable path, because the generic redelivery finder excludes a held state-signal row while the boundary-drain finder does not. The prior invariant sentence "Persistence precedes delivery" is now stated as the state-signal-specific durable order with its failure behavior and its monotonic-stall surface. Ranges re-derived; verification metadata remains closeout-owned.

- 2026-09-08T14:22:32+02:00 — 260831-LOCR-L08 curator: reconciled state-signal action-time structural-owner derivation, no-current-occupant publication refusal, and per-subject `TaskDocumentRefError` fencing with the current source. Existing delivery, persistence ordering, and replacement semantics remain the shared boundary.

- 2026-09-06T22:11:05+00:00 — Preserved current source-verified notifier/reclamation semantics from retired test cards; historical claims are not active coverage and verification pins are unchanged.


- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: contained typed structural failures at both the
  ordinary action and pre-batch expiry boundaries so unrelated findings continue. Verification
  remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_agent_notifier_actions.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded action-time revalidation, fresh routing
  metadata, fail-closed mutation handling, and role-neutral subordinate relays. Verification
  metadata remains pinned until closeout stamps the code commit.

- 2026-08-09T21:10+02:00 — No content impact: master integration gate repair corrected the source's stale
  `_signal_dead_upstream` self-citation to the declaration's current line. Runtime behavior
  and the action surface are unchanged. Verification metadata stays pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the judgment-action demolition --
  respawn/ladder/auto-nudge/mark-missed action functions deleted, `_FINDING_ACTIONS` reduced to
  the fact-relay surface, nudge store + escalation knobs removed from the context, and the
  stale "ladder owns later climb" docstring claim corrected (reviewer F1). Verification
  metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the rebind/expiry/unresolved
  action family (`_rebind_due`, `_rebind_expired`, `_expire_pending`, `_mark_unresolved`),
  the attempt-ceiling terminal in `_redeliver` (N3), the architect-mailbox readdress on grace
  expiry (N2/N3), the removal of the `escalation-due` action mapping (ladder dormant), and the
  latest-fold transition call sites (F1). Verification metadata pinned until closeout stamps
  the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded `_emit_compound_idle` (action-time
  episode signature in ask + marker, master-scoped member read, one-hop orchestrator owner,
  no-owner skip, no coverage exemption, boundary-gated post) and the manager branch in
  `_emit_non_reaction` (manager residue → orchestrator; worker residue unchanged). Verification
  metadata pinned until closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay actions and the
  owner-signals extraction (posting primitives moved to `owner_signals.py`; retired
  `turn-report-stale` action; boundary admission on redeliver/escalate). Verification metadata
  pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the event dual-emission seam (`AGENT_NOTIFIER_EVENT_PREFIX` + `LEGACY_SUPERVISOR_EVENT_PREFIX` in `_log_event`) and the ask-prefix identity in `_find_coalescible`. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
