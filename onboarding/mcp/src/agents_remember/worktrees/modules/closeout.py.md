# mcp/src/agents_remember/worktrees/modules/closeout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree and direct closeout preview/apply behavior.

## Code Commentary

Closeout validates source branch positions and explicit commit approval, commits
code first, refreshes onboarding metadata, route overview metadata, generated
route indexes, and entity fingerprints to that new code commit, runs
`memory_quality_check`, commits memory content only after the quality gate is
clean, updates the external memory ledger, and returns the closeout payload.
Direct closeout applies the same ordering to the current source branches without
task worktrees. Worktree closeout uses the code worktree as the source of truth
for drift and fingerprint checks after the worktree code commit exists.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Ledger updates use the kernel memory ledger parser and renderer. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| Closeout refresh helpers provide sidecar metadata, route overview metadata, route index, and entity fingerprint updates before the memory commit. | [onboarding.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/onboarding.py) |
| Worktree tests cover dry-run previews, approval notes, missing onboarding blocking, route overview/index refresh, memory quality gating, and direct closeout ledger updates. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-29T18:35+02:00: Typed route-index/memory-quality dicts as `dict[str, Any]`, `validate_direct_external_context` -> `MemoryLedger`; extracted `_refresh_plans_have_work` and `_format_memory_quality_finding` to reduce preview/failure-message complexity; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-28T15:24+02:00: Updated after closeout began enforcing route overview/index refresh plus a clean memory quality gate before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
