# mcp/tests/test_curator_review_assessment_publication.py

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

## Evidence

### Repo-Internal References

- The integration-lane row this module's classification rests on, and the lane header that declares the classification. [1]
- The integration-lane row this module's classification rests on, and the lane header that declares the classification. [2]
- The shared support module this module is registered as a consumer of. [3]
- The publication wiring the cases drive, including the exact-coverage obligation they leave untouched. [4]
- The destination and read-back the survival and blocked cases measure. [5]
- The typed collection the publish action accepts and the uniqueness rule it enforces. [6]

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

## 260921-ICR-L15 The Closeout Projection Answers "Measured?" The Same Way The Surface Does

`260921-ICR-L15` (`ICR-R15@v1`) moves this module's integration cases onto the measured vocabulary, and
the two defects are asserted against each other rather than one at a time.

**The KS-era case was re-contracted, not annotated.** The case that pinned the old default — an
unmeasured assessment reported `stale` — is now
`test_an_unmeasured_assessment_is_reported_not_measured_not_current`, and it asserts all four facts the
new rule states: the subject `status` is `not-measured`, `notMeasuredCount == 1`, `staleCount == 0`,
and the entry's own `currentness` is `not-measured`. Its second half supplies an **empty** measurement
(`current={}`) and asserts the same `not-measured` with a zero stale count, which is the packet's
non-conforming example measured directly: a mapping's presence decides nothing.

**A new case states what does decide.** `test_only_a_complete_measured_match_reports_the_stored_assessment_current`
drives the real publication, takes the stored record's own declared identities as the measurement, and
asserts `current` on both the subject status and the entry — so the two halves of the rule (nothing
measured ⇒ `not-measured`; everything measured and agreeing ⇒ `current`) are pinned through the same
closeout entry point the rest of the integration suite uses.

The module grew 948 → 988 lines. Nothing else in it changed: the same fixture, the same published
assessment, and the same `curator_coherence_subject_assessment_state` projection under test.
