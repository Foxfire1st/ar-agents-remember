# dashboard/src/cockpit/frameTrayChannel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Join dashboard tray state to the controller of each document or Chats frame.

## Code Commentary

### Logic

The nonpersisted vanilla store keeps composer measurement/unavailability, pick notices, shown-chat identity and requested tray space per frame page. A measured composer edge is one of two shapes: the vertical edge alone, or that edge with the message box's own `left` and `width`. The module provides hooks for consumers and one shared copy-on-highlight preference.

onPick counts registered listeners. receiveFrameTray delivers picks to them, removes that page’s stale pick notice after a successful pick, and records composer and failure reports, storing `left` and `width` only when the parsed message carries both so a report without the pair keeps the vertical-only shape. Exported composerExtent reads that pair back for the dock.

frameTrayReady clears prior page reports and subscribes only when the plugin names pick. It posts changed ar.tray wishes and per-page ar.tray-space heights; stop releases the subscription. Requested space is finite, rounded and nonnegative.

### Invariants And Boundaries

Origin/window validation occurs in paseoFrameControl before receiveFrameTray; this store does not inspect or steer an iframe. undefined shown-chat identity means no report yet, whereas null is an explicitly unnamed chat.

## Evidence

- Normalized height and listener lifecycle [1]
- Per-page incoming state and pick dispatch [4]
- Capability-gated subscription and deduplicated outgoing messages [3]
