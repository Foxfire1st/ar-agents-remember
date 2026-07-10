# mcp/src/agents_remember/serving/inbox_delivery.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/inbox_delivery.py`    |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash |                                                        `fdff55f2921d7aaa8ba240c11087d02c15a170d7`|
| lastVerifiedCommitDate |                                                        2026-07-10T15:53:23+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview.md](overview.md)

## Purpose

Push-delivery helper that takes one durable operator inbox entry and injects it
into a matching hosted terminal session through the server-side echo-confirmed
paste seam.

## Code Commentary

### 260707-HFX2-L17 Injected Delivery Time

`deliver_inbox_entry` accepts optional `delivery_at` and uses it for persisted delivery metadata.
The supervisor supplies its sweep timestamp, preventing wall-clock drift from changing fixture
retention or retry behavior; ordinary callers retain the existing current-time default.

### Logic

**260707-HFX2-L15 hosted inbox delivery.** `deliver_inbox_entry` builds a `HarnessSessionLog` from
the target catalog row, passes it into the shared injector, and persists a newly bound log id/path
through `TerminalCatalog.bind_session_log`. Durable delivery detail now says
`harness-log-confirmed`; an unconfirmed result carries only failure-pane diagnostics, while a draft
is explicitly landed but unsubmitted.

