# mcp/src/agents_remember/memory_quality/ — Memory Quality Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/memory_quality/`  |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`memory_quality/` owns memory-layer quality control for the MCP package. It
groups integrity checks that compare onboarding to source state and style
checks that enforce repository memory conventions.

## Hot Path Summary

`check.py` is the public package-level runner. It can execute style-only checks
without repository context, or combine drift integrity and style checks when an
MCP controller supplies `DriftCheckContext`. Drift logic lives under
`integrity/onboarding_drift_check/`; the pre-code-commit missing-onboarding
check lives at `integrity/check_missing_onboarding.py`; update-history ordering lives under
`style/update_history/`. The history-order checker is diagnostic; the matching
`history_order_fix.py` module is the explicit mutating script for timestamped
history-order fixes.

## Route Model

- `check.py` normalizes check names, dispatches quality runners, and returns one
  combined payload.
- `integrity/onboarding_drift_check/` contains the moved `c-02-memory-quality-control` skill drift classifier
  and bounded summary helper; the summary run also persists a durable
  `ar-drift-snapshot/v1` JSON (best-effort) under `logs/observer/drift/` for the
  observer dashboard to read without re-classifying (slice 3b). Task 29 S7 writes the snapshot's
  `sourceRoot`, `memoryRoot`, optional `reportPath`, and `checkedAt` provenance so actionable-drift
  attention can say which repo/memory pair raised the notice and when it was measured. Task 32 routes
  that writer through the shared observer drift-snapshot path helper so producer
  writes, projection pruning, and cleanup deletion share one filename contract.
- `integrity/check_missing_onboarding.py` checks only current worktree
  additions so newly added eligible files get sidecars before the code commit.
- `style/update_history/` checks that onboarding `## Update History` bullets
  are newest-first and timestamped, and contains the dedicated history-order
  fix script.

## Invariants And Boundaries

- Task-start work should use `drift_check` to build the onboarding worklist.
- Closeout should run `memory_quality_check` after onboarding refresh and before
  the memory content commit.
- Closeout should run `check_missing_onboarding` before the code commit when
  the task added source files; this is local worktree responsibility, not a
  whole-repository adoption scan.
- Style checks should not block the beginning of normal implementation work.
- `memory_quality_check` should stay diagnostic; mechanical style rewrites
  belong in focused fix scripts.
