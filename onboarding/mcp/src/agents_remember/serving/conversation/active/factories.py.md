# mcp/src/agents_remember/serving/conversation/active/factories.py

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The running-session projector factory: resolves one exact running session from the terminal
catalog, proves its harness/native identity through the production IPC seam, reads the live
bridge epoch and adapter snapshot, and constructs the per-harness active projector mapper —
failing closed typed for unknown rows, dead sessions, sessions without a protocol control
endpoint, harnesses without a projector, and sessions without proven native identity.

## Code Commentary

### Logic

cit:([`SessionResolutionError`], mcp/src/agents_remember/serving/conversation/active/factories.py:31-35) is the typed base; `UnknownSessionError` 404,
`UnsupportedSessionError` 409 `unsupported`, `ControlUnavailableError` 503
`control-unavailable` cit:([`ControlUnavailableError`], mcp/src/agents_remember/serving/conversation/active/factories.py:51-53) are the wire-visible refusals. `resolve_running_entry`
cit:([`resolve_running_entry`], mcp/src/agents_remember/serving/conversation/active/factories.py:63-76) mirrors the serving idiom: the catalog row must exist, be `running`, be a `harness`
kind with a `control_endpoint`, and be alive on the terminal host. cit:([`build_identity`], mcp/src/agents_remember/serving/conversation/active/factories.py:79-105)
selects the harness projector via `projector_for`, requires the snapshot's proven
`vendor_session_id`, assembles the `ActiveConversationRef` (harness, vendor conversation,
project scope from the catalog cwd, AR session id, bridge epoch), and stamps the server-issued
`identity_digest` — an HMAC-SHA256 over the canonical identity tuple cit:([`identity_digest`], mcp/src/agents_remember/serving/conversation/active/factories.py:53-60), recomputable for comparison, never accepted from a client. `current_bridge_epoch`
cit:([`current_bridge_epoch`], mcp/src/agents_remember/serving/conversation/active/factories.py:108-114) and cit:([`live_snapshot`], mcp/src/agents_remember/serving/conversation/active/factories.py:117-123) wrap the validated IPC reads and map
`HarnessControlError` to `ControlUnavailableError`.

### Conventions

No session state is ever manufactured: every fact comes from the catalog row, the live
submission authority, or the live adapter snapshot through the production seam. The identity
digest is a server-issued comparison token, not an authorization grant.

### Invariants And Boundaries

- A session without a proven `vendor_session_id` fails `unsupported`; identity is never assumed
  from the harness id alone.
- IPC failures are `control-unavailable` (503), never raw 500s (the O4 idiom).
- The factory holds no caching and no app state; projector lifetime is the service's concern.
- The bridge epoch comes only from the live submission authority read — ambient server context
  is never a substitute.

### Todos

None.

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. The production seam contracts are
repository-owned and cited below.

No configured domain documentation was available for this factory.

### Repo-Internal References

The validated IPC client owns the authority/snapshot reads; the catalog owns the row shape; the
projector registry owns per-harness mapper selection; the service drives this factory per wire.

- The validated exact-session IPC reads used here. [1]
- `AdapterSnapshot.vendor_session_id` is the proven native identity the factory requires. [2]
- The catalog row supplies status, kind, control endpoint, tmux name, and cwd. [3]
- `projector_for` returns `None` for harnesses without a projector, failing resolution typed. [4]

### Cross-Repo References

No cross-repository implementation participates in this factory.

No meaningful cross-repo references found.
