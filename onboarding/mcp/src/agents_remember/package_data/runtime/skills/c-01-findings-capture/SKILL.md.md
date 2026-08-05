# `c-01-findings-capture` skill findings capture SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T16:30+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`         |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This onboarding is backed by the skill entrypoint and its companion workflow.

| Finding | Anchor | Source |
| --- | --- | --- |
| The skill entrypoint applies when durable knowledge emerges during developer discussion, task execution, review, or direct clarification. | `# c-01-findings-capture Findings Capture` | mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md:6-39 |
| Durable destinations include task-local artifacts and onboarding through `c-05-create-or-update-onboarding-files` skill when a verified factual current-state clarification should survive outside the task. | `## Durable Destinations` | mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md:19-27 |
| The entrypoint now requires code/onboarding verification and forbids copying developer clarifications into onboarding verbatim when code reality contradicts or only partially supports them. | `## Rules` | mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/SKILL.md:28-39 |
| The companion workflow requires verification before capture, only propagates factual current-state findings to onboarding after the guardrail passes, and preserves evidence/capture summaries. | `### 2. Verify before capture`; `### 5. Apply the onboarding guardrail`; `### 7. Return a capture summary` | mcp/src/agents_remember/package_data/runtime/skills/c-01-findings-capture/findings-capture-workflow.md:38-106 |

As of the 260703-L9 lifecycle convergence, the task-workflow trigger names an `l-01-agent-lifecycles` orchestrator build job (the retired session-job skill name is gone); the capture workflow itself is unchanged.

As of the 260703-L8 remediation the trigger names an orchestrator build phase (the retired 'build job' vocabulary is gone).

## Cross-Repo References

No sibling repository evidence is needed for this package skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T18:41+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the four malformed rows with
  `#`-heading anchors and exact markdown extents — the entrypoint trigger (`# c-01-findings-capture
  Findings Capture`, SKILL.md:6-8), `## Durable Destinations` (19-26), `## Rules` (28-33), and the
  three workflow step headings (findings-capture-workflow.md:38-106). Spurious `agents-remember/`
  prefixes dropped; claim wording unchanged.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): retired build-job vocabulary removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the task-workflow reference now names the l-01-agent-lifecycles orchestrator build job. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-02T04:25+02:00: Redirected the Operating Modes "inside a heavy-task-workflow task" reference to an L-01 build job or W-02 task (incl. master + light sub-task series) after W-01 retirement; behavior unchanged. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-15T15:08+02:00: Documented that `c-01-findings-capture` skill now explicitly rejects verbatim onboarding capture for developer clarifications until the clarification has been checked against code reality and mismatches have been resolved.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
