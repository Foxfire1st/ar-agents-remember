# 01 — The Lifecycle As A First-Class Entity

| Field | Value |
| --- | --- |
| Topic | The root primitive under the dashboard: an observable, identifiable lifecycle |
| Status | **SETTLED 2026-06-10** (two discussion rounds); **sharpened 2026-06-11** (baseline alignment: guarded start, switch-only target id, save gate, TTL fleeting-only, contract-enclosure identity, multi-repo openness). Remaining: per-harness propagation verification, schema details with note 02, and one spawned follow-up (worktree-only closeout policy) |
| Sources | Issue #43, `l-01-session-job-lifecycle` skill, observer-branch event contract, developer discussions 2026-06-10/11 |

## Developer Direction (verbatim intent)

The Attention Queue is a primitive for the *visual*. The underlying most important
primitive is the **lifecycle**. Tasks and worktrees are bound to it. Every action
that happens within a lifecycle should carry its id, so actions and tool calls
don't look random but are attributable to a specific lifecycle. "If we can make
that work then we have a huge piece of the puzzle down."

## Current Truth (verified during recon, MCP 2.7.0/2.8.0)

- The l-01 lifecycle is **markdown machinery**: phases exist only as skill prose,
  chat behavior, and hand-written `Status` lines in `task.md` files.
- No machine-readable lifecycle record: no id, no phase artifact, no event trail.
- Tool calls are anonymous: responses carry token metadata but no attribution;
  `logs/mcp/` exists and is empty.
- Bindings half-exist as implicit joins: the worktree contract knows its task and
  group; `task.md` knows its issue; neither knows a lifecycle.

## The Settled Model

### Signals and states (the video-player model)

The model drives **action signals** that translate into **states** — like player
buttons, only one state true at a time:

| Signal (tool) | Resulting state | Notes |
| --- | --- | --- |
| `lifecycle_start` | `running` | Takes no identifier; performs only the transition no-lifecycle → running. **Guarded** — while any lifecycle is active in the session, start is rejected with a reminder naming the active lifecycle: it can neither restart nor stack. Leaving happens only via `lifecycle_end` or `switch_lifecycle` |
| `lifecycle_pause` | `paused` | For genuine off-task digressions ("how is the weather"), not repo research |
| `lifecycle_resume` | `running` | Pause+resume simultaneously is nonsensical by intention — states are exclusive |
| `lifecycle_block` | `blocked` | Approval pendings and similar gates. Models already wait at gates today, so the motivation to signal is real — and the dashboard uses exactly this signal to draw attention to the blocker |
| `lifecycle_end` | `completed` or `abandoned` | `completed` = the human declared the task done; `abandoned` otherwise |
| `switch_lifecycle` | (transition) | The only signal that carries a target identifier. See pivoting below |

**Phases are orthogonal to states.** Phases (the l-01 enum: request, trust,
reframe/research, decide, build, close) are also one-at-a-time but semantically
different — declared via a dedicated **`lifecycle_phase`** tool. You can be in
the *research phase* and the *paused state* at once; you cannot be paused and
running at once. Two axes, two tools.

Naming rule: the family is `lifecycle_*` — never `workflow_*` (collides with
w-02 and harness workflow tooling), never "runtime" (note 02).

### Minting, and why the model never handles ids

- **A lifecycle represents work, not a repo.** One lifecycle can enclose work
  spanning multiple repos (2, 4, or 6 — untested but never conceptually
  forbidden when the repos together describe one larger product); repos are
  where the work lands, never the lifecycle's identity key. A session holds
  zero or one active lifecycle.
- **Minting moment: adjacent to `context_packet`.** At l-01 entry the agent has
  read the skill but doesn't know whether the task touches a managed repo;
  `context_packet` answers that definitively — governance confirmed ⇒ start.
  A second `context_packet` for another repo mid-lifecycle mints nothing: the
  same lifecycle encloses that work.
- **The system manages relationships; the model manages signals.** The model's
  whole job is start / end / pause / resume / block / switch / phase. It never
  juggles ids: guarded start prevents duplicates (start-while-active is
  rejected with a reminder), and the **contract** makes resume MCP-owned
  (below). Ambient propagation (below) tags everything else.

### The commitment boundary: fleeting vs persistent

The consistent boundary is *commitment to a code change* — the point that would
produce a w02 task if the work were bigger. That point is the **worktree**, the
fixture chat builds and w02 builds share:

