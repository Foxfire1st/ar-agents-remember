# mcp/src/agents_remember/serving/inbox_delivery.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/inbox_delivery.py`    |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated | 2026-09-06T22:06:54+00:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview.md](overview.md)

## Purpose

Delivers one persisted inbox row through the hosted adapter and records correlated acceptance. It
re-resolves ordinary structural addresses to the current occupant immediately before delivery.

## Code Commentary

The availability gate is enforced by `messageKind`: every state-signal waits for a turn boundary even if the caller did not request boundary gating. A correlated adapter acceptance at that boundary may land the row; queued acknowledgement alone cannot. Redelivery of an already-correlated request reconciles its existing identity without sending the message again. cit:([`_delivery_refusal`; `_redelivery`; `_record_receipt`], mcp/src/agents_remember/serving/inbox_delivery.py:113-168; mcp/src/agents_remember/serving/inbox_delivery.py:232-255; mcp/src/agents_remember/serving/inbox_delivery.py:265-291).

### Logic

`target_session_for_entry` exact-pins only dispatch briefs; ordinary task-document-and-role rows use
`_structural_target`, which delegates incumbent/staged-heir choice and ambiguity refusal to the
shared `current_seat_occupant` selector. Delivery
submits the whole message once with the durable entry id as request correlation. Accepted delivery at
a turn boundary records formal landing; queued/busy delivery remains pending on its durable schedule.

### Conventions

Adapter receipt and reconciliation are acknowledgement authority. Terminal paste is not used as a
fallback for protocol delivery.

### Invariants And Boundaries

- Persistence happens before this module runs.
- Ordinary messages are replacement-aware at delivery time.
- One row is one whole-message boundary.
- Model completion/consume cannot acknowledge or trigger a second wake.
- Delivery does not own a duplicate replacement-selection algorithm.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Delivery records adapter acceptance and boundary-aware landing. | `deliver_inbox_entry` | mcp/src/agents_remember/serving/inbox_delivery.py:171-229 |
| Structural delivery target selection consumes the one canonical seat selector. | `_structural_target` | mcp/src/agents_remember/serving/inbox_delivery.py:365-373 |
| Dispatch brief is the sole exact-pinned targeting exception. | `target_session_for_entry` | mcp/src/agents_remember/serving/inbox_delivery.py:396-413 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-09-06T22:06:54+00:00 — Preserved source-verified runtime semantics from retired test onboarding; no removed coverage is claimed and verification pins are unchanged.

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed delivery-time
  canonical re-resolution and exact-pinned dispatch briefs remain accurately documented.
  Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: structural delivery now consumes the shared
  incumbent/staged-heir selector; canonical vacancy-time rows rebind to the new occupant.
  Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `inbox_delivery.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the vocabulary sweep — the
  fail-closed availability-gate comment names "a boundary drain" instead of "an escalation
  rung" as the third delivery driver; no ladder path calls `deliver_inbox_entry` anymore.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the N16 landing decision point —
  boundary sampling while the target state is live and `landed=at_boundary and accepted`
  threaded through `_redelivery`/`_record_receipt`/`_record_reconciliation`/`_record`, so a
  correlated boundary acceptance writes the formal `landed` state (lock-held latest-fold, F1)
  and queued/non-boundary acceptance never lands. Corrected the sole-acknowledgement prose in
  Purpose/Invariants (consume is attribution-only). Verification metadata pinned until closeout
  stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the fail-closed row-kind
  availability gate (`DeliveryAdmission.boundary`, `_delivery_refusal` state-signal refusal)
  and the `target_session_for_entry` extraction. Verification metadata pinned until closeout
  stamps the 260713-TES-L2 commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-02T21:40:21+02:00 — 260731-EFA-L6 curator W2-B10: resolved 8 citation findings by repairing 4 findings across 2 reference rows and deleting the 2 unanchorable claims under the 2026-08-02 14:10 citation ruling; scoped recheck clean.
- 2026-08-02T01:05+02:00 — No content impact: repaired this document's `Repo-Internal References` table shape. Rows carrying a citation cell were rendering short: the header declared two columns while those rows held three, and GFM TRUNCATES the extra cell, so the citation was in the source but invisible in the rendered table (`memory_quality/style/document_shape/tables.py`, `table_row_cell_count_mismatch`). Widened the header and its delimiter row to `| Finding | Citations | Source Path |` — the shape 1,941 rows in this tree already use — and padded the two-cell rows with `n/a`, which is this tree's own no-citation value (489 uses; zero empty citation cells exist). No finding text and no citation was changed by the widening. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `InboxDeliveryLog`, `RedeliveryFloor`, `DeliveryAdmission`, `_DeliveryOutcome` and `_AdapterCorrelation`, plus `_delivery_refusal` / `_redelivery`; durable semantics unchanged.
- 2026-07-14T15:00:00+02:00 — PHA-ME-FL2: reconciled normative delivery to inbox-rooted adapter submission and
  explicit consume acknowledgement; historicized pane/log/copy-mode/raw-paste authority.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: replaced log-window/raw-paste authority with adapter receipts and R13/R14 semantics.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

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
