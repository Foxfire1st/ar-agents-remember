# W-03-chat-task-workflow/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/W-03-chat-task-workflow/SKILL.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-14T20:11+02:00                     |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a` |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This skill defines the compact chat-mode coding workflow for approved current-checkout edits. It preserves the normal Agents Remember onboarding gate and pairs source with verified onboarding before implementation, while sending small approved edits through C-09 `direct-closeout` for external-memory commit and ledger discipline.

## Code Commentary

### Logic

The workflow starts each coding task by resolving C-08 context and running C-02 drift detection once for the repository. During investigation it requires relevant source files and onboarding files to be read together, then requires the developer to approve a plan with distinct implementation examples before code changes begin. After approval, code and onboarding updates happen in the same editing pass. Small approved current-checkout edits close through C-09 `direct-closeout`, which previews first, then commits code, refreshes onboarding metadata, commits memory content, and commits the ledger after explicit commit approval.

### Conventions

W-03 is intentionally lightweight: planning can stay in chat, but it still uses the same trust gates as larger workflows. It treats modified source/onboarding pairs as pending verification after the initial gate, and it delegates the Git sequence to C-09 instead of hand-assembling code, memory, and ledger commits.

### Invariants And Boundaries

Do not plan against drifted, missing-verification, or orphaned pre-existing onboarding. Do not implement before explicit developer approval. Do not postpone required onboarding updates to the end of the task when the source change affects durable current-state knowledge. Direct closeout must remain preview-first and must rerun C-05 when required onboarding is missing.

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
| The workflow requires C-08 and C-02 at task start, blocks planning against stale onboarding, and avoids rerunning the gate merely because the current task later changes files. | L8-L8 | [W-03 SKILL.md](agents-remember-md/skills/W-03-chat-task-workflow/SKILL.md) |
| Investigation pairs source and onboarding reads, treats already modified pairs as pending verification, and waits for explicit developer approval before code changes. | L10-L10 | [W-03 SKILL.md](agents-remember-md/skills/W-03-chat-task-workflow/SKILL.md) |
| After approval, source and onboarding updates happen in the same pass, and small current-checkout edits close through C-09 direct closeout with external-memory ledger sequencing. | L12-L14 | [W-03 SKILL.md](agents-remember-md/skills/W-03-chat-task-workflow/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-14T20:11+02:00: Created file-level onboarding for the chat task workflow while preparing direct closeout for the external-memory terminology alignment.
