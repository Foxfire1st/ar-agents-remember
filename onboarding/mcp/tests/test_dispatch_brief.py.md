# mcp/tests/test_dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/tests/test_dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | mcp/tests/overview.md |

## Governing Overview

Governing overview: mcp/tests/overview.md

## Purpose

Dispatch-brief delivery is readiness-gated, exact-session, harness-log-confirmed, calibrated beyond the active Enter-suppression window, and pending without respawn on proof failure.

## Code Commentary

### Logic

Dispatch-brief delivery is readiness-gated, exact-session, harness-log-confirmed, calibrated beyond the active Enter-suppression window, and pending without respawn on proof failure.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

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

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
