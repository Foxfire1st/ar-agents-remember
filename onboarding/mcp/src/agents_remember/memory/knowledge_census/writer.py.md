# mcp/src/agents_remember/memory/knowledge_census/writer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_census/writer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The census section of the knowledge writer (MIK-R20 Scope): every census write, checked.**
`CensusWriter(memory_root)` writes one converted memory working tree. Each operation reads the tree, builds
the new file bytes in the canonical formatting, and runs `check_censuses` (the checks the validator
registers) over the result with the current tree as the base; any finding for that census refuses the
write with `CensusWriteError`, and nothing is written.

## Code Commentary

### Logic

- `create(baseline, inventory)` writes `inventory.json` first and `baseline.json` last, so the baseline
  is the commit point. A census directory holding only `inventory.json` is an interrupted creation and
  is written again against a base without it; any other existing census file refuses with "already
  exists" (review R1 finding 4).
- `add_claims(census_id, route, claims)` appends claims to the route's claims file.
- `append_assessment(census_id, claim_id, assessment)` appends one assessment; `set_disposition` sets the
  disposition and linked records. Both go through `_replace_claim`.
- `append_status(census_id, route, entry)` appends one status entry.
- `_refusing_invalid` turns a pydantic `ValidationError` during model construction into
  `CensusWriteError` (review R1 finding 5).
- `_commit` checks, then writes each file with `atomic_write_bytes`.

### Conventions

- The writer has no operation that edits or removes an assessment or a status; it can only append.
- Only findings under the written census's directory refuse its write.

### Invariants And Boundaries

- **The writer refuses an unconverted tree**, one without `knowledge/layout.json` (`_tree`). Before the cutover (MIK-R37) no production memory tree is converted, so the writer never touches production memory.
- A refused write leaves the tree byte-for-byte unchanged.

### Todos

- An agent-facing entry (an MCP tool or a `knowledge-ingest` section) for claims, assessments and statuses belongs to MIK-R12 and MIK-R19; today only the Python API and `knowledge-census inventory` reach the writer.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The refusal type, the checked commit and each operation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Model refusals are write refusals. | `_refusing_invalid` | mcp/src/agents_remember/memory/knowledge_census/writer.py:63-70 |
| An unconverted tree is refused. | `_tree` | mcp/src/agents_remember/memory/knowledge_census/writer.py:83-90 |
| Check against the current tree, then write atomically. | `_commit` | mcp/src/agents_remember/memory/knowledge_census/writer.py:92-121 |
| Create once; the baseline is the commit point. | `create` | mcp/src/agents_remember/memory/knowledge_census/writer.py:123-147 |
| Append claims, assessments and statuses; set a disposition. | `add_claims`; `append_status` | mcp/src/agents_remember/memory/knowledge_census/writer.py:149-160; mcp/src/agents_remember/memory/knowledge_census/writer.py:209-220 |
| The writer's tree passes the validator after appends. | `test_the_writer_appends_observations_and_its_tree_passes_the_validator` | mcp/tests/test_knowledge_census_files.py:237-269 |
| The writer refuses and writes nothing. | `test_the_writer_refuses_and_writes_nothing` | mcp/tests/test_knowledge_census_files.py:272-300 |
| An interrupted create can be repeated. | `test_an_interrupted_create_leaves_no_baseline_and_can_be_repeated` | mcp/tests/test_knowledge_census_files.py:535-562 |
| Model refusals in the writer are `CensusWriteError`. | `test_model_refusals_in_the_writer_are_census_write_errors` | mcp/tests/test_knowledge_census_files.py:565-582 |

## Cross-Repo References

No meaningful cross-repo references found: the writer writes one memory working tree named by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
