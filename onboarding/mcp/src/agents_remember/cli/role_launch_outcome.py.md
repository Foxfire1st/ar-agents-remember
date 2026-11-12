# mcp/src/agents_remember/cli/role_launch_outcome.py

## Purpose

Publish host launch results while preserving recoverable empty step-up seats.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

Created results publish execution/applied choices and any observed workspace preparation. Held creation retains replayRequest when no prompt was sent; ordinary running creation drops it. Host warnings and observed choice metadata remain separate from AR acceptance.

A refused launch records lost-agent or unsettled-predecessor archival debt. Only a step-up with no lost agent and predecessor_settled retains its saved call and advises same-call retry for an empty seat; other refusals drop replayRequest and remain closed.

Unanswered outcomes remain unknown with HTTP 202 and the exact saved-call identity. Rejected outcomes return HTTP 502. The receipt owner delegates publication here and performs task-decision reconciliation outside this projection.

## Evidence

- Created/held/unknown results preserve prior lifecycle semantics. [1]
- Only settled empty step-up refusals remain retryable. [2]

- The caller saves and reconciles task metadata around the host outcome. [3]

- Test source checks rejected empty seat and successful same-ID retry. [4]
