# mcp/src/agents_remember/serving/conversation/active/projector/references.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/references.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Mints stable public-safe coordinates for live evidence, native history, and transcript echoes.

## Code Commentary

### Logic

`ProjectionEvidenceRefs` derives a short epoch prefix and formats `ar-ev`, `ar-native`, and
`ar-echo` reference strings. It stores no payload and performs no I/O.

### Conventions

References identify evidence coordinates; they are not source cursors or authorization tokens.

### Invariants And Boundaries

- Raw harness payloads never enter a reference.
- The bridge epoch scopes all coordinates to one authority generation.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| References are attached during native and echo ingestion. | [native_ingestion.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py), [echo_ingestion.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the evidence-reference
  sidecar. Verification metadata remains blank until commit.
