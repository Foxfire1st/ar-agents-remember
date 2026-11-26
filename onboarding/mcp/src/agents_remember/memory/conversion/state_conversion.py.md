# mcp/src/agents_remember/memory/conversion/state_conversion.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Plans one-time conversion of legacy record state and evidence for the retained revisions, and defines the shared `state_conversion_only` predicate used by the knowledge worklist to recognize conversion-only record JSON diffs.

## Code Commentary

- `state_conversion_only(base_raw, candidate_raw)` (with `_parse_json_object` and `_validated_stamp`) returns `True` only when both sides decode as UTF-8 JSON objects, the base text matches `canonical_text(base)`, removing any `status` in `LEGACY_STATE_WORDS` and adding a `WriterStamp`-validated `writer` (when absent in base) changes the document, and `canonical_text(expected).encode("utf-8") == candidate_raw`.
- Byte-identical inputs, non-canonical formatting, non-legacy `status` edits, changes or removals of an existing `writer`, partial conversions, invalid stamps, and any other field edits return `False`.

## Evidence

- Conversion plans the complete content update without changing record meaning. [1]
- Usable historical review facts are selected before the conversion updates the memory tree. [2]

- `state_conversion_only` applies legacy status removal and validated writer-stamp addition to canonical base JSON and compares canonical bytes against candidate. [3]
- `_parse_json_object` and `_validated_stamp` enforce UTF-8 JSON object parsing and `WriterStamp` schema validation for the predicate. [4]
