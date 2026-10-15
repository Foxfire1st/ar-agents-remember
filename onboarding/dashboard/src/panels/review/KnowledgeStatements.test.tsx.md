# dashboard/src/panels/review/KnowledgeStatements.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The **renderer half** of ICR-R06@v1. Nine cases drive the real `ReviewSurface` over the real
intent-review client with only `fetch` stubbed, so the payload below travels the same route a
browser's does: JSON in, shared `getReviewJson` decode and the mounted component tree's actual selected-statement
caller or declared-operand fallback, with shipped diff/viewer primitives — which do render in jsdom because
`dashboard/src/test/setup.ts` supplies the `matchMedia`, `ResizeObserver` and
`Range.getClientRects` answers jsdom omits. Nothing here renders a hand-rolled stand-in for the
statement area, and no assertion reads a prop the test itself passed: every case asserts what the
rendered DOM contains.

The production-composition suite in `mcp/tests/test_knowledge_review_one_sided_statements.py` independently reads real snapshots through `compose_review`. The three authored statement strings match across the two source files, and both suites protect related declared-state/text obligations. Their complete fixtures and field assertions are not identical: this renderer suite uses its own acceptance reference, recorded-empty lifecycle and unequal structured provenance values. The Python field case instead checks a `text-knowledge:` acceptance reference and a proposed-to-accepted lifecycle, with no differing provenance row. Matching titles, comments or three strings are not a cross-half fixture-equivalence guarantee.

## Code Commentary

### Logic

The mounted helper awaits `review-center-column` and scopes its assertions to the selected subject's main reading area. The statement pane is no longer under Technical details. The no-operand case selects a subject whose two operands are unresolved; it does not claim that the surface mounts a knowledge pane when no subject is selected. The absent/recorded-empty distinction is checked through non-authored field rows, because authored statement/conditions values are intentionally excluded from that list.

**Fixture provenance is per value, not inherited from the module comment.** `ADDED_STATEMENT`, `REMOVED_STATEMENT` and `SHARED_STATEMENT` have the same literal texts as the Python suite's constants. That static source comparison does not make every overlay a measured server reply. `SHARED_ACCEPTANCE_REF` is the renderer fixture `requirement:KS-R08@v1`; the absent side, recorded-empty lifecycle and two unequal structured provenance projections are authored here for the mounted field-row case. `ABSENT_BEFORE`, `ABSENT_AFTER` and `UNRESOLVED_AFTER` supply this suite's detail text; the Python cases assert their own returned states/text and selected detail substrings, not all these full fixture operands. Its structured-value case checks equality under key reordering rather than two differing provenance envelopes. `BINARY_AFTER` is explicitly a declared-state renderer fixture, not a shipped statement-builder output.

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

- Addition and removal: the named absent side carries its own detail and the complete available operand appears in the shipped diff DOM.
- Both present: both recorded operands remain available to the diff and neither named side-state line appears.
- Unreadable opposite: the available text remains in the content pane with the opposite side's own reason; no diff or manufactured empty operand appears.
- Declared absent, unresolved and binary states retain their distinct tokens, including the labelled binary vocabulary fixture.
- Neither present: a selected subject with two unresolved operands has both named state lines and neither a diff nor a content pane.
- Field rows: `acceptance_ref` is named absent before; the recorded-empty `lifecycle` value is explicit after; the two compact structured provenance values remain distinct. Authored condition text is not reintroduced into the non-authored rows.

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
- **DOM behavior assertions.** Rendering behavior is read from the DOM; the field-row case also asserts that its two renderer-authored structured provenance constants differ.
- **Related obligations, independently authored fixtures.** The three matching statement literals support a source comparison, not a single fixture source or automatic cross-half failure. Each suite has its own states, detail/field values and assertions; acceptance/provenance/recorded-empty overlays here are not claimed as the Python composition's measured output.
- **A declared-state fixture is labelled as such.** `binary` is exercised because the renderer must
  treat unsupported content distinctly from a known absence, not because a producer exists.
- **Boundary.** This is the mounted renderer contract over test-authored wire fixtures. The actual selected-subject callers and declared-operand fallback draw the bodies; neither diff nor viewer is re-implemented. The suite does not certify production-composition fixture equivalence.

### Todos

None recorded. The `binary` producer gap is recorded on `KnowledgeStatements.tsx`'s card and is a
vocabulary obligation rather than a missing case.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the suite's own header comment and
case bodies, the actual renderer callers, the surface/client and jsdom setup, plus the independently authored production-composition suite. No shared fixture source or identical field/operand population is implied.

**Current citation form.** References 7–11 use whole-file source ranges, while 12 and 13 bind the no-readable-operand and field-row assertion ranges. They no longer carry the former quoted case-name anchors. Source ranges and their notes are evidence locators, not named typed proofs or a claim of backend/renderer fixture identity.


- The real surface the cases mount, and the real client it calls — neither is stubbed. [2]











- The jsdom answers that let the shipped CodeMirror primitives render in these cases. [14]
- The component under test and the rule it implements. [15]
- The shipped renderers whose DOM these cases read back: the diff engine and the viewer, each asserted through its own host element. [16]


- The shipped renderers whose DOM these cases read back. [17]

- The production-composition suite independently checks statement states/text, text-knowledge acceptance and proposed-to-accepted lifecycle without a differing provenance row; its separate structured-value assertion checks key-order equality. [18]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The suite stubs one HTTP transport inside
one browser test and carries no identity that ranges beyond the repository namespace the payload
names.

No meaningful cross-repo references found.

- The mounted suite uses the real surface/client with fetch stubbed; its authored overlays and the module comment do not establish identical backend-measured field fixtures. [1]
- Three statement literals match the Python source constants; the acceptance and unequal structured provenance values are renderer-authored fixtures, as is the labelled binary vocabulary case. [3]
- The four typed side builders and the two payload builders the cases spread overrides into. [4]
- **The transport stub and the mount helper: `fetch` and nothing else, so the payload travels the production route.** [5]
- The teardown that keeps a stubbed global from leaking between cases. [6]
- **The addition: the absent before line, the present after line, and the full after statement read out of the rendered diff pane.** [7]
- The removal, symmetrically. [8]
- **The control that a two-sided area names no side — the one case that must keep passing under both the old and the new implementation.** [9]
- **The unreadable-opposite case: the reason beside the text, the explicit no-diff line, the operand in `file-pane`, and `diff-pane` absent.** [10]
- The three declared states carried through as their own tokens and never collapsed into one another. [11]
- A selected subject with two unresolved operands has two named states, no diff and no content pane. [12]
- Non-authored field rows distinguish absent acceptance reference, recorded-empty lifecycle and two unequal structured provenance values. [13]
