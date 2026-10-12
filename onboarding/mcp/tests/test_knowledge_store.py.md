# mcp/tests/test_knowledge_store.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Read behavior and schema integrity of derived knowledge index files.

## Code Commentary

### Logic

Test-only rows supply separately recorded single-revision identities sharing the derived display label `r1`. Production readers retain their exact statements and empty predecessor sets, reopen exact identities/digests and reject writable or absent-file opens. [1] [2] [13]

Cases protect database immutability triggers, read-time payload seals, declared schema structure and its pin. Missing tables/triggers or another version refuse open and name conversion. Canonical insert/duplicate/lineage write rules and their old cases are removed. [6] [7] [8]

### Invariants And Boundaries

- Production opens are read-only; fixture row insertion is test-only.
- Schema drift refuses rather than repairing or re-pinning.

### Logic

| Node | Protects |
| --- | --- |
| `test_three_separately_recorded_revisions_stay_independently_addressable` | three single-revision records stay independently addressable with their exact statements after a close/reopen cycle |
| `test_reopening_the_same_path_keeps_identity_and_schema` | reopen validates the same generation instead of creating or repairing |
| `test_stored_revision_rows_refuse_update_and_delete` | direct `UPDATE`/`DELETE` raises `immutable_revision` at the database level |
| `test_payload_digest_seals_more_than_the_statement` | the seal covers the stored cells, so a rewritten cell fails the read-time check |
| `test_lower_ranked_owners_do_not_import_the_memory_domain` | the layer direction holds: no owner below `memory` imports the storage package |

### Conventions

The module imports the fixture through the bare module name `knowledge_fixture_test_support`, which is how
`mcp/tests/conftest.py` puts this directory on `sys.path`. Assertions name the observable outcome (state, refusal
code, offending record, row counts) rather than internal call order.

### Todos

None recorded. Later leaves (KS-R02 … KS-R08) extend the fixture and add their own modules rather than growing this
one.

## Evidence

### Docs References


### Repo-Internal References

- Three separately recorded single-revision records stay independently addressable. [1]


- Identity/schema preserved on reopen. [2]


- Stored revisions reject mutation. [6]


- Decode verifies seal beyond statement. [7]


- Schema drift and unsupported files refuse. [8]


- Read-only production store and test-only builder. [13]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

- The current separate-record revision read; the former divergent-successor population is not this text fixture's executable coverage. [14]
- The database-level immutability proof against the stored revision rows. [15]
- The seal covering more than the statement. [16]
- The layer-direction case. [17]
- The shared fixture every case builds from. [18]
- The lane registration that makes the repository's manifest load (this module's row inside the lane, after the `KS-R03` insertions). [19]
- The fixture's registered stable contract and evidence node. [20]

### Cross-Repo References

No cross-repository contract is established by this file.

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
