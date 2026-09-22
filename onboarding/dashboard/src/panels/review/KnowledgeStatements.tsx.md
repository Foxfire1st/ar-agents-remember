# dashboard/src/panels/review/KnowledgeStatements.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/KnowledgeStatements.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l6`, uncommitted; base `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` |
| lastVerifiedCommitHash | `d21bc8a6c5d30e2394a72d056bff216b766407c2` |
| lastVerifiedCommitDate | 2026-09-22T08:22:57+02:00|
| reviewedWorkingCandidate | candidate `ar/260921-icr-l3`, uncommitted; base `d80a0513e928ef29a973527d09597c82c96fde87` |
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The statement area of pane 1: the two recorded operands, and the state of each side. It is the one
owner of the rule ICR-R06@v1 states — **a knowledge addition or removal renders the complete
available statement alongside the explicit known-absent side** — and it exists because the surface
that used to own that area got it wrong in a way no gate caught: `ReviewSurface`'s `KnowledgePane`
drew the shipped diff only when *both* sides were `present`, and its `sideState` helper returned
`null` for the side that *was* present, so an added or a removed statement rendered as two muted
state lines and **no statement text at all**. The header comment states that history and the rule
that replaces it, and `ReviewSurface` now delegates the whole area to this component.

The component is display-only in the same sense the rest of the surface is: it renders the two
`ReviewSideContent` values the payload carried, holds no state, makes no request, and adds no
control. It reuses the shipped `DiffPane` and `FilePane` rather than growing a second diff engine or
a second viewer.

## Code Commentary

### Logic

**Every branch is decided by a side's declared `state`, never by inspecting its text.** That is the
module header's own rule and it is what makes the four cases below exhaustive without a fifth: the
component counts the `present` sides and branches on the count, so the text of a non-present side can
never be read as an operand.

**Both sides `present` → the shipped two-sided diff, exactly as before.** `bothPresent` renders
`DiffPane` with `before.text ?? ""`, `after.text ?? ""`, `language={before.language}`, `mode="split"`
and `collapse={false}` — the same call, and the same before-side language, the pane made before the
one-sided paths existed. The `?? ""` can only apply to a `present` side, which the model guarantees
carries text.

**One `present`, the other `absent` → a one-sided diff with the absent side named above it.**
`oneSidedDiff` feeds `DiffPane` the present operand on its own side and a genuinely empty string on
the absent side — which is the diff engine's own shape for an addition (an empty `a` = every line
added) or a removal (an empty `b` = every line removed). The empty half is a *stated* fact rather
than one the reader has to interpret, because the caller renders `sideLine` for **both** sides beside
it: `<name> (<state>): <detail>`, carrying `data-testid="review-<name>-state"` and
`data-side-state={side.state}`. The language passed to the diff is the drawn operand's own, because
that operand is the only text in the pane.

