# dashboard/src/panels/session-cockpit/StatusLine.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/StatusLine.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the footer's segment order, launch/state evidence, bounded elapsed/freshness copy, and the
collapse-or-explain grammar (R3/R4/A1/A2 — 260718-CHATS-L5P): no dash chains, no reassurance zeros, no
reserved UA-5 slot.

## Code Commentary

### Logic

- The primary case freezes time and checks DOM order across harness, pair badge, state/elapsed,
  leaf/seat, pending/queue, freshness, actions, and hint. **260718-CHATS-L5P:** the order slice is now
  7 (the `status-ua5-slot` segment is gone) and the case asserts `queryByTestId("status-ua5-slot")` is
  `null` — the reserved `ctx — / cost — (UA-5 slot)` segment was DROPPED (leaked jargon + bare dashes).
- **No-focus collapse (R3/A1)** — the `session={undefined}` case now asserts a single `status-empty`
  phrase `no chat focused — open one from the rail` and that `status-pair`/`status-leaf-seat`/
  `status-pending-sets`/`status-queued-messages` are all `null` (no `harness — model — · effort — · …`
  chain); the palette hint stays present.
- **Healthy-collapse (R4/A2)** — a NEW case pins that a healthy steady seat shows no `pending sets 0/2`
  / `queued messages 0 yours` chips and that the freshness cluster is one calm `poll ✓` token (never
  `poll healthy · missed 0 · beat age 0s`).

### Invariants And Boundaries

- Order assertions are deliberate: new segments require an explicit contract change.
- The UA-5 slot MUST stay absent (`status-ua5-slot` is `null`); a real ctx/cost readout renders itself
  when that authority exists. This supersedes the prior "the reserved slot must remain `ctx — / cost —
  (UA-5 slot)`" contract.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Contractual order (UA-5 slot absent) + freshness case. | L71-L111 | [StatusLine.test.tsx](StatusLine.test.tsx) |
| No-focus collapse (R3) + healthy-collapse (R4) cases. | L111-L155 | [StatusLine.test.tsx](StatusLine.test.tsx) |
| Component under test. | L56-L230 | [StatusLine.tsx](StatusLine.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: updated the pins to the collapse-or-explain
  behavior — the order slice dropped the removed `status-ua5-slot` (now asserted `null`), the absent-seat
  case became the `no chat focused` single-phrase collapse with sibling segments `null`, and a new
  healthy-collapse case pins `poll ✓` with no reassurance-zero chips. Corrected the "reserved UA-5 slot
  must remain" contract. Verification pinned to the leaf base (`352d5cd`) until closeout stamps the
  candidate commit.
- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
