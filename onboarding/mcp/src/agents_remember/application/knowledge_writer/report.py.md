# mcp/src/agents_remember/application/knowledge_writer/report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:13:03+02:00 |
| lastVerifiedCommitHash | `3eb034a6ab0493a51da5dcd6d013aa6f27f39496`|
| lastVerifiedCommitDate | 2026-09-30T03:31:21+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**What one writer operation reports.** A written or planned operation lists every record, entry and
history row with its ID and action, every entry's evidence and where it is stored, and the validator's
report-only findings; a refused one lists every problem and refusing violation. Since MIK-R13 it also lists every requirement endpoint the run's records link, `resolved` or
`unresolved` with the owner's reason. `to_document` is the
`--json` form (`"operation": "knowledge-write"`), `render` the text form.

## Code Commentary

### Logic

- `Action` is `created`, `updated`, `unchanged` or `removed`; `WriteState` is `written`, `planned` or
  `refused`; `EvidenceState` is `proof_written`, `needs_facet` or `unresolvable`.
- `EvidenceOutcome.stored_in` names the records whose `origin.handoff` holds the evidence, or
  `knowledge/history/<owner>.json#<record ID>` for evidence stored in a history row. An empty `stored_in`
  renders "nothing: the entry authored no record".
- `authorization` is carried because the file format has no field for it.
- `carried` (MIK-R08) lists the entries the operation re-recorded at C because their anchored content is
  unchanged while their file's blob moved (`carry.carry_entries`). It is a JSON list and, in the text form,
  one line per entry: `carried <ID>: blob re-recorded at C (content unchanged)`.
- **Requirement endpoints (MIK-R13 rule 4).** `EndpointOutcome` is one requirement link target of a record this
  run touched: `record`, `field` (`links.<i>`), `relation`, `endpoint` (the key
  `<repository>/<task path>#<id>@<version>`), `state` (`resolved` or `unresolved`) and, when unresolved, the
  owner's `code` and `detail` verbatim. `WriteReport.requirements` holds them (filled by
  `requirement_links.requirement_endpoints`); the JSON key is `requirementEndpoints`, and the text form adds one
  line per endpoint (`requirement <key> from <record> <field> (<relation>): <state> [<code>] <detail>`). An
  unresolved endpoint is **reported, never refused**: it does not change `refused` or the state.
- The text lines come from the module helper `_endpoint_line`, applied with `map`, so `WriteReport.render`
  keeps its base complexity (radon C, 16; L13 review F3, ruling 02:05:07).

### Conventions

- JSON keys are camelCase (`memoryRoot`, `codeTree`, `historyRows`, `handoffEntry`, `storedIn`).

### Invariants And Boundaries

- The report is the product, as for the database `knowledge-ingest`; nothing else records the operation.

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

The report shapes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The outcome of one evidence-bearing entry. | `EvidenceOutcome` | mcp/src/agents_remember/application/knowledge_writer/report.py:59-66 |
| The report and its refused flag. | `WriteReport` | mcp/src/agents_remember/application/knowledge_writer/report.py:85-164 |
| The JSON form. | `to_document` | mcp/src/agents_remember/application/knowledge_writer/report.py:109-129 |
| The text form. | `render` | mcp/src/agents_remember/application/knowledge_writer/report.py:131-164 |
| The carried entries in the report, JSON and text. | `carried`; "blob re-recorded at C (content unchanged)" | mcp/src/agents_remember/application/knowledge_writer/report.py:102-102; mcp/src/agents_remember/application/knowledge_writer/report.py:147-147 |
| One requirement endpoint and the owner's answer; unresolved is reported, never refused. | `EndpointOutcome` | mcp/src/agents_remember/application/knowledge_writer/report.py:69-83 |
| The report's requirement endpoints, and their JSON key. | `requirements`; `requirementEndpoints` | mcp/src/agents_remember/application/knowledge_writer/report.py:103-103; mcp/src/agents_remember/application/knowledge_writer/report.py:128-128 |
| The text line per endpoint comes from a helper, so `render` does not grow (review F3). | `_endpoint_line` | mcp/src/agents_remember/application/knowledge_writer/report.py:162-162; mcp/src/agents_remember/application/knowledge_writer/report.py:221-226 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **body updated for MIK-R13.** Purpose and Logic record `EndpointOutcome`, `WriteReport.requirements` (JSON `requirementEndpoints`) and the text lines from `_endpoint_line` (review F3, ruling 02:05:07: `render` stays at its base complexity). Three rows were added. The `WriteReport`, `to_document`, `render` and `carried` rows were re-pointed by the exact base-to-staged line shift (the new dataclass moved them +16/+18); no claim was reworded. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **body updated for MIK-R08.** Logic gains the `carried` field (the IDs `carry.carry_entries` re-recorded at C), with its JSON and text forms, and a row cites it.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
