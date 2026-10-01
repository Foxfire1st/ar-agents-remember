# mcp/tests/test_knowledge_file_canonical.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R21 rule 8: the canonical formatter and the `knowledge-format` command.** Each case checks
that output is canonical and stable under a second pass, and that the parsed value is unchanged apart
from identified-entry order. Registered in the `unit-regression` lane.

## Code Commentary

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

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases cover `canonical.py` and `cli/knowledge_format.py`.

- Idempotence and content preservation. [1]
- Only declared positions are sorted. [2]
- Content-changing input is refused. [3]
- The command's exit codes and skip rules. [4]
- Lane registration. [5]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is exercised.
