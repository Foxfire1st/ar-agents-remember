# mcp/tests/test_dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/tests/test_dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-09T01:21+02:00 |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`|
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview | mcp/tests/overview.md |

## Governing Overview

Governing overview: mcp/tests/overview.md

## Purpose

Pins the serving dispatch-brief contract end to end: exact-session readiness gating, adapter
submission and receipt handling, durable inbox rooting, expectation-clock startup, and the
byte-identical canonical/packaged skill copies the dispatch instructions encode.

## Code Commentary

### Logic

`test_ready_dispatch_is_inbox_rooted_and_starts_expectation_clocks` posts a `dispatch-brief`
through `operator_inbox_post_payload` with a `HostedDelivery` seam set and asserts the durable
row is `delivered`/`accepted`/`pending`, the submitted control prompt carries the prompt keywords
and entry id, and the expectation rows become exactly `{ack-by, briefed-by}` with
`briefed-by` met (260713-TES-L2: `turn-report-by` is no longer written at dispatch). Receipt tests
pin that a rejected adapter receipt keeps the same row pending and
that an ambiguous redelivery reconciles without resubmitting. Refusal tests pin that a not-ready
session raises before any durable row exists, that an uncommitted caller (`submit=False`) is
recorded as adapter-rejected without touching the wire, that a closed dispatch gate keeps its own
reason with the row pending for retry, and that a missing exact session yields
`no-hosted-session` rather than falling back to a matching lifecycle. The sync test asserts the
canonical `skills/l-01-agent-lifecycles` files carry the protocol phrases and equal their packaged
copies byte-for-byte.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Dispatch proof remains exact-session and fail-closed: the exact agent target is never
replaced by a lifecycle match, refusals never contact the adapter, and a pending row survives
redelivery ambiguity without a second submission.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260731-EFA-L2 Delta — refusals before the adapter

- An **uncommitted caller** is recorded as rejected **without touching the adapter**: the refusal
  is durable, and no vendor process is contacted for a dispatch that was never authorised.
- A **closed dispatch gate** refuses the brief and **keeps the gate reason**, so the operator sees
  why rather than a generic denial.

## 260731-EFA-L6 Delta — imports follow the serving move

`HostedDelivery` (and `DispatchBriefGate`) are now imported from
`agents_remember.serving.dispatch_brief` instead of the deleted
`agents_remember.mcp.tools.dispatch_brief`; the suite itself is unchanged and still pins the same
readiness-gated, inbox-rooted contract against the serving policy module.

## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the dispatch expectation-set change
  (`{ack-by, briefed-by}`; no turn-report-by row minted). Verification metadata pinned until
  closeout stamps the 260713-TES-L2 commit.
- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: replaced the placeholder body with the actual
  suite: inbox-rooted dispatch with expectation clocks, receipt/reconciliation handling, refusal
  and no-fallback pins, and canonical/packaged skill sync equality. Recorded that imports now come
  from `serving.dispatch_brief` after the tool-layer move. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
