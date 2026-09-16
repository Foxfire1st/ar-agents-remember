# skills/l-01-agent-lifecycles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/l-01-agent-lifecycles` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `e9300687218205ec1c4b0b86f96d3ac7c2f344d3`|
| lastVerifiedCommitDate | 2026-09-16T09:41:55+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |

## Purpose

This route owns canonical lifecycle doctrine: the session router, the shared `core/` blocks, the role
registry, the nine self-contained role lifecycles, the eight `operations/` procedure blocks, the
reference-only rationale and rulings, the composition manifest, dispatch briefs, durable reports, review
criteria, and authority templates. Generated package/harness trees mirror this route and never define
independent behavior.

260915-CAPS-L1 restructured this route: `SKILL.md` is now a **thin router with no doctrine** (620 → 179
lines), `core/` · `operations/` · `reference/` · `composition-manifest.json` are new, and all nine role
files were rewritten into one readable order (purpose/authority → required inputs → normal workflow →
permitted writes → stop/escalation → completion/handoff, then the knob block) with an `**Inherits:**`
line naming their shared sources. A role file now names a sibling role file only to wear that hat or
dispatch that seat.

## Hot Path Summary

Manager, orchestrator and curator handoffs name actual code/memory output refs and scoped onboarding evidence. They never require a ledger commit, cache freshness proof or cache-repair transaction; downstream consumers can rebuild the ledger from committed attribution.

## Detailed Route Context

### IAS Planning-To-Runtime Boundary

Planning truth is upstream of runtime scheduling. Architect, strategist, and orchestrator seats may
author otherwise-valid task changes without asking a closeout queue or atomic-series selector for
permission. A material task change invalidates the affected disposable projection and causes the
waiting frontier to be recomputed from current truth; it does not freeze task authoring.

Multiple live atomic masters on one protected source pair are normal. Implementation admission is
contract-scoped: each canonical series contract owns its own activation record, so selection
publishes `reconciling` for that exact contract — which suspends nothing and excludes no other
master — and the contract becomes `active` only when both of its own protected source tips are
current. One master's selection never pauses another, and multiple nonterminal contracts remain
valid. Role doctrine must treat retained sync conflicts as agent-resolvable, resumable, or
cancellable worktree state, never as a reason to rewrite planning around a stuck queue. Exact changed
doctrine files and synchronized copies are reconciled to the frozen candidate; commit verification
remains closeout-owned.

Nothing serializes a graph-less sprint. A sprint without an `executionGraph` declares no
dependencies, so the shipped `atomic-sequential` default describes the sprint's SHAPE — every
commanded master executes atomically — and is not a serialization mechanism: independent atomic
masters proceed concurrently and no master is held because another is selected. Only an explicit
`executionGraph` gates masters on real predecessors (`predecessor-incomplete:`).

Free chat launches ordinary role-shaped work by compiling `templates/architect-brief.md` from
current sprint truth and calling `dispatch_agent` exactly once on the sprint document. An explicit
developer-declared task-seat takeover instead targets the named role on its canonical task document. Missing plane identity
selects ambient target-document and architect-altitude validation. After handoff, the architect and
other spawning seats use the same public verb under plane identity and direct-child scope; a plane
refusal never becomes an ambient retry. Source-lineage conflicts remain resumable through the
contract-addressed sync continuation until a genuine semantic ambiguity requires escalation. The
internal session primitive and readiness/brief correlations remain control-plane details. The architect owns sprint composition and the initial ruled topology.
When the graph is missing or materially stale, an approved strategist authors the evidence-cited
plan before the orchestrator exists. The orchestrator adopts that plan, recomputes its ready
frontier after material events, and records every queue or reprioritization judgment with rationale,
evidence, author, confidence, and supersession. Structural task document plus role remains the
durable address at every altitude.

An organizational master is a logical grouping whose ordinary leaves branch directly from the
current super line and may land independently. An atomic master keeps its own integration branch
and exposes no partial result; each contract's own activation record controls that master's
implementation exposure, while a separate landing authority serializes conflicting protected-ref
movement. That ref-landing exclusion is not sprint scheduling: nothing serializes a graph-less
sprint's masters. Mechanisms publish facts and candidate sets; architect, strategist, orchestrator,
and manager seats retain their explicit judgment boundaries. Integration lines are not repair
workbenches.

