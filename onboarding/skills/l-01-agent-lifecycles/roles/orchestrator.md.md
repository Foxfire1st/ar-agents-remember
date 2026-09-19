# skills/l-01-agent-lifecycles/roles/orchestrator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/orchestrator.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-19T17:09+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312`|
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

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

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The seat's self-definition is an event loop over durable task state that never converses with the developer. | "You run one sprint's backend as an event loop over durable task state, not a conversation." | skills/l-01-agent-lifecycles/roles/orchestrator.md:8-11 |
| The generic event loop is owned by the coordination operation, which wins on disagreement. | "The event loop itself is" | skills/l-01-agent-lifecycles/roles/orchestrator.md:35-38 |
| The topology duty fixes super off `main`, organizational vs atomic masters, and the waiting final push. | "**The topology, single home.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:55-62 |
| Priority judgment is recorded before it changes selection. | "**Priority judgment is recorded before it changes selection**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:63-66 |
| Release and landing follow execution nature, with worker checks and the curator's complete result as prerequisite evidence. | "**Release and land per execution nature**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:67-73 |
| The spirit test is this seat's alone and cannot widen a fix-verification scope. | "**The spirit test — this seat only.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:74-80 |
| Master exit decides one open manager handover gate and never treats a verdict as the decision. | "**Master exit.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:81-87 |
| The seat owns the portfolio bird's-eye through eight numbered duties. | "**Four failure rules.**"; "**No native sub-agents on this seat.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:88-104 |
| The seat's children are enumerated with the manager/system-specialist/super-exit reviewer split. | "**Your children and their dispatch.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:106-112 |
| Role-seat immutability refuses a pasted brief for another role. | "**Role-seat immutability.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:114-117 |
| The producers' curator hand-off list is passed through to the curator unparaphrased. | "**The producers' hand-off list, handed to the curator unparaphrased.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:127-131 |
| The by-hand portfolio-wide retire authority is exceptional and the write surface is enumerated. | "**The portfolio-wide retire authority, exceptional cases only.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:152-172 |
| The seat's prohibitions and the architect ceiling with its four-field decision item are explicit. | "**The developer-worthy wait is a decision item**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:174-204 |
| Provider degradation has a fixed four-step response that ends in the always-legal teardown. | "**Provider degradation — your own four-step response.**" | skills/l-01-agent-lifecycles/roles/orchestrator.md:214-224 |

## Cross-Repo References

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

## Update History
- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`): re-read this card against the source at `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678` (previous verification stamp `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`). **This is a rewrite, not an increment:** the diff replaces the whole 614-line `Lifecycle — Orchestrator` seat handbook with a 228-line self-contained role page in the corpus's function shape — `## Inputs` (`:13-31`), `## Process` (`:33-117`, whose generic event loop now lives in `../operations/coordination.md`), `## Outputs` (`:119-150`), `## What you may do` (`:152-172`), `## What you must not do` (`:174-190`), `## Stop and escalate — the architect is your ceiling` (`:192-228`) — and adds **the producers' curator hand-off list passed to the curator unparaphrased** (`:127-131`). Body: replaced the Purpose and the whole Code Commentary with a re-derived account of the current text (inputs; the coordination-owned event loop and the eight portfolio duties; the children/dispatch split; role-seat immutability; outputs; permissions; the architect ceiling with its four-field decision item and the provider-degradation response), corrected the CCR-R12@v5 boundary's "full memory quality … explicit operations only" clause (the curator's complete result travels with the edge as prerequisite evidence, `:67-73`), and folded the 260805-ARG-L1 section into a corrected dated note — its still-true retirement fact is kept, while the cheap-first/content-addressed retry paragraph it recorded is no longer stated in this file after the rewrite. The IAS section carries the same treatment: its source-pair/queue doctrine is no longer in this file and is marked as the pre-rewrite record. Citations: this card was prose-only, so a Repo-Internal References table was **added** with fourteen rows, each anchor verified inside its cited extent at HEAD (seat definition `:8-11`; coordination-owned loop `:35-38`; topology `:55-62`; priority `:63-66`; release/land `:67-73`; spirit test `:74-80`; master exit `:81-87`; the eight duties `:88-104`; children `:106-112`; immutability `:114-117`; hand-off list `:127-131`; retire authority `:152-172`; prohibitions and decision item `:174-204`; provider degradation `:214-224`).
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: documented the
  orchestrator-stamped sprint super reviewer and its separation from the architect plan-review
  generation. Verification remains closeout-owned.

- 2026-08-30T12:57+02:00 — 260821-ARSPAWN-L3 review correction: replaced create/replace
  takeover wording with idempotent canonical-seat convergence. Verification remains
  closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the orchestrator as a plane-hosted caller
  and explicit ambient-takeover target, removed caller-visible readiness sequencing, and kept its
  structural authority outside settings. Verification remains closeout-owned.

- 2026-08-26T08:35+02:00 — Restored the required navigable governing-overview link while
  reconciling orchestrator activation doctrine.

- 2026-08-26T05:20+02:00 — Replaced the global exclusive-blocker reading with exact source-pair
  selection plus separate landing authority; documented pause preservation, task-authoring
  primacy, disposable queue projection, and agent-owned resumable conflict resolution.
  Verification remains post-Dagger/closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: recorded ready-frontier recomputation, auditable queue
  judgment, organizational direct landing, atomic blockers, and no-workbench repair routing.
  Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled canonical orchestrator guidance with generic
  repository-resolved policy. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 cadence: recorded the exact leaf-closeout/master-integration
  acceptance owners and the pull-request-only non-test GitHub boundary.
- 2026-08-10T07:30+02:00 — 260805-ARG-L1: recorded exact-leaf subordinate completion cleanup and
  the cheap-first/content-addressed quality retry doctrine. Verification metadata remains blank
  until closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the idle-safety wording — silence
  is supervised by the agent-notifier sweep and the state-signal relay; the escalation ladder
  is no longer part of the supervision story. Verification metadata pinned until closeout
  stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
