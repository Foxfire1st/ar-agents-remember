# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/l-01-agent-lifecycles/roles` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-30T03:13:03+02:00 |
| lastVerifiedCommitHash | `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` |
| lastVerifiedCommitDate | 2026-09-30T03:31:21+02:00|

## The curator lifts the decisions that keep governing code (260928-MIK-L13)

[`curator.md`](curator.md.md), Process step 3, gains four lines for MIK-R13 rule 5: on converted memory, the
curator turns each developer ruling and requirement-packet choice that still constrains code into a decision record
with the alternatives it weighed, and leaves decisions that matter only within the task in the task. The step
points to the hand-off template's "Decision records (MIK-R13)" section for the fields and the rules. Lifting is
guidance; nothing enforces it mechanically, and the decision authority stays with the developer. No other role
changed; the package copy and the eight harness starter copies are synced by `sync-skills.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifting pointer in step 3. | "Lift the decisions that keep governing code." | skills/l-01-agent-lifecycles/roles/curator.md:95-98 |

## The reviewer checks a leaf's declared knowledge effects (260928-MIK-L11)

[`reviewer.md`](reviewer.md.md), Process step 7 (where each requirement revision is adjudicated), gains one
line for MIK-R11 rule 2: when the leaf's task document declares `expectedKnowledgeEffects`, the reviewer checks
that declaration against the leaf's requirement packet — its declared subjects and effects match what the
packet requires, with no effect missing and none invented — and a mismatch is a finding. The architect ruled
the line in (Q3, 2026-09-29T21:56:18+02:00). It sits in the role file rather than a criteria catalog, because
the catalogs admit a standing criterion only with catching evidence. Who writes the declaration (the
architect, or the worker with the architect's approval) stays procedural. No other role changed; the package
copy and the eight harness starter copies are synced by `sync-skills.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The declaration check in step 7. | "check that declaration against the" | skills/l-01-agent-lifecycles/roles/reviewer.md:74-76 |

## Curator successor-family examination

The curator role requires explicit stored membership IDs and authored bases when retaining unchanged siblings in a justified family successor. It preserves each existing invariant revision and checks the ordinary published roster. The role’s code, task-state and Git prohibitions remain unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The curator process carries exact retained-sibling authoring and readback. | `## Process` | skills/l-01-agent-lifecycles/roles/curator.md:59-163 |

## Curator authors a rationale for every realization target (260921-ICR-L45)

Process step 3 of the curator role now requires every hand-off target to carry its own authored
`rationale` (why that place carries the obligation, specific to the construct it names) and an optional
`role` before ingest; where the producer gave none, the curator writes it from the evidence. That is
supplying a missing explanation, not re-deriving a producer field. The writer never generates one and
refuses an unexplained target with `realization_rationale_absent`. The role's code, task-state and Git
prohibitions are unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The curator's step-3 rationale duty. | "every target carries its own authored" | skills/l-01-agent-lifecycles/roles/curator.md:70-76 |

## Curator authored knowledge and retained review

The curator remains the leaf memory writer and the bounded taskless foundation author. Leaf ingest requires explicit semantic scope and reports family, source and publication planes independently. Before handoff the role uses the existing comparison producer and carries its actual generation or refusal, including code-only work with validated unchanged knowledge. Lifecycle, code edits and closeout ownership stay with their existing seats.

## 260921-ICR-L32 The Curator Role Is Admitted Taskless, And The Bootstrap Role Reads Rather Than Reaches

Two of this route's ten role files moved, and both movements are the same policy change. `roles/curator.md`'s
foundation-entry paragraph now says the seat is admitted **either way** — opened on a leaf's task document for
the leaf pass, or opened with no task document as the taskless carrier of the repository-foundation entry
(the developer's 2026-09-24 ruling) — and its writer-choice sentence now names the taskless
`agents-remember knowledge-bootstrap` entry as the one a taskless curator session uses, since there is no
enclosure to name. `roles/bootstrap.md` states the admission in the product's own words (the taskless seats
are `chat`, a plain `terminal` pane, this seat, and a **curator seat**) and keeps its own read-and-report half
otherwise unchanged. Both were propagated into all ten copies by `scripts/sync-skills.py`, and the
seat-policy note below each card is dated rather than rewritten, so the L27 note stays true at L27's bytes.

## 260921-ICR-L27 The Curator And Bootstrap Roles Get The Repository-Foundation Entry

`260921-ICR-L27` (`ICR-R27@v1`) gives this route's two role files the **repository-foundation entry** —
the shape a curator's work takes when the scope is a repository's first or resumed knowledge foundation
rather than one leaf's delta — and the seat gate that shape depends on.

**`roles/curator.md` — the same work, a second carrier.** The role file gains a paragraph stating that
the foundation entry is a bounded second shape with its own carrier, and a process block that runs the
`c-14-knowledge-bootstrap` procedure in its order. The ownership is unchanged on both entries: the
reconciliation and the authored knowledge belong to this seat, and there is still one admitted writer
and one declared published location. What changes is the carrier, the admission and the scope.

**`roles/bootstrap.md` — the seat that reads and reports, and authors nothing.** The role's step 5 makes
it the carrier that exists for the foundation before a task does: it reads the state at the declared
knowledge location, reports it, and hands the authoring to a curator — on a task document, or through the
taskless writer an instructed session holds. Its output template gains a `Knowledge foundation:` line,
and its prohibition list gains "Never author knowledge records either."

