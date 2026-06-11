# `c-01-findings-capture` skill findings capture SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`         |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|

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

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the skill entrypoint and its companion workflow.

| Finding | Citations | Source Path |
| ------- | --------- | ----------- |
| The skill entrypoint applies when durable knowledge emerges during developer discussion, task execution, review, or direct clarification. | L6-L17 | [mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md) |
| Durable destinations include task-local artifacts and onboarding through `c-05-create-or-update-onboarding-files` skill when a verified factual current-state clarification should survive outside the task. | L19-L26 | [mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md) |
| The entrypoint now requires code/onboarding verification and forbids copying developer clarifications into onboarding verbatim when code reality contradicts or only partially supports them. | L28-L39 | [mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md) |
| The companion workflow requires verification before capture, only propagates factual current-state findings to onboarding after the guardrail passes, and preserves evidence/capture summaries. | L38-L42; L70-L95; L97-L105 | [mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/findings-capture-workflow.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/findings-capture-workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for this package skill.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-02T04:25+02:00: Redirected the Operating Modes "inside a heavy-task-workflow task" reference to an L-01 build job or W-02 task (incl. master + light sub-task series) after W-01 retirement; behavior unchanged. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-15T15:08+02:00: Documented that `c-01-findings-capture` skill now explicitly rejects verbatim onboarding capture for developer clarifications until the clarification has been checked against code reality and mismatches have been resolved.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
