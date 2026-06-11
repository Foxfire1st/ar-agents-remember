# mcp/src/agents_remember/providers/cgc/context/materialize.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/providers/cgc/context/materialize.py`   |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2`                                                        |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                                                    |

## Purpose

Materialize a resolved `CgcRuntimeLayout` onto disk: create the runtime
directories and write the default CGC config files.

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

| Finding | Source Path |
| --- | --- |
| `CgcRuntimeLayout` definition and construction. | [core.py](agents-remember/mcp/src/agents_remember/providers/cgc/context/core.py) |
| Ignore/requirements constants and `.gitignore` reader. | [constants.py](agents-remember/mcp/src/agents_remember/providers/cgc/context/constants.py) |

## Update History

- 2026-05-29T18:35+02:00: Created when `ensure_cgc_runtime_layout` and the runtime file/dir writers were extracted from `core.py` (commit `01f503d`).
