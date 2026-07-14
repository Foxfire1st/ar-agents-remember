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

Hosted readiness is a bounded, read-only check of the exact catalog session's protocol adapter. It
requires an identity-matching snapshot with `control=ready` and an accepting state of `immediate` or
`queued`. Pane text, copy mode, placeholders, footer glyphs, and log timing are not readiness inputs.

## Code Commentary

### Logic

The readiness path reads the exact session adapter snapshot, validates its identity against the
catalog row, and returns protocol-derived readiness/capability evidence. Legacy raw-TUI and
settings-defined custom sessions are explicitly unsupported until restarted through a bridge. Pane,
terminal-log, and copy-mode observations may be retained as diagnostics only; they cannot authorize
readiness or delivery.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Dispatch proof remains exact-session and fail-closed. This sidecar's current contract is
protocol-backed; earlier pane/copy-mode/log readiness descriptions are historical and superseded by
the L5 adapter handshake.

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
- 2026-07-14T15:00:00+02:00 — PHA-ME-FL2: reconciled normative readiness to the exact adapter handshake and
  historicized pane, copy-mode, footer, and log timing observations as diagnostics-only.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed exact adapter handshake and unsupported behavior.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
