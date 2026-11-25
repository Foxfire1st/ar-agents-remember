# mcp/src/agents_remember/cli/knowledge_format.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-format [--check] PATH...` applies canonical knowledge formatting**
(MIK-R21 rule 8). Each operand can name a file or directory. Directory walks format JSON and
skip generated route-index caches. Within a converted memory root’s `knowledge/` and
`onboarding/` subtrees, those walks include dot directories. Elsewhere the walk prunes dot
directories. The converted validator names `agents-remember knowledge-format <path>` when
it refuses a noncanonical file.

## Code Commentary

### Logic

- `add_arguments` declares `paths` (one or more) and `--check`.
- `iter_json_files` yields a named file as supplied. For a directory it sorts the JSON paths from
  `_directory_json_files`. That walker resolves the operand and recognizes converted memory
  ancestors or roots it reaches. It enables dot-directory descent inside their actual
  `knowledge/` and `onboarding/` subtrees. Same-named directories outside those subtrees
  retain ordinary pruning. Every walked JSON path uses the validator’s generated-cache filter.
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
- **Directory operands share the validator’s generated-cache predicate.** Converted-root detection
  and traversal belong to the CLI walker. An explicit file operand retains its separate path.
- The pre-layout runtime used the SQLite knowledge store. The converted validator consumes
  the canonical knowledge files.

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

The formatting rules live in the model package; this adapter only walks paths and writes.

- Arguments. [1]
- Directory operands include dot paths within the knowledge or onboarding subtrees of a converted memory root. The directory walk shares the validator’s generated-cache exclusion. [2]
- Exit statuses and the atomic rewrite. [3]
- Registration in the umbrella.
- The formatter test checks rewrites across equivalent and containing operands, including hidden memory files, and preserves generated caches and Git metadata. [5]

### Cross-Repo References

No meaningful cross-repo references found: the command rewrites only the files it is given.

No cross-repo boundary is crossed by this file.

- Registration in the umbrella. Anchor: "knowledge-format" [4]
