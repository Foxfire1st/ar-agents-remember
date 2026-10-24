# dashboard/src/cockpit/reviewChatColumn.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify the review chat column’s task binding and frame continuity at the CockpitShell seam.

## Code Commentary

### Logic

The review surface is a stand-in exposing Back and chat toggle. Walks from Operations/task/review and Chats/Operations/review assert the same rail frame and generation survive, with one descriptor/load/hello for that rail.

Cold review preloads closed without agent, chat-list, warmup or dispatch reads. Opening reads the exact leaf explainer state, with no Worker chat lookup. Pending task hydration holds the binding; an absent task names the problem; a known missing explainer seat shows its placeholder without starting one. Unreachable Paseo retains review Back and Retry.

Reload starts chat closed without visibility storage. Media-query cases assert 420px overlays below 1440px, narrow fixed placement with a viewport cap, reachable close, and independent per-width-class resize storage.

### Invariants And Boundaries

The tests deliberately replace ReviewSurface and stub HTTP/native messages; their assertions concern shell composition and request counts, not final review layout or live host acceptance.

## Evidence

- Frame continuity and cold preload/task binding [1]
- Overlay/narrow placement and independent width persistence [3]

Cold review still preloads the same frame without a seat/chat/warmup/dispatch read. Opening now reads the exact leaf explainer state and steers that retained frame to a-exp, with no Worker document-chat lookup. Pending or missing task identity makes no explainer-state request. A known no-seat answer draws explainer-placeholder rather than a role launcher. The existing page walk now permits one native open to select the explainer while asserting the same frame node and generation.

- Cold review still preloads the same frame without a seat/chat/warmup/dispatch read. Opening now reads the exact leaf explainer state and steers that retained frame to a-exp, with no Worker document-chat lookup. Pending or missing task identity makes no explainer-state request. A known no-seat answer draws explainer-placeholder rather than a role launcher. The existing page walk now permits one native open to select the explainer while asserting the same frame node and generation. [4]

- The retained shell cases cover pending and missing task identity without chat reads, a no-seat explainer placeholder without dispatch, unavailable host recovery and reload-closed behavior; they do not require a Worker default or a role launcher in the review column. [2]