- New memory-quality checks should be placed under `style/` or `integrity/`
  according to what they validate.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The MCP controller builds drift context and calls the package runner for `memory_quality_check`. | [memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |
| Tool metadata and server registration expose `memory_quality_check` to agents. | [mcp/tools/memory.py](agents-remember/mcp/src/agents_remember/mcp/tools/memory.py); [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. | [history_order_fix.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py) |
| The missing-onboarding checker catches newly added worktree files before code commit. | [check_missing_onboarding.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py) |

## 260731-EFA-L2 — Every Verdict Is Now Emitted From One Place

The check catalogue, the dispatch contract and the diagnostic-only rule are unchanged. What changed
is that each classifier now emits its verdicts through a single constructor, which is what makes the
verdict *set* auditable — previously the same nine-field `DriftRow` or `MissingOnboarding` was
rebuilt at every branch, and a field could silently disagree between two of them.

- **`check_missing_onboarding.py`** dispatches on storage mode to `_missing_sidecar_onboarding`
  (the mirrored path this source expects, reported when the file does not exist) and
  `_missing_inline_onboarding` (the in-source block, reported when absent *or unreadable*). The
  three states remain `missing`, `unsupported` (non-UTF-8 source, or a storage mode this checker
  does not implement) and "no finding"; the unsupported-storage-mode fallthrough is now the
  function's visible last statement rather than a branch buried after the inline path.
- **`sidecar.py`** builds one local `row(...)` closure that fixes the sidecar's identity and
  verification stamp, so a classifier only supplies `classification` / `trust` /
  `affected_sections` / `note`. `_early_classification` groups the three pre-diff verdicts —
  `missing verification`, `orphaned`, and the recorded commit not being in git history — and
  returning `None` from it is what means "go on and diff". The classification vocabulary and trust
  levels are byte-identical.
- **`entities.py`** takes `EntityCatalog` (frozen: `onboarding_file`, `onboarding_root`,
  `repository`, `settings`, `last_updated`). All five are read out of one document before any row
  is emitted and every row builder needs all five, so the catalog travels as the document it is.
- **`drift.py`** and `check_missing_onboarding.py` resolve coordination context through
  `hints=CoordinationHints(topology=, coordination_root=, settings_path=, onboarding_root=)` — the
  resolver's new keyword-bundle API (see
  [kernel/coordination_context](../kernel/coordination_context/overview.md)). Resolved contexts are
  identical.

## 260731-EFA-L3 — Every Verdict Is Now Read Through One Git Runner

Every check this route emits is ultimately a statement about *a repository*: which files
the worktree added, which blobs a source has, whether a recorded commit is in history.
Two files in this route each carried their own private `run_git`, and both were the
kernel's runner with `env=git_environment()` dropped — the guard that strips the eight
`GIT_DIR`-family repository selectors. `cwd=` does not defeat those variables, so with
`GIT_DIR` exported these checks would read a *different repository* and emit verdicts
about it in the current one's name. Both copies are gone; both files now import
`run_git` from `agents_remember.kernel.git_command`.

- **`integrity/check_missing_onboarding.py`** is the pre-code-commit gate, so a
  misdirected read is not a wrong report but a wrongly-passed gate — this is the check
  whose stated boundary above is that it is "local worktree responsibility, not a
  whole-repository adoption scan", and until this leaf an exported `GIT_DIR` was enough
  to make it enumerate someone else's worktree. Its private runner always raised on a
  nonzero return, so `run_git` was the wrong name for it; it is now **`require_git`**
  (line 176), delegating to the owner and keeping the fail-fast contract. It still
  returns the `CompletedProcess` rather than stripped text — unlike the same-named
  helper in `worktrees/modules/git.py` — because every caller reads NUL-delimited
  output that a `.strip()` would corrupt. Both call sites moved:
  `worktree_added_sources` (lines 82-83, the three `-z` enumerations) and
  `code_repository_name_from_git` (line 192, the `--git-common-dir` probe that decides
  which repository name the finding is filed under).
- **`integrity/onboarding_drift_check/git_ops.py`** is the drift classifier's entire git
  surface — `current_branch_name` (line 15), `local_change_note` (line 22),
  `list_repo_sources` (line 41), `git_stdout` (line 54), `git_blob_hash` (line 61) and
  the entity fingerprints built on it. Its `run_git` was the route's other copy and is
  deleted; `drift.py`, `report.py` and `sidecar.py` correspondingly import `run_git`
  from the kernel rather than re-exporting it through `git_ops`.

The checks, their names, their classification vocabulary and their emitted rows are
unchanged. What changed is that a verdict can no longer be computed against a repository
the caller did not name. `mcp/tests/test_git_command.py` holds the proof against a decoy
repository named by the selectors.

## Update History

- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: recorded that this route no longer contains a
  git runner. `integrity/onboarding_drift_check/git_ops.py` and
  `integrity/check_missing_onboarding.py` each held a private `run_git` that was the kernel's
  runner minus `env=git_environment()`, so an exported `GIT_DIR` could make these checks read a
  different repository — including the pre-code-commit gate whose stated boundary is that it is
  local-worktree-scoped. Both now call `kernel/git_command.run_git`; the misnamed always-raising
  copy in `check_missing_onboarding.py` became `require_git` (line 176), with
  `worktree_added_sources` and `code_repository_name_from_git` moved onto it. No statement in the
  body was false — the route model, check catalogue and emitted rows are unchanged — this adds the
  correctness fact behind them. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: verdict construction was centralized per classifier
  (`_missing_sidecar_onboarding`/`_missing_inline_onboarding`, `sidecar.py`'s `row(...)` closure
  and `_early_classification`, `EntityCatalog` in `entities.py`), and both CLI entry points now
  pass `hints=CoordinationHints(...)` to the resolver. No check was added, removed or reclassified;
  emitted rows are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: drift snapshot summaries now carry source-root,
  memory-root, optional report-path, and checked-at provenance for actionable-drift attention detail.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-27T23:09+02:00 — Task 32 route impact: the drift summary writer now uses the shared observer drift-snapshot path helper, keeping producer writes aligned with projection pruning and cleanup deletion. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T20:48+02:00 — Slice 3b (browser-dashboard): the drift summary run now also persists a durable `ar-drift-snapshot/v1` JSON under `logs/observer/drift/` (`_write_drift_snapshot`, best-effort) for the observer dashboard to read without re-classifying; recorded this new output in the `integrity/onboarding_drift_check/` Route Model bullet. The route's check responsibilities are otherwise unchanged. Verification metadata pinned until closeout stamps the 3b code commit.
- 2026-06-11T15:20+02:00 — No route impact: onboarding_drift_check/git_ops.py fingerprint helpers gained a keyword-only ref parameter for carryover entity-catalog validation; route structure and check responsibilities are unchanged.
- 2026-06-06T12:15: Re-verified against the current memory-quality package; corrected controller and MCP payload-builder references after memory tools moved out of the former `skill_tools.py`/`mcp/tools.py` surfaces.
- 2026-05-31T12:40+02:00: Removed the `integrity/ledger_consistency.py` reserved-stub bullet after the empty stub source and its sidecar were deleted in the 1.0.0 remediation.
- 2026-05-24T03:24+02:00: Updated after adding `check_missing_onboarding` as the pre-code-commit integrity pass for newly added files.
- 2026-05-24T03:09+02:00: Updated after adding the dedicated `history_order_fix.py` script and keeping `memory_quality_check` report-only.
- 2026-05-24T02:47+02:00: Created after memory quality became a first-class package route with integrity and style subdomains.
