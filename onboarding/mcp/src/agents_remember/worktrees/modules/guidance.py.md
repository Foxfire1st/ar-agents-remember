# mcp/src/agents_remember/worktrees/modules/guidance.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/guidance.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Builds lifecycle status payloads and typed next-operation guidance for worktree
tools.

## Code Commentary

The module converts a `WorktreeContract` plus current worktree dirtiness into
stable MCP-facing lifecycle phases such as commit approval pending, integration
pending, cleanup pending, and done. It also renders contract dataclasses into
JSON-compatible dictionaries.

`status_payload` includes a `providers` block from
`provider_async.provider_setup_status(contract)` when present: the
`worktree_status` poll surface for background provider setup — running with
currentPhase/heartbeat/seedFallback, stale on a dead heartbeat, terminal
ok / ready-with-failed-phases / failed with `retryArgs` (GitHub #53).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packet worktree status consumes the facade-exported status payload. | [status.py](agents-remember-md/mcp/src/agents_remember/worktrees/status.py) |
| MCP skill tools return the typed next-operation payloads produced here. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-06-10T07:30+02:00 — `status_payload` includes a `providers` block from `provider_async.provider_setup_status(contract)` when present: the worktree_status poll surface for background provider setup (running with currentPhase/heartbeat/seedFallback, stale on dead heartbeat, terminal ok/ready-with-failed-phases/failed with retryArgs) (GitHub #53).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
