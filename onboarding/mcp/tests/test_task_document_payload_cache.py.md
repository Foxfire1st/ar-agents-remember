# mcp/tests/test_task_document_payload_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_payload_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Proves the task-document payload cache reparses only changed and new files and reclaims deleted
entries at two corpus sizes.

## Code Commentary

#

- 260731-EFA-L7 (trace delta): the task-document payload-cache suite is retained as a family entry of the split `test_task_document_*` modules; assertions unchanged.
## Logic

The suite counts reader calls across an initial corpus, an unchanged pass, and a pass with
changed, added, and removed files. It verifies both returned payloads and retained entry count.

### Conventions

Tests mutate real temporary file stat identities rather than mocking the cache key.

### Invariants And Boundaries

- Unchanged files produce no parser call.
- Changed and new files each parse once.
- Removed files are absent from results and retained state.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Cache under test. | "class TaskDocumentPayloadCache" | mcp/src/agents_remember/observer/task_document_cache.py:23-23 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the task-document payload-cache suite is retained as a family entry of ...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` row with an
  exact anchor and source-backed range; exact non-fixing check returns zero findings.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  task-document parse-cache regression. Verification metadata remains blank until commit.
