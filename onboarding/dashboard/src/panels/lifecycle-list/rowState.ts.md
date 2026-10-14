# dashboard/src/panels/lifecycle-list/rowState.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure presentation facts for one Operations row: the mark, single task-state word, need band, numeric progress and complete hover text.

## Code Commentary

A lifecycle inferred without any last event is not a report of pause: the document status speaks, or waiting when no document exists. Reported lifecycles speak their own state and eligible age; completed and abandoned states use document-style marks. `rowWord` now returns only that task state and its eligible age. Asking and blocked lifecycle states remain band zero, ahead of working, waiting and over bands; this is the task-state classification, not the former gate/inbox/chat priority selector. Hover text preserves current lifecycle facts, document status, current step, worktree/repository and abandoned/discarded progress. Short IDs are derived from an exact master-folder/id prefix, not guessed filename numbering. The removed `askingWord` helper and gate/pickup/chat-activity inputs belong to the historical L144 priority promise, narrowed by the architect's L113 INV-7GVWYD ruling; they are not current consumers.

## Evidence

- State comes from a reporting lifecycle or the document, without mutating either. [1]

- The one word is the task state with eligible age; removed outside-attention inputs no longer participate. [2]
- Whole-row hover retains the other current document, lifecycle and worktree facts. \[3] [3]
