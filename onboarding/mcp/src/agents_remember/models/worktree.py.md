# mcp/src/agents_remember/models/worktree.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/worktree.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0` |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree.py` defines context-packet worktree summaries and public worktree
tool response envelopes.

## Code Commentary

`WorktreeSummary` is strict and uses literal state fields for known C-09
lifecycle values such as workflow kind, memory mode, human review status,
closeout status, integration status, phase, next operation, and next tool. The
command response models remain flexible because worktree service results can
carry operation-specific planning and closeout fields.

## Invariants And Boundaries

- `WorktreeSummary` is the stable context-facing shape.
- Worktree command payloads may remain flexible while the service API is still
  carrying operation-specific result blocks.
- Do not reintroduce raw shell command strings into context-packet next hints.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Read-only worktree status projects worktree-manager payloads into the context summary shape. | [status.py](agents-remember-md/mcp/src/agents_remember/worktrees/status.py) |
| Public worktree MCP controllers delegate to the package worktree manager. | [worktree_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/worktree_tools.py) |

## Update History

- 2026-06-01T20:45+02:00 — `CleanupStatus` gained the `abandoned` literal and a `WorktreeAbandonResponse` model was added for the discard-without-integration tool.
- 2026-05-28T19:52+02:00: Created after worktree context summaries gained typed Pydantic literal fields.
