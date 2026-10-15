# skills/c-01-findings-capture/SKILL.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The authored findings-capture entrypoint decides where confirmed knowledge belongs when it emerges in discussion, execution, review or direct clarification. It keeps task intake separate from durable current-state onboarding and delegates the detailed procedure to the adjacent findings-capture workflow.

## Commentary

### Trigger and companion ownership

The source names two operating modes: a task workflow, including the lifecycle orchestrator build phase or a light-task/master-and-subtask series, and standalone clarification. These are descriptions of the skill contract, not authority to open a task or acquire a role. The named companion supplies procedure; the entrypoint supplies the destination and safety rules.

### Routing by responsibility

A requirement or intent change belongs in requirement_change_candidates.md; a structural uncertainty belongs in architecture_open_questions.md; phase-local truth belongs in the active phase artifact. A verified factual clarification that should outlive the task may reach onboarding through c-05. This routing prevents one finding from silently becoming approved requirements or architecture.

### Verification and propagation order

Developer confirmation is not a license to copy chat into onboarding: relevant code and onboarding must be checked, partial support or contradiction resolved, and remaining ambiguity exposed. When both destinations are affected, the task-local owner is updated first. Speculation, future-state decisions, open questions and task-only notes stay out of onboarding; broader discovery is conditional on direct checks being insufficient.

### Copy and maintenance boundary

This card describes skills/c-01-findings-capture/SKILL.md. Its inspected packaged twin is byte-identical and supplies no separate contract, role or permission. The historical verification-metadata todo and the successive build-job/build-phase vocabulary notes are retained below as scoped history, not claims that a commit, refresh or workflow run occurred.

### Scoped inherited commentary and evidence

The following inherited account is retained for commentary, migration history, todos and evidence meaning. It is not wholesale re-certified. Its uses of “current”, “now”, dates, milestones, tool names, command examples, topology descriptions, implementation claims or verification stamps describe that inherited account only. The source-grounded account above and evidence table below own newly authored claims. Historical reference numbers are not converted reference identities: original reference identities remain historical, not freshly allocated identities for the current evidence. This retained body creates no role, task, permission, live-build or execution authority.

> **Inherited heading: `c-01-findings-capture` skill findings capture SKILL.md**
>
> **Inherited heading: Purpose**
>
> This skill defines the durable findings-capture entrypoint for confirmed
> current-state facts and important developer clarifications that should not stay
> stranded in chat.
>
> **Inherited heading: Code Commentary**
>
> **Inherited heading: Logic**
>
> The skill routes durable findings either to task-local artifacts or to
> onboarding through `c-05-create-or-update-onboarding-files` when the finding is
> a verified factual current-state clarification. Its rules now make the
> code-reality check explicit: developer clarifications are not copied verbatim
> into onboarding, and contradictions or partial support must be surfaced and
> resolved before durable capture.
>
> **Inherited heading: Conventions**
>
> Use this onboarding unit with the skill source when changing how confirmed
> findings are routed into task-local durable artifacts or promoted into
> onboarding maintenance. The companion `findings-capture-workflow.md` remains the
> detailed procedure for verification, guardrail checks, capture order, and return
> summaries.
>
> **Inherited heading: Invariants And Boundaries**
>
> `c-01-findings-capture` skill is for confirmed findings and factual current-state clarification capture,
> not speculative notes or future-state planning. It must preserve the distinction
> between task-local artifacts and onboarding, and it must not treat a developer
> clarification as onboarding-ready until the relevant code and supporting context
> have been checked.
>
> **Inherited heading: Todos**
>
> Refresh verification metadata after this skill entrypoint update is committed.
>
> **Inherited heading: Docs References**
>
> No external documentation is needed for this repository-local skill entrypoint.
>
> No relevant external documentation found.
>
> **Inherited heading: Evidence**
>
> **Inherited heading: Repo-Internal References**
>
> This onboarding is backed by the skill entrypoint and its companion workflow.
>
> - The skill entrypoint applies when durable knowledge emerges during developer discussion, task execution, review, or direct clarification.
> - Durable destinations include task-local artifacts and onboarding through `c-05-create-or-update-onboarding-files` skill when a verified factual current-state clarification should survive outside the task.
> - The entrypoint now requires code/onboarding verification and forbids copying developer clarifications into onboarding verbatim when code reality contradicts or only partially supports them.
> - The companion workflow requires verification before capture, only propagates factual current-state findings to onboarding after the guardrail passes, and preserves evidence/capture summaries.
>
> As of the 260703-L9 lifecycle convergence, the task-workflow trigger names an `l-01-agent-lifecycles` orchestrator build job (the retired session-job skill name is gone); the capture workflow itself is unchanged.
>
> As of the 260703-L8 remediation the trigger names an orchestrator build phase (the retired 'build job' vocabulary is gone).
>
> **Inherited heading: Cross-Repo References**
>
> No sibling repository evidence is needed for this package skill.
>
> No meaningful cross-repo references found.

### Scoped inherited companion commentary

These are the old companion’s explanatory notes, retained as historical evidence descriptions rather than freshly validated targets. Original anchor objects, source paths, blobs, digests and locator values remain unchanged in input custody; they are not re-authored here.

> The skill entrypoint applies when durable knowledge emerges during developer discussion, task execution, review, or direct clarification.

> Durable destinations include task-local artifacts and onboarding through `c-05-create-or-update-onboarding-files` skill when a verified factual current-state clarification should survive outside the task.

> The entrypoint now requires code/onboarding verification and forbids copying developer clarifications into onboarding verbatim when code reality contradicts or only partially supports them.

> The companion workflow requires verification before capture, only propagates factual current-state findings to onboarding after the guardrail passes, and preserves evidence/capture summaries.

## Evidence

The following references support the source-contract commentary, not fresh runtime acceptance. Canonical authored source owns the contract; the inspected package copy is an equal distribution twin only. Root overview ownership context is onboarding/overview.md, especially its construction/ownership and retained naming-versus-reading doctrine. The description of a source contract is not runtime acceptance or permission to execute its operations.

- Identity, trigger and companion [1]
- Task and standalone operating modes [2]
- Task destinations versus factual onboarding [3]
- Verification, approval, speculation and ordering guards [4]
