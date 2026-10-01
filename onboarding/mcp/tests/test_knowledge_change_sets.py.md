# mcp/tests/test_knowledge_change_sets.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

`SemanticChangeSet` and the preservation claim: the composed record and its separate sibling. **29 cases**,
in the order the requirement states its clauses, all in the `unit-regression` lane.

## Code Commentary

### Logic

Every case protects one clause group: the six declared parts, the two exact snapshot identities, the
membership computed from the members' own declarations, the succession edge, preservation as a record that
is *not* an effect, the generation the record group joins, the requirement-revision reference under the
opaque-reference clause, and the derived read that reports facts and no verdict.

**The succession edge is a new record with a predecessor, never an edited row.** A successor has its own
identity and its own edge row, and the superseded change set is still readable with its own payload
afterwards. The edge is written inside the successor's own creation batch — the command union carries no
member that appends an edge to a stored change set — a self-named predecessor is refused as the shipped
`lineage_cycle` with nothing written, the appended generation's triggers refuse an update and a delete of
the edge row, and a fork is two records both naming one predecessor rather than one winner. A rewritten
lineage, an in-place revision and a mutable "current version" pointer all fail here.

**Nothing may conclude a verdict or a summary.** Two probe tuples name what would make a change set a task
authority or a decision rather than a record of authored work, and each probe is asserted refused by the
frozen payload's ordinary `extra="forbid"` rule **and** absent from the columns of every registered
generation over `knowledge_record` and `change_set_predecessor`. The payload's own field set is asserted
exactly, an open question declares exactly its three fields and is served as open with no answered field on
either the payload or the served type, and no `preserve` spelling and no preservation flag is representable
in the effect vocabulary.

Three further properties are load-bearing:

- **Both snapshot identities are stored verbatim.** The baseline *and* the candidate are read back exactly
  as the author declared them, including the schema version, and neither is re-derived from what is current
  at read time; a change set assembled from two namespaces is refused at construction, because it is not a
  comparison any reader could interpret.
- **Membership is a computed fact, and a member belongs to one change set.** A claim is listed only under
  the change set it declares and the other change set lists nothing; a change set holding preservation
  claims and no effect claims is complete and valid, and one holding no member at all is equally complete
  rather than refused or filled in.
- **An unresolved reference is a state, never a refusal and never a repair.** Requirement-revision
  references and realization-claim identities are stored verbatim and reported as unresolved references
  with the field, the holder record and the holder revision; the same references are reported from both the
  per-record plane and the scope plane, and the scope-level list is exactly the union of the per-record
  lists. A realization claim deleted after the change set was written is reported unresolved rather than
  re-pointed at a neighbouring claim, and no `requirement_revision` record is fabricated to satisfy a
  reference.

**The generation's append is asserted by name and by comparison, not against a hard-coded list.**
Generation 8's tables are generation 7's tables with exactly one table appended — `change_set_predecessor`,
whose primary key is the ordered triple `repository_id`, `successor_change_set_id`,
`predecessor_change_set_id` — and every one of generation 7's **thirty-three** names keeps its columns and
its primary key. So generation 8's **thirty-four** tables are thirty-three inherited plus one appended.
The case also asserts the suffix is that one table, that generation 8's trigger set and index set are
strict supersets of generation 7's, that the appended table carries no `content_digest` column, and that
no registered generation's DDL contains `ALTER TABLE` — so a later renumber changes two operand names and
nothing else. A fresh store declares the current generation and is served by the record group's own read.

**One assertion in that case was re-scoped by `260915-KS-L21`, which appends generation 9.** The line read
`assert CURRENT_GENERATION is GENERATION_8`; the registry's tip is now generation 9, so that was a false
statement about the tree and it became `assert CURRENT_GENERATION.user_version > GENERATION_8.user_version`
(`mcp/tests/test_knowledge_change_sets.py:683`), with the source comment above it recording why
(`:678-682`). The case's property is unchanged and is now stated against the generation that actually
carries the authored-effect group's table: the generation-8 prefix, columns, primary keys, trigger and
index sets and the `ALTER TABLE` sweep are all asserted exactly as before, and the new form says the
registry's tip lies **beyond** generation 8 rather than **at** it — which is the stronger reading, because
it stays true for every later generation while the identity form had to be edited by each one. The
`CURRENT_GENERATION is GENERATIONS[-1]`-style "newest registered" naming this card already records
elsewhere in the suite is the same move the facet module made for its own generation case. Nothing was
deleted, skipped, deselected or weakened, and no case was added here: the full generation-9 descent — that
generation 9 appends to generation 8 with only its own census tables and that every generation-8 table keeps
its columns and primary keys — is asserted in the census module's own
`test_the_census_record_kinds_join_a_registered_generation_that_appends_to_its_predecessor`
(`mcp/tests/test_migration_census.py:360-369`), which is the generation this module's record group descends
through.

**The closed vocabularies are asserted as exact sets, and they pin rather than union.** The three member
kinds map to exactly three frozen models of three different types, with neither payload type a subclass of
the other; the preservation subject kinds are exactly the four declared ones with an effect label refused
as a subject; the change-set payload registers under exactly one kind and one schema; requirement-revision
references stay inside the shipped `REFERENCE_MAX_LENGTH` bound and round-trip byte-identically, so
spellings a parser would fold together stay distinct stored values. A reference declared twice is refused,
because two identical references would look like two authored members.

