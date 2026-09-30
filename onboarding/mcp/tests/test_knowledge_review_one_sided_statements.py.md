# mcp/tests/test_knowledge_review_one_sided_statements.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_one_sided_statements.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T05:58:11+02:00 |
| lastVerifiedCommitHash | `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c` |
| lastVerifiedCommitDate | 2026-09-30T06:21:14+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition half** of ICR-R06@v1, in six cases. They drive the real
`compose_review` over **two real datasets**, each built through the public store operations by
`read_scope_test_support.build_read_scope_fixture` and then extended with one authored invariant
apiece. Nothing here substitutes a payload, edits a stored row or deletes a record to manufacture a
case: the after snapshot simply holds an invariant the before snapshot does not, and the before
snapshot holds one the after snapshot does not. Those two snapshots are what an addition and a
removal **are**, and the reviewed subject is selected from each side in turn.

The renderer half of the same requirement is `dashboard/src/panels/review/KnowledgeStatements.test.tsx`,
which uses these same values. A change to either half's contract fails in one of the two.

## Code Commentary

### Logic

**The fixture is two independently built snapshots, and that is the preservation boundary made
mechanical.** The module-scoped `pair` fixture mints one random namespace, builds a
`build_read_scope_fixture` tree for the "before" half and another for the "after" half **under the
same namespace**, then authors four invariant revisions through `author_invariant`:
`ADDED_*` into *after* only, `REMOVED_*` into *before* only, and one shared identity proposed in
*before* and accepted in *after*. So the addition and the removal are a real difference between two
real snapshots, not an edit of one dataset, and no stored identity is altered to produce a case.
Module scope is documented in the fixture's own docstring: both datasets are read-only once built, no
case writes after the fixture is built, and a per-case rebuild would pay for two fixture trees to
measure the same bytes.

**`author_invariant` writes through the store's own operations and refuses quietly never.** It opens
the fixture's database with `open_knowledge_store`, calls `create_invariant` and then
`create_revision`, and raises an `AssertionError` carrying the store's own refusal when either
answers anything but `"created"`. The acceptance reference is **not** a free argument:
`SHARED_ACCEPTANCE_REF` is attached only when the authored origin state is `accepted`, because the
vocabulary refuses a *proposed* revision that claims an acceptance — a proposal claiming an event
that did not happen. That single rule is what makes the shared subject's `acceptance_ref` transition
real rather than fabricated.

**`review` is the one composition call, and it fails loudly on a refusal.** It hands `compose_review`
a hand-assembled `ReviewCandidateResolution` (the two databases, the two `git_root`s and the two
`git_tree_id`s the fixtures carry), a `ReviewSurfaceRequest` naming the master, the leaf and the
selector, and an empty `ReviewRecordInputs`; when the result carries no payload it raises with the
composition's own refusal rather than asserting on `None`. The one case that must render *no*
subject — `test_a_review_that_compared_no_subject_serves_no_operand_at_all` — calls `compose_review`
directly with `selector=None` instead, because that path is the point of the case.

**The six cases, and the property each one owns.**

- **An addition** (`:249-269`): the after side is `present` and carries `ADDED_STATEMENT` verbatim,
  the before side is `absent` with `text is None` and its own no-record detail, and the comparison's
  own `side_absence:before:selector_absent` travels beside it in the payload's limitations. The
  reviewed subject is selected by its own recorded `InvariantIdentitySeed`.
- **A removal** (`:272-285`): the mirror image, with `side_absence:after:selector_absent`.
- **A one-sided field row** (`:288-317`): the shared revision identity is proposed in *before* and
  accepted in *after*, so the comparison reports the transition and each side's own value; the roster
  is asserted **by exact key set** (`acceptance_ref`, `lifecycle`, `payload_digest`, `provenance`),
  `acceptance_ref` keeps `before_value is None` beside `after_value == SHARED_ACCEPTANCE_REF`, and
  `lifecycle` is `("proposed", "accepted")`. Dropping the row, or printing the side that did record a
  value as blank, is what a one-sided statement must not become.
- **A structured value** (`:320-350`): the `provenance` row the comparison reports as *changed*
  carries a value on **both** sides, the two differ, and each is parsed back out of its marker and
  checked against the fixture's own stored authorship envelope (`actor_ref`, `operation_id`,
  `authorization_ref`) — so the projection invents nothing. The case also pins the projection's
  canonicality: `structured_value_text({"b": 1, "a": 2}) == structured_value_text({"a": 2, "b": 1})`.
- **A one-sided record keeps an empty roster** (`:353-369`): an addition reports
  `field_changes == ()` and `before_conditions == ()` while `after_conditions == CONDITIONS`, because
  the comparison reports such a record through its coverage and nine field rows would state nine
  differences where there is one absence.
