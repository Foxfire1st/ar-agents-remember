# mcp/tests/test_conversation_library_agents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_agents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Library sub-agent grouping tests with fake native boundaries: codex
sub-agent threads list through the probed camelCase `sourceKinds` vocabulary and group
client-side under their parent's row via `parentThreadId`; claude `subagents/agent-*.jsonl` +
`.meta.json` children group under their parent session row with meta-bound identity.
Unproven shapes stay visibly unavailable through `agents_note` — never silently absent,
never guessed.

## Code Commentary

### Logic

cit:([`CodexLibraryAgentTests`], mcp/tests/test_conversation_library_agents.py:256-412) drives `CodexConversationLibrary` over a canned
app-server transport that dispatches `thread/list` by `sourceKinds`: the additive agent
fetch uses exactly the probed `_AGENT_SOURCE_KINDS` tuple (`subAgent`,
`subAgentReview`, `subAgentCompact`, `subAgentThreadSpawn`, `subAgentOther` — pinned
against the vendored `ThreadSourceKind` enum and a live 0.145.0 probe) while the top-level
fetch does not; agent rows group under their parent with evidence-bound identity
(nickname/role/agent_path from the wire) or the honest `agent <short-id>` fallback; the
agent conversation key mints the agent's OWN native identity so opening it reads the agent
thread via `thread/read`, not the parent's; a vendor refusal of the agent kinds degrades
to the exact `agents_note` while top-level listing still works; a truncated agent listing
is visible; nested depth-2 agents (parent is itself an agent thread) can never group under
a visible top-level row and are NAMED in the note, not silently absent (fix-round finding
7); and an ungroupable agent row (no `parentThreadId`) fails closed as a shape-validation
store error.

cit:([`ClaudeLibraryAgentTests`], mcp/tests/test_conversation_library_agents.py:471-648) drives `ClaudeConversationLibrary` over a fake
helper host: per-row `agents` children group under the parent session with identity from
`.meta.json` evidence only (description/role/join key) or the `agent <short-id>` fallback;
the agent key round-trips to the composite `<sessionId>/<agentId>` vendor id; a helper
response WITHOUT the `agentsEnumerated` marker degrades to the visible "no sub-agent
evidence" note — including over an EMPTY catalog, where no row exists to carry per-row
evidence (fix-round finding 11) — while an enumerated-but-empty catalog stays quiet; an
agent read routes through the helper with the composite id split into
`vendorConversationId` + `agentId`; an agent resume target fails closed with the exact
reason and no helper call; and an agent row without an id fails closed.

### Conventions

Fake boundaries record every call so channel discipline (exact `sourceKinds`, payload
split) is asserted, not just outcomes. All capabilities are scripted `supported` via a
shared `_caps()` helper; scope is a temp-dir canonical library scope per test. The codex
fixture injects its fake boundary through one `AppServerSeams(env=..., transport_factory=...)`
value rather than two loose `CodexConversationLibrary` keywords.

### Invariants And Boundaries

- Identity is evidence-bound: nickname/role/path come from the wire or meta file; the
  fallback label is `agent <short-id>`, never a fabricated name.
- Degradation is visible: unproven or truncated agent evidence surfaces through
  `agents_note`; silently absent agents are a bug.
- Opening an agent conversation reads the agent's own native thread/transcript.
- Shape-skewed agent payloads fail as typed store errors, never raw exceptions.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the vocabularies are proven against the
vendored codex enum and the installed claude on-disk layout.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The codex library under test: additive agent fetch, client-side grouping, agent read, agents_note degrade paths. | `CodexConversationLibrary` | mcp/src/agents_remember/serving/conversation/library/codex.py:265-668 |
| The claude library under test: per-row agent grouping, marker degrade, composite-id read split, resume refusal. | `ClaudeConversationLibrary` | mcp/src/agents_remember/serving/conversation/library/claude.py:80-424 |
| The helper-side sub-agent enumeration and agent transcript read the claude port consumes. | `listSubagents`, `readClaudeAgentTranscript` | mcp/native_helpers/conversation_library/src/claude.ts:180-204; mcp/native_helpers/conversation_library/src/claude.ts:313-369 |
| The signed cursor authority minting and verifying the agent conversation keys. | `LibraryCursorAuthority` | mcp/src/agents_remember/serving/conversation/library/cursor.py:62-297 |
| The empty-page agent fetch added to the shared ports fake boundary. | `_FakeCodexTransport` | mcp/tests/test_conversation_library_ports.py:67-121 |

## Cross-Repo References

The codex `sourceKinds` vocabulary is proven against the vendored `ThreadSourceKind` enum
(and a live 0.145.0 app-server probe); the vendor's own `parentThreadId` list filter is
experimental-gated on 0.145.0, which is why grouping is client-side.

| Finding | Anchor | Source |
| --- | --- | --- |
| The camelCase sub-agent `ThreadSourceKind` variant the agent fetch pins. | ["subAgentReview"] | mcp/src/agents_remember/serving/conversation/library/codex.py:74-74 |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 6 repository-internal references for the Codex and Claude libraries, helper agent enumeration/read, cursor authority, shared fake boundary, and the pinned camelCase source-kind literal; final scoped result 0 (checker-clean).

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: a prose line had been hard-wrapped at a ` + ` conjunction, leaving the plus at column zero where markdown reads `+ ` as a list bullet, so a wrapped sentence rendered as a spurious new list item mid-thought. The plus moved to the end of the previous line; the rendered prose is character-for-character unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the codex fixture now builds its library with
  `seams=AppServerSeams(env=..., transport_factory=...)` instead of the two loose keywords, so
  the Conventions paragraph names that parameter object; the import addition plus several `ruff
  format` joins shifted both class anchors, and the Logic ranges were re-verified against the
  current file and corrected (`CodexLibraryAgentTests` L257-L416 to L256-L412,
  `ClaudeLibraryAgentTests` L475-L656 to L471-L648). No test case was added, removed, or renamed
  and every grouping, identity, degrade, and fail-closed claim still matches the source.

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new
  library sub-agent grouping suite (fix-round findings 7/11 pins). Verification is blank
  because the new source file is uncommitted; closeout owns its first source stamp.
