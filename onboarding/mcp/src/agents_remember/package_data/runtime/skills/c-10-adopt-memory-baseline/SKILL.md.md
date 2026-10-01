# c-10-adopt-memory-baseline/SKILL.md

## Purpose

This skill documents the ergonomic adoption path for existing external-memory onboarding that predates `memory.md`. It tells agents how to inspect that onboarding, surface drift, and create the first ledgered baseline only after the developer has accepted the trust decision.

## Code Commentary

### Logic

The skill routes users through `status` before `adopt`. The workflow resolves the code repository with `c-08-ar-coordination-context-resolver` skill using `--code-repository-name` or `--code-repository-root`, runs `c-02-memory-quality-control` skill drift classification with the reusable report under `c-08-ar-coordination-context-resolver` skill's resolved temp root by default, checks for an existing ledger, blocks actionable drift unless `--accept-drift` is present, and then delegates the actual external-memory bootstrap and `memory.md` creation to `c-09-git-worktree-manager` skill.

### Conventions

The output is state-oriented: `ready`, `blocked-drift`, `already-ledgered`, `adopted`, and `would-adopt` are the reviewable states. `--accept-drift` is not an automatic refresh; it records the developer's assertion that the current onboarding is factual enough to become the memory baseline.

### Invariants And Boundaries

`c-10-adopt-memory-baseline` skill may create the initial ledgered external-memory baseline through `c-09-git-worktree-manager` skill, but it must not overwrite an existing `memory.md` and must not update onboarding content. `c-05-create-or-update-onboarding-files` skill remains the refresh path for stale or incomplete onboarding.

### Todos

No current todo is recorded for the skill description itself. Future work should stay in the script and tests unless the user-facing workflow changes.

### Docs References

No external documentation is needed for this repository-local skill.

No relevant external documentation found.

## Evidence

### Repo-Internal References

The skill is the human-facing contract for the adoption script and its trust boundary.

- The skill defines the adoption use case, uses `--code-repository-name`/`--code-repository-root` command examples, and makes `c-02-memory-quality-control` skill drift plus explicit acceptance the central trust boundary. [1]
- The package baseline service implements the documented states and delegates baseline creation to `c-09-git-worktree-manager` skill. [2]
- `c-10-adopt-memory-baseline` skill's drift run delegates report path resolution to `c-02-memory-quality-control` skill with the resolved `coordination_root` and `temp_root`. [3]

### Cross-Repo References

No sibling repository evidence is needed for the skill itself.

No meaningful cross-repo references found.
