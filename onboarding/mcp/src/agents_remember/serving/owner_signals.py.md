# mcp/src/agents_remember/serving/owner_signals.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/serving/owner_signals.py`       |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-08-09T01:21+02:00                                    |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The extracted one-row-per-root-cause owner-signal posting primitive
(260713-TES-L2): `_post_owner_signal` and its coalescing lookup moved here from
`_agent_notifier_actions.py` so every agent-notifier owner-addressed emission (nudge,
seat-liveness, escalation, respawn, dead-upstream, state-signal, non-reaction) shares the
same durable-row creation/renewal + hosted-delivery attempt path.

## Code Commentary

### Logic

`OwnerSignal` cit:(["class OwnerSignal:"], mcp/src/agents_remember/serving/owner_signals.py:36-52) bundles message kind, ask, response, and the subject pair
(leaf, seat role) plus optional subject agent id — the message and its subject are
inseparable because coalescing matches on (ask, kind, leaf, role) and renewal rewrites the
subject from the same value. `OwnerSignalOptions` cit:(["class OwnerSignalOptions:"], mcp/src/agents_remember/serving/owner_signals.py:53-62) bundles the sweep timestamp, the
in-sweep inbox fold, and the `DeliveryAdmission` policy one signal attempt rides.

`_find_coalescible` cit:(["def _find_coalescible("], mcp/src/agents_remember/serving/owner_signals.py:64-91) is the ruled coalescing lookup (developer ruling 2026-07-09):
only a pending row created by `supervisor` or `agent-notifier` with the same message kind,
same normalized ask identity (`_seat_liveness_ask_identity`), same leaf and same seat role is
renewed. Legacy-prefix rows coalesce with current-prefix re-fires during the rename window.

`_post_owner_signal` cit:(["def _post_owner_signal("], mcp/src/agents_remember/serving/owner_signals.py:93-158) resolves the subject, finds or creates one durable inbox row,
stamps routing/owner at post time, remembers the row on the sweep fold, and attempts hosted
delivery through `deliver_inbox_entry` with the options' admission policy. A re-fire renews
the existing pending row (bumped response, refreshed subject, readdressed to the current
owner) instead of minting a duplicate — the storm that took the host down was a new pending
row per re-fire.

### Conventions

The module owns posting only; predicates and finding kinds stay in their own modules. The
message/ask identity seam is imported from `_agent_notifier_evaluation` so both modules agree
on one prefix normalization.

### Invariants And Boundaries

- One row per root cause: coalescing is content- and subject-matched, never address-matched,
  so a ladder-readdressed row still renews under its root condition.
- The marker write (e.g. `state_signal_emitted_for`) happens AFTER the post by the caller;
  a crash between the two leaves a pending row the next sweep renews/coalesces, never a
  duplicate.
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
| The delivery attempt it drives and the admission policy it carries. | "def deliver_inbox_entry("; "class DeliveryAdmission:" | mcp/src/agents_remember/serving/inbox_delivery.py:165-217; mcp/src/agents_remember/serving/inbox_delivery.py:87-105 |
| The sweep facade re-exporting the primitive for existing callers. | "def _post_owner_signal("; "def _find_coalescible(" | mcp/src/agents_remember/serving/owner_signals.py:93-158; mcp/src/agents_remember/serving/owner_signals.py:64-91 |
| The ask-identity normalization shared with the evaluation module. | "def _seat_liveness_ask_identity(" | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:235-235 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this posting primitive. | — | — |

## 260713-TES-L5 Current Delta — Rebinding Vocabulary

`_find_coalescible`'s ruled-invariant prose now says "a row the rebind machinery has
re-addressed still coalesces with its re-firing root condition" (the ladder readdressing is
gone), and `_post_owner_signal`'s storm note is historical ("each of which then escalated
into more rows" describes the pre-demolition past, not a live path). The posting primitive
itself is unchanged. This entry supersedes any earlier description in this sidecar that
conflicts with the current source behavior above; verification metadata stays pinned to the
pre-commit source history until closeout.

## Update History
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
