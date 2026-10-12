# dashboard/src/cockpit/document-chat/knownChats.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Protects the distinction between an unknown selected chat and confirmed absence, bounded preclick knowledge, and visibility-owned polling.

## Code Commentary

Mounted DocumentChat cases keep the earlier frame visible/inert during unknown lookup, then hide the same element only after an empty answer; a batch-known selection sends the switch with the click before its fresh answer, and fresh absence corrects it. Store/tree cases assert oldest eviction, finite caps and prioritization on large trees. Hook cases assert no reads while pane/tab is hidden, genuine due-time resume, aborted stale completion and zero remaining timers on teardown. These are network/frame-message fixtures, not native installation acceptance.

## Evidence

- The suite checks mounted retention, immediate known switching, both caps and visibility cleanup with explicit assertions. [1]
