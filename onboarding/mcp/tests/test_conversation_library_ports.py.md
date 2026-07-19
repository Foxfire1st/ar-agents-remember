# mcp/tests/test_conversation_library_ports.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_ports.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Dormant port normalization tests for 260718-CHATS-L2 with fake native boundaries: proves the
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
| The Codex direct port and its thread-item parser under test. | L232-L322; L40-L59 | [codex.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/codex.py), [codex_normalize.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/codex_normalize.py) |
| The Claude and Pi helper-backed ports under test. | L87-L182; L88-L182 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/claude.py), [pi.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/pi.py) |
| The installed-runtime suite covering the same ports live. | L134-L262 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No neighboring repository participates in this ports suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the dormant port normalization
  suite sidecar. Verification is blank until closeout commits and stamps the new source.
