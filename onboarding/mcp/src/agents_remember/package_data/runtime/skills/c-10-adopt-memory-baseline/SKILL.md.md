# c-10-adopt-memory-baseline/SKILL.md

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember-md                                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md` |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4`                    |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

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

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

The skill is the human-facing contract for the adoption script and its trust boundary.

| Finding                                                                                                                                                                                     | Citations                | Source Path                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| The skill defines the adoption use case, uses `--code-repository-name`/`--code-repository-root` command examples, and makes `c-02-memory-quality-control` skill drift plus explicit acceptance the central trust boundary. | L8-L19; L23-L30; L40-L45 | [`c-10-adopt-memory-baseline` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md)                                    |
| The package baseline service implements the documented states and delegates baseline creation to `c-09-git-worktree-manager` skill.                                                                                               | n/a     | [baseline.py](agents-remember-md/mcp/src/agents_remember/memory/baseline.py) |
| `c-10-adopt-memory-baseline` skill's drift run delegates report path resolution to `c-02-memory-quality-control` skill with the resolved `coordination_root` and `temp_root`.                                                                            | n/a                  | [baseline.py](agents-remember-md/mcp/src/agents_remember/memory/baseline.py) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — the `c-10-adopt-memory-baseline` skill `memory_baseline_adopt` example now models preview-first (`dry_run=true`) then apply.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T17:50+02:00: Updated implementation reference after the baseline script route was removed from the skill tree and the MCP package became the only implementation route.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-10-adopt-memory-baseline` name.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` after confirming the `c-10-adopt-memory-baseline` skill coordination-rename contract remains current.
- 2026-05-11T18:34: Updated after `c-10-adopt-memory-baseline` skill command examples adopted `--code-repository-name` and `--code-repository-root`.
- 2026-05-10T00:36: Refreshed verification metadata after `c-10-adopt-memory-baseline` skill's temp-root report wording landed on main.
- 2026-05-09T23:22: Updated after `c-10-adopt-memory-baseline` skill documented temp-root drift report placement.
- 2026-05-09T22:46: Created onboarding for the `c-10-adopt-memory-baseline` skill adoption skill.
