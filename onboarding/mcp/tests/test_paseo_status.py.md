# mcp/tests/test_paseo_status.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Ordered status-table cases distinguish unavailable host, absent/archived agent, closed session, permission wait, running/failed/cancelled/idle turns and unknown states. Refresh uses read commands, preserves an unreachable receipt, and keeps receipt liveness calls outside the dispatch lock. Revive resumes the recorded agent only under retained task scope; resume refusal persists until the host shows an open session.

The options regression expects `catalog` and the subsequent `agent-state` read to run while the launch lock is free. If catalog discovery fails, the options answer uses saved catalog data marked `source = saved` with a non-null `readAt`, and keeps the same catalog-before-agent ordering. When a later fresh question fails, the returned models remain the saved models and `readAt` remains the original answer time. With the launch lock already held, both forms of Options return before contacting the host. [1]

The result route and both options requests report a launch in progress before contacting the host when the launch lock is held. Parked task-bound, Investigator and taskless legacy receipt reads allow Start to reach admission. The replacement and migration cases ensure an earlier observation cannot replace a newer or already migrated receipt. [1]

The open-execution and unreadable-holder cases assert `catalog` then `agent-state`. The failed-Revive case separately checks that a plain Start is refused and a replacing Start archives the holder before creating the successor. Across those two commands it asserts `catalog`, `agent-state`, `catalog`, `agent-state`, `agent-archive`, `workspace-open`, `agent-create`, `agent-create`.


- The open-execution cases assert catalog before agent-state. The failed-Revive case checks the combined refused and replacing Start trace. [2]



## Evidence




- Tests cover status, Revive, saved catalogue answers, lock-free host reads and launch-in-progress responses with zero host calls. [1]
