# mcp/tests/test_closeout_queue_abandoned_rows.py

## Governing Overview

[tests overview](overview.md)

## Purpose

An abandoned row of a master is outside the closeout queue's walks of that master's rows. The case sets a master's rows and checks that an abandoned row needs no document while every other unfinished row still does.

## Code Commentary

`_set_rows` writes the rows, `_rebuild` rebuilds the queue projection and `_candidate_population` reads the queue's candidate count; `test_abandoned_rows_need_no_document_and_other_rows_still_do` carries the rule.

## Evidence

- An abandoned row of a master needs no document and is outside the closeout queue's walks; other unfinished rows still need one. [1]
