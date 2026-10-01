# mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The `verification_observation` row codec: one observation's own row in both directions, and its
observable-row digest. It is the observation half of
[`evidence_records.py`](evidence_records.py.md), which imports every public name here and keeps it in its
own `__all__`, so callers name `evidence_records` and never this module. `260921-ICR-L57` moved the
codec here verbatim to keep `evidence_records.py` under the 1200-line rail. The move changed no
behaviour and no caller.

## Code Commentary

### Logic

**Why this codec separates cleanly.** An observation row is the only evidence row whose columns are a
flat projection of a frozen payload rather than a ledger edge. Its column order, its three
all-or-nothing column groups and its toolchain decoding form one unit, with no dependency on the claim,
subject, coverage or envelope codecs.

**`OBSERVATION_COLUMNS` is a declared order, not a convenience.** It is the generation's own column order
after the two key columns the write path supplies. `evidence.py` builds the insert statement's column
list from it, and `observation_row` builds the parameter tuple from `observation_cells` in the same
order. So a column added to the codec and not to the statement, or the reverse, cannot produce a
silently shifted row. `observation_cells` is keyed rather than positional for the same reason: the order
is written once.

**Every cell is derived from the frozen payload.** The row and the sealed revision cannot disagree about
what the run recorded. The knowledge snapshot's three columns are `NULL` together when the run tested
no knowledge dataset; that is the table's own constraint.

**The decode half refuses a partial group instead of guessing.** `decode_observation_row` rebuilds the
payload with `_snapshot_of_columns`, `_artifact_of_columns`, `_publication_of_columns` and
`_toolchain_of_column`. Each column group (knowledge snapshot, result artifact, publication) is either
wholly present or wholly `NULL`. A partly populated group, or a toolchain that is not a JSON list of
pairs, raises `KnowledgeStorageError` naming the observation, because it means the table's constraint
was bypassed.

**The observable-row digest is computed from the row as it stands.** The row is not a sealed revision.
An operation that names one by digest computes `observation_row_digest` over the namespace, the
observation identity and the exact payload the columns were projected from. `decode_observation_row`
recomputes it into the record's `row_digest`, which is the value the read path exposes. It is not a
digest of the artifact's bytes; that identity is `artifact_sha256`.

### Conventions

A codec module owns row ↔ value conversion and nothing else: no policy and no judgement. It refuses
only a stored row that breaks the table's own constraint. The private decoders are named for the column
group they rebuild.

### Invariants And Boundaries

- **Column order is contract.** The insert statement and the row tuple both derive from
  `OBSERVATION_COLUMNS`.
- **A digest is computed from the row as it stands.** No path returns a stored digest of the row.
- **One owner, one public door.** The codec is defined here and reached through `evidence_records`. A
  caller that imports this module directly would bypass the owner's single registered surface.
- **No blob.** The only digest that describes something outside the database is the artifact
  reference's, and it is carried as text.

### Todos

None.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's own statement that it is the observation half of `evidence_records`, re-exported there, and why it separates. [1]
- The observation's cells and the declared column order the insert statement is derived from. [2]
- The observation's row and its observable-row digest. [3]
- **The all-or-nothing column-group decoders and the toolchain decoder, each refusing a partial group by name.** [4]
- The decode, which recomputes the row digest rather than reading one. [5]
- **The re-export that keeps every caller naming `evidence_records`.** [6]
- The insert statement built from the declared order, and the write that uses the row tuple. [7]
- A case that decodes stored rows through the re-export. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
