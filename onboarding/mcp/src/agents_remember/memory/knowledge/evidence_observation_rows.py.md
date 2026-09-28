# mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T23:41:23+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4`|
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement that it is the observation half of `evidence_records`, re-exported there, and why it separates. | `__all__` | mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:1-37 |
| The observation's cells and the declared column order the insert statement is derived from. | `observation_cells`; `OBSERVATION_COLUMNS` | mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:40-78; mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:80-102 |
| The observation's row and its observable-row digest. | `observation_row`; `observation_row_digest` | mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:105-109; mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:112-130 |
| **The all-or-nothing column-group decoders and the toolchain decoder, each refusing a partial group by name.** | `_snapshot_of_columns`; `_artifact_of_columns`; `_publication_of_columns`; `_toolchain_of_column` | mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:133-150; mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:153-175; mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:178-195; mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:228-243 |
| The decode, which recomputes the row digest rather than reading one. | `decode_observation_row` | mcp/src/agents_remember/memory/knowledge/evidence_observation_rows.py:198-225 |
| **The re-export that keeps every caller naming `evidence_records`.** | "from agents_remember.memory.knowledge.evidence_observation_rows import ("; `__all__` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:39-45; mcp/src/agents_remember/memory/knowledge/evidence_records.py:944-1006 |
| The insert statement built from the declared order, and the write that uses the row tuple. | `_OBSERVATION_INSERT_COLUMNS`; `observation_row` | mcp/src/agents_remember/memory/knowledge/evidence.py:113-121; mcp/src/agents_remember/memory/knowledge/evidence.py:280-280 |
| A case that decodes stored rows through the re-export. | `test_the_write_time_digest_is_checked_against_the_bytes_and_recorded_as_checked` | mcp/tests/test_knowledge_evidence_observations.py:331-380 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): created this one-to-one card for the observation row codec, which the worker moved verbatim out of `evidence_records.py` to bring that module under the 1200-line rail. It reuses the `OBSERVATION_COLUMNS` and column-group text from `evidence_records.py.md`, where the text was removed. It adds the refusal rule for partial groups and the re-export boundary. Verification metadata remains empty until closeout stamps the code commit.
