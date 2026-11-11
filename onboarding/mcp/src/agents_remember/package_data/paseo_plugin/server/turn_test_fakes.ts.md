# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_test_fakes.ts

## Governing Overview

[Native Paseo plugin](../overview.md)

## Purpose

The fakes the declared-wait tests share, so a case drives one turn end through the pure decision without a host.

## Code Commentary

`makeSender` keeps every message it is asked to send. `fakeClock` stands at a fixed time and collects the timers the decision arms; a case fires them by hand and reads the pending ones with their delays. `hostState` gives one agent's host state, idle unless a case says otherwise, and `endSeatTurn` runs `noteTurnEnded` for one seat on the fake clock with a completed outcome and, when the case names none, an idle seat and an idle parent as the host's agents. The file is not a test itself: the plugin's test script runs only `server/*.test.ts`.

## Relationships

Imported by `background_wait.test.ts` and `subagent_wait.test.ts`; it calls `noteTurnEnded` from `turn_ended.ts`.

## Evidence

- The sender keeps what it sent. [1]
- The clock's timers are fired by hand and can be read with their delays. [2]
- An agent's host state is idle unless a case overrides it. [3]
- One seat's turn end runs through the decision on the fake clock, with an idle seat and parent by default. [4]
