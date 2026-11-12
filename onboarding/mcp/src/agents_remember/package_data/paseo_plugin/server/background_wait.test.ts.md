# mcp/src/agents_remember/package_data/paseo_plugin/server/background_wait.test.ts

## Governing Overview

[Native Paseo plugin](../overview.md)

## Purpose

The package test for the declared background wait: the declaration on any seat, its check time, both waits declared in one end, the wait's endings, the silent end beside it, and the open wait as the host-activity record shows it.

## Code Commentary

Every case drives the pure turn-end decision with a fake clock and a fake sender from `turn_test_fakes.ts`, so no host is needed; the timers are fired by hand and the delays asserted exactly. The source declares seventeen `test` calls, two of them inside loops that register one case per seat kind or per keyword. The cases cover: an ACP seat and a seat not on ACP each declaring a background wait that is not silent, gives the parent nothing and is checked at three minutes; a named check time used, and a value outside 1 to 30 clamped with the row saying so; both waits in one end giving one check at the earlier time that asks about helpers and processes; the next undeclared end ending the wait; archiving ending both waits with no check sent; a declaring end of a seat the host reports archived; an end that declares only one of two open waits; a background check re-armed for its own time in a permission wait; the silent end's message naming the background declaration; the keyword read only at a line start; the plugin's background checks recognised as its own; a Claude seat's helper declaration; a harness wake being the seat's own continuation whose undeclared end ends the wait; the open wait handed to the host-activity record and evicted declarations announced; and the record carrying an open wait beside the host's idle state.

## Relationships

It runs with the plugin's `test` script (`node --experimental-strip-types --test server/*.test.ts`). The helper wait's own cases are in `subagent_wait.test.ts`; the code under test is `background_wait.ts`, `declared_wait_state.ts`, `turn_ended.ts` and `host_activity.ts`. A source case is not a live-host delivery witness.

## Evidence

- A named check time is used, and a value outside 1 to 30 is clamped with the row saying so. [1]
- Both waits declared in one end get one check, at the earlier time, asking about both. [2]
- Archiving ends both waits with their rows, and no check goes out. [3]
- A silent end's message ends with the background sentence, and only an ACP seat gets the ACP sentence. [4]
- The record carries an open wait beside the host's idle state, writes nothing for an unchanged one and drops it for an ended agent. [5]
