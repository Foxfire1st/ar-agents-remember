# mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T08:40+02:00 |
| lastVerifiedCommitHash |  `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b`|
| lastVerifiedCommitDate |  2026-08-18T03:31:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

This module runs one pinned Dagger quality graph in a clean Ubuntu/Playwright container and publishes its latest reports into the worktree enclosure. It replaces ad-hoc nested-Docker execution with one explicit, observable executor selected by settings.

## Code Commentary

### Logic

`run_clean_quality` validates mode and candidate roots, prepares an isolated sandbox containing the exact staged candidate and required Git ancestry, invokes the pinned Dagger module while streaming progress, and publishes only recognized reports. It parses the exported result rather than trusting the Dagger CLI transport exit code alone.

`_publish_reports` now records a caller-bound attestation in the report manifest; `published_quality_attestation` reads it back for crash-safe recovery.

### Conventions

The Dagger, Codex, and base image versions are constants. The scratch sandbox is self-overwriting inside the enclosure and is separate from durable reports.

### Invariants And Boundaries

- No Docker socket or nested Docker daemon is mounted into the test container.
- Invalid/missing exported status fails closed; local quality is not a fallback.
- Candidate Git identity must match before and after sandbox materialization.
- Reports are atomically replaced, not accumulated per run.
- Report promotion uses the kernel-owned `atomic_replace` primitive after copying to the target's
  sibling temporary file; this keeps replacement semantics on the shared platform boundary.

### Todos

None.

## Docs References

The repository source pins the toolchain; no external Domain Documentation source is configured in memory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tool and image versions are repository-owned pinned inputs. | `DAGGER_VERSION`; `CODEX_VERSION`; `PLAYWRIGHT_IMAGE` | mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py:23-30 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The executor validates, materializes, streams, parses, and publishes one clean quality run. | `run_clean_quality` | mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py:36-167 |
| Helper boundaries preserve Git identity, atomic report publication, and native Dagger resolution. | `_publish_reports`; `_resolve_dagger` | mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py:207-273; mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py:468-469 |

## Cross-Repo References

The only external boundary is the pinned container/tool runtime, not a sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| Dagger is explicitly resolved through the native subprocess boundary. | `_stream_dagger`; `_resolve_dagger` | mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py:364-421; mcp/src/agents_remember/worktrees/modules/clean_quality_executor.py:468-469 |

## Update History
- 2026-08-17T12:30+02:00 — 260815-DAG-L5: report publication now carries an attestation; added `published_quality_attestation`. Verification remains closeout-owned.

- 2026-08-14T06:36+02:00 — L23 final candidate review: the Dagger executor starts a fresh attempt,
  makes two report projections share one authoritative result, bounds live output, prunes stale
  predecessor reports, and fails closed on status reads; no local runner remains.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: recorded that report promotion now routes through `kernel.atomic_write.atomic_replace` instead of calling `os.replace` directly. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23's pinned, observable Dagger quality executor; verification provenance remains closeout-owned.
