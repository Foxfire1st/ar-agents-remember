# skills/l-01-agent-lifecycles/roles/orchestrator.md

## Governing Overview

[l-01 role overview](overview.md)

## Purpose

This source defines the sprint-bound orchestrator as a **spawned backend portfolio seat that runs one
sprint's backend as an event loop over durable task state, not a conversation** (`:8-11`). It routes
backend events — an architect dispatch, a manager handover, a worker report, a verdict, or its own
finding — into portfolio and orchestration work, releases only the ready generation a valid
projection admits, lands the super integration branch, and **never converses with the developer**:
every developer-worthy item leaves as one decision item to the architect. The architect ordinarily
creates this seat, while an identity-free developer launcher may target it only for an explicit
task-seat takeover.

## Code Commentary

### The Function Shape

The file is now one self-contained role page in the corpus's function shape — `## Inputs` (`:13-31`),
`## Process` (`:33-117`), `## Outputs` (`:119-150`), `## What you may do` (`:152-172`), `## What you
must not do` (`:174-190`) and `## Stop and escalate — the architect is your ceiling` (`:192-228`).
The seat handbook this card previously described — the Job P / Job O listings, the standalone
hat-collapse rule, the invariant ladder, the `## Knobs` block and the role table — is gone: those
duties are now numbered items inside `## Process`, and the generic event loop is no longer restated
here.

**Inputs (`:13-31`).** The canonical JSON-primary sprint/master/leaf documents read from durable
state (never a transcript, including the rung-up documents the seat must not mutate); the
architect-ruled plan — the adopted orchestration task, or the record of a developer-sanctioned
strategist skip — with its requirement-corpus references, reasoned topology choice, every commanded
master's `executionNature` and any `executionGraph`; the control plane's mechanical facts (graph
validity, derived waves, completed predecessors, current closeout-door generations, closeout-
projection validity, lineage, gates, and changed routes/seams) against this seat's own judgment
inputs (the accepted priority grade and any recorded urgency change); the review mode with its
sealed baseline, preceding result and outstanding IDs when a seam was requested; the resolved memory
layer; and the templates/catalogs the seat compiles from. A brief missing one is incomplete and is
refused, never repaired by guessing.

**Process (`:33-117`).** The generic event loop has a single home — `../operations/coordination.md`
— which owns routing an event by what exists and what is asked, building the legal frontier,
selecting from current truth rather than a queue row, the recompute triggers, and the one-item
developer relay, and **governs where the two files disagree** (`:35-38`). On top of it this page
carries the opening move (converge on the canonical `(sprint document, orchestrator)` seat, run the
trust checkpoint, `lifecycle_start`, orient and say the portfolio back before asking anyone to
decide, then route the event), the standing authority the developer's plan acceptance gives the
subordinate edges (the seat does not stop merely because an operation creates a commit, advances a
lifecycle, cleans up a spent worktree, or fast-forwards a subordinate branch), and **eight portfolio
duties**: the topology and its single home (`:55-62`), priority judgment recorded before it changes
selection (`:63-66`), release and landing per execution nature (`:67-73`), the spirit test
(`:74-80`), master exit through the one open `master-handover-approval` gate (`:81-87`), four
failure rules (`:88-95`), processing and acking the signals the seat is woken with (`:96-100`), and
no native sub-agents on this seat (`:101-104`). It also fixes **the children and the dispatch** —
managers, system-specialists and the same-sprint super-exit reviewer are this seat's; the
strategist, a separate designer chair and the plan reviewer are architect children, and leaf/route
and master-exit reviewers are manager children (`:106-112`) — and **role-seat immutability**: a
dashboard-owned orchestrator session stays an orchestrator for its lifetime, a pasted brief for
another role is refused and escalated to the architect, and roles expand horizontally rather than as
native sub-agents (`:114-117`). The single structural dispatch transaction is `dispatch_agent` once
with the target's real task document, the role and one complete brief, where `dispatched` and
`dispatch-queued` both mean the brief is durable.

**Outputs (`:119-150`).** The super-exit packet plus demo notes — shape authority
`../templates/conversation-handover-packet.md`, and it must offer a reviewable environment and carry
"what changed visibly" demo notes per master; the adopted orchestration task with its adoption
decision-log entry; **the producers' curator hand-off list handed over unparaphrased** (`:127-131`);
durable notes and reports with decision-log entries; and the self-improvement close stated as
proposals only. A turn ends when its artifact is written and nothing is pending, and a resumed
successor reconstructs everything from durable state alone.

**Permissions and limits (`:152-190`).** `task_doc` authoring; the master-handover `gate_decide`
plus `gate_list`/`lifecycle_gate` and `dispatch_agent`/`retire_child` for direct children — never a
strategist on this seat's own authority; the closeout, landing, lifecycle and message tools; the
by-hand portfolio-wide retire authority as an exceptional case (`:165-169`); and read-only
retrieval. Never converse with the developer, never pull the designer hat, never dispatch the
strategist on this seat's own authority, never build a seat-local watcher, and never set the
operator knobs.

**Stop and escalate (`:192-228`).** The architect is the ceiling, and the **quo-vadis test** — not
being stumped — decides what goes up; a high-blast-radius truth goes up immediately as a four-field
decision item, and never a second developer item while the first is unresolved. The hand-off
junctions and the gate kind each carries are `../operations/closeout.md`'s table, and provider
degradation has a fixed four-step response ending in the always-legal provider teardown when the
issue is not fixable in session (`:214-224`).

### Invariants And Boundaries

- The seat is a spawned backend seat: it never converses with the developer and never wears another
  role's hat.
