# Role message file primitives

## Governing Overview

[Repository MCP overview](../../../overview.md)

## Purpose

Own the message's durable filesystem representation, not recipient selection or host delivery. The full body is a file with no payload limit; only the wake text is bounded by the caller's messaging policy.

## Contract

Names carry a UTC second, sender role/id and recipient role/id, with counters for collisions. A payload is encoded, written and fsynced once to a private staged file, then published by atomic no-overwrite link. A FIFO-bounded next-counter cache skips previously occupied names; the link is authoritative, so eviction or another process can cause retries without replacing a message. The tested same-process batch allocation is linear with no directory enumeration, not a universal performance promise across cache misses or independent processes.

The narrowest shared leaf/master/sprint determines the record folder. With no shared task, storage is beside the sender class's native execution briefs. A workspace's `messages` link always points to its own leaf record folder; divergent links and occupied non-links are preserved with warnings. Cleanup elsewhere removes the link, not the record files.

All attachment paths are checked and hashed before copying. Task-record and leaf-workspace files stay in place with their paths and hashes; outside files are copied. A failed copy removes its partial target and earlier message-owned copies. Message delivery owns cleanup if later message storage fails. The rendered file retains sender/recipient/task/time/message identity, wake text, body and attachment hashes.

## Boundaries

Host refusals are retained as `.undelivered.md` with refusal detail when marking succeeds; the marking helper falls back to the original path on filesystem failure. Do not mistake that fallback for a successfully renamed refusal file. Link warnings do not abort the canonical record write. This module does not enforce the settings limit or decide recipient authority.

## Evidence

- Stage and sync the payload once, allocate with a bounded cache and atomic no-overwrite link. [1]
- Scope storage to the narrowest shared task, or the sender class's taskless execution record. [2]

- Validate/hash every attachment before the copy phase. [3]
- Preserve occupied or divergent workspace links with warnings. [4]
- Failed copies remove their partial target and earlier message-owned copies. [5]
- Retain refused-file detail, returning the original path if marking fails. [6]
