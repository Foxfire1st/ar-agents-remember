# mcp/tests/test_knowledge_reopen.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Checks append-only leaf attempt histories and the exact-tree memory gate on closeout and recovery.

## Code Commentary

A reopened leaf writes its next attempt without reopening a closed history file; the latest row about a subject governs across attempts. Closeout closes the latest attempt, preview reads its verdict, and an unconverted preview reports no gate verdict. A continued leaf creates its next attempt. A file rewritten while the gate runs must not be committed unjudged, and a missing landed history refuses by name. Removed canonical-dataset reopen scenarios are historical, not current helpers or tests. This card records assertions, not a passing run.

The same-size, same-second Git rewrite scenario imports the single `rewrite_in_the_second_of_the_index_write` owner from [knowledge_index_test_support.py](knowledge_index_test_support.py.md). Its real clock alignment is the scenario's subject; the 120-second alignment guard does not assert scheduler speed. The original captured-tree/currentness assertions remain at this file's test owner.

## Evidence

### Repo-Internal References

- `test_a_reopened_leaf_writes_its_next_attempt_and_its_history_is_every_file` owns the current boundary described above. [25]
- `test_the_public_closeout_refuses_an_open_item_and_commits_once_it_is_answered` owns the current boundary described above. [26]

- `test_the_latest_row_about_a_subject_governs_across_attempts` owns the current boundary described above. [28]

- The shared owner establishes a same-size rewrite in the index-write second. [29]

- `test_a_file_rewritten_while_the_gate_runs_is_never_committed_unjudged` owns the current boundary described above. [27]
