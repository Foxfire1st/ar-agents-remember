# mcp/src/agents_remember/serving/conversation/library/factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The L0 composition defines the immutable runtime this factory derives from; the service module
consumes the injected port builder through the documented no-cycle seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| The immutable runtime/scope types and install-once binding used by this factory. | `ConversationScope`; `ConversationRuntime`; `install_conversation_runtime` | mcp/src/agents_remember/serving/conversation/runtime.py:47-52; mcp/src/agents_remember/serving/conversation/runtime.py:55-78; mcp/src/agents_remember/serving/conversation/runtime.py:81-87 |
| The service module's injected `port_builder` seam. | "port_builder: PortBuilder" | mcp/src/agents_remember/serving/conversation/library/service.py:84-84 |
| The foundation suite pins per-app isolation and no import-time singleton for the composition this factory preserves. | `test_no_import_time_mutable_singleton`; `test_child_composition_is_isolated_per_app` | mcp/tests/test_conversation_runtime_composition.py:197-208; mcp/tests/test_conversation_runtime_composition.py:211-224 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local factory module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

The library factory now builds one `LibraryBinding(runtime=…, shared=…, authorization=…)` and
passes it on, instead of three parallel keywords: the app-scoped library authorities bound to ONE
caller. Every operation fingerprint, ledger key and minted session id is derived from that pairing,
so binding them once is what stops one caller's request from being keyed under another's identity.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that ran past
  the end of `mcp/tests/test_conversation_runtime_composition.py` (the file is 252 lines). Narrowed
  it to the exact two tests the claim names — `test_no_import_time_mutable_singleton` and
  `test_child_composition_is_isolated_per_app` — cit:([`test_no_import_time_mutable_singleton`; `test_child_composition_is_isolated_per_app`], mcp/tests/test_conversation_runtime_composition.py:197-208; mcp/tests/test_conversation_runtime_composition.py:211-224) instead of sweeping the whole suite.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `LibraryBinding` call shape.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the dormant resolver factory
  sidecar. Verification is blank until closeout commits and stamps the new source.