**The rule both files now state, and that a round-one verdict was `blocking` over.** A session opened
for the curator with no task document is refused (`400 task-binding-required`, "named role scope is
required"), because the opener admits only the taskless seats without one. Before a task exists the step
is therefore carried by the taskless bootstrap seat, not by a curator-labelled session — and the
writing session for a taskless run must have no enclosure in scope, because the taskless writer refuses
one (`enclosure_in_scope`). Both files state that refusal in the code's own vocabulary rather than
asserting an admission the product does not make.

**A repository whose knowledge is not recorded is not reported as ready.** The onboarding and the
baseline can both be complete while the knowledge foundation is absent; the role file states those as
separate facts rather than one verdict.

## 260921-ICR-L28 The Curator Role Authors Family Coverage And Reads Both Planes Back

`260921-ICR-L28` (`ICR-R28@v2`) adds one numbered step to `roles/curator.md` — **Examine family coverage
and author it, then read the two planes back** — and renumbers the steps after it, so the role's
readable order is unchanged while its duty set grows by exactly one. Its **function shape** is
untouched: the role still runs one leaf's whole curation operation, still writes only what is its own,
and still leaves the coherence authority to the step that already owned it.

**What the role now owns.** Two further hand-off keys are the curator's to author — `family` and
`external_sources` — and the template states their shape; the producer writes neither. An entry
carrying neither is reported as **unexamined** rather than as family-free or source-free, and nothing in
either key may be inferred from a path, a route, a label or a shared anchor. The role authors the
family identity with its **own** guarantee text and the exact memberships that place exact invariant
revisions; where no joint obligation is supported it records the deliberate `no_family` outcome **with
its basis**; and it declares every external source it inspected with its document identity, version or
retrieval time, inspected-content digest and location.

**The report is read back as a measurement, not as a success signal.** `family` and `sources` each
carry their own state (`recorded` / `projected` / `not-recorded`), the guarantees authored versus
examined with their exact revisions, the memberships added, reused and retired, the deliberate
no-family outcomes with their bases, and the entries neither plane examined. **A plane whose state is
not `recorded` measured nothing, and its null counts are not zeroes.** The same coverage travels into
the role's record, so the next seat reads a measured result rather than a claim.

**Why the numbers matter to a role file.** The step is placed before the full
`memory_quality_check` operation and before the coherence gate, because authoring both planes is part
of producing the grounded foundation the gate then judges — not a follow-up to it.

## 260921-ICR-L20 The Curator Role Gains An Authoring Step, And Its Function Shape Is Unchanged

One of this route's ten role files moved, and the movement is **inside** an existing section rather
than a new shape. `roles/curator.md` (144 lines) gained the knowledge-authoring obligation the curator
seat had been missing: a fourth numbered step in `## Process` that hands the reconciliation's
requirement-shaped items to the real writer with the ordinary route's invocation
(`agents-remember knowledge-ingest … --baseline <the published dataset this task forked from>
--publish --commit --json`), a line in the permitted-writes list naming that route, a prohibition in
`## What you must not do` against writing the dataset from this seat, and a sentence in the curator
report that carries the read-back identity. The section order this route standardized at
`260915-CAPS-L22` — `## Inputs`, `## Process`, `## Outputs`, then the permitted and prohibited lists —
is exactly what the change slots into, and no `**Inherits:**` line, knob block or sibling reference
changed.

Two route-level rules the change makes explicit, because they are now load-bearing for any seat reading
this file: **a per-entry refusal is a result, not a tool failure** (the report is the product, and a
zero exit is not evidence that the repository holds the knowledge), and **the mounted `knowledge_change`
tool is not a write route at all** — it refuses every record kind and exists only to name the subcommand
that reaches the write plane, which is why the role file's prohibition names it rather than the
operation. **`260921-ICR-L32` corrected that naming to both shipped entry points**: `knowledge-ingest`
for a leaf enclosure's ordinary route and `knowledge-bootstrap` for the taskless repository-foundation
route (the second shipped by `ICR-R29@v1` after this section was written), completed rather than
deleted, and now pinned by a case that reads the refusal's own detail.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The authoring step this route's curator file now carries, with the invocation and the report fields to consume.** | "Author and publish the durable knowledge through the real writer."; "Read the report, never the exit status" | skills/l-01-agent-lifecycles/roles/curator.md:70-70; skills/l-01-agent-lifecycles/roles/curator.md:81-81 |
| The permitted-action line that makes the subcommand this seat's route, and the prohibition that keeps the dataset out of its hands. | "ordinary knowledge authoring route"; "Never write the knowledge dataset yourself." | skills/l-01-agent-lifecycles/roles/curator.md:195-195; skills/l-01-agent-lifecycles/roles/curator.md:212-212 |
| The report sentence that carries the published identity into the handoff. | "knowledge hand-off result"; "published dataset identity" | skills/l-01-agent-lifecycles/roles/curator.md:172-173 |
| The operation block the same obligation landed in, which is the procedure this role file composes. | "Route the durable knowledge through the real writer, and publish it." | skills/l-01-agent-lifecycles/operations/curation.md:60-71 |

## Purpose

This route owns the self-contained lifecycle for each role. Every file states what one seat is,
which task-document altitude it occupies, the loop and artifacts it owns, its communication path,
and the work it must refuse or escalate.

260915-CAPS-L1 rewrote all nine files here into one readable order — purpose and authority → required
inputs → normal workflow → permitted writes and actions → stop and escalation cases → completion and
handoff, then the machine-readable knob block — and each declares the shared sources it composes
with in an `**Inherits:**` line instead of restating them, because the shared rules moved into a new
sibling `core/` and the procedures into `operations/`. A role file may name a sibling role file only to
wear that hat or dispatch that seat (architect → designer; orchestrator → strategist, designer;
strategist → manager; reviewer → manager); the shipped corpus check fails on any other reference. The
route's files are 2,792 → 2,322 lines in total, and the router that selects between them is no longer a
doctrine source.

**That L1 paragraph records what L1 did; it is not the current shape.** leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling)
rewrote all **ten** role files here — architect, orchestrator, strategist, designer, manager, worker,
reviewer, curator, system-specialist and bootstrap — out of the L1 section shape and into one **function
shape**: every file is now `# <Role>` followed by `## Inputs`, `## Process`, `## Outputs`,
`## What you may do`, `## What you must not do`, and a closing `## Stop and …` section, plus a per-role
extra only where a role genuinely has one (`### The checks you owe` in the worker, `## Seam scope, when
your brief names one` in the reviewer, `## Terminal custody — rows whose whole owner chain is dead` and
`## The one hat-collapse this lifecycle allows, and its limit` in the architect). The numbered
`## 1 — Purpose And Authority` … `## 6 — Completion And Handoff` sections, the
`## Knobs, Tool Surface, And Dispatch Authority` block, and the `**Inherits:**` declaration line are all
**gone** from these files; the composed sources are named inside `## Inputs` instead. Any citation into
this route that still names one of those headings is stale. The ten files now total **1,578** lines
(L1 recorded 2,322 across nine), and the corpus test that enforced the old readable order and the knob
block no longer exists under that name — `mcp/tests/test_role_instruction_corpus.py` keeps `ROLE_ORDER`
and `SANCTIONED_SIBLING_REFERENCES`, but not
`test_every_role_source_carries_the_readable_order_and_knob_block`. The `core/` and `operations/`
siblings are unchanged by this pass.

