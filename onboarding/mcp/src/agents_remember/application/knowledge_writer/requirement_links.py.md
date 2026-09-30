# mcp/src/agents_remember/application/knowledge_writer/requirement_links.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/requirement_links.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The requirement endpoints of the records one writer run authored, resolved by their owner (MIK-R13 rule 4).**
`requirement_endpoints(state, records, coordination_root)` is called by `writer.write_knowledge` and fills
`WriteReport.requirements` (JSON `requirementEndpoints`).

## Code Commentary

### Logic

- For each distinct record ID the run created, updated or left unchanged (`dict.fromkeys` keeps order and drops
  repeats), it reads the record from the memory state and walks its `links`. A link whose `target` is an object with
  a `task` key is a requirement endpoint: it is parsed as `RequirementReference` and resolved through
  `requirement_endpoint.resolve_requirement_endpoint`.
- Each endpoint becomes an `EndpointOutcome` with the record ID, `links.<i>`, the relation, the key, the state and
  the owner's code and detail.
- A target that does not parse as a requirement reference is skipped: the model check of the rendered record
  names it.
- Only `links[]` is scanned. Requirement targets in sidecar `references{}` (MIK-R21 rule 6) are not resolved here,
  which is enough for MIK-R13, whose scope is decision links (review F2).

### Conventions

- It never refuses and never edits: the link is written exactly as the curator authored it.

### Invariants And Boundaries

- **An unresolved requirement endpoint is reported, never refused.** Proved by
  `test_a_lifted_decision_round_trips_and_its_requirement_endpoints_are_reported` (`links.2` resolved, `links.3`
  `unresolved` with `task-intent-requirement-packet-version-mismatch`, the run written, an idempotent rerun), by
  the bootstrap dispatch test (`[("links.2", "resolved"), ("links.3", "unresolved")]`, review F4) and by the refused
  write that still reports its endpoint unresolved with no root.

### Todos

- **L14 (review F2), partly resolved by L14:** the endpoints of `reconsider_on` links are now reported in every
  worklist run's `reconsideration.links` summary (resolution and approval state, from the leaf's coordination root,
  MIK-R14). A standalone `knowledge-validate` or a commit route still reports no requirement endpoints; only a
  writer run does, for the records it touched. The reads that show endpoints stay with L29.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The one function.

| Finding | Anchor | Source |
| --- | --- | --- |
| Each requirement link target of the run's records, with the owner's resolution. | `requirement_endpoints` | mcp/src/agents_remember/application/knowledge_writer/requirement_links.py:24-53 |
| A lifted decision round-trips; one endpoint resolved, one reported unresolved; the rerun is unchanged. | `test_a_lifted_decision_round_trips_and_its_requirement_endpoints_are_reported` | mcp/tests/test_knowledge_writer.py:787-813 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree, writes the paired memory worktree, and only reads task packets under the coordination root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): this card's source is unchanged. **A forward reference to L14 is resolved in the Todos:** MIK-R14 adds the validator rule `R14.1-linked-alternative-order` (index stability, L13's carried Q6/F1) and reports `reconsider_on` requirement endpoints in the worklist's `reconsideration.links` summary (Q5/F2, partly: commit routes still resolve none, and the reads stay with L29). The installed fixer found nothing to change here. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): created this card for the new file MIK-R13 adds, recording ruling 01:45:56 Q5 and review F2 and F4. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
