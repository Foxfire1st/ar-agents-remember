# mcp/src/agents_remember/serving/owner_signals.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/serving/owner_signals.py`       |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-09-15T13:15+02:00                                    |
| lastVerifiedCommitHash | `52bee42965e9437b3692325954ca1dcac92813e6`                                    |
| lastVerifiedCommitDate | 2026-09-15T13:39:30+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The extracted one-row-per-root-cause owner-signal posting primitive
(260713-TES-L2): `_post_owner_signal` and its coalescing lookup moved here from
`_agent_notifier_actions.py` so every agent-notifier owner-addressed emission (nudge,
seat-liveness, escalation, respawn, dead-upstream, state-signal, non-reaction) shares the
same durable-row creation/renewal + hosted-delivery attempt path. Since 260831-LOCR-L10 it also
owns the kind-scoped source identity a coalescing lookup matches on, and the optional
post-persistence step that must be durable before anything reaches the wire.

## Code Commentary

### Logic

`OwnerSignal` cit:(["class OwnerSignal:"], mcp/src/agents_remember/serving/owner_signals.py:39-54) bundles message kind, ask, response, and the subject pair
(leaf, seat role) plus optional subject agent id — the message and its subject are
inseparable because coalescing matches on (ask, kind, subject) and renewal rewrites the
subject from the same value. What "subject" means is kind-scoped: a state signal is identified
by the exact seat it reports on, every other kind by the task document and role it names.
`OwnerSignalOptions` cit:(["class OwnerSignalOptions:"], mcp/src/agents_remember/serving/owner_signals.py:58-73) bundles the sweep timestamp, the
in-sweep inbox fold, the `DeliveryAdmission` policy one signal attempt rides, and the optional
`after_persist` step that must be durable before the first delivery attempt.

`_find_coalescible` cit:([`_find_coalescible`], mcp/src/agents_remember/serving/owner_signals.py:92-114) is the ruled coalescing lookup (developer ruling 2026-07-09):
only a pending row created by `supervisor` or `agent-notifier` with the same message kind and
the same normalized ask identity (`_seat_liveness_ask_identity`) is renewed, and which subject
fields that row must share is decided by `_coalesces_on_source` cit:(["def _coalesces_on_source("], mcp/src/agents_remember/serving/owner_signals.py:76-89) — a
`state-signal` row is identified by the exact `subjectAgentId` it reports on, while every other
kind keeps the structural task-document + seat-role key and never reads occupant identity.
Legacy-prefix rows coalesce with current-prefix re-fires during the rename window. The lookup
takes the posted `OwnerSignal` itself rather than its five fields, so the subject seat id
reaches it by construction; `_post_owner_signal` is its only caller.

`_post_owner_signal` cit:([`_post_owner_signal`], mcp/src/agents_remember/serving/owner_signals.py:117-209) resolves the subject, finds or creates one durable inbox row,
stamps routing/owner at post time, remembers the row on the sweep fold, runs
`options.after_persist` when one was supplied, and only then attempts hosted delivery through
`deliver_inbox_entry` with the options' admission policy. A re-fire renews the existing pending
row (bumped response, refreshed subject, readdressed to the current owner) instead of minting a
duplicate — the storm that took the host down was a new pending row per re-fire.

### Conventions

The module owns posting only; predicates and finding kinds stay in their own modules. The
message/ask identity seam is imported from `_agent_notifier_evaluation` so both modules agree
on one prefix normalization, and the kind-scoped source identity lives in one function
(`_coalesces_on_source`) so the loop that walks pending rows never re-implements the split.

### Invariants And Boundaries

- One row per root cause: coalescing is content- and subject-matched, never address-matched,
  so a rebind-readdressed row still renews under its root condition.
- The row is durable before anything else happens to it. A marker or delivery failure leaves the
  already-appended/renewed pending row as the recovery authority and the next sweep renews or
  coalesces it, never appending a competitor.
- A caller whose marker must be stamped *between* persistence and delivery (a state signal's
  `state_signal_emitted_for`) passes `OwnerSignalOptions.after_persist`; the callback runs after
  append-or-renew and `sweep.remember`, and strictly before `deliver_inbox_entry`, so a failing
  callback leaves one pending row unmarked and makes zero adapter submissions. A caller whose
  marker stays a post-return write passes no callback and keeps its previous ordering.
- State signals therefore hold the durable order row persisted → marker stamped → delivery
  attempted; every other kind keeps persist-then-deliver.
- The state-signal key deliberately excludes the mutable R08 routing projection
  (`subjectTaskDocumentRef`, `seatRole`, owner address): a same-seat rebind renews and
  readdresses the same row, while two replacement seats reporting the same evidence id keep
  distinct rows and never renew each other.
- Delivery is a push attempt layered on the durable row; acceptance does not consume and does
  not ack the row.
