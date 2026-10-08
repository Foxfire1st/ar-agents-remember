# skills/l-01-agent-lifecycles/roles/manager.md

## Governing Overview

[roles overview](overview.md)

## Purpose

The manager is one persistent seat on one canonical master document. It owns that master's leaf
execution and closeout chain: dispatch workers, verify builder evidence, obtain independent review,
obtain curator coherence, decide delegated leaf gates, close out and integrate leaves, and hand the
completed master to the orchestrator.

## Logic

For each dependency-ready real leaf, the manager calls structural `dispatch_agent` with the leaf
task document, role, and complete brief. The control plane owns readiness and the exact-pinned initial
brief; the manager never requests or stores an occupant id. The manager starts the Worker and Reviewer together and the Curator at the first freeze; the
leaf's Worker, Reviewer and Curator hand freezes, findings, verdicts and memory changes directly to
each other. Before the gate the manager inspects the complete changed-file diff and both verdicts
and calls `worktree_status` for the canonical leaf, requiring the complete task-derived
`sourceLineage` projection to be current; the curator brief carries it and dispatch re-proves it
before host creation. It consumes the worker's targeted-check
report and curator's scoped onboarding handoff before the closeout transaction. Closeout and
integration do not launch or require full quality, full tests, full memory quality, certification, or
review; any explicitly requested operation remains owned by its existing lifecycle workflow.

The role table advertises this seat as a plane-hosted caller and an explicit ambient-takeover
target. The orchestrator ordinarily creates it; once hosted, it dispatches only its direct
worker/reviewer/curator children. Its public request never selects caller kind, and a plane
authorization refusal never retries as an ambient launch. The `dispatch` and `tools` rows describe
structural authority/capability rather than settings keys.

Before dispatch, the manager independently verifies that every exact stable ID + version points to
the approved version-addressed packet and that the packet carries its durable corpus-ruling
citation. Missing, duplicate, unapproved, or mismatched revisions make the brief invalid rather
than a condition the worker is expected to repair.

When all leaves land, an adversarial master-exit verdict becomes evidence on the handover seam; the
manager writes the master-handover packet and remains reachable at `(master document, manager)`.
Ordinary follow-ups and escalations use structural child/parent messaging so replacements are
transparent.

Before worker dispatch, the manager compiles the exact stable IDs applicable to the leaf, including
inherited master requirements. It requires one complete worker envelope per ID and gives that same
set to the reviewer for independent accepted/rejected adjudication. Missing/duplicate IDs, missing
evidence fields, or an overall pass with any rejection fail closed. The separate durable-evidence
promotion hold point remains in both briefs and cannot satisfy requirement acceptance.

The same loop also carries exact attempt identity. The manager compiles the next review-handoff
attempt ID without advancing it at dispatch or during internal implementation/test/evidence runs,
checks the lightweight immutable worker record and its content-addressed expanded-evidence anchor,
and sends that exact candidate to review. It records bounded invalidation only after independent
direct-regression proof and maintains a rebuildable master summary linked to leaf journals; leaf
records remain authority and summary freshness never gates task, lifecycle, closeout, integration,
or queue work.

Internal runs stay in a separate protocol-event log. Repair to a reviewer-rejected manifestation
creates a successor at the next handoff. An unrelated later candidate does not reopen accepted work.

The curator receives that same exact approved revision set, every canonical packet, the durable
corpus ruling, and the reviewer's per-revision adjudication. Rejected or worker-blocked revisions
are curator blockers, not authority to write current onboarding intent.

## Conventions

- One manager sees one master, not the portfolio.
- Independent leaves dispatch in parallel unless a named dependency or one-writer constraint applies.
- Builder, reviewer, and curator are distinct real leaf seats with distinct artifacts.
- Delegated decisions are attributed; human-only gates remain human-owned.
- Completed subordinate seats may be reclaimed only after their durable report exists.

## Invariants And Boundaries

- Manager identity is the canonical master document plus `manager` role.
- Manager never becomes a native sub-agent, worker, reviewer, curator, orchestrator, or architect.
- Manager may retire only its own master's worker/reviewer/curator child seats.
- Manager owns reviewer dispatch at two altitudes: leaf review on the leaf document and master-exit
  review on its master document; both generations are stamped back to this manager.
- Manager does not self-approve, bypass blocked checks, or invent portfolio-wide authority.
- Handover and completion rely on durable artifacts and terminal/finalizer truth, not model completion posts.
- A worker/reviewer pair must cover the same exact stable requirement set.
- A worker/reviewer pair must bind the same exact attempt and candidate; neither can rewrite the
  requirement or prior attempt record.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full quality, full tests, full memory quality, certification, and independent review are explicit operations only. Requested reviews retain the sealed finding list and monotonic three-round limit.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The Manager no longer carries freezes, findings, verdicts or memory changes between a leaf's agents: it starts the Worker and Reviewer together and the Curator at the first freeze, reads the leaf's state from reports and task records, hears from the leaf only on its named occasions (closeout readiness, rule-5/6 notices, ownership or authority, an extra round or pass, a disputed Curator code finding, a Manager-owned sync step), decides the gate and keeps closeout, integration, status, acceptance and landing order. It gains the same harness-freedom paragraph.

## Evidence

### Repo-Internal References

- One manager owns one canonical master and the complete leaf closeout chain. [1]
- Hosted child dispatch uses leaf document, role, and complete brief without retained occupant ids. [2]
- The leaf loop sequences builder, reviewer, exact-packet/adjudication curator intake, closeout, integration, and cleanup duties. [3]
- Master exit and handover use durable verdict/packet evidence and structural ownership. [4]
- Structural parent/child messages are the role's communication path. [5]
- Manager dispatch compiles and preserves the exact per-ID acceptance set through reviewer and curator handoffs. [6]

## L23 Manager And Leaf Admission

The manager seat is created only after current master ancestry is proved, and
each worker/reviewer/curator dispatch re-proves the complete parent chain.
Recovery is contract-addressed and replacement-safe; no agent supplies branch
commit or session identity.

Pre-curator admission is manager-owned: the Curator is started when the Worker's first freeze
exists, and the leaf's seats hand their inputs directly before any onboarding work. If super or master moved, the manager synchronizes and reconciles the code first;
the curator is never asked to document a stale leaf. Closeout and integration independently repeat
lineage after long quality gates to close their later time-of-check/time-of-use windows.

## R39 Generic Manager Doctrine

The canonical manager role resolves executor, environment, arguments, resources, retry, and
evidence from repository memory. Leaf closeout accepts once, leaf integration reuses that commit,
and master integration accepts full once; no fallback is inferred.

## 260815-DAG-L2 Nature-Aware Manager Boundary

The manager owns one organizational or atomic task group but does not rank the sprint. It reports
only closeout-ready facts—canonical refs, routes, seams, blockers, and current acceptance—and waits
for the orchestrator's recomputed-frontier release. Organizational leaves close against the current
super source and land directly; atomic leaves close against the isolated master branch and expose
nothing to super until the whole block is ready.

At organizational master exit, any review or full quality operation runs only when explicitly
requested and uses the exact proposed candidate. The ordinary exit still consumes the prepared Git
transaction and its authority/ref safeguards.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
