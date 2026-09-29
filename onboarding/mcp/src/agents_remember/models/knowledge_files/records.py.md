# mcp/src/agents_remember/models/knowledge_files/records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The ten global record kinds, one JSON file per truth under `knowledge/<kind-dir>/` (MIK-R21 rule
4).** Each record declares `schema: ar-<kind>/v1`, its stable `id`, its `origin`, and — for every kind
— a `revision` (≥1, increments only when meaning changes) and a `status`. The module also fixes
**relationship ownership** (Doc14 §2): a relationship is written once, on its owner's side, and the
models refuse the fields that would give it a second owner.

## Code Commentary

### Logic

- `_Record` holds `id` and `origin` and checks that the ID carries the kind's own prefix and that
  every `links` relation is in `RELATIONS_BY_KIND[kind]`.
- `InvariantRecord` (`statement`, `applicability`, `conditions`, `exclusions`, `supersedes[]`,
  `admission`) lists **no** realizations, tests, families or decisions; `extra="forbid"` refuses them.
- `FamilyRecord` owns `members` (invariant IDs) and `routes` (repository directories), both unique.
- `DecisionRecord` owns `alternatives` (`option`, `status` chosen/rejected/deferred, `reason`,
  `reconsider_when?`), `consequences`, `decider`, `supersedes[]` and its `links`; its status is
  `active` | `under_reconsideration` — `superseded` is derived from a later record's `supersedes`,
  never stored.
- `_FacetRecord` (incident and the six other facets) adds `revision` and `status`
  (`proposed`|`accepted`|`retired`) — added in repair round 1 so MIK-R24 rule 8 (conflict revision)
  and MIK-R22 rule 3 (retire, never delete) apply to every kind. Facets carry no `admission`.
- `IncidentRecord` requires `recovery` and `corrective_actions` unless `applicability` is
  `unresolved`. The six facet records carry exactly the fields of today's payload models in
  `models/knowledge/facet.py`, which a test compares field set by field set.
- `RECORD_MODELS` maps kind → model; `schema_name(kind)` spells `ar-<kind>/v1` with `-` for `_`.

### Conventions

- The relation vocabulary is closed per kind: decision {explains, constrains, motivated_change_to,
  reconsider_on}; incident {violated, exposed_gap_in, occurred_at, led_to}; failure_mode {threatens,
  occurs_at}; assumption {conditions, underlies}; limitation {bounds}; scenario {exercises};
  diagnostic {diagnoses}; term {defines_term_in}; invariant and family have none.

### Invariants And Boundaries

- **One owner per relationship.** An invariant never lists where it is realized or proved, nor its
  family or decisions; those live in sidecars, family `members` and decision `links`.
- Only invariant, family and decision records carry `admission` (a criterion set or
  `legacy-unassessed`). What a criterion means, and decision content rules (alternatives, when
  `reconsider_when` is required), belong to MIK-R27 and MIK-R13.
- A record is never deleted; it leaves use through `status: retired` (or supersession for decisions).

### Todos

`ar-failure-mode/v1`, `ar-diagnostic/v1` and `ar-term/v1` are spellings chosen by this leaf; the packet did not fix them.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The facet payload models this mirrors live in the shipped knowledge vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-kind relation vocabulary. | `RELATIONS_BY_KIND` | mcp/src/agents_remember/models/knowledge_files/records.py:56-66 |
| Prefix and relation checks shared by every record. | `_Record` | mcp/src/agents_remember/models/knowledge_files/records.py:76-96 |
| Revision and status on incident and facet records. | `_FacetRecord` | mcp/src/agents_remember/models/knowledge_files/records.py:103-113 |
| The invariant record: no second-owner fields. | `InvariantRecord` | mcp/src/agents_remember/models/knowledge_files/records.py:116-137 |
| Incident recovery is required once not unresolved. | `IncidentRecord` | mcp/src/agents_remember/models/knowledge_files/records.py:195-220 |
| The kind → model table. | `RECORD_MODELS` | mcp/src/agents_remember/models/knowledge_files/records.py:302-312 |
| Facet fields equal today's payload fields. | `test_facet_records_carry_todays_payload_fields_plus_links` | mcp/tests/test_knowledge_file_formats.py:298-310 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
