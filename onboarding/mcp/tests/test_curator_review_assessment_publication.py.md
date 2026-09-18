# mcp/tests/test_curator_review_assessment_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_review_assessment_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:27+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
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
| The integration-lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_curator_review_assessment_publication.py"; "integration = [" | mcp/tests/test-evidence-lanes.toml:166-168; mcp/tests/test-evidence-lanes.toml:236-238; mcp/tests/test-evidence-lanes.toml:273-273; mcp/tests/test-evidence-lanes.toml:255-262; mcp/tests/test-evidence-lanes.toml:183-190; mcp/tests/test-evidence-lanes.toml:264-264; mcp/tests/test-evidence-lanes.toml:192-192; mcp/tests/test-evidence-lanes.toml:194-194; mcp/tests/test-evidence-lanes.toml:266-266; mcp/tests/test-evidence-lanes.toml:267-267; mcp/tests/test-evidence-lanes.toml:195-195; mcp/tests/test-evidence-lanes.toml:268-268; mcp/tests/test-evidence-lanes.toml:196-201 |
|The shared support module this module is registered as a consumer of.|"mcp/tests/test_curator_review_assessment_publication.py"| mcp/tests/evidence-lifecycle.toml:360-360; mcp/tests/test-evidence-lanes.toml:240-240; mcp/tests/evidence-lifecycle.toml:403-410; mcp/tests/evidence-lifecycle.toml:414-415 |
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

- 2026-09-18T19:54:49+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The integration-lane row cited `test-evidence-lanes.toml:238-238`, another module's lane entry, for this module's own path literal, whose live occurrence is the `273` entry; that cell now cites `273-273`. Its last range `196-196` (the previous lane's closing `]`) was widened to `196-201` so the `integration = [` lane key the claim names is inside a cited range. (b) The consumer row cited `evidence-lifecycle.toml:414-414` (the entry above this module's) for the same path; the range was widened to `414-415`, which is where the consumer list declares it. Claims, anchors and all other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T19:27+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **this card described a module that no longer matches its source: it said "Three test classes" and "these 18 cases", and the leaf added two classes and four cases.** `TestPublisherCallerAddress` (`:759-836`) carries item 19 — a bare leaf-document name that names the addressed document resolves and the record/`publishedBy` carry the canonical path, while a bare name for another document is refused through the application boundary with the demanded shape and this contract's exact value; `TestAttestationDurability` (`:881-932`) carries item 18's second half — the bound attestation is copied into the surviving tree and reads back by the path the record carries after the enclosure `reports` directory is removed, and a republish reuses the immutable copy. The module-level `_tool_publish_bare_name` (`:839-878`) is the boundary driver. The `### Logic` class list, the Purpose's load-bearing properties and the `KS-R15@v1` section were corrected to five classes / 22 source-defined cases (counted from the file, not collected — no test run is claimed), with the R15 leaf's `18`/`+18` measurement retained as that leaf's own. The stale `reviewedWorkingCandidate` row (`ar/260915-ks-l15`) now names this leaf's candidate. Read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced; the reference rows are left to the citation-range repair pass that owns them.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the leaf's integration module — the four load-bearing properties
  it measures against a real external-memory enclosure, its integration lane and shared-support
  consumer registrations, and the boundary that survival is read back after cleanup rather than
  asserted. Verification metadata remains closeout-owned; no acceptance or certification claim is
  made.
