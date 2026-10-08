# dashboard/src/cockpit/document-chat/sidebar.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Focused regression tests for the document page's native-sidebar isolation and the page-mode channel.

## Code Commentary

The first case drives the real plugin bridge, the load-time write watcher and `documentSidebar` together: it asserts one collapse per native open, the hidden menu button under the document style, that the rail's in-memory closed choice never becomes the shared stored choice, and that leaving document mode stops the isolation and restores native storage behavior. The second case verifies the page mode is accepted only from the listed parent origin, and that a Chats mode leaves the host's own controls and storage untouched.

## Evidence

- The tests exercise the actual bridge, write watcher and sidebar module rather than fakes. [1]
- The storage-preservation and repeated-collapse behavior is asserted end to end. [2]
- Parent-only page mode and untouched Chats behavior are asserted through the real client. [3]
