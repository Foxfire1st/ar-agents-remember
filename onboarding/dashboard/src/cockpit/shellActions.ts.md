# dashboard/src/cockpit/shellActions.ts

## Governing Overview

[overview](../overview.md)

## Purpose

Connects shell-owned state to document, seat-chat, change-set and notes actions.

## Code Commentary

Opening a change set and opening notes are mutually exclusive. Note selection stays in the selected notes target. The bell handler requests the exact seat and selects Chats without writing the observed-chat channel. Bottom-tab changes delegate to useTabChange, which owns Operations retention and review-address parking.

## Relationships

Cockpit owns the state and composes these handlers. tabMemory owns tab behavior; this module supplies actions rather than a second view store.

## Evidence

- Connects shell-owned state to document, seat-chat, change-set and notes actions. [1]
