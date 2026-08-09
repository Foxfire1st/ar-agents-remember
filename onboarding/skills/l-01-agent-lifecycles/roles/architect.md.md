# skills/l-01-agent-lifecycles/roles/architect.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/architect.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`|
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

Governing overview: skills/l-01-agent-lifecycles/roles/overview.md

## Purpose

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

## Code Commentary

### Logic

This source participates in the L4 spawn → readiness → dispatch contract; onboarding preserves one-to-one source mapping and canonical ownership.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the custody rewrite — rows whose
## 260713-TES-L5 Current Delta — Mailbox Custody, Not Ladder Rungs

The terminal-custody section now says rows whose entire owner chain is dead surface to the
architect as a mailbox (the timed escalation ladder is retired), rows land at the architect's
turn boundary (the system acks), and `operator_inbox_consume` is an optional attribution
marker. The developer remains an authority, not an address.

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the custody rewrite — rows whose
  entire owner chain is dead surface to the architect as a mailbox, not a ladder rung (the
  timed escalation ladder is retired); rows land at the architect's turn boundary and
  `operator_inbox_consume` is an optional attribution marker, never a mechanical ack.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
