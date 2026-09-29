# mcp/src/agents_remember/application/knowledge_worklist/surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
| governingOverview | `../overview.md` |

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
| The tool returns the last persisted worklist and computes nothing. | "The tool computes nothing here" | mcp/src/agents_remember/application/knowledge_worklist/surface.py:1-9 |
| The compact item row, with its `planning` mark where present. | `_compact`; `planning` | mcp/src/agents_remember/application/knowledge_worklist/surface.py:26-32 |
| The three states, the compact item rows and `plannedEffects`. | `leaf_worklist_fields`; `worklist_summary` | mcp/src/agents_remember/application/knowledge_worklist/surface.py:35-56 |
| The tool's consumer of these fields. | `knowledge_integrity_check_payload`; `leaf_worklist_fields` | mcp/src/agents_remember/mcp/tools/knowledge.py:684-721 |
| The tool returns the latest worklist and the checklist shows it. | `test_the_tool_returns_the_latest_worklist_and_the_checklist_shows_it` | mcp/tests/test_knowledge_worklist_leaf.py:389-420 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one file in the coordination task root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** The compact item row (`_compact`) now carries `planning` where present and the response carries `plannedEffects`; recorded rule 7's visibility and ruling 21:56:18 Q1 (the reviewer UI carried to L31). One row added and the states row reworded; ranges re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/src/agents_remember/mcp/tools/knowledge.py`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
