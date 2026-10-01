# mcp/src/agents_remember/models/knowledge_files/canonical.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one canonical formatting of every knowledge JSON file (MIK-R21 rule 8).** Canonical text is
UTF-8, two-space indentation, sorted object keys, identified-entry arrays sorted by `id`, and one
trailing newline. The formatter changes formatting only; input it cannot reformat without changing
content is refused. `agents-remember knowledge-format` applies it, and the validator (MIK-R22) will
name that command when it reports a non-canonical file.

## Code Commentary

### Logic

- `parse_json` is strict: a byte-order mark, `NaN`/`Infinity`, invalid JSON and an object that
  repeats a key (which `json.loads` would silently collapse) raise `CanonicalFormatError`.
- `canonical_value` sorts an array only when it sits under a key in `IDENTIFIED_ENTRY_KEYS`
  (`realizes`, `proves`, and a history file's `rows` with each row's `covers` and `examined`, the
  last two added by MIK-R07 with the architect's leave) **and** every element is an object with a
  string `id`. Every other
  array keeps authored order — a reference's `targets` (whose ID targets also carry `id`) and a
  decision's `alternatives` (addressed by index) included. This restriction came from review R1.
- `canonical_text` dumps with `indent=2`, `sort_keys=True`, `ensure_ascii=False`, `allow_nan=False`
  and appends `\n`. `format_text`, `format_bytes` (refuses non-UTF-8) and `is_canonical` wrap it.

### Conventions

- `FORMATTER_COMMAND` is the command string other code quotes.

### Invariants And Boundaries

- **Formatting never changes content.** Parse → canonical text → parse yields the same value apart
  from the order of identified-entry arrays, which the packet defines as formatting.
- Keys sort as strings, so reference `"10"` precedes `"2"`.

### Todos

None recorded. The MIK-R21 todo about `rows` is closed: MIK-R07's `ar-history/v1` names its arrays
`rows`, `covers` and `examined`, all now in the set.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The formatter command and the tests are the consumers.

- Only the declared positions are sorted, history `covers` and `examined` included. [1]
- Strict parsing refuses content-changing input. [2]
- The sort rule. [3]
- The serialization. [4]
- Idempotence and content preservation are tested. [5]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
