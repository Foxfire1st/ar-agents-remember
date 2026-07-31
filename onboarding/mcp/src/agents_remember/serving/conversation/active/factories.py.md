# mcp/src/agents_remember/serving/conversation/active/factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

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

`SessionResolutionError` (L31-L35) is the typed base; `UnknownSessionError` 404,
`UnsupportedSessionError` 409 `unsupported`, `ControlUnavailableError` 503
`control-unavailable` (L38-L50) are the wire-visible refusals. `resolve_running_entry`
(L63-L76) mirrors the serving idiom: the catalog row must exist, be `running`, be a `harness`
kind with a `control_endpoint`, and be alive on the terminal host. `build_identity` (L79-L105)
selects the harness projector via `projector_for`, requires the snapshot's proven
`vendor_session_id`, assembles the `ActiveConversationRef` (harness, vendor conversation,
project scope from the catalog cwd, AR session id, bridge epoch), and stamps the server-issued
`identity_digest` — an HMAC-SHA256 over the canonical identity tuple (`identity_digest`
L53-L60), recomputable for comparison, never accepted from a client. `current_bridge_epoch`
(L108-L114) and `live_snapshot` (L117-L123) wrap the validated IPC reads and map
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

## Docs References

The resolved `Domain Documentation` registry has no entries. The production seam contracts are
repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this factory. | — | — |

## Repo-Internal References

The validated IPC client owns the authority/snapshot reads; the catalog owns the row shape; the
projector registry owns per-harness mapper selection; the service drives this factory per wire.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `read_submission_authority` and `read_control_snapshot` are the validated exact-session IPC reads used here. | L86-L118 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| `AdapterSnapshot.vendor_session_id` is the proven native identity the factory requires. | L141-L160 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The catalog row supplies status, kind, control endpoint, tmux name, and cwd. | L51-L80 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| `projector_for` returns `None` for harnesses without a projector, failing resolution typed. | L119-L120 | [__init__.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/__init__.py) |

## Cross-Repo References

No cross-repository implementation participates in this factory.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/active/factories.py` since the L2 base commit is
  the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 6 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `harness_control_client.py`, `terminal_catalog.py`; those ranges
  shifted because this task edited those files, so treat the cited numbers as approximate and the
  linked cards as authoritative.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the running-session
  factory — catalog resolution, live identity proof, server-issued digest, typed refusals.
  Verification is blank because the new source file is uncommitted; closeout owns its first
  source stamp.
