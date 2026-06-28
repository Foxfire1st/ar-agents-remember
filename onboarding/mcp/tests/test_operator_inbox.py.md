# mcp/tests/test_operator_inbox.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/test_operator_inbox.py`    |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-06-25T13:20+02:00                |
| lastVerifiedCommitHash |                                       `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                       2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Focused backend tests for the external-chat operator inbox record, store, and
MCP payload builders.

## Code Commentary

### Logic

`OperatorInboxRecordTests` covers pure create/consume snapshots, address
validation, and schema alias round-trip. `OperatorInboxStoreTests` verifies
pending filtering by lifecycle, agent, and both keys; the lower-level store consume path appends a
consumed snapshot and repeated consume calls are idempotent. Task 23/24 adds the public payload
semantics: `operator_inbox_consume_payload` returns the consumed entry and then physically deletes the
throwaway pending row from the public inbox log. `OperatorInboxToolTests` patches `_store` to an in-memory temp
store and drives the real post, poll, and consume payload builders.

### Conventions

Tests mirror the gate control-plane test style: temporary directories, patched
store factories for payload-builder tests, and direct assertions on modeled
payload dictionaries.

### Invariants And Boundaries

- A mailbox post/poll must include `lifecycle_id` or `agent_id`.
- Store-level consume preserves an auditable snapshot for direct store users, while the public MCP consume
  payload deletes the throwaway pending row after returning it.
- Tool tests exercise payload builders, not FastMCP transport.

### Todos

None.

## Docs References

No relevant external documentation found after checking the in-repo design docs
listed as Domain Documentation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Record tests cover create/consume purity, required addressing, and schema alias round-trip. | L22-L74 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |
| Store tests cover lifecycle/agent filters, idempotent consume, missing entry, and missing address errors. | L77-L163 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |
| Tool tests cover post, poll, consume payload deletion, and no-address poll validation. | L166-L220 | [test_operator_inbox.py](agents-remember/mcp/tests/test_operator_inbox.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-06-25T13:20+02:00 — Task 23/24: added coverage that the public consume payload deletes throwaway pending inbox entries after returning them.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: focused tests for record snapshots, store filtering/idempotent consume, and payload builders. Verification metadata pinned until closeout stamps the task-10 code commit.
