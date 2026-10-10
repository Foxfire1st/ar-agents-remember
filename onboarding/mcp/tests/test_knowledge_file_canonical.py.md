# mcp/tests/test_knowledge_file_canonical.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of the canonical JSON formatter (`models/knowledge_files/canonical.py`) and of the
`knowledge-format` command. Each formatting case checks that the output is canonical and stable under a
second pass, and that the parsed value is unchanged apart from the order of identified-entry arrays.

## Code Commentary

- `test_formatter_is_idempotent_and_preserves_content` formats one deliberately untidy document (CRLF,
  unsorted keys, a non-ASCII path, unsorted `realizes`). It checks idempotence, two-space indentation,
  unescaped UTF-8, exactly one trailing newline, keys sorted as strings (`"10"` before `"2"`), `realizes`
  sorted by `id`, and `alternatives` in authored order.
- `test_only_identified_entry_positions_are_sorted` shows that `proves` and `rows` are sorted while a
  reference's `targets` and an array under an undeclared key keep their order.
- `test_formatter_refuses_input_it_cannot_reformat_without_changing_content` has seven parameter cases:
  one repeated key; two repeated keys among five pairs, where the message must be
  `repeats key(s): ['a', 'b']`; a repeated key inside a nested object; `NaN`; a byte-order mark; bytes that
  are not UTF-8; and truncated JSON. Each must raise `CanonicalFormatError` with the named reason.
- `test_knowledge_format_command_checks_rewrites_and_skips_caches` runs the command through the package's
  `main` on a temporary tree. `--check` exits 1, names the file and writes nothing. A rewrite exits 0 and
  keeps the parsed value. The route-index cache `overview.index.json` and a file in a hidden directory are
  left untouched. A file with a repeated key exits 2 and is left as it was.

### Logic

- `test_formatter_is_idempotent_and_preserves_content` formats a deliberately messy document (CRLF,
  unsorted keys, non-ASCII, unsorted `realizes`) and checks idempotence, two-space indentation, raw
  UTF-8, one trailing newline, string key order (`"10"` before `"2"`) and value equality.
- `test_only_identified_entry_positions_are_sorted` shows `proves` and `rows` are sorted while
  reference `targets` and an undeclared `other` array keep authored order (added in repair round 1;
  it fails under the earlier sort-any-`id`-array rule).
- `test_formatter_refuses_input_it_cannot_reformat_without_changing_content` covers repeated keys,
  `NaN`, a BOM, invalid UTF-8 and truncated JSON.
- `test_knowledge_format_command_checks_rewrites_and_skips_caches` runs `main(["knowledge-format",
  …])` on a temporary tree: `--check` exits 1 and writes nothing; a rewrite exits 0; the
  `overview.index.json` cache and a hidden-directory file are untouched.

### Conventions

Drives the command through the umbrella `main`, as a user would.

### Invariants And Boundaries

- Formatting must never change a parsed value beyond identified-entry order.

### Todos

None recorded.

## Evidence

- Idempotence and content preservation on the untidy document. [6]
- Only declared positions are sorted. [7]
- The seven refused inputs, three of them repeated keys. [8]
- The command's exit codes and skipped files. [9]
- The hook under test. [10]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases cover `canonical.py` and `cli/knowledge_format.py`.

- Idempotence and content preservation. [11]
- Only declared positions are sorted. [12]
- Content-changing input is refused. [13]
- The command's exit codes and skip rules. [14]
- Lane registration. [15]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is exercised.
