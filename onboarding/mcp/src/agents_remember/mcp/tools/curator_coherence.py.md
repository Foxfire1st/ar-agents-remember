# mcp/src/agents_remember/mcp/tools/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tool-adapter overview](overview.md)

## Purpose

Provides the one payload adapter between the public `curator_coherence` registration and its
configured application boundary.

## Code Commentary

### Logic

`curator_coherence_payload` delegates the typed request to `curator_coherence_tool` and passes the
result through the common `_tool_payload` response-model conformance boundary.

### Conventions

Adapters in this route contain no lifecycle policy. Public schema, configured admission, and
publication semantics remain in their dedicated owners.

### Invariants And Boundaries

- The adapter does not add action aliases, filename fallbacks, or alternate response shapes.
- Tool-response conformance is applied exactly once through the shared helper.

### Todos

None recorded.

## Docs References

No configured external documentation applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| This adapter is repository-internal. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter delegates one request and validates one named public result. | `curator_coherence_payload` | mcp/src/agents_remember/mcp/tools/curator_coherence.py:14-18 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository boundary is introduced. | — | — |

## Update History

- 2026-08-29T08:52+02:00 — Created for the lifecycle-owned curator-coherence tool adapter.
  Verification remains closeout-owned.
