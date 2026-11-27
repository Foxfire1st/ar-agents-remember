# mcp/src/agents_remember/cli/provider_limit_drain.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

What a held-message drain owes a recipient whose provider limit is running: wait for the reset, and pay at most one host read per `ended` stamp.

## Code Commentary

The drain checks the provider limit before its ordinary recipient read, except for uncreated deferred held seats (`is_deferred_held_receipt`), which return immediately without checking provider limits or resolving absent because they have no host agent or usage report yet. During an active limit on a live recipient, an `ended` publication can trigger one host read per new event stamp, using the boot identifier when the publication has no event time. A found, unarchived recipient, including a closed session, keeps its messages waiting. The same stamp triggers no repeat read.

A confirmed archive or absence resolves held messages as undelivered. An unreachable host returns `host-unreachable` and releases the drain claim. The remaining limited cases retain their messages with `provider-limit`. When `pause_for_provider_limit` pauses a claim with a known `limited_until`, it publishes a `ResetTarget` to `HeldResetIndex` (releasing the claim on `(sqlite3.Error, OSError, ValueError)` before re-raising so waiting messages never stay locked) so the independent reset scheduler wakes at the reset rather than waiting for the ordinary rotating receipt cursor.

Both decisions are policy, so they live here rather than in the held-message store's own module: that module owns the store and the drain, this one decides when they wait.

- The drain bypasses uncreated deferred held receipts, uses one confirmation read per new ended stamp for limited live seats, and resolves held messages on confirmed archive or absence. [1]
