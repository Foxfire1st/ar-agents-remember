# mcp/src/agents_remember/models/knowledge_files/records.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The twelve global record kinds, one JSON file per truth under `knowledge/<kind-dir>/` (MIK-R21 rule
4).** Each record declares `schema: ar-<kind>/v1`, its stable `id`, its `origin` and a `revision` (≥1,
increments only when meaning changes). The current revision can carry a product-owned `writer` stamp. Invariants, families and facets use `status: retired` when retired. Decisions carry their own status and weaknesses carry `state` (`open` or `closed`). The module also fixes
**relationship ownership** (Doc14 §2): a relationship is written once, on its owner's side, and the
models refuse the fields that would give it a second owner.

## Code Commentary

### Logic

- `_Record` holds `id` and `origin` and checks that the ID carries the kind's own prefix and that
  every `links` relation is in `RELATIONS_BY_KIND[kind]`.
- `InvariantRecord` carries an optional `title` of type `InvariantTitle`. An older record may still omit this display name. Its rule fields (`statement`, `applicability`, `conditions`, `exclusions`, `supersedes[]`,
  `admission`) own the rule's meaning and preserve single ownership of realizations, tests, families and decisions; `extra="forbid"` refuses them.
- `FamilyRecord` owns `members` (invariant IDs) and `routes`, both unique. Since MIK-R04 (leaf 260928-MIK-L04, ruling Q3) `routes` is `tuple[RoutePath, ...]`: a repository directory, or `.` for the repository root route, which a family uses only when it genuinely has no narrower home. `RoutePath` comes from `sidecars.py` and reuses the route sidecar's root handling; every other spelling of the root (`""`, `"./"`, `"./mcp"`, `".."`, `"/"`, `"mcp/"`) is still refused, and every other path field stays `RepositoryPath`.
- `DecisionRecord` owns `alternatives` (`option`, `status` chosen/rejected/deferred, `reason`,
  `reconsider_when?`), `consequences`, `decider`, `supersedes[]` and its `links`; its status is
  `active` | `under_reconsideration` — `superseded` is derived from a later record's `supersedes`,
  never stored.
- `_FacetRecord` carries a revision and an optional stored lifecycle word. The parser also accepts old `proposed` and `accepted` words so older trees can be read. The lifecycle helper treats those old words as empty, and standing is derived from the selected tree. Facets carry no `admission`.
- IncidentRecord requires recovery and corrective_actions unless applicability is unresolved. The other six facet record classes declare their text-file meanings directly. The canonical-database facet payload models and the old cross-model field-set comparison were retired by MIK-R26; these records remain the text format's own declarations.
- `WeaknessRecord` (`ar-weakness/v1`, MIK-R118) records a weakness of the code where it occurs:
  `kind` (one of `context`, `compute`, `storage`, `time`, `fault`, `debt`), a one-sentence
  `statement`, an `anchor` that must name its file, `seen` (`{task, role}`), `state` (`open` |
  `closed`), an optional `measurement` (`{number, unit, how, commit, date}`), an optional `closed`
  (`{task, commit?, reason?}`) and `links`, whose only permitted relation is `burdens`.
  `Closure` permits an absent commit only when a reason is supplied; the task remains required. `WeaknessRecord` refuses
  an anchor with no path, a `closed` block that disagrees with `state` (in either direction), a
  statement longer than 400 characters, an unknown kind and any extra field.
  It has no priority or proposal field: a weakness that belongs to no file is not recorded here.
- `DependentRecord` (`ar-dependent/v1`, MIK-R124) records one document of the code repository and
  every place it stands on: `document`, at least one `stands_on` link — an anchor naming its file, a
  file with its `blob`, or a record ID with its `revision`, each with an optional `heading` — and
  `confirmed` (`{task, role, commit, codeTree?, uncommitted?, statement?}`). It refuses two links
  that repeat the same kind and value — a `heading` does not tell them apart — an empty
  `stands_on`, an anchor link with no path, and extra fields. It stores neither the document's text
  nor whether the document is stale; that is derived.
- `RECORD_MODELS` maps kind → model; `schema_name(kind)` spells `ar-<kind>/v1` with `-` for `_`;
  `record_status(record)` returns a weakness's own state or a kind's stored lifecycle word. It returns empty for legacy standing words and for a dependent, whose currency is computed when read.

### Conventions

- The relation vocabulary is closed per kind: decision {explains, constrains, motivated_change_to,
  reconsider_on}; incident {violated, exposed_gap_in, occurred_at, led_to}; failure_mode {threatens,
  occurs_at}; assumption {conditions, underlies}; limitation {bounds}; scenario {exercises};
  diagnostic {diagnoses}; term {defines_term_in}; weakness {burdens}; dependent none; invariant and
  family have none.

### Invariants And Boundaries

- **One owner per relationship.** An invariant never lists where it is realized or proved, nor its
  family or decisions; those live in sidecars, family `members` and decision `links`. A dependent
  record owns its `stands_on` links.
- Only invariant, family and decision records carry `admission` (a criterion set or
  `legacy-unassessed`). What a criterion means, and decision content rules (alternatives, when
  `reconsider_when` is required), belong to MIK-R27 and MIK-R13: MIK-R13's content rules are the pure functions
  of `models/knowledge_files/decisions.py` (at least two alternatives and exactly one chosen, `reconsider_when` on
  every rejected or deferred alternative, `reconsider_on` indexes, the derived `superseded`), which the validator
  refuses on through `rules_decisions.py` (leaf 260928-MIK-L13).
- A record is never deleted; it leaves use through `status: retired` (or supersession for decisions),
  and a weakness through `state: closed` with the closing task and either its known commit or a
  reason when no commit is supplied. A dependent
  has no lifecycle word of its own: whether its document is stale is derived, never stored. The one
  record a tree may be rid of is a dependent whose document the task deleted: the writer's
  `_remove_record` takes it out of the tree, `check_record_kept` exempts exactly that missing dependent
  ID when the leaf's retired `record` row answers it, and every other kind keeps the retention rule
  whole — a weakness is closed, never deleted.

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



- A family route is a repository path or the root route. [5]
- Incident recovery is required once not unresolved. [7]



- Text facet records declare their own fields, with current kind parsing and malformed-field checks. [9]


### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.

- Prefix and relation checks shared by every record. [2]
- Revision and status on incident and facet records. [3]
- The family record: members and routes, a route being a repository directory or `.`. [4]
- The invariant model permits an optional display title and refuses relationship fields owned elsewhere. [6]

- The per-kind relation vocabulary. [1]
- The kind → model table. [8]
