# mcp/src/agents_remember/cli/knowledge_worklist.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**CLI adapter `agents-remember knowledge-worklist` (MIK-R08).** It computes the change-to-knowledge
worklist for a leaf (`--contract`), exactly as the curator's memory-quality run does and persisted beside
the contract, or for four explicitly named sides (evidence runs on scratch copies), and prints it as JSON.

## Code Commentary

### Logic

- `add_arguments`: `--contract`, or the explicit form `--code`, `--base`, one of `--candidate` or
  `--code-worktree`, `--memory`, `--memory-base`, one of `--memory-candidate` or `--memory-worktree`, plus
  `--maintenance-scope`, `--owner`, `--output`, `--cache-dir` and, since MIK-R14, `--coordination-root`: where
  requirement endpoints' owning tasks live, passed into `ExplicitSides.coordination_root` so the explicit form can
  resolve `reconsider_on` requirement endpoints; omitted, none resolves. `--contract` takes the contract's own
  coordination root (`leaf_worklist`).
- `_explicit` names the missing required flags, or the "exactly one of" pair that is wrong, and otherwise
  builds `ExplicitSides` (K_B taken as given, not searched by trailer).
- `run` calls `leaf_worklist(load_contract(...))` for `--contract` (which persists beside the contract) or
  `worklist_for_sides`; `--output` also writes the document there.
- **Exit status:** 0 for a complete worklist, 1 for an incomplete one, 2 when no worklist applies (both
  memory sides unconverted, or not a leaf's contract) or the explicit flags are invalid.

### Conventions

- Registered as a subcommand in `cli/__main__.py`, next to `knowledge-index`.

### Invariants And Boundaries

- The explicit form writes only `--output`; it never writes a memory tree or an enclosure.
- The converted-base cache is used only when `--cache-dir` is named, and it refuses a directory inside a
  Git working tree.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The two forms and the exit statuses. [1]
- The arguments. [2]
- Explicit sides, with named argument errors. [3]
- The optional coordination root for requirement endpoints (MIK-R14), in the usage line, the parser and the sides. [4]
- The run and its exit status. [5]
- The subcommand registration. [6]

### Cross-Repo References

No meaningful cross-repo references found: the command reads the repositories its flags or the contract
name.

No cross-repo boundary is crossed by this file.
