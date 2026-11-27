# mcp/tests/test_curator_review_assessment_publication.py

## Governing Overview

[tests overview](overview.md)

## Purpose

**The integration population for `KS-R15@v1`'s publication route, the evidence-byte destination and
the read-back.** The suite uses a real external-memory leaf enclosure built by the shared lifecycle
fixture. It combines production publication/read-back cases, direct evidence-byte helper checks,
and request/record-model validation. A model refusal is evidence about the model's accepted shape;
an application refusal code is asserted only by the cases that call `curator_coherence_tool`.
Nothing here re-implements the publication path or fakes a contract. Since `260915-KS-L23`
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
- the attestation the record commits to is readable **after** the enclosure's `reports` directory is removed,
  by the copy path the record itself carries;
- the shipped exact-coverage obligation `_judgments_cover_candidates_exactly` is untouched by a record
  that carries assessments.

## Code Commentary

### Logic

**Five** test classes contain **23** test definitions at code tree `96bf7343`, by complete AST inspection, without pytest collection or execution. The three-class, 18-case and 22-case accounts later in this card belong to their named earlier leaves:

- `TestPublishedAssessment` — an assessment publishes to the canonical authority and reads back; the
  stored author is whatever the publication path supplied; cited evidence bytes are read back by their
  recorded path and digest, and their size is checked against the fixture content; the recorded bytes survive removal of the
  enclosure `reports` directory; publishing an assessment does not disturb the exact-coverage
  obligation; a leaf with no assessment publishes and reports `none-recorded`.
- `TestReadStatesOverAStoredCollection` — a measured move marks the stored assessment stale and keeps
  it readable; `unresolved` is reported as its own state rather than as a clearance. Missing, empty or incomplete measurements report `not-measured`; a complete matching measurement reports `current`.
- `TestAssessmentRefusals` — the author-supplying case constructs `CuratorCoherenceRequest` and
  asserts `ValidationError` containing `authorRef`; it does not call the application publication
  boundary or assert a returned refusal code. Separate `_tool_publish` cases assert application
  refusal codes and byte-identical canonical authority. Direct evidence-byte helper cases check
  invalid destinations, digest mismatch, published copies and post-publication absence. The case `test_a_citation_naming_a_worktree_file_is_published_to_the_surviving_tree` belongs to this class: it publishes a `code:feature.txt` citation into the surviving task tree and requires the published text to equal the fixture’s `cited bytes\n`.
- `TestPublisherCallerAddress` (class `:784-855`, case bodies `:795-855`) — item 19's two cases. A **bare** leaf-document file name
  that names the addressed document publishes, and the stored record's `taskDocumentRef.path` and
  `publishedBy` carry the canonical `<task-dir>/<leaf>.json` rather than the caller's spelling. A bare
  name for a **different** document is refused through the application boundary
  (`curator_coherence_tool`), and the case asserts `curator-coherence-caller-refused`, the demanded
  shape `<task-slug>/<leaf-document-file>` **and** this contract's exact canonical path in the detail,
  plus the `expected`/`observed` refs. Red if resolution is removed, if the refusal names nothing
  again, or if a bare name for another document starts being accepted.
- `TestAttestationDurability` (class `:910-963`, case bodies `:919-963`) — item 18's second half. The bound attestation is copied
  into the surviving task tree; the case then removes the enclosure's `reports` directory — the thing
  finalize reclaims — and reopens the copy **by the path the record carries**, re-verifying its digest
  and asserting the recorded source-candidate list equals the attestation's own. The second case pins
  that a re-publication over unchanged bytes reuses the same content-addressed copy rather than
  rewriting an immutable one. Red if the copy is not written, not recorded, not the bound bytes, or if
  the enclosure path is the only one that works.

The module-level helper `_tool_publish_bare_name` (`:858-892`) drives the refusal case through the
application boundary rather than the domain function, so the asserted code is the code a caller
receives.

The module also writes the canonical leaf document and its passing route review in a `_leaf_document`
fixture, because the coherence route resolves the terminal leaf document and a contract alone is not
enough. There is no `test_`-prefixed re-implementation of anything: the fixture builds real state for
the production path to drive.

### Conventions

- The cases stand up real repositories and an external-memory enclosure.
- The current lifecycle catalog has **18 contracts and 122 artifacts**. The earlier 13/54 consumer-addition account describes the creating leaf's source epoch.
- `_tool_publish` and `_tool_publish_bare_name` reach the **application** boundary
  (`curator_coherence_tool`) for returned refusal-code assertions. The author-field case instead
  checks request-model `ValidationError`; direct evidence-byte cases inspect
  `AssessmentEvidenceBlockedError` from the domain helpers. These assertion classes are distinct.

### Invariants And Boundaries

- **Survival is read back, never asserted.** The post-cleanup case removes the enclosure `reports`
  directory, asserts it is gone, and only then opens the recorded bytes.
- **The record's own digest is not the bytes' read-back.** Each byte is opened by the path recorded on
  the assessment and compared to the digest recorded beside it.
- **Application publication refusals leave the authority byte-identical.** The no-evidence,
  duplicate-identity and unresolved-citation cases compare the canonical file before and after
  `_tool_publish`; the author-field and evidence-byte helper refusals assert their own model/domain
  errors instead of that publication read-back.
- **Exact coverage is a preservation boundary.** The case asserts the shipped obligation still refuses
  a mismatched judgment set on a record that carries assessments.

## Evidence

Superseded card wording retained for custody (not certified as true of any source epoch or measured candidate):

> `TestPublisherCallerAddress` (`:759-836`)

> `TestAttestationDurability` (`:881-932`)

> `_tool_publish_bare_name` (`:839-878`)

### Repo-Internal References

> Retained earlier citation wording: - The integration-lane row this module's classification rests on, and the lane header that declares the classification. Source caption: "mcp/tests/test_curator_review_assessment_publication.py"; "integration = ["

> Retained earlier citation wording: - The integration-lane row this module's classification rests on, and the lane header that declares the classification. Source caption: "mcp/tests/test_curator_review_assessment_publication.py"; "integration = ["

> Retained earlier citation wording: - The lifecycle catalog declares this suite as an exact consumer of curator_coherence_test_support.py and the Node package-lock fixture. Declaration is not invocation.

### Repo-Internal References (renewed)

- The destination/read-back helpers and the TestAssessmentRefusals worktree-citation case keep the cited bytes in the surviving task tree. [5]

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

At that `260921-ICR-L15` source epoch, the recorded account was: the module grew 948 → 988 lines. Nothing else in it changed: the same fixture, the same published
assessment, and the same `curator_coherence_subject_assessment_state` projection under test.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:1951-1951 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The `integration` lane selects `mcp/tests/test_curator_review_assessment_publication.py`. [1] [2]









- The lifecycle catalog lists this module as an exact consumer of `mcp/tests/_user_settings_guard.py`.
- The publication wiring the cases drive, including the exact-coverage obligation they leave untouched. [4]
- The record's `assessments` collection that the publish action accepts holds each assessment identity once, a rule kept separate from judgment-to-candidate coverage. [6]



- The lifecycle catalog lists `mcp/tests/test_curator_review_assessment_publication.py` among the exact consumers of `mcp/tests/curator_coherence_test_support.py`, `mcp/tests/fixtures/repository_profiles/node/package-lock.json`. These source declarations establish no execution or passing result. [8]
