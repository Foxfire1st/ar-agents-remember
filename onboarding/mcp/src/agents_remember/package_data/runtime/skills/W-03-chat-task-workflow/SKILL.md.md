# W-03-chat-task-workflow/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/W-03-chat-task-workflow/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|

## Purpose

This skill defines the compact chat-mode coding workflow for approved current-checkout edits. It preserves the normal Agents Remember onboarding gate and pairs source with verified onboarding before implementation, while sending small approved edits through C-09 `direct-closeout` for external-memory commit and ledger discipline.

## Code Commentary

### Logic

The workflow starts each coding task by resolving C-08 context and running C-02
memory quality control once for the repository, using task-start drift as the
trust baseline and applying C-02's clean-source versus dirty-source drift
classification. During investigation it requires relevant source files and
onboarding files to be read together, then requires the developer to approve a
plan with distinct implementation examples before code changes begin. After
implementation approval, code and onboarding updates happen in the same editing
pass. Before code commit, tasks that added source files run
`check_missing_onboarding` and create reported missing sidecars through C-05.
Small approved current-checkout edits close through C-09 `direct-closeout`,
which previews first and then stops for explicit commit approval before real
commits.

### Conventions

W-03 is intentionally lightweight: planning can stay in chat, but it still uses the same trust gates as larger workflows. It treats modified source/onboarding pairs as pending verification after the initial gate, and it delegates the Git sequence to C-09 instead of hand-assembling code, memory, and ledger commits.

### Invariants And Boundaries

Do not plan against clean-source drifted, missing-verification, or orphaned pre-existing onboarding. Leave dirty-source drift as active work-in-progress unless the developer explicitly takes ownership of it. Do not implement before explicit developer approval. Do not postpone required onboarding updates to the end of the task when the source change affects durable current-state knowledge. Newly added source files must not be committed before the missing-onboarding check has passed or C-05 has created the reported sidecars. Direct closeout must remain preview-first and must rerun C-05 when required onboarding is missing.

### Todos

No current todo is recorded for this workflow skill.

### Docs References

No external domain documentation applies to this repository-local workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

W-03 is the chat-mode workflow that complements W-02 light tasks and C-09 direct closeout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The workflow requires C-08 and C-02 memory quality control at task start, applies clean-source versus dirty-source drift classification, blocks planning against clean-source stale onboarding, and avoids rerunning the gate merely because the current task later changes files. | L8-L8 | [W-03 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-03-chat-task-workflow/SKILL.md) |
| Investigation pairs source and onboarding reads, treats already modified pairs as pending verification, and waits for explicit developer approval before code changes. | L10-L10 | [W-03 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-03-chat-task-workflow/SKILL.md) |
| After implementation approval, source and onboarding updates happen in the same pass, newly added source files run the missing-onboarding check before code commit, and small current-checkout edits close through C-09 direct closeout only after a separate commit-approval stop. | L12-L16 | [W-03 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-03-chat-task-workflow/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to W-03 task-start checks.
- 2026-05-24T04:34+02:00: Updated after chat workflow separated implementation approval from commit approval and routed task-start checks through C-02 memory quality control.
- 2026-05-24T03:24+02:00: Updated after chat closeout adopted `check_missing_onboarding` before code commit for newly added files.
- 2026-05-14T20:11+02:00: Created file-level onboarding for the chat task workflow while preparing direct closeout for the external-memory terminology alignment.
