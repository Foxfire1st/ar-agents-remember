# scripts/sync-runtime.py

| Field                  | Value                         |
| ---------------------- | ----------------------------- |
| repository             | agents-remember             |
| path                   | `scripts/sync-runtime.py`      |
| doc_type               | `file-level-onboarding`        |
| lastUpdated            | 2026-06-10T00:40+02:00         |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`             |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-runtime.py` keeps the root canonical runtime asset folders
(`agents-md-files/`, `benchmarks/`, `providers/`, and `system/`) synchronized
with their generated MCP package-data copies.

## Code Commentary

### Logic

The script resolves the repository root from its own path, declares the MCP
package-data root, and defines four explicit `RuntimeTarget` mappings:

- `agents-md-files/` to `mcp/src/agents_remember/package_data/runtime/agents-md-files/`
- `benchmarks/` to `mcp/src/agents_remember/package_data/benchmarks/`
- `providers/` to `mcp/src/agents_remember/package_data/runtime/providers/`
- `system/` to `mcp/src/agents_remember/package_data/runtime/system/`

It computes SHA-256 digests for every non-ignored file under each canonical
source and target, reports missing, extra, and changed paths, and exits non-zero
from `--check` when any generated target is stale. Normal sync mode replaces
each package-data target directory wholesale from its canonical source and then
runs the same check. `--list-targets` prints the explicit source-to-target
mapping.

### Conventions

Ignore only local/generated filesystem noise: `.DS_Store`, cache directories,
`__pycache__`, and `.pyc` files. Runtime asset targets are MCP package-data
targets only; harness starter packages are intentionally not included.

### Invariants And Boundaries

- The four root runtime asset folders are canonical.
- The matching MCP package-data folders are generated.
- The helper refuses to sync a target path onto its own source path.
- The helper does not sync skills, harness starter packages, docs, or user-owned
  installed runtime files.

### Todos

No open file-local todos.

## Docs References

No external documentation is needed for this repository-local helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The four explicit canonical-to-package-data runtime targets. | `TARGETS` | scripts/sync-runtime.py:44-53 |
| Digest comparison reports missing, extra, and changed files for `--check`. | `diff_target`; `check_targets` | scripts/sync-runtime.py:111-123; scripts/sync-runtime.py:173-186 |
| Normal sync refuses self-sync, performs copy-then-swap replacement, and rechecks targets. | `sync_target`; `replace_tree`; `sync_targets` | scripts/sync-runtime.py:130-133; scripts/sync-runtime.py:136-156; scripts/sync-runtime.py:189-202 |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-06-10T00:40+02:00 — `sync_target` now uses crash-safe `replace_tree` (copy to `<target>.ar-sync-new`, rename live target aside, swap in, then remove the old tree; stale staging/retired leftovers are cleaned on re-run), and `extended_length()` applies the Windows `\\?\` prefix so syncs and `--check` walks work past 260-char paths even with `LongPathsEnabled=0`. Replaces the delete-then-copy that gutted `package_data` when a long-path crash hit mid-delete (2026-06-09 incident).
- 2026-06-08T11:53+02:00: Created onboarding for the new runtime asset synchronization helper. Verification metadata is pending until the code commit exists.
