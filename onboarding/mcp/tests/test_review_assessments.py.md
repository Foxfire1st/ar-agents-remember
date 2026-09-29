# mcp/tests/test_review_assessments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_assessments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `7127756cd132d1103cd0a24bc7dc6884ddb663ee` |
| lastVerifiedCommitDate | 2026-09-30T01:41:06+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

**The unit population for `KS-R15@v1`'s `ReviewAssessment` record, its binding, and the states a read
reports.** These cases protect the record's *decidable* content: which fields a stored assessment must
carry, that its three dispositions are not interchangeable, that its binding is compared for equality
rather than reinterpreted, that absence is never rendered as a favourable disposition, and that the
`knowledgeReview` checklist section is a factual, report-only section of the one artifact.

Nothing here fakes a contract or a store, and no case claims a survival it did not read back. The
publication route's real behaviour — the authenticated caller, the evidence-byte destination and the
post-cleanup read-back — is exercised against a real external-memory leaf enclosure in
`mcp/tests/test_curator_review_assessment_publication.py`; this module is the hermetic half.

## Code Commentary

### Logic

Seven test classes, each owning one property rather than one function:

- `TestAssessmentRecordShape` — a record missing its examined inputs or its provenance does not
  construct; the submission shape has no field for a caller-supplied author; an undeclared field is
  refused; the record is validated structurally and never for truth.
- `TestDispositionVocabulary` — the vocabulary is exactly the three declared values; `unresolved` is
  not a synonym for `no_concern_found`; `no_concern_found` may not carry a finding; an unknown
  disposition is refused.
- `TestSubjectShape` — a family subject names the family's own record and its revisions; the revision
  lists are required for a revision-bearing kind and refused for `comparison`.
- `TestExaminedInputBinding` — the binding uses the shipped contract's two own vocabularies; the policy
  requires exactly the clause-five inputs; a relocated input with identical content is **not**
  equivalent; an input that can no longer be read is a mismatch rather than a pass; a moved input
  marks the binding stale with its exact identity; per-item coverage is not inherited from a sibling.
- `TestEvidenceBytesAreRecordedAsThreeFacts` — each cited byte is recorded with path, digest and size.
- `TestReadStates` — the three recorded states plus `none-recorded` are reported distinctly; a
  projection cannot report a disposition for an absent subject; a count that contradicts its records
  is refused.
- `TestKnowledgeReviewSection` — the section moves no count and adds no finding; it is written into the
  one checklist artifact; an unresolved signal is reported as its own state rather than a clearance.

`_Binding` at the top is the module's own small builder for a well-formed assessment, so each case
varies exactly the field it is about instead of restating the whole record; `_Published` at the bottom
serves the cases that need a stored projection.

### Conventions

- Registered in `mcp/tests/test-evidence-lanes.toml` as a **unit-regression** member: every case is
  hermetic (temporary directories, in-process state, no integration marker, no repository or
  subprocess), so the default unit lane is each one's behaviour-preserving classification.
- Each case names a distinct failure in the leaf's clause envelope; none is a variant of another, and
  no case asserts the *absence* of an operation, which would be a source census rather than a
  behavioural check.

### Invariants And Boundaries

- **No case here claims a survival it did not read back** — that property belongs to the integration
  module, which drives the real publication path.
- **No fake contract and no fake store.** The module builds records and projections in process; it
  never stands up an enclosure.
- **Structural claims only.** A case asserts that a shape is refused or that a state is reported; no
  case asserts that a finding is true.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_review_assessments.py"; "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:259-259; mcp/tests/test-evidence-lanes.toml:5-5 |
| The record, its submission shape and the validator the shape cases drive. | `ReviewAssessment`; `ReviewAssessmentRevision`; `_AuthoredAssessmentFields` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:292-354; mcp/src/agents_remember/models/lifecycles/review_assessment.py:357-371; mcp/src/agents_remember/models/lifecycles/review_assessment.py:374-395; mcp/src/agents_remember/models/lifecycles/review_assessment.py:326-341 |
| The equality comparison and the stale-marking the binding cases drive. | `disputed_dependencies`; `AssessmentCurrentness`; `require_current_assessment_binding` | mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:92-107; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:125-140; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:143-172; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:195-220 |
| The state projection the read cases drive. | `assessment_state_for`; `SubjectAssessmentState` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:453-539; mcp/src/agents_remember/models/lifecycles/review_assessment.py:542-594 |
| The report-only section the checklist cases assert. | `knowledge_review_section` | mcp/src/agents_remember/memory_quality/knowledge_review.py:76-142 |

## KS-R15@v1 Unit Protection

**The leaf that created this module.** `KS-R15@v1` §1–§5 and §8.2 are the clauses these 47 cases
carry. The leaf's case-budget measurement records this module alone as `47 tests collected`, and the
combined population delta as `+47 unit` against the base `e963a01c`.

