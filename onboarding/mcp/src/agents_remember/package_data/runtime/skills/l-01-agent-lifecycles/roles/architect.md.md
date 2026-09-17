# l-01-agent-lifecycles/roles/architect.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| This package-data artifact contains the synchronized architect lifecycle, in the corpus's readable order. | `# Lifecycle — Architect`; `## 1 — Purpose And Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:1-13; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:14-52 |
| The role names the shared sources it composes with instead of restating them. | `**Inherits:**` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:12-12 |
| Strategist recommendation depends on current reasoning, recognizes graph-less atomic-sequential validity, and transfers full duty on a sanctioned skip. | `### Spool-up — the chain is self-driving`; `### Mandatory Requirement-Compilation Gate — before task topology` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:89-114; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:115-156 |
| Master attachment keeps graph-node equality conditional on graph presence and states that the graph-less default serializes nothing. | `### Adding a master to a running sprint` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:171-201 |
| Event routing repeats that the atomic attachment adds a graph node only when a graph exists and carries a nature ruling when needed. | `### Event routing` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:202-217 |
| The shipped architect role still names the graph-less default rather than the removed source-pair-selected wording. | "where nothing serializes the masters" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:188-189 |
| The architect is the one seat that may wear another role's hat, and the corpus permits exactly that one sibling reference. | `SANCTIONED_SIBLING_REFERENCES`; `## Knobs, Tool Surface, And Dispatch Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:366-383; mcp/tests/test_role_instruction_corpus.py:110-114 |
| The router's registry still names architect as the developer-facing owner seat. | "design conversation, decision-item relay, and drawing board" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:71-71 |
| The design hat the architect wears inline when shaping intent or task docs. | `# Lifecycle — Designer` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md:1-15 |
| The canonical source owns this doctrine. | `# Lifecycle — Architect` | skills/l-01-agent-lifecycles/roles/architect.md:1-14 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

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

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `SANCTIONED_SIBLING_REFERENCES`; `## Knobs, Tool Surface, And Dispatch Authority` repointed to mcp/tests/test_role_instruction_corpus.py:110-114; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:366-383. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "design conversation, decision-item relay, and drawing board" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:71-71. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `../../../../../../../overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `../../../../../../../overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. SOURCE UNCHANGED BY THIS LEAF; card prose falsified by CAPS-R18@v1. Replaced the shared transaction-boundary boilerplate sentence, which presented full memory quality as an explicit request, with the completed-curation rule.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.** The
  canonical architect role was rewritten (383 lines) into the corpus's readable order and declares its
  ten inherited sources with `**Inherits:**`. Updated Purpose (readable order, inherited sources, and why
  this remains the longest role file — it is the one seat that may wear another role's hat), Logic (a new
  "where the doctrine this card used to describe now lives" paragraph mapping every shared rule to its
  single `core/` home), and Repo-Internal References (the three citations whose anchors no longer exist —
  `Strategist pass — propose, never auto-run.`, `## Adding A Master To A Running Sprint`, `Sprint attach`
  — replaced by current anchors, plus rows for `**Inherits:**`, the knob block,
  `SANCTIONED_SIBLING_REFERENCES`, and the canonical source). The graph-less claim this card tracks is
  preserved verbatim in the shipped role at `:188-189`. **Metadata repair:** `governingOverview` pointed
  at `../../../../../../../overview.md` (the repository root overview) while its link text said "MCP
  package overview"; corrected to `../../../../../overview.md`, and the missing blank line between the
  metadata table and `## Governing Overview` was restored. Verification metadata remains closeout-owned —
  the source is uncommitted, so no stamp was advanced and no commit hash invented.

- 2026-09-13T15:02:41+02:00 — 260831-LOCR-L36 round 2 shipped-text correction: removed the
  shipped-source debt row and debt paragraph and replaced them with the corrected shipped range —
  the frozen architect role now says a first graph bootstrap onto a graph-less sprint runs "the
  graph-less atomic-sequential default, where nothing serializes the masters" at `:142-143`, cited
  as `:134-143`. Body prose now states the developer ruling (nothing serializes a graph-less sprint;
  `atomic-sequential` is sprint shape; independent atomic masters proceed concurrently;
  per-contract activation records each contract's own `reconciling -> active`; only explicit
  `executionGraph` waves gate on `predecessor-incomplete:`), and the document-scope and
  `## Adding A Master To A Running Sprint` ranges were re-grepped and repointed to `:1-391` and
  `:123-160`, with the orchestrator relay ranges repointed to `:1-21`/`:135-182`. Source
  documentation only; verification metadata remains closeout-owned and no acceptance or test claim
  is made.
