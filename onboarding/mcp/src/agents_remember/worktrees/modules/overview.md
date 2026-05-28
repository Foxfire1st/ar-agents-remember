# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |
| lastUpdated            | 2026-05-28T15:10:01+02:00                  |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, closeout, integration,
cleanup, and CLI argument wiring while preserving the public facade import path.

## Hot Path Summary

- `git.py` owns raw Git subprocess operations and small repository state checks.
- `guidance.py` renders lifecycle phase and typed next-operation payloads.
- `start.py`, `closeout.py`, `integrate.py`, and `cleanup.py` own the named
  C-09 lifecycle operations.
- `onboarding.py` owns closeout-time onboarding metadata and entity fingerprint
  refresh planning.
- `cli.py` keeps command-line parsing and JSON print adapters out of operation
  modules.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package is imported through the public worktree manager facade. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Focused worktree tests exercise the facade and operation payloads. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-25T20:41+02:00: Created when C-09 worktree lifecycle logic was split into focused implementation modules.
