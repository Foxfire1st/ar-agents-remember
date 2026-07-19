# mcp/src/agents_remember/serving/conversation/library/factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant resolver factory: derives the app-scoped library authorities (cursor signing key,
live gate registry, helper host, bounded open ledger) once per exact L0 runtime, and builds
per-request caller-bound ports and services without any `app.state` or composition edit.

## Code Commentary

### Logic

`LibraryShared` bundles the four app-scoped authorities; `library_shared` memoizes one bundle
per exact `ConversationRuntime` in a lock-guarded weak-key dictionary — each app gets its own
bundle, the bundle is reclaimed with its runtime, and nothing is held at import time.
`build_port` constructs the dormant resolver for one normalized harness (direct
`CodexConversationLibrary`; helper-backed `ClaudeConversationLibrary`/`PiConversationLibrary`)
bound to the caller's authorization; `build_library_service`/`build_open_service` wire the
services with a port-builder lambda so the service module never imports this factory (no import
cycle). `require_normalized_harness` narrows a raw path segment to `codex`/`claude`/`pi` or
raises for the route's 404 mapping.

### Conventions

Per-request pieces (ports, services) are built fresh with the caller's server-resolved
authorization binding, so every minted cursor, key, and operation re-binds that exact
principal/tenant on every call. App-scoped pieces are memoized because a per-request rebuild
would re-run gates and forget open operations, while a module-level singleton would break the
per-app isolation L0 proves.

### Invariants And Boundaries

- Child leaves never touch `app.state`: the L0 composition hands the immutable runtime and this
  factory derives child-owned ports from it.
- The weak-key map is the only shared-state mechanism; no import-time instance exists.
- Unknown harness ids fail closed as `UnknownLibraryHarnessError` at both the route narrowing
  and the port construction seams.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal factory module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The L0 composition defines the immutable runtime this factory derives from; the service module
consumes the injected port builder through the documented no-cycle seam.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The immutable runtime/scope types and install-once binding define the app-scoped composition this factory memoizes per instance. | L47-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| The service documents the injected port-builder seam that keeps this factory import-free. | L1-L11 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/service.py) |
| The foundation suite pins per-app isolation and no import-time singleton for the composition this factory preserves. | L106-L260 | [test_conversation_runtime_composition.py](agents-remember/mcp/tests/test_conversation_runtime_composition.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local factory module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the dormant resolver factory
  sidecar. Verification is blank until closeout commits and stamps the new source.
