# mcp/src/agents_remember/serving/conversation/library/helper_host.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/helper_host.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The Python host for the repository-owned locked Claude/Pi conversation-library helpers: one
short-lived Node process per operation with a handshake on every spawn. Since 260718-CHATS-L5F R4
(developer ruling 2026-07-21) the handshake reports the observed runtime/helper versions as
INFORMATIONAL evidence only — it is never a gate. THE CONTRACT IS THE ONLY GATE: the list/read
operation result, not any runtime/helper version-string comparison, decides success.

## Code Commentary

### Logic

`ConversationLibraryHelperHost.call` resolves node and the locked harness entry, writes one
handshake request plus one operation request as JSON lines to the helper's stdin, and reads
exactly two correlated responses. `_expect_handshake` validates only the handshake's SHAPE (its
`status` is one of `ready`/`incompatible`; a malformed handshake raises `LibraryStoreError`) and
reads the observed `runtimeVersion`/`helperVersion` as informational evidence — there is NO
version-string comparison and no observed-versus-locked raise (the R4 removal). The gate is the
OPERATION: `_expect_result` raises `LibraryStoreError` when the list/read call itself fails against
the installed runtime. The expected-version constants are sent as `expected*` hints on the request
as informational provenance only. `helper_preflight` reports statically why a helper cannot run (no
node, missing entry, locked dependencies not installed) without spawning. `helper_root` resolves the repository helper package from the
installed `agents_remember` package — never npm caches, OpenSrc checkouts, or global installs.

### Conventions

The host runs `node --import tsx <entry>` from the repository's own locked package with a 30 s
timeout, a 64 MiB response bound, and a 1 MiB stream buffer. Helper-reported `stale-identity`
maps to `StaleNativeIdentityError`, `invalid-request` to `InvalidLibraryCursorError`, and
anything else to `LibraryStoreError`; raw helper stderr is diagnostic-only and never disclosed
(the protocol's allow-list redaction plus this host's fixed-copy boundary).

### Invariants And Boundaries

- The handshake is part of the same process as the operation, but it does NOT gate on versions:
  it observes the runtime/helper versions as informational evidence; the operation result is the
  gate (R4 contract-only rule).
- A non-zero exit, timeout, oversized or malformed response, a malformed handshake shape, or
  correlation drift fails closed as `LibraryStoreError`. A runtime/helper version drift alone does
  NOT fail closed.
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

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false "handshake must report ready against the locked version
  constants or the call raises" doctrine: the handshake reports observed versions as informational
  evidence, `_expect_handshake` validates only the status shape, there is no version-comparison
  raise, and the list/read operation result is the only gate. Uncommitted; closeout re-stamps.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the locked helper host sidecar.
  Verification is blank until closeout commits and stamps the new source.
