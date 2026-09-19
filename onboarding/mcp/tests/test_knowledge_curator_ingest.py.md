# mcp/tests/test_knowledge_curator_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_curator_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:14+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312` |
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

The module is the evidence for the curator's **reachable single-entry write path**: one hand-off entry
becomes one admitted batch and one readable citation. Until
`agents_remember.application.knowledge_ingest` existed the knowledge write plane had no production
caller — every importer of the application knowledge seam was a test, and the mounted change tool
refuses every record kind — so these six cases are that path's own proof, and each one names the part
of the claim it measures.

What they pin, as properties rather than as a list:

- a citation committed for a **symbol** and one committed for a **line range** both read back with
  their path, their recorded source identity and their **decoded** locator, on the mounted
  source-context view rather than on the raw column;
- the locator of a row the ingest did **not** write is decoded too — the read-path defect the fix
  closes, because a consumer handed the stored text can classify no locator at all;
- the claim really is the edge `invariant_revision_id -> anchor_id` the statement is reached by, not a
  convention a reader has to assume;
- the recorded blob identity is what the knowledge lane's own observation can verify: the exact
  recorded bytes pass, and different bytes recorded at the same path are reported as a mismatch rather
  than as a success;
- no ingest moves a sealed revision: equal sealed content digests equally with and without a citation,
  every pre-existing revision row stays byte-identical, and the citation is a second record beside it.

Those properties are what make the write path auditable after the fact: an obligation is attributable
only if its citation survives the round trip, is reached by a recorded edge, and names bytes the
observation can confirm. The list-level half of the operation — the leaf's own line as the resolution
tree, the refusal vocabulary, dry runs and the route leg — belongs to
`mcp/tests/test_knowledge_curator_ingest_list.py` and is not re-protected here.

## Code Commentary

### Logic

`Authored` pairs one `CuratorEntry` with the `CuratorCitation` its assertions name later. The module
constants are the fixed spellings the cases vary a fact around: `SYMBOL_LOCATOR`, `RANGE_LOCATOR` and
`RATIONALE`, plus `WRONG_RECORDED_BLOB`, a 40-zero object id the fixture tree does not hold at
`INTEGRATION_PATH` — which is what makes "the bytes at this path are not the bytes this anchor
recorded" a measurement about the tree rather than a constant.

