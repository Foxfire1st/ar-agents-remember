# mcp/src/agents_remember/models/knowledge_files/canonical.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The one canonical formatting of a knowledge JSON file: UTF-8, two-space indentation, sorted object keys,
arrays of identified entries sorted by `id`, and one trailing newline. The formatter changes formatting
only and refuses input it cannot reformat without changing content. `FORMATTER_COMMAND`
(`agents-remember knowledge-format`) is the command other code names.

## Code Commentary

- `parse_json` is strict. A byte-order mark, invalid JSON, `NaN` or `Infinity`, and an object that repeats
  a key each raise `CanonicalFormatError`.
- `_refuse_duplicate_keys` is the object hook of that parse and runs once for every JSON object. It builds
  the dictionary first and counts keys only when the dictionary came out shorter than the list of pairs,
  which is exactly the case of a repeated key. The refusal then names every repeated key in sorted order:
  `object repeats key(s): [...]`. An object without a repeated key costs one dictionary construction.
- `canonical_value` sorts an array by `id` only when it sits under one of `IDENTIFIED_ENTRY_KEYS`
  (`realizes`, `proves`, `rows`, `covers`, `examined`) and every element is an object with a string `id`.
  Every other array keeps its authored order, including a reference's `targets` and a decision's
  `alternatives`.
- `canonical_text` dumps with `indent=2`, `sort_keys=True`, `ensure_ascii=False` and `allow_nan=False` and
  appends one newline. Keys sort as strings, so `"10"` comes before `"2"`.
- `format_text`, `format_bytes` (which refuses bytes that are not UTF-8) and `is_canonical` wrap these.

## Evidence

- The positions whose arrays are sorted. [6]
- The duplicate-key hook builds the dictionary first and counts only on a collapse. [7]
- The strict parse. [8]
- The sort rule. [9]
- The serialization. [10]
- Bytes that are not UTF-8 are refused. [11]
- Repeated keys are refused, with every repeated key named and also inside a nested object. [12]
- Formatting is idempotent and keeps the parsed value. [13]
- Only the declared positions are sorted. [14]