**The line-count change is a structural fact, not a measured context reduction** (labelled by
260915-CAPS-L10, which measured the capsule this corpus feeds). Fewer lines in the role files does not
mean a session reads less: the shared rules and procedures moved into the sibling `core/` and
`operations/` blocks, and a role's capsule now composes them per role and per operation. The one
measurement that exists reports the assembled **capsule larger** than the legacy startup chain at the
worker elevation (**11,828** vs **5,928** tokens, **+5,900**; like-for-like 11,645, **+5,717**), with
manager and architect **UNMEASURED** (`binding-unresolved`) and **adoption acceptance FAILED** —
disposition **REVISE**. Obligation preservation is intact (**36/36** across ten declared roles plus
launcher routing). **No card may describe this route as saving context**; the claim this route may carry
is the single-source, role-addressed structure itself — one canonical file per role, its composed
sources named in `## Inputs`, and every other tree generated from it by `scripts/sync-skills.py`.

## Hot Path Summary

Manager, orchestrator and curator handoffs name actual code/memory output refs and scoped onboarding evidence. They never require a ledger commit, cache freshness proof or cache-repair transaction; downstream consumers can rebuild the ledger from committed attribution.

## Detailed Route Context

Manager hosted dispatch consistently names the canonical leaf or master **task document**. That
vocabulary matches the public structural request and its task-reference authority; generated and
packaged role projections are synchronized from the canonical role file rather than edited apart.

### IAS Frozen Role Boundary

Architect, strategist, and orchestrator responsibilities operate on canonical task documents, not
on a queue-owned copy of the plan. They may change approved planning whenever their role authority
allows; downstream closeout projections are invalidated and rebuilt. For atomic work, implementation
admission is contract-scoped: each canonical series contract owns its own activation record, so
selecting a master publishes `reconciling` for that contract only — which suspends nothing and
excludes no other master — and it becomes `active` only when its own two protected source tips are
current. Nothing serializes a graph-less sprint: a sprint without an `executionGraph` declares no
dependencies, so the shipped `atomic-sequential` default describes sprint SHAPE (every commanded
master executes atomically) rather than a serialization mechanism, and no master is held because
another is selected. No role should discard or terminalize a valid master merely to free scheduling
state.

When source reconciliation retains a conflict, the assigned agent resolves and stages it in the
reported worktree, then continues the same contract-addressed operation or explicitly cancels it.
Private journal/ref identity stays in the plane; role briefs carry the public contract address and
recovery guidance.

Architect owns sprint-level direction, the initial plan loop, and the sprint plan-review reviewer.
Strategist authors the evidence-cited dependency graph when dispatched. Orchestrator adopts the
ruled artifact, maintains the runtime frontier, and records bounded reprioritization judgments;
substantial reshapes return through the architect-owned strategist loop. Manager owns readiness
inside one organizational or atomic master. Worker owns one leaf; reviewer owns independent route
or completion verdict evidence; and curator reconciles ruled intent with implementation.

Reviewer is one target-only role projected at the reviewed artifact's altitude: leaf, master, or
sprint. Managers own leaf and master-exit generations, the architect owns the plan generation, and
the orchestrator owns the super-exit generation. The control plane stamps that structural parent;
the shared role name and sprint address do not blur plan and super authority.

Organizational masters have no integration branch: their leaves are direct super descendants and
the final leaf is reviewed and full-gated as part of the exact proposed super candidate before it
lands. Atomic masters retain the branch-backed, no-partial-exposure block. A failed review routes
repair to an owning, reopened, or new scoped leaf—never to a master or super workbench.

Manager, orchestrator, and worker doctrine shares one quality altitude rule: the pinned Dagger
graph is the only Agents Remember acceptance environment. Leaf closeout selects targeted mode
exactly once; leaf integration and series closeout do not rerun it. The master gate selects full
mode once. Every run receives the explicit task-derived diff base. Host pytest/wrapper execution
is refused; a constrained lifecycle environment may explicitly configure a hard cap.

