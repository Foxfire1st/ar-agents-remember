# mcp/src/agents_remember/controlplane/held_reset_index.py

## Governing Overview

[overview](overview.md)

## Purpose

Durable SQLite scheduling index for recipients whose waiting held messages carry a known provider reset timestamp. It stores one replaceable, generation-fenced row per waiting recipient ordered by next eligible delivery attempt; it does not read launch receipts, open held-message stores, or send messages.

## Code Commentary

`ResetTarget` carries the waiting recipient's `agent_id`, `receipt_path`, `workspace_path`, and UTC `reset_at`, and `ResetEntry` pairs a `ResetTarget` with the row's random hex `generation` token.

`HeldResetIndex` opens `<coordination_root>/temp/held-resets.sqlite` with one `due` table (`agent` primary key, `receipt`, `workspace`, `reset`, `next_attempt`, `generation`) and one `due_time` index on `(next_attempt, agent)`. Every write path goes through `_writer()`, which checks `require_durable_write_target(self.path)` before creating parent directories or opening a writable SQLite connection. Read paths (`next_attempt`, `due_at`) use `_reader()` in `?mode=ro` URI mode and return `None` or `[]` when the database file does not yet exist.

- `schedule(target)` upserts (`INSERT ... ON CONFLICT(agent) DO UPDATE`) the recipient's latest `receipt`, `workspace`, `reset`, `next_attempt`, and a fresh `generation` so live admissions and drain pauses always publish the latest reset.
- `enroll(targets)` inserts startup-adopted chunks with `INSERT ... ON CONFLICT(agent) DO NOTHING`, so an already-published live index entry is never overwritten by a stale startup scan.
- `next_attempt()` returns `MIN(next_attempt)` as a UTC `datetime` or `None` when empty.
- `due_at(now)` returns all rows with `next_attempt <= now.timestamp()` ordered by `(next_attempt, agent)`.
- `finish(entry, retry_at)` scopes its mutation to `WHERE agent=? AND generation=?`, deleting the row when `retry_at is None` and updating `next_attempt` when `retry_at` is set; an earlier generation can never delete or overwrite a newer scheduled generation for the same recipient.

## Boundaries

This module is a non-knowledge scheduling store explicitly allowed by the database-retirement guard (`controlplane/held_reset_index.py`). It does not substitute for the recipient's held-message store file as message authority; removal of an entry is owned by the delivery caller after confirming the store is empty or gone.

## Evidence

- `ResetTarget` and `ResetEntry` define the recipient reset scheduling target and generation-fenced entry shape. [1]
- `HeldResetIndex` stores one row per waiting agent in `<coordination_root>/temp/held-resets.sqlite` indexed on `(next_attempt, agent)` and enforces `require_durable_write_target` before writes while reading in `?mode=ro` mode. [2]
- `schedule` upserts with a new generation, `enroll` preserves existing live rows via `ON CONFLICT(agent) DO NOTHING`, `next_attempt` and `due_at` query due order, and `finish` fences deletes and retries by `(agent, generation)`. [3]
