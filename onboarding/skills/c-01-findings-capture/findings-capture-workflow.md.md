# skills/c-01-findings-capture/findings-capture-workflow.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The authored companion expands findings capture into a verification-first procedure, from establishing context to returning a durable-capture summary. It distinguishes a confirmed finding from discussion and makes factual onboarding propagation a separate guarded decision.

## Commentary

### Inputs and capture sequence

The caller supplies the finding, task status, affected surfaces, known evidence and current phase. The procedure establishes context, verifies the finding, chooses its owner, writes a task-local owner first when present, considers onboarding only after the guardrail, and returns the result. A missing or ambiguous fact calls for targeted clarification rather than invented capture.

### Qualification is not promotion approval

Developer-confirmed clarifications, code/doc corrections, established invariants or migration boundaries, and explanatory current-state truth can qualify for capture. An option, debate, proposal or unresolved ambiguity does not. Even a qualified finding does not silently rewrite approved requirements.md or architecture.md: scope and structure changes enter their own intake surfaces and normal approval flow.

### Destination and missing-owner handling

The workflow adds a shared overview or phase summary for genuinely cross-file truth. If an expected owner is missing, the nearest open intake artifact is used rather than inventing retired documentation layers. Standalone findings use onboarding only for factual current-state clarification; otherwise the caller must supply a task or destination. The source does not authorize a findings ledger as the primary store.

### Onboarding guardrail and completion

All five guardrail conditions matter: factual current-state truth, code/supporting verification, durability beyond the task, explanatory rather than planning ownership, and exclusion of future decisions, open questions and task-only notes. Capture preserves evidence, remains local, and updates shared overviews only for cross-file truth. The summary names the finding, destination, evidence, onboarding outcome and follow-up. Completion requires the correct owner, guarded onboarding and no confirmed finding left only in chat where a durable destination exists.

### Paired contract and custody

The old short card correctly tied this workflow to the entrypoint and the distinction between facts and notes/questions/design intent. That useful commentary remains below. No old JSON companion exists for this workflow; its absence is recorded rather than filled with fabricated reference metadata.

### Scoped inherited commentary and evidence

The following inherited account is retained for commentary, migration history, todos and evidence meaning. It is not wholesale re-certified. Its uses of “current”, “now”, dates, milestones, tool names, command examples, topology descriptions, implementation claims or verification stamps describe that inherited account only. The source-grounded account above and evidence table below own newly authored claims. Historical reference numbers are not converted reference identities: original reference identities remain historical, not freshly allocated identities for the current evidence. This retained body creates no role, task, permission, live-build or execution authority.

> **Inherited heading: findings-capture-workflow.md**
>
> **Inherited heading: Purpose**
>
> This workflow document gives the detailed `c-01-findings-capture` skill procedure for turning confirmed findings into durable records.
>
> **Inherited heading: Notes**
>
> Keep this paired with the `c-01-findings-capture` skill entrypoint; changes here affect how agents distinguish confirmed facts from notes, questions, or design intent.

## Evidence

The following references support the source-contract commentary, not fresh runtime acceptance. Canonical authored source owns the contract; the inspected package copy is an equal distribution twin only. Root overview ownership context is onboarding/overview.md, especially its construction/ownership and retained naming-versus-reading doctrine. The description of a source contract is not runtime acceptance or permission to execute its operations.

- Workflow purpose and goal [1]
- Caller inputs and durable capture order [2]
- Context and verification before writing [3]
- Durable qualification and unresolved discussion exclusion [4]
- Owners, approvals, missing artifacts and standalone routing [5]
- Five-part onboarding guardrail [6]
- Local changes, evidence and caller summary [7]
- Prohibitions and completion criteria [8]
