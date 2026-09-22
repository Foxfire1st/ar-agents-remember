# mcp/tests/test_curator_review_assessment_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_review_assessment_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T11:39:00+02:00 |
| lastVerifiedCommitHash | `2edad477bcd9127a90e4618d345ce34ef7e6a6d9` |
| lastVerifiedCommitDate | 2026-09-23T00:33:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

**The integration population for `KS-R15@v1`'s publication route, the evidence-byte destination and
the read-back.** Every case drives the **production** curator-coherence publication against a real
external-memory leaf enclosure built by the shared lifecycle fixture. Nothing here re-implements the
publication path, fakes a contract, or asserts a survival it did not read back. Since `260915-KS-L23`
it is also the integration population for the route's **caller address** (item 19) and for the
durability of the attestation a publication binds (item 18's second half).

The load-bearing properties:

- the `knowledgeReview` surface's source — the record's own assessment collection — is written through
  the `curator_coherence` `publish` action and read back from the canonical authority on disk;
- each cited evidence byte is opened **by the task-root-relative path recorded on the assessment** and
  verified against its recorded digest, which is the read-back the requirement asks for and the
  record's own digest cannot substitute for;
- the survival read-back still resolves after the enclosure's `reports` directory — the one directory
  terminal cleanup removes for a leaf contract — is gone;
- the caller's document reference is resolved to the canonical identity the record and an assessment's
  author carry, or refused with the shape **and** the exact value this contract expects;
- the attestation the record commits to is readable **after** the enclosure it was observed in is gone,
  by the path the record itself carries;
- the shipped exact-coverage obligation `_judgments_cover_candidates_exactly` is untouched by a record
  that carries assessments.

## Code Commentary

### Logic

**Five** test classes — this card said three until `260915-KS-L23` added the last two:

- `TestPublishedAssessment` — an assessment publishes to the canonical authority and reads back; the
  stored author is whatever the publication path supplied; each cited evidence byte is recorded with
  path, digest and size; the published copy is the cited bytes by content; a citation naming a
  worktree file is published to the surviving tree; the recorded bytes survive removal of the
  enclosure `reports` directory; publishing an assessment does not disturb the exact-coverage
  obligation; a leaf with no assessment publishes and reports `none-recorded`.
- `TestReadStatesOverAStoredCollection` — a measured move marks the stored assessment stale and keeps
  it readable; `unresolved` is reported as its own state rather than as a clearance.
- `TestAssessmentRefusals` — a submission supplying an author is refused as an undeclared field
  **through the application boundary**, so the code asserted is the code a caller receives; a byte
  that does not read back blocks with the destination and the digest; a published byte removed after
  publication is a blocked absent state; a refused submission leaves the canonical authority
  byte-identical.
- `TestPublisherCallerAddress` (`:759-836`) — item 19's two cases. A **bare** leaf-document file name
  that names the addressed document publishes, and the stored record's `taskDocumentRef.path` and
  `publishedBy` carry the canonical `<task-dir>/<leaf>.json` rather than the caller's spelling. A bare
  name for a **different** document is refused through the application boundary
  (`curator_coherence_tool`), and the case asserts `curator-coherence-caller-refused`, the demanded
  shape `<task-slug>/<leaf-document-file>` **and** this contract's exact canonical path in the detail,
  plus the `expected`/`observed` refs. Red if resolution is removed, if the refusal names nothing
  again, or if a bare name for another document starts being accepted.
- `TestAttestationDurability` (`:881-932`) — item 18's second half. The bound attestation is copied
  into the surviving task tree; the case then removes the enclosure's `reports` directory — the thing
  finalize reclaims — and reopens the copy **by the path the record carries**, re-verifying its digest
  and asserting the recorded source-candidate list equals the attestation's own. The second case pins
  that a re-publication over unchanged bytes reuses the same content-addressed copy rather than
  rewriting an immutable one. Red if the copy is not written, not recorded, not the bound bytes, or if
  the enclosure path is the only one that works.

The module-level helper `_tool_publish_bare_name` (`:839-878`) drives the refusal case through the
application boundary rather than the domain function, so the asserted code is the code a caller
receives.

The module also writes the canonical leaf document and its passing route review in a `_leaf_document`
fixture, because the coherence route resolves the terminal leaf document and a contract alone is not
enough. There is no `test_`-prefixed re-implementation of anything: the fixture builds real state for
the production path to drive.

### Conventions

- Registered in `mcp/tests/test-evidence-lanes.toml` as an **integration** member: it stands up real
  repositories and an external-memory enclosure, which is the population that measures that behaviour.
- Registered in `mcp/tests/evidence-lifecycle.toml` as a **consumer** of the shared support module
  `mcp/tests/curator_coherence_test_support.py` (owner `curator-coherence-test-port`) and of
  `mcp/tests/test_worktree_support.py`. This leaf added a consumer row; it did not add a contract or
  an artifact, so the catalogue's counts stay at 13 contracts / 54 artifacts while its digest moves.
- Refusal assertions are routed through the **application** boundary (`curator_coherence_tool`) rather
  than the domain function, so claimed codes are the codes a caller receives.

### Invariants And Boundaries

- **Survival is read back, never asserted.** The post-cleanup case removes the enclosure `reports`
  directory, asserts it is gone, and only then opens the recorded bytes.
- **The record's own digest is not the bytes' read-back.** Each byte is opened by the path recorded on
  the assessment and compared to the digest recorded beside it.
- **A refused publication leaves the authority byte-identical.** The refusal cases measure the
  canonical file rather than only the raised error.
- **Exact coverage is a preservation boundary.** The case asserts the shipped obligation still refuses
  a mismatched judgment set on a record that carries assessments.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The integration-lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_curator_review_assessment_publication.py"; "integration = [" | mcp/tests/test-evidence-lanes.toml:297-297; mcp/tests/test-evidence-lanes.toml:223-223; mcp/tests/test-evidence-lanes.toml:296-296; mcp/tests/test-evidence-lanes.toml:222-222 |
| The integration-lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_curator_review_assessment_publication.py"; "integration = [" | mcp/tests/test-evidence-lanes.toml:297-297; mcp/tests/test-evidence-lanes.toml:223-223; mcp/tests/test-evidence-lanes.toml:296-296; mcp/tests/test-evidence-lanes.toml:222-222 |
|The shared support module this module is registered as a consumer of.|"mcp/tests/test_curator_review_assessment_publication.py"| mcp/tests/evidence-lifecycle.toml:360-360; mcp/tests/test-evidence-lanes.toml:294; mcp/tests/evidence-lifecycle.toml:403-410; mcp/tests/evidence-lifecycle.toml:414-420 |
| The publication wiring the cases drive, including the exact-coverage obligation they leave untouched. | `curator_coherence_action`; `_exact_review_assessments`; `_record` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:88-98; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:248-302; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:352-451 |
| The destination and read-back the survival and blocked cases measure. | `publish_assessment_evidence_bytes`; `read_back_published_bytes`; `AssessmentEvidenceBlockedError` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:64-96; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:152-193; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:195-240 |
| The typed collection the publish action accepts and the uniqueness rule it enforces. | `CuratorCoherenceRecord`; `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:190-234; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:370-434 |

## KS-R15@v1 Integration Protection

**The leaf that created this module.** `KS-R15@v1` §6, §7 and §10.4 are the clauses the 18 cases that
leaf created carry. The leaf's case-budget measurement records this module alone as `18 tests
collected`, and the combined population delta as `+18 integration` against the base `e963a01c`; both the
unit and the integration ceilings stay under their declared budgets, so this leaf raised neither.

**Measured from the source at `260915-KS-L23`:** the module now defines **22** test cases in **5**
classes. The four that leaf added — two caller-address cases in `TestPublisherCallerAddress`, two
attestation-durability cases in `TestAttestationDurability` — are described under `### Logic`; the
`18`/`+18` figures above remain the `KS-R15@v1` leaf's own measurement and are not restated as the
current population.

The governed-inventory consequence, recorded here because a reader of this card is the person most
likely to ask: the module is ordinary `test_`-prefixed test source, so no artifact is promoted and no
new shared support module was written. The evidence-lifecycle catalogue's identity moved only because
a **consumer list** changed, and the catalogue guard validates that change in both directions.

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **sync-merge resolution of the parked candidate against the landed ICR-L7 curation (1 region).** Additive union: the module's integration row re-derived to the merged tree (`:292`) with the `integration = [` key (`:218`); the consumer row keeps its evidence-lifecycle ranges with the lanes row at `:292`. Both sides' history preserved. No verification stamp was advanced.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by the lane row this leaf inserted.** This file is not a changed source file. Its one lane-registration row cited a cluster of ranges that no longer held either anchor; it was re-read and re-cited to the lines this candidate actually carries — the module's own integration row at `:288` and the `integration = [` key that declares the classification at `:214`. No claim wording or anchor was changed, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; this leaf appended one row to `mcp/tests/test-evidence-lanes.toml` at `:89` and two consumer rows to `mcp/tests/evidence-lifecycle.toml` at `:733` and `:1271`, so every lane row below `:88` shifted by one and every evidence-catalog line below those rows by one and two respectively. Each affected row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file — and, where a row's anchor is a lane or consumer entry, from the line that actually carries it — rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **citation repair only.** `260921-ICR-L1` inserted one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:105`, so every row and lane key below it moved one line lower; this card's claim rows that cite that manifest were re-derived under that mapping from the anchor's real position (the ranges are shifted exactly where they cross `:105`, and left alone where they do not). No claim was re-worded, no row was deleted, and the generated history entries in this card keep the ranges they were written with. No verification stamp was advanced.
- 2026-09-20T01:20+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_curator_review_assessment_publication.py.md:114` ("mcp/tests/test_curator_review_assessment_publication.py") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_curator_review_assessment_publication.py.md:113` (mcp/tests/test_curator_review_assessment_publication.py) — re-read the row against the merged registry: the anchor is at the line named in the checker's own message, and the cited range was widened to the line that carries it.

- 2026-09-18T19:54:49+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The integration-lane row cited `test-evidence-lanes.toml:238-238`, another module's lane entry, for this module's own path literal, whose live occurrence is the `273` entry; that cell now cites `273-273`. Its last range `196-196` (the previous lane's closing `]`) was widened to `196-201` so the `integration = [` lane key the claim names is inside a cited range. (b) The consumer row cited `evidence-lifecycle.toml:414-414` (the entry above this module's) for the same path; the range was widened to `414-415`, which is where the consumer list declares it. Claims, anchors and all other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T19:27+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **this card described a module that no longer matches its source: it said "Three test classes" and "these 18 cases", and the leaf added two classes and four cases.** `TestPublisherCallerAddress` (`:759-836`) carries item 19 — a bare leaf-document name that names the addressed document resolves and the record/`publishedBy` carry the canonical path, while a bare name for another document is refused through the application boundary with the demanded shape and this contract's exact value; `TestAttestationDurability` (`:881-932`) carries item 18's second half — the bound attestation is copied into the surviving tree and reads back by the path the record carries after the enclosure `reports` directory is removed, and a republish reuses the immutable copy. The module-level `_tool_publish_bare_name` (`:839-878`) is the boundary driver. The `### Logic` class list, the Purpose's load-bearing properties and the `KS-R15@v1` section were corrected to five classes / 22 source-defined cases (counted from the file, not collected — no test run is claimed), with the R15 leaf's `18`/`+18` measurement retained as that leaf's own. The stale recorded working candidate (`ar/260915-ks-l15`) now names this leaf's candidate. Read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced; the reference rows are left to the citation-range repair pass that owns them.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the leaf's integration module — the four load-bearing properties
  it measures against a real external-memory enclosure, its integration lane and shared-support
  consumer registrations, and the boundary that survival is read back after cleanup rather than
  asserted. Verification metadata remains closeout-owned; no acceptance or certification claim is
  made.
