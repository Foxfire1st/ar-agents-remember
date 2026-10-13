# mcp/src/agents_remember/application/knowledge_reports.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Publish the complete lists behind bounded naming answers as caller-readable reports with explicit resource admission and truthful write-failure evidence.

## Code Commentary

Report placement follows the tool-log owner: the enclosure reports directory when a live enclosure is resolved, otherwise the configured day-detail folder. Without a known root the operation refuses; it does not choose an arbitrary fallback destination.

The writer counts serialized bytes in chunks, charges the actual log/report budget family and reserves a fraction of that budget for concurrent log growth. A census with unreadable entries refuses rather than undercounting. Accepted payloads stream to a sibling partial file and are atomically renamed.

A write failure attempts partial-file removal. If cleanup also fails, ReportWriteError carries the residual path and the refusal names it; callers must not claim universal zero residue. Reports are whole-or-refused, not shortened tool answers or tool-log replacements.

## Evidence

- Reports resolve through the existing enclosure or log root. [1]
- Publication admits a whole streamed payload and reports cleanup residue honestly. [2]
- Admission charges measured family usage plus reserved margin and refuses unreadable usage. [3]
