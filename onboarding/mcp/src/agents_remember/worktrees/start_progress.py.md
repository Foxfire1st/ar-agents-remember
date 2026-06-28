# mcp/src/agents_remember/worktrees/start_progress.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/worktrees/start_progress.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T19:35                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                           |

## Governing Overview

[worktrees overview](../../../overview.md)

## Purpose

Writes and clears a small, transient "start progress" file for the pre-contract window of
`worktree_start` (slice 5e, §5.4). A start can block on external memory, providers, or a stale
base *before* a `contract.md` is written, leaving the Engine Room's enclosure surface (which reads
contracts) blind to that gated start. This module records each blocked early return and clears it
once the contract supersedes it, so the enclosure-centered Engine Room process map can show a start
that is stuck before it ever produces a contract.

## Code Commentary

### Logic

`START_PROGRESS_SCHEMA` (L22) is the `ar-worktree-start-progress/v1` tag that gates reads.
`start_progress_dir` (L25) anchors files under `<coordination_root>/temp/worktree-start`, and
`start_progress_path` (L29) extends it to `<repo_name>/<worktree_name>.json`.
`write_start_progress` (L33-74) builds a camelCase payload (schema, repo/task/worktree identity,
`worktreeGroup`, `phase`, `memoryMode`, the optional `code*` fields, `completedPhases`, `choices`,
and an ISO `updatedAt`), adds `blockedReason` only when one is given (L67-68), then `mkdir`s the
parent and writes pretty JSON; any `OSError` is swallowed (L73-74). `clear_start_progress` (L77-82)
unlinks the file with `missing_ok=True`, also swallowing `OSError`. `read_start_progress` (L85-93)
parses one file by path, returning `None` on `OSError`/`JSONDecodeError` or when the payload is not
a dict carrying the exact `START_PROGRESS_SCHEMA`.

### Invariants And Boundaries

- Lives in the worktrees layer so `start.py` writes and `observer.snapshots` reads it without
  creating an observer<->worktrees import cycle (L10-12).
- Every write is best-effort: writers catch `OSError` and return rather than propagate, because
  observability must never make a start fail (L50, L73-74, L79-82).
- Reads are schema-gated: a payload missing or mismatching `START_PROGRESS_SCHEMA` yields `None`,
  so stale/foreign files are ignored rather than rendered (L91-92).
- The file is transient: it exists only while a start is pre-contract and is cleared once the
  contract lands.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Schema tag gating reads | L22, L91 | [start_progress.py](start_progress.py) |
| Path layout under `temp/worktree-start/<repo>/<worktree>.json` | L25-L30 | [start_progress.py](start_progress.py) |
| Best-effort write that never raises | L33-L74 | [start_progress.py](start_progress.py) |
| `blockedReason` only emitted when present | L67-L68 | [start_progress.py](start_progress.py) |
| Clear on contract supersession | L77-L82 | [start_progress.py](start_progress.py) |
| Schema-gated read returning `None` on miss | L85-L93 | [start_progress.py](start_progress.py) |
| Layer placement avoids observer<->worktrees cycle | L10-L12 | [start_progress.py](start_progress.py) |

## Series-Contract Notes

Start-progress remains the transient pre-contract surface, but the durable endpoint it waits for is now the leaf `series-contract.md` enclosure file.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the transient start-progress module prose now names leaf `series-contract.md` files as the durable dashboard anchor rather than task-root `contract.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-15T19:35 — Created for slice 5e: slice 5e §5.4: transient durable progress for the pre-contract window of worktree_start (write/clear/read); lives in worktrees layer to avoid an observer<->worktrees cycle; every write best-effort. Verification metadata pinned until closeout stamps the 5e code commit.