Role continuity is task-document and artifact based. Workers build and report, reviewers provide
independent verdict evidence, curators reconcile system intent and memory, managers decide
delegated leaf gates and integrate a master, and orchestrators govern master handovers. Mechanical
fact relay replaces role-local polling and inference.

Reviewer is polymorphic without becoming ambiguous: it binds the exact leaf, master, or sprint
being reviewed, while the plane stamps the generation's parent document+role. Managers therefore
own leaf and master-exit review, the architect owns plan review, and the orchestrator owns super
review. An unstamped sprint reviewer cannot route because choosing between those two sprint planes
would be invented authority.

Requirement completion is an exact-set protocol. Before dispatch, the manager compiles the stable
IDs inherited from the master and owned by the leaf. The worker must write one acceptance envelope
per ID with delivery and verification rationales, independently inspectable citations, and exact
commands/results or durable evidence. The reviewer receives the same set, inspects the artifacts
itself, and accepts or rejects every ID separately; an invalid citation, wrong evidence class, or
missing developer ruling is a requirement rejection and prevents an overall pass. Non-code work
uses deliverable paths plus stable section anchors rather than invented code fields.

Requirement revisions, delivery attempts, and internal protocol events are separate. Semantic
revisions require explicit developer approval. Workers advance immutable exact-candidate attempts
only at review handoff or after reviewer rejection; internal implementation/test/evidence reruns
remain separate protocol events. Lightweight requirement-specific records link content-addressed
expanded evidence, reviewers append independent adjudications, and rejected work advances through
linked successors with one closed failure class. Accepted attempts remain closed across unrelated
later candidates; only direct-regression proof plus bounded owner invalidation or an approved
requirement revision can reopen them. Leaf journals remain authority while the master summary
excludes protocol events, is rebuildable, and never gates tasks, lifecycle, closeout, integration,
or queues.

The quality altitude ladder uses the pinned Dagger graph for Agents Remember acceptance. Leaf
closeout selects targeted mode exactly once; leaf integration and series closeout do not rerun it.
Master integration selects full mode exactly once. Both require the task-derived explicit diff
base. Host pytest/wrapper runs are refused; a hard cap remains an explicit constrained-lifecycle
setting rather than role-local judgment.

A curator completes only after the current-additions missing-onboarding check and full leaf-scoped
memory-quality worklist have been repaired and rerun. Dirty-source drift and future commit-derived
verification can be classified as closeout-owned only after no repairable citation, claim, shape,
history, entity, or index finding remains. The curator then publishes the sole structured,
candidate-bound coherence authority through the lifecycle API; generated Markdown is only its
human-readable projection.

Before that curator is created, the manager requires the leaf's task-derived source-lineage
projection to be current and includes it in the complete brief. The structural dispatch transaction
re-proves lineage before host creation, so a parent move between status and dispatch fails closed.

## Conventions

- Canonical role doctrine lives under `roles/`; templates feed complete role inputs.
- Shared rules live in `SKILL.md` and are not restated as competing role-local variants.
- Runtime package and harness copies are synchronized artifacts of the complete canonical tree.
- Current intent stays in default bodies; semantic history records transitions without leaf diaries.
- `dispatch_agent` is the sole public spawn verb; caller kind is derived from process context, never
  selected in the request.
- Role-table `dispatch` and `tools` rows are fixed authority/capability documentation rather than
  settings knobs.

## Invariants And Boundaries

- Runtime ids never become model-held work addresses.
- Spawn ancestry is provenance, not responsibility topology.
- Each role acts only at its assigned task altitude and authority boundary.
- Initial briefs are exact-pinned; ordinary messages re-resolve current structural occupants.
- Ambient bootstrap and plane-hosted child dispatch share one exact-brief transaction, while their
  authority checks remain disjoint and never fall back into one another.
- Curator completion requires zero curator-actionable findings from both required onboarding checks;
  the structured coherence authority is published only after their repair-and-rerun loop.
- Commit-derived memory verification follows the real code commit during governed closeout.
- Aggregate completion prose cannot replace the worker envelope or reviewer adjudication for any
  stable requirement ID.


## CCR-R12@v5 Lifecycle Boundary

