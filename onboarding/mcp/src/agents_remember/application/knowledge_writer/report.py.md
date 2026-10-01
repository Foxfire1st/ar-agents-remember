# mcp/src/agents_remember/application/knowledge_writer/report.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The report shapes.

- The outcome of one evidence-bearing entry. [1]
- The report and its refused flag. [2]
- The JSON form. [3]
- The text form. [4]
- The carried entries in the report, JSON and text. [5]
- One requirement endpoint and the owner's answer; unresolved is reported, never refused. [6]
- The report's requirement endpoints, and their JSON key. [7]
- The text line per endpoint comes from a helper, so `render` does not grow (review F3). [8]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
