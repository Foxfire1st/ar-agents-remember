# mcp/tests/test_conversation_library_ports.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_ports.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Dormant port normalization tests with fake native boundaries: prove the
Codex, Claude, and Pi resolvers produce the landed normalized grammar (strict
`ConversationItem` validators included), honest cursor/generation behavior, and exact resume
targets — without touching real harness processes.

## Code Commentary

### Logic

Twelve async tests drive the three ports with fake transports/helpers: Codex list maps rows,
keys, and next cursor; generation mismatch resets the cursor; reads normalize items with
ordinals and windows; shape-skewed list/read payloads fail as typed store errors (review F3);
resolve mints the exact `codex-thread-resume` target. Claude list rows and paging; a
range-absurd `lastModified` fails as a typed store error (review F4); read maps blocks, roles,
and provenance; resolve mints the `--resume` argv target. Pi read maps roles, tools, and
notices; resolve mints the `--session <file>` argv target.

The `_FakeCodexTransport` boundary (cit:([`_FakeCodexTransport`], mcp/tests/test_conversation_library_ports.py:67-121)) also covers the library's additive sub-agent
fetch: a `thread/list` whose
`sourceKinds` is outside the plain top-level vocabulary answers an empty page at this fake
boundary, keeping these dormant port cases green while the agent-grouping suite
(`test_conversation_library_agents.py`) owns the non-empty sub-agent cases. That fake transport and
a stubbed environment reach the Codex library through a single `AppServerSeams(env=...,
transport_factory=...)` object in `_codex_library` (cit:(["transport_factory="], mcp/tests/test_conversation_library_ports.py:150-150)), not as two loose constructor
keywords.

### Conventions

Fake native payloads deliberately include hostile shapes (skewed types, absurd timestamps,
unknown vendor kinds) so normalization is probed adversarially; the installed suite covers the
same ports against real harnesses.

### Invariants And Boundaries

- Normalized items must pass the strict contract validators; unknown vendor kinds surface as
  explicit `unknown-vendor` evidence, never guessed semantics.
- Corrupt-but-type-valid native payloads fail as typed store errors, never raw exceptions.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The repository sources are direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Codex direct port and its thread-item parser under test. | `CodexConversationLibrary` | mcp/src/agents_remember/serving/conversation/library/codex.py:265-668 |
| The Claude and Pi helper-backed ports under test. | `ClaudeConversationLibrary`; `PiConversationLibrary` | mcp/src/agents_remember/serving/conversation/library/claude.py:80-424; mcp/src/agents_remember/serving/conversation/library/pi.py:72-320 |
| The installed-runtime suite covering the same ports live. | `CodexInstalledTests`; `PiInstalledTests` | mcp/tests/test_conversation_library_installed.py:103-186; mcp/tests/test_conversation_library_installed.py:189-281 |

## Cross-Repo References

No neighboring repository participates in this ports suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:03:33+02:00 — W3-B05 curator: resolved 5 Tier-2 citation claims (3 table, 2 prose) with exact anchors and source paths; fixer generated all final ranges.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. Only the
  row's first range was stale: `CodexConversationLibrary` — the dormant port with the
  `AppServerSeams` constructor and the three port methods `list` / `read` /
  `resolve_resume_target` — is now `codex.py` L265-L401. The second range was already correct:
  `conversation_items_from_thread`, the thread-item parser, is still `codex_normalize.py` L40-L59.
  No claim text changed.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: followed the Codex library's seam grouping into
  the card. `_codex_library` now injects the fake app-server boundary through one
  `AppServerSeams(env=..., transport_factory=...)` object instead of the two loose
  `env`/`transport_factory` keywords, and the widened import pushed the file down two lines, so the
  `_FakeCodexTransport` sub-agent-fetch citation was re-anchored from L91-L97 to L97-L103 (verified
  against the current source) and the construction seam is now cited at L141-L151. The twelve
  async cases, the hostile-shape payloads, and the typed-store-error invariants are unchanged.
  Verification metadata stays pinned; closeout re-stamps the candidate commit.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the additive sub-agent fetch at the
  fake codex boundary (a non-top-level `sourceKinds` `thread/list` answers an empty page; the
  non-empty agent-grouping cases live in `test_conversation_library_agents.py`). Verification
  metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the dormant port normalization
  suite sidecar. Verification is blank until closeout commits and stamps the new source.
