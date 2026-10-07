# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| sourceRoute | `skills/l-01-agent-lifecycles/roles` |

## The curator's converted-memory steps (260928-MIK-L37)

[`curator.md`](curator.md.md) gains two paragraphs for converted memory (L37 fix round P1b). Process step 2: the
curator follows the c-05 skill's converted-card workflow, in which a card's evidence is a citation table that
`citation_fix` turns into `- <finding> [n]` lines and sidecar references, and a changed file whose card needs no
change is answered by an `onboarding_trace` row. Process step 3: `agents-remember knowledge-ingest` is then the
file writer, writes files in the leaf's memory worktree and publishes no dataset. No other role file changed.

- The curator's converted-card step. [17]
- The curator's file-writer step. [18]


## The curator lifts the decisions that keep governing code (260928-MIK-L13)

[`curator.md`](curator.md.md), Process step 3, gains four lines for MIK-R13 rule 5: on converted memory, the
curator turns each developer ruling and requirement-packet choice that still constrains code into a decision record
with the alternatives it weighed, and leaves decisions that matter only within the task in the task. The step
points to the hand-off template's "Decision records (MIK-R13)" section for the fields and the rules. Lifting is
guidance; nothing enforces it mechanically, and the decision authority stays with the developer. No other role
changed; the package copy and the eight harness starter copies are synced by `sync-skills.py`.

- The lifting pointer in step 3. [1]

## The reviewer checks a leaf's declared knowledge effects (260928-MIK-L11)

