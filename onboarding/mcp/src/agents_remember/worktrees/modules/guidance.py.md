# mcp/src/agents_remember/worktrees/modules/guidance.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/guidance.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:56+02:00     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46` |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
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

`status_payload` also includes a `freshness` block from `base_freshness`
(issue #54): a deliberately fetch-free comparison of the contract's recorded
base commits against the current LOCAL source branch tips
(`baseBehindSource` counts per side). Local source branches move mid-task when
a parallel cycle lands (PR merge ff's code main, carryover advances memory
main); when behind, the block carries a `syncHint` recommending
`worktree_sync` with a dry-run preview. No network in this path — it must stay
safe for the provider-setup polling loop; the fetching freshness checks live in
`context_packet` (`include_freshness`), the start preflight, and
`worktree_sync` itself.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Context packet worktree status consumes the facade-exported status payload. | [status.py](agents-remember/mcp/src/agents_remember/worktrees/status.py) |
| MCP skill tools return the typed next-operation payloads produced here. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-06-10T09:56+02:00 — Issue #54 sub-task D: added `base_freshness` (fetch-free recorded-base vs local source tip counts with a `worktree_sync` `syncHint`) and wired it into `status_payload` as `freshness`.
- 2026-06-10T07:30+02:00 — `status_payload` includes a `providers` block from `provider_async.provider_setup_status(contract)` when present: the worktree_status poll surface for background provider setup (running with currentPhase/heartbeat/seedFallback, stale on dead heartbeat, terminal ok/ready-with-failed-phases/failed with retryArgs) (GitHub #53).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
