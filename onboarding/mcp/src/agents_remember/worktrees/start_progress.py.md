# mcp/src/agents_remember/worktrees/start_progress.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/worktrees/start_progress.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-31T00:00+02:00                                 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`       |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

`START_PROGRESS_SCHEMA` (L23) is the `ar-worktree-start-progress/v1` tag that gates reads.
`start_progress_dir` (L58) anchors files under `<coordination_root>/temp/worktree-start`, and
`start_progress_path` (L62) extends it to `<repo_name>/<worktree_name>.json`.
`write_start_progress(coordination_root, enclosure, beat)` builds a camelCase payload (schema,
repo/task/worktree identity, `worktreeGroup`, `phase`, `memoryMode`, the optional `code*` fields,
`completedPhases`, `choices`, and an ISO `updatedAt`), adds `blockedReason` only when the beat
carries one, then `mkdir`s the parent and writes pretty JSON; any `OSError` is swallowed.

Since 260731-EFA-L2 its thirteen keywords are two frozen parameter objects, split along the seam
that actually exists in the data — **what the beat is about** versus **how far the start has got**:

- **`StartingEnclosure(repo_name, task_name, worktree_name, worktree_group, memory_mode,
  code_source_branch="", code_base_commit="", code_repo_path="", code_worktree="")`** — the
  contract's own front-matter facts. They are written early *precisely because* the contract that
  would normally carry them does not exist yet. Every writer builds it from the in-flight contract
  (`start._starting_enclosure`), which is why they travel as one thing.
- **`StartBeat(phase, completed_phases=(), choices=(), blocked_reason=None)`** — how far the start
  has got: the phase it is in, the phases already behind it, the choices it is waiting on, and why
  it is blocked. `blocked_reason=None` is the happy-path beat, and is what keeps `blockedReason`
  out of the payload.

The written JSON is byte-identical to the pre-split version, so `observer.snapshots` and the
Engine Room read exactly what they read before. `clear_start_progress` (L98-82)
unlinks the file with `missing_ok=True`, also swallowing `OSError`. `read_start_progress` (L106-93)
parses one file by path, returning `None` on `OSError`/`JSONDecodeError` or when the payload is not
a dict carrying the exact `START_PROGRESS_SCHEMA`.

### Invariants And Boundaries

- Lives in the worktrees layer so `start.py` writes and `observer.snapshots` reads it without
  creating an observer<->worktrees import cycle (L10-12).
- Every write is best-effort: writers catch `OSError` and return rather than propagate, because
  observability must never make a start fail (L71, L73-74, L79-82).
- Reads are schema-gated: a payload missing or mismatching `START_PROGRESS_SCHEMA` yields `None`,
  so stale/foreign files are ignored rather than rendered (L112-92).
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

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `write_start_progress` was re-signed from thirteen keywords to `(coordination_root, enclosure:
  StartingEnclosure, beat: StartBeat)`, and the two new frozen dataclasses were added. The written
  JSON payload is byte-identical, so `observer.snapshots` and the Engine Room are unaffected.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the transient start-progress module prose now names leaf `series-contract.md` files as the durable dashboard anchor rather than task-root `contract.md`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-15T19:35 — Created for slice 5e: slice 5e §5.4: transient durable progress for the pre-contract window of worktree_start (write/clear/read); lives in worktrees layer to avoid an observer<->worktrees cycle; every write best-effort. Verification metadata pinned until closeout stamps the 5e code commit.
