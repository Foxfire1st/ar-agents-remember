# mcp/tests/facet_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/facet_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**The shared harness for the authored-judgment facet cases, and the measured constants they are read
against.** It owns two things no single facet case can own:

1. **One admitted candidate, built through the production application seam.** `build_admitted_candidate`
   writes an authorship envelope, admits a destination and initializes the namespace, and the writers in
   this module drive the real operations — the standalone facet operations through `write_facet` and the
   batch path through `apply_commands`/`change_knowledge_candidate` — so every facet case exercises the same
   admission, lock and transaction boundary a caller would.
2. **One recorded dataset whose page digests were measured before this leaf existed.** The
   `build_recorded_fixture` dataset is built through generation 2's own recorded DDL with fixed identities
   and a fixed authorship instant, so the page it produces is a function of the substrate rather than of a
   UUID draw — which is what makes the byte-identity evidence reproducible instead of merely plausible.

It is test support, not production code: it decides no behavior and holds no expectation. It is registered
as a governed artifact in `mcp/tests/evidence-lifecycle.toml` (contract `knowledge-facet-cases`) with
exactly one declared consumer, `mcp/tests/test_knowledge_facets.py`.

## Code Commentary

### Logic

- **The measured pre-leaf constants are observations, not assertions.** `PRE_LEAF_GENERATION_2_FINGERPRINT`,
  `PRE_LEAF_DATASET_DIGEST`, `PRE_LEAF_PAGE_DIGEST`, `PRE_LEAF_RESULT_DIGEST`,
  `PRE_LEAF_SELECTED_ITEMS`, `PRE_LEAF_ITEM_LIMIT` and `PRE_LEAF_MAX_PAGE_ITEMS` were read on the base
  revision — before this leaf existed — by building the recorded fixture and serializing what the shipped
  operations returned. The module's docstring says so, and the case that consumes them compares against
  them, so a shipped selection that moved would fail a measurement rather than a self-consistency check.
- **The recorded fixture is one construction, in one order.** `build_recorded_fixture` creates the file
  through `open_database` + `create_schema_statements(GENERATION_2)`, sets `PRAGMA user_version` to
  generation 2's own version, inserts the one `repository` row, then authors one invariant and revision,
  one family and family revision, one membership, one source anchor and one realization claim through the
  production store calls — with `REPOSITORY_ID`, `INVARIANT_ID`, `REVISION_ID`, `FAMILY_ID`,
  `FAMILY_REVISION_ID`, `MEMBER_ID`, `ANCHOR_ID`, `CLAIM_ID`, `FIXTURE_BLOB` and `FIXTURE_PATH` fixed, and
  an `Authorship` carrying a fixed `operation_id` and `recorded_at`. `build_recorded_generation_2_dataset`
  is the same creation without the fixture rows, for the case that needs a genuine version-2 dataset to
  refuse a facet write against.
- **`table_counts` counts what the *open dataset* declares**, iterating `store.generation.tables` rather
  than a literal table list — so the same helper measures a generation-2 dataset's own set, and "the
  refusal wrote nothing" is a comparison over the tables that dataset actually has.
- **The helpers drive the production entry points by kind.** `write_facet` maps the command's kind to the
  operation that owns it and builds a `FacetWriteRequest` carrying `destination.authorship`, so a case can
  drive all six writes through one call shape without hand-building a request per act; `store_facet`,
  `attach_facet` and `author_explanation` are the three convenience wrappers over it, each asserting the
  write was applied before returning the identities the case needs.
- **The subject and endpoint fixtures are authored, never fabricated.** `seed_subject` authors a real
  invariant and revision; `endpoints_for_subject` authors one stored target of **every** attachment kind
  (an anchor, a realization claim over that anchor, and a family with its revision and a membership) and
  returns one typed endpoint per kind, so the per-kind attachment walk has real rows to point at.
- **The union introspection is recursive rather than one `get_args` deep.** `member_models` walks an
  annotation that may be `Annotated[Union[…], Field]` or a bare union and collects only concrete
  `BaseModel` subclasses, because a `Literal` argument must not be mistaken for a member; `payload_kinds`,
  `declared_subject_kinds` and `command_kinds` are the three questions the closed-vocabulary cases ask
  through it.
