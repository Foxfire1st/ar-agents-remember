# dashboard/src/data/ — Cockpit State And Authority Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/`                            |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

This route owns the browser-side state and authority boundaries consumed by the dashboard UI. It
normalizes terminal catalog rows, keeps session and per-seat cockpit state, reconciles the daemon's
catalog, drives launch/set/submit lifecycles, and exposes pure derivations for rail, task, command,
and state-grammar surfaces. Components may project these facts, but must not invent a second
catalog, delivery ledger, or lifecycle authority.

FEUI-L8 makes this overview the strategic owner for the data plane so the root and panels
overviews can remain compact. It also records the retirement of the legacy `sessionGroups` model:
role/spawn hierarchy and attention are now derived by `railModel.ts`, while product-facing grouping
and rendering live in the canonical Chats cockpit's `SessionRail.tsx`.

## Route Model

### Catalog And Session Identity

- `sessions.ts` owns `OpenSession`, the catalog-backed registry, live-action `activeId`, connection
  registries, leaf/lifecycle attachment patches, and cross-tab catalog-change notifications.
- `catalogPoll.ts` is the single catalog read/reconcile boundary. `CockpitShell` owns both its
  refcounted interval and eager/cross-tab reconciler for the shell lifetime. Remote terminate is
  removed locally and excluded from the confirming read so a stale echo cannot resurrect it.
- Cockpit inspection focus is deliberately separate from `activeId`: landed rows remain
  inspectable, but only a running row can own the action/reload route through `preferLiveSession`.
- `sessionCockpitStore.ts` owns ephemeral per-seat UI evidence, drafts, queue state, focus, poll
  health, and layout intent. The inspector's product default is closed; responsive geometry is a
  separate concern and must not rewrite deliberate operator intent.

### Reliable Submit And Authoritative Withdrawal

- `submitClient.ts` is the whole-message submission boundary. It retains exact request ids and
  drafts across route errors, distinguishes accepted/queued/rejected/unsupported truth, reconciles
  ambiguous outcomes, and politely announces focused-seat receipts.
- `submissionLifecycleClient.ts` polls authoritative submission state and owns withdrawal. Pop-back
  is not a local queue edit: the client resolves the last queued request, calls the bridge with the
  expected epoch, applies only an authoritative withdrawn result, and retains recovery/endgame
  evidence when convergence is uncertain.
- Queue, submit history, withdrawal recovery, composer draft, and rail/stage notices are projections
  of the same per-seat store. A failed or ambiguous operation must not move the active route or
  discard the operator's draft.

### Lifecycle Cleanup And Honest Residuals

- `sessionLifecycle.ts` keeps detailed terminate outcomes, focus-independent stop residuals, and
  landed-cleanup outcomes. A successful terminate may still carry an informational control-stop
  residual; it is not reclassified as failure.
- When landed cleanup returns no authoritative result, the exact `{id,label}` target snapshot is
  retained in `cleanupFailure` and remains visible/retryable outside the collapsible rail. Partial
  success keeps both closed and skipped rows/reasons.
- Exited and retired rows are catalog evidence rather than live PTYs. Landed rows remain read-only
  inspectable until authoritative cleanup removes them.

### Controls, Keymaps, And Accessibility

- `capabilityCatalog.ts`, `setClient.ts`, and the set/launch helpers separate pre-session envelope
  truth from exact-session control truth and preserve pending/clamped/refused evidence.
- [data/keymap overview](keymap/overview.md) owns effective keyboard bindings, browser-reserved
  rejection, the immutable F6 focus escape, and Emacs/Vim composer profiles.
- `announcer.ts` is the shared polite/assertive store. Urgent transitions from one hydration are
  committed as one batch so synchronous seats cannot overwrite one another before assistive
  technology observes them.

### Dev-Bench Authority Boundary

The `/dev/bench` cockpit scenarios replace transport only. Scenario switches revoke unresolved
catalog, capability, snapshot, submission-poll, withdrawal, and connection ownership by generation
before seeding the successor fixture. These reset exports are dev-only authority seams; production
code must not use them as ordinary recovery APIs.

## Invariants And Boundaries

- The terminal catalog and bridge responses are authoritative; browser state is a projection and
  cache, never a replacement history database.
- One shell-level catalog driver/reconciler serves every route and tab. View remounts must not create
  a second timer or listener.
- `focusedSessionId` may name a landed/ended row for inspection; `activeId` must name a live row for
  actions. Catalog hydration must not steal deliberate landed focus.
