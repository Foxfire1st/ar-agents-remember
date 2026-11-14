# dashboard/src/cockpit/sidebarChatStaysLoaded.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Five fixture-based unit cases over the real Operations right rail check iframe identity, generation, selection messages, hidden state, burst coalescing and focus containment.

## Code Commentary

The `Rig` mounts the real `RightRail` with a stubbed fetch backend (frame descriptor plus per-role agent answers) and Projects/Master/Task/ghost refs. `readyFrame` forges the plugin ready report against the stubbed origin. The river-toggle case asserts the same iframe element and generation while its wrapper changes hidden state. The message-switch case checks `ar.open` with the selected agent and workspace while retaining element and generation. The ghost case checks generation while hidden and the same element on return. The burst case checks unchanged generation before readiness, no early post and exactly one `ar.open` for the latest selection after readiness. These assertions do not count document loads. The focus case checks containment and `aria-hidden` with initial focus outside the chat; it supplies no live-host keyboard measurement.

## Evidence


- The river toggle retains the iframe element and generation while toggling its hidden wrapper. [1]


- Selection switches post ar.open with the agent and workspace while retaining element and generation. [2]


- The agentless selection hides the same frame, retains its generation and shows it again on return. [3]


- A not-ready burst retains generation, posts nothing early and forwards only the latest selection after readiness. [4]


- No focus stays inside the hidden chat. [5]
