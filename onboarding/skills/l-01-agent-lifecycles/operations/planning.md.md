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


## Evidence

- Before a new leaf starts, the Architect asks once for go or review first, discloses the planned comparison and first-Explain workspace, and records the choice; intent-review-open holds until go. [6]

- One master takes one Manager, two or more take one Orchestrator; direct coordination is the developer-chosen exception. [1]
- Each independently falsifiable obligation gets a stable ID, version and canonical packet before topology. [2]
- A packet-named recorded invariant/family effect is declared by the Architect before implementation; no named effect means no declaration. [3]

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

- The authored source owns this contract; the distribution copy is not a separate authority. [4]

- Marks all common text all-role and limits the preimplementation expectedKnowledgeEffects declaration to Architect, restoring all-role afterward. [5]
