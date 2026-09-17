# mcp/src/agents_remember/memory/knowledge/schema_v2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T19:11+00:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Generation 2's appended tables, as pinned data.** Six tables — `route`, the `knowledge_record`
envelope, `record_revision`, and the three governing-route joins — with their column orders, key
tuples, typed-JSON column sets, DDL, indexes and immutability triggers.

This module owns **only what generation 2 appends**. Generation 1's ten tables stay declared verbatim
in `schema.py`; nothing here redeclares, reorders, renames, retypes or drops one of them. That is
requirement 1.3 as a hard rule rather than a convention, and it is the reason the governing-route
association is expressed as new join tables instead of as a `governing_route_id` column added to
`source_anchor`, `invariant` or `family`: appending a column to a generation-1 table would change
that table's declared column set, and generation 1's own record must keep declaring the table without
it.

## Code Commentary

### Logic

The module is pure data: it defines **no functions and no classes**. Its whole surface is eight
module constants, and each is a member of the generation record `schema_generations.GENERATION_2`
composes:

- `APPENDED_TABLES` — the ordered tuple `("route", "knowledge_record", "record_revision",
  "source_anchor_route", "invariant_route", "family_route")`. The order is load-bearing: it is the
  order the encoder serializes them in, and it is appended after generation 1's ten so generation 2's
  manifest **begins with** generation 1's, unchanged.
- `APPENDED_COLUMNS`, `APPENDED_PRIMARY_KEYS`, `APPENDED_JSON_COLUMNS` — the per-table declared
  column order, key tuple and typed-JSON set the encoder orders and decodes rows through.
- `APPENDED_TABLE_DDL` — one `CREATE TABLE` per appended table.
- `APPENDED_INDEX_DDL` — nine indexes, each covering the reverse direction of a declared lookup.
- `APPENDED_TRIGGERS` — eight immutability triggers.
- `APPENDED_FEATURES` — `("json_functions",)`, the one SQLite feature generation 2 needs beyond
  generation 1's set, because `json_valid` now appears in a `CHECK`.

Why the tables are shaped this way:

- **`route`** carries a repository-relative code-path scope and a self-referencing parent. The
  self-reference is `ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED` like every shipped foreign
  key, so one transaction may insert a whole hierarchy without depending on insert order. The
  one-node cycle is a `CHECK (parent_route_id IS NULL OR parent_route_id <> route_id)`; the longer
  cycle is found by a recursive-CTE walk run inside the same transaction before commit
  (`routes.require_acyclic_routes`).
- **`knowledge_record`** is the envelope, and it carries **no content address, no logical digest and
  no fingerprint column**. That absence is the enforcement of requirement 3.3: a table with no
  identity-valued column cannot quietly become a second identity authority later. It carries `kind`,
  `authority_home`, `lifecycle`, `record_schema` and a nullable `governing_route_id` referencing
  `route`. `record_schema` names the frozen payload shape its `kind` resolves to; it is **not** a
  fingerprint.
- **`record_revision`** is where the payload lives, because `Doc13:85` puts "revision payload/schema"
  on the revision rather than on the envelope. `payload` is the typed-JSON column —
  `TEXT NOT NULL CHECK (json_valid(payload))` — which is what `storage-design.md:97` means by
  `TEXT_JSON`, and it is why generation 2 adds `json_functions` to its feature set. The revision also
  carries `content_digest`, an optional predecessor and provenance.
- **The three `*_route` tables** associate a shipped generation-1 entity with the route that governs
  it: `source_anchor_route`, `invariant_route`, `family_route`. Each takes the governed entity's key
  as its **own primary key**, which makes "at most one governing route per governed row" a constraint
  of the table rather than a convention, and each foreign key names one exact table, which is the
  endpoint-kind compatibility `Doc13:102` requires of a scoped association.

### Conventions

- Every table is `STRICT`, every primary-key column is declared `NOT NULL` explicitly, and every
  foreign key is composite and `DEFERRABLE INITIALLY DEFERRED`, exactly as the ten shipped tables are.
- Trigger messages share the shipped `immutable_revision:` prefix so `map_sqlite_error` steers a
  trigger-originated error to that code. The eight triggers refuse: rewriting a sealed record
  revision (`record_revision_no_rewrite`, covering `record_schema`, `payload`,
  `predecessor_revision_id`, `content_digest` and `provenance`), deleting one
  (`record_revision_no_delete`), rebinding an envelope's identity (`knowledge_record_no_rebind`),
  rebinding or deleting a route (`route_no_rebind`, `route_no_delete`), and repointing a governing
  association (`source_anchor_route_no_repoint`, `invariant_route_no_repoint`,
  `family_route_no_repoint`).
