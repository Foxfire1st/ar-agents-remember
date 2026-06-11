# 02 — Event Model And The Reducer Middle Layer

| Field | Value |
| --- | --- |
| Topic | Point events vs long-running spans; a reducer that owns interpretation; what to salvage from `ar/observer-runtime-and-tui` |
| Status | Concepts accepted as inspiration; code explicitly NOT a base; rename pending |
| Sources | Branch `ar/observer-runtime-and-tui` (tip `8d2fbe3`, +5,677 lines, ~136 commits behind main at recon), its `docs/observer-*.md`, developer notes 2026-06-10 |

## Developer Direction

The TUI is at best a little inspiration — it predates the MCP, the lifecycle, and
most current primitives, and we are building a web dashboard, not a TUI. The one
interesting idea is the **"runtime" engine** (name must change): it produced a
middle layer that framed events and lifecycle types, distinguishing **long-running
processes** from **point events in time**.

## The Concepts Worth Keeping (and nothing else)

1. **Two temporal shapes.**
   - *Point events*: immutable facts at an instant (approval granted, drift report
     written, closeout applied, alarm raised). Append-only.
   - *Spans / long-running processes*: things with started/heartbeat/progress/
     finished (provider setup phases, indexing scans, a build phase, the lifecycle
     itself). The 2.7.0 `setup-progress.json` (currentPhase + completedPhases +
     15s heartbeat + stale-after-90s) is the house's existing span idiom — the
     event model should generalize it, not invent a competitor.
2. **A single reducer owns interpretation.** The branch's best doctrine line:
   frontends must consume the resolved state, *"so every frontend does not
   reimplement lifecycle assembly."* One component tails the event log + file
   snapshots and projects: current state tree, metrics, and staleness. The web
   dashboard, a future TUI, and even an agent are all just clients.
3. **Trust provenance on every event**: `declared | observed | inferred | approved`,
   with the rendering rule "do not pretend declared events are observed." This is
   unusually mature and matches the repo's evidence culture (provider results are
   "candidate routing evidence, not proof").
4. **Precomputed action availability.** The reducer — not the UI — decides whether
   an action (approve, cleanup, retry) is currently safe, and emits
   `disabledReason` / `nextSafeAction`. The cockpit never infers safety client-side.
   This becomes load-bearing the moment the control plane (note 04) exists.
5. **Atomic projection writes** (`latest-state.json` + `latest-metrics.json`
   written atomically) and **append-only corrections** (`correction.recorded`,
   `problem.reopened`) instead of mutating history.

## What Is Explicitly Dead

- The Textual TUI, its tabs, its client-lease mechanism — inspiration only.
- The event family taxonomy (`runtime.session.*`, `skill.*`, `read.session.*`, …) —
  designed against a skills-and-python world with no MCP and no l-01; the new
  taxonomy must be derived from today's primitives (lifecycle phases, gates,
  worktree contract transitions, provider span events, memory/ledger events).
- The branch as a code base: ~136 commits behind, pre-MCP architecture. Rebasing
  is worth less than re-implementing the concepts inside the `mcp` package with
  current models/registry/token discipline. (Reverses the recon report's "rebase
  and land it" suggestion — developer call 2026-06-10.)

## Naming (open)

"Runtime engine" collides with `runtime_install` / provider runtime. Candidates:

- **observer core / observer reducer** (`agents_remember.observer`) — keeps the
  established "observer" word from the branch and issue language.
- **projection engine / state projector** — says exactly what it does (events →
  projected state) and matches #43's "streams are projections."
- **telemetry reducer** — honest but smells like metrics-only; it also owns
  lifecycle truth, so probably too narrow.

Lean: module `observer`, the thing it builds called a *projection*. Decide in the
design task.

## Open Questions

- Event store location: #43 says `sessions/<id>/events.jsonl`; per-lifecycle files
  vs one workspace log with lifecycle-id columns — per-lifecycle matches retention
  and #43, one log simplifies tailing. (Possibly: per-lifecycle truth + a derived
  workspace feed.)
- Who emits? Tools emit their own events at the `_tool_payload` choke point
  (cheap, complete for tool-visible actions) vs explicit emit calls in skills
  (covers chat-side facts but depends on model discipline). Likely both, with
  trust = `observed` for tool-emitted and `declared` for skill-emitted.
  The fleeting→persistent *promotion* event (save gate, note 01) belongs in
  the minimum v1 event set.
- Schema versioning from day one (`ar-observer-event/v2`?) and how corrections
  reference corrected event ids.
- Retention: the branch had maxDays 1 / 250MB — a dashboard with history charts
  wants more; decide what is truth-forever (ledger-like) vs rolling.
