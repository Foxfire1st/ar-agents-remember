# mcp/src/agents_remember/providers/cgc/context/materialize.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/providers/cgc/context/materialize.py`   |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-07-03T01:55+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`                                                        |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `CgcRuntimeLayout` definition and construction. | `CgcRuntimeLayout` | mcp/src/agents_remember/providers/cgc/context/core.py:36-126 |
| Ignore/requirements constants and `.gitignore` reader. | `read_gitignore_patterns` | mcp/src/agents_remember/providers/cgc/context/constants.py:16-21; mcp/src/agents_remember/providers/cgc/context/constants.py:79-90 |

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 2 citation findings. Re-anchored the
  constants/reader row to `read_gitignore_patterns` with the exact requirements and ignore-text spans
  (constants.py:16-21; 50-90). Scoped recheck clean.
- 2026-07-03T01:55+02:00 — L12: ensure_cgc_runtime_layout also materializes the enriched .cgcignore into run/home/.codegraphcontext/global/.cgcignore (byte-identical), closing the dead-config gap where the watch context read cgc's auto-created plain defaults instead.
- 2026-05-29T18:35+02:00: Created when `ensure_cgc_runtime_layout` and the runtime file/dir writers were extracted from `core.py` (commit `01f503d`).
