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

## Evidence

- Idempotence and content preservation on the untidy document. [6]
- Only declared positions are sorted. [7]
- The seven refused inputs, three of them repeated keys. [8]
- The command's exit codes and skipped files. [9]
- The hook under test. [10]
