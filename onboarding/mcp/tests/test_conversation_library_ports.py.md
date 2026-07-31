# mcp/tests/test_conversation_library_ports.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_ports.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

The `_FakeCodexTransport` boundary (L97-L103) also covers the library's additive sub-agent
fetch: a `thread/list` whose
`sourceKinds` is outside the plain top-level vocabulary answers an empty page at this fake
boundary, keeping these dormant port cases green while the agent-grouping suite
(`test_conversation_library_agents.py`) owns the non-empty sub-agent cases. That fake transport and
a stubbed environment reach the Codex library through a single `AppServerSeams(env=...,
transport_factory=...)` object in `_codex_library` (L141-L151), not as two loose constructor
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Codex direct port and its thread-item parser under test. | L265-L401; L40-L59 | [codex.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/codex.py), [codex_normalize.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/codex_normalize.py) |
| The Claude and Pi helper-backed ports under test. | L87-L182; L88-L182 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/claude.py), [pi.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/pi.py) |
| The installed-runtime suite covering the same ports live. | L136-L263 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No neighboring repository participates in this ports suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
