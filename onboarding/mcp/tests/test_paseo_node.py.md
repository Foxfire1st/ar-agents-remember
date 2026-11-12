# mcp/tests/test_paseo_node.py

## Governing Overview

[overview](overview.md)

## Purpose

The Node acquisition cases: a digest mismatch removes the archive and names both digests, a foreign folder is refused while a valid Node is read-only, a verified archive is placed as a whole, other platforms are unsupported, an existing target must report the pinned version and an answering npm, a partial HTTP read is a named failure and is reclaimed, a valid target reclaims owned staging without downloading, competing acquisitions have a finite retryable refusal, and empty XDG values use home defaults.

## Code Commentary

The module substitutes the fetch and the command runner, and exercises the file lock and the archive staging paths directly.

The lock-expiration test observes the actual thread/flock holder before calling acquisition. It asserts `node_operation_busy`, no fetch and no target creation while the lock is held, then releases and joins the holder under the shared guard. The expected product expiry is the subject; there is no elapsed-speed ceiling.

## Evidence

- The digest refusal case. [1]
- The whole placement case. [2]
- The partial-read reclamation case. [3]
- The empty-XDG case. [4]

- The observed holder retains the lock until the expected semantic refusal. [5]
