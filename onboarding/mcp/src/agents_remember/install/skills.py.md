# mcp/src/agents_remember/install/skills.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/install/skills.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T17:34+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8` |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`skills.py` implements the MCP-owned `skills_install` service. It copies
packaged Agents Remember skills into the configured harness skill root.

## Code Commentary

### Logic

The service finds the packaged runtime skills through `source_root_from_package`.
It supports `tree` layout by copying the whole skill tree under
`agents-remember-md`, and `flat` layout by copying each named skill directory
directly under the install root. Existing targets are either archived or
replaced depending on the request. Replacement handles normal directories, file
links, directory symlinks, and Windows junction/reparse-point directories so
legacy symlink installs can be migrated to the copy-only layout.

### Invariants And Boundaries

- This service must copy skill directories; it must not create symlinks.
- `overwrite` and `archive_existing` are mutually exclusive.
- Existing non-archived/non-overwritten targets are errors so stale local skill
  copies are not silently merged.
- Replacing an old symlink or junction target must remove only the link itself,
  not the linked target tree.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `skills_install` is exposed as an MCP payload. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Runtime package discovery is shared with runtime install. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| MCP tests cover replacing a legacy symlink skill tree with a copied tree. | [test_tools.py](agents-remember-md/mcp/tests/test_tools.py) |

## Update History

- 2026-05-23T17:34+02:00: Documented overwrite handling for legacy symlink and Windows junction skill installs.
- 2026-05-23T13:09+02:00: Created for copy-only MCP skill installation.