Workers provide targeted checks and curators provide scoped onboarding checks with honest failed or not-run states. The prepared code and memory-content outputs move through the authorized Git transaction, whose commit legs suppress automatic quality and test hooks. The consumer ledger is refreshed without a commit while ordinary explicit Git hook policy outside the transaction remains unchanged; full quality, full tests, full memory quality, certification, and review require an explicit developer request. Requested reviews retain the sealed monotonic three-round rule.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared routing, authority, loop, and dispatch doctrine is canonical here. | "## Which Lifecycle Am I? (the router — exactly three conditions, in order)"; "## Delegated Series Authority"; "Caller kind comes only from process context"; "Every launcher or role that dispatches a hosted role calls" | skills/l-01-agent-lifecycles/SKILL.md:13-13; skills/l-01-agent-lifecycles/SKILL.md:422-422; skills/l-01-agent-lifecycles/SKILL.md:466-466; skills/l-01-agent-lifecycles/SKILL.md:473-473 |
| The graph-less atomic-sequential default describes sprint shape; nothing serializes a graph-less sprint. | "nothing serializes a graph-less"; "nothing serializes its masters" | skills/l-01-agent-lifecycles/templates/orchestration-task.md:172-172; skills/l-01-agent-lifecycles/roles/orchestrator.md:265-265 |
| The architect launcher packet is one canonical compiler contract, not fixture prose or a second brief. | "# Template — Architect Brief"; "This architect seat is now plane-hosted."; "Compiler notes for the launcher" | skills/l-01-agent-lifecycles/templates/architect-brief.md:1-84 |
| Curator owns conservative three-way memory reconciliation, the complete pre-closeout onboarding worklist, and structured authority publication. | "## What This Seat Is"; "### 4 — Repair Affected Onboarding, Then Publish" | skills/l-01-agent-lifecycles/roles/curator.md:7-49; skills/l-01-agent-lifecycles/roles/curator.md:153-195 |
| Manager owns one real master and its leaf closeout chain. | "## What This Seat Is" | skills/l-01-agent-lifecycles/roles/manager.md:10-30 |
| Worker owns one real leaf's implementation and durable report. | "## What This Seat Is" | skills/l-01-agent-lifecycles/roles/worker.md:7-17 |
| The shared frame defines the mandatory per-ID worker envelope and independent reviewer disposition. | "Requirement acceptance is per stable ID and version, never aggregate." | skills/l-01-agent-lifecycles/SKILL.md:295-295 |

Current working-candidate evidence for this route:

| Finding | Citations | Source Path |
| --- | --- | --- |
| Lifecycle publication and recovery carry the actual code/memory outputs. | L66-L72 | [mcp/src/agents_remember/models/lifecycles/operation.py](mcp/src/agents_remember/models/lifecycles/operation.py) |

## L23 Pre-Dispatch Lineage

Canonical lifecycle guidance now places task-derived ancestry before process
creation: managers require current master lineage and leaf roles require the
full chain. Refusal creates no child and recovery is contract-addressed, keeping
commit/session identity inside the control plane.

## R39 Repository-Resolved Quality Doctrine

The lifecycle skill is repository-generic: roles and briefs resolve executor, environment,
arguments, retry, resources, and evidence from the active repository memory. The cross-repository
cadence remains fixed at leaf closeout once and master integration once, with no leaf-integration
rerun and no inferred fallback.

## 260815-DAG-L14 Doctrine Route

The `l-01-agent-lifecycles` doctrine was synced to the atomic `attach_master` flow and the
first-class sprint seats structure: `roles/orchestrator.md`, `roles/strategist.md`,
`roles/architect.md`, `criteria/plan-review.md`, and `templates/orchestration-task.md` all
updated, with canonical and generated copies kept identical by `scripts/sync-skills.py`.

## 260815-DAG-L15 Review-Doctrine Repair

The review doctrine route was repaired: `roles/reviewer.md` gained the Review Independence and Evidence-Type Matching section (reviewer seat ≠ author seat; rendering → mounted-UI proof, scheduling → operation-level proof, data model → artifact-level proof, doctrine → code anchor); `roles/orchestrator.md` gained the independence paragraph; `criteria/plan-review.md` gained standing PR-8; `criteria/report-verification.md` extended RV-1 to `git diff --summary` mode rows; `criteria/doctrine.md` gained D-6 (bounded `L<leaf>-R<n>`/`S<n>` requirement ids allowed — reconciled with the memory canonical Source Comment Scope rule, folded at master level); `templates/verdict.md` gained rule 7 + the author-seat row; `templates/manager-brief.md` gained the independence/evidence line; `SKILL.md` extended the three-party-loop paragraph. All 9 generated copy trees stay byte-identical via `scripts/sync-skills.py`.

