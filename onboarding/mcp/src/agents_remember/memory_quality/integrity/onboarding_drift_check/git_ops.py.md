# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`git_ops.py` is the git interaction boundary for drift detection. It runs git
subprocesses and derives the source-change notes and deterministic evidence
fingerprints the classifiers rely on.

## Code Commentary

### Logic

`run_git` wraps `subprocess.run` with `safe.directory` and `stdin=DEVNULL`;
`git_stdout`/`git_blob_hash` read single values; `compute_git_blob_set_fingerprint`
sorts evidence paths, resolves each `HEAD:<path>` blob, and sha256s the
`path\\0blob` list. `local_change_note`, `local_route_change_note`, and
`entity_local_change_notes` report staged/unstaged state; `list_repo_sources`
and `current_branch_name` expose repo facts.

### Conventions

Git subprocesses use `stdin=subprocess.DEVNULL` so they cannot consume MCP stdio
transport input.

### Invariants And Boundaries

- External git boundary only: it provides facts, it does not classify or decide policy.
- The `git-blob-set-v1` fingerprint is a deterministic Git blob-set hash over curated evidence paths.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `entities.py` recomputes entity fingerprints and change notes through these helpers. | [entities.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py) |
| `sidecar.py` reads source diff/notes through `run_git` and the change-note helpers. | [sidecar.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |

## Update History

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
