# `c-01-findings-capture` skill findings capture SKILL.md

## Purpose

This skill defines the durable findings-capture entrypoint for confirmed
current-state facts and important developer clarifications that should not stay
stranded in chat.

## Code Commentary

### Logic

The skill routes durable findings either to task-local artifacts or to
onboarding through `c-05-create-or-update-onboarding-files` when the finding is
a verified factual current-state clarification. Its rules now make the
code-reality check explicit: developer clarifications are not copied verbatim
into onboarding, and contradictions or partial support must be surfaced and
resolved before durable capture.

### Conventions

Use this onboarding unit with the skill source when changing how confirmed
findings are routed into task-local durable artifacts or promoted into
onboarding maintenance. The companion `findings-capture-workflow.md` remains the
detailed procedure for verification, guardrail checks, capture order, and return
summaries.

### Invariants And Boundaries

`c-01-findings-capture` skill is for confirmed findings and factual current-state clarification capture,
not speculative notes or future-state planning. It must preserve the distinction
between task-local artifacts and onboarding, and it must not treat a developer
clarification as onboarding-ready until the relevant code and supporting context
have been checked.

### Todos

Refresh verification metadata after this skill entrypoint update is committed.

### Docs References

No external documentation is needed for this repository-local skill entrypoint.

No relevant external documentation found.

## Evidence

### Repo-Internal References

This onboarding is backed by the skill entrypoint and its companion workflow.

- The skill entrypoint applies when durable knowledge emerges during developer discussion, task execution, review, or direct clarification. [1]
- Durable destinations include task-local artifacts and onboarding through `c-05-create-or-update-onboarding-files` skill when a verified factual current-state clarification should survive outside the task. [2]
- The entrypoint now requires code/onboarding verification and forbids copying developer clarifications into onboarding verbatim when code reality contradicts or only partially supports them. [3]
- The companion workflow requires verification before capture, only propagates factual current-state findings to onboarding after the guardrail passes, and preserves evidence/capture summaries. [4]

As of the 260703-L9 lifecycle convergence, the task-workflow trigger names an `l-01-agent-lifecycles` orchestrator build job (the retired session-job skill name is gone); the capture workflow itself is unchanged.

As of the 260703-L8 remediation the trigger names an orchestrator build phase (the retired 'build job' vocabulary is gone).

### Cross-Repo References

No sibling repository evidence is needed for this package skill.

No meaningful cross-repo references found.