The manager also owns exact requirement-set compilation: each worker and reviewer receives the
same stable IDs applicable to the leaf. Workers give delivery and verification evidence per ID;
reviewers independently inspect that evidence and adjudicate every ID `accepted` or `rejected`.
Missing or wrong-class evidence, invalid citations, and missing developer approval reject the ID,
and one rejected ID prevents an overall pass. This requirement-acceptance plane is separate from
the durable-evidence stable-contract-or-expiry hold point.

The same role chain preserves append-only attempt identity. The worker writes a lightweight,
candidate-bound delivery record only at review handoff and keeps internal implementation/test/
evidence events separate; the reviewer writes an independent exact-attempt adjudication; the
manager records bounded invalidation and rebuilds an observational summary that excludes protocol
events. Unrelated later candidates do not reopen accepted attempts.

The curator's terminal structured authority is valid only after current-additions coverage and the
full leaf-scoped memory-quality worklist have been repaired and rerun. The lifecycle API publishes
that sole candidate-bound authority and renders Markdown from it. Expected dirty-source drift and
real-commit verification fields remain separately closeout-owned; they do not excuse a repairable
onboarding or citation finding.

Roles are immutable within dashboard-owned seats. For ordinary role-shaped work, free chat creates
the sprint architect through one identity-free `dispatch_agent` call built from the canonical
architect-brief template; an explicit developer-declared task-seat takeover instead targets the
named role at its canonical altitude. Once hosted, architect, orchestrator, and manager are plane
callers with only their documented direct-child scope. Strategist, designer, worker, reviewer,
curator, and system-specialist are target-only roles. The role-table dispatch/tool rows document
fixed structural authority and capability, not settings keys. Plane authorization
failures never retry as ambient launches. Native sub-agents, when allowed by a hands-on role,
remain read/search helpers and never become AR role seats.

## Conventions

- A role file is complete enough to start from its brief without transcript history.
- The source role files are canonical; packaged copies are exact synchronization outputs.
- Each role writes its artifact of record and communicates structurally one rung at a time.
- Shared dispatch/authority doctrine remains in the parent `SKILL.md`.
- Every role table names whether that role is an ambient target, a plane-hosted caller, or
  target-only; the request never carries a caller-mode selector.

## Invariants And Boundaries

- Manager owns a real master; worker/reviewer/curator own real leaves.
- Role replacement preserves the task-document/role address.
- `dispatch_agent` is the only public spawn verb. Ambient and plane authority are disjoint even
  though both use the same exact-brief transaction.
- Builder, reviewer, curator, and owner duties remain separate.
- Curator completion requires the required missing-onboarding and full-quality reruns to name no
  curator-actionable work.
- No role absorbs lifecycle machinery, memory duty, or gate authority assigned to another role.
- Terminal/finalizer truth and durable artifacts, not model completion posts, signal completion.
- No role may collapse per-requirement evidence into an aggregate completion claim.


## CCR-R12@v5 Lifecycle Boundary

Workers provide targeted checks and curators provide scoped onboarding checks with honest failed or not-run states. The prepared code and memory-content outputs move through the authorized Git transaction, whose commit legs suppress automatic quality and test hooks. The consumer ledger is refreshed without a commit while ordinary explicit Git hook policy outside the transaction remains unchanged; full quality, full tests, full memory quality, certification, and review require an explicit developer request. Requested reviews retain the sealed monotonic three-round rule.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The curator owns affected onboarding and admitted knowledge authoring, with full diagnostics and a structured handoff; source code, task and lifecycle writes stay outside the seat. | `## Process`; `## What you may do`; `## What you must not do` | skills/l-01-agent-lifecycles/roles/curator.md:59-163; skills/l-01-agent-lifecycles/roles/curator.md:190-207; skills/l-01-agent-lifecycles/roles/curator.md:208-222 |
| Manager is one master-scoped owner of the builder/reviewer/curator closeout chain. | "# Manager"; "You drive exactly one master's leaf sequence from dispatch to handover." | skills/l-01-agent-lifecycles/roles/manager.md:1-47 |
| Worker is one leaf-scoped builder whose terminal artifact is the turn report. | "# Worker"; "You build one leaf."; "The turn report" | skills/l-01-agent-lifecycles/roles/worker.md:1-33; skills/l-01-agent-lifecycles/roles/worker.md:72-83 |
| The shared registry enumerates every remaining role file. | "## The Role Registry" | skills/l-01-agent-lifecycles/SKILL.md:67-67; skills/l-01-agent-lifecycles/SKILL.md:119-119 |
| Worker and reviewer roles define the two independent halves of per-ID acceptance. | "the one Requirement Acceptance Envelope for your owned primary"; "Adjudicate every requirement revision separately"; "An aggregate verdict or a sampled subset is invalid" | skills/l-01-agent-lifecycles/roles/reviewer.md:70-73; skills/l-01-agent-lifecycles/roles/reviewer.md:101-160; skills/l-01-agent-lifecycles/roles/worker.md:76-89; skills/l-01-agent-lifecycles/roles/worker.md:71-78 |
| The graph-less atomic-sequential default describes sprint shape; nothing serializes the masters. | "nothing serializes the masters"; "nothing serializes its masters" | skills/l-01-agent-lifecycles/criteria/plan-review.md:64-67; docs/reference/execution-topology-migration.md:61-63; skills/l-01-agent-lifecycles/roles/architect.md:28-28 |
| The strategist lifecycle makes topology an explicit choice and refuses an unreasoned default. | "or explicitly adopt the graph-less atomic-sequential default" | skills/l-01-agent-lifecycles/roles/strategist.md:46-46 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle publication and recovery carry the actual code/memory outputs. | `LifecycleOperationRecoveryCommits` | mcp/src/agents_remember/models/lifecycles/operation.py:66-72 |