- **`MINIMAL_PAYLOADS` is one valid payload per subtype, and `ENDPOINT_NOUNS` one noun per endpoint kind.**
  Both are declared data the cases read, so a case names the subtype or kind it varies and the assertion
  still says which one broke.

### Conventions

- **Build up, never down.** The recorded datasets are created from generation 2's own recorded DDL and its
  own recorded `user_version`; nothing here downgrades a generation-3 database to obtain a version-2 one.
- **Support only.** The module defines no fixtures, no policy and no expectation; the only assertions it
  contains are its own preconditions on the writes its wrappers drive (`assert written.state == "applied"`).
- **The harness is registered, not implicit.** A test module must appear in the lane manifest and a support
  module must appear as a governed artifact with an exact consumer list, because a module missing from
  either registry fails the collection rather than passing quietly.
- **`SHIPPED_COMMAND_KINDS` is the twelve shipped commands as data**, so the case that measures the widened
  union (12 → 18) states which twelve it means rather than restating them from the union it is testing.

### Invariants And Boundaries

- A store produced by `build_admitted_candidate` is an **admitted** candidate: its provenance comes from
  `write_authorship` and the destination, not from any payload a case supplies.
- The recorded fixture's digests are only meaningful against the exact construction above. A change to the
  fixture's identities, order or authorship instant invalidates the comparison, which is why the
  construction and the constants live in one module rather than in the case that reads them.
