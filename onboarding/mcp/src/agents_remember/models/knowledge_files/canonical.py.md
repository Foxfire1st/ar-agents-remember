# mcp/src/agents_remember/models/knowledge_files/canonical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/canonical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../overview.md` |

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
  (`realizes`, `proves`, `rows`) **and** every element is an object with a string `id`. Every other
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

`rows` anticipates MIK-R07 history files; if their schema names the array differently this set must follow.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The formatter command and the tests are the consumers.

| Finding | Anchor | Source |
| --- | --- | --- |
| Only the declared positions are sorted. | `IDENTIFIED_ENTRY_KEYS` | mcp/src/agents_remember/models/knowledge_files/canonical.py:27-27 |
| Strict parsing refuses content-changing input. | `parse_json` | mcp/src/agents_remember/models/knowledge_files/canonical.py:46-56 |
| The sort rule. | `canonical_value` | mcp/src/agents_remember/models/knowledge_files/canonical.py:65-80 |
| The serialization. | `canonical_text` | mcp/src/agents_remember/models/knowledge_files/canonical.py:83-89 |
| Idempotence and content preservation are tested. | `test_formatter_is_idempotent_and_preserves_content` | mcp/tests/test_knowledge_file_canonical.py:30-47 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
