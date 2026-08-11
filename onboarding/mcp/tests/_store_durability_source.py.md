# mcp/tests/_store_durability_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_store_durability_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T21:54+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Bounded source-tree pinning support for the cross-process durability harness. This module owns the
reproducible base-commit archive, the behavior-neutral supervisor-to-agent-notifier compatibility
shim for that historical tree, and the fresh-interpreter runner. The executable harness remains
`_store_durability.py`; extracting these mechanics keeps both files below the repository's
1,200-line source limit without changing the public test-helper surface.

## Code Commentary

### Logic

`BASE_COMMIT` and `REPO_ROOT` identify the historical source tree and the repository from which it
is archived (cit:([`BASE_COMMIT`, `REPO_ROOT`], mcp/tests/_store_durability_source.py:14-15)).
`extract_base_commit_tree` uses `git archive` plus the system `tar`, then applies the rename shim to
the extracted package only; it never creates a nested worktree or mutates the live source
(cit:([`extract_base_commit_tree`], mcp/tests/_store_durability_source.py:79-105)).

The rename shim maps the historical supervisor module paths and identifiers to their current
agent-notifier names so the current harness can import the pinned implementations without changing
their store behavior (cit:([`_RENAMED_SOURCE_FILES`, `_apply_rename_shim_to_base_tree`], mcp/tests/_store_durability_source.py:21-38; mcp/tests/_store_durability_source.py:41-76)).

`run_against_source` writes a JSON configuration, starts a fresh interpreter with `PYTHONPATH`
pinned to the requested source root, and reads the JSON result. `HARNESS_PATH` deliberately points
back to `_store_durability.py`, which retains `_require_source_root`, `main`, all adapters, and the
script entry point (cit:([`HARNESS_PATH`], mcp/tests/_store_durability_source.py:16-16); cit:([`run_against_source`], mcp/tests/_store_durability_source.py:108-132)).

### Conventions

The source-pinning functions are imported and re-exported by `_store_durability.py`, preserving the
existing imports used by both durability contract suites. Private rename machinery stays in this
module because it exists solely to make the historical archive loadable by the current driver.

### Invariants And Boundaries

- Archive the pinned commit; never add a nested Git worktree for a measurement.
- Apply compatibility renames only inside the extracted archive, never to the live checkout.
- Keep `HARNESS_PATH` pointed at `_store_durability.py`; this helper prepares and launches the
  experiment but is not its executable entry point.
- Pin `PYTHONPATH` to the selected source tree and retain the harness-side import guard, so a
  measurement cannot silently run against installed or live code.
- Preserve the public helper signatures imported by the contract suites.

### Todos

None.

## Docs References

No external domain documentation governs this test helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external documentation was required. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The executable durability harness imports both source-pinning helpers from this bounded sibling. | "from _store_durability_source import extract_base_commit_tree, run_against_source" | mcp/tests/_store_durability.py:53-53 |
| The harness preserves its public helper surface by listing both imported names in `__all__`. | "    \"extract_base_commit_tree\","; "    \"run_against_source\"," | mcp/tests/_store_durability.py:104-105 |
| The executable harness retains the source-root guard and owns `main`; this sibling only prepares and launches that entry point. | `_require_source_root`; `main` | mcp/tests/_store_durability.py:1112-1120; mcp/tests/_store_durability.py:1123-1136 |
| The control-plane contract imports both public helpers to prove the defect against the archived base tree. | "from _store_durability import (" | mcp/tests/test_controlplane_store_durability.py:42-52 |
| The provider contract imports the same helpers so both store families use one pinned-source mechanism. | "from _store_durability import (" | mcp/tests/test_provider_store_durability.py:72-79 |

## Cross-Repo References

No meaningful cross-repository references: the archive and subprocess remain inside the
agents-remember repository and its test tree.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference was found. | — | — |

## Update History

- 2026-08-09T21:54+02:00 — 260713-TES master integration repair: created this one-to-one card
  with the bounded source-pinning helper split. The split preserves the harness API and behavior
  while clearing the repository's 1,200-line source limit; closeout owns the first verification
  stamp.