- The generic event loop belongs to `../operations/coordination.md`; where the two disagree, that
  file wins.
- Only the first-ready generation a `valid-built` projection admits is released, priority judgment
  is recorded before it changes selection, and integration branches are not workbenches.
- No seat-local watcher, polling, nudging, or timer loop; a finding held only in a chat is a bug.
- Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
  outputs. Dispatch proof remains exact-session and fail-closed; plane refusal never becomes an
  ambient retry.


## 260805-ARG-L1 Completion Cleanup And Quality Retry — as the rewrite leaves it

The master-to-super integration duty keeps manager/orchestrator owners out of automatic cleanup
while retiring exact-leaf worker/reviewer/curator seats only after their durable report is present;
the rewritten file carries that as the by-hand portfolio-wide retire authority plus
`retirement.autoCloseCompletedSeats=false` restoring the previous landed/archive behavior for the
three automatic leaf-altitude roles (`:165-169`). **Correction (260915-KS-L28):** the cheap-first
ordering and content-addressed retry contract this entry also recorded is no longer stated in this
file — the function-shape rewrite leaves the landing mechanics to `../operations/closeout.md`
(`:67-68`) — and the transaction paragraph survives as the seat consuming worker targeted checks and
the curator's **complete** memory-quality result as the edge's prerequisite evidence (`:67-73`).

## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; memory quality is the curator's standing exception — the curator always runs it complete, and that result travels with the landing edge as prerequisite evidence, never relabelled as full green. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

- The seat's self-definition is an event loop over durable task state that never converses with the developer. [1]
- The generic event loop is owned by the coordination operation, which wins on disagreement. [2]
- The topology duty fixes super off `main`, organizational vs atomic masters, and the waiting final push. [3]
- Priority judgment is recorded before it changes selection. [4]
- Release and landing follow execution nature, with worker checks and the curator's complete result as prerequisite evidence. [5]
- The spirit test is this seat's alone and cannot widen a fix-verification scope. [6]
- Master exit decides one open manager handover gate and never treats a verdict as the decision. [7]
- The seat owns the portfolio bird's-eye through eight numbered duties. [8]
- The seat's children are enumerated with the manager/system-specialist/super-exit reviewer split. [9]
- Role-seat immutability refuses a pasted brief for another role. [10]
- The producers' curator hand-off list is passed through to the curator unparaphrased. [11]
- The by-hand portfolio-wide retire authority is exceptional and the write surface is enumerated. [12]
- The seat's prohibitions and the architect ceiling with its four-field decision item are explicit. [13]
- Provider degradation has a fixed four-step response that ends in the always-legal teardown. [14]

### Cross-Repo References

No meaningful cross-repo references.

## 260713-TES-L5 Current Delta — Idle Safety Via The State-Signal Relay

The orchestrator's idle-safety line now says silence is supervised by the agent-notifier sweep
and the state-signal relay; the escalation ladder is no longer part of the supervision story.
Ending a turn with nothing pending remains correct.

## R39 Generic Orchestrator Doctrine

The canonical orchestrator role resolves quality mechanics from the active repository memory and
keeps acceptance at leaf closeout and master integration only. Repository-specific Dagger/retry
instructions no longer leak into generic orchestration.

## 260815-DAG-L2 Ready-Frontier And Landing Authority

The orchestrator mechanically recomputes the ready frontier after candidate, blocker, landing, or
accepted-priority changes, then applies explicit priority judgment with canonical graph node order
only as the deterministic equal-priority tie-break. Every queue judgment records rationale,
evidence, author, confidence, and supersession before it changes selection; ordinary bounded
reprioritization stays here, while a substantial graph/classification reshape is proposed through
the architect-owned strategist loop.

Organizational leaves land directly on super as released; the final leaf is combined with prior
contributions into the exact proposed final candidate and receives the one full master gate before
super moves. Atomic masters expose no intermediate leaf state to super, but source-pair selection
may pause one live master and select another without retiring either durable branch. The separate
landing authority serializes only conflicting protected-ref movement. Integration refs are not
feature/fix workbenches, and super-exit repairs return to an owning, reopened, or newly scoped leaf.

## IAS Activation, Queue, And Reconciliation Boundary

Before a manager or worker receives implementation exposure for an atomic master, the control
plane selects its exact code/memory source pair as `reconciling`, auto-pauses the former selection,
reconciles both recorded bases, and publishes `active`. Reviewer and curator inspection does not
switch selection. Chats, processes, worktrees, contracts, and claimed lifecycle journals remain
intact across a logical pause.

Task authoring is not subordinate to selection or queue state. Valid task mutations publish first,
then invalidate/rebuild affected disposable projections. Queue rows merely observe
active/reconciling/paused/vacant facts and own no lifecycle or commit evidence. A malformed selector
fails closed only for affected projection/admission and is replaced with archived evidence by an
exact selecting operation; there is no contract-presence fallback.

Retained sync or integration conflicts are agent-owned when current requirements, code, tests, and
decisions determine a resolution. Continue or cancel the contract-addressed operation through its
advertised API; escalate only genuine semantic ambiguity through the architect.

**Correction (260915-KS-L28):** the function-shape rewrite no longer carries this section's
source-pair and queue doctrine in this file. The generic event loop and its selection duty now live
in `../operations/coordination.md` — "selecting from current truth rather than a queue row"
(`:35-36`) — the seat receives closeout-door generations, closeout-projection validity, lineage and
gates as control-plane inputs (`:22-25`), and the file forbids leaving an intrinsically valid task
write undone because a closeout generation exists and forbids mutating an old queue row
(`:184-185`). The paragraphs above are kept as the historical record of the pre-rewrite file.