## L23 Role Recovery Semantics

Architect guidance treats a resumed thematic master behind super as a sync of
the same master, while manager guidance requires current master and leaf edges
before reading or delegating work. Both rely on plane-owned task identity and
never pass branch/commit/session ids between roles.

## L23 Pre-Curator Admission Boundary

The manager's last action before onboarding is a canonical-leaf `worktree_status` call whose full
code and external-memory `sourceLineage` projection must be `current`. That projection enters the
curator brief as evidence, and structural dispatch independently re-proves it before creating the
curator host. This boundary prevents stale onboarding; the later closeout/integration checks remain
separate because they guard ancestry movement during their own long quality phases.

## L23 Final Candidate Route Disposition

Manager, reviewer, curator, and orchestrator roles share one handoff: independent per-route review
is bound to the exact candidate, current lineage is proven before curator creation, and acceptance
uses targeted leaf or full master Dagger authority without model-carried operation ids.

## R39 Generic Role Boundary

Manager, orchestrator, and worker roles now obtain concrete acceptance from repository memory
instead of carrying Agents Remember-specific Dagger commands. They retain the one leaf-closeout,
no leaf-integration rerun, one master-integration cadence and must fail closed rather than invent a
runner or fallback.

## 260815-DAG-L14 Roles Route

`roles/orchestrator.md` replaces the seat-row prescription with the seats-structure +
`attach_master` adoption flow; `roles/strategist.md` and `roles/architect.md` adoption payloads
updated.

## 260815-DAG-L15 Roles Route

`roles/reviewer.md` gained the Review Independence and Evidence-Type Matching section (no self-review; requirement-evidence-type table: rendering → mounted-UI proof, scheduling → operation-level proof, data model → artifact-level proof, doctrine → code anchor); `roles/orchestrator.md` gained the review-independence paragraph. All 9 generated copy trees are byte-identical via `scripts/sync-skills.py`.

## 260821-DAGQC-L2 Curator Quality Invocation

No role authority changed. Curator doctrine now uses explicit sync/start/poll request objects and
treats capacity as poll/wait/retry guidance over the same API, never as permission for a fallback.

## CCR-L42 Review-Phase And Altitude Update

The role files now distinguish a complete `reviewMode=baseline` from
`reviewMode=fix-verification`: the first review seals the agreed scope and issue IDs, while a
successor verifies only those outstanding IDs and cannot add routes, criteria, or new findings.
The role chain also records that standalone and organizational leaves carry independent route
review, atomic child leaves defer to the accumulated master integration review, and workers must
document applicable targeted checks before handoff. Task-document authority and the three-round
review limit remain in force.

## Ungoverned Mirror Status (known defect)

**260915-CAPS-L1 decision, recorded rather than implied.** This leaf rewrote all nine canonical role
files, so a contract-scoped quality pass reports this route's cards as unmodified bodies against changed
sources. The curator updated **this overview**, because route meaning genuinely changed. It deliberately
did **not** refresh the per-role cards under `onboarding/skills/l-01-agent-lifecycles/roles/**`: they sit
outside `pathRules.include`, they are already declared knowingly stale below, and a partial hand-refresh
would leave them mutually inconsistent while duplicating the governed cards on the tracked generated copy
under `onboarding/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/**`.
The govern-or-remove decision this section already asks for also determines whether those cards should be
refreshed or deleted. No fingerprint or verification stamp was advanced.

This route overview lives in the `onboarding/skills/**` tree, which mirrors the code repository's
`skills/**` route. `skills/**` is absent from `settings.json`'s `pathRules.include`, so this whole
onboarding tree sits outside normal onboarding census coverage: it is legacy and ungoverned. It is
retained here only because the contract-scoped memory-quality checker still validates these documents
whenever `skills/**` is part of a leaf's changed set, which is exactly why this overview was updated
by hand rather than by a governed maintenance pass. The remaining sibling sidecars under
`onboarding/skills/**` — the other role, criteria, and template cards — are knowingly stale and are
deliberately left untouched pending a follow-up decision on whether this mirror should be governed or
removed. That mismatch between the declared path rules and the enforced checking scope is itself the
recorded defect.

## 260915-CAPS-L18 Complete Curation Reaches This Route

CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale** — that is the coherence
gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`.
On the success path, where the record is already current, the combined field is **not rewritten** at all
and keeps its incoming `ready-for-closeout` value, with `closeoutReady=true`; `ready-for-closeout` is
therefore observable in the combined field once the whole pipeline is already complete. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** this sentence previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read the raw field to end the
loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.
Note also what that guard is: a **fragment matcher** with a declared blind spot, so a wrong gate restated
in fresh vocabulary is invisible to it, and corrected cards still carry no machine check.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## Update History
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **route body updated.** Added the section "The curator lifts the decisions that keep governing code (260928-MIK-L13)" at the top: the role's four new step-3 lines. One row. Rows below the insertion were re-pointed by the installed fixer or, where it declined, by the exact +4 shift. No verification stamp was advanced.
- 2026-09-30T01:05:55+00:00: Generated citation repair: "knowledge hand-off result"; "published dataset identity" repointed to skills/l-01-agent-lifecycles/roles/curator.md:172-172; skills/l-01-agent-lifecycles/roles/curator.md:173-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 8a187177fd97aa785f74b03e4a26914c71c4a09b0afe5ab323208b62b13057b0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **route body updated for MIK-R11.** Added the section "The reviewer checks a leaf's declared knowledge effects (260928-MIK-L11)" at the top (step 7's new line, architect ruling 2026-09-29T21:56:18 Q3). Rows citing `reviewer.md` below the three inserted lines were re-pointed by the installed fixer or the exact +3 line shift. No verification stamp was advanced.
- 2026-09-28T17:19:01+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): body update — added the section for Process step 3's per-target realization rationale duty. Other ranges re-pointed through the exact base-to-candidate line map. No stamp advanced.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-27T00:23:53+00:00: Generated citation repair: "knowledge hand-off result"; "published dataset identity" repointed to skills/l-01-agent-lifecycles/roles/curator.md:165-165; skills/l-01-agent-lifecycles/roles/curator.md:166-166. No content impact: mechanical anchor-range projection bound to citation source snapshot b3d8afb8f498929bc7654ed009a5dcd2751720da84f958f62808fd0ab2890e00; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-26T23:48:33Z — L39: No route impact: the curator’s existing knowledge-authoring responsibility gains an exact input, without a new role or authority. Current guidance is stated above.

- 2026-09-26T21:21:16+00:00: Generated citation repair: "knowledge hand-off result"; "published dataset identity" repointed to skills/l-01-agent-lifecycles/roles/curator.md:161-161; skills/l-01-agent-lifecycles/roles/curator.md:162-162. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled the current reviewer and curator responsibilities without changing role or transaction authority.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Author and publish the durable knowledge through the real writer."; "Read the report, never the exit status" repointed to skills/l-01-agent-lifecycles/roles/curator.md:70-70; skills/l-01-agent-lifecycles/roles/curator.md:76-76. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "knowledge hand-off result"; "published dataset identity" repointed to skills/l-01-agent-lifecycles/roles/curator.md:149-149; skills/l-01-agent-lifecycles/roles/curator.md:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **route body updated — two of the ten role files moved.** The new section records `roles/curator.md`'s either-way admission and its choice of the taskless writer for a taskless run, `roles/bootstrap.md`'s statement of the admission in the product's own words, and that both were propagated into all ten copies by the generator. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T12:32:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **route body updated for the repository-foundation entry in both role files.** `roles/curator.md` gained the entry paragraph and process block; `roles/bootstrap.md` gained step 5 (reach the foundation, report the state, hand the authoring on) with its output line and its prohibition on authoring knowledge records. The section states the seat gate both files now carry in the product's own vocabulary — a session opened for the curator with no task document is refused `400 task-binding-required`, so the pre-task step belongs to the taskless bootstrap seat — because the round-one adversarial verdict was `blocking` on the earlier claim that such a session was admitted. **Citation accounting:** the rows this document already carried into `roles/curator.md` were re-read against this candidate and their drifted ranges re-anchored to the lines that now carry each construct; no claim and no row was dropped. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **route body updated for the curator role's new numbered
  step.** The role declares the readable order — Inputs, Process, Outputs — with no operator-knob block,
  and this leaf added the family/coverage step and renumbered the following ones without changing that
  shape. The section records the two keys the curator now authors, that an entry carrying neither is
  reported as unexamined rather than family-free, and that a plane whose state is not `recorded`
  measured nothing. **Citation accounting:** the `citation_claim_reopened` rows the product reported for
  this route's carriers were re-read against the current constructs and disposed of by hand, and the
  `citation_anchor_absent_from_range` rows were re-anchored to the lines that carry them rather than
  shifted by a remembered delta. No verification stamp was advanced: the candidate is uncommitted and
  the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **route body updated for the one role file this leaf moved.** `roles/curator.md` is 144 lines and gained a fourth numbered step in `## Process` (the real knowledge-authoring invocation and what to consume from its report), a permitted-action line naming the subcommand, a prohibition against writing the dataset from this seat, and a report sentence carrying the read-back identity — all **inside** the function shape this route standardized at `260915-CAPS-L22`, with no `**Inherits:**` line, knob block or sibling reference touched. The section also states the two rules the change makes load-bearing (a per-entry refusal is a result, and the mounted `knowledge_change` tool is not a write route). **Citation accounting:** the rows this document already carried into `roles/curator.md` were re-derived rather than shifted — `curator_coherence` `:42-59` → `:46-77`, and the curator row's `:56-56` → `:74-74` — because the file grew five net lines in the workflow's third step and one line in each of two later lists. No claim and no row was dropped, and no verification stamp was advanced — the governed closeout owns it.
