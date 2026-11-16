# skills/l-01-agent-lifecycles/reference/curator/encountered-records.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for authoring an encountered weakness or a document dependency through the writer and answering their worklist rows.

## Code Commentary

Weaknesses and dependents are written through the writer like other records, using the record shapes in the hand-off list template. A producer entry of kind `weakness` becomes a `WKN-` record, or the report explains why it did not; the writer refuses an unknown entry kind and names the field. A producer entry of kind `dependent` becomes a `DPD-` record. A weakness row is answered by deciding whether the weakness stands, with its anchor moving with the code, or is closed; a changed document's row is answered only by the confirmed dependent record. Neither record refuses a task.

A weakness removed by the running task closes with that task's ID and a one-sentence reason, without a commit. A closure by another task requires that task's real code commit. After closeout, the closed-record read obtains the code commit from the memory commit's `Code-Commit` trailer; before closeout, it reports that the commit comes with closeout.

## Evidence

- Producer weakness and dependent entries become `WKN-` and `DPD-` records through the writer. [1]
- Their worklist rows are answered by standing-or-closed and confirmed-dependent decisions, and neither record refuses a task. [2]