**What the cases deliberately do NOT assert.** No case asserts that a change set is complete, endorsed,
reviewed or gated — the requirement's own position is that an authored record concludes nothing — and none
asserts a canonical spelling, a requirement identity parsed out of a reference, or a stored read.

### Conventions

Hermetic like its sibling: temporary directories, in-process APSW databases built through the candidate
namespace seam of `mcp/tests/candidate_batch_test_support.py`, and the shared knowledge fixture. The lane
row is `mcp/tests/test-evidence-lanes.toml:163`, and the module is inside the unit population registered in
`mcp/tests/evidence-lifecycle.toml`. The cases drive direct assertions rather than parametrization, with
every assertion naming the part, member or reference it is about.

### Invariants And Boundaries

- **No case was removed to make room.** The module is new; it adds 29 cases to the unit population and
  changes no shipped case.
- **The absence assertions are made at both planes.** A case that asserted only the validator half would
  leave the schema free to hold the value later, so no column of any registered generation may carry a
  probe name.
- **Every refusal in this module is a shipped code**, and a refusal is asserted with its facts
  (`lineage_cycle` naming the record on the cycle, `invalid_reference` naming the identity) and with
  `wrote_nothing()`, so a check that fell through would fail on the refusal's facts as well as on the row
  count.
- **The generation contract is asserted against the generation actually landed on rather than a literal**,
  which is why the case carries its own `RENUMBERED for the sync` note. `260915-KS-L21` appended
  generation 9, so the case's registry-tip assertion was re-scoped in the same pass to the ordering fact
  it was standing in for; the source comment beside it records that a re-scoped assertion is the
  correction, not a weakening.
- **Nothing in this module writes outside a temporary root**, and the change set's own read is derived: two
  reads over unchanged rows are equal and dump to the same JSON.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module docstring stating what these cases protect: the six declared parts, the two exact snapshot identities, the membership, the succession edge, and preservation as a record that is not an effect. [1]
- The probe names that would make a change set a task authority rather than a record of authored work. [2]
- The probe names that would make a change set a decision, or a generated narrative. [3]
- The case that asserts both snapshot identities are stored verbatim, are not re-derived at read time, and must be two sides of one namespace. [4]
- The case that asserts all six declared parts are readable from one change set, the three member-declared ones as computed membership. [5]
- The case that asserts membership is computed from the members' own declarations, so a member is listed under one change set only. [6]
- The case that asserts preservation-without-effect and the memberless change set are both complete states. [7]
- The case that asserts no preservation spelling is in the closed effect set and no preservation flag fits the effect payload. [8]
- The case that asserts the three member kinds resolve to three distinct models sharing no table and no inheritance. [9]
- The case that asserts the preservation subject kind set is exactly the four declared kinds, with an effect label refused. [10]
- The case that asserts a preservation subject that resolves to nothing is kept verbatim and reported unresolved. [11]
- The case that asserts the unresolved state is reported for the subject that resolves to nothing and not for one that resolves. [12]
- The case that asserts supersession is a new record naming its exact predecessor while the predecessor survives. [13]
- The case that asserts the edge is written inside the successor's own creation batch and that no union member appends an edge. [14]
- The case that asserts a self-named predecessor is refused as the shipped lineage cycle with nothing written. [15]
- The case that asserts the appended generation's triggers seal the edge against an update and a delete. [16]
- The case that asserts two successors of one predecessor are two records and neither edits the other. [17]
- The generation-8 append: generation 7's thirty-three names keep their columns and primary keys and exactly one table is appended. **Re-scoped by `260915-KS-L21`:** the registry-tip identity assertion became an ordering assertion, so the case now records where generation 8 sits in the registry instead of asserting it is the tip. [18]
- **Generation 9, appended by `260915-KS-L21`, is why that assertion was re-scoped: generation 9's tables are generation 8's with only the census tables appended, and every generation-8 table keeps its columns and primary keys.** [19]
- The case that asserts a new store declares the current generation and is served by this record group's read. [20]
- The case that asserts a requirement-revision reference is stored verbatim, reported unresolved with its holder, and fabricates no requirement record. [21]
- The case that asserts near-miss spellings round-trip byte-identically and stay distinct, so nothing canonicalises them. [22]
- The case that asserts the shipped reference-length bound is a property of the record. [23]
- The case that asserts a reference or a realization-claim identity declared twice is refused. [24]
- The case that asserts an identity no stored claim carries is refused as an invalid reference naming it, with nothing written. [25]
- The case that asserts a reference whose row is gone is reported unresolved rather than dropped or re-pointed. [26]
- The case that asserts an open question declares exactly its fields and nothing records it answered. [27]
- The case that asserts no task status, seat ownership or approval is representable at either plane. [28]
- The case that asserts no verdict or generated summary field is representable and the payload's field set is exactly its declared composition. [29]
- The case that asserts the payload registers under exactly one kind and one schema. [30]
- The case that asserts the read projection reports every unresolved reference verbatim with its holder and that the scope list is exactly the union of the per-record lists. [31]
- The case that asserts the read is derived: two reads over unchanged rows are equal and dump to the same JSON. [32]
- The lane row placing this module in the unit population, as the last entry of the `unit-regression` list. **Re-cited by `260915-KS-L21`:** the leaf's one-line insertion of `mcp/tests/test_migration_census.py` at `:128` shifted every later row, so the four ranges this row carried were re-derived against the file as it now stands. [33]
- The registration listing this module among the exact consumers of the shared candidate-batch case harness. [34]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The cases exercise one in-process knowledge store
under a temporary root and construct no process, publication or Git object.

No meaningful cross-repo references found.
