# scripts/sync-runtime.py

## Governing Overview

[overview](../overview.md)

## Purpose

`scripts/sync-runtime.py` keeps the three canonical runtime asset folders (`benchmarks/`, `providers/`, `system/`) synchronized with their generated MCP package-data copies.

## Code Commentary

### Logic

The script resolves the repository root from its own path, declares the MCP
package-data root, and defines three explicit `RuntimeTarget` mappings:

- `benchmarks/` to `mcp/src/agents_remember/package_data/benchmarks/`
- `providers/` to `mcp/src/agents_remember/package_data/runtime/providers/`
- `system/` to `mcp/src/agents_remember/package_data/runtime/system/`


### Comparison boundaries

`RuntimeTarget` carries label/source/path only. Comparison and copy use the same global local-noise predicate.

`RuntimeDiff` carries **`source_missing`**, and `in_sync` requires its absence. Without the
flag a target whose canonical source and generated copy are *both* missing would compare equal and
report `ok`: an empty comparison is not evidence of a synced tree, and a caller who pointed the
generator at the wrong root would read green rows for nothing. `diff_target` returns
`source_missing=True` before digesting, and `print_diff` names the absent canonical source.

It computes SHA-256 digests for every non-ignored file under each canonical
source and target, reports missing, extra, and changed paths, and exits non-zero
from `--check` when any generated target is stale. Normal sync mode replaces
each package-data target directory wholesale from its canonical source and then
runs the same check. `--list-targets` prints the explicit source-to-target
mapping.

### Conventions

`replace_tree` removes stale staging/retired leftovers, completes the new copy, then renames the old target aside and the staged tree into place before removing the retired tree. A copy failure before the first rename leaves the live target intact. The two renames are separate operations; this description does not claim an atomic directory exchange.

Ignore local/generated filesystem noise: `.DS_Store`, cache directories, `__pycache__` and `.pyc` files through the shared predicate. Runtime targets are MCP package-data only.

### Invariants And Boundaries

- The three root runtime asset folders are canonical. Root docs remain authored documentation, not a target of this synchronizer.
- The matching MCP package-data folders are generated.
- The helper refuses to sync a target path onto its own source path.
- The helper does not sync docs, skills or user-owned installed runtime files. The packaged `tool-details.md` is separate from these three generator targets.
- **A target whose canonical source is absent is never reported in sync**, and the generated
  package-data folders are never hand-edited; the read-only `--check` is their currency proof.

### Todos

No open file-local todos.

## Evidence

### Docs References

No external documentation is needed for this repository-local helper.

No relevant external documentation found.

### Repo-Internal References

- The three canonical-to-package-data runtime targets: benchmarks, providers and system. [1]

- Digest comparison reports missing, extra, and changed files for `--check`, and refuses to call an absent canonical source in sync. [2]


- Normal sync refuses self-sync, performs copy-then-swap replacement, and rechecks targets. [3]

- Digest walk and copy use the same shared local-noise predicate. [4]

### Cross-Repo References

No sibling repository evidence is needed for this helper.

No meaningful cross-repo references found.
