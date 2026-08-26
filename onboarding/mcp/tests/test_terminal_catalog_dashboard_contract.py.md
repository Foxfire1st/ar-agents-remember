# mcp/tests/test_terminal_catalog_dashboard_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_catalog_dashboard_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T22:27+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins the dashboard's declared terminal-catalog interface bidirectionally to the server response
model, including private diagnostic fields such as the dispatch-brief receipt.

## Code Commentary

### Logic

`_dashboard_catalog_fields` parses the `TerminalCatalogRow` body and extracts every declared wire
name. The test compares that set in both directions with the aliases of
`TerminalCatalogEntryWire` and pins the nonempty 66-field count so an empty parser result cannot
pass vacuously.

### Conventions

This is a source-contract check, not a browser behavior test. It reads the worktree TypeScript file
directly and treats Pydantic aliases as the server wire vocabulary.

### Invariants And Boundaries

- A field added or removed on either side fails until the other side agrees.
- The fixed count prevents two empty or accidentally truncated sets from appearing equal.
- Equality proves shape parity only; it does not grant addressing authority to diagnostic fields.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is a repository-owned wire-parity test.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parser extracts field names only from the declared dashboard catalog interface. | `_dashboard_catalog_fields` | mcp/tests/test_terminal_catalog_dashboard_contract.py:14-28 |
| Server and dashboard field sets are equal in both directions and pinned at 66. | `test_dashboard_full_catalog_mirror_matches_server_aliases_bidirectionally` | mcp/tests/test_terminal_catalog_dashboard_contract.py:31-37 |

## Cross-Repo References

No cross-repository dependency governs this test module.

## Update History

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: created for Python-to-TypeScript catalog wire
  parity. Verification remains closeout-owned.
