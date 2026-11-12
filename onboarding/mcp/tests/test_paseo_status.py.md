# mcp/tests/test_paseo_status.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Ordered status-table cases distinguish unavailable host, absent/archived agent, closed session, permission wait, running/failed/cancelled/idle turns and unknown states. Refresh uses read commands, preserves an unreachable receipt, and scopes lock duration to the bridge call. Revive resumes the recorded agent only under retained task scope; resume refusal persists until the host shows an open session.

For options requests, the lock-scope regression expects a fresh `catalog` read while the launch lock is free, followed by `agent-state` with the lock held. If catalog discovery fails, the options answer uses saved catalog data marked `source = saved` with a non-null `readAt`, and keeps the same catalog-before-agent ordering. When a later fresh question fails, the returned models remain the saved models and `readAt` remains the original answer time. With the launch lock already held, options still asks for the catalog but refuses before reading the agent. [1]

The failed fresh catalog question returns the saved options answer rather than a refusal. With the launch lock held, refresh refuses without a bridge call; options still asks the fresh catalog and then refuses before reading the agent. Both refusal responses name a launch in progress. [1]

New-start tests require a fresh `catalog` query before `agent-state` in the open-execution-rule cases, unreadable-agent refusal and held-seat refusal. In the replacing-start test, a plain request is first refused and a subsequent replacing request succeeds; their combined command history is `catalog`, `agent-state`, `catalog`, `agent-state`, `agent-archive`, `workspace-open`, `agent-create`. Each attempt makes its own catalog query before reading the agent. [1]

## Evidence


- The scoped current source carries the module/document behavior described above. [1]
