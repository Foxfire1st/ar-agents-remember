# mcp/tests/test_codex_history_production_path.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_history_production_path.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Replays the original 4,846,576-byte failure through the production-shaped Codex stdio, capability
probe, adapter, Unix control IPC, and selected-child active projection path while proving second-wave
failure containment and sibling/parent continuity.

## Code Commentary

### Logic

One fake app-server process emits the exact measured below-fuse response. The test observes
items-list `-32601`, turns/full success, and no legacy `thread/read`. It then introduces a cyclic
second-wave child and a healthy sibling: only the cyclic child becomes unavailable, while the first
child, second sibling, parent control, and event path remain usable.

### Conventions

This is deliberately a composed seam rather than another unit fixture. Its exact payload size and
request transcript protect the diagnosed transport/projection interaction.

### Invariants And Boundaries

- The measured valid payload must cross the shared transport.
- Installed 0.145-shaped evidence is items unsupported and turns accepted; the test must never claim
  that both bounded methods succeed.
- Child failure remains a typed local projection state and never tears down the parent bridge.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The protocol accepts valid payloads through the separate 128 MiB emergency fuse. | L18-L23; L217-L240 | [codex_app_server_protocol.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_protocol.py) |
| The active projector hydrates only selected children and contains typed failures. | L502-L635 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |

## Cross-Repo References

The fake Codex process is repository-local; no external repository is executed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the exact
  measured-size production seam and second-wave continuity regression. Verification metadata
  remains blank because the new test is uncommitted.
