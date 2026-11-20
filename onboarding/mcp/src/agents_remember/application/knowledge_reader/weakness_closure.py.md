# mcp/src/agents_remember/application/knowledge_reader/weakness_closure.py

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Derive closing-code attribution for a closed weakness's read response while leaving its stored closure unchanged. [1]

## Code Commentary

`closure_document` starts from the closure's document copy and returns an explicit closing commit unchanged. [1]

Without a stored commit, it seeks the unique memory commit introducing the selected closure block and reads that commit's own `Code-Commit` trailer. [1] [2]

A derived value is returned as `commit` only when it resolves to that identical full commit in the selected code repository; a missing trailer, unusable commit or read failure instead produces an unavailable `commitNote`. [1]

A directory selection with no selected revision, or whose selected revision does not yet contain its closure block, gets the note that the code commit comes with the task's closeout. [1] [2]

A historical selection with no revision or a different closure, unreadable history, an ambiguous origin or incomplete ancestry gets an unavailable explanation. [1] [2]

`_closing_memory_commit` gathers the record ID's historical filenames with merge-preserving history, compares the selected closure block, requires one origin and checks the origin's actual parents for incomplete ancestry. [2]

`_closure_origins` follows only parent blocks equal to the selected closure, using a local memo and visited set to identify independent origins. [3]

`_closure_at` searches the known historical filenames at one exact revision, treats no matching file as no closure and reports multiple files, invalid records or a mismatched ID through the unavailable-attribution path. [4]

## Invariants And Boundaries

`marks.weakness_list` uses this display for closed rows, and `truth.record_view` uses the same returned closure in both `record.document.closed` and `facet.closed`.

The derived fields belong to the read response; this module does not write a closing commit or a closure state into the record or index. [1]

## Evidence

- A copied closure keeps its explicit commit or displays derived attribution and a reason when unavailable. [1]
- The exact closed block is attributed through the selected memory history, with pending and ancestry checks. [2]
- A local merge-preserving walk identifies matching closure origins. [3]
- Historical filenames are read by stable record ID at an exact revision. [4]

- Both weakness-list and truth-view callers consume the shared returned display. [5]
