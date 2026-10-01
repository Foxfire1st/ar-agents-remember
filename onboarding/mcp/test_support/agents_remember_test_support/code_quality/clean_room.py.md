# mcp/test_support/agents_remember_test_support/code_quality/clean_room.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

This is the narrow CLI boundary for the pinned Dagger clean-Linux quality executor. Since CCR-R22@v1 (L22, commit `685f83c44055`) it also requires `--repository-id` and `--certification-profile` arguments and forwards them as `CleanQualityRequest.repository_id`/`profile_reference`, so the CLI runs the same repository-profile admission as the lifecycle. It accepts the candidate checkout, enclosure, repository identity, profile reference, targeted/full mode, diff base, and optional memory cap, then returns the executor's real exit status without a local-container fallback.

## Code Commentary

### Logic

`build_parser` defines the public arguments (now including the two required repository-identity/profile flags). `main` resolves paths, builds `CleanQualityRequest` with `repository_id` and `profile_reference`, runs the canonical executor, streams its transcript, and reports invalid environment or request state as a refusal.

### Conventions

The command delegates all orchestration and reporting to `clean_quality_executor`; it does not duplicate Dagger policy.

### Invariants And Boundaries

- Executor failures remain failures; there is no silent host-quality fallback.
- An omitted memory cap means host-managed capacity, not an inferred limit.
- The exit code is the clean-room proof result.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured in `system/sources.md`.

No configured external documentation is cited by this internal adapter.

### Repo-Internal References

- The parser and main routine preserve the exact executor inputs and exit status. [1]

### Cross-Repo References

No cross-repository contract is owned here.

- The adapter is confined to one resolved code worktree and enclosure. [2]
