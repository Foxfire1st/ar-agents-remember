# mcp/src/agents_remember/cli/role_handover_restore.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Restores a saved launch's hand-over files and optional direct opening-message sidecar before its first message is sent again, from the receipt alone, and puts target-check refusals in one type the callers understand.

## Code Commentary

`restore_launch_files` checks every reference and every target before the first byte is written, so a refusal leaves the receipt and all its files untouched and says what must be put right. It validates `handoverFile` first (preserving complete-file diagnostic priority), then `handoverArtifact` (using `resolve_handover_envelope`, also re-exported here, which accepts both suffix and legacy-prefix boundaries), then optional `stepUpArtifact`, and then optional `openingMessageArtifact` (`role_opening_offload.checked_opening_message_target`), preflights every target before writing, and restores any missing files together. A missing request locator is rebuilt at the folder the receipt recorded by the artifact check before the frozen instruction details are validated, so validation sees the same locator the launch published and an altered or rebound detail refuses before any file is restored. `HandoverFileRefusal` is a `ValueError` wrapping target-validation refusals so the held-seat opener returns `cannot-open` and releases its delivery claim while the retry route returns HTTP 409; preflight and detail-validation refusals raise `ValueError` directly. `saved_handover_file` reads the receipt's recorded reference for one path and returns `None` only when the `handoverFile` key is absent; a present non-object value refuses. That accessor result does not grant legacy replay: the receipt owner still enters full restoration whenever `handoverArtifact` or `handoverFile` is recorded.

## Evidence

- A receipt without the second file's reference reports none rather than inventing one. [3]

- `HandoverFileRefusal` wraps target-validation refusals in a `ValueError` recognized by the held opener and retry route, while preflight and detail checks raise `ValueError` directly. [1]
- `restore_launch_files` checks `handoverFile`, `handoverArtifact`, `stepUpArtifact`, and `openingMessageArtifact`, preflights all targets, validates details, and restores missing files together. [2]
