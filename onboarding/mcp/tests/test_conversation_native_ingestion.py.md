# mcp/tests/test_conversation_native_ingestion.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proves that native-history projection remains available and addressable when a harness bridge
replaces an oversized payload with an `arEvidenceTruncated` envelope or when an otherwise
identity-bearing native payload fails exact mapper schema parsing.

## Code Commentary

### Logic

`NativeFrameIdentityFallbackTests` drives the real active projector with scripted native pages.
The Codex truncation case reproduces the observed 318,975-byte MCP result and asserts the emitted
row keeps `mcp-call-17` and `turn-9`; the malformed Codex case proves the same transport identity
survives an `UnmappableShape`; and the Pi case proves eager native continuation uses the identical
fallback contract. Each case also pins the harness-qualified degradation type.

The helper patches only `asyncio.to_thread` so the repository's scripted bridge executes inline;
the projector, mapper, ingestion component, store, and page path remain production objects. This
avoids an inherited `IsolatedAsyncioTestCase` default-executor shutdown hang without weakening the
behavior under test.

### Conventions

Fixtures put ids and parent ids on `NativeEvidenceFrame`, never inside the clipped raw body, because
the transport envelope is the authoritative identity boundary this suite protects.

### Invariants And Boundaries

- Every fallback row must retain the exact `native_id` and `native_parent_id` supplied by the
  bridge.
- Assertions must cover Codex parent-history hydration and Pi eager continuation.
- Tests inspect only the bounded unknown-vendor summary; clipped preview content is never promoted
  into a conversation block.
- The fallback must keep the rest of the projector page readable rather than raising
  `UnmappableShape` out of ingestion.

### Todos

None.

## Evidence

### Docs References

The resolved Domain Documentation registry has no entries; this repository owns the native-frame
and projection contracts exercised here.

No configured domain documentation was available for this suite.

### Repo-Internal References

The suite crosses the native transport model, shared ingestion fallback, and harness projector
composition while reusing the active-service bridge double.

- `NativeEvidenceFrame` keeps item, parent, type, timestamp, and raw payload as separate transport fields. [1]
- Shared ingestion turns truncation or mapper failure into a bounded row keyed by transport identity. [2]
- The scripted bridge and projector factory exercise production projector composition with doubled reads. [3]

### Cross-Repo References

No cross-repository implementation participates in this suite.

No meaningful cross-repo references found.
