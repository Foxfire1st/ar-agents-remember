# skills/l-01-agent-lifecycles/operations/planning.md

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

Shapes a bounded plan from the developer's outcome and current knowledge: one stable requirement ID and version with one canonical packet per independently falsifiable obligation, one primary requirement per executable leaf, developer approval before task topology, and the Architect's delegation defaults.

## Code Commentary

For one master the Architect's first delegation is one Manager on that canonical master; for two or more masters worked at the same time it is one Orchestrator on the canonical sprint, which starts one Manager per master. Direct Architect coordination is only the developer-chosen exception. The plan names deliverables, roots, dependencies, evidence class, requested review, curation needs and publication authority; contradictions, scope expansion and high-impact open decisions go to the developer first.

Before implementation, when a leaf's packet names an effect on a recorded invariant or family, the Architect declares that effect in `expectedKnowledgeEffects` through `task_doc` on `agents-remember-task`. A packet naming no such effect requires no declaration.

After a new leaf task document exists, the Architect asks the developer once, before any start: "go, or review first?" The Architect discloses that review uses a planned comparison without a task workspace, and first Explain creates the explainer workspace. It records `review-first` or `go` (`agreedRevision`) in `intentReview` through `task_doc`; `intent-review-open` holds until `go`.

## Current composition and authoring contract

The shared planning contract still requires bounded approved canonical packets, one primary requirement per executable leaf, preserved prior approvals and explicit owner/delegation/evidence/publication scope. Developer authority remains required for changed promises.

The `expectedKnowledgeEffects` declaration is selected only for Architect: when a leaf packet names a recorded invariant/family effect, Architect records it before implementation; no named effect means no declaration. This audience change removes an Architect-only instruction from Designer/Strategist/Orchestrator capsules without changing its actor or weakening the common planning and permission boundaries.


Before release, a reader other than the drafter compares a new or revised packet in both directions against every open leaf packet of its master, before the intent-review choice and again before go after review changes. Changed promises go to the developer; stale facts are fixed through registered revisions, and an issue stays in its original leaf unless another charter already covers it. Before any seat starts, Prepared context names record IDs/state, code/files/lines, unattributed callers and traps, including complete paged knowledge and the code it leaves unattributed.

A packet adding a row, disposition, writer field or gate states how its own curation completes on the installed build; new behavior is proven on fixtures and scratch copies. Reported complete checks name included and excluded work, and pre-existing failures need same-cause base evidence. Under developer-chosen direct coordination, the Reviewer receives its exact bound intake first; plan/super-exit reviews have no startable seat and go through the Architect.

The Architect reports an hour-long small item or a second repair round/freeze that day with a proposal to bound it. A UI fix is called working only after observation on the developer installation; otherwise it is landed and not verified there. At a handover or held/full-store result, the named message-handover detail owns sender and receipt handling.

## Evidence
Retained authoring-row wording:

Finding: Before a new leaf starts, the Architect asks once for go or review first, discloses the planned comparison and first-Explain workspace, and records the choice; intent-review-open holds until go.

Anchor:

Source: skills/l-01-agent-lifecycles/operations/planning.md:28-31

- One master takes one Manager, two or more take one Orchestrator; direct coordination is the developer-chosen exception. [1]
Retained authoring-row wording:

Finding: Each independently falsifiable obligation gets a stable ID, version and canonical packet before topology.

Anchor:

Source: skills/l-01-agent-lifecycles/operations/planning.md:4-4

Retained authoring-row wording:

Finding: Finding

Anchor: Anchor

Source: Source

Retained authoring-row wording:

Finding: ---

Anchor: ---

Source: ---

Retained authoring-row wording:

Finding: A packet-named recorded invariant/family effect is declared by the Architect before implementation; no named effect means no declaration.

Anchor:

Source: skills/l-01-agent-lifecycles/operations/planning.md:28-31

## Inherited Source-Epoch Commentary

The following account preserves the former distribution-copy card and its useful explanations, history and warnings. It is inherited scope, not a second current contract or a fresh certification of its dated/currentness, tool, provider, registry, execution or permission claims. The canonical account above retains its existing attribution and qualifications; the authored source below is the authority for the file. Historical reference labels in this quotation are provenance labels, not reference identities of this card.

