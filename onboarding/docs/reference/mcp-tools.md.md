# docs/reference/mcp-tools.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | docs/reference/mcp-tools.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview | docs/reference/overview.md |

## Governing Overview

Governing overview: docs/reference/overview.md

## Purpose

Reference documentation records the three-state dispatch contract, readiness proof, settings timing, public hosted_session_readiness, tool census, and concurrency ruling.
The memory-tool reference also distinguishes the full contract-scoped curator checklist from
subset/official quality calls, including its stable enclosure path, zeroable curator count, and
cleanup lifetime.
Since 260713-TES-L4 it also records the N16 inbox landing contract (the row lands terminal
`landed` only on correlated adapter acceptance at a turn boundary), terminal inspectability
(`include_terminal`, N11), the attribution-only `operator_inbox_consume`, and the explicit
`operator_inbox_supersede` tool (R11).

## Code Commentary

### Logic

Reference documentation records the three-state dispatch contract, readiness proof, settings timing, public hosted_session_readiness, tool census, and concurrency ruling.

**260713-TES-L4 inbox rows.** The `operator_inbox_post` row now reads "queue a durable
external-chat inbox row; the row lands (terminal `landed`) only on correlated adapter
acceptance at a turn boundary (N16)". `operator_inbox_poll` gained `include_terminal=false`
with the N11 marker-retention wording; `operator_inbox_consume` is documented as an optional
attribution marker with nothing mechanical attached; the new `operator_inbox_supersede`
row documents explicit supersession (R11) — terminal `superseded`, no false ack, skipped by
every retry/evaluation path.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-11T16:54+02:00 — Documented the one enclosure-local, atomically replaced curator
  checklist, its scoped-only response fields, and cleanup/abandon garbage collection.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the N16 post/poll/consume/
  supersede reference rows — terminal `landed` at boundary acceptance, `include_terminal`
  inspectability (N11), attribution-only consume, explicit supersession (R11). Verification
  metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
