# dashboard/src/panels/review/KnowledgeStatements.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/KnowledgeStatements.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:14:26+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82` |
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The **renderer half** of ICR-R06@v1. Nine cases drive the real `ReviewSurface` over the real
intent-review client with only `fetch` stubbed, so the payload below travels the same route a
browser's does: JSON in, `getJson` decode, component tree, `KnowledgeStatements`, and the shipped
`DiffPane`/`FilePane` CodeMirror primitives — which do render in jsdom because
`dashboard/src/test/setup.ts` supplies the `matchMedia`, `ResizeObserver` and
`Range.getClientRects` answers jsdom omits. Nothing here renders a hand-rolled stand-in for the
statement area, and no assertion reads a prop the test itself passed: every case asserts what the
rendered DOM contains.

The **production-composition half** of the same requirement lives in
`mcp/tests/test_knowledge_review_one_sided_statements.py`, which drives the real `compose_review`
over two real snapshots. The two halves assert the **same** statements, the same absent/unresolved
details and the same `acceptance_ref`/`provenance` field rows, so a change to either half's contract
fails in one of the two.

## Code Commentary

### Logic

The mounted helper awaits the technical-details region and scopes its one-sided statement assertions to that region. This keeps the existing statement-pane contract separate from the central selected-subject rendering covered by SubjectReview.test.tsx; the operand and unavailable-state assertions remain unchanged.

**The values are the server's measured output, not invented fixtures.** `ADDED_STATEMENT`,
`REMOVED_STATEMENT`, `SHARED_STATEMENT`, `SHARED_ACCEPTANCE_REF`, `ABSENT_BEFORE`, `ABSENT_AFTER` and
`UNRESOLVED_AFTER` are declared "the authored words and identities the server-side cases measure,
verbatim", and `STRUCTURED_BEFORE`/`STRUCTURED_AFTER` are the pane's own
`<recorded as a structured value, rendered as compact JSON: …>` projections of the two authorship
envelopes. `BINARY_AFTER` is the documented exception: `binary` is a state the review vocabulary
declares and **no shipped statement-side builder emits**, so the constant is labelled a declared-state
fixture whose detail is the case's own words rather than the server's.

**The defect the cases catch is stated in the file, and it is the reason each case asserts DOM text
rather than a shape.** The pane used to draw its diff only when *both* statements were `present`,
while the side line returned `null` for the present side: an added or a removed statement rendered as
two muted lines and no statement text at all. Every `absent`/`present` case below fails against that
implementation, because the statement text is only in the DOM when it is drawn.

**The transport is the only stub, and `serve`/`reviewed` keep it that way.** `serve(result)` stubs
`globalThis.fetch` with a function returning `{ok: true, status: 200, json: async () => result}`;
`reviewed(knowledgeOver, payloadOver)` composes that with `payload(...)`/`knowledge(...)` and calls
`render(<ReviewSurface repo master leaf onBack />)`. `intentReview` — the real client — therefore
runs, and the surface reaches the statement area exactly as production does.

**The nine cases, and what each one pins.**

- **An addition** (`:194-212`): the before state line carries `data-side-state="absent"` and the
  before snapshot's own no-record detail, the after line carries `present`, and the diff pane's
  `textContent` — read through `waitFor`, because CodeMirror renders asynchronously — contains the
  full after statement. The statement is asserted in the **rendered DOM**, not in the payload the test
  sent.
- **A removal** (`:214-228`): the mirror image, with the before statement in the diff pane and the
  after line `absent`.
- **Both present** (`:230-241`): the shared statement is in the diff pane and **neither**
  `review-before-state` nor `review-after-state` exists, so a two-sided area names no side.
- **An unreadable opposite** (`:243-259`): the after line is `unresolved` with its own reason, the
  `review-no-diff-claimed` line states that no diff is drawn, the readable operand stays visible in
  `file-pane`, and `diff-pane` is **absent** — the assertion that an empty-string operand was not
  manufactured.
