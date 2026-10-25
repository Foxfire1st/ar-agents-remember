# skills/l-01-agent-lifecycles/roles/orchestrator.md

## Current supported-pair account — R100/R116 composition

The only changed permission seam now answers held, propagates the named child permission upward, and leaves eventual delivery to the product; no prompt is answered and no duplicate message is sent. Sprint/master containment, Manager coordination, ordinary role/task returns and actual-parent-ID developer questions retain their distinct authority.

This account controls the named changed seams; contradictory earlier card wording below is retained only as historical evidence. Unchanged role duties and R117 file-only wake/report transport are preserved. Source inspection supplies no new runtime test, CODE verdict, review counter or acceptance.

- The only changed permission seam now answers held, propagates the named child permission upward, and leaves eventual delivery to the product; no prompt is answered and no duplicate message is sent. Sprint/master containment, Manager coordination, ordinary role/task returns and actual-parent-ID developer questions retain their distinct authority. [20]


## Message/file transport and return addressing

Messages are short wake-ups naming work and files; report/verdict/evidence content travels in file-only `body` or existing-file `attach`, not pasted text. Within a shared task the files stay in its record and a leaf workspace exposes the folder link. Wake text uses the settings limit without a pinned number. Ordinary report-written notices and final report-path returns use the supplied parent role/task address, including an instructed reporting-recipient change. Developer-needed questions remain addressed to the actual parent/instructed-recipient ID. These are distinct message purposes, not an ID exception to the return rule. Fixed launch-parent identity and existing role/peer/write/acceptance boundaries remain preserved.


## Governing Overview

[l-01 role overview](overview.md)

## Purpose

This source defines the sprint-bound orchestrator: it coordinates one selected sprint when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master. It reuses each Architect-named Manager, starts one Manager for each other master, verifies Manager delivery with separately addressed evidence, and hands the master exit over. It operates at Projects altitude; a Paseo agent's state is not an AR acceptance ledger.

## 260928-MIK-R72@v2 Current Coordination Default And Reporting Duty

MIK-R72@v2 changed the sentences this page's opening account describes. The post-R72 role text selects the Orchestrator when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master; it reuses each existing Manager the Architect names and starts one Manager for each other master. The Orchestrator decides ordinary requirement readings and operational rulings itself, keeps its rulings record, requirement-change list and status file under the selected task's notes for the Architect to read, and messages the Architect only for the four developer-needed categories plus one final report-path notice. The older event-loop account below and the sections that repeat it are retained historical evidence for their own dated files, not the current contract.

## Code Commentary

### The Current Shape

The file is one short role page: `## Work from canonical truth` (`:10-12`), `## Coordinate role agents` (`:14-26`), `## Verify and hand over` (`:28-32`), `## Result contract` (`:34-36`), `## Organise your own work` (`:38-40`), `## Developer questions and answers` (`:42-44`) and `## Questions received from children` (`:46-50`). The seat handbook this card previously described — the Job P / Job O listings, the standalone hat-collapse rule, the invariant ladder, the `## Knobs` block, the role table, the event-loop restatement and the eight portfolio duties — is gone: the page keeps sprint coordination, verification without loop takeover, and the whole owed result.

**Work from canonical truth (`:10-12`).** Resolve the sprint and only the documents needed for current decisions, with exact `taskDocReadArgs`; never fabricate refs.

**Coordinate role agents (`:14-26`).** Reuse Architect-named Managers and start one Manager per other master with `role_start`; those Managers coordinate their Workers, Reviewers, Curators and Investigators. Decide ordinary requirement readings and operational rulings itself, keeping the rulings record, requirement sentences and status file; message the Architect only for developer decisions plus one final report-path notice.

**Verify and hand over (`:28-32`).** Verify each Manager's delivery and aggregate evidence without taking over the loop; the Worker's and Reviewer's Curator hand-off lists go directly to the Curator, which this seat never relays.

**Result contract (`:34-36`).** The owed result is collected whole here: rulings record, requirement-change list, status paths, decision messages, finished-or-unfinishable report-path message, blocker records, verified Manager delivery and pending questions.

**Organise, ask, escalate (`:38-50`).** Seat-owned harness freedom with boundary acts; developer questions to the parent Architect; children's developer questions answered in authority or passed up unchanged.

### Invariants And Boundaries

- The seat is a spawned backend seat: it never converses with the developer and never wears another
  role's hat.
- The generic event loop belongs to `../operations/coordination.md`; where the two disagree, that
  file wins.
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

## 260928-MIK-L99 — a leaf's agents hand over to each other

The Orchestrator keeps its sprint coordination and Manager starts; the change adds the same harness freedom and boundary paragraph as the other roles.

## 260928-MIK-R93 — questions received from children

Beyond the four developer-needed categories, the Orchestrator now answers a child's developer question itself where its authority reaches and says the answer is its own, or passes it up to the Architect unchanged with the originating role, task and agent id and its own recommendation apart. A child that waits at a permission prompt is reported at once with the permission as supplied or "not supplied"; the Orchestrator tries a held message once in each turn it takes until MIK-R100 lands, and the Architect gives it that occasion. Developer answers are returned with the receiving agent's id and the quoted words, passed unchanged.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References















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


## Current Investigator contract impact

The Orchestrator coordinates concurrent masters through their Managers and may start Investigator under its own sprint for a concern or check belonging to no leaf. Leaf checks stay with their Worker and Reviewer. A refusal preserves actual parent routing or the parentless blocker; no invented Architect or recipient identity replaces it.


- The Orchestrator may start Investigator under its own sprint as a child concern and report carrier. [19]



## Evidence


- The seat coordinates one sprint above Managers and verifies delivery without taking over the loop. [16]


- The owed result is collected whole in the Result contract. [17]


- Developer questions go to the parent Architect; children's questions are answered or passed up. [18]
