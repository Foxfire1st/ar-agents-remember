# mcp/tests/test_explainer_server.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Tests the explainer’s mounted render and grade tools, their leaf binding and lock, bounded answers, publication records, and browser announcement and failure state.

## Code Commentary

- The mounted surface provides `render`, `define_category`, `remove_category` and `grade`; publication re-reads the binding under the leaf lock.


- A grade at a binding the environment has left is refused; a writer waits on the leaf's lock so neither writer loses keys.


- The browser cases hold the render boundary at its mounted surface: the announce answer names the missing part and the one sentence and begins no run; the serving path answers that announce on a browserless installation instead of raising; and the state payload carries `lastRender` and `browserNotice` read from the workspace's own records.

## Evidence





- The serving path answers announce on a browserless installation. [6]
- The page reads the last render that ended for a missing browser. [7]
- The page carries the sentence before the first fetch. [8]


- The case `test_a_grade_at_a_binding_the_environment_left_is_refused` protects a grade at a binding the environment left being refused. [4]

- The render tool description asks the seat to say the announcement before fetching and names no shell command. [5]

- The render case checks report and picture paths, full on-disk errors and a bounded reply, publication part map and coverage, revision copies, resumed successor publication and moved-binding refusal. [9]