`deliver_inbox_entry(...)` resolves a target running `TerminalCatalogEntry` by
exact agent id first and lifecycle id second. It verifies the tmux session still
exists through `TerminalHost.has_session`, formats an inbox block with message
kind, sender, entry id, an ack instruction, optional artifact path, ask, and
response (`_push_text`), then — 260707-HFX2-L3 (R1 + R3) — builds a `DeliveryRow`
(`envelope=False`, since `_push_text` already renders this payload's own header)
and calls `serving.injector.deliver`, the ONE delivery path every other payload
class (spawn briefs, dispatch/nudge/redelivery rows) now goes through, instead of
calling `TerminalPaster.paste` itself. The same inbox entry is updated through
`OperatorInboxStore.record_delivery(...)` with `delivered`, `unconfirmed`, or
`no-hosted-session` metadata — this schema (`InboxDeliveryState`) is UNCHANGED by
this leaf (widening it is bigger blast radius than this leaf; the dashboard, the
backoff predicate, and the L2 supervisor all key off it as-is). **260707-HFX2-L8**
adds an optional `current` snapshot parameter that is passed through to `record_delivery`, letting
one supervisor sweep reuse its in-memory operator-inbox index instead of re-folding the jsonl for
each redelivery finding. `_delivery_state`
maps the injector's four-way `DeliveryOutcome` back onto it: `acked → delivered`,
everything else (`landed-unacked`/`blocked`/`failed`) → `unconfirmed`.
HFX2-L9 adds `redelivery_floor_seconds`: every delivery outcome path, including `no-hosted-session`,
passes that optional floor through to `OperatorInboxStore.record_delivery`, so a first push attempt
is scheduled minutes out instead of letting the old 30/60-second ladder re-fire while the message may
still be queued or under model processing.
`_delivery_detail` keeps the exact `"echo-confirmed"` success string and the
exact `_unconfirmed_detail` wording for a `failed` outcome (tail-bounded pane
capture, `_CAPTURE_EVIDENCE_LIMIT` = 2000 chars; empty capture gets
"paste was not capture-verified (empty pane capture)"); a NEW `blocked` outcome
(a modal dialog trap — codex quota/rate-limit #20, a permission prompt) gets a
`"NEEDS-ATTENTION: blocked (<reason>); ..."` prefixed detail instead of the
generic unconfirmed wording, so it stays structured and diagnosable without a
schema change; a `landed-unacked` outcome (draft-only, or submitted but the turn
did not visibly start) gets its own distinct wording too.

### Conventions

Delivery is a push attempt layered on a durable inbox row. The helper never
deletes the row; polling/consuming remain available when hosted delivery is
missing or unconfirmed. All the actual paste/blocked/turn-started classification
now lives one level down, in `serving.injector.deliver` + `serving.harness_adapters`
— this module's job is purely the InboxDeliveryState translation layer.

### Invariants And Boundaries

- A catalog row alone is not enough; the tmux session must also pass
  `TerminalHost.has_session`.
- `delivered` means the delivery outcome was `acked` (paste landed, submitted,
  and the turn was confirmed started) — not merely pane output during harness
  boot.
- An unconfirmed push must carry its evidence: the durable `deliveryDetail`
  embeds the bounded pane-capture tail (260707-HFX-L3), and the success detail
  stays the exact string `"echo-confirmed"` (dashboard copy depends on it).
  `InboxDeliveryState` itself is pinned to its four existing values
  (`queued`/`no-hosted-session`/`delivered`/`unconfirmed`) — a `blocked` outcome
  is carried in `deliveryDetail`'s text, never a new enum value (260707-HFX2-L3
  scoping decision: widening the schema ripples into the dashboard type and
  `inbox_backoff.py`'s redeliverable-state set, a bigger leaf than this one).
- The formatted stdin text is simple Markdown-ish text for agents, not a hidden
  protocol.
- The optional `current` snapshot is only a caller-supplied performance seam; omitted callers keep the
  previous read-modify-append behavior.
- The optional `redelivery_floor_seconds` is scheduling policy only; this module still maps delivery
  outcomes onto the unchanged `InboxDeliveryState` vocabulary.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Delivery state is persisted on the operator inbox record. | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| Echo-confirmed paste behavior lives in the server-side paster. | [terminal_paste.py](agents-remember/mcp/src/agents_remember/serving/terminal_paste.py) |
| The dashboard serving route and MCP payload builder both pass catalog/host/paster seams for delivery. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| 260707-HFX2-L3: `deliver_inbox_entry` now builds a `DeliveryRow` and calls the ONE delivery path, `serving.injector.deliver`, instead of calling `TerminalPaster.paste` directly. | `deliver` | [injector.py](injector.py.md) |
| `serving.supervisor`'s `_redeliver`/`_post_owner_signal` are the only callers of `deliver_inbox_entry` — every nudge/redelivery/signal-emit action the supervisor takes rides through this same translation layer. | `_redeliver`; `_post_owner_signal` | [supervisor.py](supervisor.py.md) |
| `deliver_inbox_entry` threads `redelivery_floor_seconds` into every `record_delivery` path. | L42-L90 | [inbox_delivery.py](agents-remember/mcp/src/agents_remember/serving/inbox_delivery.py) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added an optional injected delivery timestamp so
  supervisor simulation and production decisions persist on the same clock.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: changed hosted inbox acceptance from pane echo/turn
  evidence to bound harness-log evidence and persisted the binding without replacing newer catalog
  liveness state. Verification metadata remains pinned until closeout stamps the eventual L15 code
  commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: added the optional `redelivery_floor_seconds` scheduling
  parameter and passed it through to `OperatorInboxStore.record_delivery` for hosted delivery,
  missing-session, and unconfirmed paths. Verification metadata pinned until closeout stamps the
  260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (bounded inbox sweep, R2): `deliver_inbox_entry`
  accepts an optional operator-inbox `current` snapshot and passes it through to
  `OperatorInboxStore.record_delivery`, so supervisor redelivery can update rows against one
  in-sweep index instead of reparsing the whole inbox file per finding. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 (paste injector hardening, R1 + R3): `deliver_inbox_entry`
  now routes through the ONE delivery path (`serving.injector.deliver`) instead of calling
  `TerminalPaster.paste` directly; `_push_text` gained an `entry:`/`ack:` header line (the R3
  payload-envelope ack instruction, folded into the existing inbox header rather than a second
  wrapper). `InboxDeliveryState`'s four values are UNCHANGED — a new `blocked` outcome is carried as
  a `NEEDS-ATTENTION:`-prefixed `deliveryDetail` string, a deliberate scoping decision (see
  Invariants) to keep this leaf's blast radius off the dashboard type and `inbox_backoff.py`. All
  existing tests in `test_operator_inbox.py`'s `OperatorInboxDeliveryTests` pass UNCHANGED.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): the unconfirmed
  `deliveryDetail` now embeds the paster's pane capture, tail-bounded to 2000 chars
  (`_unconfirmed_detail` + `_CAPTURE_EVIDENCE_LIMIT`; empty capture gets its own loud wording);
  the success detail string `"echo-confirmed"` is unchanged. Verification metadata pinned until
  closeout stamps the HFX-L3 commit.
- 2026-07-04T12:31+02:00 - L3: created the hosted inbox push-delivery helper card. Verification metadata pinned until closeout stamps the L3 commit.
