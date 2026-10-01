# mcp/src/agents_remember/cli/knowledge_format.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-format [--check] PATH...`: the command that applies the canonical
knowledge formatting (MIK-R21 rule 8).** Each PATH is a file or a directory; a directory contributes
every `*.json` below it except the generated route-index cache (`*.index.json`) and anything under a
hidden directory (such as `.ar-index`). A dot-named *file* is still formatted. It is the command the
validator (MIK-R22) names, as `agents-remember knowledge-format <path>`, when it refuses a
non-canonical file.

## Code Commentary

### Logic

- `add_arguments` declares `paths` (one or more) and `--check`.
- `iter_json_files` yields a named file as-is, and for a directory the sorted `rglob("*.json")`
  minus every path that `memory_quality.knowledge_validator.trees.is_excluded_from_knowledge` excludes:
  a `*.index.json` cache, or a path with a dot-named *directory* component. Since MIK-R22 this is the
  validator's own predicate, so the formatter and the validator cannot disagree about which files are
  knowledge. The module's former `CACHE_SUFFIX` constant and its own copy of the rule are gone.
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
- **The formatter and the validator share one "is this a knowledge file" predicate.** The import runs
  from the CLI layer down to `memory_quality`, which is the permitted direction.
- **Nothing in the installed runtime reads or writes these files before MIK-R37.** The package is
  reached only from `agents-remember knowledge-format` and the tests; the live memory repository
  is still read and written through the SQLite knowledge store until the layout switch.

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
- Cache files and hidden directories are skipped through the validator's shared predicate. [2]
- Exit statuses and the atomic rewrite. [3]
- Registration in the umbrella. [4]
- The command's check, rewrite and skip behaviour is tested end to end. [5]

### Cross-Repo References

No meaningful cross-repo references found: the command rewrites only the files it is given.

No cross-repo boundary is crossed by this file.
