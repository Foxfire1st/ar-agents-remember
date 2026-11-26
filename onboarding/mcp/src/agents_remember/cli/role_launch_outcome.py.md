# mcp/src/agents_remember/cli/role_launch_outcome.py

## Purpose

Publish host launch results while preserving recoverable empty step-up seats.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

Created results publish execution/applied choices and any observed workspace preparation. Held creation retains replayRequest when no prompt was sent; ordinary running creation drops it. Host warnings and observed choice metadata remain separate from AR acceptance.

A refused launch records lost-agent or unsettled-predecessor archival debt. An empty step-up may retain its saved call when the predecessor settled and the refusal reports no lost agent. A missing recorded native Antigravity agent settles the refusal and drops replayRequest, including for an empty step-up.

Unanswered outcomes remain unknown with HTTP 202 and the exact saved-call identity. Ordinary rejected creation returns HTTP 502. A saved native Antigravity launch whose recorded agent is absent returns HTTP 409 with ACP guidance and hostAgentExists=false. The receipt owner delegates publication here and performs task-decision reconciliation outside this projection.

## Evidence


- Created/held/unknown results preserve prior lifecycle semantics. [1]




- An eligible settled empty step-up can be retried. An absent native Antigravity agent instead closes the request with HTTP 409 and ACP guidance. [2]









- The receipt owner records the task step-up decision before running the saved call and reconciles that decision after publishing the host outcome. [3]






- Test source checks rejected empty seat and successful same-ID retry. [4]