- **Three declared states as their own tokens** (`:261-274`, a three-row `it.each` over `absent`,
  `unresolved` and `binary`): each renders as its own `data-side-state`, the opposite side stays
  `absent`, and no diff is drawn — so no one of the three collapses into another.
- **Neither present** (`:276-289`): the task-context pane renders both `unresolved` state lines and
  neither `diff-pane` nor `file-pane`.
- **Field rows** (`:291-336`): four rows in one render assert
  `acceptance_ref: (absent) → requirement:KS-R08@v1`, `lifecycle: proposed → accepted`,
  `provenance: <structured before> → <structured after>` with the two projections asserted **unequal**
  (a shared note would have made a changed field read as one unchanged value), and
  `essential_conditions: … → (recorded empty)` — the absent value, the changed text value, the changed
  structured value and the present-but-empty value, none of them printed as a blank.

**The fixture builders are deliberately minimal and typed.** `present`/`absent`/`unresolved`/`binary`
build one `ReviewSideContent` each; `knowledge(over)` and `payload(over)` build a complete
`ReviewKnowledgePane`/`ReviewPayload` with spread overrides. `afterEach` runs `cleanup()` and
`vi.unstubAllGlobals()`, so a stubbed `fetch` cannot leak into the next case.

### Conventions

React Testing Library throughout: `render`, `findByTestId` for the awaited first paint and
`getByTestId`/`queryByTestId` afterwards, `waitFor` around every CodeMirror-backed assertion. Case
names are full sentences describing the rendering obligation, matching the surface's other suites.
The test ids it reads are the production ones — `review-before-state`, `review-after-state`,
`review-no-diff-claimed`, `review-field-changes`, `diff-pane`, `file-pane` — so the suite cannot pass
against a private vocabulary of its own.

### Invariants And Boundaries

- **The real component and the real client.** Only `fetch` is stubbed; no case renders a stand-in for
  the surface, the statement area, the diff or the viewer.
- **DOM assertions only.** No case asserts a prop it passed, and no case asserts an intermediate
  value; the statement text is read back out of the rendered DOM.
- **The two halves share one set of values.** The statements and details asserted here are the ones
  the Python composition test measures; changing one side's string is what makes the other half fail.
- **A declared-state fixture is labelled as such.** `binary` is exercised because the renderer must
  treat unsupported content distinctly from a known absence, not because a producer exists.
- **Boundary.** This is the statement area's renderer contract. The wire values are the server's, the
  element bodies are `KnowledgeStatements.tsx`'s, and neither diff nor viewer is re-implemented by the
  suite.

### Todos

None recorded. The `binary` producer gap is recorded on `KnowledgeStatements.tsx`'s card and is a
vocabulary obligation rather than a missing case.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the suite's own header comment and
case bodies, the component it drives, the surface and client it deliberately does not stub, the jsdom
setup that lets the shipped CodeMirror primitives render, and the server-side case module it mirrors.

