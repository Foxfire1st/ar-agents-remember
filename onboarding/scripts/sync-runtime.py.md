# scripts/sync-runtime.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-runtime.py` keeps the root canonical runtime asset folders
(`agents-md-files/`, `benchmarks/`, `providers/`, `system/`, and — since
260915-CAPS-L9 — `eve_runtime/`) synchronized with their generated MCP
package-data copies.

## Code Commentary

### Logic

The script resolves the repository root from its own path, declares the MCP
package-data root, and defines five explicit `RuntimeTarget` mappings:

- `agents-md-files/` to `mcp/src/agents_remember/package_data/runtime/agents-md-files/`
- `benchmarks/` to `mcp/src/agents_remember/package_data/benchmarks/`
- `providers/` to `mcp/src/agents_remember/package_data/runtime/providers/`
- `system/` to `mcp/src/agents_remember/package_data/runtime/system/`
- `eve_runtime/` to `mcp/src/agents_remember/package_data/runtime/eve-runtime/`

### 260915-CAPS-L9 The Fifth Target And The Two Comparison Corrections

`RuntimeTarget` gained a **per-target** `ignored_names: frozenset[str]`, because the machine-local
trees differ per canonical folder: the eve application carries `node_modules` and eve's own
`.eve`/`.output`/`.vercel` state, and none of them is authored source. **The rule travels with
the tree it applies to** — a global ignore would silently drop a same-named directory from any
other target. `ignored()` and `file_digests()` take the target's set and thread it into
`copy_ignore(names, target_ignored)`, so the digest comparison and the copy agree by
construction. Only the `eve-runtime` target declares a non-empty set, and
`test_only_the_eve_application_target_ignores_machine_local_trees` pins exactly that.

`RuntimeDiff` gained **`source_missing`**, and `in_sync` now requires its absence. Without the
flag a target whose canonical source and generated copy were *both* missing compared equal and
reported `ok`: an empty comparison is not evidence of a synced tree, and a caller who pointed the
generator at the wrong root read green rows for nothing. `diff_target` returns
`source_missing=True` before digesting, and `print_diff` names the absent canonical source.

It computes SHA-256 digests for every non-ignored file under each canonical
source and target, reports missing, extra, and changed paths, and exits non-zero
from `--check` when any generated target is stale. Normal sync mode replaces
each package-data target directory wholesale from its canonical source and then
runs the same check. `--list-targets` prints the explicit source-to-target
mapping.

### Conventions

`replace_tree` removes stale staging/retired leftovers, completes the new copy, then renames the old target aside and the staged tree into place before removing the retired tree. A copy failure before the first rename leaves the live target intact. The two renames are separate operations; this description does not claim an atomic directory exchange.

Ignore only local/generated filesystem noise: `.DS_Store`, cache directories,
`__pycache__`, and `.pyc` files — plus, **per target**, the machine-local trees that target's own
canonical folder carries (`node_modules`, `.eve`, `.output`, `.vercel`, declared only by
`eve-runtime`). Runtime asset targets are MCP package-data targets only; harness starter packages
are intentionally not included.

### Invariants And Boundaries

- The five root runtime asset folders are canonical.
- The matching MCP package-data folders are generated.
- The helper refuses to sync a target path onto its own source path.
- The helper does not sync skills, harness starter packages, docs, or user-owned
  installed runtime files.
- **A target whose canonical source is absent is never reported in sync**, and the packaged
  application mirror is generated content: it is never hand-edited, and the read-only `--check`
  is its currency proof.

### Todos

No open file-local todos.

## Evidence

### Docs References

No external documentation is needed for this repository-local helper.

No relevant external documentation found.

### Repo-Internal References

- The five explicit canonical-to-package-data runtime targets, with the per-target ignore set declared beside the tree it applies to. [1]
- Digest comparison reports missing, extra, and changed files for `--check`, and refuses to call an absent canonical source in sync. [2]
- Normal sync refuses self-sync, performs copy-then-swap replacement, and rechecks targets. [3]
- The per-target ignore set threads into both the digest walk and the copy, so comparison and copy cannot disagree. [4]

### Cross-Repo References

No sibling repository evidence is needed for this helper.

No meaningful cross-repo references found.
