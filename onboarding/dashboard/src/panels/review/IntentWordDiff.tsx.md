# dashboard/src/panels/review/IntentWordDiff.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The word-level intent diff, drawn (MIK-R35, adopting ICR-R35@v1), and the tree-comparison scope every
intent label reads.** On a tree comparison (MIK-R25, the payload's `review:trees:<n>` token) a changed statement,
applicability, condition, exclusion or family guarantee reads as one prose passage with its removed and added words
marked in place, inside the decluttered structure of MIK-R31 rule 3, which it keeps (identical wording once,
one-sided statements as labelled prose). `wordDiff.ts` decides what is marked; this module renders it. A dataset
review keeps the landed rendering (ruling Q3).

## Code Commentary

### Logic

- **The scope (`TreeComparisonScope`, `IntentWordDiffScope`, `useTreeComparison`).** One React context says
  whether the renderers below read a tree comparison. `FamilyReviewCenter` sets it from its payload
  (`IntentWordDiffScope`, via `treeComparisonNumber`), and `FamilyTree` from its `tree` prop, because the family
  navigator is mounted by the workspace outside the centre (review R1 F2). Only inside a true scope is intent wording
  word-diffed and does any label compare text bytes rather than revision identities.
- **Passages (rules 1, 3 and 4).** `TextPassage` renders one field: `identical` as plain prose, `whitespace_only` as
  `WhitespaceOnly` (the after text once, labelled "whitespace-only change", with a disclosure of both exact texts,
  whitespace made visible), and `words` as `Prose` inline or `SideBySide`. A rewrite (above `REWRITE_RATIO`) is
  shown side by side even when the preference is inline and says why ("Mostly rewritten: n of m words changed
  (p%), above the 50% rewrite ratio…"); its **"Show inline"** applies to that passage only, is not saved, and resets
  when the texts change (ruling Q2). A coarse diff says that the changed region was too long to align word by word.
- **Marks (rule 7).** `Mark` draws a removal as `<del>` (struck) and an addition as `<ins>` (underlined), each with
  visually hidden ` removed: ` / ` added: ` text, so the marks never depend on colour. A whitespace run is drawn as
  glyphs hidden from assistive technology and announced in words, **with a closing space** so the announcement never
  runs into the next word (the accessibility bug the F4 tests exposed; guarded by mutation G12).
- **Lists (rule 1a).** `ListPassage` renders `alignLists`: unchanged items plain, a `changed` pair as its own
  `TextPassage`, a `moved` item tagged "moved from item i to item j", and removed or added items as a mark with a
  tag.
- **One side (rule 5).** `OneSidedLine` carries the R06 indication: "added in after — before: known absent" /
  "removed in after — after: known absent" only when the other side is a known absence; a side that could not be read
  reads "recorded on the \<side\> side only — \<other\>: \<state\>, not known absent (\<detail\>)". `OneSidedStatement`
  renders an added or removed statement as that line plus labelled prose; when the present side is not present it
  falls back to `KnowledgeStatements`. `FieldBody` treats a `null` field on one side as the record's known absence
  (the worker's interpretation 4, pinned by review F4's X11 case). No diff is ever drawn against an absent or unavailable
  side.
- **Projected lists.** A list the comparison only reported joined (`projected`, from `SubjectReview.authoredSides`
  when a side had no member row and the `exclusions` field row answered) is shown as reported, "before: … · after:
  …", never aligned, because aligning a joined string would invent list items (F4's X13 case).
- **The statement area (`IntentStatementBody`).** Added and removed selections render `OneSidedStatement`. A
  compared selection renders the statement (`StatementText`: a `TextPassage` when the statement changed and both
  sides are present, else the prose once, else each side's own state line through `KnowledgeStatements`) and one
  `intent-field-change` section per other changed field. Ambiguous and unresolved selections never reach here:
  `SelectedStatement` keeps the landed "no statement diff" body for them (rule 6 as substituted).
- **The layout control (rule 4; review R1 F5, R2-1).** `ProseLayoutControl` switches every passage between inline
  and side by side through `intentDiffPreference.ts`. It is offered only where a word-diffed passage is drawn
  (`offersLayout`, `drawsPassage`, `wordsPassage`): never for an identical or whitespace-only text, a one-sided
  field, moved, added or removed items, or a projected list; for a list, only when a paired item's diff is `words`.
  The guarantee offers it only when its own diff is `words`.
- **The guarantee.** `guaranteeTextChange` answers the before and after guarantees whenever both exist and their
  text differs, **including one revision whose two texts differ** (MIK-R21 increments `revision` only when meaning
  changes; ruling Q1), else `null` so the landed block answers. `GuaranteeTextChange` renders "Changed guarantee ·
  revision a → b" (for one revision, "revision r2 → r2 · the same revision on both sides; its text differs"), the
  passage in the landed guarantee card, and both revision IDs under "Revision records". `OneSidedGuaranteeLabel` says
  "Added guarantee" / "Removed guarantee" with the known-absent line only when the other side is `not_recorded`,
  else "Guarantee recorded on one side only". `guaranteeFact` gives the centre details
  `same_revision_text_changed` instead of `unchanged_revision` on a tree comparison when one revision's texts
  differ (review R1 F2).

### Conventions

- Styling uses `styled-system/css` module constants, like the other review renderers; the removal and addition
  fills are `DiffPane`'s own colours, and the line (strike or underline) is what tells them apart.
- Test ids are the contract: `intent-diff` (with `data-field` and `data-layout`), `intent-diff-inline`,
  `intent-diff-side-by-side`, `intent-diff-before` / `-after`, `intent-diff-whitespace-only` and its label, text and
  exact-text ids, `intent-diff-rewrite`, `intent-diff-coarse`, `intent-diff-list` (items carry `data-item`),
  `intent-one-sided` (`data-known`), `intent-field-change`, `intent-field-projected`,
  `intent-diff-layout-control` / `intent-diff-layout`, and `review-center-guarantee-changed`
  (`data-word-diff="true"`).
- `offersLayout` and `drawsPassage` compute `textDiff` / `alignLists` a second time beside the passages' memoized
  diffs; this is bounded (about 12 ms at the cell limit) and has no functional effect (review R2-3, accepted as a
  note at 2026-09-30T12:43:15).
- The file is 699 lines, under the 1,200 bound.

### Invariants And Boundaries

- **Candidate invariant (not ingested): on tree comparisons, no review surface calls a changed text unchanged; the
  byte comparison decides, even at the same revision.** Realized here by `guaranteeTextChange`, `guaranteeFact` and
  the scope, with `textFirstComparison` (`statementWording.ts`), `SubjectReview.authoredSides`, and
  `FamilyTree.guaranteesOf` / `memberSideTag`. Proved by the "labels of one revision whose texts differ" and F1 probe
  cases of `IntentWordDiff.test.tsx`, and the same-revision guarantee case of `ReviewSurface.wordDiff.test.tsx`
  (centre label, rail notes and details fact); the reviewer's R2 grep found no remaining tree-path "unchanged" label
  that is not byte-gated.
- **Candidate invariant (not ingested): a changed intent field reads as one passage with removed and added words
  marked in place, and both texts are reconstructed byte for byte.** Realized by `TextPassage` and `Mark` over
  `wordDiff.textDiff`; proved by the accessible-text assertions here and `wordDiff.test.ts`'s reassembly case.
- **Candidate invariant (not ingested): dataset reviews get no word diff.** Realized by the scope (false without
  `review:trees:<n>`); proved by the dataset cases of `IntentWordDiff.test.tsx` and `ReviewSurface.wordDiff.test.tsx`
  (the guarantee keeps its `DiffPane`, "Joint guarantee · unchanged" stays).
- The text shown is exactly the recorded text (rule 8): nothing here normalizes, trims or summarizes it.
- Out of scope, as ruled (Q6): the family roster in the centre (`FamilyMemberContext`) still lists each member
  revision's statement separately; it is a roster, not a compared-statement renderer, and carries no "unchanged"
  label.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured. The requirement packets `MIK-R35@v1` and the adopted `ICR-R35@v1`,
the leaf's rulings (`35_word-level-intent-diff.json`: 11:53:13 Q1–Q6, 12:16:39 R1, 12:43:15 R2) and the evidence
folder `notes/reports/260928-MIK-L35-evidence/` (real-browser rounds r1–r3 over a converted scratch leaf) live
outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of rules 1, 1a, 3, 4, 5 and 7, and the dataset boundary. [1]
- The tree-comparison scope the centre and the navigator set. [2]
- The one layout control. [3]
- A mark: struck or underlined, announced, whitespace as hidden glyphs with a closing space. [4]
- Whitespace-only rendering with both exact texts disclosed. [5]
- One passage per changed field; the rewrite fallback, its reason and the unsaved "Show inline". [6]
- Aligned lists, including moved items. [7]
- The R06 indication: known absent, or a side that could not be read. [8]
- A null field as known absence; a projected list shown as reported. [9]
- The control only where a word-diffed passage is drawn (F5, R2-1). [10]
- The statement area of a tree comparison's selected invariant. [11]
- The guarantee's changed text, including one revision whose texts differ, and the details fact. [12]
- The changed-guarantee block and the one-sided guarantee label. [13]
- Where the centre and the navigator set the scope. [14]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