- State-signal posts pass `DeliveryAdmission(boundary=True)`; the seam-level row-kind gate in
  `inbox_delivery._delivery_refusal` is the enforcement, caller admission is defense-in-depth.

### Todos

None for this module.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
posting semantics are same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this posting primitive; the ruled coalescing contract is the source of truth. | `_post_owner_signal` | mcp/src/agents_remember/serving/owner_signals.py:93-158 |

## Repo-Internal References

The primitive composes the control-plane inbox record/transition helpers and the delivery
helper; the action layer and the sweep import it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The inbox row record/creation and renewal/readdress transitions it composes. | "def create_operator_inbox_entry("; "def renew(" | mcp/src/agents_remember/controlplane/operator_inbox_records.py:244-244; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:434-434 |
| The delivery attempt it drives and the admission policy it carries. | "def deliver_inbox_entry("; "class DeliveryAdmission:" | mcp/src/agents_remember/serving/inbox_delivery.py:171-217; mcp/src/agents_remember/serving/inbox_delivery.py:94-105 |
| The row is durable and on the sweep fold before the optional marker step (lines 185-192), which precedes the delivery attempt. | `_post_owner_signal` | mcp/src/agents_remember/serving/owner_signals.py:117-209 |
| The kind-scoped source identity the lookup delegates to. | `_coalesces_on_source`; `_find_coalescible` | mcp/src/agents_remember/serving/owner_signals.py:76-89; mcp/src/agents_remember/serving/owner_signals.py:92-114 |
| The sweep facade re-exporting the primitive for existing callers. Note the lookup's signature is now the single `signal=` carrier, not the five keyword values it used to take. | `_post_owner_signal`; `_find_coalescible` | mcp/src/agents_remember/serving/owner_signals.py:117-209; mcp/src/agents_remember/serving/owner_signals.py:92-114 |
| The ask-identity normalization shared with the evaluation module. | "def _seat_liveness_ask_identity(" | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:240-240 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this posting primitive. | — | — |

## 260831-LOCR-L10 Current Delta — Kind-Scoped Source Identity And The Post-Persistence Step

Two parts of the posting primitive changed, both scoped to the state-signal kind. Coalescing now
asks `_coalesces_on_source` which fields a pending row must share: a `state-signal` row matches on
the exact `subjectAgentId` alone, because R08 may rewrite the same seat's task document, role, and
owner address before a retry while two different replacement seats must never renew one another's
rows; every other kind keeps the structural task-document + seat-role key and still ignores
occupant identity. `_find_coalescible` consequently takes the posted `OwnerSignal` as one carrier
instead of five keyword values — behaviorally identical input, forced by the repository's
argument budget (`ruff PLR0913`, no `# noqa`). Second, `OwnerSignalOptions.after_persist` is the
optional step that becomes durable between the row write and the first delivery attempt;
`_emit_state_signal` is its only supplier today. A marker write that raises therefore leaves one
pending unmarked row and zero adapter submissions, and the next sweep renews that row before
retrying the marker.

## 260713-TES-L5 Current Delta — Rebinding Vocabulary

`_find_coalescible`'s ruled-invariant prose now says "a row the rebind machinery has
re-addressed still coalesces with its re-firing root condition" (the ladder readdressing is
gone), and `_post_owner_signal`'s storm note is historical ("each of which then escalated
into more rows" describes the pre-demolition past, not a live path). The posting primitive
itself was unchanged by that leaf. This entry supersedes any earlier description in this sidecar
that conflicts with the current source behavior above; verification metadata stays pinned to the
pre-commit source history until closeout.

## Update History
- 2026-09-15T13:15+02:00 — 260831-LOCR-L10 curator: recorded the current posting contract. Coalescing is kind-scoped through `_coalesces_on_source`: a `state-signal` row is identified by exact `subjectAgentId` and no longer by the mutable task-document/role projection, while every other kind keeps the structural key and still ignores occupant identity; `_find_coalescible` now takes the posted `OwnerSignal` as the one carrier of those fields. `OwnerSignalOptions.after_persist` is the new optional post-persistence/pre-delivery step, invoked after append-or-renew and `sweep.remember` and strictly before `deliver_inbox_entry`, so a failed marker write leaves one pending unmarked row and no adapter submission. The prior bullet that placed the state-signal marker write after the post by the caller is superseded, and every construct range was re-derived against the current source. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `owner_signals.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the rebind-vocabulary sweep in
  `_find_coalescible`/`_post_owner_signal` (ladder readdressing → rebind machinery; storm
  note historical). Verification metadata pinned until closeout stamps the 260713-TES-L5
  commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the extracted
  owner-signal posting primitive (`OwnerSignal`/`OwnerSignalOptions`, `_find_coalescible`,
  `_post_owner_signal` moved from `_agent_notifier_actions.py`; admission policy now rides
  the options). Verification metadata pinned to the leaf base `1c1629fc` until closeout stamps
  the 260713-TES-L2 commit.
