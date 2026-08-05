# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`git_ops.py` is the git interaction boundary for drift detection. It derives the source-change
notes and deterministic evidence fingerprints the classifiers rely on, over the one shared git
runner.

## Code Commentary

### Logic

Since 260731-EFA-L3 this module owns no runner. Its local `run_git` — a bare `subprocess.run` with
`safe.directory` and `stdin=DEVNULL`, but no environment guard, no timeout and no explicit encoding
— was deleted, and every helper here now calls `run_git` imported from
`agents_remember.kernel.git_command`, e.g. `run_git(repo_root, ["ls-files", "-z"])` in
`list_repo_sources`. No call site passes `timeout=`, so they all take the runner's default
`GIT_LOCAL_TIMEOUT_SECONDS` (300s).
`git_stdout`/`git_blob_hash` read single values; `compute_git_blob_set_fingerprint`
sorts evidence paths, resolves each `HEAD:<path>` blob, and sha256s the
`path\\0blob` list. Both fingerprint helpers take keyword-only `ref` (default
`HEAD`) so callers like the carryover entity-catalog validation can compute
against an explicit ref such as the official branch. `local_change_note`, `local_route_change_note`, and
`entity_local_change_notes` report staged/unstaged state; `list_repo_sources`
and `current_branch_name` expose repo facts.

### Conventions

Git subprocesses still cannot consume MCP stdio transport input, but the guarantee is
`kernel.git_command.run_git`'s: it passes `stdin=subprocess.DEVNULL` unless a caller supplies
`input_text`, and no helper here supplies one.

### Invariants And Boundaries

- External git boundary only: it provides facts, it does not classify or decide policy.
- No second runner: every git subprocess here is `kernel.git_command.run_git`. The
  `env=git_environment()` scrubbing that keeps `git ls-files` / `git diff --quiet` off an ambient
  `GIT_DIR` — and therefore keeps `list_repo_sources` and `local_change_note` reporting on the
  repository the caller passed — belongs to that function, not to this module.
- The `git-blob-set-v1` fingerprint is a deterministic Git blob-set hash over curated evidence paths.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `entities.py` recomputes entity fingerprints and change notes through these helpers. | `classify_entity_fingerprint` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:222-280 |
| `sidecar.py`'s external classifier calls the imported `local_change_note` helper; its own `cat-file` and `diff --quiet` calls go straight to the kernel runner. | `classify_external_onboarding` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:33-112 |
| `run_git` lives here now: selector scrubbing, DEVNULL stdin, and the local/remote/metadata timeout classes. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 4 citation findings (2 rows); scoped recheck clean.

- 2026-07-31T20:54+02:00 — 260731-EFA-L3 curator: the local `run_git` was deleted and every helper
  re-pointed at `kernel.git_command.run_git`, so the Logic sentence describing this module's own
  `subprocess.run` wrapper and the Conventions claim that it sets `stdin=DEVNULL` were both false.
  Rewrote them, recorded that no helper passes `timeout=` (so all take the 300s local default),
  added the "no second runner" invariant, and corrected the `sidecar.py` reference row: sidecar no
  longer imports `run_git` from here, only the change-note helpers.
- 2026-06-11T15:05+02:00 — `git_blob_hash()` and `compute_git_blob_set_fingerprint()` accept a keyword-only `ref` (default `HEAD`) so the carryover entity-catalog validation can recompute fingerprints against the official code ref.
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
