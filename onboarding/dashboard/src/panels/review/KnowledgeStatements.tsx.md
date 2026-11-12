# dashboard/src/panels/review/KnowledgeStatements.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render the supplied statement operands according to their declared `present`, `absent` or `unresolved` states, keeping every available statement and the explicit reason for an unavailable opposite. This is a display-only declared-operand renderer and fallback: it makes no request, holds no state and adds no control or local content classifier.

## Code Commentary

Every branch depends on declared state, never on whether the text looks empty. Two present sides use the shipped `DiffPane` over their own text, with the before side's language. That early return draws no state lines. In every other case, `sideLine` draws both supplied state/detail lines, with `review-before-state` / `review-after-state` test IDs and each side's `data-side-state` token. [22]

With one present side and a known absent opposite, `oneSidedDiff` uses the present text on its own side and an empty string on the absent side. The language belongs to the present operand. This is a stated addition or removal: both state lines name the absence rather than leaving the empty diff half for the reader to interpret. [23]

With one present side and an unresolved opposite, `availableContent` renders the full available operand in the shipped `FilePane`, uses that operand's language, and explicitly says that no diff is claimed. An unresolved side is not a known-empty operand, so drawing a one-sided diff would invent an addition or removal. When neither side is present, only the two state/detail lines are drawn; no content or diff pane is created. [22] [23]

Diff layout defaults to split and accepts the caller's inline mode. Both diff branches use `collapse={false}`. All three pane calls now use `fit`, so the page's reading column owns scrolling instead of a nested statement pane. The diff engine and file viewer remain shared implementations. [23]

## Invariants And Boundaries

The server model owns consistency between a side's declared state and its text. This component does not deeply validate arbitrarily cast JavaScript props. Its `?? ''` fallbacks apply to text used by a declared-present branch; they do not authorize treating unreadable content as an empty document. The statement wire's current vocabulary is present/absent/unresolved. Binary code-source content is a separate contract, with no binary statement branch or future binary-producer obligation here.

This module does not own every selected-revision statement display or the former technical-pane location. `SubjectReview.SelectedStatement` delegates to `IntentWordDiff.IntentStatementBody`; that owner's addition/removal path draws its own labelled prose, falling back here when its expected present operand is unavailable. The raw declared-operand calls and local branches remain this module's responsibility.

The stored `KnowledgeStatements.test.tsx` cases supply direct synthetic operands while mounting the real shipped pane components. They cover full addition/removal words, both-present words without side lines, unresolved-opposite content without a diff, and absent/unresolved tokens with neither side present. The fit cases compare the assigned pane class with direct fit panes. These are source-declared component assertions, not a native captured-comparison, browser geometry, performance or MEMORY acceptance result; no tests were run for this restoration.

## Evidence

No configured domain documentation source was available. This account uses repository implementation and stored assertion declarations.


The remaining supporting owners are `models/knowledge/review.py::ReviewSideContent`, `application/review_statement_sides.py::side_content`, `SubjectReview.tsx::SelectedStatement`, `IntentWordDiff.tsx::OneSidedStatement` / `IntentStatementBody`, and the complete stored cases in `KnowledgeStatements.test.tsx`.

- The exported component counts declared-present sides and retains both state lines outside its two-sided branch. [22]
- The shared two-sided and one-sided diff calls preserve operand language and layout; the available-content call explicitly refuses a diff; all three request fit panes. [23]
- Supporting current owner mcp/src/agents_remember/models/knowledge/review.py [24]
- Supporting current owner mcp/src/agents_remember/application/review_statement_sides.py [25]
- Supporting current owner dashboard/src/panels/review/SubjectReview.tsx [26]
- Supporting current owner dashboard/src/panels/review/IntentWordDiff.tsx [27]
- Supporting current owner dashboard/src/panels/review/IntentWordDiff.tsx [28]
- Supporting current owner dashboard/src/panels/review/KnowledgeStatements.test.tsx [29]
