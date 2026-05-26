# C-12-closeout/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-12-closeout/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-26T16:25+02:00                     |
| lastVerifiedCommitHash | `011f84f5a839c95ff0c54a9778794592a4ef30ca` |
| lastVerifiedCommitDate | 2026-05-26T16:27:41+02:00|

## Purpose

This skill documents C-12, the shared closeout contract for approved Agents
Remember edits in repositories that use external memory.

## Code Commentary

### Logic

C-12 owns closeout sequencing for both direct current-checkout edits and
worktree-backed tasks. It selects the matching MCP closeout preview/apply tools,
requires a non-mutating preview before real commits, requires explicit commit
approval with an intent note, runs the package-local missing-onboarding gate,
commits code, refreshes affected onboarding metadata and entity fingerprints,
runs the full memory quality check, commits memory content, prepends the
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
eligible source files cannot escape the gradual onboarding adoption boundary.
Entity fingerprints are refreshed after the code commit because
`git-blob-set-v1` resolves `HEAD:<path>` Git blobs.

### Invariants And Boundaries

C-12 must not commit without explicit approval after a preview, must not create
a memory content commit whose affected onboarding metadata still points at
pre-closeout code, and must not push automatically. It does not create
worktrees, integrate worktrees, clean up worktrees, or initialize memory roots.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-12 defines direct and worktree closeout tool usage and centralizes the shared closeout sequence. | L17-L29; L62-L82 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-12-closeout/SKILL.md) |
| C-12 keeps commit approval separate from implementation approval and requires preview before apply. | L31-L39 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-12-closeout/SKILL.md) |
| C-12 uses the missing-onboarding gate before code commit and routes missing sidecars to C-05. | L50-L59 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-12-closeout/SKILL.md) |
| C-09 routes worktree closeout to C-12 and retains worktree lifecycle, integration, and cleanup ownership. | L8-L14; L63-L74 | [C-09 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-26T16:25+02:00: Created after closeout guidance was promoted from C-09 into a shared direct/worktree closeout skill.
