# mcp/src/agents_remember/cli/knowledge_worklist.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_worklist.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two forms and the exit statuses. | "Exit status: 0 for a complete worklist" | mcp/src/agents_remember/cli/knowledge_worklist.py:1-17 |
| The arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_worklist.py:34-60 |
| Explicit sides, with named argument errors. | `_explicit`; `ExplicitSides` | mcp/src/agents_remember/cli/knowledge_worklist.py:63-96 |
| The optional coordination root for requirement endpoints (MIK-R14), in the usage line, the parser and the sides. | "[--coordination-root DIR]"; "\"--coordination-root\","; "coordination_root=args.coordination_root" | mcp/src/agents_remember/cli/knowledge_worklist.py:8-8; mcp/src/agents_remember/cli/knowledge_worklist.py:56-60; mcp/src/agents_remember/cli/knowledge_worklist.py:95-95 |
| The run and its exit status. | `run`; `leaf_worklist` | mcp/src/agents_remember/cli/knowledge_worklist.py:99-114 |
| The subcommand registration. | "knowledge-worklist" | mcp/src/agents_remember/cli/__main__.py:96-101 |

## Cross-Repo References

No meaningful cross-repo references found: the command reads the repositories its flags or the contract
name.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** The `add_arguments` bullet records the optional `--coordination-root` of the explicit form (into `ExplicitSides.coordination_root`, so requirement endpoints can resolve; the `--contract` form uses the contract's root). One row added. The `_explicit` row, which still held its anchors but no longer its extent, was re-pointed by the exact line shift (`58-90` → `63-96`); the other two rows were normalised by the installed fixer. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