- **Fleeting lifecycle (no worktree yet):** unbound to any durable artifact —
  recorded server-side (the dashboard shows a bare-bones entry: phase + some
  context), but the model can't track it and shouldn't. Ends early and
  cheaply: discarded on `switch_lifecycle` once the save gate (below) is
  declined (nothing to return to — no worktree, and whatever research it did
  is still in the agent's context), or TTL-reaped (~**1h**) when the clear
  signal is missing entirely.
- **Persistent lifecycle (worktree locked):** the lifecycle lingers *because the
  fixture lingers on disk* — disk fixture ↔ dashboard entity is a consistency
  rule (a worktree only visible in the filesystem is easily forgotten; this is
  the hangar panel, note 06). Visually distinct from fleeting entries to
  communicate "this survives the chat."
- **TTL is fleeting-only.** It reaps a fleeting lifecycle whose signals go
  missing; a persistent worktree-backed lifecycle is **never** auto-reaped —
  when persistent work rots, the dashboard surfaces the staleness (hangar
  panel, note 06) and the developer steps in.

### Resume across sessions: MCP-owned via the contract

Every worktree group comes with a contract (today `contract.md` YAML front
matter, `ar-worktree-contract/v1`). **The lifecycle's identity anchor is the
contract enclosure** — the wrapper `contract.md` defines, not any individual
code or memory worktree inside it. Today that enclosure wraps one code+memory
pair; conceptually it may span several repos of one larger product (untested —
keep in mind, don't design it out). A multi-task series runs in one enclosure
and is therefore one lifecycle. The contract binds the lifecycle identity the
moment a worktree exists. Continuing a task days later, in a new
chat, after compaction: attach to the worktree → the contract tells the MCP the
lifecycle id → the session switches into that lifecycle and all further work is
attributed. Resume depends on the MCP, **not** on the model inferring anything —
which is what prevents duplicate lifecycle entries on the dashboard.

End, once a worktree is involved, is defined by the repo's instructions
(`git-workflow.md`) or by the developer making it explicit — worktree cleanup,
task finished or abandoned. A 10-page multi-task with one straggler checkbox can
be *declared* finished.

### Pivoting: `switch_lifecycle`

`lifecycle_start` is for session starts (and is guarded); pivoting mid-chat
is an **intended choice** with its own lever. `switch_lifecycle` is the only
signal that carries a target identifier — a reference to an existing
worktree-backed lifecycle, which the contract resolves to the lifecycle id
(the model never handles raw ids). It either:

- creates a brand-new lifecycle (new task, nothing existing), or
- switches into the lifecycle of an **existing worktree** (= resume it).

Switching **auto-pauses** the lifecycle being left if it is persistent
(worktree-backed), and **auto-ends** it if it is fleeting. Inner-switches
between tasks on a managed repo are therefore deterministic.

**The switch boundary is a gate (save gate).** When the lifecycle being left
is a *fleeting* research task, the model first asks the developer whether to
**save** the work: saving creates a worktree, puts the notes in it, and — if
the task is understood — a task file too, which *promotes* the lifecycle to
persistent before the switch (so it auto-pauses instead of auto-ending).
Declining is a deliberate discard: the switch commits without a worktree and
the fleeting lifecycle auto-ends. Progress is either preserved or thrown away
on purpose — never by surprise.

**Where saved work lands (design note, 2026-06-11).** Tasks and worktrees are
grouped by repo — but a fleeting lifecycle is not necessarily bound to a
single tangible repo under the Agents Remember domain (e.g. a research task
across many pages, which you still don't want to lose). To give such work a
home when saving, the task root gains a **`0_misc`** folder (number prefix so
it sorts distinctly above the repo folders). By the same logic, multi-repo
work (the multi-repo enclosure above) needs its own **`1_inter-repo-work`**
folder — without it, every save would force an arbitrary choice of one repo's
folder, which would be wrong. Final names can be improved; settle them before
the save gate is built.

### Worktree-only closeouts (original design intent; cleanup incomplete)

**There is no closeout without a worktree.** This is not a new decision: when
the lifecycle skill was designed, the developer consciously made *changes
affecting the code repo = worktree (code + memory)* — both to keep memory clean
and to lay the foundation for a later dashboard. The direct-closeout path is a
**leftover** from before that decision; the cleanup simply wasn't thorough
enough. Both chat builds and w02 builds must produce worktrees; worktrees are
the goto in agentic engineering, and the memory repo is easily corrupted
without them. Skills, code, and docs are being brought in line in a **separate
alignment task** (see Q22 / the task folder) so the dashboard work can continue
on a clean foundation.

Spawned follow-up (outside dashboard scope, prerequisite alignment):
**`tasks/agents-remember/260610_worktree-only-closeout-alignment/task.md`**
(created 2026-06-10, status planning) carries the removal plan. Affected
surface for reference (canonical sources; the 8 harness starter copies +
package_data are regenerated by `scripts/sync-runtime.py`):

- Tools: `direct_closeout_preview` / `direct_closeout_apply` —
  `mcp/src/agents_remember/mcp/tools/worktree.py`, `controllers/worktree_tools.py`,
  `worktrees/modules/closeout.py` + `cli.py`, `models/worktree.py`,
  `models/tool_registry.py`, `mcp/server.py`, tests
  (`test_worktree_support.py`, `test_tools.py`, `test_tool_response_conformance.py`)
- Skills: `skills/l-01-session-job-lifecycle/SKILL.md` (close step offers
  direct_closeout_preview when git-workflow permits), `skills/c-12-closeout/SKILL.md`
  ("both direct checkout and worktree-backed tasks")
- Docs: `docs/workflows.md`, `docs/reference/mcp-tools.md`,
  `docs/reference/worktrees-c09.md`, `docs/guides/adopt-existing-memory.md`,
  `mcp/README.md`, `docs/README.md`
- Installed/coordinator copies + onboarding sidecars follow via sync + closeout.

### Lifecycle vs harness session

The lifecycle is what **the MCP + contract can own**. The harness session is
strongly correlated but not causal — a lifecycle survives chat sessions (resume
above). Session identity is provenance metadata at most.

## Propagation Refinement (proposed, to confirm)

Because the MCP server is **stdio, one server process ≈ one harness session**:
`lifecycle_start`/`switch_lifecycle` set an ambient *current lifecycle* in the
server process, and every subsequent tool call is **auto-tagged server-side** —
the audit trail is complete by construction, not by model discipline. Explicit
`lifecycle_id` param exists only as an override. Subagents sharing the parent's
MCP connection inherit the ambient id. Verify per harness that the server
process is genuinely session-scoped (true for Claude Code; check Codex/Cursor/
others).

## Remaining Questions (small)

1. **Per-harness server scoping** for ambient propagation (above).
2. **Blocked → running transition:** when a gate is approved from the dashboard
   (note 04), does the reducer auto-project the lifecycle back to `running`, or
   does the model signal resume when it notices? Lean: system-driven unblock
   (gate state change clears the block), model signal optional. Settle with 02/04.
3. **Precedence rules** — guarded `lifecycle_start` is now unambiguous, so the
   open question reduces to: contract-driven resume on worktree attach vs. an
   already-active lifecycle (when must attach behave as a switch?). Write the
   decision table when drafting the tool specs.
4. **Phase enum finalization + schema field names** — with the event schema (02).

## Prior Art In The Mockups

The `origin/browser-dashboard` review screenshots (note 07) already prototype
lifecycle-as-organizing-principle: an operation tree pivotable **by lifecycle**
(tasks grouped under Request / Context-Trust / Research / Build), a per-task
phase stepper (Request→Close), and event-log rows tagged `LIFECYCLE · L-01`.
The visual layer assumed this entity exists — this note makes that assumption
true. The fleeting-vs-persistent distinction adds a new visual requirement:
bare-bones entries for fleeting lifecycles, a distinct persistent treatment once
the worktree locks.

## How Deep Did The Tickets Actually Go? (historical)

- **Issue #43** went furthest: sessions as root tasks, gates as `input-required`,
  durable event store, `lifecycle_checkpoint`-style tool sketches. It named
  session-id propagation but did not design minting/propagation — that design is
  what the 2026-06-10 discussions settled.
- **The observer branch** had the richest correlation model
  (`workspaceId/sessionId/runId/lifecycleId/operationId/taskId/repoName/worktreeId`)
  — precedent, not contract (pre-MCP vintage). The settled model collapses this:
  lifecycle is primary, session is provenance.
- **Issue #46** (note 05) is where per-call observability gets a concrete tool
  surface to attach to.

## Invariants To Preserve

- Approval gates remain durable and auditable — the lifecycle entity formalizes
  them, never softens them.
- The lifecycle record is append-only history + current-state projection, not a
  mutable status field with no memory.
- A lifecycle that vanishes mid-chat must be detectable (staleness via last-event
  age — precedent: `setup-progress.json` heartbeat/stale rule). Staleness
  detection applies to every lifecycle; TTL cleanup applies only to fleeting
  ones — rotting persistent lifecycles are surfaced for the developer to step
  in, never auto-reaped.
- Ids are minted locally (no network), unique across parallel sessions.

## Why This Is Note 01

Every other note consumes this one: events need a subject (02), the control
plane needs a gate-bearing entity (04), reads need attribution (05), the
attention queue is a *projection over lifecycles* (06) — and the `blocked`
state is precisely what feeds it.
