# mcp/src/agents_remember/code_quality/clean_room.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/clean_room.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

This is the narrow CLI boundary for the pinned Dagger clean-Linux quality executor. It accepts only the candidate checkout, enclosure, targeted/full mode, diff base, and optional memory cap, then returns the executor's real exit status without a local-container fallback.

## Code Commentary

### Logic

`build_parser` defines the public arguments. `main` resolves paths, builds `CleanQualityRequest`, runs the canonical executor, streams its transcript, and reports invalid environment or request state as a refusal.

### Conventions

The command delegates all orchestration and reporting to `clean_quality_executor`; it does not duplicate Dagger policy.

### Invariants And Boundaries

- Executor failures remain failures; there is no silent host-quality fallback.
- An omitted memory cap means host-managed capacity, not an inferred limit.
- The exit code is the clean-room proof result.

### Todos

None.

## Docs References

No external Domain Documentation source is configured in `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external documentation is cited by this internal adapter. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parser and main routine preserve the exact executor inputs and exit status. | `main` | mcp/src/agents_remember/code_quality/clean_room.py:15-42 |

## Cross-Repo References

No cross-repository contract is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter is confined to one resolved code worktree and enclosure. | `main` | mcp/src/agents_remember/code_quality/clean_room.py:25-42 |

## Update History

- 2026-08-12T15:19+02:00 — Created for L23's clean-Linux Dagger quality entry point; verification provenance remains closeout-owned.
