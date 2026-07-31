# mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

`check_missing_onboarding.py` checks only the current Git worktree additions
for eligible source files that do not yet have their required onboarding pair.

## Code Commentary

### Logic

The script collects added, copied, renamed, and untracked files from Git status
sources, resolves each path through the same storage/path-rule helpers used by
drift detection, and reports missing sidecar or inline onboarding for eligible
new files. For CLI runs it derives the canonical repository name from Git's
common directory, so a linked worktree can be named after the task without
changing external-memory resolution. It intentionally does not scan the whole
historical repository.

`missing_onboarding_for_source` is now a three-way router (260731-EFA-L2): `disabled` returns
`None`, sidecar storage delegates to `_missing_sidecar_onboarding(onboarding_root, source_file,
storage_mode)`, `inline` delegates to `_missing_inline_onboarding(code_repository_root,
source_file, storage_mode)`, and anything else falls through to the single `unsupported` row. The
two helpers own one storage mode each: the sidecar one reports the mirrored path when that file
does not exist; the inline one reports `unsupported` on a `UnicodeDecodeError` and `missing` when
no inline block is found. Every `MissingOnboarding` state, `expected_onboarding` value and note
string is byte-identical to the pre-split version.

`main()` passes `--topology` / `--coordination-root` / `--settings-path` / `--onboarding-root`
to `resolve_coordination_context` inside a `CoordinationHints(...)`, matching the resolver's
current signature.

### Conventions

The module is a pre-code-commit closeout helper. Agents run it while new files
are still visible in the worktree, create any reported sidecars, then commit
code and refresh the new sidecars to the real code commit hash.

### Invariants And Boundaries

- Disabled path-rule matches are ignored.
- Sidecar storage is detected by the boolean `is_sidecar_storage(storage_mode)`
  predicate (re-exported by the resolver), not by a truthy label string.
- Sidecar-managed files require `onboarding/<source-path>.md`.
- Inline-managed files require an inline onboarding block.
- Unsupported storage modes are reported instead of guessed.
- Git subprocesses use `stdin=subprocess.DEVNULL`.
- Linked-worktree basenames are not repository identifiers; the Git common
  directory is the repository identity source for CLI resolution.
- Sidecar existence and inline source reads use the shared filesystem helper so
  long Windows paths are checked consistently.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Drift helpers provide sidecar path construction and inline block parsing. | [drift.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |
| Resolver helpers provide storage/path-rule decisions. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| Tests cover untracked, staged, excluded, and renamed file cases. | [test_missing_onboarding.py](agents-remember/mcp/tests/test_missing_onboarding.py) |
| The kernel filesystem helper handles long-path sidecar and source probes. | [filesystem.py](agents-remember/mcp/src/agents_remember/kernel/filesystem.py) |

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  `missing_onboarding_for_source` was split into per-storage-mode helpers
  `_missing_sidecar_onboarding` and `_missing_inline_onboarding`; `main()` was updated for the
  resolver's `CoordinationHints` signature. Every reported state/path/note is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Source swapped the `sidecar_storage_label(storage_mode)` truthy-label check for the boolean `is_sidecar_storage(storage_mode)` resolver predicate (import and call site); recorded the predicate in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-24T18:51+02:00: Updated after the CLI began deriving repository identity from Git common directories and using long-path-safe filesystem probes.
- 2026-05-24T03:24+02:00: Refreshed verification metadata after the source commit landed.
- 2026-05-24T03:22+02:00: Created before the source commit so the new file has an onboarding pair before closeout.