**Citation repair, and why the test-name rows read as quoted literals.** Seven rows cite one case by
its suite range, and each names that case by the double-quoted string the case itself passes to `it` —
which is the only anchor form that both the citation grammar and the occurrence rule accept here: a
test's own name is several words, so a backticked span is *not* identifier-shaped, and the citation
grammar explicitly refuses such a span as an anchor and requires a double-quoted literal instead. The
`file-pane` and `diff-pane` anchors in the unreadable-opposite row stay backticked because those are
single identifiers. The suite itself is unchanged by that repair; only this card was wrong.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The suite's own scope statement: the real component and the real client with only `fetch` stubbed, the values' provenance from the server-side cases, and the defect these cases catch.** | `ReviewSurface`; `KnowledgeStatements` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:1-27 |
| The real surface the cases mount, and the real client it calls — neither is stubbed. | `ReviewSurface`; `intentReview` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:1-14; dashboard/src/data/review.ts:328-347 |
| **The measured server strings, the pane's two structured projections, and the declared-state `binary` fixture with its own labelling comment.** | `ADDED_STATEMENT`; `REMOVED_STATEMENT`; `SHARED_ACCEPTANCE_REF`; `STRUCTURED_BEFORE`; `STRUCTURED_AFTER`; `BINARY_AFTER` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:45-47; dashboard/src/panels/review/KnowledgeStatements.test.tsx:49-49; dashboard/src/panels/review/KnowledgeStatements.test.tsx:54-59; dashboard/src/panels/review/KnowledgeStatements.test.tsx:69-69 |
| The four typed side builders and the two payload builders the cases spread overrides into. | `present`; `absent`; `unresolved`; `binary`; `knowledge`; `payload` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:71-73; dashboard/src/panels/review/KnowledgeStatements.test.tsx:75-85; dashboard/src/panels/review/KnowledgeStatements.test.tsx:76-80; dashboard/src/panels/review/KnowledgeStatements.test.tsx:87-104; dashboard/src/panels/review/KnowledgeStatements.test.tsx:106-164 |
| **The transport stub and the mount helper: `fetch` and nothing else, so the payload travels the production route.** | `serve`; `reviewed` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:168-174; dashboard/src/panels/review/KnowledgeStatements.test.tsx:176-187 |
| The teardown that keeps a stubbed global from leaking between cases. | `afterEach` | dashboard/src/panels/review/KnowledgeStatements.test.tsx:188-191 |
| **The addition: the absent before line, the present after line, and the full after statement read out of the rendered diff pane.** | "draws an added invariant's full after statement beside an absent-before label" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:195-213 |
| The removal, symmetrically. | "draws a removed invariant's full before statement beside an absent-after label" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:215-229 |
| **The control that a two-sided area names no side — the one case that must keep passing under both the old and the new implementation.** | "keeps both statements when both sides recorded one, and names no side" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:231-242 |
| **The unreadable-opposite case: the reason beside the text, the explicit no-diff line, the operand in `file-pane`, and `diff-pane` absent.** | "keeps the available text and claims no diff when the other side is unreadable" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:244-260 |
| The three declared states carried through as their own tokens and never collapsed into one another. | "renders a %s side as that state and never as another one" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:262-275 |
| The task-context case: two named states, no diff and no content pane. | "draws no diff and both named states when no subject was compared" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:277-290 |
| **The field-row case: absent, changed-text, changed-structured (asserted unequal) and recorded-empty in one render, none printed as a blank.** | "names an absent field value and a recorded empty one without printing either as blank" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:292-337 |
| The jsdom answers that let the shipped CodeMirror primitives render in these cases. | `Range.getClientRects`; `ResizeObserver`; `matchMedia` | dashboard/src/test/setup.ts:65-83; dashboard/src/test/setup.ts:108-112 |
| The component under test and the rule it implements. | `KnowledgeStatements`; `unavailable`; `sideLine` | dashboard/src/panels/review/KnowledgeStatements.tsx:34-35; dashboard/src/panels/review/KnowledgeStatements.tsx:37-45; dashboard/src/panels/review/KnowledgeStatements.tsx:94-121 |
| The shipped renderers whose DOM these cases read back: the diff engine and the viewer, each asserted through its own host element. | `DiffPane`; `FilePane` | dashboard/src/panels/changeset/DiffPane.tsx:123-193; dashboard/src/panels/file-viewer/FilePane.tsx:25-78 |
| The shipped renderers whose DOM these cases read back. | `DiffPane`; `FilePane` | dashboard/src/panels/changeset/DiffPane.tsx:123-193; dashboard/src/panels/file-viewer/FilePane.tsx:25-78 |
| **The server-side half these cases mirror: the same statements and details measured through the real composition.** | `test_an_added_statement_renders_its_after_text_beside_a_named_absent_before`; `test_a_field_row_keeps_the_side_that_recorded_a_value_and_names_the_side_that_did_not`; `test_a_structured_field_value_is_rendered_as_its_own_text_and_never_as_an_absence` | mcp/tests/test_knowledge_review_one_sided_statements.py:249-269; mcp/tests/test_knowledge_review_one_sided_statements.py:288-317; mcp/tests/test_knowledge_review_one_sided_statements.py:320-348 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The suite stubs one HTTP transport inside
one browser test and carries no identity that ranges beyond the repository namespace the payload
names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: MIK-R34 extracted `DiffPane`'s two view builders above the component and gave `FilePane` an optional `marks` prop, so the two renderer rows no longer held `DiffPane` in their old range. Both were re-measured by hand onto the two components' current extents (`DiffPane.tsx:123-193`, `FilePane.tsx:25-78`), the extents the fixer gives the same anchors elsewhere. Claims unchanged. No stamp advanced.
- 2026-09-26T20:40:46Z — Reconciled the shared revision-selection consumer and scoped technical-pane regression account.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T23:13+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by this leaf's second curation pass.** six reference rows anchored their cases with a backticked prose title, which the citation checker does not read as an anchor (a code identifier, a `#` heading or a double-quoted literal); each now carries the case's exact `it(...)` title as a double-quoted literal, and the cited ranges already hold it. No claim was re-worded and no range changed. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout's metadata refresh owns the real one.

- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only — a pre-existing defect the quality gate reports, and this leaf does not change the suite it cites.** Seven rows of the reference table named their case with a **backticked** test name. That form satisfies neither half of the citation grammar: a test name is several words, so the span is not identifier-shaped (the grammar refuses it as an unchecked span and requires a double-quoted literal instead, and a TypeScript parse of a bare sentence is not a call or a generic type), and the occurrence rule would reject it anyway. So each of those rows was a row with Source content and **no anchor**. Each was repaired by writing the case's own name as the double-quoted literal the suite passes to `it`, which occurs literally inside the cited range: `194-212` ("draws an added invariant's full after statement beside an absent-before label"), `214-228` ("draws a removed invariant's full before statement beside an absent-after label"), `230-241` ("keeps both statements when both sides recorded one, and names no side"), `243-259` ("keeps the available text and claims no diff when the other side is unreadable"), `261-274` ("renders a %s side as that state and never as another one"), `276-289` ("draws no diff and both named states when no subject was compared") and — the same defect, in a row the gate's range list did not enumerate — `291-336` ("names an absent field value and a recorded empty one without printing either as blank", whose row also carried the inverted, impossible range `291-289`, now corrected to the case's real `291-336`). No claim's meaning was changed, no range was re-pointed except that one inversion, and the `file-pane`/`diff-pane` identifiers in the unreadable-opposite row were left as they are. **This is not a consequence of this leaf:** `dashboard/src/panels/review/KnowledgeStatements.test.tsx` is **not** touched by `260921-ICR-L3` (its bytes are identical to `d80a0513e928ef29a973527d09597c82c96fde87`), so every range above still resolves against the same unchanged file and only this card was wrong. **Stamp accounting:** the verification pair now names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against, and the commit whose bytes the cited suite still has — while the recorded working candidate records the candidate this card was read in; the repair itself is uncommitted and closeout owns the real stamp.
- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`):
  **created.** The module is new in this leaf and this is its one-to-one card. It records the two
  load-bearing choices a reader must not weaken: the cases drive the **real** `ReviewSurface` over the
  **real** `intentReview` client with only `fetch` stubbed, and every assertion reads the rendered DOM
  rather than a prop the test passed (which is what makes the addition/removal cases fail against the
  pre-fix pane). It records the nine cases one by one, the deliberate `binary` declared-state fixture
  and why it is labelled, the shared-value binding to
  `mcp/tests/test_knowledge_review_one_sided_statements.py`, and the jsdom setup that lets the shipped
  CodeMirror primitives render. **Stamp accounting:** the verification pair names production line
  `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` — the leaf's base, and the last real commit the reading
  was taken against — because every construct this card cites exists only in this leaf's uncommitted
  candidate and no commit contains the bytes a stamp would claim to have verified.
  What was actually read is stated beside it; closeout owns the stamp.
