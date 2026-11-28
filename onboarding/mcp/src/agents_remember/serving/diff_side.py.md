# mcp/src/agents_remember/serving/diff_side.py

## Governing Overview

[overview](overview.md)

## Purpose

Classifies each present diff side as text, supported media or other binary content, attaches per-side server-computed UTF-16 syntax highlights, and assembles `FileDiff` wire payloads.

## Code Commentary

An absent side stays absent. Supported media returns type and size metadata without first loading its payload. Other content is checked for binary data before text decoding. Working and committed sources keep their own selected identities. `side_with_highlights` serializes an optional `SideContent` with `"highlights": None` for binary/media sides and `highlights_wire_for(...)` for text sides. `file_diff_payload(*, scope, memory, path, sides, code_repo_root=None)` centralizes `FileDiff` wire assembly across all changeset diff endpoints, resolving display language from the catalog (ignoring `code_repo_root` when `memory=True`) and attaching independent per-side highlights.

## Relationships

Change-set JSON routes (`serving/changeset.py` `file_diff`, `master_file_diff`, `leaf_file_diff`, and `serving/changeset_comparison.py`) use `file_diff_payload` and `side_with_highlights`. Media bytes travel through the selected-side bytes route; metadata is not an implicit payload read.

## Evidence

- Classifies each present diff side as text, media, or binary and assembles `FileDiff` wire responses with catalog language and per-side highlights. [1]
