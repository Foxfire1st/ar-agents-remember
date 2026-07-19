# mcp/src/agents_remember/serving/conversation/library/helper_host.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/helper_host.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The Python host for the repository-owned locked Claude/Pi conversation-library helpers: one
short-lived Node process per operation with a version handshake on every spawn, so a version
drift between the gate and a call fails closed instead of silently reading an incompatible
history.

## Code Commentary

### Logic

`ConversationLibraryHelperHost.call` resolves node and the locked harness entry, writes one
handshake request plus one operation request as JSON lines to the helper's stdin, and reads
exactly two correlated responses. The handshake must report `ready` against the locked
runtime/helper version constants (Claude 2.1.211 / SDK 0.3.207; Pi 0.80.7 / 0.80.7) or the call
raises `LibraryStoreError` carrying the observed-versus-locked tuple. `helper_preflight`
reports statically why a helper cannot run (no node, missing entry, locked dependencies not
installed) without spawning. `helper_root` resolves the repository helper package from the
installed `agents_remember` package — never npm caches, OpenSrc checkouts, or global installs.

### Conventions

The host runs `node --import tsx <entry>` from the repository's own locked package with a 30 s
timeout, a 64 MiB response bound, and a 1 MiB stream buffer. Helper-reported `stale-identity`
maps to `StaleNativeIdentityError`, `invalid-request` to `InvalidLibraryCursorError`, and
anything else to `LibraryStoreError`; raw helper stderr is diagnostic-only and never disclosed
(the protocol's allow-list redaction plus this host's fixed-copy boundary).

### Invariants And Boundaries

- The handshake is part of the same process as the operation: every spawn re-proves
  runtime/helper compatibility before the operation executes.
- A non-zero exit, timeout, oversized or malformed response, version mismatch, or correlation
  drift fails closed as `LibraryStoreError`.
- The 64 MiB response bound is checked after `communicate()` returns (review O3, accepted
  posture for a repository-owned locked helper); stream-bounded reading is the recorded
  hardening direction if the helper's trust posture ever weakens.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal helper host.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The helper package owns the JSONL protocol this host pairs with; the installed suite drives the
real helper end-to-end including its malformed-request refusals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The versioned JSONL serve loop, typed failure vocabulary, and paging primitives the host correlates against. | L102-L259 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The installed suite proves the helper handshake plus malformed-request rejection on the real process seam. | L263-L280 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |
| The Python foundation suite forbids incidental module resolution in the helper sources this host spawns. | L102-L120 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local helper host.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the locked helper host sidecar.
  Verification is blank until closeout commits and stamps the new source.
