# mcp/src/agents_remember/serving/hosted_readiness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/serving/hosted_readiness.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b`|
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | mcp/src/agents_remember/serving/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/serving/overview.md

## Purpose

Exact-session harness-aware readiness is bounded, read-only, and requires catalog identity, pane boot readiness, copy-mode clearance, and an identity recheck.

## Code Commentary

### Logic

Exact-session harness-aware readiness is bounded, read-only, and requires catalog identity, pane boot readiness, copy-mode clearance, and an identity recheck.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.

### 260713-PHA-L5 Exact-Session Readiness

Readiness is derived only from the identity-matching adapter snapshot: control ready and acceptance
immediate or queued. Legacy/custom sessions are unsupported; pane glyphs, copy mode, footer text,
and log flush windows cannot make a session ready.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed exact adapter handshake and unsupported behavior.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
