# docs/design/ — Design Documentation Overview

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| sourceRoute            | `docs/design/`                              |
| doc_type               | `route-local-overview`                      |
| lastUpdated            | 2026-07-18T07:43+02:00                      |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`  |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `../../overview.md`                         |

## Governing Overview

[agents-remember onboarding overview](../../overview.md)

## Purpose

`docs/design/` holds the **in-repo design documentation** for the Agents Remember dashboard — durable design
references kept beside the code so the design intent survives across sessions without running the dashboard.
It covers the engine-room visualization, top-level observable-lifecycle and harness-matrix notes, and the
`dashboard/` evidence set. FEUI-L8 makes that evidence set the bounded home for the canonical Chats scenario
catalog, closeout evidence, and upstream contract register instead of packing those concerns into the root
dashboard route overview.

## Hot Path Summary

In-repo design documentation for the dashboard. Child route `engine-room/` is the engine-room design
reference — a living spec paired with the prototype/scenario player the React engine room was built from.
The `dashboard/` folder now carries the FEUI-L8 scenario matrix and reproducible accessibility/performance
evidence, the closeout evidence pack, and the upstream-register boundary for contracts the frontend must not
fabricate. Two top-level notes also live here: `observable-lifecycle.md` and `harness-matrix.md`.

## Child Routes

- `engine-room/` — the engine-room design reference: the living visual-language spec + the prototype /
  scenario player the `dashboard/src/panels/engine-room/` renderer was built from. See
  [engine-room/ overview](engine-room/overview.md).

## Route Model

- `engine-room/` — the engine-room visual design reference (see child route above).
- `dashboard/scenario-catalog.md` — the canonical cockpit scenario/evidence catalog, including L8
  accessibility, performance, fetch, invariant, and end-to-end coverage.
- `dashboard/session-cockpit-closeout-evidence.md` — the bounded closeout evidence pack for the complete
  Sessions-to-Chats cockpit series.
- `dashboard/session-cockpit-upstream-register.md` — the explicit serving-contract gaps plus the ruled
  one-Chats cutover and duty-transfer record; UA-1 remains absent, so xterm's runner line-log is not described
  as a structured conversation UI.
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
- The L8 evidence documents record tested behavior and missing upstream contracts. They do not enlarge the
  product contract: the one product-facing Chats destination is backed by the session cockpit, Operations
  remains the default, RailChat remains contextual, and structured transcript/history authority stays future
  work until an adapter-normalized feed exists.
- `observable-lifecycle.md` is covered by file-level onboarding; `harness-matrix.md` remains present but
  not yet file-onboarded, so document only verified harness-matrix facts when it is onboarded later.

## Docs References

The active memory repository's `system/sources.md` has no configured Domain Documentation entries. This
overview was refreshed from the same-repository design documents, reviewed FEUI-L8 implementation/tests,
and the accepted worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external Domain Documentation source governs this route. | `system/sources.md` checked | — |

## Cross-Repo References

The FEUI-L8 design evidence and Chats ruling are repository-local. No cross-repository implementation was
needed to establish the route model.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Same-repository design/source review | — |

## Repo-Internal References

| Finding | Source Path |
| ------- | ----------- |
| The engine-room design reference child route (living spec + prototype) governing the dashboard engine room. | [engine-room/ overview](engine-room/overview.md) |
| The dashboard engine-room renderer the engine-room design docs govern. | [dashboard/src/panels/engine-room/overview.md](../../dashboard/src/panels/engine-room/overview.md) |
| FEUI-L8's canonical scenario, accessibility, performance, and invariant evidence. | [scenario catalog](agents-remember/docs/design/dashboard/scenario-catalog.md) |
| The explicit upstream gaps and one-Chats cutover ruling. | [session cockpit upstream register](agents-remember/docs/design/dashboard/session-cockpit-upstream-register.md) |
| The bounded series closeout evidence pack. | [session cockpit closeout evidence](agents-remember/docs/design/dashboard/session-cockpit-closeout-evidence.md) |

## Update History

- 2026-07-18T07:43+02:00 — 260715-FEUI-L8 route impact: added the `dashboard/` evidence route to the
  current model, routed scenario/accessibility/performance and closeout proof there, and preserved the
  upstream-register boundary: the canonical Chats cockpit is the product surface, while UA-1 structured
  transcript/history authority remains absent. Verification metadata stays pinned until closeout stamps the
  accepted code commit.
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
