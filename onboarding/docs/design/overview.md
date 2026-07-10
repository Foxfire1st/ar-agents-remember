# docs/design/ — Design Documentation Overview

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| sourceRoute            | `docs/design/`                              |
| doc_type               | `route-local-overview`                      |
| lastUpdated            | 2026-07-08T23:59+02:00                      |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`  |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `../../overview.md`                         |

## Governing Overview

[agents-remember onboarding overview](../../overview.md)

## Purpose

`docs/design/` holds the **in-repo design documentation** for the Agents Remember dashboard — durable design
references kept beside the code so the design intent survives across sessions without running the dashboard.
It currently covers the engine-room visualization (its own subfolder) plus two top-level design notes on the
observable lifecycle and the harness matrix. These documents are the design authority the dashboard
renderers are built to satisfy.

## Hot Path Summary

In-repo design documentation for the dashboard. Child route `engine-room/` is the engine-room design
reference — a living spec (`engine-room-visual-language.html`, the canonical colour/motion/glow/timing
source of truth) paired with the prototype/scenario player (`podstage.html`) the React engine room was built
from. Two top-level notes also live here: `observable-lifecycle.md` (file-onboarded, including the
task-23/24 interaction-retention model) and `harness-matrix.md` (present but not yet file-onboarded).

## Child Routes

- `engine-room/` — the engine-room design reference: the living visual-language spec + the prototype /
  scenario player the `dashboard/src/panels/engine-room/` renderer was built from. See
  [engine-room/ overview](engine-room/overview.md).

## Route Model

- `engine-room/` — the engine-room visual design reference (see child route above).
- `observable-lifecycle.md` — top-level design note on the observable lifecycle, now including
  `lifecycle_gate` as the public gate junction plus the interaction-retention tiers: durable work
  records stay, gate/inbox interactions delete on response, dismiss, clear, consume, or the
  24-hour passive TTL. HFX2-L8 adds the operator-inbox storm recovery runbook: quarantine to `.bak`,
  park/terminate only dead terminal rows, restart cleanly, verify heartbeat/backlog metrics, and
  never delete transcripts.
- `harness-matrix.md` — top-level design note on the harness matrix. **Present but not yet file-onboarded**
  (no sidecar created in this pass).

## Invariants And Boundaries

- These are **design reference documents**, not shipped application code. The engine-room HTML docs animate
  in CSS purely for portability; the dashboard itself animates in GSAP + Motion (CSS static-only) per the
  engine-room motion doctrine.
- Design intent flows **doc → code**: the design references are the authority the dashboard renderers are
  built to satisfy; keep them and the renderers in sync.
- `observable-lifecycle.md` is covered by file-level onboarding; `harness-matrix.md` remains present but
  not yet file-onboarded, so document only verified harness-matrix facts when it is onboarded later.

## Repo-Internal References

| Finding | Source Path |
| ------- | ----------- |
| The engine-room design reference child route (living spec + prototype) governing the dashboard engine room. | [engine-room/ overview](engine-room/overview.md) |
| The dashboard engine-room renderer the engine-room design docs govern. | [dashboard/src/panels/engine-room/overview.md](../../dashboard/src/panels/engine-room/overview.md) |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 route impact: `observable-lifecycle.md` now includes the
  non-destructive operator-inbox storm recovery runbook for stale-supervisor incidents. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-06T12:10+02:00 — No route impact: reviewed during the 260703-L10 one-vocabulary sweep — the design specs here are historical design records (engine-room visual language, observable-lifecycle 3.0 design) and are not rewritten by vocabulary sweeps; their only `orient` hits are SVG marker attributes.
- 2026-06-26T14:16+02:00 — Task 25: route overview now points to `lifecycle_gate` as the observable-lifecycle design's public gate junction.
- 2026-06-25T13:20+02:00 — Task 23/24: onboarded `observable-lifecycle.md` and recorded the interaction-retention design update for gate/inbox throwaway data.
- 2026-06-21T23:35 — Created. Route overview for `docs/design/` (in-repo dashboard design documentation):
  recorded the `engine-room/` child route (living spec + prototype) and noted the two top-level design notes
  `observable-lifecycle.md` + `harness-matrix.md` as present-but-not-yet-file-onboarded. The engine-room
  source files are newly added and not yet committed; verification metadata pinned to repo HEAD until a
  commit stamps them.
