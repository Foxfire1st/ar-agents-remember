# dashboard/src/dev/DevApp.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/DevApp.tsx`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-05T18:20+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The DEV-only harness router (lazy-loaded from `App` under `import.meta.env.DEV`, so it is
dead-code-eliminated from the production bundle). `/dev/reference` = the mc2 mount; `/dev/bench` =
the component gallery; `/dev/flows` = the lifecycle-design canvas (orchestration L0); otherwise a small
index.

## Code Commentary

### Logic

Path-prefix routing over `window.location.pathname`. Imports `./dev.css` (the co-located dev-gallery
styles, slice 5d) and uses the global `.raw-list` utility (index.css). The `/dev/flows` branch (L15-L20)
renders the panels `FlowTab` inside a `.cockpit` wrapper, passing `initialModel` from the `?model=` query
param (`new URLSearchParams(window.location.search).get("model") ?? undefined`) — a deep link into a
specific drawn model. The index list (L27-L37) carries a `/dev/flows` entry alongside `/dev/bench` and
`/dev/reference`.

### Invariants And Boundaries

DEV-only — never ships in production (the static `import.meta.env.DEV` branch in `App.tsx` drops the
chunk). Its CSS is co-located in `dev.css`, loaded only here.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The DEV-only route gate that drops this chunk in prod. | L8-L18 | [App.tsx](../App.tsx) |
| The co-located dev-gallery styles it imports. | — | [dev.css](dev.css) |
| The lifecycle-design canvas mounted at `/dev/flows` (`initialModel` from `?model=`). | L15-L20 | [panels/FlowTab.tsx](../panels/FlowTab.tsx) |

As of cycle 5 the /dev/flows index label lists the converged model set (router first; build job and frame gone).

## Update History

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): dev index label aligned with the converged canvas. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T09:40+02:00 — 260703-L0 (Canvas & playground): added the `/dev/flows` route — it renders
  the panels `FlowTab` lifecycle-design canvas in a `.cockpit` wrapper with `initialModel` seeded from the
  `?model=` query param, and a matching index-list entry. Kept out of the cockpit mode bar (task 29); the
  harness stays DEV-only / dead-code-eliminated in production. Verification metadata pinned until closeout
  stamps the L0 commit.
- 2026-06-15T17:00 — Created for slice 5d: now imports the co-located `dev.css` (the dev-gallery
  styles moved out of the retired monolith). Verification metadata pinned until closeout stamps the
  5d code commit.