- 2026-09-20T01:06+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 1 enforced citation row this card carried (citation_anchor_absent_from_range). The curator row's third citation, `skills/l-01-agent-lifecycles/roles/curator.md:42-52`, stopped short of the fourth numbered duty: `curator_coherence` — the structured authority publication the claim names — is written at 56, so the range was widened to `:42-59`, the four duties the claim summarises. The row's heading and quoted anchors were re-read against their cited ranges and stand, and both other citations are untouched. No claim wording, anchor or other range was changed, and no verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `overview.md:171` (curator_coherence) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-18T13:27+02:00 — 260915-KS-L13 curator (range-closure pass): **the last seven dead-anchor rows in this document were re-cited to the lines that now carry their facts.** `# Lifecycle — Curator` / `# Lifecycle — Manager` / `# Lifecycle — Worker` were the *retired* file titles: the rewritten role files title themselves `# Curator`, `# Manager`, `# Worker`, so the dead title was replaced by each file's live opening duty sentence (`You run one leaf's coherence pass and you write onboarding.`, `You drive exactly one master's leaf sequence from dispatch to handover.`, `You build one leaf.`) and, for the worker row, the `The turn report` bullet the claim names. `### 4 — Repair Affected Onboarding, Then Publish` and the curator row's `run the complete curation operation …` now read the live `## Process` item 3 plus the `curator_coherence` gate, whose extent was widened from `42-46` to `42-52` so the authority tool the claim names is inside it. `### 4 — Per-Requirement Acceptance Envelope And Delivery Attempt` and `## Per-Requirement Independent Attempt Adjudication` were the *rewritten* role files' old section headings; the live carriers are the worker template sentence `the one Requirement Acceptance Envelope for your owned primary` and the reviewer's `Adjudicate every requirement revision separately` / `An aggregate verdict or a sampled subset is invalid`, so the dead headings were replaced by those quotes. `nothing serializes its masters` was re-sourced to the migration note that carries it verbatim (`docs/reference/execution-topology-migration.md:63`) and the `.agents/` generated copy was replaced by the root `skills/l-01-agent-lifecycles/criteria/plan-review.md:64-67` catalog, whose own wording (`nothing serializes the masters`) the row's sibling anchor already quotes — the stale `architect.md:143-143` extent was re-pointed to the architect's live plan-review binding at `architect.md:28-28`. No claim was deleted or softened and no anchor set was dropped. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T13:20+02:00 — 260915-KS-L13 curator (post-merge pass): **stale citations repaired in this document after the master's sync onto its moved super line.** The role rows whose anchors no longer exist anywhere in the indexed corpus were re-worded to the headings and sentences the rewritten role files now carry, and their cited ranges were widened with the carrying per-site source where the construct had moved. Rows whose anchors name text that exists nowhere in the tree are named in `notes/reports/260915-KS-L13-named-residue.md` rather than re-pointed at an adjacent site.

- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **the route now describes its own files correctly.** This overview still presented the 260915-CAPS-L1 section shape as current — the numbered `## 1 — Purpose And Authority` … `## 6 — Completion And Handoff` sections, the `## Knobs, Tool Surface, And Dispatch Authority` block, and an `**Inherits:**` declaration line. leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling) rewrote all **ten** role files on this route into the **function shape** — `# <Role>`, `## Inputs`, `## Process`, `## Outputs`, `## What you may do`, `## What you must not do`, and a closing `## Stop and …` section, with a per-role extra only where the role has one — so none of those constructs exists any more and a citation naming one is stale. Purpose now carries the current shape beside the retained L1 record, the ten files are measured at **1,578** lines, and the corpus test that enforced the old order and knob block is recorded as no longer existing under its old name (`mcp/tests/test_role_instruction_corpus.py` keeps `ROLE_ORDER` and `SANCTIONED_SIBLING_REFERENCES`). Body rows in the Repo-Internal References table were re-pointed to constructs that exist in the rewritten files. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits. **Correction (`D51`, made in the same pass):** this entry first attributed the rewrite to `CAPS-R24@v1`. No such requirement revision exists — the master declares `CAPS-R01@v1` … `CAPS-R19@v1` — and the rewrite is leaf `260915-CAPS-L22`'s, under the developer's 2026-09-17 ruling. This curator fabricated the id; it is corrected here and in the body above.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "## The Role Registry" repointed to skills/l-01-agent-lifecycles/SKILL.md:67-67. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.

- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **the route's line-count restructure is labelled as structure, not as a measured saving.** Added the measured qualification to Purpose: the `2,792 → 2,322` lines moved shared rules and procedures into `core/` and `operations/` rather than removing them, the one measurement that exists reports the assembled capsule **larger** than the legacy startup chain at the worker elevation (**11,828** vs **5,928**, **+5,900**; like-for-like 11,645, +5,717), manager and architect are **UNMEASURED** (`binding-unresolved`), preservation is intact at **36/36** across ten declared roles plus launcher routing, and **adoption acceptance FAILED** with disposition **REVISE**. Also **corrected a landed defect (`D35`)** in the CAPS-L18 section: `ready-for-closeout` is never a value of the combined `checklistStatus`; the repair loop's gate is the **raw** `qualityChecklistStatus`, the combined field then reports `coherence-required`, and `closeoutReady` follows validation (`application/memory_quality/controller.py:664,671,678,687`). No verification stamp or fingerprint advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: the complete-curation doctrine reaches this route. The canonical sources on this route now state that the full `memory_quality_check` operation is part of every leaf's curation, that a subset never stands in for it, and that closeout and integration carry the completed result as a prerequisite while invoking nothing. Body updated as above; no verification stamp advanced because the sources are uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "nothing serializes the masters"; "nothing serializes its masters" repointed to skills/l-01-agent-lifecycles/roles/architect.md:143-143; skills/l-01-agent-lifecycles/roles/orchestrator.md:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **route body updated** for the corpus consolidation. Purpose now names the route's actual shape (nine files in one readable order with `**Inherits:**` lines, a new sibling `core/`, procedures moved to `operations/`, sanctioned sibling references only, 2,792 → 2,322 lines), and the Ungoverned Mirror Status section records this pass's explicit decision to update the route overview while deliberately leaving the per-role cards under `onboarding/skills/l-01-agent-lifecycles/roles/**` unrefreshed (outside `pathRules.include`, already declared stale, and a partial refresh would duplicate the governed `mcp/**` cards without resolving the govern-or-remove question). No verification stamp or fingerprint was advanced.


- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Aligned role/template handoff doctrine with two outputs and non-authoritative cache status. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T15:01:46+02:00 — Gate-required ungoverned-mirror curation: rewrote the frozen role
  boundary to the shipped per-contract activation (selecting a master publishes `reconciling` for
  that contract only, which suspends nothing and excludes no other master; `active` requires its own
  two protected source tips) and added the explicit developer ruling that nothing serializes a
  graph-less sprint, with `atomic-sequential` describing sprint SHAPE rather than a serialization
  mechanism. Added the graph-less ruling citation row against
  roles/architect.md:143-143 and roles/orchestrator.md:265-265, both `grep -n`-verified. Re-checked
  the remaining role rows against the frozen role files and they still hold (curator.md:1-6/153-195,
  manager.md:1-47, worker.md:1-33, SKILL.md:119-119, worker.md:77-145, reviewer.md:101-160). Added the
  Ungoverned Mirror Status defect statement. Verification metadata remains closeout-owned.
- 2026-09-10T09:58+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the curator reference row against the rewritten `skills/l-01-agent-lifecycles/roles/curator.md` — section 4 is now `### 4 — Repair Affected Onboarding, Then Publish`, so the row carries the current heading and its 153-195 extent. Verification metadata remains closeout-owned.

- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-10T00:46+02:00 — CCR-L42 route reconciliation: recorded the current review-phase,
  review-altitude, and worker-check obligations from the canonical role files. Source inspection
  only; verification metadata remains closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: added the four reviewer
  contexts and plane-stamped parent ownership to the role map. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the complete role caller-context matrix,
  separated one-call architect bootstrap from explicit ambient takeover, corrected manager-only
  leaf-seat dispatch, and kept structural rows outside settings overrides. Verification remains
  closeout-owned.

- 2026-08-29T09:14+02:00 — MCAR-L02 made lifecycle-published structured coherence authority,
  rather than hand-authored Markdown, the curator's terminal artifact. Verification remains
  closeout-owned.

- 2026-08-27T22:15+02:00 — Recorded worker, manager, and reviewer ownership of phase-sensitive
  malformed-attempt recovery without worker self-rejection.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2 role impact: separated internal protocol events from
  review-handoff attempts and made leaf records lightweight content-addressed views.
- 2026-08-27T19:59+02:00 — M40-M45 role impact: recorded worker/reviewer/manager attempt ownership
  and the accepted-attempt non-reopening boundary.
- 2026-08-27T12:43+02:00 — M38: recorded exact stable-ID dispatch, the worker acceptance envelope,
  independent per-ID reviewer adjudication, and separation from durable-evidence promotion.
  Verification metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-26T08:55+02:00 — Finalized the IAS role boundary label against the frozen pass-13
  candidate.

- 2026-08-24T14:19+02:00 — No route impact: aligned curator quality invocation and capacity guidance with the canonical controller. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: reviewer.md independence + evidence-type section; orchestrator.md independence paragraph. Verified at code commit de3a0fd9.


- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: orchestrator/strategist/architect role
  docs updated to the atomic attach flow and seats structure. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `architect.md` and `orchestrator.md` now
  name `task_doc.author_execution_graph` as the graph bootstrap/edit seam and teach the
  atomic-sequential default for graph-less sprints; the `migrate_execution_topology` reference is
  gone. Role lifecycles are unchanged. Verification remains closeout-owned.

- 2026-08-18T09:25+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: reconciled initial-plan ownership, strategist and
  orchestrator judgment boundaries, organizational/atomic manager duties, pre-landing completion
  scope, and leaf-owned remediation. Verification remains closeout-owned.
- 2026-08-14T11:29+02:00 — R39 curator: reconciled the role route with repository-resolved
  acceptance doctrine. Verification remains closeout-owned.
- 2026-08-14T06:25+02:00 — L23 final candidate review: manager, reviewer, curator, and orchestrator
  roles preserve one candidate-bound route-review handoff, current-lineage admission, and Dagger-only
  acceptance without model-carried operation or commit ids. Verification remains closeout-owned.
- 2026-08-13T14:32+02:00 — L23 final roles-route review: synchronized Dagger-only acceptance,
  targeted/full altitude, mandatory explicit diff base, and diagnostic-only host execution.
  Verification remains closeout-owned.
- 2026-08-13T09:05+02:00 — L23 curator body review: clarified that the manager's immediately
  pre-curator `worktree_status.sourceLineage=current` proof is carried into the brief and repeated
  by dispatch before host creation, while closeout/integration independently close later races.
  Final provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: recorded the manager-owned pre-curator current-lineage check and the structural dispatch recheck before curator host creation. Verification metadata remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented architect/manager lineage recovery and dispatch boundaries; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 route impact: manager,
  orchestrator, and worker quality-altitude doctrine now uses host-managed
  master memory by default and keeps leaf checks targeted. Verification
  metadata remains pinned until closeout stamps L24.

- 2026-08-11T14:40+02:00 — Made the curator's missing-onboarding and full-quality repair-and-rerun
  obligation part of the role route's current contract, with commit-derived stamps left to closeout.
- 2026-08-11T14:10+02:00 — Replaced task-delta sections with direct current role ownership,
  altitude, artifact, and separation contracts.
- 2026-08-10T07:30+02:00 — Durable reports became the cleanup precondition for short-lived seats.
- 2026-08-09T12:08+02:00 — Role-local watcher/ladder prose was superseded by fact relay.
- 2026-07-12T14:20+02:00 — Established the governing role-route overview.
