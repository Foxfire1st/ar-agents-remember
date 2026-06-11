# c-12-closeout/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-29T07:36+02:00                     |
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6` |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|

## Purpose

This skill documents `c-12-closeout` skill, the shared closeout contract for approved Agents
Remember edits in repositories that use external memory.

## Code Commentary

### Logic

`c-12-closeout` skill owns closeout sequencing for worktree-backed tasks. It
uses the worktree closeout preview/apply tools against the task contract,
requires a non-mutating preview before real commits, requires explicit commit
approval with an intent note, runs the package-local missing-onboarding gate,
commits code, refreshes affected onboarding metadata, entity fingerprints, route
overview metadata, and generated route indexes, runs the full memory quality
check, commits memory content only after the quality gate is clean, prepends the
`C2 | M2` mapping to `memory.md`, and commits the ledger update.

Closeout is worktree-only: every change affecting the code repo runs through a
`c-09-git-worktree-manager` dual worktree (code + memory), and the former
direct-closeout usage block was removed (issue #62). Worktree closeout is used
when `c-09-git-worktree-manager` skill created or attached a task contract;
`c-09-git-worktree-manager` skill then owns later integration and cleanup.

### Conventions

Closeout approval is separate from implementation approval. Agents must not
treat a previous "looks good", implementation approval, or their own judgment
as commit approval. The matching preview tool is the approval prompt surface:
it reports the proposed code, memory, and ledger commit messages before the
apply tool mutates Git.

The missing-onboarding check is scoped to current additions so newly added
eligible source files cannot escape the gradual onboarding adoption boundary. A
parallel content gate covers changed (already-onboarded) files: a changed source
whose existing sidecar body was not updated this task fails closeout, so
verification metadata is never advanced over stale onboarding content.
Entity fingerprints are refreshed after the code commit because
`git-blob-set-v1` resolves `HEAD:<path>` Git blobs. Route overview metadata and
generated route indexes are refreshed before `memory_quality_check` so the
quality gate sees the same memory tree that will be committed.

### Invariants And Boundaries

`c-12-closeout` skill must not commit without explicit approval after a preview, must not create
a memory content commit whose affected onboarding metadata still points at
pre-closeout code, must not commit memory before route overview metadata,
generated route indexes, and `memory_quality_check` are clean for the new code
commit, must not advance verification metadata for a changed source file whose
sidecar content was not updated in the task, and must not push automatically. It does not create worktrees, integrate
worktrees, clean up worktrees, or initialize memory roots.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-12-closeout` skill defines worktree closeout tool usage and centralizes the closeout sequence. | L11-L31; L70-L96 | [`c-12-closeout` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-12-closeout` skill keeps commit approval separate from implementation approval and requires preview before apply. | L31-L39 | [`c-12-closeout` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-12-closeout` skill uses the missing-onboarding gate before code commit and routes missing sidecars to `c-05-create-or-update-onboarding-files` skill. | L50-L59 | [`c-12-closeout` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-09-git-worktree-manager` skill routes worktree closeout to `c-12-closeout` skill and retains worktree lifecycle, integration, and cleanup ownership. | L8-L14; L63-L74 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: the skill no longer offers `direct_closeout_preview`/`apply` or the "small approved edits" direct-closeout guidance; the MCP Tools block lists only the worktree closeout pair and the intro states the worktree-only rule.
- 2026-05-29T07:36+02:00: Updated after `c-12-closeout` skill added a changed-file content gate — a changed source whose existing sidecar body was not updated this task fails closeout — plus the matching failure condition and boundary against metadata-only verification refreshes.
- 2026-05-28T15:24+02:00: Updated after `c-12-closeout` skill explicitly required route overview metadata, generated route index refresh, and clean `memory_quality_check` before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-26T16:25+02:00: Created after closeout guidance was promoted from `c-09-git-worktree-manager` skill into a shared direct/worktree closeout skill.
