# mcp/src/agents_remember/serving/conversation/library/pi.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/pi.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this internal port.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The ports suite proves rows/paging, role/tool/notice mapping, and session-file argv targets on
fake helpers; the installed suite proves the live gate, the round-trip, and the real end-to-end
open; the locked helper implements the native seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pi read maps roles, tools, and notices; resolve mints the session-file argv target on fake helper boundaries. | "def test_read_maps_roles_tools_and_notices(self) -> None:"; "def test_resolve_mints_session_file_argv(self) -> None:" | mcp/tests/test_conversation_library_ports.py:684-684; mcp/tests/test_conversation_library_ports.py:709-709 |
| The installed suite proves the live helper gate, list/read/resolve round-trip, and the real Pi open with exact identity and retirement. | "def test_live_helper_gate_supports_pi_history(self) -> None:"; "def test_live_list_read_resolve(self) -> None:"; "def test_open_real_pi_session_proves_exact_identity(self) -> None:" | mcp/tests/test_conversation_library_installed.py:237-237; mcp/tests/test_conversation_library_installed.py:254-254; mcp/tests/test_conversation_library_installed.py:394-394 |
| The locked helper's SessionManager list/branch-read/session-file resolution implementations. | "export async function handlePi(request: HelperRequest): Promise<unknown> {"; "async function listPiSessions("; "async function readPiSession("; "async function resolvePiResumeTarget(" | mcp/native_helpers/conversation_library/src/pi.ts:54-54; mcp/native_helpers/conversation_library/src/pi.ts:69-69; mcp/native_helpers/conversation_library/src/pi.ts:101-101; mcp/native_helpers/conversation_library/src/pi.ts:133-133 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local port.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `test_conversation_library_installed.py`. The live Pi helper gate + list/read/resolve round-trip now
  read at L217-L263 and the real-open E2E class `PiOpenEndToEndTests` at L284-L413 (was
  `L215-L262; L360-L479`, which now lands inside the Codex open E2E). Both ranges read back.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R4 version-gate removal — recorded the
  contract-only gate doctrine now stated in the docstring: the helper handshake reports observed
  runtime/helper versions as informational evidence only, and the succeeding native `list`/`getBranch`
  operation is the sole proof (never a version-string comparison; a drift never demotes the surface).
  Change uncommitted; closeout re-stamps verification.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the helper-backed Pi port sidecar.
  Verification is blank until closeout commits and stamps the new source.