[`reviewer.md`](reviewer.md.md), Process step 7 (where each requirement revision is adjudicated), gains one
line for MIK-R11 rule 2: when the leaf's task document declares `expectedKnowledgeEffects`, the reviewer checks
that declaration against the leaf's requirement packet — its declared subjects and effects match what the
packet requires, with no effect missing and none invented — and a mismatch is a finding. The architect ruled
the line in (Q3, 2026-09-29T21:56:18+02:00). It sits in the role file rather than a criteria catalog, because
the catalogs admit a standing criterion only with catching evidence. Who writes the declaration (the
architect, or the worker with the architect's approval) stays procedural. No other role changed; the package
copy and the eight harness starter copies are synced by `sync-skills.py`.

- The declaration check in step 7. [2]

## Curator successor-family examination

The curator role requires explicit stored membership IDs and authored bases when retaining unchanged siblings in a justified family successor. It preserves each existing invariant revision and checks the ordinary published roster. The role’s code, task-state and Git prohibitions remain unchanged.

- The curator process carries exact retained-sibling authoring and readback. [3]

## Curator authors a rationale for every realization target (260921-ICR-L45)

Process step 3 of the curator role now requires every hand-off target to carry its own authored
`rationale` (why that place carries the obligation, specific to the construct it names) and an optional
`role` before ingest; where the producer gave none, the curator writes it from the evidence. That is
supplying a missing explanation, not re-deriving a producer field. The writer never generates one and
refuses an unexplained target with `realization_rationale_absent`. The role's code, task-state and Git
prohibitions are unchanged.

- The curator's step-3 rationale duty. [4]

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

- **The authoring step this route's curator file now carries, with the invocation and the report fields to consume.** [5]
- The permitted-action line that makes the subcommand this seat's route. [6]
- The prohibition that keeps the dataset out of its hands. [26]
- The report sentence that carries the published identity into the handoff. [7]
- The operation block the same obligation landed in, which is the procedure this role file composes. [8]

## Purpose

This route owns one canonical file per role. The current native launcher exposes seven roles: Architect, System Specialist, Orchestrator, Manager, Worker, Reviewer and Curator. Other registry files remain in the corpus without becoming launchable through this path. Each delivered native capsule contains its selected role followed by one applicable operation, while canonical task/workspace facts arrive separately in the handover; the retained shared core is not injected.

Architect owns the developer’s semantic conversation and, for work inside one master, first hands coordination to one Manager on that master; when two or more masters are worked on at the same time one Orchestrator on the sprint starts one Manager per master. Direct coordination by the Architect and an Orchestrator above a single master are the developer’s explicit choices. Worker, Reviewer and Curator use the selected paired leaf scope. Architect and System Specialist may start manually without task references and ask only for missing scope; separate repository-foundation admissions keep their own contract.

Worker implements the approved leaf and leaves code uncommitted. Reviewer examines the complete requested candidate, exact requirement evidence and sealed findings independently. Curator preserves MIK’s converted writer, authored scope/rationale, exact families/siblings, full normal MQC/coherence and comparison evidence. Native host language changes no owner’s review, curation or paired-Git duty. Dated L1/L22 structure and L10 token measurements remain historical candidate facts, not descriptions or measurements of this current route.

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

- Canonical role files own doctrine; package/harness role files are exact synchronization outputs.
- Read selected canonical tasks/packets through supplied exact arguments and actual bound schemas; recover prior rulings and approvals across reconnects.
- Preserve actual agent IDs, report and handover paths. Native starts/messages use `agents-remember-task`; a manually dashboard-started role needs no parent.
- Keep distinct builder, independent reviewer, curator and semantic/publication owners. The Architect’s first delegation is one Manager for one master or one Orchestrator for concurrent masters, unless the developer chooses direct coordination.
- Use current source anchors for current claims; retain dated older structure and metrics as historical evidence rather than current section pointers.

## Invariants And Boundaries

- One leaf owns one approved primary requirement; inherited/adjacent requirements remain preservation constraints or dependencies.
- Task/workspace/recipient/parent identity is supplied or resolved by the owning AR boundary, never invented from Projects or a chat title.
- A rejected candidate returns finding-specific repair to the same Worker. Requested fix-verification preserves the sealed baseline and outstanding IDs.
- Normal Curator authoring remains complete: full contract-scoped MQC, exact blocked findings and required coherence. A report-only admission is bounded and never reported as that normal pass.
- No role absorbs another role’s write authority, creates duplicate uncertain work or treats turn status/tests as semantic acceptance or Git publication.
- Commit-derived memory attribution follows the real source commit through the governed closeout owner.
- Per-requirement worker/reviewer evidence is preserved; aggregate completion prose cannot replace it.


## CCR-R12@v5 Lifecycle Boundary

Workers provide targeted checks and curators provide scoped onboarding checks with honest failed or not-run states. The prepared code and memory-content outputs move through the authorized Git transaction, whose commit legs suppress automatic quality and test hooks. The consumer ledger is refreshed without a commit while ordinary explicit Git hook policy outside the transaction remains unchanged; full quality, full tests, full memory quality, certification, and review require an explicit developer request. Requested reviews retain the sealed monotonic three-round rule.

## Evidence

### Repo-Internal References

- The curator owns affected onboarding and admitted knowledge authoring, with full diagnostics and a structured handoff; source code, task and lifecycle writes stay outside the seat. [9]
- Manager is one master-scoped owner of the builder/reviewer/curator closeout chain. [10]
- Worker is one leaf-scoped builder whose terminal artifact is the turn report. [11]
- The shared registry enumerates every remaining role file. [12]
- Worker and reviewer roles define the two independent halves of per-ID acceptance. [13]
- The graph-less atomic-sequential default describes sprint shape; nothing serializes the masters. [14]
- The strategist lifecycle makes topology an explicit choice and refuses an unreasoned default. [15]

Current working-candidate evidence for this route:

- Lifecycle publication and recovery carry the actual code/memory outputs. [16]

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

## Current native instruction evidence

- Taskless subject and one coordinating agent under the Architect. [19]

- Master coordination under the Architect and exact paired scope. [20]

- Sprint coordination above one Manager per master and separate evidence. [21]

- Bound uncommitted Worker duty. [22]
- Independent exact assigned review and sealed findings. [23]
- Bound and preserved normal Curator duties. [24]
- Taskless real concern and report-first remediation. [25]

## Retained pre-import corpus account and measurements

The following text is retained verbatim from the pre-import source account. Its dated measurements, source counts and old composition vocabulary describe those recorded candidates; the current native contract is stated above.

### Former Purpose

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


### Former Conventions

- A role file is complete enough to start from its brief without transcript history.
- The source role files are canonical; packaged copies are exact synchronization outputs.
- Each role writes its artifact of record and communicates structurally one rung at a time.
- Shared dispatch/authority doctrine remains in the parent `SKILL.md`.
- Every role table names whether that role is an ambient target, a plane-hosted caller, or
  target-only; the request never carries a caller-mode selector.


### Former Invariants And Boundaries

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
