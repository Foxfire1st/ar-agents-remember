# adopt_memory_baseline.py

| Field                  | Value                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                    |
| path                   | `skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py` |
| doc_type               | `file-level-onboarding`                                                               |
| lastUpdated            | 2026-05-12T10:59                                                                      |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`                                            |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

`adopt_memory_baseline.py` is the C-10 command helper. It lets a developer ask whether existing external-memory onboarding can become the first `memory.md` baseline, then performs that adoption only when the ledger is absent and drift is either clean or explicitly accepted.

## Code Commentary

### Logic

The script dynamically loads C-08, C-02, and C-09 so it can reuse the active resolver, drift classifier, and bootstrap behavior without duplicating their logic. `status` resolves context through `code_repository_name` or `code_repository_root`, runs drift, writes a report through C-02's `temp_root`-based report resolver by default, and prints a JSON payload with topology, roots, drift counts, and ledger status. Its C-02 report resolver call passes `context.memory_root` so explicit adoption report paths under the durable memory repo are redirected back to coordination temp. `adopt` requires external topology, stops when a ledger already exists, exits with code 2 when actionable drift is present without `--accept-drift`, supports `--dry-run`, and otherwise creates a default adoption contract before calling C-09 `bootstrap_memory_repo`.

### Conventions

The JSON payload is designed for both humans and wrappers: every path is serialized as POSIX text, `code_repository_name` and `code_repository_root` identify the code checkout explicitly, `state` carries the control decision, existing ledger status reports commit mapping metadata, and `accepted_drift` is included only for adoption paths. C-10 does not invent a separate report path convention; it delegates report path handling to C-02 so adoption drift reports land under the resolved temporary artifact root by default and stay out of durable memory.

### Invariants And Boundaries

This script does not refresh onboarding content, infer that stale onboarding is true, or overwrite existing ledgers. It treats C-02 actionable classifications as a block unless the caller supplies `--accept-drift`, and it lets C-09 own Git initialization, commits, and ledger writing.

### Todos

No current implementation todo is recorded. Broader integration can add wrapper UX around the JSON output without changing the baseline adoption semantics.

### Docs References

No external documentation is needed for this standard-library helper.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

The helper coordinates three existing core packages instead of becoming a fourth owner of resolver, drift, or Git mutation behavior.

| Finding                                                                                                                                                                                                               | Citations            | Source Path                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| The script loads the resolver, drift checker, worktree manager, memory ledger helper, and worktree contract helper directly from the core skill tree.                                                                 | L16-L25; L28-L40     | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| Drift classification writes a report through C-02's path resolver with the resolved memory root, then contributes counts/actionable rows plus `code_repository_name` and `code_repository_root` to the state payload. | L53-L67; L103-L123   | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| Adoption requires external topology, blocks actionable drift unless accepted, supports dry run, and delegates baseline creation to C-09.                                                                                | L135-L176; L198-L202 | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| C-09 bootstrap refuses to overwrite an existing ledger, initializes Git identity when needed, preserves empty docs with `.gitkeep`, and writes the initial ledger.                                                    | L97-L105; L397-L464  | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T10:59: Updated ledger-status notes after branch fields were removed from canonical ledger metadata and C-10 payloads.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected same-repo citation ranges after verifying the C-10 coordination rename behavior.
- 2026-05-11T18:34: Updated after C-10 switched resolver arguments, CLI flags, and status payload keys to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:11: Updated after C-10 passed `memory_root` into C-02 report path resolution so adoption reports cannot land in durable memory.
- 2026-05-10T00:36: Refreshed verification metadata after C-10 delegated report placement to the temp-root resolver path on main.
- 2026-05-09T23:22: Updated after C-10 delegated drift report placement to C-02's temp-root report resolver.
- 2026-05-09T22:46: Created onboarding for the C-10 adoption command helper.
