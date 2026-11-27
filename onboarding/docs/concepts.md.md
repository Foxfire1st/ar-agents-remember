# docs/concepts.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The glossary of the user documentation. It defines each term the other pages use, in five groups: the programs, the settings and folders, memory, roles and tasks, and review.

## Code Commentary

The `Tool log` entry says where the tool server writes one row for each tool call: the day's `ar-tools-<YYYY-MM-DD>.jsonl` file, in the enclosure's `logs/` folder for a role agent's call on an enclosed task and in the transcript root for every other call.

The same entry says how a cancelled request is logged. A tool that raises after its request is cancelled leaves a `raised` row whose detail keeps the error and sets `requestCancelled`. A cancellation during the build-currentness check, the wait for the write lock or the wait for a detached worker thread leaves a `cancelled` row whose `waitingFor` names the wait and which says the tool never ran. A result that arrives after the cancellation is logged as usual.

Under `How an agent finds memory`, the guide describes `read_ar_files` brief/count/compact replies alongside 11-view `knowledge_read` (auto-pairing the code tree from `repo_id`, `contractPath`, or `memoryRoot`; returning text-bearing `impact`/`search` rows, verbatim `records` for up to 25 IDs, and structured locations/reports in the other views; reserving native file opens for source code, tests, briefs, and cards).

## Relationships

The tool reference links the `Tool log` entry from its sync and closeout sections. The rows it describes are written by `mcp/src/agents_remember/mcp/server.py`.

## Evidence

- The tool log entry names the daily file, the enclosure folder and the transcript root. [1]
- The entry names the raised and cancelled rows and their detail fields. [2]