- Reliable submit and withdrawal preserve request identity. Never resend blindly after an ambiguous
  boundary and never implement pop-back as a local-only deletion.
- Operator text, agent-bus messages, lifecycle control, and adapter interaction answers remain
  distinct authority channels. A future structured conversation UI must consume adapter-normalized
  history/resume capabilities rather than scrape or duplicate vendor TUIs.
- Controlled PTY output is currently a runner line-log, not the requested structured conversation
  transcript. UA-1 history/index/resume capability is not implemented by FEUI-L8.

## Hot Path Summary

1. `CockpitShell` starts catalog polling/reconciliation and receives authoritative terminal rows.
2. `sessions.ts` normalizes rows; data-layer stores derive focus, lifecycle, control, and delivery
   evidence without replacing daemon truth.
3. The canonical Chats cockpit projects the same stores into rail, stage, inspector, composer, and
   status surfaces.
4. Submit, answer, set, attach, terminate, cleanup, and withdrawal operations cross their dedicated
   authority routes before local state commits.
5. Cross-tab invalidations trigger one confirming catalog read; generation guards discard results
   owned by a retired dev scenario.

## Child Route Onboarding Map

| Child route | Governing overview | Responsibility |
| --- | --- | --- |
| `dashboard/src/data/keymap/` | [keymap overview](keymap/overview.md) | Static/effective keyboard bindings, focus zones, browser safety, and composer profiles. |

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| Catalog and session registry | [catalogPoll.ts](catalogPoll.ts.md) · [sessions.ts](sessions.ts.md) |
| Cockpit state and announcements | [sessionCockpitStore.ts](sessionCockpitStore.ts.md) · [announcer.ts](announcer.ts.md) |
| Lifecycle and cleanup | [sessionLifecycle.ts](sessionLifecycle.ts.md) |
| Reliable submit and withdrawal | [submitClient.ts](submitClient.ts.md) · [submissionLifecycleClient.ts](submissionLifecycleClient.ts.md) |
| Control/capability truth | [capabilityCatalog.ts](capabilityCatalog.ts.md) · [setClient.ts](setClient.ts.md) |
| Role/spawn rail derivation | [railModel.ts](railModel.ts.md) |

## Docs References

The curator checked the memory repository's `system/sources.md`; it contains “No entries configured
yet,” so no Domain Documentation source was available for this route. The current statements were
verified from same-repository source/tests, the L8 task/worker/reviewer records, and the recovered
same-repository history pack.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for the L8 data route. | `system/sources.md` checked during curation | — |

## Cross-Repo References

The data route's imports and authority calls resolve inside agents-remember; no cross-repository
implementation source governs this slice. Adapter behavior is consumed through this repository's
own server contracts, so no external code path is cited as authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found for these browser state/authority modules. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Catalog/session ownership and cross-tab reconciliation. | [catalogPoll.ts](catalogPoll.ts) · [sessions.ts](sessions.ts) |
| Per-seat UI and evidence state. | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| Reliable submission and authoritative withdrawal. | [submitClient.ts](submitClient.ts) · [submissionLifecycleClient.ts](submissionLifecycleClient.ts) |
| Lifecycle termination, residuals, and landed cleanup. | [sessionLifecycle.ts](sessionLifecycle.ts) |
| Role/spawn hierarchy replacing legacy `sessionGroups`. | [railModel.ts](railModel.ts) |
| Effective keymap and composer profile. | [keymap overview](keymap/overview.md) |
| Product projection of this data plane. | [session-cockpit overview](../panels/session-cockpit/overview.md) |

## Placement Decision

FEUI-L8 considered new overview routes for `dev/` and the cockpit-scenario files. Their code is a
bounded test/fixture authority seam and remains governed by the root overview; creating another
overview would fragment the product architecture. The high-churn state/authority modules instead
receive this `data/` overview, while `keymap/` remains its own child and `session-cockpit/` remains
the UI composition owner. Detailed legacy grouping knowledge was preserved here and in the
session-cockpit overview before the six obsolete sidecars were removed.

## Update History

- 2026-07-18T07:22+02:00 — Created during 260715-FEUI-L8 curation to own catalog/session state,
  reliable submit and withdrawal, lifecycle cleanup, control-authority boundaries, and the
  `sessionGroups` → `railModel`/`SessionRail` duty transfer. Verification metadata remains pinned to
  the leaf base because the reviewed L8 candidate is uncommitted; closeout owns candidate stamping.
