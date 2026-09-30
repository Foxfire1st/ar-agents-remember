# mcp/tests/test_curator_review_assessment_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_review_assessment_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:44:12+02:00 |
| lastVerifiedCommitHash | `31d761a241055d67b85ef3908033856b78a86a57` |
| lastVerifiedCommitDate | 2026-09-30T05:10:40+02:00|
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
| The integration-lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_curator_review_assessment_publication.py"; "integration = [" | mcp/tests/test-evidence-lanes.toml:356-356; mcp/tests/test-evidence-lanes.toml:279-279 |
| The integration-lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_curator_review_assessment_publication.py"; "integration = [" | mcp/tests/test-evidence-lanes.toml:356-356; mcp/tests/test-evidence-lanes.toml:279-279 |
|The shared support module this module is registered as a consumer of.|"mcp/tests/test_curator_review_assessment_publication.py"| mcp/tests/test-evidence-lanes.toml:329-329; mcp/tests/evidence-lifecycle.toml:360-360; mcp/tests/evidence-lifecycle.toml:403-410; mcp/tests/evidence-lifecycle.toml:414-420 |
| The publication wiring the cases drive, including the exact-coverage obligation they leave untouched. | `curator_coherence_action`; `_exact_review_assessments`; `_record` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:93-103; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:259-313; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:363-464 |
| The destination and read-back the survival and blocked cases measure. | `publish_assessment_evidence_bytes`; `read_back_published_bytes`; `AssessmentEvidenceBlockedError` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:66-96; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:154-194; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:197-219 |
| The typed collection the publish action accepts and the uniqueness rule it enforces. | `CuratorCoherenceRecord`; `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:226-307; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:449-529 |

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
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; rows citing lane rows after the one `unit-regression` row MIK-R10 inserted at `test-evidence-lanes.toml:124` (or catalog lines after `evidence-lifecycle.toml:836`) were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No claim was reworded, so the fixer's bullets are kept. No verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact: this card's source is unchanged. Rows citing lines that MIK-R25 moved in `test-evidence-lanes.toml` were re-pointed, by the installed fixer (its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; each such row was byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R13 inserted one `unit-regression` row at `test-evidence-lanes.toml:121`, so citation ranges into later lane rows were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (+1 at or after `:121`; each such row was byte-identical to memory HEAD).
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R01 moved lines in `test-evidence-lanes.toml`, so citation ranges into it were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (each such row was byte-identical to memory HEAD).
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; L06 inserted one `unit-regression` row at `test-evidence-lanes.toml:69`, so its citations to later lane rows moved down one line. The multi-anchor lane rows the fixer declined were re-pointed by that exact +1 shift, and each was checked to hold its anchors in the shifted ranges; any other moved row was re-pointed by the installed fixer, which records its own bullet. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 added one row at `:112` of `test-evidence-lanes.toml`, moving every later row down one line, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): No content impact: this card's source is unchanged; its citations into `mcp/tests/test-evidence-lanes.toml` moved by this leaf's two-line `unit-regression` insertion at `:107-108` and were re-pointed (by the installed anchor-range projection where it could, otherwise by exact base-to-working line mapping). Each re-pointed row cites the same lane line it cited at base; no claim wording changed and no verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 inserts two `unit-regression` rows at `mcp/tests/test-evidence-lanes.toml:102-103`, which moves every later lane row down by two lines; this card's lane-row citations were re-pointed by that exact shift (by base-to-working line mapping where the installed fixer declined a multi-anchor row), their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): No content impact: MIK-R07 inserts one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:98`, so this card's rows citing lane lines below it were re-pointed one line down (by the installed anchor-range projection or, where it declined a multi-anchor row, by an exact one-line shift confirmed by every anchor resolving in the current file). Claim wording unchanged. No stamp advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: multi-anchor rows re-measured against their cited files after MIK-R21's two-line insertion into `test-evidence-lanes.toml`; each anchor now cites the one line that holds it. Claim meaning unchanged; no stamp advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 5 citations into `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 3 citations into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 5 citations into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`models/knowledge/read.py` lost the moved anchor vocabulary; the evidence TOMLs gained one row) were re-measured against the candidate by the curator so each anchor lands on its construct again; no claim wording changed.

- 2026-09-28T16:25:39+02:00 — 260921-ICR-L42 curator: No content impact: re-pointed this card's citations into `test-evidence-lanes.toml` after this leaf's line insertions (candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`). Each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.

- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 3 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
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

## Update History
- 2026-09-23T13:10:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58`, so the honest basis for every claim here is that commit plus the working-tree delta): **the integration cases move onto the measured vocabulary (948 → 988 lines).** The KS-era `…_is_reported_stale_not_current` case was re-contracted into `…_is_reported_not_measured_not_current` (asserting `not-measured`, `notMeasuredCount == 1`, `staleCount == 0`, and an empty measurement answering the same), and `test_only_a_complete_measured_match_reports_the_stored_assessment_current` was added. Recorded in the body rather than as a history-only note because the memory-refresh check requires the sidecar body itself to reflect a changed source. No claim, anchor or citation range changed here, and **no verification stamp was advanced**: the candidate is uncommitted, the header's stamp values are untouched, and the governed closeout owns the real stamp.
