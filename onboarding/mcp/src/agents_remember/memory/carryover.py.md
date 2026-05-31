# mcp/src/agents_remember/memory/carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory/carryover.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`carryover.py` is the package-local C-11 implementation for planning and
applying branch-memory carryover after code has landed.

## Code Commentary

### Logic

The module compares old base, source branch, and official branch source changes,
classifies carryover candidates by evidence, and can copy proven onboarding into
official memory while updating metadata and the ledger. `CarryoverRequest`,
`build_plan_for_request()`, and `apply_carryover_for_request()` are the service
entry points used by MCP controllers; CLI commands remain adapters around those
functions.

### Invariants And Boundaries

- Only proven evidence tiers auto-carry.
- `evidence_for_path()` returns the strongest `exact-landed-commit` tier only
  when EVERY source-branch commit touching the path is an ancestor of the
  official ref; a single landed commit is not enough, so a later unlanded commit
  to the same path cannot be silently carried over as landed.
- Review-required paths must be selected explicitly before apply.
- The MCP facade constrains memory paths to the configured coordination root.
- MCP controllers should pass `intent_note` to the service API and should not
  route through CLI `--approved` / `--approval-note` parsing.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_carryover_plan` and `memory_carryover_apply` call this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Ledger updates are delegated to kernel memory ledger helpers. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Update History

- 2026-05-31T12:30+02:00 — `evidence_for_path()` now requires ALL source-branch commits touching a path to be ancestors of the official ref for `exact-landed-commit`, not just one (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Narrowed `plan['candidates']` to a `list` before iterating to clear a Pyright not-iterable error; behavior-preserving (commit `0549b28`).
- 2026-05-24T00:35+02:00: Updated after adding carryover request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
