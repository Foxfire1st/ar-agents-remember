# mcp/tests/test_knowledge_store.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Read behavior and schema integrity of derived knowledge index files.

## Code Commentary

### Logic

Test-only rows supply separately recorded single-revision identities sharing the derived display label `r1`. Production readers retain their exact statements and empty predecessor sets, reopen exact identities/digests and reject write attempts and refuse absent-file opens.

Cases protect database immutability triggers, read-time payload seals, declared schema structure and its pin. Missing tables or triggers refuse open; unsupported versions also name conversion.

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
| `test_lower_ranked_owners_do_not_import_the_memory_domain` | the checked `worktrees` and `memory_quality` modules contain no direct imports of the memory domain |

### Conventions

The module imports the fixture through the bare module name `knowledge_fixture_test_support`.
`mcp/tests/conftest.py` prepends the product and test-support directories to `sys.path`. Assertions name the observable outcome (state, refusal
code, offending record, row counts) rather than internal call order.

### Todos

None recorded.

The schema pin is ar-knowledge-sqlite/v10 with user_version 10. The expected derived tables include ix_revision. The open guard refuses generations 1, 9 and 11 by name.

## Evidence

### Docs References


### Repo-Internal References
























### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.


### Repo-Internal References (continued)






- The layer-direction case. [17]

### Cross-Repo References

No cross-repository contract is established by this file.

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

### Repo-Internal References (continued)



### Repo-Internal References (renewed)

- The shared branching fixture used by the revision cases. Anchor: `build_branching_knowledge_fixture` [18]


- The schema pin observes the new generation and verifies table drift refusal. [25]
- The declared derived table set includes ix_revision. [26]

- The unit-regression lane selects mcp/tests/test_knowledge_store.py. [19]

- The identity-branching replacement contract declares mcp/tests/test_knowledge_store.py::test_three_separately_recorded_revisions_stay_independently_addressable as its evidence node. [20]

- The seal covering more than the statement. [16]
- The current separate-record revision read: three single-revision records stay independently addressable, and the former divergent-successor population is not this fixture's executable coverage. [14]
- The database-level immutability proof against the stored revision rows. [15]

- Read-only production store and test-only builder. [13]
- Three separately recorded single-revision records stay independently addressable with their exact statements. [1]
- Identity/schema preserved on reopen. [2]
- Stored revisions reject mutation. [6]
- Decode verifies seal beyond statement. [7]
- Schema drift and unsupported files refuse. [8]
