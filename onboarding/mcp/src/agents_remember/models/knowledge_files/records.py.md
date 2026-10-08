# mcp/src/agents_remember/models/knowledge_files/records.py

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
- `FamilyRecord` owns `members` (invariant IDs) and `routes`, both unique. Since MIK-R04 (leaf 260928-MIK-L04, ruling Q3) `routes` is `tuple[RoutePath, ...]`: a repository directory, or `.` for the repository root route, which a family uses only when it genuinely has no narrower home. `RoutePath` comes from `sidecars.py` and reuses the route sidecar's root handling; every other spelling of the root (`""`, `"./"`, `"./mcp"`, `".."`, `"/"`, `"mcp/"`) is still refused, and every other path field stays `RepositoryPath`.
- `DecisionRecord` owns `alternatives` (`option`, `status` chosen/rejected/deferred, `reason`,
  `reconsider_when?`), `consequences`, `decider`, `supersedes[]` and its `links`; its status is
  `active` | `under_reconsideration` — `superseded` is derived from a later record's `supersedes`,
  never stored.
- `_FacetRecord` (incident and the six other facets) adds `revision` and `status`
  (`proposed`|`accepted`|`retired`) — added in repair round 1 so MIK-R24 rule 8 (conflict revision)
  and MIK-R22 rule 3 (retire, never delete) apply to every kind. Facets carry no `admission`.
- IncidentRecord requires recovery and corrective_actions unless applicability is unresolved. The other six facet record classes declare their text-file meanings directly. The canonical-database facet payload models and the old cross-model field-set comparison were retired by MIK-R26; these records remain the text format's own declarations.
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
  `reconsider_when` is required), belong to MIK-R27 and MIK-R13: MIK-R13's content rules are the pure functions
  of `models/knowledge_files/decisions.py` (at least two alternatives and exactly one chosen, `reconsider_when` on
  every rejected or deferred alternative, `reconsider_on` indexes, the derived `superseded`), which the validator
  refuses on through `rules_decisions.py` (leaf 260928-MIK-L13).
- A record is never deleted; it leaves use through `status: retired` (or supersession for decisions).

### Todos

`ar-failure-mode/v1`, `ar-diagnostic/v1` and `ar-term/v1` are spellings chosen by this leaf; the packet did not fix them.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The facet payload models this mirrors live in the shipped knowledge vocabulary.

- The per-kind relation vocabulary. [1]
- Prefix and relation checks shared by every record. [2]
- Revision and status on incident and facet records. [3]
- The family record: members and routes, a route being a repository directory or `.`. [4]
- A family route is a repository path or the root route. [5]
- The invariant record: no second-owner fields. [6]
- Incident recovery is required once not unresolved. [7]
- The kind → model table. [8]

- Text facet records declare their own fields, with current kind parsing and malformed-field checks. [9]


### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
