# mcp/src/agents_remember/application/task_docs/task_retirement_shared.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

Supplies retirement payload parsing, the restart notice, root-folder guards, source digests and archive-hook handling.

## Code Commentary

`archive_hook` invokes review-artifact cleanup and converts any hook exception into a failed report. `hook_failed` recognizes reported failures and `hook_remainder` counts artifacts that a preview still lists for deletion. The real retirement result and its state are owned by `task_master_retirement._clean_up`; this module does not contain a separate cleanup state machine.

Root-folder admission refuses a nested master before changes. A restart notice applies when a record exists or a request would create it, including later refusals, rather than to every pre-recording refusal.

## Evidence

- Shared helpers parse payloads and classify hook failure and remaining work. [7]
- Real cleanup outcome and operation state are attached by the retirement owner. [8]
