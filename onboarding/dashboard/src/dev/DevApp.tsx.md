# dashboard/src/dev/DevApp.tsx

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
`/dev/reference`. cit:(["return <PtyRenderBench />", "FlowTab initialModel"], dashboard/src/dev/DevApp.tsx:16-16; dashboard/src/dev/DevApp.tsx:22-22)

### Invariants And Boundaries

DEV-only — never ships in production (the static `import.meta.env.DEV` branch in `App.tsx` drops the
chunk). Its CSS is co-located in `dev.css`, loaded only here.

## Evidence

### Repo-Internal References

- The DEV-only route gate that drops this chunk in prod. [1]
- The co-located dev-gallery styles it imports. [2]
- The L6 renderer measurement harness mounted at `/dev/pty-bench`. [3]
- The lifecycle-design canvas mounted at `/dev/flows` (`initialModel` from `?model=`). [4]

As of cycle 5 the /dev/flows index label lists the converged model set (router first; build job and frame gone).


## 260815-DAG-L12 Sprint-Graph Dev Route

The DEV harness router gains the `/dev/sprint-graph` branch (L12-R7): it renders `SprintGraphPage` — the real sprint page (Operations DetailPanel) seeded with the deterministic sprint-graph fixture, the one-shot mounted-UI evidence surface. The index list carries a matching entry.
