# mcp/src/agents_remember/serving/conversation/active/factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

## Docs References

The resolved `Domain Documentation` registry has no entries. The production seam contracts are
repository-owned and cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this factory. | — | — |

## Repo-Internal References

The validated IPC client owns the authority/snapshot reads; the catalog owns the row shape; the
projector registry owns per-harness mapper selection; the service drives this factory per wire.

| Finding | Anchor | Source |
| --- | --- | --- |
| The validated exact-session IPC reads used here. | "def read_submission_authority(self"; "def read_control_snapshot(entry: ControlledSession) -> AdapterSnapshot:  # pragma: no cover" | mcp/src/agents_remember/serving/harness_control_client.py:642-642; mcp/src/agents_remember/serving/harness_control_client.py:133-133 |
| `AdapterSnapshot.vendor_session_id` is the proven native identity the factory requires. | `AdapterSnapshot` | mcp/src/agents_remember/models/conversations/control_wire.py:126-151 |
| The catalog row supplies status, kind, control endpoint, tmux name, and cwd. | "def from_json(cls" | mcp/src/agents_remember/models/terminal_catalog.py:80-510 |
| `projector_for` returns `None` for harnesses without a projector, failing resolution typed. | `projector_for` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:122-123 |

## Cross-Repo References

No cross-repository implementation participates in this factory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 8 citation claims and preserved verification metadata.

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
