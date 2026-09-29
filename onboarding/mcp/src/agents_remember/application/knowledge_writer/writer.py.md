# mcp/src/agents_remember/application/knowledge_writer/writer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/writer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**`write_knowledge(WriteRequest) -> WriteReport`: the curator writer's one operation (MIK-R12 rules 2, 4
and 7).** It reads the hand-off document (`handoff.read_handoff`), loads the memory tree
(`MemoryState.load`), captures the code candidate tree C (`CodeSnapshot.capture`), applies the document
(`Authoring.run`), carries every `carried` entry forward at C (`carry_entries`, MIK-R08), checks every row of the owner's history file (`owner_history_problems`), renders each
touched document canonically after model validation (`_render`), then runs the MIK-R22 validator
(`validate_tree`) over the **whole resulting tree**, with the memory worktree's `HEAD` as base when that
base is converted. Only then does it write, and only in a committing run.

## Code Commentary

### Logic

- `WriteRequest` carries the two roots, the `Owner`, the hand-off path as `origin.handoff.path` records it,
  the parsed document, the commit word and the `authorization` reference. The file format has no field for
  the authorization, so the report records it. Since MIK-R11 it also carries `decisions`, the task
  owner's `DecisionResolver` for a planned `dropped` row's cited decision, which `write_knowledge` hands to
  `Authoring`; a write without a task owner (a wave, `decisions=None`) refuses such a row. The leaf route
  binds it (`cli/knowledge_write_route.leaf_decisions`).
- An unconverted memory tree is refused by name (`UNCONVERTED`, placed at `LAYOUT_MARKER_PATH`) before C is
  captured.
- Problems from reading, authoring, the history check and rendering are all collected; any of them refuses
  the operation before validation runs.
- **Carry-forward (MIK-R08 definition 4).** After authoring and before the history check, every operation
  calls `carry.carry_entries(state, snapshot, owner)`: each `realizes` or `proves` entry whose file's blob
  moved at C while its anchored content is identical is re-recorded at C (`blob`, and a line range's lines),
  and this owner's own open history row that still names the old anchor as `after` follows it. The IDs go
  into `WriteReport.carried`. This is the mechanical update the worklist's `carried` class promises, so such
  an entry needs no disposition. The carry runs over the whole tree, not only the leaf's changed paths.
- `_writer_split` turns refusals of the rules the registry marks `writer_reports`
  (`writer_reported_rule_ids()`: today `R04.1-route-directory`, `R04.2-coverage`, `R04.2-non-empty`) into
  report-only violations **inside the writer**, so a leaf may place family routes over several runs
  (MIK-R04 rule 6). Every other refusal still refuses. `require_valid_commit` is not touched, so every
  commit route still refuses those rules (the L04 carry-over obligation, met at the L12 sync).
- `_finish`: without `commit` the state is `planned` and `written`/`removed` list what *would* change; with
  it, `MemoryState.write` writes and the state is `written`.
- `_render` validates a history document with `parse_history_document` and every other document with
  `parse_document`, then renders `canonical_text`; a model refusal is a `Problem` per pydantic error.

### Conventions

- Report assembly uses `dataclasses.replace` on the frozen `WriteReport` at each stage.

### Invariants And Boundaries

- **All or nothing (rule 4):** a refused operation writes nothing and names every problem and every
  refusing violation. Report-only findings (family coverage among them) are carried and never refuse.
- A violation already present in the base still refuses a write unless the validator classes it as carried
  and report-only (architect ruling 6); the curator repairs such damage by direct edit first.
- Nothing is written before validation: `MemoryState.write` is reached only from `_finish` with
  `commit=True`.
- **The carry never edits authored fields or another owner's row (architect ruling 5, MIK-R08).** It never
  changes a locator kind, a name or `content`, and it leaves closed history files and other owners' rows
  alone; with this owner's own file closed, the history check then refuses the write ("closed and frozen").

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The operation and its stages.

| Finding | Anchor | Source |
| --- | --- | --- |
| The refusal text for an unconverted memory tree. | `UNCONVERTED` | mcp/src/agents_remember/application/knowledge_writer/writer.py:55-59 |
| One operation's inputs, including the authorization reference the report records and the task owner's decision resolver. | `WriteRequest`; `decisions` | mcp/src/agents_remember/application/knowledge_writer/writer.py:62-81 |
| Read, author, check history, render, validate, then finish or refuse. | `write_knowledge` | mcp/src/agents_remember/application/knowledge_writer/writer.py:84-130 |
| The carry-forward call and its report field. | `carry_entries`; `carried=carried` | mcp/src/agents_remember/application/knowledge_writer/writer.py:81-125 |
| The carry itself. | `carry_entries` | mcp/src/agents_remember/application/knowledge_writer/carry.py:47-72 |
| The `writer_reports` rules become reports inside the writer; commit routes still refuse them. | `_writer_split` | mcp/src/agents_remember/application/knowledge_writer/writer.py:133-148 |
| Planned or written. | `_finish` | mcp/src/agents_remember/application/knowledge_writer/writer.py:151-164 |
| Model validation then canonical rendering of every touched document. | `_render` | mcp/src/agents_remember/application/knowledge_writer/writer.py:167-189 |
| The registry side of the writer-reported rules. | `writer_reported_rule_ids` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:83-88 |
| A validator refusal writes nothing and names every violation. | `test_a_validator_refusal_writes_nothing_and_names_every_violation` | mcp/tests/test_knowledge_writer.py:326-338 |
| Route rules are reports in the writer and refusals at a commit route. | `test_family_route_rules_are_reports_in_the_writer_and_refusals_at_a_commit_route` | mcp/tests/test_knowledge_writer.py:614-652 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** The `WriteRequest` Logic bullet and row now name `decisions`, the task owner's resolver passed to `Authoring` for a planned `dropped` row (a wave refuses such a row). The reworded `WriteRequest` row reopened on the new `decisions` anchor; only the generated-repair bullet this pass's fixer wrote for it was removed. Ranges below the new field were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T15:42:32+00:00: Generated citation repair: `UNCONVERTED` repointed to mcp/src/agents_remember/application/knowledge_writer/writer.py:55-59. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **body updated for MIK-R08.** Purpose and Logic now name the carry-forward step (`carry.carry_entries`, called in every operation between authoring and the history check, its IDs in `WriteReport.carried`), and Invariants records architect ruling 5 (the carry updates only this leaf's own open row, never closed files or other owners' rows). Two rows cite the call and the new `carry.py`. The module docstring's new "Carried entries" paragraph is the source.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