- **No subject compared** (`:370-408`): `selection_state == "task_context"`, `comparison is None`,
  both sides `unresolved` with `text is None` and **the same** detail ("no knowledge operand was
  compared"), and an empty roster — the case a one-sided rendering must not swallow.

**The fixture helpers are typed and named.** `AuthoredInvariant` is a frozen dataclass carrying the
identities, the words and the origin state; `OneSidedPair` is a frozen dataclass carrying the
namespace, the two `ReadScopeFixture`s and the six identities the cases select subjects by. Every id
is drawn once (`uuid4()`), so a case asserts against the exact identity the review was asked for
rather than against a shape that could be anything.

### Conventions

`pytestmark = pytest.mark.evidence_unit` is the module's whole lane declaration; its membership is the
`unit-regression` row at `mcp/tests/test-evidence-lanes.toml:105`, and its consumption of
`read_scope_test_support` is the consumer row at `mcp/tests/evidence-lifecycle.toml:1436` on that
artifact's `consumer_scope = "exact"` list. The import block is alphabetical within its groups, and
the case functions are full sentences naming the rendering obligation they measure. Constants are
module-level and upper-case, and each case's docstring states the property rather than the mechanics.

### Invariants And Boundaries

- **Two real snapshots, no manufactured edit.** The difference between the halves is authored
  content, not a mutation of one dataset; no stored identity is altered and no record is deleted to
  produce a removal example.
- **The composition is real, and it is the adapter's own entry point.** `compose_review` is called
  with the shipped request type; no payload is substituted and no private helper is reached into.
- **The values the dashboard renders are the values asserted here.** The statements, the
  absent/unresolved details and the `acceptance_ref`/`provenance` rows are the binding between this
  module and the renderer suite.
- **A `None` on a field row is an absence and nothing else.** The structured-value case exists to
  make that falsifiable from both directions: `before_value is not None` and the two projections
  differ.
- **Read-only after the fixture is built.** No case writes to either dataset, and the fixture is
  module-scoped precisely because that holds.
- **Boundary.** This is measurement, not a second implementation: the module imports
  `structured_value_text` to check the projection's markers and canonicality, and it re-derives no
  composition rule of its own.

### Todos

None recorded. One measured limit is deliberately out of this module's scope and is recorded by the
leaf for R07: when the reviewed subject exists only on one side **and that side holds several retained
revisions**, `_identity_item` still returns `candidates[0]`, so which revision's statement is shown is
decided by page order. These cases avoid it by authoring subjects with a single revision and no
claims.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and case
bodies, the fixture module it builds on, the store operations it authors through, the composition it
drives, the owner of the projection it asserts against, and the catalogue and lane rows that register
it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own scope statement: six cases over the real adapter and two real datasets, and the load-bearing properties each one owns.** | `compose_review`; `build_read_scope_fixture` | mcp/tests/test_knowledge_review_one_sided_statements.py:1-28 |
| The module's whole lane declaration. | `pytestmark` | mcp/tests/test_knowledge_review_one_sided_statements.py:69-69 |
| The authored identities and words every case asserts against, drawn once in the builder. | `ADDED_STATEMENT`; `REMOVED_STATEMENT`; `SHARED_STATEMENT`; `SHARED_ACCEPTANCE_REF` | mcp/tests/test_knowledge_review_one_sided_statements.py:74-74; mcp/tests/test_knowledge_review_one_sided_statements.py:76-76; mcp/tests/test_knowledge_review_one_sided_statements.py:78-78; mcp/tests/test_knowledge_review_one_sided_statements.py:80-80 |
| **The two frozen fixture values: one invariant to author (with the origin state that alone decides its acceptance reference) and the pair of snapshots plus the identities cases select by.** | `AuthoredInvariant`; `OneSidedPair` | mcp/tests/test_knowledge_review_one_sided_statements.py:86-99; mcp/tests/test_knowledge_review_one_sided_statements.py:102-114 |
| **The authoring helper: the store's own `create_invariant`/`create_revision`, the refusal carried into an `AssertionError`, and the rule that only an accepted origin state carries the acceptance reference.** | `author_invariant` | mcp/tests/test_knowledge_review_one_sided_statements.py:117-153 |
| **The fixture: two independently built snapshots under one namespace, and the four authored revisions that make an addition, a removal and a real transition.** | `pair` | mcp/tests/test_knowledge_review_one_sided_statements.py:156-219 |
| The one composition call, with the hand-assembled resolution and the loud failure on a refusal. | `review` | mcp/tests/test_knowledge_review_one_sided_statements.py:222-246 |
| **The addition and the removal: the complete present-side statement, the named absent side with `text is None`, and the comparison's own side-absence code.** | `test_an_added_statement_renders_its_after_text_beside_a_named_absent_before`; `test_a_removed_statement_renders_its_before_text_beside_a_named_absent_after` | mcp/tests/test_knowledge_review_one_sided_statements.py:249-269; mcp/tests/test_knowledge_review_one_sided_statements.py:272-285 |
| **The field row: the roster asserted by exact key set, the one-sided value kept, and the lifecycle transition beside it.** | `test_a_field_row_keeps_the_side_that_recorded_a_value_and_names_the_side_that_did_not` | mcp/tests/test_knowledge_review_one_sided_statements.py:288-317 |
| **The structured value: both sides present and different, each projection round-tripped back to the stored envelope, and the projection's canonicality pinned.** | `test_a_structured_field_value_is_rendered_as_its_own_text_and_never_as_an_absence` | mcp/tests/test_knowledge_review_one_sided_statements.py:320-348 |
| The one-sided record reported by coverage with an empty roster, against the conditions the after side really recorded. | `test_a_one_sided_record_is_reported_by_its_coverage_and_not_by_a_roster_of_field_rows` | mcp/tests/test_knowledge_review_one_sided_statements.py:351-367 |
| **The task-context case: no comparison, both sides unresolved with the same reason and no text, and no roster.** | `test_a_review_that_compared_no_subject_serves_no_operand_at_all` | mcp/tests/test_knowledge_review_one_sided_statements.py:370-408 |
| **The projection owner whose markers and canonicality this module asserts.** | `structured_value_text`; `STRUCTURED_VALUE_LEAD`; `STRUCTURED_VALUE_TAIL` | mcp/src/agents_remember/application/review_statement_sides.py:61-62; mcp/src/agents_remember/application/review_statement_sides.py:69-83 |
| The adapter entry point the cases drive, and the one-sided contract its pane values carry. | `compose_review`; `ReviewCandidateResolution`; `ReviewRecordInputs` | mcp/src/agents_remember/application/knowledge_review.py:69; mcp/src/agents_remember/application/knowledge_review.py:334-574; mcp/src/agents_remember/application/knowledge_review.py:86 |
| **The fixture this module builds on, and the public store operations it authors through.** | `ReadScopeFixture`; `build_read_scope_fixture`; `open_knowledge_store`; `create_invariant`; `create_revision` | mcp/tests/read_scope_test_support.py:177-243; mcp/tests/read_scope_test_support.py:270-287; mcp/src/agents_remember/memory/knowledge/store.py:767-784; mcp/src/agents_remember/memory/knowledge/store.py:272-289; mcp/src/agents_remember/memory/knowledge/store.py:291-325 |
| **The lane row that selects this module, and the artifact consumer row that registers it against the fixture it consumes.** | "mcp/tests/test_knowledge_review_one_sided_statements.py" | mcp/tests/test-evidence-lanes.toml:133-133; mcp/tests/evidence-lifecycle.toml:1531-1531 |
| The `consumer_scope = "exact"` artifact whose list this module joined. | `"mcp/tests/read_scope_test_support.py"`; `consumer_scope` | mcp/tests/evidence-lifecycle.toml:1425-1472 |
| **The renderer half that uses these same values, which is what makes a change to either half fail in one of the two.** | `KnowledgeStatements`; `names an absent field value and a recorded empty one without printing either as blank` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:291-336; dashboard/src/panels/review/KnowledgeStatements.tsx:94-121 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): No content impact: citation-only repair. This card's source is unchanged. Rows citing `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml` were re-pointed to the lines MIK-R05 moved, by the installed fixer or by the exact line shift where it declined (each such row byte-identical to memory HEAD, its anchors checked in the base and the shifted ranges); no claim was reworded.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; rows citing lane rows after the one `unit-regression` row MIK-R10 inserted at `test-evidence-lanes.toml:124` (or catalog lines after `evidence-lifecycle.toml:836`) were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No claim was reworded, so the fixer's bullets are kept. No verification stamp was advanced.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R01 moved lines in `evidence-lifecycle.toml` and `test-evidence-lanes.toml`, so citation ranges into it were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (each such row was byte-identical to memory HEAD).
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 moved lines in `evidence-lifecycle.toml` (one consumer at `:832`) and `test-evidence-lanes.toml` (one row at `:112`), and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `evidence-lifecycle.toml`, `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`evidence-lifecycle.toml`, `test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 2 citations into `mcp/tests/evidence-lifecycle.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/tests/evidence-lifecycle.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by the lane row this leaf inserted.** This file is not a changed source file; both ranges that moved belong to `mcp/tests/test-evidence-lanes.toml` (one row inserted at `:111`) and `mcp/tests/evidence-lifecycle.toml` (two rows added). Its one registration row was re-read and re-derived from the lines that actually carry each anchor: the module's lane row `:105` → `:109`, and its read-scope consumer row `:1436` → `:1446`, the row this leaf's own new consumer entry sits above. No claim wording or anchor was changed, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.

- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`):
  **created.** The module is new in this leaf and this is its one-to-one card. It records the two
  independent snapshots that make an addition and a removal real rather than manufactured (the
  preservation boundary made mechanical), the authoring rule that only an accepted origin state
  carries the acceptance reference, the six cases and the property each owns, the exact-key-set
  assertion on the one-sided field roster, and the structured-value case's round-trip back to the
  stored authorship envelope plus its canonicality check. It records the module's registration in the
  `unit-regression` lane and its `consumer_scope = "exact"` consumer row on the shared read-scope
  fixture, and the R07 revision-selection limit the cases deliberately avoid. **Stamp accounting:**
  the verification pair names production line
  `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` — the leaf's base, and the last real commit the reading
  was taken against — because every construct this card cites exists only in this leaf's uncommitted
  candidate and no commit contains the bytes a stamp would claim to have verified.
  What was actually read is stated beside it; closeout owns the stamp.
