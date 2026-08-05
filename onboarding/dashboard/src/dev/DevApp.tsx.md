# dashboard/src/dev/DevApp.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/DevApp.tsx`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The DEV-only harness router (lazy-loaded from `App` under `import.meta.env.DEV`, so it is
dead-code-eliminated from the production bundle). `/dev/reference` = the mc2 mount; `/dev/pty-bench` =
the PTY renderer measurement harness (260715-FEUI-L6, master OQ-B); `/dev/bench` = the component
gallery; `/dev/flows` = the lifecycle-design canvas (orchestration L0); otherwise a small index.

## Code Commentary

### Logic

Path-prefix routing over `window.location.pathname`. Imports `./dev.css` (the co-located dev-gallery
styles, slice 5d) and uses the global `.raw-list` utility (index.css). The `/dev/pty-bench` branch
renders the L6 `PtyRenderBench` measurement harness. The `/dev/flows` branch renders the panels
`FlowTab` inside a `.cockpit` wrapper, passing `initialModel` from the `?model=` query param
(`new URLSearchParams(window.location.search).get("model") ?? undefined`) — a deep link into a
specific drawn model. The index list carries a `/dev/flows` entry alongside `/dev/bench` and
`/dev/reference`. cit:(["return <PtyRenderBench />", "FlowTab initialModel"], dashboard/src/dev/DevApp.tsx:15-15; dashboard/src/dev/DevApp.tsx:20-20)

### Invariants And Boundaries

DEV-only — never ships in production (the static `import.meta.env.DEV` branch in `App.tsx` drops the
chunk). Its CSS is co-located in `dev.css`, loaded only here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The DEV-only route gate that drops this chunk in prod. | "const DevApp = import.meta.env.DEV" | dashboard/src/App.tsx:8-8 |
| The co-located dev-gallery styles it imports. | "./dev.css" | dashboard/src/dev/DevApp.tsx:6-6 |
| The L6 renderer measurement harness mounted at `/dev/pty-bench`. | "return <PtyRenderBench />" | dashboard/src/dev/DevApp.tsx:15-15 |
| The lifecycle-design canvas mounted at `/dev/flows` (`initialModel` from `?model=`). | `initialModel` | dashboard/src/panels/FlowTab.tsx:111-111 |

As of cycle 5 the /dev/flows index label lists the converged model set (router first; build job and frame gone).

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 7 initial citation findings (3 anchor, 1 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6: added the `/dev/pty-bench` route mounting the
  `PtyRenderBench` renderer-measurement harness (master OQ-B; driven by the un-carded
  `dashboard/e2e/ptyRenderBench.mjs` node script). Verification metadata pinned to the leaf base
  until closeout stamps the L6 code commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): dev index label aligned with the converged canvas. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T09:40+02:00 — 260703-L0 (Canvas & playground): added the `/dev/flows` route — it renders
  the panels `FlowTab` lifecycle-design canvas in a `.cockpit` wrapper with `initialModel` seeded from the
  `?model=` query param, and a matching index-list entry. Kept out of the cockpit mode bar (task 29); the
  harness stays DEV-only / dead-code-eliminated in production. Verification metadata pinned until closeout
  stamps the L0 commit.
- 2026-06-15T17:00 — Created for slice 5d: now imports the co-located `dev.css` (the dev-gallery
  styles moved out of the retired monolith). Verification metadata pinned until closeout stamps the
  5d code commit.
