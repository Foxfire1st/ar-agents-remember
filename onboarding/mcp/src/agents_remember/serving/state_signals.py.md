# mcp/src/agents_remember/serving/state_signals.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Derives terminal-outcome, compound-idle, non-reaction, and boundary-drain findings from catalog
truth using real task-document containment for manager ownership. The boundary-drain gate decides
whether a pending inbox row has a new delivery opportunity at its target's current turn boundary.

## Code Commentary

### Logic

`compound_idle_sets` groups a manager with running leaf-role occupants whose documents are direct
children of that manager's master. State-signal and non-reaction evaluation resolve the current
manager structurally through the shared incumbent/staged-heir selector. Compound-idle groups include only the current manager generation. Their candidate documents are
projected from the same running-manager snapshot consumed by the canonical selector, so each
non-ambiguous document necessarily has a primary or staged-replacement claimant; no synthetic
missing-occupant fallback is part of that path. Observer sweeps suppress a finding for an ambiguous
occupant rather than choosing a generation; a finding for an ambiguous or
malformed task-document route is suppressed the same way, without aborting unrelated seats.
`TaskDocumentRefError` is therefore a per-subject fence at state-signal finding evaluation;
action-time owner derivation remains a separate revalidation boundary. Inbox delivery/landing
remains owned by the shared durable message path.

`evaluate_boundary_drain_findings` is the boundary-delivery gate for a pending inbox row. It asks
`_boundary_follows_last_attempt(entry, boundary_at)` whether the target's current turn boundary is a
new delivery opportunity. A row carrying no attempt clock is a drain candidate only when
`messageKind == "state-signal"`: rebinding a held signal to a replacement occupant resets that clock
(`attemptCount=0`, `lastAttemptAt=None`), the generic redelivery path then suppresses the row through
`state_signal_held_on_boundary`, and this boundary gate is its only remaining delivery path. Every
other no-attempt row keeps the ordinary redelivery path and is still refused here. A parseable
attempt clock still requires `boundary_at > attempted_at`; an unparseable clock is refused.

Reviewer subjects are polymorphic: leaf and master reviewers route to their manager, while sprint
reviewers route to the architect or orchestrator stamped on that generation. The non-reaction
notifier expands only this reviewer family; it preserves its historical worker/curator subordinate
scope and does not silently treat every sprint role as a notifier subject. Unstamped historical
reviewers retain only the deterministic old leaf-manager meaning while those rows drain; master and
sprint reviewer notifications require the generation's explicit parent stamp.

`state_signal_ask(entry, evidence_id)` cit:([`state_signal_ask`], mcp/src/agents_remember/serving/state_signals.py:506-519) is the one derivation of a seat's
canonical state-signal ask — terminal outcome plus the exact `terminal_evidence_id`. Three readers
share it rather than re-spelling the text: the emitter that mints the row
(`_emit_state_signal`), the kind-scoped coalescing lookup that finds that row again
(`owner_signals._coalesces_on_source` on the same normalized ask), and the action-time marker guard
that decides whether a pending row is the unmarked half of an interrupted post
(`_agent_notifier_actions._state_signal_awaits_marker`). Deriving it once is what keeps the emit
identity and the recovery identity from drifting apart.

### Conventions

Task hierarchy determines ownership; runtime ids only correlate observed episodes.

### Invariants And Boundaries

- Spawn ancestry does not establish manager/subordinate membership.
- A subordinate lookup with no current manager fails closed; an ambiguous canonical manager seat is
  locally suppressed.
- A missing or ambiguous task-document parent raises a typed refusal that suppresses only that
  subject; later sweeps can retry after topology recovers.
- Compound-idle manager documents come from the same immutable running snapshot used for selection,
  which guarantees a claimant after ambiguity is excluded.
- Findings arise from terminal/turn evidence, not model artifact judgment.
- State-signal delivery still obeys the target turn boundary.
- Boundary-drain eligibility for a pending row with no attempt clock is state-signal-scoped; every
  other row kind keeps the ordinary redelivery path, and an unparseable attempt clock never drains.
- A pending row whose target has no classified turn boundary is not drained by this gate; the row
  stays durable and pending, so that is a delay and not row loss.
- Ambiguity is local to the affected canonical seat; observers neither guess nor fail the whole
  sweep.
- Reviewer notification follows the generation's structural parent, while non-reviewer expansion
  remains bounded to the notifier's historical subordinate classes.
- The ask that identifies a state signal is derived once (`state_signal_ask`) and is the same
  identity for emitting it, coalescing it, and fencing its delivery; no reader parses the ask or
  mints a second key. It carries the terminal outcome and the evidence id, so a later turn is a
  different identity and re-arms the seat.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Compound-idle membership follows direct task containment and one current manager generation. [1]
- Terminal outcome findings resolve manager ownership structurally and suppress only ambiguous or malformed subjects. [2]
- A held state-signal row is suppressed from the generic redelivery path while its resolved target is running. [3]
- Non-reaction evaluation uses topology, current-generation identity, and durable landed rows. [4]
- Non-reaction subject expansion adds all reviewer altitudes without widening unrelated role scope. [5]
- Boundary drain admits a pending row whose target turn boundary follows its last recorded attempt. [6]
- Boundary-drain eligibility for a no-attempt row is state-signal-scoped; the sweep reuses the same durable pending row. [7]
- One canonical ask identity (terminal outcome + evidence id) shared by the emitter, the coalescing lookup and the action-time marker guard. [8]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
