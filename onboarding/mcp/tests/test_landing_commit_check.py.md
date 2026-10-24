# mcp/tests/test_landing_commit_check.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

A landing passes the repository's commit check (MIK-R152): the hook Git would run judges the staged tree, a
failing hook refuses the publication and keeps state, a hook that cannot run is a refusal rather than a pass, and
the pass fact rides the commit so a later route can trust it. Answer and text cases keep the refusal small and
the shipped texts current.

## Code Commentary

### Logic

`_init()`, `_hook()`, `_stage()`, `_write_tree()` and `_status()` build a scratch repository with a real hook,
and `PassingHookTests`/`FailingHookTests`/`UnrunnableHookTests` drive the check through the routes that publish.

- **Passing.** `test_a_passing_hook_passes_naming_hook_log_and_time` names the log and the time,
  `test_each_repository_runs_its_own_hook` keeps code and memory repositories on their own hook, and
  `test_no_hook_passes_saying_so` lands a repository without a hook as before.
- **Failing.** A failing hook refuses while keeping state; `test_a_hook_that_rewrites_a_tracked_file_refuses_naming_it`
  requires the judged tree to be the commit's tree, and
  `test_a_hook_that_stages_a_change_refuses_and_gives_the_index_back` refuses when the hook's run changed the
  index and returns the index.
- **Unrunnable.** A non-executable hook file, a missing interpreter, a hanging hook and the settings bound are
  each a named refusal (`test_the_settings_bound_governs_the_run`), and an unrecoverable isolation stash is named
  and never touched.
- **Trailer.** `test_the_trailer_round_trips_with_last_wins` and `test_the_published_commit_carries_the_fact`
  put the pass fact on the commit and let the last one win.
- **Route coverage.** `RouteCoverageTests` keeps every route on the check: the provisional path runs the hook
  before the move, integration trusts a commit carrying the fact and checks one without it, and a failing
  candidate without a fact never moves the master line.
- **Answer and texts.** `AnswerAndTextTests` keeps the answer to result, failing step and log path. Its text case
  reads `closeout_texts()`: the canonical `w-02-light-task-workflow/workflows/closeout.md` and its single packaged
  serving copy. The generator check invokes `scripts/sync-skills.py --check` with the current Python interpreter.
  The cases also protect the no-skip policy, commit-tree census and baseline-adoption check.
- **Round-one findings.** `RoundOneFindingTests` covers closed pipe readers, a group-escaped holder that ignores
  `TERM`, a tracked rewrite after the pass, a descendant that holds the pipe, whole streaming of hook output with
  an elapsed footer, log reclamation to the newest twenty, and `stdin` readers getting `EOF`.

### Conventions

Hooks are real scripts in a scratch repository, so Git's own rules — executable bit, interpreter, exit status —
decide the outcome rather than a mocked runner.

### Invariants And Boundaries

- The tree the hook judged is the tree that is committed.
- A hook that cannot run refuses; it never counts as a pass.

## Evidence

- A landing passes the repository's commit check through every publishing route. [1]

- FailingHookTests: qualified source contract — `FailingHookTests` in mcp/tests/test_landing_commit_check.py. [2]
- UnrunnableHookTests: qualified source contract — `UnrunnableHookTests` in mcp/tests/test_landing_commit_check.py. [3]
- StashRecoveryTests: qualified source contract — `StashRecoveryTests` in mcp/tests/test_landing_commit_check.py. [4]
- TrailerFactTests: qualified source contract — `TrailerFactTests` in mcp/tests/test_landing_commit_check.py. [5]
- RoundOneFindingTests: qualified source contract — `RoundOneFindingTests` in mcp/tests/test_landing_commit_check.py. [6]
- Remaining-route fixtures protect exact-tree ordinary/direct publication refusal and pass facts — `RemainingRouteProductionTests` in mcp/tests/test_landing_commit_check.py. [7]

- AnswerAndTextTests owns the skill-sync subprocess using the current interpreter; this is source attribution, not execution. [8]

- The landing text case reads the transferred w-02 closeout workflow through the shared canonical/package helper, and its generator check uses the current interpreter; this is source attribution, not a fresh run. [9]
