# scripts/sync-runtime.py

| Field                  | Value                         |
| ---------------------- | ----------------------------- |
| repository             | agents-remember             |
| path                   | `scripts/sync-runtime.py`      |
| doc_type               | `file-level-onboarding`        |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253`             |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../overview.md`                              |

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

## Docs References

No external documentation is needed for this repository-local helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five explicit canonical-to-package-data runtime targets, with the per-target ignore set declared beside the tree it applies to. | `TARGETS`; `RuntimeTarget` | scripts/sync-runtime.py:61-78; scripts/sync-runtime.py:27-41 |
| Digest comparison reports missing, extra, and changed files for `--check`, and refuses to call an absent canonical source in sync. | `diff_target`; `RuntimeDiff`; `print_diff` | scripts/sync-runtime.py:137-153; scripts/sync-runtime.py:44-58; scripts/sync-runtime.py:204-219 |
| Normal sync refuses self-sync, performs copy-then-swap replacement, and rechecks targets. | `sync_target`; `replace_tree`; `sync_targets` | scripts/sync-runtime.py:162-167; scripts/sync-runtime.py:168-203; scripts/sync-runtime.py:236-257 |
| The per-target ignore set threads into both the digest walk and the copy, so comparison and copy cannot disagree. | `ignored`; `file_digests`; `copy_ignore` | scripts/sync-runtime.py:100-106; scripts/sync-runtime.py:123-136; scripts/sync-runtime.py:154-161 |

## Cross-Repo References

No sibling repository evidence is needed for this helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: documented the fifth target (`eve_runtime/` →
  `package_data/runtime/eve-runtime/`) with its **per-target** ignore set, the `source_missing`
  correction that stops an absent canonical source from reading `ok`, and the agreement between
  the digest walk and the copy that the same set now guarantees. Repointed the three reference
  rows at their current lines and added a row for the ignore plumbing. This candidate is
  **uncommitted**, so verification metadata remains closeout-owned; the real stamp is the
  closeout's.
- 2026-09-06T22:07:53+00:00 — Reconciled copy-before-rename preservation against current replace_tree and retired sync test knowledge. Historical entries and verification pins remain unchanged.
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-06-10T00:40+02:00 — `sync_target` now uses crash-safe `replace_tree` (copy to `<target>.ar-sync-new`, rename live target aside, swap in, then remove the old tree; stale staging/retired leftovers are cleaned on re-run), and `extended_length()` applies the Windows `\\?\` prefix so syncs and `--check` walks work past 260-char paths even with `LongPathsEnabled=0`. Replaces the delete-then-copy that gutted `package_data` when a long-path crash hit mid-delete (2026-06-09 incident).
- 2026-06-08T11:53+02:00: Created onboarding for the new runtime asset synchronization helper. Verification metadata is pending until the code commit exists.
