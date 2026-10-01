# mcp/src/agents_remember/serving/hosted_readiness.py

## Governing Overview

[overview.md](overview.md)
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

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

### Cross-Repo References

No meaningful cross-repo references.

#### 260713-PHA-L5 Exact-Session Readiness

Readiness is derived only from the identity-matching adapter snapshot: control ready and acceptance
immediate or queued. Legacy/custom sessions are unsupported; pane glyphs, copy mode, footer text,
and log flush windows cannot make a session ready.

## 260731-EFA-L2 Current Delta

**`ReadinessWait`** (`seconds=0.0`, `poll_interval=0.1`, `monotonic`, `sleep`; module default
`NO_READINESS_WAIT` = *observe exactly once and answer with what is true right now*) replaces the
four loose waiting arguments. A bound without a poll interval never re-observes and a poll interval
without a bound never stops, so the four are one decision — and the clock/sleep pair must be the
same one the bound is measured in, which separate parameters cannot guarantee.

Two named steps carry the readiness path: `_bridge_unreachable(...)` returns the result to report
when a row has no bridge to read (or `None` to go read it), and `_readiness_from_snapshot(...)`
re-reads the catalog **after** the bridge call and projects the snapshot onto the current row. The
readiness contract itself is unchanged: an identity-matching snapshot with `control=ready` and an
accepting state of `immediate` or `queued`; pane text, copy mode, footer glyphs and log timing are
still not readiness inputs.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
