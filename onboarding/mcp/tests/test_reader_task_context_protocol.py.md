# mcp/tests/test_reader_task_context_protocol.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

An in-memory registered MCP session verifies the optional exact task_context pair on context_packet/read_ar_files. Alternating and concurrent base/leaf reads return their own source and memory roots, wrong repository/contract or incomplete pair refuses, and the temporary marker cleanup restores both Git statuses. It launches no host runtime or stdio server.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