- 2026-09-13T14:24:00+02:00 — 260831-LOCR-L36 activation re-keying: rewrote this card's graph-less
  planning boundary from source-pair selection with a paused former master to the per-contract
  activation record — each series contract owns its record, the only waiting reason is
  `atomic-series-reconciling`, and a sibling master that shares the protected source pair is never
  paused or waited on — and recorded the shipped-source debt that the frozen mirrored architect role
  still names the removed source-pair-selected graph-less default at its own `:142`, flagged for a
  future code leaf. That debt observation is superseded by the 260831-LOCR-L36 round-2 entry above:
  the shipped text is corrected and the debt note is removed. Source documentation only; verification metadata remains closeout-owned and no
  acceptance or test claim is made.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Sprint attach" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md:187-187. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: synchronized architect
  ownership and retirement bounds for the sprint plan-review generation. Verification remains
  closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized ordinary architect bootstrap versus
  explicit takeover, sole public dispatch vocabulary, and fixed structural-row ownership.
  Verification remains closeout-owned.

- 2026-08-27T21:53+02:00 — Synchronized M40@v2 revision-versus-attempt/event authority.

- 2026-08-27T18:06+02:00 — M43: synchronized requirement-revision authority and attempt/version
  separation from the canonical architect role.

- 2026-08-27T14:04+02:00 — Clarified immutable packet addressing, packet-local corpus approval,
  and new-file revision handling in the synchronized architect doctrine.
- 2026-08-27T13:32+02:00 — M39@v1: added the architect-owned requirement-compilation gate before
  any sprint/master/leaf topology, including clause splitting, canonical packets, fresh-agent cold
  reads, developer corpus approval, one-primary leaf projection, and targeted version invalidation
  plus rebriefing. Verification remains closeout-owned.

- 2026-08-26T08:45+02:00 — Restored the canonical Docs reference section for this changed
  synchronized architect-role card.

- 2026-08-26T05:20+02:00 — Reconciled the generated architect role with source-pair activation,
  pause preservation, and task-authoring primacy. Final citation ranges and verification remain
  post-Dagger/closeout-owned.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: reconciled the synchronized
  architect role to graph-optional planning, complete strategist-skip transfer, and conditional
  graph-node membership. Canonical/generated sync is architect-reported green; Dagger acceptance
  and verification stamping remain closeout-owned.
- 2026-08-20T05:10+02:00 — 260815-DAG-L14: "Adding A Master" rewritten to the atomic
  `attach_master` flow. Verified at code commit 2f494982.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: synchronized the scheduling-default doctrine —
  `author_execution_graph` owns graph edits including the graph-less bootstrap; the
  `migrate_execution_topology` reference is gone. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized explicit topology admission and
  architect-owned strategist/reviewer authority. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented replacement-safe thematic-master sync recovery; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Recorded `architect.md` as a synchronized runtime artifact of the current canonical lifecycle doctrine; it introduces no independent role contract.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: aligned the packaged architect lifecycle with
  sprint-qualified custody and spool-up. Verification metadata remains pinned until closeout
  stamps the code commit.

- 2026-08-09T13:59+02:00 — 260713-TES-L5 curator completion round 2: refreshed this synced
  runtime copy for the custody doctrine (mailbox surface; ladder retired; attribution-only
  consume); verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-05T23:30+02:00 — 260731-EFA-L16 curator: recorded the drawing-board doctrine naming — the Design And Drawing Board section now points at `tasks/AGENTS.md` (task-collaboration doctrine) as the decomposition discipline for the phase: reviewable reframing, explicit assumptions/truth gaps/invariants/non-goals, typed evidence plan, examples before risky change, plan derived from the framing (developer ruling; corrected from an initial whether-a-task-is-needed misreading). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T22:10+02:00 — 260731-EFA-L16 curator: recorded the spawn-doctrine binding (role seats only via `spawn_agent_session`; native fan-out scoped to solo build per the developer correction) and the Opening-Move `system/tools.md` standing read — as the repo's tool inventory, phrased generically because the shipped role files span repos whose memory layers name different tools; widened from the solo-build-only naming after the developer noted tools.md is not just the quality gate. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: restored canonical/package-data source ownership
  citations and removed the unsupported hosted-cutover impact section.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T02:39+02:00 — HFX3 retro curation: reconciled the architect card with the free-chat
  launcher, settings-owned clean spawn, propose-first strategist and short-root questions, and
  architect terminal custody. Added the governing-overview backlink. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: event routing now tells the
  developer-facing architect to run Developer Clarification Triage before choosing note-only
  handling. Close/current/small clarifications fold into the active task and implementation; future
  queue is recorded durably; unclear fit asks the developer which route they intend.
- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: created onboarding
  for the new developer-facing architect lifecycle, including design ownership, role-seat
  immutability, one-at-a-time decision-item relay over the existing operator inbox, backend
  role spawning, and architect-only solo/flat hat-collapse. Verification metadata is blank until
  closeout stamps the first commit containing this new package-data source file.
