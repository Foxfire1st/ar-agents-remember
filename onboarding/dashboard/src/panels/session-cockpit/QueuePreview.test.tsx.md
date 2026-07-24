# dashboard/src/panels/session-cockpit/QueuePreview.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/QueuePreview.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Session cockpit overview](overview.md)

## Purpose

Pins the queue-head steer affordance and its evidence boundaries.

## Code Commentary

### Logic

The fixture seeds active-conversation identity, capability, and turn state. Tests cover absent or
unsupported evidence, supported working-turn visibility, and the direct interrupt request while
asserting that both queue rows remain present in their original order.

### Conventions

The focused request is observed at the fetch boundary so the test checks the exact bridge epoch,
turn id, and generated request id without duplicating client implementation.

### Invariants And Boundaries

Steer is not queue mutation: it may only interrupt a proved working turn and leaves authority-owned
queued entries untouched.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured in `system/sources.md`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Projection fixtures build interrupt-capability and working-turn evidence. | L21-L143 | [QueuePreview.test.tsx](QueuePreview.test.tsx) |
| Cases prove visibility gating and the no-withdraw/no-duplicate steer request. | L144-L217 | [QueuePreview.test.tsx](QueuePreview.test.tsx) |
| Implementation under test. | L74-L141 | [QueuePreview.tsx](QueuePreview.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the queue-steer regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
