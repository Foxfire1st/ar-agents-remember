# mcp/src/agents_remember/canvas/explainer_planned_read.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The reads behind the planned-mode page: one task document, one statement per declared existing subject, one file per packet, the reference folder's names and the code tip's path set.

## Code Commentary

- `planned_payload` performs exactly those reads and hands them to the pure page builder, so the page is a function of what the caller actually read and nothing else.
- `subject_statements` reads each existing subject's current statement at the memory tip, and leaves out a subject the tree does not hold or whose statement cannot be read, so the page shows the declaration alone rather than a statement it never read.
- `_packet_texts` reads the file each requirement names and skips one it cannot read, which the page then reports as `unread` rather than as empty prose.
- `_code_tip_paths` refuses `planned-comparison-unavailable` when the code tip cannot be listed, instead of resolving scope paths against nothing.
- Nothing here starts a model turn, captures a comparison or writes, so reading a planned page never changes the leaf.

## Evidence

- The leaf's reference files are looked for in one task-relative folder [1]
- The page is built from the documents and tips the caller's own reads returned [2]
- A subject the memory tree does not hold is left out instead of stated from another version [3]
- A packet that cannot be read is left out, and the page reports it unread [4]
- An unreadable code tip is a named refusal, not an empty path set [5]
