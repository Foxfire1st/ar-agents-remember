# mcp/src/agents_remember/serving/dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/serving/dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-30T21:25+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | mcp/src/agents_remember/serving/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/serving/overview.md

## Purpose

Governs the first durable message to a newly dispatched child. It is the sole internally exact-pinned
inbox delivery because the brief belongs to that newly created occupant.

## Code Commentary

### Logic

The gate requires the exact target to be running and ready, starts the brief expectation, and verifies
delivery against the same session correlation. Prompt keywords are applied only to this initial brief.
Ordinary relationship traffic does not use this exact-pin rule.

The default readiness check now waits through one bounded ten-second spawn-to-bridge startup window.
Expiry does not trigger a second dispatch or readiness call: the exact-pinned durable brief remains
pending for the ordinary notifier path, preserving one-call spawn semantics.

### Conventions

Exact session identity is private transaction evidence. The agent-facing dispatch request supplies
only task document, role, brief, and optional label.

### Invariants And Boundaries

- Initial brief delivery never rebinds to a replacement.
- Persistence precedes delivery.
- Failure leaves no silently live unbriefed child; the structural application performs rollback.
- Briefed truth comes from correlated delivery evidence, not model completion.
- Startup convergence is bounded once inside the gate; timeout never becomes an external retry loop
  or a second child/brief operation.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dispatch target admission requires the exact hosted target. | `require_dispatch_target` | mcp/src/agents_remember/serving/dispatch_brief.py:114-139 |
| Dispatch brief is explicitly the exact-pinned exception. | `dispatch_stays_on_exact_session` | mcp/src/agents_remember/serving/dispatch_brief.py:229-232 |
| Brief expectation fulfillment reads durable delivery evidence. | `fulfill_briefed_expectation` | mcp/src/agents_remember/serving/dispatch_brief.py:235-247 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 added one bounded spawn-to-bridge readiness window while preserving durable exact-pinned brief delivery and no caller retry. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `dispatch_brief.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: rewrote this card for the current source after
  `mcp/tools/dispatch_brief.py` moved into serving — the delivery seams and expectation-clock
  helpers are now owned here, exact-session readiness still refuses before persistence, and the
  test suite pins the same contract. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: replaced pane/log readiness with exact adapter handshake evidence.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
