# agents-remember-md Memory Layer

This repository is the shared memory layer for the `agents-remember-md` code repository.

It is meant to be read beside the code, not instead of it. The code lives at:

- https://github.com/Foxfire1st/agents-remember-md

## What This Repository Shows

This memory repo is a working example of the Agents Remember memory model:

- `onboarding/` stores file-level and repo-level current-state knowledge.
- `memory.md` records the ledger that maps code commits to memory commits.
- `system/` stores memory-layer settings, source registries, and tool notes.
- `docs/` is available for durable supporting documentation that is not tied to one source file.

The important property is that memory is versioned separately from code while still staying tied to exact code commits. Agents can inspect `memory.md` to see which memory commit was verified against which code commit.

## How To Read It

Start with:

1. `memory.md` to see the code-to-memory ledger.
2. `onboarding/overview.md` for the repo-level map.
3. Matching files under `onboarding/` when reading source files in the code repo.

For example, source file:

```text
skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md
```

has memory documentation at:

```text
onboarding/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md.md
```

## Relationship To The Code Repo

The code repo owns behavior. This memory repo owns the durable explanation of that behavior.

When code changes, the corresponding onboarding files should be updated and committed here. The memory ledger should then record the final pair:

```text
<code commit> | <memory commit>
```

That pairing is what lets later agents decide whether onboarding is current, stale, or unsafe to rely on.
