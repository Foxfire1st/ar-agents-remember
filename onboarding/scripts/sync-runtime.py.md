# scripts/sync-runtime.py

| Field                  | Value                         |
| ---------------------- | ----------------------------- |
| repository             | agents-remember-md             |
| path                   | `scripts/sync-runtime.py`      |
| doc_type               | `file-level-onboarding`        |
| lastUpdated            | 2026-06-08T11:53+02:00         |
| lastVerifiedCommitHash | `19b33573a71c8634acfb836d4245f1ead8594f06`             |
| lastVerifiedCommitDate | 2026-06-08T12:38:40+02:00|
| governingOverview      | `overview.md`                  |

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script defines the four root runtime asset source folders and maps them only to MCP package-data targets. | L13-L52 | [scripts/sync-runtime.py](agents-remember-md/scripts/sync-runtime.py) |
| `--check` compares canonical and target file digests, reports missing/extra/changed paths, and exits non-zero when a target is out of sync. | L99-L155 | [scripts/sync-runtime.py](agents-remember-md/scripts/sync-runtime.py) |
| Normal sync mode refuses self-sync, replaces each package-data target folder, copies the canonical source tree into place, and reruns the check. | L118-L125; L158-L171 | [scripts/sync-runtime.py](agents-remember-md/scripts/sync-runtime.py) |
| The root AGENTS instructions tell contributors to edit root runtime asset folders first and run `python3 scripts/sync-runtime.py` rather than editing generated package-data copies directly. | L100-L123 | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-08T11:53+02:00: Created onboarding for the new runtime asset synchronization helper. Verification metadata is pending until the code commit exists.
