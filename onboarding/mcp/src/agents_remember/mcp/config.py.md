# mcp/src/agents_remember/mcp/config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/config.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`config.py` loads and validates the trusted MCP authority settings.

## Code Commentary

### Logic

The loader requires an absolute JSON settings path, rejects coordinator
`system/settings.json` as an authority file, rejects settings located inside the
coordinator root, defaults omitted transcript roots to `logs/mcp`, parses
configured repositories, derives default memory roots, parses optional contract
paths inside the coordinator, infers harness skill roots from harness-local
`mcp/<settings>.json` placement such as `.codex/mcp/<settings>.json`, derives
provider runtime roots under `providers/runners/<provider>/<instance>` and
provider log roots under `logs/providers/<provider>/<instance>`, and exposes
sorted allowed repo/provider ids.

### Invariants And Boundaries

- MCP settings are the authority for the server path.
- Coordinator files may teach agents what to ask for, but they do not grant MCP
  authority.
- Provider path fields are derived by the server, not repeated in settings.
- Memory settings includes must stay inside the configured code repo or memory
  repo boundaries.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server registration consumes this config object. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Config tests cover authority rejection, harness-root inference, provider derivation, and include containment. | [test_config.py](agents-remember-md/mcp/tests/test_config.py) |

## Update History

- 2026-05-29T18:35+02:00: Extracted `_parse_repository_entry` from `parse_repositories` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-28T12:32+02:00: Updated after transcript roots defaulted to `logs/mcp` and provider log roots moved under `logs/providers/`.
- 2026-05-24T09:23+02:00: Updated after config coverage switched the normal Codex harness placement from `.agents/mcp` to `.codex/mcp`.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after MCP settings became the only authority route.
