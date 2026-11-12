# skills/l-01-agent-lifecycles/operations/planning.md

## Governing Overview

[overview](../overview.md)

## Purpose

Shapes a bounded plan from the developer's outcome and current knowledge: one stable requirement ID and version with one canonical packet per independently falsifiable obligation, one primary requirement per executable leaf, developer approval before task topology, and the Architect's delegation defaults.

## Code Commentary

For one master the Architect's first delegation is one Manager on that canonical master; for two or more masters worked at the same time it is one Orchestrator on the canonical sprint, which starts one Manager per master. Direct Architect coordination is only the developer-chosen exception. The plan names deliverables, roots, dependencies, evidence class, requested review, curation needs and publication authority; contradictions, scope expansion and high-impact open decisions go to the developer first.

Before implementation, when a leaf's packet names an effect on a recorded invariant or family, the Architect declares that effect in `expectedKnowledgeEffects` through `task_doc` on `agents-remember-task`. A packet naming no such effect requires no declaration.

After a new leaf task document exists, the Architect asks the developer once, before any start: "go, or review first?" The Architect discloses that review uses a planned comparison without a task workspace, and first Explain creates the explainer workspace. It records `review-first` or `go` (`agreedRevision`) in `intentReview` through `task_doc`; `intent-review-open` holds until `go`.

## Current composition and authoring contract

The shared planning contract requires bounded approved canonical packets, grouped or split by `reference/coordination/shared/requirement-design.md#plan-a-topic-merge-or-propose-a-split`, one primary requirement per executable leaf, preserved prior approvals and explicit owner/delegation/evidence/publication scope. Developer authority remains required for changed promises.

The `expectedKnowledgeEffects` declaration is selected only for Architect: when a leaf packet names a recorded invariant/family effect, Architect records it before implementation; no named effect means no declaration. The Orchestrator, the other planning role, does not receive it; the common planning and permission boundaries stay in the all-role text.

Before release, a reader other than the drafter compares a new or revised packet in both directions against every open leaf packet of its master, before the intent-review choice and again before go after review changes. Changed promises go to the developer; stale facts are fixed through registered revisions, and an issue stays in its original leaf unless another charter already covers it. Before any seat starts, Prepared context names record IDs/state, code/files/lines, unattributed callers and traps, including complete paged knowledge and the code it leaves unattributed.

A packet adding a row, disposition, writer field or gate states how its own curation completes on the installed build; new behavior is proven on fixtures and scratch copies. Reported checks name what ran and what was left out under the shared every-role rule, and pre-existing failures need same-cause base evidence. Under developer-chosen direct coordination, the Reviewer receives its exact bound intake first; plan/super-exit reviews have no startable seat and go through the Architect.

The Architect reports an hour-long small item or a second repair round/freeze that day with a proposal to bound it. A UI fix is called working only after observation on the developer installation; otherwise it is landed and not verified there. At a full-store refusal, the named message-handover section owns the pending handover, single retry and second-refusal report.

## Evidence

- One master takes one Manager, two or more take one Orchestrator; direct coordination is the developer-chosen exception. [1]

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- Each independently falsifiable obligation gets a stable ID, version and canonical packet before topology. [2]

- A packet-named recorded invariant/family effect is declared by the Architect before implementation; no named effect means no declaration. [3]

- The authored source owns this contract; the distribution copy is not a separate authority. [4]

- Planning marks the Architect-only alignment sweep, knowledge-effect declaration, intent-review and cold-read Prepared-context work explicitly, with all-role requirement, ownership, Prepared-context and plan-boundary text outside that audience slice. [5]

- Before a new leaf starts, the Architect asks once for go or review first, discloses the planned comparison and first-Explain workspace, and records the choice; intent-review-open holds until go. [6]

- Before release, a reader other than the drafter compares a new or revised packet in both directions against every open leaf packet of its master, before the intent-review choice and again before go after review changes. Changed promises go to the developer; stale facts are fixed through registered revisions, and an issue stays in its original leaf unless another charter already covers it. Before any seat starts, Prepared context names record IDs/state, code/files/lines, unattributed callers and traps, including complete paged knowledge and the code it leaves unattributed. A packet adding a row, disposition, writer field or gate states how its own curation completes on the installed build; new behavior is proven on fixtures and scratch copies. Reported checks name what ran and what was left out, and pre-existing failures need same-cause base evidence. Under developer-chosen direct coordination, the Reviewer receives its exact bound intake first; plan/super-exit reviews have no startable seat and go through the Architect. The Architect reports an hour-long small item or a second repair round/freeze that day with a proposal to bound it. A UI fix is called working only after observation on the developer installation; otherwise it is landed and not verified there. At a full-store refusal, the named message-handover section owns the pending handover, single retry and second-refusal report. [7]