## 260815-DAG Master Full-Gate Repair Route Impact

The `templates/orchestration-task.md` heading was restored to `## Canonical executionGraph Adoption Payload` (the `executionGraph` qualifier phrase restored); all 9 generated copy trees re-synced byte-identically via `scripts/sync-skills.py`.

## 260821-DAGQC-L2 Curator Call Synchronization

No lifecycle topology or authority changed. The curator brief now demonstrates the canonical
discriminated memory-quality request so fresh seats do not reconstruct the retired flat grammar.

## Ungoverned Mirror Status (known defect)

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

**260915-CAPS-L1 decision, recorded rather than implied.** This leaf rewrote the canonical route (the
router became a thin router; `core/` · `operations/` · `reference/` · `composition-manifest.json` were
added; all nine role files were rewritten), so a contract-scoped quality pass reports this route's
unmodified bodies. The curator updated **this overview**, because route meaning genuinely changed and the
overview is the right home for it. It deliberately did **not** refresh the legacy role/criteria/template
sidecars under `onboarding/skills/l-01-agent-lifecycles/**`: they sit outside `pathRules.include`, they are
already declared knowingly stale by this section, and a partial hand-refresh would leave them
inconsistent with each other while duplicating the governed cards that do exist — the 18 new and 17
updated cards on the tracked generated copy under
`onboarding/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/**`. The follow-up
decision this section already asks for (govern or remove the mirror) also determines whether those cards
should be refreshed or deleted, so resolving it now by hand would prejudge it. No fingerprint or
verification stamp was advanced.

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **route body updated** for the corpus consolidation. Purpose now names the route's actual 260915-CAPS-L1 shape (thin router + `core/` + nine role files + eight `operations/` blocks + `reference/` + `composition-manifest.json`), and the Ungoverned Mirror Status section records this pass's explicit decision: the overview is updated because route meaning changed, while the legacy `onboarding/skills/l-01-agent-lifecycles/**` sidecars are deliberately left untouched because they are outside `pathRules.include`, already declared knowingly stale, and a partial hand-refresh would duplicate the governed cards on the tracked generated `mcp/**` copy without resolving the govern-or-remove question this section already raises. No verification stamp or fingerprint was advanced.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Aligned role/template handoff doctrine with two outputs and non-authoritative cache status. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-13T15:01:46+02:00 — Gate-required ungoverned-mirror curation: rewrote the planning/runtime
  boundary to the shipped per-contract activation (each canonical series contract owns its own
  activation record; `reconciling` suspends nothing and excludes no other master; multiple
  nonterminal contracts remain valid) and added the explicit developer ruling that nothing serializes
  a graph-less sprint — `atomic-sequential` describes sprint SHAPE, not a serialization mechanism.
  Repaired the rotated citation row after `grep -n` verification: `"## Delegated Series Authority"`
  → SKILL.md:422-422, `"Caller kind comes only from process context"` → SKILL.md:466-466, `"Every
  launcher or role that dispatches a hosted role calls"` → SKILL.md:473-473 (all three had been bound
  to each other's line), and added the graph-less ruling row citing
  templates/orchestration-task.md:172-172 and roles/orchestrator.md:265-265. Added the Ungoverned
  Mirror Status defect statement. Verification metadata remains closeout-owned.
- 2026-09-10T09:58+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the curator reference row against the rewritten `skills/l-01-agent-lifecycles/roles/curator.md` — section 4 is now `### 4 — Repair Affected Onboarding, Then Publish`, so the row carries the current heading and its 153-195 extent. Verification metadata remains closeout-owned.

- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "Requirement acceptance is per stable ID and version, never aggregate." repointed to skills/l-01-agent-lifecycles/SKILL.md:295-295. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded task-altitude
  reviewer binding, generation-bound parent stamping, and the fail-closed unstamped sprint seam.
  Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 adopted one public `dispatch_agent` verb, separated
  ordinary architect bootstrap from explicit takeover, clarified fixed role authority versus
  launch settings, and preserved resumable lineage-conflict recovery. Verification remains
  closeout-owned.

- 2026-08-29T09:14+02:00 — MCAR-L02 replaced the hand-authored coherence report with one
  lifecycle-published structured authority and a generated Markdown projection. Verification
  remains closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled lifecycle overview citations against the committed PDLS
  candidate; the architect/seat routing and acceptance boundaries are unchanged.

- 2026-08-27T22:15+02:00 — Clarified the route-wide attempt boundary: never-handed-off malformed
  rows are non-attempt corrections, while handed-off malformed records require reviewer rejection.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2 route correction: formal attempts now begin at review
  handoff, internal protocol events stay separate, and lightweight journal records link frozen
  expanded evidence without inflating the master summary.
- 2026-08-27T20:45+02:00 — Clarified that each leaf has one physical append-only attempt journal;
  worker and reviewer records share that authority while reports and verdicts link exact anchors.
- 2026-08-27T19:59+02:00 — M40-M45 route impact: recorded leaf-authoritative attempt journals,
  non-gating summaries, and the M42 distinction between stale in-flight candidates and unrelated
  post-acceptance movement.
- 2026-08-27T12:43+02:00 — M38: documented the exact stable-ID acceptance set, worker evidence
  envelope, independent reviewer adjudication, non-code citation form, and overall no-rejection
  rule. The durable-evidence promotion hold point remains separately mandatory. Verification
  metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-26T08:20+02:00 — Reconciled the planning/runtime source-pair boundary and synchronized
  doctrine set to the frozen candidate; verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — No route impact: aligned the curator brief's quality examples with the canonical sync/start/poll request. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: orchestration-task template heading restored to `## Canonical executionGraph Adoption Payload`; copies re-synced. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: review-doctrine repair — no-self-review + evidence-type matching (reviewer/orchestrator), PR-8, RV-1 extension, D-6 bounded requirement ids, verdict/manager-brief templates, SKILL.md three-party loop. Verified at code commit de3a0fd9.


- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: doctrine files updated to the
  `attach_master` flow and seats structure. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: the architect/orchestrator roles and the
  orchestration-task template now teach the atomic-sequential default — a graph-less sprint runs
  one master at a time, `task_doc.author_execution_graph` owns graph bootstrap and edits, and the
  `migrate_execution_topology` cutover reference is gone; lifecycle routing doctrine is unchanged.
  Verification remains closeout-owned.

- 2026-08-18T09:25+02:00 — No route impact: renamed the atomic 'barrier' concept to 'blocker' throughout; route purpose unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: documented architect-owned initial planning,
  evidence-cited judgment, ready-frontier recomputation, organizational versus atomic master
  topology, exact pre-landing organizational completion, and the no-workbench boundary.
  Verification remains closeout-owned.
- 2026-08-14T11:29+02:00 — R39 curator: removed Agents Remember-specific quality commands from
  generic lifecycle guidance while preserving exact cadence. Verification remains closeout-owned.
- 2026-08-14T06:25+02:00 — L23 final candidate review: lifecycle doctrine keeps Dagger as the sole
  acceptance graph and makes manager lineage plus exact candidate-bound route review mandatory
  before curator dispatch. Verification provenance remains closeout-owned.
- 2026-08-13T14:32+02:00 — L23 final route review: synchronized Dagger-only acceptance,
  targeted/full altitude, explicit diff-base ownership, and diagnostic-only host execution across
  canonical lifecycle doctrine. Verification remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: added the manager-owned pre-curator lineage gate, brief-carried projection, and pre-host dispatch recheck to canonical lifecycle doctrine. Verification metadata remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented canonical pre-dispatch lineage policy; verification remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 route impact: manager,
  orchestrator, worker, and their dispatch briefs now state that master full
  gates use host-managed RAM/swap by default. Verification metadata remains
  pinned until closeout stamps L24.

- 2026-08-11T14:40+02:00 — Made the required missing-onboarding and full leaf-quality
  repair-and-rerun loop part of current curator completion doctrine; real-commit fields remain
  closeout-owned only after the curator-actionable worklist is empty.
- 2026-08-11T14:10+02:00 — Replaced accumulated route-impact sections with the compact current
  lifecycle topology, authority, dispatch, and synchronization contract.
- 2026-08-10T07:30+02:00 — Completion cleanup kept durable reports/transcripts while reclaiming
  completed subordinate seats.
- 2026-08-09T12:08+02:00 — Fact-relay supervision superseded ladder and watcher doctrine.
- 2026-08-08T02:00+02:00 — Quality work was assigned to leaf closeout and master integration
  altitudes.
- 2026-07-12T14:20+02:00 — Established governing route coverage.
