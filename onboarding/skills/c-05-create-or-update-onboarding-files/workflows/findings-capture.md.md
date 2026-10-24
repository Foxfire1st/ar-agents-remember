# skills/c-05-create-or-update-onboarding-files/workflows/findings-capture.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

The findings-capture procedure this skill now owns: a confirmed finding gets a durable destination instead of staying in chat, and a verified factual current-state clarification may propagate into onboarding.

## Code Commentary

The file is the surviving owner of the procedure kept from the retired findings-capture skill, and its opening comment says so: its durable destinations are onboarding files authored through this skill, and a finding held only in chat is still a defect (`l-01 core/invariants.md`). It keeps the skill's frontmatter name for its new parent and states the two operating modes — inside a task workflow (an `l-01-agent-lifecycles` orchestrator build phase or a `w-02-light-task-workflow` task, including a master with light sub-tasks) and standalone during direct clarification.

It keeps the four durable destinations and their ownership order: `requirement_change_candidates.md` when the finding changes scope, requirements or developer intent; `architecture_open_questions.md` when it exposes a structural decision, dependency boundary or design uncertainty; the active phase artifact when it is planning-, implementation- or review-local; and onboarding through this skill when the finding is a verified factual current-state clarification that should survive outside the task. The guardrail on propagation survives too: developer clarifications are checked against code before durable capture, a mismatch is surfaced and resolved rather than copied, approved `requirements.md` and `architecture.md` are never rewritten from one finding without approval, and speculative, future-state, unresolved or task-only notes stay out of onboarding. The workflow file it names as its companion, `findings-capture-workflow.md`, carries the ordered procedure.

## Evidence

- The kept procedure names its durable destinations, its two operating modes and the rule that a confirmed finding is never left only in chat. [1]
- Onboarding propagation is the last resort destination and is gated on verified current-state fact, with approved requirement and architecture text never rewritten from one finding. [2]
