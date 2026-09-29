# mcp/tests/test_knowledge_file_canonical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_file_canonical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `overview.md` |

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

The cases cover `canonical.py` and `cli/knowledge_format.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Idempotence and content preservation. | `test_formatter_is_idempotent_and_preserves_content` | mcp/tests/test_knowledge_file_canonical.py:30-47 |
| Only declared positions are sorted. | `test_only_identified_entry_positions_are_sorted` | mcp/tests/test_knowledge_file_canonical.py:50-65 |
| Content-changing input is refused. | `test_formatter_refuses_input_it_cannot_reformat_without_changing_content` | mcp/tests/test_knowledge_file_canonical.py:78-82 |
| The command's exit codes and skip rules. | `test_knowledge_format_command_checks_rewrites_and_skips_caches` | mcp/tests/test_knowledge_file_canonical.py:85-120 |
| Lane registration. | "mcp/tests/test_knowledge_file_canonical.py" | mcp/tests/test-evidence-lanes.toml:96-96 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is exercised. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
