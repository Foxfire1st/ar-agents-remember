# test_config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_config.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T18:05+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_config.py` verifies MCP authority settings parsing and derived runtime
paths.

## Code Commentary

### Logic

The tests create temporary MCP settings files and assert that config loading
rejects relative or missing paths, rejects coordinator `system/settings.json`,
rejects MCP settings inside the coordinator root, derives allowed repo/provider
ids, derives transcript and provider data roots, infers `.agents/skills` from a
`.agents/mcp` registration path, honors explicit `harnessSkillRoot`, keeps
contract paths inside the coordinator, rejects memory settings includes outside
repo boundaries, and rejects provider path fields that should be server-derived.

### Invariants And Boundaries

These tests protect the MCP authority boundary: settings live outside the
coordinator, path-rich provider settings are not duplicated, and caller-provided
include paths cannot escape configured repo/memory roots.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tested loader lives in MCP config. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-05-23T18:05+02:00: Created during direct closeout prep for MCP config coverage.
