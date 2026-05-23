# mcp/src/agents_remember/install/skills.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/install/skills.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `d445e83e7d28e3c34b15d8299d279d65ab9183b9` |
| lastVerifiedCommitDate | 2026-05-23T05:45:38+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Purpose

`skills.py` implements the MCP-owned `skills_install` service. It copies
packaged Agents Remember skills into a requested harness skill root.

## Code Commentary

### Logic

The service finds the packaged runtime skills through `source_root_from_package`.
It supports `tree` layout by copying the whole skill tree under
`agents-remember-md`, and `flat` layout by copying each named skill directory
directly under the install root.

### Invariants And Boundaries

- This service must copy skill directories; it must not create symlinks.
- `overwrite` and `archive_existing` are mutually exclusive.
- Existing non-archived/non-overwritten targets are errors so stale local skill
  copies are not silently merged.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `skills_install` is exposed as an MCP payload. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Runtime package discovery is shared with runtime install. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-05-23T13:09+02:00: Created for copy-only MCP skill installation.