> # operations/planning.md
>
> ## Governing Overview
>
> [MCP package overview](../../../../../../../overview.md)
>
> ## Purpose
>
> Turn the developer outcome and current relevant knowledge into approved, bounded requirements and an owner graph.
>
> ## Current Contract
>
> Give independently falsifiable obligations stable IDs/versions and canonical packets, cold-read new packets, and obtain developer approval before projecting task topology. Each executable leaf has one primary requirement; adjacent obligations are dependencies or preservation constraints. Preserve existing approvals.
>
> The Architect’s first delegation is one Manager on the master, or one Orchestrator on the sprint for concurrent masters with one Manager per master; direct coordination is only the developer’s exception. Name deliverables, paired/report roots, dependencies, evidence class, requested review, curation and publication authority.
>
> ## Conventions
>
> Canonical skills/l-01-agent-lifecycles/operations/planning.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.
>
> ## Invariants And Boundaries
>
> Tasks project approved scope and do not replace requirements. New scope, requirement contradiction or high-impact unresolved decisions return to the developer through the owner; unaffected versions stay valid. No fake task or agent identity is created for a taskless Projects role.
>
> ## Code Commentary
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Repo-Internal References
>
> | Finding | Anchor | References |
> | --- | --- | --- |
> | Canonical approved requirements, first delegation to one coordinating agent and ruled scope changes. | lines 3-7 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/planning.md:3-7 |
>
> ### Docs References
>
> No external or domain documentation governs this repository-local instruction file; it is canonical
> repository prose consumed by the skill router.
>
> No relevant documentation found after checking live sources.
>
> ### Repo-Internal References
>
> - The operation block's declared purpose, source path, and applicable roles. (historical reference 1)
> - The canonical source of this block. (historical reference 2)
>
> ### Cross-Repo References
>
> No sibling-repository contract defines this instruction file.
>
> No meaningful cross-repo references found.

Inherited reference 1 commentary (not a revalidated target):

> The operation block's declared purpose, source path, and applicable roles.
>
> Anchor: `planning`

Inherited reference 2 commentary (not a revalidated target):

> The canonical source of this block.
>
> Anchor: `# Operation`

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.


Retained authoring-row wording:

Finding: The authored source owns this contract; the distribution copy is not a separate authority.

Anchor:

Source: skills/l-01-agent-lifecycles/operations/planning.md


Past-epoch caption (retained wording): - Marks all common text all-role and limits the preimplementation expectedKnowledgeEffects declaration to Architect, restoring all-role afterward.

Original-target custody: `skills/l-01-agent-lifecycles/operations/planning.md`, blob `39174489f4ffee8369bf9973ae1be09ef15b5307`, declared “Use the developer's outcome and applicable current knowledge to shape a bounded plan. For new scope, assign a stable requirement ID/version and one canonical packet per independently falsifiable obligation; keep one primary requirement per ”. The earlier caption is detached from the live number; the current table carries only the current clause and target.

Retained authoring-row wording:

Finding: Planning marks the Architect-only alignment, Prepared-context, effect-declaration and intent-review work explicitly, with all-role planning scope and permission boundaries outside that audience slice.

Anchor:

Source: skills/l-01-agent-lifecycles/operations/planning.md:6-42

- Each independently falsifiable obligation gets a stable ID, version and canonical packet before topology. [2]
- A packet-named recorded invariant/family effect is declared by the Architect before implementation; no named effect means no declaration. [3]
- The authored source owns this contract; the distribution copy is not a separate authority. [4]
- Planning marks the Architect-only alignment, Prepared-context, effect-declaration and intent-review work explicitly, with all-role planning scope and permission boundaries outside that audience slice. [5]
- Before a new leaf starts, the Architect asks once for go or review first, discloses the planned comparison and first-Explain workspace, and records the choice; intent-review-open holds until go. [6]

- Before release, a reader other than the drafter compares a new or revised packet in both directions against every open leaf packet of its master, before the intent-review choice and again before go after review changes. Changed promises go to the developer; stale facts are fixed through registered revisions, and an issue stays in its original leaf unless another charter already covers it. Before any seat starts, Prepared context names record IDs/state, code/files/lines, unattributed callers and traps, including complete paged knowledge and the code it leaves unattributed. A packet adding a row, disposition, writer field or gate states how its own curation completes on the installed build; new behavior is proven on fixtures and scratch copies. Reported complete checks name included and excluded work, and pre-existing failures need same-cause base evidence. Under developer-chosen direct coordination, the Reviewer receives its exact bound intake first; plan/super-exit reviews have no startable seat and go through the Architect. The Architect reports an hour-long small item or a second repair round/freeze that day with a proposal to bound it. A UI fix is called working only after observation on the developer installation; otherwise it is landed and not verified there. At a handover or held/full-store result, the named message-handover detail owns sender and receipt handling. [7]
