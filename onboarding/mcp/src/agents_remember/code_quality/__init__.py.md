# mcp/src/agents_remember/code_quality/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T06:05+02:00                     |
| lastVerifiedCommitHash | `98af161a6c8d77f7dfc30457c9f6ab1c20e411ab`                      |
| lastVerifiedCommitDate | 2026-05-24T06:49:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`__init__.py` marks `agents_remember.code_quality` as the package-local domain
for source-development quality helpers.

## Code Commentary

### Logic

The package currently exposes helper modules by explicit import. It does not
register MCP tools or runtime behavior.

### Invariants And Boundaries

- Code quality helpers are source-development utilities, not installed
  coordinator runtime behavior.
- Runtime MCP dependencies should not grow just because a development helper
  exists in this package.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CRAP-Calculator lives in this package. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| The source quality suite wrapper lives in this package. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |

## Update History

- 2026-05-24T06:30+02:00: Updated after adding the source quality suite wrapper.
- 2026-05-24T06:05+02:00: Created for the code quality helper package.
