# mcp/src/agents_remember/cli/held_reset_adoption.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Enrolls previously saved provider-limited held waits into `HeldResetIndex` once at dashboard startup so aged or pre-index waiting messages are delivered at their reset even when they have left the bounded held-receipt queue.

## Code Commentary

`adopt_held_resets(config, index)` iterates over all live receipt roots returned by `receipt_roots(config.coordination_root)` using a `ReceiptWalk` per root, closing each walk in `finally`. Each loop iteration reads up to `_ADOPTION_READS = 32` receipt paths via `walk.take(_ADOPTION_READS)`, inspects each candidate with `_existing_wait`, and passes the resulting targets to `index.enroll(...)`.

`_existing_wait(path)` reads the launch receipt via `_read_receipt` (ignoring `HTTPException`), extracts `(folder, agent)` via `_store_endpoints`, reads waiting rows with `read_waiting_rows(folder, agent)`, and skips incomplete reads or stores without any non-null `limitedUntil` timestamp. When one or more `limitedUntil` values are present, it builds a `ResetTarget(agent, path, Path(folder), min(resets))` using the earliest reset timestamp. Because enrollment calls `index.enroll` (`ON CONFLICT(agent) DO NOTHING`), any live entry already scheduled for that recipient wins over startup adoption.

## Boundaries

Startup adoption reads receipts and held stores in bounded 32-path walk chunks without modifying store files or sending messages. Unreadable receipts and incomplete store reads are skipped rather than raising across the startup walk.

## Evidence

- `_existing_wait` extracts the earliest `limitedUntil` timestamp from complete `read_waiting_rows` output for a readable launch receipt. [1]
- `adopt_held_resets` walks all live `receipt_roots` in chunks of `_ADOPTION_READS` (32) and calls `index.enroll` so existing live generations win. [2]
