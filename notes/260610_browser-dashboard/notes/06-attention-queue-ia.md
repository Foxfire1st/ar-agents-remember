# 06 — Attention Queue And Information Architecture

| Field | Value |
| --- | --- |
| Topic | The home-screen interaction model: attention queue + operations console IA |
| Status | **Accepted as working theory** (developer, 2026-06-10) — with a mandated future sub-task: *"Can we do this better?"* |
| Sources | mc2 mockup (`browser-dashboard` branch), issue #2 mockup image (`raw/issue2-mockup.png`), developer notes 2026-06-10 |

## The Working Theory

Home screen = **Attention Queue first**: every item that needs the human, across
all repos and parallel agent sessions, in one ranked place. Developer: "that's
gonna be a first place to check thing for me too — especially when working with
agents in parallel, potentially on different repos at the same time."

Item anatomy (consistent across the mockup lineage — the older issue-2 design
and the canonical `origin/browser-dashboard` mockups; see note 07):

- type: `approval held | rebase conflict | decision needed | question | blocked`
- lane: repo / worktree / lifecycle it belongs to
- wait time (how long it has been asking)
- severity coloring; resolve affordance **inline** (ties into note 04 — resolution
  happens in the same UX, not in the harness)

Supporting IA (the rest of the operations console, accepted alongside):

- **Live session strip** — active lifecycles with phase, repo(s), worktree, age
  (the projection over note 01's entity); fleeting lifecycles appear as
  bare-bones entries visually distinct from persistent (worktree-backed) ones.
- **Operation tree** — workspace → repo → checkout/worktree → task, pivotable by
  repo or by lifecycle (mc2's two-axis tree).
- **Detail panel** — selected task/lifecycle: phase mini-map, step checklist,
  artifacts, gate banner.
- **Engine room** — per-worktree provider stacks (note 08 visual grammar).
- **Memory mirror** — coverage/drift/ledger currency segmented bar.
- **Event river** — filtered observer feed with trust provenance.
- **Hangar** — stale/uncleaned worktree groups debt. Load-bearing: persistent
  lifecycles are never TTL-reaped (note 01), so this panel is *the* surfacing
  mechanism for rotting persistent work where the developer must step in.

The whole mockup lineage settled on a three-pane console (tree | detail |
health+attention+events) — treat as the working IA, not as final. The coupling
of the queue with the tree pivot is **deliberate design intent**: during the
Open Design loop the developer annotated the BY REPO | BY LIFECYCLE toggle with
an arrow into the Attention Queue, and mc2 (the designated endpoint, note 07)
carries the resulting combined Attention / By repo / By lifecycle panel.

## The Mandated Challenge Sub-Task ("Can we do this better?")

Park, do not answer now. Prerequisites before the question is even askable:
lifecycle entity (01), event model (02), gate tools (04) — because alternatives
can only be judged against real items with real wait-time distributions.
Candidate angles for that future sub-task:

- One global severity-ranked queue vs per-repo lanes vs cockpit "master caution +
  per-system annunciators" (aviation pattern: one lamp, then drill into panel).
- Escalation: wait-time SLAs, desktop notifications, audio chirp policy.
- Queue *hygiene*: items that auto-expire vs items that demand explicit dismissal
  (the mockup's "non-blocking debt" item type is interesting prior art).
- Multi-workspace future (more than one coordination root?).

## Honest Gaps In The Working Theory

- Attention items now have a **designed producer**: the `lifecycle_block` signal
  + gate records (notes 01/04) — models already wait at gates today, so the
  signal has natural motivation. Still unbuilt; the queue remains a projection,
  not a data source.
- Wait-time truthfulness depends on event timestamps, not render time.
- Parallel-harness reality: two agents can block on gates in two repos at the
  same moment; ordering/dedup policy is undesigned.
