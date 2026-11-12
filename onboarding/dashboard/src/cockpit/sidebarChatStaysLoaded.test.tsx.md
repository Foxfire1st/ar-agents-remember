# dashboard/src/cockpit/sidebarChatStaysLoaded.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The MIK-R122 unit suite: five rig cases over the real Operations right rail proving one loaded chat that switches by message, hides without unloading, coalesces bursts, and stays out of reach.

## Code Commentary

The `Rig` mounts the real `RightRail` with a stubbed fetch backend (frame descriptor plus per-role agent answers) and Projects/Master/Task/ghost refs. `readyFrame` forges the plugin ready report against the stubbed origin. Per-case scope is exact: the river-toggle case asserts the same iframe element with the load count unchanged; the message-switch case asserts `ar.open` with agent and workspace with element and generation unchanged; the ghost case asserts generation unchanged while hidden and the same element on return; the burst case asserts nothing loads in between with exactly one `ar.open` for the latest selection; the focus case discards the ready return and asserts only containment and `aria-hidden` outside the hidden chat. The focus setup starts outside Chat, so the case is credited at that unit scope, not as a native keyboard certificate.

## Evidence


- The river toggle keeps the same frame element with the load count unchanged. [1]


- Selection switches post ar.open with agent and workspace and never load again. [2]


- The agentless selection hides the frame without unloading it and switches back. [3]


- A not-ready burst loads nothing in between and brings only the latest selection forward. [4]


- No focus stays inside the hidden chat. [5]