Two clauses are deliberately **not** carried by a case here, and the leaf recorded why rather than
leaving the gap silent: §3.2's "a citation keeps both types" is a structural property (there is no
function taking a signal and returning an assessment), and asserting the absence of an operation
would be a source census rather than a behavioural check; and §6.9's scope refusal is the shipped,
unmodified `_require_leaf_external_memory`, so a case would assert a rail this leaf did not touch.

## Update History
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; L06 inserted one `unit-regression` row at `test-evidence-lanes.toml:69`, so its citations to later lane rows moved down one line. The multi-anchor lane rows the fixer declined were re-pointed by that exact +1 shift, and each was checked to hold its anchors in the shifted ranges; any other moved row was re-pointed by the installed fixer, which records its own bullet. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 added one row at `:112` of `test-evidence-lanes.toml`, moving every later row down one line, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): No content impact: this card's source is unchanged; its citations into `mcp/tests/test-evidence-lanes.toml` moved by this leaf's two-line `unit-regression` insertion at `:107-108` and were re-pointed (by the installed anchor-range projection where it could, otherwise by exact base-to-working line mapping). Each re-pointed row cites the same lane line it cited at base; no claim wording changed and no verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 inserts two `unit-regression` rows at `mcp/tests/test-evidence-lanes.toml:102-103`, which moves every later lane row down by two lines; this card's lane-row citations were re-pointed by that exact shift (by base-to-working line mapping where the installed fixer declined a multi-anchor row), their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): No content impact: MIK-R07 inserts one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:98`, so this card's rows citing lane lines below it were re-pointed one line down (by the installed anchor-range projection or, where it declined a multi-anchor row, by an exact one-line shift confirmed by every anchor resolving in the current file). Claim wording unchanged. No stamp advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the lane-row citation re-measured after MIK-R21's two-line insertion into `test-evidence-lanes.toml`. Claim meaning unchanged; no stamp advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 1 citation into `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`models/knowledge/read.py` lost the moved anchor vocabulary; the evidence TOMLs gained one row) were re-measured against the candidate by the curator so each anchor lands on its construct again; no claim wording changed.

- 2026-09-28T16:25:39+02:00 — 260921-ICR-L42 curator: No content impact: re-pointed this card's citations into `test-evidence-lanes.toml` after this leaf's line insertions (candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`). Each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.

- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 1 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58`, so the honest basis for every claim below is that commit plus the working-tree delta): **citation repair only, forced by this leaf's own changes to the sources this card cites.** One row was re-pointed: the state-projection row's `assessment_state_for` range `mcp/src/agents_remember/models/lifecycles/review_assessment.py:416-439` → `:542-594`, the function's own extent on this candidate; the sibling `SubjectAssessmentState` range `:441-501` still holds its declaration and was left as it stands. The claim-reopen this anchor also carried is cleared by that one edit — a cited range now contains the declaration line — and not by any wording change. No Finding, anchor or claim was re-worded, no range was deleted and none was appended, and **no verification stamp was advanced**: the candidate is uncommitted, so `lastVerifiedCommitHash`/`lastVerifiedCommitDate` keep the values they hold and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **sync-merge resolution of the parked candidate against the landed ICR-L7 curation (1 region).** Additive union: the module's lane row re-derived to the merged tree (`:204`) with the `unit-regression = [` key (`:5`). Both sides' history preserved. No verification stamp was advanced.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by the lane row this leaf inserted.** This file is not a changed source file. Its one lane-registration row cited `mcp/tests/test-evidence-lanes.toml:197`, one line above the line that carries `"mcp/tests/test_review_assessments.py"` on this candidate; the row was re-read and the range re-derived to `:200`, and its other ranges were read back as still correct. No claim wording or anchor was changed, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; this leaf appended one row to `mcp/tests/test-evidence-lanes.toml` at `:89` and two consumer rows to `mcp/tests/evidence-lifecycle.toml` at `:733` and `:1271`, so every lane row below `:88` shifted by one and every evidence-catalog line below those rows by one and two respectively. Each affected row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file — and, where a row's anchor is a lane or consumer entry, from the line that actually carries it — rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **citation repair only.** `260921-ICR-L1` inserted one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:105`, so every row and lane key below it moved one line lower; this card's claim rows that cite that manifest were re-derived under that mapping from the anchor's real position (the ranges are shifted exactly where they cross `:105`, and left alone where they do not). No claim was re-worded, no row was deleted, and the generated history entries in this card keep the ranges they were written with. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_review_assessments.py.md:82` (mcp/tests/test_review_assessments.py) — re-read the row against the merged registry: the anchor is at the line named in the checker's own message, and the cited range was widened to the line that carries it.

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the leaf's unit module — the seven properties it protects, its
  hermetic classification and lane registration, and the two clauses the leaf recorded as
  structural-or-shipped rather than case-carried. Verification metadata remains closeout-owned; no
  acceptance or certification claim is made.
