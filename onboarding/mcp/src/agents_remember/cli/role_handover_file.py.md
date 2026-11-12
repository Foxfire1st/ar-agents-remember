# mcp/src/agents_remember/cli/role_handover_file.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Holds the complete hand-over object of one launch as the immutable JSON file the first message names, so the agent reads a field when a step needs it instead of carrying the whole object in every turn.

## Code Commentary

handover_file_text renders the object at one-space indent with a final newline. planned_handover_file computes the reference and the bytes without writing, so the message can name a file the launch has not written yet. write_handover_file publishes through the shared write-once contract and returns the path, canonical path, digest and size the receipt stores. preflight_handover_file decides a saved launch's refusal before any write, and restore_handover_file writes a lost file again from the receipt's own text alone, refusing a changed file, a mismatched text or a path that no longer leads to the recorded file.

## Evidence


- The object is rendered at one-space indent with a final newline; the serializer sets no size bound, and the reference records the byte count of what it did write. [1]

- The reference and bytes are planned without writing, so the message names what the launch will write. [2]
- The file is written once under the shared contract and reused only on equal bytes. [3]
- A lost file is restored from the receipt alone; a changed or moved one is refused before any write. [4]
