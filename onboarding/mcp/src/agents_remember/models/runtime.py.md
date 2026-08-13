# mcp/src/agents_remember/models/runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00     |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`runtime.py` defines response contracts for runtime installation and resolved
coordination context tools.

## Code Commentary

`RuntimeInstallResponse` remains flexible because install reports include
summary and message blocks from installer services; since 2.5.1 it also
declares an optional `reportPath` — the full install detail (watcher rebind
runs, compose renders, transcripts) is filed under `temp/tool-reports/` while
the inline payload keeps counts and a compact rebind digest.
`ResolveContextResponse` uses a strict tool envelope and carries the resolved
context dictionary.

## Invariants And Boundaries

- Runtime install response shape is modeled, but installer-specific summary
  details remain flexible for now.
- Resolver output remains authoritative context data from the resolver service;
  path authority still comes from MCP settings.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime install application entry point produces the installer response payload. | `run_runtime_install` | mcp/src/agents_remember/application/runtime/install.py:13-17 |
| Coordination application entry point exposes resolver output through MCP. | `resolve_context_tool` | mcp/src/agents_remember/application/coordination_tools.py:20-50 |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 2 citation claims; scoped result 0 findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-10T05:30+02:00 — `RuntimeInstallResponse` gains a documented optional `reportPath` field for the S4 response-budget compaction (2.5.1).
- 2026-05-28T19:52+02:00: Created for runtime and resolver response contracts.