**One `present`, the other `binary` or `unresolved` → the available text as content, the
unavailable side's own reason beside it, and no diff.** `unavailable(state)` is the one predicate for
that pair, and `availableContent` renders the `review-no-diff-claimed` line ("no diff is drawn: the
other side is not a known-empty operand, so an addition or a removal cannot be claimed from it.") and
the present operand in a shipped `FilePane`. A diff here would claim the opposite operand is a
known-empty document — precisely the claim the server's `absent`/`unresolved` split exists to make
unavailable, and precisely the empty-string operand the packet forbids.

**Neither side `present` → both sides' own state lines and nothing else.** This is the task-context
pane, where no subject was compared and neither side may read as an empty operand; no diff and no
content pane are rendered.

**The text is never re-typed here.** A present side's `text` is what the server recorded, and a side
that is not `present` carries no text at all (the model refuses one that does), so nothing in this
module can turn a missing operand into an empty document — the property the renderer's cases assert
against the real `DiffPane`/`FilePane` DOM rather than against a prop.

### Conventions

The component takes exactly two props, `before` and `after`, both `ReviewSideContent` from
`../../data/review`; it declares no client and holds no state. Its helpers are plain module-level
functions with lower-case names (`unavailable`, `sideLine`, `bothPresent`, `oneSidedDiff`,
`availableContent`) and the exported component is the one declaration in `PascalCase`, matching the
route's idiom. `sideLine` is the single source of the `review-before-state` / `review-after-state`
test ids and of the `data-side-state` attribute, so a case can read a side's declared state back out
of the DOM instead of inferring it from a sentence. Inline `style` objects match the cockpit panels'
idiom.

### Invariants And Boundaries

- **A state is drawn, never inferred.** The four branches are a function of `state` alone; no branch
  reads a side's text to decide what it is.
- **Known absence is named, and it is not the same fact as unavailable content.** An `absent` side is
  the empty operand of a one-sided diff *and* a named state line; a `binary`/`unresolved` opposite
  never reaches the diff at all and gets the explicit no-diff line instead.
- **A present statement is always drawn.** Every path that has one `present` side renders its text
  (in the diff, or in `FilePane`); no path can drop it, which is the defect this component closes.
- **The diff engine and the viewer are reused, not re-implemented.** `DiffPane` comes from the
  change-set route and `FilePane` from the file-viewer route; this module declares neither.
- **Display-only.** No request, no control, no state, no conclusion; the component renders records
  another owner stored.
- **Boundary.** It owns the statement area's *rendering* contract only. What a side's state and text
  are is `mcp/src/agents_remember/application/review_statement_sides.py`'s contract, and the payload
  those values arrive in is the server's wire shape; this file re-derives neither.

### Todos

None recorded. One declared limit, restated here because it is a rendering obligation rather than a
defect: `binary` is a declared `ReviewSideState` with **no producer** on the statement-side path
today (it appears in the vocabulary and in the source-inventory content classification, and in no
statement-side builder), so the renderer's `binary` case is a declared-state fixture whose detail is
the test's own words rather than a server value. The branch is still required: the renderer must
treat unsupported content distinctly from a known absence whether or not a producer exists yet.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the component's own header comment
and its four branches, the shipped renderers it reuses, the model types it consumes, the surface
that now delegates to it, and the case module that drives the real `ReviewSurface` over the real
client.

**Test-name anchors are quoted, not backticked.** A row that cites one case names it by the
double-quoted string the case passes to `it`: a test name is several words, so a backticked span is not
identifier-shaped and the citation grammar refuses it as an anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own record of the defect and the rule: the pane drew the diff only when both sides were present while the side line returned null for the present side, and the four branches that replace it are decided by declared state.** | "neither side `present`" | dashboard/src/panels/review/KnowledgeStatements.tsx:1-26; dashboard/src/panels/review/KnowledgeStatements.tsx:93-118 |
| The two shipped renderers and the wire types this module imports, and the absence of any client import. | `ReviewSideContent`; `DiffPane`; `FilePane` | dashboard/src/panels/review/KnowledgeStatements.tsx:28-30 |
| **The one predicate for the unavailable-content pair, which is what keeps `binary`/`unresolved` out of the diff branch.** | `unavailable` | dashboard/src/panels/review/KnowledgeStatements.tsx:32-34 |
| **The state line rendered for every non-two-sided area, carrying the state's own token in `data-side-state`.** | `sideLine` | dashboard/src/panels/review/KnowledgeStatements.tsx:36-44 |
| The unchanged two-sided path, with the before side's declared language preserved exactly as the pre-R06 pane passed it. | `bothPresent` | dashboard/src/panels/review/KnowledgeStatements.tsx:46-60 |
| **The one-sided diff: the present operand on its own side, the known-absent side genuinely empty, and the drawn operand's own language.** | `oneSidedDiff` | dashboard/src/panels/review/KnowledgeStatements.tsx:62-77 |
| **The available-content path: the explicit no-diff line and the readable operand as content, so no addition or removal is claimed from an unreadable side.** | `availableContent` | dashboard/src/panels/review/KnowledgeStatements.tsx:79-91 |
| **The branch itself: count the present sides, render both state lines for anything that is not two-sided, and split on `unavailable`. The two-present early return is why a both-present area names no side.** | `KnowledgeStatements` | dashboard/src/panels/review/KnowledgeStatements.tsx:93-118 |
| The model a side is: the closed four-member state literal and the value that carries `state`, optional `text`, `language` and `detail`. | `ReviewSideState`; `ReviewSideContent` | dashboard/src/data/review.ts:12-12; dashboard/src/data/review.ts:15-21; dashboard/src/data/review.ts:36-36; dashboard/src/data/review.ts:122-122; dashboard/src/data/review.ts:123-123; dashboard/src/data/review.ts:33-33; dashboard/src/data/review.ts:37-37 |
| The pane whose two statement fields feed this component. | `ReviewKnowledgePane` | dashboard/src/data/review.ts:98-103 |
| **The delegation: pane 1 renders `KnowledgeStatements` where it used to hold the both-present gate and the `sideState` helper.** | `KnowledgePane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewSurface.tsx:182-205; dashboard/src/panels/review/ReviewSurface.tsx:7-7; dashboard/src/panels/review/ReviewSurface.tsx:48-48; dashboard/src/panels/review/ReviewSurface.tsx:220-220; dashboard/src/panels/review/ReviewSurface.tsx:210-210; dashboard/src/panels/review/ReviewSurface.tsx:624-624 |
| The one-sided diff engine, unchanged and reused: a split-mode CodeMirror diff over `before`/`after` with its own `diff-pane` host. | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-48; dashboard/src/panels/changeset/DiffPane.tsx:117-117 |
| The content viewer the unreadable-opposite path reuses, and its own test id. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:20-20; dashboard/src/panels/file-viewer/FilePane.tsx:49-49 |
| **The renderer cases: the addition and the removal assert the statement text in the real diff DOM, and the unreadable-opposite case asserts the viewer's content with no diff pane present.** | "draws an added invariant's full after statement beside an absent-before label"; "draws a removed invariant's full before statement beside an absent-after label"; "keeps the available text and claims no diff when the other side is unreadable" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:194-212; dashboard/src/panels/review/KnowledgeStatements.test.tsx:214-228; dashboard/src/panels/review/KnowledgeStatements.test.tsx:243-259 |
| **The renderer cases: the addition and the removal assert the statement text in the real diff DOM, and the unreadable-opposite case asserts `FilePane` content with no `diff-pane` present.** | "draws an added invariant's full after statement beside an absent-before label"; "draws a removed invariant's full before statement beside an absent-after label"; "keeps the available text and claims no diff when the other side is unreadable" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:194-212; dashboard/src/panels/review/KnowledgeStatements.test.tsx:214-228; dashboard/src/panels/review/KnowledgeStatements.test.tsx:243-259 |
| The case that a both-present area names no side, and the case that each of the three non-present states is carried through as its own token. | "keeps both statements when both sides recorded one, and names no side"; "renders a %s side as that state and never as another one" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:230-241; dashboard/src/panels/review/KnowledgeStatements.test.tsx:261-274 |
| The case that no subject compared renders two named states and neither pane. | "draws no diff and both named states when no subject was compared" | dashboard/src/panels/review/KnowledgeStatements.test.tsx:276-289 |
| **The server-side half of the same contract: the statement sides and the field rows these branches are a function of.** | `test_an_added_statement_renders_its_after_text_beside_a_named_absent_before`; `test_a_removed_statement_renders_its_before_text_beside_a_named_absent_after` | mcp/tests/test_knowledge_review_one_sided_statements.py:249-269; mcp/tests/test_knowledge_review_one_sided_statements.py:272-285 |
| The owner of the data half of this contract. | `side_content`; `side_conditions` | mcp/src/agents_remember/application/review_statement_sides.py:86-117; mcp/src/agents_remember/application/review_statement_sides.py:120-124 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The component renders one repository
namespace's records and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T23:13+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by this leaf's second curation pass.** the same anchor repair for the four case-title anchors this card carries: each backticked prose title became the case's exact `it(...)` title as a double-quoted literal inside the range that already held it. No claim was re-worded and no range changed. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout's metadata refresh owns the real one.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair, forced by this leaf's edit to a file this card cites — and the same test-name defect already recorded on the suite's own card.** This leaf changed `dashboard/src/panels/review/ReviewSurface.tsx` (462 → 549 lines: its inventory rows open into their content through the new `SourceContent.tsx`), which moved two constructs this card cites into that file, so the delegation row was re-derived (`ReviewSurface.tsx:179-201` → `182-205`). In the same pass, four rows that cite `KnowledgeStatements.test.tsx` by case were repaired: they named their case with a **backticked** test name, which the citation grammar refuses as an anchor (a several-word span is not identifier-shaped and must be written as a double-quoted literal), so each of those rows was a row with Source content and no anchor. Each now names the case's own name as the double-quoted literal the suite passes to `it`: `194-212`, `214-228`, `243-259`, `230-241`/`261-274` and `276-289`. No claim's meaning changed, no range moved except the two above, and `KnowledgeStatements.test.tsx` itself is **not** touched by this leaf (its bytes equal `d80a0513`'s). **Stamp accounting:** the verification pair still names `9043a82ec…` — the last real commit whose bytes this card's claims were verified against — and a `reviewedWorkingCandidate` row now states the candidate this repair was read in; nothing in this leaf is committed, so closeout owns the real stamp.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `KnowledgeStatements` repointed to dashboard/src/panels/review/KnowledgeStatements.tsx:93-118. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`):
  **created.** The component is new in this leaf and this is its one-to-one card. It records the four
  branches and the rule that decides them (a side's declared `state`, never its text), the one-sided
  diff with the named absent side above it and the drawn operand's own language, the
  available-content-with-reason path that draws no diff and claims no addition or removal, the
  neither-present task-context case, and the reused `DiffPane`/`FilePane` rather than a second diff
  engine. It also records the defect the component closes — the old two-present gate plus a
  `sideState` that returned null for the present side — because the state line and the data
  attributes are the readable evidence that the present-side statement is drawn. **Stamp
  accounting:** the verification pair names production line
  `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` — the leaf's base, and the last real commit the reading
  was taken against — because every construct this card cites exists only in this leaf's uncommitted
  candidate and no commit contains the bytes a stamp would claim to have verified.
  `reviewedWorkingCandidate` states what was actually read; closeout owns the stamp.
