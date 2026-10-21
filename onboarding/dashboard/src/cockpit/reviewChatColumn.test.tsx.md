# dashboard/src/cockpit/reviewChatColumn.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify the review chat column’s task binding and frame continuity at the CockpitShell seam.

## Code Commentary

### Logic

The review surface is a stand-in exposing Back and chat toggle. Walks from Operations/task/review and Chats/Operations/review assert the same rail frame and generation survive, with one descriptor/load/hello for that rail.

Cold review preloads closed without agent, chat-list, warmup or dispatch reads. Opening asks for the leaf Worker’s chat. Pending task hydration holds the binding; an absent task names the problem; a task without chat shows its bound launcher without starting one. Unreachable Paseo retains review Back and Retry.

Reload starts chat closed without visibility storage. Media-query cases assert 420px overlays below 1440px, narrow fixed placement with a viewport cap, reachable close, and independent per-width-class resize storage.

### Invariants And Boundaries

The tests deliberately replace ReviewSurface and stub HTTP/native messages; their assertions concern shell composition and request counts, not final review layout or live host acceptance.

## Evidence

- Frame continuity and cold preload/task binding [1]
- Pending/absent/agentless/unreachable/reload boundaries [2]
- Overlay/narrow placement and independent width persistence [3]
