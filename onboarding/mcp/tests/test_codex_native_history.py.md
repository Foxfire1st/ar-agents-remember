# mcp/tests/test_codex_native_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_native_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T08:46+02:00 |
| lastVerifiedCommitHash |  `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate |  2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Pins the Codex native-history reader's contract probe, opaque one-shot continuation, explicit
resource ceilings, cycle/refetch guards, exact legacy fallback, and typed IPC round trip.

## Code Commentary

### Logic

The suite proves items-first probing, installed-shaped turns fallback, linear expansion at 10/20/40
frames, oldest-walk eviction, over-cap refusal, `A -> B -> A` source-cursor termination, and no
silent fallback after a recognized bounded RPC error. Legacy cases require two exact `-32601`
responses, apply the source-response ceiling to the aggregate frame bytes, make one `thread/read`
across multiple AR pages, and reject evicted continuation without refetch.

### Conventions

Scaled ceilings make resource behavior deterministic without allocating production-size payloads.
Exact request lists are assertions: they prevent an implementation from appearing correct while
reissuing or silently changing history contracts.

### Invariants And Boundaries

- Bounded capability is runtime-result authority; version strings are absent from selection tests.
- Cursor cycles and expired cursors terminate typed.
- A continuation emits every native id once and decodes each source response once.
- The complete parsed response ceiling is separate from the 128 MiB transport fuse.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The history reader implements the contracts exercised by this suite. | `CodexNativeHistoryReader`; `read_page` | mcp/src/agents_remember/serving/codex_app_server_history.py:110-612 |
| Native-history unavailability retains a typed machine-readable code. | "class NativeHistoryUnavailable(" | mcp/src/agents_remember/errors.py:437-442 |
| Native-history limit failures retain actual and permitted byte counts. | "class NativeHistoryLimitExceeded(" | mcp/src/agents_remember/errors.py:445-457 |

## Cross-Repo References

No cross-repository fixture is used.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated the unavailable and bounded-materialization exception definitions. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the native-history errors.py citations (390-397/398-410 to 423-428/431-443) shifted by the CCR-R08 +33-line errors.py insertion. Citation-only re-anchor; no content impact.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:13:21+02:00 — W2-B07 curator: repaired 2 repository-reference citations and normalized 1 historical prose citation after bounded source reads; the scoped citation check is clean.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation whose end ran
  14 lines past `serving/codex_app_server_history.py`, which is 681 lines. Narrowed it to L41-L681
  and read both ends: L41 is still the `SourceContract` literal that opens the contract vocabulary
  and L681 is the last line of `_decode_bounded_cursor`'s walk-id validation, so the range covers
  the whole reader — constants, `_BoundedWalk`/`_OutputWindow`/`BoundedPageRequest`,
  `CodexNativeHistoryReader`, and the cursor codec.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  native-history unit/resource suite. Verification metadata remains blank because the new test is
  uncommitted.
