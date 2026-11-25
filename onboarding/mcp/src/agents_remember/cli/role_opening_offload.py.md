# mcp/src/agents_remember/cli/role_opening_offload.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Enforces `settings.role_message_limit` on Turn-1 dynamic appendices (direct `opening_message` and held-seat opening batches), writing over-limit text to deterministic read-only sidecars beside the launch report and verifying or restoring direct opening sidecars on replay.

## Code Commentary

`resolve_role_message_limit(config, *, repo_id)` reads `load_agentic_settings(config.coordination_root, repo_root=...).role_message_limit`, binding `repo_root` when `repo_id` is in `config.repositories` and otherwise using coordination settings; `selection_repo_id(selection)` inspects `taskDocumentRef`, `masterDocumentRef`, and `sprintDocumentRef` in that order. Invalid settings propagate `AgenticSettingsError`.

`format_bounded_appendix(full_text, *, limit, pointer_line)` rejects `bool` or `limit < 1` with `ValueError`. When `len(full_text) <= limit`, it returns `full_text` unchanged with no sidecar. When exceeded, it caps the inline preview to `<= limit` Unicode characters (`full_text[:limit - 3] + "..."` for `limit >= 4`, or an empty preview for `limit` in `1..3`) followed by one exempt pointer line.

For direct launches, `prepare_direct_opening_message(report_path, opening_message, *, limit)` plans `<report_stem>.opening-message.md` and returns `{path, canonicalPath, sha256, bytes, content}` for receipt storage (`openingMessageArtifact`), with `preflight_opening_message_artifact` and `write_opening_message_artifact` writing read-only exact-byte-idempotent files through `immutable_artifact`. On replay, `checked_opening_message_target` returns `None` when absent, refuses malformed receipt/report metadata, rebound paths, mismatched sizes or digests, or a missing `Opening message file: <path> (SHA-256 <sha256>)` line in `message`, and `restore_opening_message_artifact` restores a missing file from verified receipt bytes.

For held seats, `prepare_held_opening_batch(config, receipt, batch_text)` resolves `role_message_limit` at open time from `receipt["selection"]` and, when `len(batch_text) > limit`, writes content-addressed `<report_stem>.held-batch-<sha256>.md` via `preflight` and `write_once`, appending `Held opening messages file: <path> (SHA-256 <sha256>)`. Equivalent batch bytes reuse the existing file; distinct batches write distinct filenames; conflicting bytes or nonregular targets raise `ValueError`.

This module never truncates or offloads the static brief, filtered `every-role.md`, compiled capsule, or handover projection.

## Relationships

- Depends on `cli/immutable_artifact.py` (`canonical_path`, `preflight`, `write_once`), `kernel/agentic_settings.py` (`load_agentic_settings`), and `kernel/primitives/runtime_config.py` (`McpRuntimeConfig`).
- Called by `cli/role_launch_routes.py::_launch_prepared_role_session` (direct opening preflight/write and receipt storage), `cli/role_handover_restore.py::restore_launch_files` (replay verification, preflight, and restore), and `cli/role_held_messages.py::_open_held_seat` (held-seat opening batch capping).
- `worktrees/role_reports.py::_launch_carrier` excludes `.opening-message.md` and `.held-batch-*.md` from canonical execution reports.

## Evidence

- `resolve_role_message_limit` and `selection_repo_id` resolve `role_message_limit` from repository or coordination settings in task/master/sprint reference order. [1]
- `format_bounded_appendix` bounds Unicode inline previews strictly to `limit >= 1` (empty preview for `limit < 4`) with one exempt pointer line. [2]
- `prepare_direct_opening_message`, `preflight_opening_message_artifact`, and `write_opening_message_artifact` plan and publish read-only `.opening-message.md` sidecars via `immutable_artifact`. [3]
- `checked_opening_message_target` and `restore_opening_message_artifact` validate receipt `openingMessageArtifact` evidence and restore missing sidecars from verified receipt bytes. [4]
- `prepare_held_opening_batch` enforces open-time `role_message_limit` and writes content-addressed `.held-batch-<sha256>.md` sidecars via `preflight` and `write_once`. [5]
