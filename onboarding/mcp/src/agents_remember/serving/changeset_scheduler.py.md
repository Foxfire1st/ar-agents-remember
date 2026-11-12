# mcp/src/agents_remember/serving/changeset_scheduler.py

## Governing Overview

[serving route overview](overview.md)

## Purpose

The change-set route family's own bounded read scheduler. It gives the blocking change-set read a
dedicated set of workers, a hard admission cap, a removable pending queue and a cancellation event
that the Git runner sees.

## Code Commentary

`_BoundedReads(threads=8, pending=8)` starts eight daemon workers and admits at most `threads +
pending` jobs (`:27-87`). `try_admit` refuses with `None` when the cap is reached; `submit` appends a
`_Work`; `reclaim` removes an abandoned queued job; `shutdown` cancels and releases every queued job
and lets the workers end. Each `_Work` copies the request context, creates its own `threading.Event`
and future, and runs the producer inside `cancellable_git_commands` (`:90-143`). `abandon` sets the
event, reclaims the queue entry if it is still queued, cancels the future; a running job releases its
admission slot only in `run`'s `finally`, after the producer physically ends. `_read_off_the_loop`
(`:146-169`) admits or answers 503 with `Retry-After: 1`, submits the work, polls the request's
disconnect state and returns 499 after `abandon`.

## Invariants And Boundaries

- The admission cap covers running plus pending physical jobs, not only worker threads.
- An abandoned queued job never runs; a running job keeps its slot until it ends; an abandoned read's
  admission is withdrawn by the cache's finish.
- The cancellation event is scoped to its copied request context; it cannot reach another task's Git
  child.
- The scheduler binds no task lifecycle, no memory admission and no retry policy.

## Evidence

- The production module; `changeset.py` creates it per app and returns 503/499 from it.
- `mcp/tests/test_changeset_cancellation.py` pins admission, withdrawal, reclamation, one kill owner
  and copied-context release.
