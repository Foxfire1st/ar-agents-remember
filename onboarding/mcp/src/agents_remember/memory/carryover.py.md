# mcp/src/agents_remember/memory/carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory/carryover.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`carryover.py` is the package-local C-11 implementation for planning and
applying branch-memory carryover after code has landed.

## Code Commentary

### Logic

The module compares old base, source branch, and official branch source changes,
classifies carryover candidates by evidence, and can copy proven onboarding into
official memory while updating metadata and the ledger.

### Invariants And Boundaries

- Only proven evidence tiers auto-carry.
- Review-required paths must be selected explicitly before apply.
- The MCP facade constrains memory paths to the configured coordination root.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_carryover_plan` and `memory_carryover_apply` call this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Ledger updates are delegated to kernel memory ledger helpers. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Update History

- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