The `fixture` is the shipped `ReadScopeFixture`: one real dataset beside one real Git tree, built
through the public write operations, which is what lets the observation cases resolve against bytes.
The drive helpers are `admitted` (the fixture's own dataset admitted as the curator's draft-candidate
destination), `resolution` (the candidate inputs the batch context resolves against), `authored` (one
entry carrying one resolved citation at one recorded location) and `committed` (the commit, raising
with the receipt's refusal whenever the batch is not `changed`). The read helpers are `stored_anchor`
(the anchor as the store reads it back, decoded to the typed union), `view_rows` (the mounted
`source_context` view), `row_for` (the single view row a claim produced) and `observed`, which hands
`observe_anchor` the **decoded** locator — the decode is the point, because the resolver classifies on
the typed union and not on the stored text.

Six cases, each a different half of the claim:

- `test_a_symbol_citation_reads_back_with_its_path_identity_and_locator` — a symbol is the preferred
  pointer, and the recorded pair survives the round trip whole: the path, the object id and a
  `SymbolLocator` equal to the one written. The lane has no symbol extractor and says so: the
  observation is `unsupported_locator` with the recorded identity preserved, because an observation
  that reported a path resolution for a symbol locator would be a resolution the recorded claim never
  made.
- `test_a_line_range_citation_reads_back_as_its_recorded_extent` — the extent `(3, 7)` is carried into
  the store and back out through the mounted view: it is the recorded rendering, not the record's
  identity.
- `test_the_read_surface_decodes_the_locator_of_a_row_the_ingest_did_not_write` — the row was written
  by the single-record operation before any ingest ran, so the statement is about the reader: the raw
  column really holds text, the reader port hands the view a flat payload keyed by record identity,
  and the mounted view still returns a `LineRangeLocator` for a claim no ingest wrote. The same decode
  is what keeps a symbol locator from falling through to the file branch and being published as a path
  resolution.
- `test_the_claim_is_the_edge_from_the_revision_to_its_anchor` — `get_realization_claim` and
  `find_claim_by_pair` prove the recorded edge, the role `enforcement` and the rationale, and the view
  row names the claim as its subject with the cited revision beside it, so a consumer reading the
  citation reads which statement it belongs to.
- `test_the_recorded_blob_identity_is_what_the_observation_can_verify` — the exact recorded blob
  observes `exact_recorded_blob`, while a deliberately wrong recorded identity observes
  `recorded_blob_mismatch` with the observed identity still the tree's own blob. The verifiable half of
  a citation is its identity, and it refuses a false success.
- `test_a_citation_moves_no_sealed_revision_byte` — two measurements, because the claim has two
  halves. Equal sealed content committed with and without a citation must digest equally (the preimage
  statement, driven through two independent candidate harnesses that share one authorship envelope and
  one repository id), and every revision row stored before an ingest must be byte-identical after it,
  with exactly the new revision id added. The receipt also names all four rows the cited batch carried,
  and the plain dataset holds no anchor or claim at all.

The private helpers close the module: `_revision_rows` reads every stored revision row keyed by
identity as the database holds it, `_harness_entry` rebuilds one entry with identities two independent
candidate datasets can author, and `_harness_revision_row` returns one candidate's stored revision row,
digests included.

### Conventions

- **The fixtures are the shipped ones and no new governed artifact is registered.** `ReadScopeFixture`
  / `build_read_scope_fixture` build the real dataset and its Git tree, and `CandidateHarness` /
  `build_candidate_harness` / `table_counts` provide the two admitted candidate datasets the digest
  comparison needs. The module registers no artifact of its own.
- **Cases assert observable state through public seams** — `observe_anchor`, `read_knowledge_view`,
  `get_realization_claim`, `find_claim_by_pair` — rather than through helpers internal to the modules
  under test.
- **Every helper that cannot proceed raises `AssertionError` with the refusal attached**, so a broken
  premise fails as loudly as a failed assertion instead of passing quietly on an empty result.
- **Fixed identities live in module constants**, so a case varies a fact rather than a UUID draw; the
  one identity deliberately disagreeing with the tree is named as such at its constant.
- The card records source behaviour. Source inspection is memory preparation: no test run was executed
  in this pass, and the verification stamps above are closeout-owned.

### Invariants And Boundaries

- One entry becomes one admitted batch, and a refused batch never half-commits — which is why the drive
  helper raises on any receipt that is not `changed`.
- A recorded citation is the pair (path, source identity) plus a typed locator, and the read surface
  returns the union member rather than the stored text — for rows this ingest wrote and for rows it
  did not.
- A citation is a *second* record: it adds an anchor and a claim beside the revision and moves no
  sealed content digest and no stored revision row.
- The knowledge lane has no symbol extractor. A symbol locator is carried, stored and observed, and
  the rail's `unsupported_locator` is reported as that answer — never as a file resolution.
- The claim is the recorded edge from the revision to the anchor, and its role and rationale travel
  with it.
- **Boundary.** This module protects the single-entry write path and its read-back. It starts no
  publication, and it does not re-protect the list-level operation, whose refusals, dry-run accounting
  and route leg have their own module.

### Todos

No file-local implementation change is requested by this card. One fact of this pass is recorded
rather than assumed: the module is not registered in `mcp/tests/test-evidence-lanes.toml` at this
commit — it and its list-level sibling are the only two test modules that registry does not carry — so
no lane placement is asserted here and no test run was executed to produce one.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below cite the module's own constructs and the seams it measures, with each anchor resolving
inside the range cited for it. Ranges are the exact construct extents at the verification commit.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixed spellings the cases vary a fact around, bound to the model's own identity and locator types. | `WRONG_RECORDED_BLOB`; `SYMBOL_LOCATOR`; `RANGE_LOCATOR`; `SymbolLocator`; `LineRangeLocator`; `GitBlobIdentity` | mcp/tests/test_knowledge_curator_ingest.py:76-76; mcp/tests/test_knowledge_curator_ingest.py:78-78; mcp/tests/test_knowledge_curator_ingest.py:79-79; mcp/src/agents_remember/models/knowledge/source.py:60-73; mcp/src/agents_remember/models/knowledge/source.py:44-57; mcp/src/agents_remember/models/knowledge/source.py:28-32 |
| One authored entry paired with the citation its assertions name later, beside the real dataset-and-Git-tree fixture. | `Authored`; `fixture` | mcp/tests/test_knowledge_curator_ingest.py:85-89; mcp/tests/test_knowledge_curator_ingest.py:93-96 |
| The drive helpers: admit the fixture's own dataset, resolve the candidate inputs, author one citation, and commit it — raising with the refusal when the batch is not `changed`. | `admitted`; `resolution`; `authored`; `committed` | mcp/tests/test_knowledge_curator_ingest.py:99-108; mcp/tests/test_knowledge_curator_ingest.py:111-120; mcp/tests/test_knowledge_curator_ingest.py:123-155; mcp/tests/test_knowledge_curator_ingest.py:158-163 |
| The read helpers: the stored anchor decoded to the typed union, the mounted source-context view, the single row a claim produced, and the observation handed the decoded locator. | `stored_anchor`; `view_rows`; `row_for`; `observed` | mcp/tests/test_knowledge_curator_ingest.py:166-173; mcp/tests/test_knowledge_curator_ingest.py:176-187; mcp/tests/test_knowledge_curator_ingest.py:190-196; mcp/tests/test_knowledge_curator_ingest.py:199-215 |
| A symbol citation survives the round trip whole, and the lane reports the kind it cannot resolve instead of resolving it as a file. | "test_a_symbol_citation_reads_back_with_its_path_identity_and_locator" | mcp/tests/test_knowledge_curator_ingest.py:218-245 |
| A line-range citation reads back as its recorded extent rather than as an identity. | "test_a_line_range_citation_reads_back_as_its_recorded_extent" | mcp/tests/test_knowledge_curator_ingest.py:248-263 |
| The read surface decodes the locator of a row the ingest did not write — the defect the decode closes. | "test_the_read_surface_decodes_the_locator_of_a_row_the_ingest_did_not_write" | mcp/tests/test_knowledge_curator_ingest.py:266-296 |
| The claim really is the recorded revision-to-anchor edge, with its role and rationale, and the view row names the statement it belongs to. | "test_the_claim_is_the_edge_from_the_revision_to_its_anchor" | mcp/tests/test_knowledge_curator_ingest.py:299-324 |
| The recorded identity is what the observation can verify: the exact blob passes and a false success is refused. | "test_the_recorded_blob_identity_is_what_the_observation_can_verify" | mcp/tests/test_knowledge_curator_ingest.py:327-349 |
| No sealed revision byte moves: equal sealed content digests equally with and without a citation, and every pre-existing revision row is byte-identical after an ingest. | "test_a_citation_moves_no_sealed_revision_byte" | mcp/tests/test_knowledge_curator_ingest.py:352-412 |
| The private readers the two measurements are built from. | `_revision_rows`; `_harness_entry`; `_harness_revision_row` | mcp/tests/test_knowledge_curator_ingest.py:415-425; mcp/tests/test_knowledge_curator_ingest.py:428-436; mcp/tests/test_knowledge_curator_ingest.py:439-451 |
| The committed-command seam the module drives: the citation and entry models, the one-entry commit, the admitted destination and the authorship envelope. | `commit_curator_entry`; `CuratorEntry`; `CuratorCitation`; `admitted_knowledge_destination`; `write_authorship` | mcp/src/agents_remember/application/knowledge_ingest.py:154-161; mcp/src/agents_remember/application/knowledge_ingest.py:83-101; mcp/src/agents_remember/application/knowledge_ingest.py:68-79; mcp/src/agents_remember/application/knowledge.py:140-156; mcp/src/agents_remember/application/knowledge.py:117-137 |
| The read and observation seams the round trip is measured through: the mounted view, the resolved read context, the rail's symbol answer and the two realization readers. | `read_knowledge_view`; `open_read_context`; `observe_anchor`; "unsupported_locator"; `get_realization_claim`; `find_claim_by_pair` | mcp/src/agents_remember/application/knowledge_views.py:86-112; mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/memory/knowledge/read_anchors.py:101-172; mcp/src/agents_remember/memory/knowledge/read_anchors.py:135-135; mcp/src/agents_remember/memory/knowledge/realizations.py:246-254; mcp/src/agents_remember/memory/knowledge/realizations.py:257-268 |
| The shipped support fixtures this module consumes — no new governed artifact. | `ReadScopeFixture`; `build_read_scope_fixture`; `CandidateHarness`; `build_candidate_harness`; `table_counts` | mcp/tests/read_scope_test_support.py:174-239; mcp/tests/read_scope_test_support.py:266-283; mcp/tests/candidate_batch_test_support.py:92-234; mcp/tests/candidate_batch_test_support.py:237-276; mcp/tests/candidate_batch_test_support.py:288-294 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-19T17:14+02:00 — 260915-KS-L28 curator (sealed finding M1-5 repair): created this
  one-to-one card for `mcp/tests/test_knowledge_curator_ingest.py`. It records the single-entry half of
  the reachable curator ingest — the shipped dataset-and-Git-tree fixture and its drive and read
  helpers, and the six cases that pin the symbol and line-range round trip, the reader-side locator
  decode for a row the ingest did not write, the recorded revision-to-anchor claim edge with its role
  and rationale, the blob identity the observation verifies (including the mismatch refusal), and the
  two measurements that show a citation moves no sealed revision byte. Every range is the construct
  extent at the committed revision this card names (`d0c1d1cf`, 2026-09-19T12:15:35+02:00), which is
  byte-identical at the code worktree HEAD `e7998504`; a sibling seat is editing the same file in the
  working tree, so the card is deliberately anchored to the committed revision rather than to that
  uncommitted change set, and closeout owns the final stamps.
