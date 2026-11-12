# mcp/src/agents_remember/memory/knowledge/request_digests.py

## Governing Overview

[memory overview](../overview.md)

## Purpose

Reuses a successful logical digest only inside one synchronous review request. The endpoint's database
origin partitions answers, even for identical endpoint bytes; within one partition the witness is the
connection-visible SQLite image (including WAL) and every field of its selected generation. A
physically different image does not share an answer, a same-connection commit counter guards against
change-and-restore, and a failed read is never retained.

## Code Commentary

- `same_request_digests` opens a fresh request scope on the calling thread; nesting starts a new
  scope, and a copied context retains no finished answer. Leaving the scope clears the answers and
  marks the request inactive.
- `digest_in_request` reuses a stored answer only when the connection is eligible: `main` is
  read-only, the connection carries no row or execution trace, and its database list is exactly
  `["main"]`. A writable connection, an attached or temporary schema or a custom trace keeps the
  caller's original semantics.
- The witness key is the origin file name, the serialized `main` image and `_generation_key`, which
  snapshots every declaration value of the generation, including custom generations that share a
  friendly name. The same handle's `PRAGMA data_version` must read the same value before and after
  the image is taken.
- A refused or unreadable witness is not a successful read: the original `compute` runs and its
  refusal stands, no observation or exception is cached, and a completed result is preserved even
  when the closing cache check cannot be read.

## Evidence

- The fresh per-request scope, its nesting and its thread guard. [1]
- The full witness key over the origin, the serialized image and the generation declaration. [2]
- The same-handle commit counter read before and after the image. [3]
- Eligibility: read-only main, no traces, exactly the main database. [4]
- A failed witness read is not cached; the original computation and its refusal stand. [5]