- Index names are a local choice, not contract; each covers the reverse direction of a lookup the
  package performs (`route_parent`, `route_path`, `knowledge_record_kind`,
  `knowledge_record_governing_route`, `record_revision_record`, `record_revision_predecessor`, and
  one route index per join table).

### Invariants And Boundaries

- **No `ALTER TABLE` appears anywhere in this module or in this package.** The single occurrence of
  the phrase in this file is inside its own docstring, as the prohibition. A generation that changed
  a column of an earlier generation is a schema divergence, not a generation.
- **Generation 2's manifest prefix is generation 1's manifest, byte for byte**, and generation 2's
  columns for each of the first ten names are generation 1's. That equality is the mechanical check
  the additive rule reduces to.
- **The envelope holds no identity.** It mints none, derives none and overrides none; `payload_digest`
  stays where generation 1 put it, on the revision aggregate that owns it; `Repository` remains the
  authority home.
- **Immutability is enforced by the database, not only by the operation.** These triggers exist so a
  changeset, a repair script or a future code path that forgot the rule still cannot rewrite a sealed
  revision or repoint a sealed association. The operations' own preconditions exist to return a typed
  refusal; the triggers exist so that forgetting them still cannot corrupt the record.
- **Boundary.** This module declares structure and nothing else: it writes no rows, performs no
  validation, returns no refusal, and owns no behaviour. Authoring a route or an association is
  `routes.py`; validating a payload is `record_envelope.py`; deciding which generation a dataset is,
  is `schema_generations.py`.
- **Not admissible, recorded so it is not re-proposed:** adding `governing_route_id` to a generation-1
  table. Requirement 1.3 forbids changing a generation-1 table's declared column set, and the
  additive check rejects it.

### Todos

None recorded. The concrete record groups the envelope will carry (`EvidenceClaim`,
`DetectionSignal`, …) are later leaves; this module declares the envelope they will use and the one
internal conformance kind that exercises its seam.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ordered appended-table tuple whose prefix rule makes generation 2's manifest begin with generation 1's ten tables. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49 |
| The declared column order, key tuple and typed-JSON set per appended table — the encoder's ordering and decoding inputs. | `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:51-101 |
| The six `STRICT` `CREATE TABLE` statements, including the route self-reference and its one-node cycle `CHECK`, and the typed-JSON payload column with `json_valid`. | `STRICT`; `CREATE TABLE`; `CHECK`; `json_valid` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-204 |
| The nine reverse-direction indexes, including the governing-route lookup index. | `APPENDED_INDEX_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:205-221 |
| The eight immutability triggers: sealed revisions cannot be rewritten or deleted, identities cannot be rebound, and a governing association cannot be repointed. | `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:222-262 |
| The one added required feature, which is part of the fingerprint because it is part of the manifest. | `APPENDED_FEATURES` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:263 |
| The generation record this module's data is composed into, and the additive composition that keeps generation 1's prefix intact. | `GENERATION_2` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:188 |
| The shipped generation-1 tables this module appends after and never touches. | `CANONICAL_TABLES` | mcp/src/agents_remember/memory/knowledge/schema.py:29-42 |
| The write layer that authors a route and attaches a governed row, and the read side that reports an ungoverned row as ungoverned. | `author_route` | mcp/src/agents_remember/memory/knowledge/routes.py:225-279 |
| The payload seam these envelope tables are read through: one registry, one entry point, the shipped `invalid_payload` code. | `validate_record_payload`; `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:69-113 |
| The schema disagreement the preflight refuses before any session exists, and the same-generation merge that must still pass on this build. | `selected_generation` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:110-155 |
| The envelope, route and governing-association cases, including the route-cycle rollback and the payload refusal. | `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1`; `test_a_confined_path_is_authored_and_its_identity_returned` | mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-311; mcp/tests/test_knowledge_routes.py:1-199 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for generation 2's appended tables. It records the additive prefix rule that makes "generation 2 is generation 1 plus these six" checkable, the exact six table names in serialization order, the deliberate absence of any identity-valued column on the envelope, the typed-JSON payload column that is the reason generation 2 adds `json_functions`, the per-join-table primary key that makes "at most one governing route per governed row" a constraint rather than a convention, and the eight triggers as the database-level backstop. It also records the excluded form (`ALTER TABLE … ADD COLUMN governing_route_id`) with the reason, so a later leaf does not re-propose it. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
