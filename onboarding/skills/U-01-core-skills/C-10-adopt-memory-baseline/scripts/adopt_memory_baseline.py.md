# adopt_memory_baseline.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:46                           |
| lastVerifiedCommitHash | `9ab2d2ceddc5dd0b83e14b64b44f5087e4d1935e` |
| lastVerifiedCommitDate | 2026-05-09T22:43                           |

## Purpose

`adopt_memory_baseline.py` is the C-10 command helper. It lets a developer ask whether existing shared-memory onboarding can become the first `memory.md` baseline, then performs that adoption only when the ledger is absent and drift is either clean or explicitly accepted.

## Code Commentary

### Logic

The script dynamically loads C-08, C-02, and C-09 so it can reuse the active resolver, drift classifier, and bootstrap behavior without duplicating their logic. `status` resolves context, runs drift, writes a report under the repo-scoped task area by default, and prints a JSON payload with topology, roots, drift counts, and ledger status. `adopt` requires shared topology, stops when a ledger already exists, exits with code 2 when actionable drift is present without `--accept-drift`, supports `--dry-run`, and otherwise creates a default adoption contract before calling C-09 `bootstrap_memory_repo`.

### Conventions

The JSON payload is designed for both humans and wrappers: every path is serialized as POSIX text, `state` carries the control decision, and `accepted_drift` is included only for adoption paths. The default report path is `tasks/<repo>/<repo>_<branch>_drift-report.md`, so adoption reports do not fall back into the flat task root.

### Invariants And Boundaries

This script does not refresh onboarding content, infer that stale onboarding is true, or overwrite existing ledgers. It treats C-02 actionable classifications as a block unless the caller supplies `--accept-drift`, and it lets C-09 own Git initialization, commits, and ledger writing.

### Todos

No current implementation todo is recorded. Broader integration can add wrapper UX around the JSON output without changing the baseline adoption semantics.

### Docs References

No external documentation is needed for this standard-library helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The helper coordinates three existing core packages instead of becoming a fourth owner of resolver, drift, or Git mutation behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script loads the resolver, drift checker, worktree manager, memory ledger helper, and worktree contract helper directly from the core skill tree. | L16-L25; L28-L40 | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| Drift classification writes a report and contributes counts/actionable rows to the state payload. | L53-L78; L106-L123 | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| Adoption requires shared topology, blocks actionable drift unless accepted, supports dry run, and delegates baseline creation to C-09. | L138-L176; L199-L205 | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| C-09 bootstrap refuses to overwrite an existing ledger, initializes Git identity when needed, preserves empty docs with `.gitkeep`, and writes the initial ledger. | L83-L87; L297-L359 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T22:46: Created onboarding for the C-10 adoption command helper.
