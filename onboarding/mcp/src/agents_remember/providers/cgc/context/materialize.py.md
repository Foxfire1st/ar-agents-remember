# mcp/src/agents_remember/providers/cgc/context/materialize.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Materialize a resolved `CgcRuntimeLayout` onto disk: create the runtime
directories and write the default CGC config files. Since L12 the enriched
`.cgcignore` (defaults + folded repo .gitignore + per-repo managed exclusions) is
written TWICE on purpose: at the runtime root AND into the HOME-scoped
`global/.cgcignore` — the file the live `cgc watch` context actually resolves;
without the second copy the enrichment never reached the watcher.

## Code Commentary

### Logic

`ensure_cgc_runtime_layout(layout)` makes every directory in
`_cgc_runtime_directories(layout)`, then writes `requirements.txt` (if missing),
`.cgcignore` (`_cgcignore_text`), the `database: falkordb-remote` config, and the
`.env` file (`_cgc_env_text`). `_cgcignore_text` seeds from `DEFAULT_CGCIGNORE`,
then appends source `.gitignore` patterns and repo-specific managed exclusions.
`_cgc_env_text` renders `layout.env()` minus `CGC_ENV_FILE_EXCLUDED_KEYS`.

### Invariants And Boundaries

- Operates only on an already-resolved `CgcRuntimeLayout` (imported from
  `core`); it does not build the layout.
- Was extracted from `core.py` (commit `01f503d`) so layout definition,
  materialization, and cleanup are separate responsibilities.

## Evidence

### Repo-Internal References

- `CgcRuntimeLayout` definition and construction. [1]
- Ignore/requirements constants and `.gitignore` reader. [2]