- **Boundary.** It is test support and is not importable by production code; it creates files only under the
  path a case hands it, and it opens nothing else.

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
| **The measured pre-leaf constants, recorded with the construction that produced them.** | `PRE_LEAF_GENERATION_2_FINGERPRINT`; `PRE_LEAF_DATASET_DIGEST`; `PRE_LEAF_PAGE_DIGEST`; `PRE_LEAF_RESULT_DIGEST` | mcp/tests/facet_test_support.py:92-100; mcp/src/agents_remember/memory/knowledge/schema_generations.py:284-284 |
| The one admitted candidate, built through the production seam with provenance from `write_authorship`. | `build_admitted_candidate` | mcp/tests/facet_test_support.py:177-192 |
| **The recorded fixture: generation 2's own DDL, fixed identities, a fixed authorship instant, and the production authoring calls.** | `build_recorded_fixture`; `build_recorded_generation_2_dataset` | mcp/tests/facet_test_support.py:535-658; mcp/tests/facet_test_support.py:516-532 |
| The count helper that measures the open dataset's own declared tables. | `table_counts` | mcp/tests/facet_test_support.py:452-458 |
| **The one write driver that maps a command kind to the operation that owns it and carries the admitted envelope.** | `write_facet` | mcp/tests/facet_test_support.py:362-380 |
| The three convenience wrappers that assert the write was applied before returning identities. | `store_facet`; `attach_facet`; `author_explanation` | mcp/tests/facet_test_support.py:394-416; mcp/tests/facet_test_support.py:419-431; mcp/tests/facet_test_support.py:434-449 |
| **The batch driver and the context resolution a batch precondition is built from.** | `apply_commands`; `resolve_context` | mcp/tests/facet_test_support.py:353-359; mcp/tests/facet_test_support.py:340-350 |
| The authored subject and the one stored target of every attachment kind. | `seed_subject`; `endpoints_for_subject` | mcp/tests/facet_test_support.py:195-223; mcp/tests/facet_test_support.py:322-337 |
| **The recursive union walk and the three closed-vocabulary questions the cases ask through it.** | `member_models`; `payload_kinds`; `declared_subject_kinds`; `command_kinds` | mcp/tests/facet_test_support.py:474-513 |
| The one valid payload per subtype and the one noun per endpoint kind. | `MINIMAL_PAYLOADS`; `ENDPOINT_NOUNS` | mcp/tests/facet_test_support.py:132-169 |
| The twelve shipped command kinds as data, so the widened union is measured against a stated set. | `SHIPPED_COMMAND_KINDS` | mcp/tests/facet_test_support.py:115-130 |
| **The governed artifact and its contract, with its one declared consumer.** | `knowledge-facet-cases`; "path = \"mcp/tests/facet_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1326-1326; mcp/tests/evidence-lifecycle.toml:55-55 |
| The production generation builder and the recorded generation-2 DDL the fixture is created from. | `create_schema_statements`; `GENERATION_2` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:173-180; mcp/src/agents_remember/memory/knowledge/schema_generations.py:208-208; mcp/src/agents_remember/memory/knowledge/schema_generations.py:284-292; mcp/src/agents_remember/memory/knowledge/schema_generations.py:186-192; mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-299; mcp/src/agents_remember/memory/knowledge/schema_generations.py:196-196; mcp/src/agents_remember/memory/knowledge/schema_generations.py:310-313; |
| The cases this harness exists for, and the byte-identity node that reads the measured constants. | "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy"; "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write" | mcp/tests/test_knowledge_facets.py:1002-1017; mcp/tests/test_knowledge_facets.py:935-979; mcp/tests/test_knowledge_facets.py:1053-1068; mcp/tests/test_knowledge_facets.py:1187-1194; mcp/tests/test_knowledge_facets.py:1135-1142; mcp/tests/test_knowledge_facets.py:1214-1214; mcp/tests/test_knowledge_facets.py:1162-1162 |
| The production generation builder and the recorded generation-2 DDL the fixture is created from. | `create_schema_statements`; `GENERATION_2` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:129-141; mcp/src/agents_remember/memory/knowledge/schema_generations.py:175-292; mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-299; mcp/src/agents_remember/memory/knowledge/schema_generations.py:310-313 |
| The cases this harness exists for, and the byte-identity node that reads the measured constants. | "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy"; "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write" | mcp/tests/test_knowledge_facets.py:986-1068; mcp/tests/test_knowledge_facets.py:935-985; mcp/tests/test_knowledge_facets.py:1187-1194; mcp/tests/test_knowledge_facets.py:1135-1142; mcp/tests/test_knowledge_facets.py:1214-1214; mcp/tests/test_knowledge_facets.py:1162-1162 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T00:57+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): hand-read the one enforced row this document carries and cleared it (`citation_anchor_absent_from_range`, "The governed artifact and its contract, with its one declared consumer."). The range written by the previous clearance (`evidence-lifecycle.toml:1318-1323`) no longer held `"path = \"mcp/tests/facet_test_support.py\""`: reading `mcp/tests/evidence-lifecycle.toml` shows that artifact block's own `path =` line now sits at `1326`, so the range was repointed to `1326-1326`; the row's other range (`55-55`, the `knowledge-facet-cases` contract id) is unchanged, as are its claim and both anchors. No claim was re-worded, no anchor or range was dropped to silence a finding, and no verification stamp was advanced. No commits.
- 2026-09-18T19:53:17+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The governed-artifact row cited `evidence-lifecycle.toml:1318-1318` (the previous lane's consumer list) for `"path = \"mcp/tests/facet_test_support.py\""`; the artifact's own `path = …` line sits at `1323`, so the range was widened to `1318-1323`. (b) and (c) Both generation-builder rows cited `schema_generations.py:310-310` — the closing `)` of `_compose_generation_2` — for `GENERATION_2`; the record itself is the next statement at `313` (`GENERATION_2 = _compose_generation_2()`), so each row's range was widened to `310-313`. Claims, anchors and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "path = \"mcp/tests/facet_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1318-1318. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "path = \"mcp/tests/facet_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1314-1314. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the new governed support module. It records the two capabilities no single facet case can own — one **admitted** candidate built through the production seam, and one **recorded** dataset whose page digests were measured on the base revision before this leaf existed — the pre-leaf constants as observations rather than assertions, the fixture construction (generation 2's own recorded DDL, fixed identities, a fixed authorship instant, the production authoring calls in one order), `table_counts` measuring the open dataset's own declared tables, the one write driver that maps a command kind to its owning operation, the authored subject and per-endpoint-kind targets, the recursive union walk behind the three closed-vocabulary questions, and the twelve shipped command kinds as data. It records the registration facts a new support module obliges: the `knowledge-facet-cases` contract and one exact consumer in `mcp/tests/evidence-lifecycle.toml`. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
