# mcp/tests/test_dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/tests/test_dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-30T22:33:39+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | mcp/tests/overview.md |

## Governing Overview

Governing overview: mcp/tests/overview.md

## Purpose

Regression suite for the control-plane-owned initial dispatch-brief transaction.

## Code Commentary

### Logic

The tests prove ready dispatch persists one exact internal row, accepted delivery starts expectation clocks, queued/not-ready delivery stays durable for retry, ambiguous receipts reconcile without resubmission, gate or caller refusal leaves evidence, and lifecycle doctrine advertises the structural dispatcher.
The default gate also passes one explicit bounded spawn-startup wait into hosted readiness so bridge
convergence remains part of the original dispatch attempt rather than becoming a caller retry.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

The agent-facing result never exposes the child occupant id; an exact internal target never falls back by lifecycle; queued work does not duplicate briefs or respawn. The bounded readiness wait never authorizes a second dispatch attempt.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `test_ready_dispatch_is_inbox_rooted_lands_and_starts_expectation_clocks` | mcp/tests/test_dispatch_brief.py:150-175 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 recorded the single bounded
  spawn-to-bridge readiness window and preserved no-resubmission semantics.

- 2026-08-11T19:58+02:00 — Reconciled `test_dispatch_brief.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: replaced the placeholder body with the actual
  suite: inbox-rooted dispatch with expectation clocks, receipt/reconciliation handling, refusal
  and no-fallback pins, and canonical/packaged skill sync equality. Recorded that imports now come
  from `serving.dispatch_brief` after the tool-layer move. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
