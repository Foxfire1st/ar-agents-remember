# mcp/src/agents_remember/serving/conversation/library/pi.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The dormant Pi library port: helper-backed list/read/resolve through the repository-owned
locked helper (`@earendil-works/pi-coding-agent@0.80.7` `SessionManager.list` / `open` +
`getBranch`), where the durable Pi entry id anchors native item identity and reading never
calls `switch_session` on any running process.

## Code Commentary

### Logic

`PiConversationLibrary.list` verifies the signed list cursor, calls the helper's `list`,
derives the catalog generation from the helper's store signature, and mints rows keyed by
session id with title preference `name`/`firstMessage` and the native ISO `modified`
timestamp. `read` verifies the read cursor, calls the helper's `read`, and maps entries by
type: `message` records by role (user unknown-input lane with text/unknown blocks; assistant
with text/thinking/toolCall blocks; toolResult as correlated tool-result items), and the notice
family (thinking level, model change, compaction, branch summary, session info, label, custom
extension messages) as system notices — unknown entry types and unrenderable content become
explicit `unknown-vendor` evidence. `resolve_resume_target` re-proves identity, resolves the
session file through the helper, and mints the server-private argv target
`--session <sessionFile>`.

### Conventions

Constructed per request with the caller's server-resolved authorization binding; the port never
authorizes. The helper handshake reports observed runtime/helper versions as informational evidence
only — since 260718-CHATS-L5F R4 the contract is the only gate: the native `list`/`getBranch`
operation succeeding is the proof, never a version-string comparison. Pi native append-only entries
are the complete session line, tool records included, so historical and tool completeness are honest
`supported` once that production contract probe passes.

### Invariants And Boundaries

- Reading a dormant conversation opens the session file read-only through the helper; open
  starts a new AR session — no in-place identity mutation on any process (design section 10.4).
- Records without a stable 1-based ordinal, valid pages without window evidence, and identity
  mismatches fail closed as typed errors.
- Unknown entry types keep `phase: "unknown"` with safe summaries; nothing is flattened into
  guessed semantics.
- The contract is the only gate: a runtime/helper version drift never demotes the surface; the
  succeeding native `list`/`getBranch` operation is the proof (L5F R4).

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal port.

No configured domain documentation was available.

### Repo-Internal References

The ports suite proves rows/paging, role/tool/notice mapping, and session-file argv targets on
fake helpers; the installed suite proves the live gate, the round-trip, and the real end-to-end
open; the locked helper implements the native seam.

- The Pi library maps durable entries and mints the verified session-file resume target without switching a running session. [1]
Historical evidence (retired with the d3610903 suite reduction): The installed suite historically exercised the live helper gate, list/read/resolve round-trip, and the real Pi open with exact identity and retirement. These removed artifacts provide no current execution or capability-enablement proof.
- The locked helper's SessionManager list/branch-read/session-file resolution implementations. [2]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

No meaningful cross-repo references found.
