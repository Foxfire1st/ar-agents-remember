# mcp/tests/test_conversation_native_ingestion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_native_ingestion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T16:43+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The resolved Domain Documentation registry has no entries; this repository owns the native-frame
and projection contracts exercised here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

The suite crosses the native transport model, shared ingestion fallback, and harness projector
composition while reusing the active-service bridge double.

| Finding | Anchor | Source |
| --- | --- | --- |
| `NativeEvidenceFrame` keeps item, parent, type, timestamp, and raw payload as separate transport fields. | `NativeEvidenceFrame` | mcp/src/agents_remember/models/conversations/evidence.py:116-124 |
| Shared ingestion turns truncation or mapper failure into a bounded row keyed by transport identity. | `NativeEvidenceIngestion` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:45-304 |
| The scripted bridge and projector factory exercise production projector composition with doubled reads. | `_ScriptedBridge`; `_projector` | mcp/tests/test_conversation_active_service.py:62-166; mcp/tests/test_conversation_active_service.py:168-188 |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: recorded the current native-ingestion identity and
  truncation coverage against the staged source; verification metadata remains pinned until closeout.

- 2026-08-09T16:43+02:00 — 260713-TES-L5 hotfix curator: created the focused Codex/Pi
  native-truncation identity regression card. As with the leaf's new judgment-demolition suite,
  verification is temporarily pinned to the real leaf base so pre-commit citations are auditable;
  closeout replaces it with the first commit that contains the new source file.
