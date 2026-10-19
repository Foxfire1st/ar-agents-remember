# mcp/src/agents_remember/canvas/presenter_host.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

A deterministic explicit harness fixture and the shared host port records: one implementation behind the presenter's runner port, doing two things at once — preparing one attempt's folder as the only place it may write, and answering the identity-bound host operations.

## Code Commentary

- `HostWorkspace.prepare` creates the attempt's own folder and refuses anything outside it; `read_input`, `write_output` and `write_bookkeeping` keep their own boundaries.
- `HostReceipt` records what one host operation answered, so the presenter records rather than invents a receipt.
- `DocumentationTools` is guidance for the author and is never review evidence; `as_review_evidence` is the explicit refusal of that conversion.

## Evidence

- One attempt's prepared folder is the only place the harness may write. [1]
- A host receipt is recorded, not invented. [2]
- Authoring documentation is never review evidence. [3]
