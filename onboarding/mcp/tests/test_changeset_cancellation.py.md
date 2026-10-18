# mcp/tests/test_changeset_cancellation.py

## Governing Overview

[tests overview](overview.md)

## Purpose

Pin the change-set read scheduler's cancellation, admission and reclamation properties on the actual
route family.

## Tested Boundary

The module runs the real scheduler/fixture seams. It proves that a slow read of one task does not
delay another; a disconnected read returns 499 and its Git child is gone; a queued abandoned read
never produces; over the cap the route answers an explicit 503; an abandoned successful read is never
cached; the cancellation is scoped to its copied request context and does not reach another task's
Git child; the runner has one kill owner; a read abandoned during finish admits nothing; a queued
abandoned read releases its slot at once; repeated populations bound admission and reclaim abandoned
jobs; copied request contexts are released; and a running abandoned job keeps its slot until its
worker ends. These are in-process fixture assertions, not installed throughput or a whole-suite run.

## Evidence

- The case names in the module (for example `test_a_slow_read_of_one_task_does_not_delay_anothers`,
  `test_a_disconnected_read_ends_its_git_process`, `test_the_runner_has_one_kill_owner`,
  `test_over_capacity_answers_an_explicit_refusal`,
  `test_abandoned_jobs_release_their_copied_request_contexts`).
- `changeset_scheduler.py`, `changeset.py`, `changeset_cache.py` and `kernel/git_command.py`.
