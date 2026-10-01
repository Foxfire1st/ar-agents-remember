# dashboard/src/panels/review/KnowledgeStatements.test.tsx

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

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

- **The suite's own scope statement: the real component and the real client with only `fetch` stubbed, the values' provenance from the server-side cases, and the defect these cases catch.** [1]
- The real surface the cases mount, and the real client it calls — neither is stubbed. [2]
- **The measured server strings, the pane's two structured projections, and the declared-state `binary` fixture with its own labelling comment.** [3]
- The four typed side builders and the two payload builders the cases spread overrides into. [4]
- **The transport stub and the mount helper: `fetch` and nothing else, so the payload travels the production route.** [5]
- The teardown that keeps a stubbed global from leaking between cases. [6]
- **The addition: the absent before line, the present after line, and the full after statement read out of the rendered diff pane.** [7]
- The removal, symmetrically. [8]
- **The control that a two-sided area names no side — the one case that must keep passing under both the old and the new implementation.** [9]
- **The unreadable-opposite case: the reason beside the text, the explicit no-diff line, the operand in `file-pane`, and `diff-pane` absent.** [10]
- The three declared states carried through as their own tokens and never collapsed into one another. [11]
- The task-context case: two named states, no diff and no content pane. [12]
- **The field-row case: absent, changed-text, changed-structured (asserted unequal) and recorded-empty in one render, none printed as a blank.** [13]
- The jsdom answers that let the shipped CodeMirror primitives render in these cases. [14]
- The component under test and the rule it implements. [15]
- The shipped renderers whose DOM these cases read back: the diff engine and the viewer, each asserted through its own host element. [16]
- The shipped renderers whose DOM these cases read back. [17]
- **The server-side half these cases mirror: the same statements and details measured through the real composition.** [18]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The suite stubs one HTTP transport inside
one browser test and carries no identity that ranges beyond the repository namespace the payload
names.

No meaningful cross-repo references found.
