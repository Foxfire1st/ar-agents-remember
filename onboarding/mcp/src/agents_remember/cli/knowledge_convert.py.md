# mcp/src/agents_remember/cli/knowledge_convert.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**CLI adapter: `agents-remember knowledge-convert MEMORY_ROOT --code CODE_REPOSITORY [--code-commit REV]
[--version V] [--report FILE] [--check]` (MIK-R24).** It converts a memory working tree (its `onboarding/`
cards and its `knowledge.sqlite`) into the text knowledge format, in place. Every card's citations are
anchored in the tree of the card's `lastVerifiedCommitHash`, read from the object store of `--code`.
`--code-commit` (default `HEAD` of `--code`) is the paired code tree, used for fallback cards and for the
report's currentness counts.

## Code Commentary

### Logic

- `add_arguments` declares the memory root, `--code` (required), `--code-commit`, `--version` (default and
  only supported value `1`), `--report` (the JSON report) and `--check` (convert and report, write
  nothing).
- `run` reads the tree (`inputs.memory_from_directory`), builds `CodeObjects` and calls `convert_memory`.
  It writes the report if asked. An already converted tree prints a no-op message. Unless `--check`, it
  then writes the changed files (`inputs.write_changed`) and prints the counts: files, references,
  unresolved targets, invariants, families, realizations.
- Exit status: 0 converted (or already converted); 1 refused (an unsupported version, validation, the
  export, or an unreadable code object); 2 an invocation or read error.

### Conventions

- Registered by `cli/__main__.py` as the `knowledge-convert` subcommand.

### Invariants And Boundaries

- **The command commits nothing.** Committing a conversion to a real memory line is the cutover's
  (MIK-R37), or a crossing sync's (rule 8).
- It writes only after the whole converted tree validated.
- No installed route calls it before MIK-R37. Later leaves use it to make the converted scratch copies
  their evidence runs on.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The arguments, the run and its registration.

- The arguments. [1]
- The run: convert, report, write unless checking, exit status. [2]
- The umbrella registration. [3]
- The conversion it drives. [4]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
