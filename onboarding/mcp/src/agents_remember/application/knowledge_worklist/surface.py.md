# mcp/src/agents_remember/application/knowledge_worklist/surface.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**What `knowledge_integrity_check` returns for a leaf: its latest worklist (MIK-R08 rule 7).** A caller
names the leaf by its series contract (`contractPath`); `leaf_worklist_fields` returns the latest persisted
`knowledge-worklist/v1` beside it as two response fields.

## Code Commentary

### Logic

- `leaf_worklist_fields(contract_path)` reads `<contract dir>/knowledge-worklist.json` through
  `read_leaf_worklist` and returns:
  - `worklistState: "present"` with `worklist` holding `worklist_summary` (state, path, digest, item count,
    counts by kind, the unreadable inputs), the `owner`, one compact `{id, kind, subject}` row per item
    (`_compact`; since MIK-R11 the row also carries `planning` when the item has a mark), and
    `plannedEffects` (MIK-R11: `{declared: false}` or the per-declaration match list);
  - `worklistState: "absent"` with only the expected path, when no file exists;
  - `worklistState: "unreadable"` with the path and the error, when the file cannot be read or parsed.
- The full facts of every item stay in the file, whose path is returned (the tool-report budget pattern).

### Conventions

- The tool computes nothing: each memory-quality run and each completed managed sync recomputes the
  worklist (rule 8), so the answer is exactly what the last run persisted, or `absent`.

### Invariants And Boundaries

- **Read-only.** The contract path is trusted as given (review R1 note 7): nothing is written, and a path
  that is not a series contract reads as `absent` or `unreadable`.
- MIK-R26 keeps the tool and points it at the validator and this worklist.
- **The planned marks are visible here** (MIK-R11 rule 7, with the curator checklist). The reviewer-UI half
  of rule 7 is carried to L31 (ruling Q1, 2026-09-29T21:56:18+02:00).

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

- The tool returns the last persisted worklist and computes nothing. [1]
- The compact item row, with its `planning` mark where present. [2]
- The three states, the compact item rows and `plannedEffects`. [3]
- The tool's consumer of these fields. [4]
- The tool returns the latest worklist and the checklist shows it. [5]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one file in the coordination task root.

No cross-repo boundary is crossed by this file.
