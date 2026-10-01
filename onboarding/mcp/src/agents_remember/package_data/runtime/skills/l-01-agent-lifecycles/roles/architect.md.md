# l-01-agent-lifecycles/roles/architect.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The portable **architect** lifecycle: the developer-facing owner seat for the `l-01-agent-lifecycles`
stack. It owns the design conversation, drawing-board rounds, decision pacing, and durable rulings
back to backend seats. It is a sync-propagated (`scripts/sync-skills.py`) package-data copy of the
canonical `skills/l-01-agent-lifecycles/roles/architect.md`.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` rather than restating them: all five shared blocks (`core/authority.md`,
`core/invariants.md`, `core/lifecycle-frame.md`, `core/loop.md`, `core/acceptance.md`) plus
`operations/orientation.md`, `operations/planning.md`, `operations/coordination.md`,
`operations/review.md`, and `operations/recovery.md`. It is still the corpus's longest role file (383
lines) because it is the only seat that may wear another role's hat.

## Code Commentary

### Spawn Doctrine And tools.md (260731-EFA-L16)

Two developer rulings landed here. First, the immutability clause now binds role-seat creation to
the public `dispatch_agent` transaction — its internal session primitive is plane-owned, and a role
seat is never a native sub-agent — while native sub-agent
fan-out is scoped to the one mode where this seat does hands-on work: solo build under the worker
discipline (developer correction). Once orchestration runs, analysis goes to spawned role seats.
Second, the Opening Move gained a standing read of the resolved `system/tools.md` — as the repo's
tool INVENTORY, not merely the quality gate — phrased generically (whatever test/lint/build/
smoke-check, discovery, and repo-local command notes that repository actually provides), because
the role files ship with the package across repos whose memory layers name different tools
(developer ruling: this role file never named the file at all; the solo-build bullet also names
the wrapper as its checks authority). Third, the drawing-board phase now names its shared
doctrine: `tasks/AGENTS.md` (task-collaboration doctrine) governs HOW the problem gets
decomposed before planning — reviewable reframing (surface request vs deeper objective vs
highest-leverage framing), explicit assumptions/truth gaps/invariants/non-goals, typed evidence
plan, examples before risky change, and an implementation plan derived from the framing sections
rather than substituted for them.

### Logic

**Where the doctrine this card used to describe now lives.** The consolidation moved the architect's
shared rules out of the role file and out of the router into single homes, so the sections below still
describe rules in force at their new anchors: seat authority, immutability, the dispatch transaction,
takeover, the escalation ladder, clarification triage, delegated series authority, the decision relay,
and notify-and-stop are `core/authority.md`; the task-doc → branch → worktree spine, default behavior,
and knob resolution are `core/invariants.md`; the trust checkpoint and provider-degradation handling are
`core/lifecycle-frame.md`; the three-party loop, tiers, rounds/convergence, and requirement-compilation
precedence are `core/loop.md`; completion truth, per-ID acceptance envelopes, and attempt lineage are
`core/acceptance.md`.

The synchronized dispatch table distinguishes ordinary identity-free architect bootstrap from an
explicit named-role task-seat takeover. Once hosted, architect dispatch remains plane-authorized;
the dispatch/tools rows describe fixed structural authority and capability rather than settings.

The packaged role dispatches the sprint plan reviewer and receives a plane-stamped reviewer
generation back at the architect parent address. This is distinct from the orchestrator-stamped
super reviewer at the same sprint+reviewer seat; architect retirement authority cannot cross that
generation boundary.

The synchronized architect contract keeps semantic revision under explicit developer approval and
keeps internal repair/test runs as protocol events until an exact candidate is handed to review.

The packaged architect lifecycle now arrives as a sprint-local command seat launched by free chat.
Its backend spool-up is scoped to the same repository+sprint binding, so decision custody and
orchestrator ownership cannot drift onto an architect from another concurrent sprint. The
developer-facing launcher remains outside that named-seat identity.

The file defines the HFX-L6 architect/orchestrator split. The initial developer-facing free chat is
a launcher, not this seat; it spawns a clean architect with the settings-owned profile for
role-shaped work. Once spawned, the architect owns the developer conversation and the backend
orchestrator never talks to the developer directly. Opening move:
read workspace instructions, resolve active Agents Remember context, run the trust checkpoint,
read portfolio state plus pending architect-addressed inbox items, and say back state before asking
the developer to decide.

Event routing maps developer shaping to **Design** (wear `roles/designer.md` inline), backend
`decision-item` rows to **Decision relay**, approved portfolio execution to horizontal role spawns,
no-state-change asks to research-only exit, and small unspawned work to architect-only solo/flat
hat-collapse. Since 260707-HFX2-L7, developer clarifications during an active task first run the
shared Developer Clarification Triage rule: if queue context shows the clarification is
close/current/small, the architect folds it into the active task surface and implements under the
current owner hat; if it is future queue, it is recorded durably for later planning; unclear fit is
asked back to the developer directly. Role-seat immutability is explicit: dashboard-owned architect
sessions stay architect; pasted role briefs are refused/escalated through the inbox; roles expand
horizontally by new chats; sub-agents drill vertically for analysis only.

The minimal decision-item relay uses the existing operator inbox, not a new queue schema. Backend
seats post one `messageKind: decision-item` at a time with decision/options/consequences/evidence
refs. The architect presents one item, records the ruling durably in `openQuestions`, decision logs,
or notes, then returns one `messageKind: decision-ruling` row referencing the durable ruling. Vague
items get a clarification row instead of a guessed decision.

The architect can spawn backend roles with refs to durable state (`AR_SPAWN_ROLE=orchestrator`,
`strategist`, `designer`, `manager`, `worker`, `reviewer`). It proposes the strategist pass as a
developer question and never auto-runs it; it likewise proposes the short root when work is truly
tiny. Solo/flat hat-collapse is reserved here:
the architect may wear backend/build hats only when no spawned role owns that work, and
owner-never-self-approves still holds.

The strategist question is driven by missing or stale evidence-backed topology/classification
reasoning, not by graph absence. A reviewed graph-less atomic-sequential activation choice is
valid: canonical commanded-master order is an equal-priority tie-break, and per-contract activation
lets two sprint-commanded atomic masters sharing one protected source pair hold independent records
without integration or retirement. Nothing serializes such a sprint (developer ruling): a graph-less
sprint declares no dependencies, so `atomic-sequential` names the sprint's shape — every commanded
master executes atomically — rather than a scheduling mechanism, independent masters proceed
concurrently, and only an explicit `executionGraph`'s `predecessor-incomplete:` waves gate. When the
developer sanctions a strategist skip, the orchestrator inherits the complete reasoning duty and
must author the reasoned plan plus explicit topology choice before manager dispatch; that choice
may remain graph-less. Adding a master remains one atomic `attach_master` operation, with graph-node
membership equality required only when a graph exists.

### Invariants And Boundaries

- The initial developer-facing session is a free-chat launcher; the spawned architect then owns the
  developer conversation, while the orchestrator remains backend-only.
- Strategist dispatch and the tiny-work short root are explicit developer decisions proposed by
  the architect, never silent defaults.
- Graph absence alone is neither a strategist trigger nor a defect. The accepted topology choice
  may be the reviewed graph-less per-contract-activated atomic-sequential default, which describes
  sprint shape and serializes nothing across masters.
- Task authoring is upstream of activation and queue state; valid planning changes invalidate and
  rebuild affected disposable projections rather than waiting for runtime scheduling permission.
- A sanctioned strategist skip transfers the full reasoned-plan and topology-choice duty to the
  orchestrator; it never permits an unreasoned implicit choice.
- Escalation terminal custody belongs to the architect; the developer is an authority, not a row
  address.
- Dashboard-owned role seats are immutable for the session lifetime.
- Decision relay is one item at a time over existing inbox rows; durable ruling comes back before
  backend action.
- Solo/flat hat-collapse is allowed only for the architect owner seat.
- Spawned roles receive durable refs, not transcript state, and never become the architect.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- This package-data artifact contains the synchronized architect lifecycle, in the corpus's readable order. [1]
- The role is a self-contained capsule — its dispatch brief is its session start — and it declares no inherited shared sources. [2]
- Strategist recommendation depends on current reasoning, recognizes graph-less atomic-sequential validity, and transfers full duty on a sanctioned skip. [3]
- Master attachment is one atomic attach_master call that writes the typed subTasks row, the orchestrates membership, and — on a sprint with a graph — the graph node, refusing a partial attach. [4]
- The attachment carries the master's explicit ruled executionNature, and size alone never makes a master atomic. [5]
- The shipped architect role still names the graph-less default rather than the removed source-pair-selected wording. [6]
- The architect is the one seat that may wear another role's hat, and the corpus permits exactly that one sibling reference. [7]
- The router's registry still names architect as the developer-facing owner seat. [8]
- The design hat the architect wears inline: with no designer chat, the architect performs this same method inline. [9]
- The canonical source owns this doctrine. [10]

### Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

No meaningful cross-repo references found.

## 260815-DAG-L14 Doctrine Sync

"Adding A Master" is rewritten to the atomic `task_doc.attach_master` flow: one validated batch
writes the typed `masterRef` row, the `orchestrates` slug, the graph lump node (when the sprint
has a graph), and the nature assertion.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## 260713-TES-L5 Current Delta — Mailbox Custody, Not Ladder Rungs (synced copy)

This synced runtime copy now says rows whose entire owner chain is dead surface to the
architect as a mailbox (the timed escalation ladder is retired), rows land at the architect's
turn boundary (the system acks), and `operator_inbox_consume` is an optional attribution
marker. The developer remains an authority, not an address.

## L23 Thematic Master Recovery

The packaged architect role treats a resumed master falling behind super as a
normal synchronization condition. It routes the contract-addressed recovery
through the backend and retries the same canonical master seat; it does not
invent a “part 2” master or burden agents with commit ancestry.

## 260815-DAG-L2 Planning Authority

The architect requires current evidence-backed dependency, route, seam, classification, priority,
and topology reasoning plus explicit `executionNature` for commanded masters before backend
execution. It proposes—never auto-dispatches—the strategist, owns the initial and runtime
plan-review loop, and rules the resulting artifact before orchestrator adoption. The explicit
topology choice may be a reviewed graph or reviewed graph-less atomic-sequential execution.

## 260815-DAG-L13 Scheduling Default Doctrine

The role treats a graph-less sprint as the atomic-sequential default, not as an error awaiting migration:
`task_doc.author_execution_graph` owns graph edits, including the first bootstrap onto a
graph-less sprint; the removed `migrate_execution_topology` is no longer named as the legacy
cutover path.

## IAS Per-Contract Activation Planning Boundary

The synchronized role now defines that graph-less default through per-contract activation rather
than full-integration serialization. The activation record is keyed by the canonical series
contract, so activating one atomic master never pauses, replaces, or blocks a sibling master that
shares the same protected source pair, and the only activation waiting reason is
`atomic-series-reconciling` for that contract's own in-flight reconciliation. Dependency truth
remains an architect planning judgment, while runtime wave gating stays with the sprint execution
graph's own `predecessor-incomplete:` reasons. Otherwise-valid task authoring never consults
activation or closeout-queue state.

**Shipped text corrected (260831-LOCR-L36 round 2).** The mirrored runtime role this card
describes — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md` —
now names the graph-less default correctly in its own text at `:142-143`: a first graph bootstrap
onto a graph-less sprint runs "the graph-less atomic-sequential default, where nothing serializes
the masters". Do not confuse this with a scheduling claim: the sprint without an `executionGraph`
declares no dependency, so independent atomic masters proceed concurrently and only explicit graph
waves gate on `predecessor-incomplete:` (developer ruling). The earlier shipped-source debt note is
therefore removed — a repo-wide grep for `source-pair-scoped`, `source-pair-selected`, the "logically
pauses the former master" admission, one-selected-master-at-a-time and source-pair activation wording
returns 0 hits in the code worktree.

## 260821-DAGQC-L4 Topology-Choice Closure

The synchronized role now closes the graph-optional doctrine end to end: graph absence alone does
not recommend a strategist pass; a reviewed graph-less atomic-sequential choice can justify a
skip; and the skip transfers the complete reasoned-plan/topology-choice duty to the orchestrator.
For sprint attachment, membership and typed rows are always equal, while graph-node equality is
conditional on an existing graph; the Event Routing shorthand repeats that condition and the
nature-ruling requirement. No mandatory-graph runtime or compatibility route is introduced.

The synchronized requirement compiler writes immutable version-addressed packets, records the
durable corpus ruling in every approved packet, and creates a new packet rather than overwriting an
approved revision when semantics change.

## M43 Requirement-Revision Authority Projection

The packaged architect role now keeps ordinary repairs on delivery-attempt lineage and routes a
verified requirement contradiction to developer-approved semantic revision. Worker/reviewer
classification never rewrites the canonical packet.
