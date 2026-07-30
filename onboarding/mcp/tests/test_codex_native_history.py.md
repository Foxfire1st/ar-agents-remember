# mcp/tests/test_codex_native_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_native_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The history reader implements the contracts exercised by this suite. | L41-L695 | [codex_app_server_history.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_history.py) |
| Typed native-history errors preserve codes and byte evidence. | L124-L144 | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |

## Cross-Repo References

No cross-repository fixture is used.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  native-history unit/resource suite. Verification metadata remains blank because the new test is
  uncommitted.
