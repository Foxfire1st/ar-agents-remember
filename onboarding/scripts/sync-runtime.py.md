# scripts/sync-runtime.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-runtime.py` keeps the four canonical runtime asset folders (`agents-md-files/`, `benchmarks/`, `providers/`, `system/`) synchronized with their generated MCP package-data copies. The product-owned `eve_runtime/` target and package mirror are removed.

## Code Commentary

### Logic

The script resolves the repository root from its own path, declares the MCP
package-data root, and defines four explicit `RuntimeTarget` mappings:

- `agents-md-files/` to `mcp/src/agents_remember/package_data/runtime/agents-md-files/`
- `benchmarks/` to `mcp/src/agents_remember/package_data/benchmarks/`
- `providers/` to `mcp/src/agents_remember/package_data/runtime/providers/`
- `system/` to `mcp/src/agents_remember/package_data/runtime/system/`


### Comparison boundaries

`RuntimeTarget` now carries label/source/path only; the Eve-specific `ignored_names` field and its propagation through digest/copy are gone. Comparison and copy use the same global local-noise predicate; there is no special application target to ignore machine-local Eve directories.

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

Ignore local/generated filesystem noise: `.DS_Store`, cache directories, `__pycache__` and `.pyc` files through the shared predicate. The removed Eve target no longer supplies special ignore names. Runtime targets are MCP package-data only; harness starter packages remain separate.

### Invariants And Boundaries

- The four retained root runtime asset folders are canonical. Root docs remain authored documentation, not a target of this synchronizer.
- The matching MCP package-data folders are generated.
- The helper refuses to sync a target path onto its own source path.
- The helper does not sync docs, skills, harness starter packages or user-owned installed runtime files. The unowned added documentation mirrors were removed; retained packaged tool-details.md is separate from these four generator targets.
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


- The four retained canonical-to-package-data runtime targets; no product-owned Eve target remains. [1]


- Digest comparison reports missing, extra, and changed files for `--check`, and refuses to call an absent canonical source in sync. [2]


- Normal sync refuses self-sync, performs copy-then-swap replacement, and rechecks targets. [3]


- Digest walk and copy use the same shared local-noise predicate; the per-target ignore API is removed. [4]


### Cross-Repo References

No sibling repository evidence is needed for this helper.

No meaningful cross-repo references found.

## Preserved incoming L109 source witness

The incoming whole-source witness is retained at its earlier source epoch, not proof that the removed fifth Eve target or per-target ignore API survives this composition.


- Historical incoming L109 declaration evidence: Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred. [5]
