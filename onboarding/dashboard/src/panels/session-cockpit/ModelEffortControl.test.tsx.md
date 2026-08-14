# dashboard/src/panels/session-cockpit/ModelEffortControl.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ModelEffortControl.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Rendered regression contract for live model/effort sourcing, corrected menus, apply routing, and
visible acceptance words.

## Code Commentary

### Logic

Proves exact-session fetching, effective trigger words, live-harness visibility, verbatim 503/409
failures, fresh-Claude nullable-effort handling, effortless-row re-gating, default pre-highlight,
model-only versus serialized pair apply, preservation of explicit effort, and queued/clamp chips.

### Conventions

Network calls are observed at the component boundary while deterministic capability snapshots and
the real cockpit store drive rendering.

### Invariants And Boundaries

The tests explicitly exclude the pre-session cache, inherited effort menus, implicit default
requests, and color-only acceptance status.

### Todos

The production sev-4 trigger-visual caveat remains documented in `ModelEffortControl.tsx.md`.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Sourcing, failure, menu, apply, and chip cases. | "ModelEffortControl" | dashboard/src/panels/session-cockpit/ModelEffortControl.test.tsx:1-391 |
| Component under test. | `ModelEffortControl` | dashboard/src/panels/session-cockpit/ModelEffortControl.tsx:635-704 |
| Capability fixtures. | `effortOption`; `modelRow`; `SET_RESULTS` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:20-32; dashboard/src/test/fixtures/capabilityEnvelopes.ts:34-52; dashboard/src/test/fixtures/capabilityEnvelopes.ts:211-247 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Current L5I Maintenance

The control tests now pin model-only trigger output when no current effort is evidenced and retain
the live-menu selection cases that distinguish actual state from launch fallback.

## Update History

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-24T13:17:17Z — Curator: recorded evidence-only model/effort trigger coverage;
  verification fields remain pre-commit.

- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R1–R3/R5/R6 rendered matrix after
  final reviewer PASS. Base verification metadata is temporary until code commit.
