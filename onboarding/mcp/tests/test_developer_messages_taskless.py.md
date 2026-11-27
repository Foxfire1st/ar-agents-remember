# mcp/tests/test_developer_messages_taskless.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers recipient-only developer tray sends: unified `developer-messages/taskless/<agent_id>/` filing, non-blocking optional `repository` context across single-, multi- and zero-repository servers, and backwards-compatible read-back, deduplication and held settlement for legacy `<repository>/taskless/<agent_id>/` files.

## Code Commentary

### Logic

`TasklessDeveloperSendTests` exercises `target_folder`, `read_developer_message` and `POST /api/role-chats/{agent_id}/message` through `register_developer_chat_routes` against a fake host runtime (`RoleToolsTestCase`):

- `test_target_folder_routes_taskful_and_taskless_recipients` checks `<repo>/<task>/` for taskful recipients and `taskless/<agent_id>/` whenever repository or task id is absent.
- `test_taskless_send_without_repository_succeeds_across_server_repo_counts` checks taskless sends with omitted or `None` repository deliver and store pick blobs under `taskless/<agent_id>/` on single-repo, multi-repo and zero-repo server configs.
- `test_unknown_request_repository_never_blocks_taskful_or_taskless_sends` checks an unconfigured `request.repository` string never blocks taskful or taskless sends and creates no folder under that name.
- `test_legacy_repo_scoped_taskless_files_read_back_dedupe_and_settle` checks existing `<repo>/taskless/<agent_id>/` files remain readable by id, enforce `message-id-reused` before host send, and settle held rows to `.undelivered.md`.

### Invariants And Boundaries

Uses `RoleToolsTestCase`'s fake Paseo runtime and temporary coordination roots rather than a live host daemon. Source-declared test assertions are not execution receipts.

## Evidence

- Checks `target_folder` routing for taskful and taskless targets. [1]
- Checks taskless sends without `repository` succeed across single-, multi- and zero-repository server configurations. [2]
- Checks an unknown `request.repository` string never blocks taskful or taskless sends and creates no folder. [3]
- Checks legacy repo-scoped taskless files still read back, refuse reused message ids and settle held undelivered rows. [4]
