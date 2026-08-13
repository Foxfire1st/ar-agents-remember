# mcp/src/agents_remember/controlplane/operator_inbox_transitions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/operator_inbox_transitions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T09:50+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Owns pure next-snapshot policy for durable inbox rows, including accepted-at-boundary landing,
redelivery scheduling, explicit terminal states, and structural owner rebinding.

## Code Commentary

L23 extracts `expiry_transition` as a pure transition factory shared by single-row expiry and batch notifier writes; the transition still changes only pending rows.

### Logic

`record_delivery` records adapter evidence and writes `landed` only when correlated acceptance
occurs at a target turn boundary. Otherwise the pending row receives restart-durable backoff.
`rebind_entry` atomically rewrites both address and routed owner to the current qualified
task-document-and-role seat.

### Conventions

The adjacent store owns locks and appends; transition functions compute policy from a folded row.

### Invariants And Boundaries

- Delivered outside a turn boundary is evidence, not terminality.
- Rebinding changes current occupant correlation while preserving message identity.
- A stale delivery cannot reverse an existing terminal transition.
- No transition depends on model-authored consume.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Delivery records terminal landing only on accepted boundary delivery. | `record_delivery` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:163-213 |
| Explicit landing remains idempotent and terminal. | `mark_landed` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:244-267 |
| Sweep-time rebinding rewrites address and owner together. | `rebind_entry` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:359-398 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current control-plane card for `operator_inbox_transitions.py` with plane-owned seat identity, routing, and enforcement boundaries.
- 2026-08-10T10:30+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the ladder-transition demolition --
  `RungAdvance`/`mark_escalated`/`advance_rung`/`mark_ladder_resolved` deleted; only the
  landing/terminal/rebind/renew transitions remain; legacy fields/states are parse-compat with
  `ladder-resolved` still written by the confirmed-gone reclamation fold (reviewer F4).
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the formal terminal vocabulary
  transitions — `DeliveryAttempt.landed` (boundary gate), `record_delivery`'s landed branch,
  `mark_landed`/`mark_superseded`/`mark_unresolved`/`mark_expired` as lock-held latest-fold
  transitions, `ExpiryOptions` (reason + optional architect-mailbox readdress), `rebind_entry`
  (N14: clears adapter correlation, resets attempt clock), and `_delivery_evidence_update`.
  Noted the dormant-ladder posture (N3): the ladder transitions remain but the sweep no longer
  drives them; L5 deletes the module. Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded `record_delivery`'s landed
  state-signal handling — `nextAttemptAt=None` when `state_signal_landed` holds after the
  attempt (terminal on the relay path, no backoff reschedule). Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: completed truncated docstring summaries for adapter receipts, deliveries, renewals, and ladder-rung transitions against the frozen source; normalized decorator-inclusive citation ranges via scoped --fix.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
