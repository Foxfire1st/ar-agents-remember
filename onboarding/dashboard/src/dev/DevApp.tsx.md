# dashboard/src/dev/DevApp.tsx

## Current A8 source account

The App.tsx DEV ternary/lazy import still gates this router. Its retained pathname prefixes mount Reference, SprintGraphPage, TaskSkeletonPage, Bench, DocumentChatHarness and FakePaseoHost, otherwise the small index. The pty-bench and flows branches/imports and flows index entry are removed. Retained sprint-graph/task-skeleton route intent remains; the old renderer/design-canvas accounts below are dated source, not current mounts or new mounted-UI acceptance.

- The current DEV router retains the six listed prefixes and index, without pty-bench or flows branches. \[5] [5]

- The App source keeps the dev router behind import.meta.env.DEV, a lazy import and the /dev/ pathname gate. \[6] [6]

## Historical original source account — retained, not authority for removed behavior


## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The DEV-only harness router (lazy-loaded from `App` under `import.meta.env.DEV`, so it is
dead-code-eliminated from the production bundle). `/dev/reference` = the mc2 mount; `/dev/pty-bench` =
the PTY renderer measurement harness (260715-FEUI-L6, master OQ-B); `/dev/bench` = the component
gallery; `/dev/flows` = the lifecycle-design canvas (orchestration L0);
`/dev/document-chat-host` + `/dev/fake-paseo-host` = the MIK-R121 cross-workspace chat repair rig
(real document chat against the fake two-workspace host running the real plugin bridge);
`/dev/task-skeletons?form=sprint|master|task` = the real DetailPanel on an isolated seeded surface; `long=1` and `rich=1` disclose synthetic content modes, and `width` sets the panel container. Otherwise a small index.

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

As of cycle 5 the /dev/flows index label lists the converged model set (router first; build job and frame gone).


## 260815-DAG-L12 Sprint-Graph Dev Route

The DEV harness router gains the `/dev/sprint-graph` branch (L12-R7): it renders `SprintGraphPage` — the real sprint page (Operations DetailPanel) seeded with the deterministic sprint-graph fixture, the one-shot mounted-UI evidence surface. The index list carries a matching entry.
