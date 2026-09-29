# mcp/src/agents_remember/cli/knowledge_format.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_format.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-format [--check] PATH...`: the command that applies the canonical
knowledge formatting (MIK-R21 rule 8).** Each PATH is a file or a directory; a directory contributes
every `*.json` below it except the generated route-index cache (`*.index.json`) and anything under a
hidden directory (such as `.ar-index`). It is the command the validator (MIK-R22) will tell an author
to run on a non-canonical file.

## Code Commentary

### Logic

- `add_arguments` declares `paths` (one or more) and `--check`.
- `iter_json_files` yields a named file as-is, and for a directory the sorted `rglob("*.json")`
  minus cache files and hidden-directory members.
- `run` reads each file, formats it with `canonical.format_bytes`, and: on `OSError` or
  `CanonicalFormatError` prints `invalid <path>: …` and sets status 2 (file untouched); if already
  canonical, continues; with `--check` prints `not canonical <path>` and sets status ≥1; otherwise
  rewrites with `kernel.atomic_write.atomic_write_bytes` and prints `reformatted <path>`.

### Conventions

- Registered in `cli/__main__.py` with the umbrella's declarative `add_arguments` +
  `set_defaults(func=run)` pair; the adapter owns its flags and exit codes.

### Invariants And Boundaries

- Exit status: 0 all canonical (after rewriting), 1 `--check` found a non-canonical file, 2 a file
  could not be read or parsed. `--check` writes nothing.
- It formats only; it validates nothing and changes no content.
- **Nothing in the installed runtime reads or writes these files before MIK-R37.** The package is
  reached only from `agents-remember knowledge-format` and the tests; the live memory repository
  is still read and written through the SQLite knowledge store until the layout switch.

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

The formatting rules live in the model package; this adapter only walks paths and writes.

| Finding | Anchor | Source |
| --- | --- | --- |
| Arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_format.py:27-33 |
| Cache files and hidden directories are skipped. | `iter_json_files` | mcp/src/agents_remember/cli/knowledge_format.py:36-49 |
| Exit statuses and the atomic rewrite. | `run` | mcp/src/agents_remember/cli/knowledge_format.py:52-70 |
| Registration in the umbrella. | "knowledge-format" | mcp/src/agents_remember/cli/__main__.py:64-64 |
| The command's check, rewrite and skip behaviour is tested end to end. | `test_knowledge_format_command_checks_rewrites_and_skips_caches` | mcp/tests/test_knowledge_file_canonical.py:85-120 |

## Cross-Repo References

No meaningful cross-repo references found: the command rewrites only the files it is given.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
