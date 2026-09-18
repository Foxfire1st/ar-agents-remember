# skills/l-01-agent-lifecycles/roles/manager.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/roles/manager.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:45+02:00|
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00 |
| governingOverview | `skills/l-01-agent-lifecycles/roles/overview.md` |

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
brief; the manager never requests or stores an occupant id. The manager gathers builder code/report
and reviewer verdict, then calls `worktree_status` for the canonical leaf and requires the complete
task-derived `sourceLineage` projection to be current immediately before curator dispatch. It
carries that projection in the curator brief; dispatch re-proves it before host creation. Only then
does it gather the curator coherence report before closeout. It consumes the worker's targeted-check
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One manager owns one canonical master and the complete leaf closeout chain. | "## What This Seat Is"; "**You drive exactly one master's leaf sequence from dispatch to handover.**" | skills/l-01-agent-lifecycles/roles/manager.md:8-12; skills/l-01-agent-lifecycles/roles/manager.md:11-30 |
| Hosted child dispatch uses leaf document, role, and complete brief without retained occupant ids. | "## Hosted Role Dispatch"; "Dispatch is one structural transaction." | skills/l-01-agent-lifecycles/roles/manager.md:41-46; skills/l-01-agent-lifecycles/roles/manager.md:48-48 |
| The leaf loop sequences builder, reviewer, exact-packet/adjudication curator intake, closeout, integration, and cleanup duties. | "### 2 — Leaf dispatch loop (per leaf)"; "The per-leaf loop" | skills/l-01-agent-lifecycles/roles/manager.md:55-143; skills/l-01-agent-lifecycles/roles/manager.md:94-272 |
| Master exit and handover use durable verdict/packet evidence and structural ownership. | "### 3 — Optional Master-exit Review"; "### 4 — Handover to the orchestrator"; "The master-handover packet" | skills/l-01-agent-lifecycles/roles/manager.md:146-152; skills/l-01-agent-lifecycles/roles/manager.md:330-341; skills/l-01-agent-lifecycles/roles/manager.md:342-352 |
| Structural parent/child messages are the role's communication path. | "## Comms Protocol"; "**Messages:**" | skills/l-01-agent-lifecycles/roles/manager.md:171-172; skills/l-01-agent-lifecycles/roles/manager.md:367-367 |
| Manager dispatch compiles and preserves the exact per-ID acceptance set through reviewer and curator handoffs. | "### 2 — Leaf dispatch loop (per leaf)"; "Per leaf before dispatch:" | skills/l-01-agent-lifecycles/roles/manager.md:24-29; skills/l-01-agent-lifecycles/roles/manager.md:108-108 |

## L23 Manager And Leaf Admission

The manager seat is created only after current master ancestry is proved, and
each worker/reviewer/curator dispatch re-proves the complete parent chain.
Recovery is contract-addressed and replacement-safe; no agent supplies branch
commit or session identity.

Pre-curator admission is manager-owned and ordered after builder/reviewer evidence but before any
onboarding work. If super or master moved, the manager synchronizes and reconciles the code first;
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

## Update History
- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **the role file this card cites was rewritten into the function shape, and the card was re-derived against it.** leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling) replaced the numbered sections and the `## Knobs, Tool Surface, And Dispatch Authority` block with `## Inputs`, `## Process`, `## Outputs`, `## What you may do`, `## What you must not do` and a closing `## Stop and …` section, so every Repo-Internal References row here that named an old heading or an out-of-range extent was re-pointed by reading the rewritten file: each anchor below is text that exists in the cited range, and each range is in bounds of the file as it stands. Where a claim described a construct the rewrite removed, the claim itself was re-worded to what the file now says. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits. **Correction (`D51`, made in the same pass):** this entry first attributed the rewrite to `CAPS-R24@v1`. No such requirement revision exists — the master declares `CAPS-R01@v1` … `CAPS-R19@v1` — and the rewrite is leaf `260915-CAPS-L22`'s, under the developer's 2026-09-17 ruling. This curator fabricated the id; it is corrected here and in the body above.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "## Comms Protocol" repointed to skills/l-01-agent-lifecycles/roles/manager.md:367-367. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "## Comms Protocol" repointed to skills/l-01-agent-lifecycles/roles/manager.md:359-359. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "## Hosted Role Dispatch" repointed to skills/l-01-agent-lifecycles/roles/manager.md:48-48. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "## Comms Protocol" repointed to skills/l-01-agent-lifecycles/roles/manager.md:406-406. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "### 2 — Leaf dispatch loop (per leaf)" repointed to skills/l-01-agent-lifecycles/roles/manager.md:108-108. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T12:00+02:00 — A005 normalized hosted-dispatch wording to the exact canonical leaf or
  master task document vocabulary consumed by the structural tool and synchronized projections.
  Verification remains closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded manager
  ownership of both leaf and master-exit reviewer generations, including exact task altitude and
  parent stamping. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded manager as a plane-hosted caller and
  explicit ambient-takeover target, with only manager-owned leaf-seat dispatch and no
  settings-owned structural authority. Verification remains closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled manager-role source ranges against the committed PDLS
  candidate after final requirement-ownership edits; behavior is unchanged.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: managers no longer count dispatch or internal reruns as
  attempts; they validate lightweight content-addressed handoff records and summaries that exclude
  protocol events.
- 2026-08-27T19:59+02:00 — M42 clarification: prevented unrelated later candidate movement from
  becoming a third implicit accepted-attempt invalidation trigger.
- 2026-08-27T18:06+02:00 — M40-M45: documented manager-owned attempt dispatch/validation,
  independent regression proof plus bounded invalidation, and the rebuildable non-gating master
  summary over authoritative leaf journals.
- 2026-08-27T16:27+02:00 — Closed the curator projection gap: the manager now feeds exact approved
  packets and per-revision adjudication through the curator brief and prohibits rejected/blocked
  deltas from becoming current intent. Verification remains closeout-owned.

- 2026-08-27T14:04+02:00 — Tightened M39 dispatch admission around approved version-addressed
  packets and packet-local durable corpus rulings; unapproved or mismatched revisions refuse.
- 2026-08-27T13:32+02:00 — M39@v1: manager dispatch and review comparison now bind exact stable
  ID + version rows to matching canonical packets. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: documented manager-owned exact requirement-set compilation,
  worker envelope validation, same-set reviewer dispatch, and separate evidence promotion.
  Verification metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: documented manager-local readiness reporting,
  nature-aware leaf lineage, and exact pre-landing organizational completion scope. Verification
  remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled canonical manager guidance with generic
  repository-resolved policy. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence: clarified leaf-closeout-only targeted acceptance,
  leaf-integration proof reuse, and the single full master-integration owner.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: made current `worktree_status.sourceLineage` an explicit input to curator dispatch and recorded the plane's second proof before host creation. Verification metadata remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented canonical manager/leaf lineage admission; verification remains closeout-owned.

- 2026-08-11T14:20+02:00 — Rewrote the default body around real-master ownership, structural child
  dispatch, and the builder/reviewer/curator closeout chain; removed duplicate history and task deltas.
- 2026-08-10T07:30+02:00 — Durable reports became the precondition for subordinate cleanup.
- 2026-08-08T02:00+02:00 — Leaf and master quality checks were assigned to their proper altitudes.
- 2026-07-12T14:20+02:00 — Established the self-contained one-master manager lifecycle.
