# mcp/src/agents_remember/memory/knowledge/schema_v5.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v5.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Generation 5's appended table and nothing else: the authored `CitationBinding` record. Generation 1's
ten tables, generation 2's six, generation 3's four and generation 4's one stay declared verbatim in
`schema.py`, `schema_v2.py`, `schema_v3.py` and `schema_v4.py`.

## Code Commentary

### Logic

`APPENDED_TABLES` names the one table, and the five registries beside it (`APPENDED_COLUMNS`,
`APPENDED_PRIMARY_KEYS`, `APPENDED_JSON_COLUMNS`, `APPENDED_TABLE_DDL`, `APPENDED_INDEX_DDL`,
`APPENDED_TRIGGERS`, `APPENDED_FEATURES`) declare what `_compose_generation_5` merges into generation
4's maps. `citation_binding` carries the prose owner revision (repository, confined document path,
recorded blob identity), the local citation key as a declared form plus its exact text, the typed
target reference, the locator's discriminator, and the nullable governing-route foreign key.

### Invariants And Boundaries

- **Appending is the only sanctioned way to add a table** (`KS-R10@v1` §1.3). Nothing here
  redeclares, reorders, renames, retypes or drops a generation-1..4 table, and no `ALTER TABLE`
  against an earlier generation's table exists anywhere in this package.
- **There is no digest, content address or fingerprint column, and the absence is the point.** The
  owner revision's blob identity is a *reference* to an identity the memory side already records, not
  a second one minted here. Ambiguity is decided by equality over the recorded key text.
- **The local key is stored as a form and its exact text.** `UNIQUE (repository_id,
  owner_document_path, owner_blob_object_id, local_key_form, local_key_text)` makes "one owner
  revision records one key once" a constraint of the table rather than a rule the write path
  remembers.
- **`target_locator_kind` is checked against the shipped union.** The `CHECK` names the union's three
  members and no fourth, so a binding-local locator spelling is inexpressible rather than merely
  unwritten.
- **The governing route is a nullable foreign key on the binding's own row**, resolved against the
  existing `route` entity: at most one governing route per binding is a constraint, a named route
  that does not exist is unrepresentable, and `NULL` is the explicit **ungoverned** state.
- **The recorded facts are sealed by triggers.** Rewriting a key or re-pointing a target in place
  would silently re-bind the row to prose that says something else; generation 5's triggers refuse
  exactly that, while leaving `lifecycle` free because a binding's lifecycle is its owner's.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one table generation 5 appends, and the registries the composition merges from.** | `APPENDED_TABLES`; `APPENDED_COLUMNS`; `APPENDED_PRIMARY_KEYS` | mcp/src/agents_remember/memory/knowledge/schema_v5.py:62-62; mcp/src/agents_remember/memory/knowledge/schema_v5.py:64-81; mcp/src/agents_remember/memory/knowledge/schema_v5.py:83-89 |
| The typed-JSON column registry, which is where the binding payload actually travels. | `APPENDED_JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v5.py:91-93 |
| **The table DDL: the unique key over the recorded key text, and the `CHECK` that names exactly the shipped locator union.** | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v5.py:95-132 |
| The index DDL and the triggers that seal the recorded facts against in-place re-binding. | `APPENDED_INDEX_DDL`; `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v5.py:134-146; mcp/src/agents_remember/memory/knowledge/schema_v5.py:148-165 |
| **The composition that puts generation 5's table after generation 4's twenty-one and asserts the prefix equality.** | `_compose_generation_5`; `GENERATION_5` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:357-365; mcp/src/agents_remember/memory/knowledge/schema_generations.py:321-325; mcp/src/agents_remember/memory/knowledge/schema_generations.py:336-352 |
| The schema name and version generation 5 declares, and its place in the registry. | `GENERATION_5_SCHEMA_NAME` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:212-212 |
| The generation-2 `route` table the governing-route foreign key resolves against. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49 |
| The generation the write path requires before a binding row may exist. | `REQUIRED_BINDING_GENERATION` | mcp/src/agents_remember/memory/knowledge/citations.py:88-88 |
| **The cases that measure the append without touching generation 4's names, the absent identity column, and the locator `CHECK` naming exactly the shipped union.** | `test_generation_5_appends_to_generation_4_without_touching_its_twenty_one_tables`; `test_the_binding_table_has_no_content_address_digest_or_fingerprint_column`; `test_the_locator_check_names_exactly_the_shipped_source_locator_union` | mcp/tests/test_knowledge_citation_bindings.py:118-176 |
| The boundary case that proves a generation-4 dataset is refused the binding table rather than widened. | `test_a_generation_4_dataset_is_refused_the_binding_table_rather_than_widened` | mcp/tests/test_knowledge_citation_boundaries.py:598-628 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A table declaration is a property of the
dataset, and a dataset's identity excludes Git commits, ledger rows and checkout locations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_a_generation_4_dataset_is_refused_the_binding_table_rather_than_widened` repointed to mcp/tests/test_knowledge_citation_boundaries.py:598-628. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_5_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `GENERATION_5_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for generation 5's one appended table. It records the three decisions a reader must not get wrong. First, **appending is the whole additive rule** — five registries merge into generation 4's maps and nothing earlier is redeclared, reordered, renamed, retyped or dropped, with the prefix-equality assertion written *by the generation it descends from* so a future renumber changes two names and not a column list. Second, **the table deliberately has no digest, content address or fingerprint column**: the owner revision's blob identity is a reference to an identity the memory side already records, and ambiguity is decided by equality over the recorded key text, which is the fact at issue. Third, **the recorded facts are sealed by triggers** while `lifecycle` stays free, because rewriting a key or re-pointing a target in place would silently re-bind the row to prose that says something else. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
