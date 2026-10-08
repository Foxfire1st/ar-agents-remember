# mcp/src/agents_remember/memory/knowledge/schema_v8.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Generation 8's appended table: the edge by which one semantic change set supersedes another. This
module owns **only what generation 8 appends** and declares no table of an earlier generation, so the
additive rule `KS-R10@v1` §1.3 states is a property of the file rather than of a review.

**The number is the landing's, not the branch's.** This leaf was authored against generation 4 and
renumbered to 8 at its sync, because three parallel leaves landed generations 5, 6 and 7 first. The
renumber moved a module name (`schema_v5.py` → `schema_v8.py`), one constant, one schema-name string
and one base argument — never the append's content. The module is an **append-only declaration** (the
`APPENDED_*` group with no `GENERATION_N` constant and no schema-name string of its own), so its number
lives in the composition, which is why the renumber was a composition edit plus a file rename.

## Code Commentary

### Logic

**One appended table, and the reason it is one.** Generation 1's ten tables, generation 2's six,
generation 3's four, generation 4's one, generation 5's one, generation 6's six and generation 7's five
stay declared verbatim in their own modules; `APPENDED_TABLES` names only `change_set_predecessor`.
The change set, the effect claim, the preservation claim and the unresolved question are all *typed
records* the shipped envelope already carries — `knowledge_record` holds the kind, the authority home,
the lifecycle and the governing route, and `record_revision` holds the frozen payload and its content
digest — so their payload shapes are registered in `PAYLOAD_MODELS` and are **not** restated as columns
here. What the envelope cannot express is a **record-to-record lineage edge**: its
`record_revision.predecessor_revision_id` is a revision-to-revision edge *inside* one record, and the
shipped envelope has no record-level predecessor at all. Requirement 4.8 makes the change-set
succession exactly that, so the edge is a row here rather than a field on the successor.

**The schema refuses what it can, so the write path is not the only guard.** The primary key is
`(repository_id, successor_change_set_id, predecessor_change_set_id)`, so one successor cannot record
the same predecessor twice, and `CHECK (successor_change_set_id <> predecessor_change_set_id)` refuses
the one-node cycle **in the schema**. The longer cycle is found by the shared acyclic walk over this
table, run inside the same transaction — the same rule and the same scan the two predecessor graphs and
the decision supersession edge use. Both endpoints are foreign keys to `knowledge_record`, so an edge
can only name records the same store holds; that the named records are *change sets* rather than some
other kind of envelope record is the write path's check, exactly as the decision supersession edge's
endpoint kind is, because a foreign key addresses a table and not a kind.

**Sealed against rewrite by triggers, not by remembering.** `change_set_predecessor_no_update` and
`change_set_predecessor_no_delete` raise `immutable_revision`, so "a predecessor change set is never
rewritten by the arrival of its successor" is a property of the schema — which is what makes a
changeset, a repair script or a future code path that forgot the rule still unable to break it.

**`APPENDED_FEATURES` is declared empty rather than omitted.** Generation 8 needs no SQLite feature
generation 7 does not already require: one table with checked foreign-key groups, a composite key, an
index and triggers are all covered by `strict_tables`, `deferrable_foreign_keys`,
`trigger_raise_abort` and `json_functions`. Declaring the empty tuple states the same fact generation
7's composition states, instead of leaving a reader to infer it from an absence.

### Conventions

This appended-table module states its own declarations and no row-writing behavior. schema_generations._compose consumes it after schema_v7 to build the single pinned derived-index schema. Tables, columns, primary keys, typed-JSON sets, DDL, indexes, triggers and features remain declared data; primary-key order is not inferred from DDL.

### Invariants And Boundaries

- No ALTER TABLE or inherited declaration rewrite appears here. The one _compose preserves earlier table declarations while adding change_set_predecessor, and require_pinned_schema_unchanged checks the complete index schema. The former GENERATION_7 and GENERATION_8 registry records are retired.
- This block declares only change_set_predecessor. Historical canonical-database effect records and their envelope writes were admitted by EFFECT_WRITABLE_TABLES and MutableRecordTable; that writer/table vocabulary was retired by MIK-R26. This module supplies derived-index declarations and grants no write capability.
- **No table here carries a content address, a logical digest or a fingerprint.** Requirement 3.7 of
  the envelope's own contract puts the content digest on `record_revision`, and none is added here.
- This declaration module performs no migration or row writing. The derived-index opener admits only the single CURRENT_GENERATION schema and refuses another declared database version; no legacy database is migrated or guessed into this schema.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one appended table — the only name this generation adds. [1]
- The appended columns, primary key and typed-JSON column, declared as the generation's pinned structure rather than derived from the DDL text. [2]
- The DDL: the composite primary key, the one-node-cycle `CHECK`, and the two foreign-key groups that make an edge able to name only records this store holds. [3]
- The reverse-direction index — "which change sets supersede this one" — and the no-update / no-delete triggers that seal a recorded succession. [4]
- The declared-empty feature tuple: generation 8 requires nothing generation 7 did not already require. [5]

- The ordered appended declarations compose into the one pinned derived-index schema. [6]


- This build creates and reads the single v9 derived-index schema; another declared database version is refused. [7]


### Cross-Repo References

No cross-repository behavior is implemented in this file. A table declaration is a property of the
dataset, and a dataset's identity excludes Git commits, ledger rows and checkout locations.

No meaningful cross-repo references found.
