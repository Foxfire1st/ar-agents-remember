# C-12-closeout/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/C-12-closeout/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-29T07:36+02:00                     |
| lastVerifiedCommitHash | `72789a48dc47acf417725ae051eaa123cadeaa0b` |
| lastVerifiedCommitDate | 2026-06-02T04:33:30+02:00|

## Purpose

This skill documents C-12, the shared closeout contract for approved Agents
Remember edits in repositories that use external memory.

## Code Commentary

### Logic

C-12 owns closeout sequencing for both direct current-checkout edits and
worktree-backed tasks. It selects the matching MCP closeout preview/apply tools,
requires a non-mutating preview before real commits, requires explicit commit
approval with an intent note, runs the package-local missing-onboarding gate,
commits code, refreshes affected onboarding metadata, entity fingerprints, route
overview metadata, and generated route indexes, runs the full memory quality
check, commits memory content only after the quality gate is clean, prepends the
`C2 | M2` mapping to `memory.md`, and commits the ledger update.

The skill keeps direct checkout and worktree-backed closeout on one shared
code-memory-ledger sequence. Direct closeout is for small approved current
checkout edits or memory-only polish. Worktree closeout is used when C-09
created or attached a task contract; C-09 then owns later integration and
cleanup.

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

C-12 must not commit without explicit approval after a preview, must not create
a memory content commit whose affected onboarding metadata still points at
pre-closeout code, must not commit memory before route overview metadata,
generated route indexes, and `memory_quality_check` are clean for the new code
commit, must not advance verification metadata for a changed source file whose
sidecar content was not updated in the task, and must not push automatically. It does not create worktrees, integrate
worktrees, clean up worktrees, or initialize memory roots.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-12 defines direct and worktree closeout tool usage and centralizes the shared closeout sequence. | L17-L29; L62-L88 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/C-12-closeout/SKILL.md) |
| C-12 keeps commit approval separate from implementation approval and requires preview before apply. | L31-L39 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/C-12-closeout/SKILL.md) |
| C-12 uses the missing-onboarding gate before code commit and routes missing sidecars to C-05. | L50-L59 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/C-12-closeout/SKILL.md) |
| C-09 routes worktree closeout to C-12 and retains worktree lifecycle, integration, and cleanup ownership. | L8-L14; L63-L74 | [C-09 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/C-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-29T07:36+02:00: Updated after C-12 added a changed-file content gate — a changed source whose existing sidecar body was not updated this task fails closeout — plus the matching failure condition and boundary against metadata-only verification refreshes.
- 2026-05-28T15:24+02:00: Updated after C-12 explicitly required route overview metadata, generated route index refresh, and clean `memory_quality_check` before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-26T16:25+02:00: Created after closeout guidance was promoted from C-09 into a shared direct/worktree closeout skill.
