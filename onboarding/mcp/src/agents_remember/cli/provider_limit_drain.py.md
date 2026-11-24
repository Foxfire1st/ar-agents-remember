# mcp/src/agents_remember/cli/provider_limit_drain.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

What a held-message drain owes a recipient whose provider limit is running: wait for the reset, and pay at most one host read per `ended` stamp.

## Code Commentary

The drain checks the provider limit before its ordinary recipient read. During an active limit, an `ended` publication can trigger one host read per new event stamp, using the boot identifier when the publication has no event time. A found, unarchived recipient, including a closed session, keeps its messages waiting. The same stamp triggers no repeat read.

A confirmed archive or absence resolves held messages as undelivered. An unreachable host returns `host-unreachable` and releases the drain claim. The remaining limited cases retain their messages with `provider-limit`. After reset, eligible messages drain in order when the bounded rotating receipt cursor reaches the recipient, which can take later ticks.

Both decisions are policy, so they live here rather than in the held-message store's own module: that module owns the store and the drain, this one decides when they wait.

- The drain uses one confirmation read per new ended stamp and resolves held messages on confirmed archive or absence. [1]
