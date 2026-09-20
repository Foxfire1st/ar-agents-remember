# mcp/tests/generation_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/generation_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T22:00+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

Support for cases that must observe a specific schema *generation*. Generation 2 makes "which schema is this" a
property of the dataset rather than of the build, and a created store is generation 2, so a case that must assert a
**generation-1** fact cannot use the ordinary creation path: it has to bring a version-1 dataset into being and open
it. This module owns that one capability, so no case re-derives it.

It is test support, not production code: it decides nothing about behavior and holds no expectation. Its docstring
states the two decisions it does encode — the dataset is built from generation 1's own recorded DDL and its own
recorded `user_version`, never by downgrading a generation-2 database (which would leave generation 2's tables behind
and test something else), and it is then opened through the production open path so a case exercises real validation
rather than a private shortcut.

## Code Commentary

### Logic

`create_generation_1_store(database_path, repository_id)` opens the file with the production `open_database`, executes
`create_schema_statements(GENERATION_1)` — generation 1's tables, then its indexes, then its triggers in sorted name
order — sets `PRAGMA user_version` to `GENERATION_1.user_version`, inserts the one `repository` row (with authority
home `memory:<repository_id>`), closes the connection, and returns
`open_existing_knowledge_store(path, repository_id)`. The DDL therefore comes from generation 1's recorded data, so the
file carries generation 1's ten tables, generation 1's triggers and version 1.

`declared_pair(database_path)` opens the file read-only, reads `PRAGMA user_version`, resolves it through
`generation_for_version`, asserts that a registered generation declares that version, and returns
`(generation.schema_name, version)`. The docstring records why the returned name is the registry's rather than the
file's: a SQLite file does not store the application schema name, so the registry's name for the file's recorded
version is exactly what the open path resolves. `declared_schema_name` is the single-value reader over that pair.

### Conventions

- **Build up, never down.** A genuine version-1 dataset is created from generation 1's record; downgrading a
  generation-2 database is explicitly rejected as a way to obtain one.
- **Open through the production path.** `open_existing_knowledge_store` is used rather than a hand-built connection, so
  the store a case receives has passed the real open-time validation.
- **Support only.** The module defines no fixtures, no policy and no expectation; the one `assert` it contains is about
  its own precondition (the version it read resolves to a registered generation).
- **Shared by the generation-aware cases.** Both `test_knowledge_schema_generations.py` and
  `test_knowledge_merge_generations_and_envelope.py` import `create_generation_1_store` by module name.

### Invariants And Boundaries

- A store produced here is a **genuine version-1 dataset**: generation 1's ten tables, generation 1's triggers and
  `PRAGMA user_version = 1`, not a version-2 dataset wearing an old number.
- It depends on generation 1's record staying pinned. If generation 1's declared tables, DDL or `user_version` moved,
  the datasets the cases build would stop being version-1 datasets — the same family of change the package's pin gate
  exists to fail on.
- **Boundary.** It is test support and is not importable by production code; it creates files only under the path a
  case hands it, and it opens nothing else.

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
| The version-1 creation path: generation 1's DDL, generation 1's `user_version`, the repository row, then the production open. | "def create_generation_1_store(database_path: Path, repository_id: str) -> OpenedKnowledgeStore:" | mcp/tests/generation_test_support.py:67-70 |
| The module's own reason for existing: a generation-1 fact cannot use the ordinary creation path, and downgrading a generation-2 database would test something else. | "which schema is this" | mcp/tests/generation_test_support.py:1-13 |
| The pair reader, and why the schema name it reports is the registry's rather than the file's. | `declared_pair`; `declared_schema_name` | mcp/tests/generation_test_support.py:115-135 |
| The production builder that turns a generation record into its statements — re-cited by hand after the registry grew to four generations. | `create_schema_statements` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:196-202 |
| Generation 1's own record, which the support reads both the DDL and the version from rather than from a literal. | `GENERATION_1` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:217-229 |
| The version-to-generation resolution this support reads a file through. | `generation_for_version` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:527-530 |
| The production open paths the support deliberately goes through. | `open_database`; `open_read_only_database`; `open_existing_knowledge_store` | mcp/src/agents_remember/memory/knowledge/connection.py:26; mcp/src/agents_remember/memory/knowledge/connection.py:52; mcp/src/agents_remember/memory/knowledge/store.py:42-42; mcp/src/agents_remember/memory/knowledge/store.py:751; mcp/src/agents_remember/memory/knowledge/store.py:787-800 |
| The unit module that consumes this support, whose import is its consumer declaration. | "from generation_test_support import create_generation_1_store, create_generation_2_store" | mcp/tests/test_knowledge_schema_generations.py:62-62 |
| The merge module that joined this support's consumer scope with this leaf. | "from generation_test_support import create_generation_1_store, create_generation_2_store" | mcp/tests/test_knowledge_merge_generations_and_envelope.py:60-60 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:28:52+00:00: Generated citation repair: "from generation_test_support import create_generation_1_store, create_generation_2_store" repointed to mcp/tests/test_knowledge_merge_generations_and_envelope.py:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `create_schema_statements` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:196-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `generation_for_version` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:527-530. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `create_schema_statements` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:186-192. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_1` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:217-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_for_version` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:495-498. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand while resolving the memory sync** — `create_schema_statements`, `GENERATION_1`, `generation_for_version`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `generation_for_version`, `create_generation_1_store`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read the generator row against the current registry and re-cited it by hand.** The row named two anchors across two stale ranges and is now one anchor per row: `create_schema_statements` at `:135-141` and generation 1's own record at `:162-180`. The claim is unchanged — the support reads both the DDL and the declared version from generation 1's own record rather than from a literal, which is exactly why appending a fourth generation did not falsify it. Verification metadata is not advanced: this support module's source did not change in this leaf.

- 2026-09-17T20:00:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`; the module is untracked in the leaf's code worktree): created this one-to-one card for the new shared support module. It records the build-up-never-downgrade rule, the use of generation 1's own recorded DDL and version, the production open path, and the two consuming test modules that define its scope.
