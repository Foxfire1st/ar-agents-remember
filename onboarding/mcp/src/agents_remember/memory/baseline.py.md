# mcp/src/agents_remember/memory/baseline.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory/baseline.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `d445e83e7d28e3c34b15d8299d279d65ab9183b9` |
| lastVerifiedCommitDate | 2026-05-23T05:45:38+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Purpose

`baseline.py` is the package-local C-10 implementation for inspecting and
adopting an existing external-memory onboarding baseline.

## Code Commentary

### Logic

The module keeps the old `status` and `adopt` command behavior but imports the
package resolver, drift checker, worktree git helpers, and memory ledger
directly instead of dynamically loading skill-local scripts.

### Invariants And Boundaries

- Adoption requires external topology.
- Actionable drift blocks adoption unless explicitly accepted.
- This module is invoked through typed MCP payloads, not through a coordinator
  runtime script path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_baseline_status` and `memory_baseline_adopt` call this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Ledger parsing and writing live in the kernel. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Update History

- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
