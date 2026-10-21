# dashboard/src/panels/review/IntentWordDiff.tsx

## Governing Overview

[Review route overview](overview.md)

## Purpose

Render supplied statement, applicability, condition, exclusion and family-guarantee wording with semantic removal/addition marks, explicit one-sided states and the reader's wording-layout preference. Text segmentation and list alignment belong to `wordDiff.ts` and shared preparation; this module draws their results.

## Code Commentary

`TreeComparisonScope` exposes the supplied boolean; `IntentWordDiffScope` derives it from the payload token. The exported renderers consume their supplied shapes, rather than each enforcing a mode gate. `IntentStatementBody` prepares only changed fields and shares the prepared map between layout eligibility and drawing. A statement is prepared only when both sides are present; projected lists remain reported joined text, rather than an invented item alignment.

A prose passage renders identical text once, or a labelled whitespace-only after text plus both exact texts. Word passages use the local preference, with an inline-preferred rewrite shown side by side until the reader chooses Show inline for that current text pair. Semantic `del`/`ins` marks, strike/underline and hidden change announcements retain the non-colour distinction. Whitespace glyphs are hidden from assistive technology and described in words. The common prose style is now 0.83rem with line-height 1.7.

Each condition or exclusion is now one independently expandable line. `ListPassage` keeps a set of open row indices, `ItemLine` exposes a focusable button role and `aria-expanded`, and click, Enter or Space toggles that row in place. Closed lines ellipsize without removing their full text from the page; open lines wrap. Unchanged and moved content stays literal, with moved positions labelled; added/removed rows retain marks and applicable fallback-note descriptions.

Changed list pairs use `LinePassage`. Inline layout retains the word marks; side-by-side uses separate before/after halves, each ellipsized while closed. A rewrite's short visible `rewritten` tag retains its full reason for assistive technology and reveals the sentence on expansion. Once the rewrite row is open, Show inline is offered outside its line. This list-item override is local boolean state in that mounted changed-item component; it is not the NUL-separated text-pair token used by the ordinary prose passage.

`IntentStatementBody` now accepts its header. Compared content puts the header and eligible wording-layout control on the same wrapping line through `StatementHead`; added/removed content keeps the header before its one-sided prose. A non-present statement side is drawn by `KnowledgeStatements`, not diffed against an absent or unavailable side. Only actual `absent` marks a statement counterpart as known absent.

Guarantees compare supplied text even at the same revision. `GuaranteeTextChange` keeps the compact revision metadata, same-revision-text-differs note and word passage. It no longer renders its own Revision records disclosure: those raw identifiers belong to the page's Technical details owner. `OneSidedGuaranteeLabel` calls only `not_recorded` known absent; other side states stay qualified.

## Invariants And Boundaries

This is rendering and local interaction, not validation of arbitrary input objects or a fresh browser, accessibility or performance result. The current source diff adds the one-line list interactions and statement-header placement, changes prose metrics and removes the local guarantee-identifier disclosure. Shared passage preparation already existed in the captured base and is not newly introduced by this diff.

## Evidence

- The supplied comparison scope and payload-token wiring remain explicit. [19]
- The layout control delegates to the browser-local wording preference. [20]
- Semantic removal/addition marks retain hidden announcements and whitespace descriptions. [21]
- Prose draws same runs literally and filters the before/after sides from supplied parts. [22]
- Whitespace-only prose keeps after text and both exact whitespace-visible values. [23]
- Prepared or memoized diffs feed ordinary prose layout and a text-pair-local inline override. Ordinary prose passages render rewrite reason, coarse note and chosen inline/side-by-side layout. [24]
- Each prepared list row has its own open index, line control and applicable fallback description. [25]
- One-sided statement labels distinguish actual absence from unavailable or other supplied states. [26]
- Projected lists remain joined reported values; ordinary arrays and text use their respective rendering branches. [27]
- Statement rendering shares prepared values and keeps its supplied header beside eligible layout control. [28]
- Guarantee changes and facts compare supplied text, including differing text at the same revision. [29]
- The guarantee body retains compact revision metadata and its passage, without the removed Revision records disclosure. [30]
- Only not_recorded gives a known-absent one-sided guarantee label. [31]
- List-item lines retain before/after wording, rewrite reasons and the local open-row inline offer. [33]
- Each list item opens by click, Enter or Space, with its complete text retained and exposed by expansion. [34]
- Closed item lines ellipsize; opened lines and their side-by-side halves wrap, while rewrite reasons retain accessible full text. [35]
- Prose typography uses the supplied mockup metrics. [36]
- Shared preparation aligns only nonprojected arrays and prepares changed-pair diffs once for both layout eligibility and drawing. [32]

## Historical predecessor account

The following is preserved in full for provenance. It is superseded where it names old symbols, dataset/ambiguity boundaries, duplicate-computation timings or earlier candidate-invariant status; its prose reference numbers are inert. It makes no additional present-tense claim.

### dashboard/src/panels/review/IntentWordDiff.tsx

#### Governing Overview

[dashboard/src/panels route overview](../overview.md)

#### Purpose

**The word-level intent diff, drawn (MIK-R35, adopting ICR-R35@v1), and the tree-comparison scope every
intent label reads.** On a tree comparison (MIK-R25, the payload's `review:trees:<n>` token) a changed statement,
applicability, condition, exclusion or family guarantee reads as one prose passage with its removed and added words
marked in place, inside the decluttered structure of MIK-R31 rule 3, which it keeps (identical wording once,
one-sided statements as labelled prose). `wordDiff.ts` decides what is marked; this module renders it. A dataset
review keeps the landed rendering (ruling Q3).

#### Code Commentary

##### Logic

- **The scope (`TreeComparisonScope`, `IntentWordDiffScope`, `useTreeComparison`).** One React context says
  whether the renderers below read a tree comparison. `FamilyReviewCenter` sets it from its payload
  (`IntentWordDiffScope`, via `treeComparisonNumber`). The compact outline navigator no longer mounts a
  semantic word-diff scope. Only inside a true scope is intent wording
  word-diffed and does any label compare text bytes rather than revision identities.
- **Passages (rules 1, 3 and 4).** `TextPassage` renders one field: `identical` as plain prose, `whitespace_only` as
  `WhitespaceOnly` (the after text once, labelled "whitespace-only change", with both exact texts open,
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

##### Conventions

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


##### Invariants And Boundaries

- **Candidate invariant (not ingested): on tree comparisons, no review surface calls a changed text unchanged; the
  byte comparison decides, even at the same revision.** Realized here by `guaranteeTextChange`, `guaranteeFact` and
  the scope, with `textFirstComparison` (`statementWording.ts`), `SubjectReview.authoredSides`, and
  the reading area's guarantee/statement renderers. Same-revision differing-text comparisons remain a
  central reading concern; removed sidebar text-label tests are not current proof of compact navigation.
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

##### Todos

No additional work is asserted by this card.

#### Evidence

##### Docs References

No domain documentation source is configured. The requirement packets `MIK-R35@v1` and the adopted `ICR-R35@v1`,
the leaf's rulings (`35_word-level-intent-diff.json`: 11:53:13 Q1–Q6, 12:16:39 R1, 12:43:15 R2) and the evidence
folder `notes/reports/260928-MIK-L35-evidence/` (real-browser rounds r1–r3 over a converted scratch leaf) live
outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

##### Repo-Internal References

- The module's own statement of rules 1, 1a, 3, 4, 5 and 7, and the dataset boundary. (historical reference 1)
- IntentWordDiffScope gates the centre's semantic wording comparisons; the compact navigator no longer supplies a tree prop or renders full intent passages. (historical reference 2)
- The one layout control. (historical reference 3)
- A mark: struck or underlined, announced, whitespace as hidden glyphs with a closing space. (historical reference 4)
- Whitespace-only rendering with both exact texts open. (historical reference 5)
- One passage per changed field; the rewrite fallback, its reason and the unsaved "Show inline". (historical reference 6)
- Aligned lists, including moved items. (historical reference 7)
- The R06 indication: known absent, or a side that could not be read. (historical reference 8)
- A null field as known absence; a projected list shown as reported. (historical reference 9)
- The control only where a word-diffed passage is drawn (F5, R2-1). (historical reference 10)
- The statement area of a tree comparison's selected invariant. (historical reference 11)
- The guarantee's changed text, including one revision whose texts differ, and the details fact. (historical reference 12)
- The changed-guarantee block and the one-sided guarantee label. (historical reference 13)
- The reading-area FamilyReviewCenter owns the payload-bound word-diff scope, not the outline sidebar. (historical reference 14)

##### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Tree comparison scope gating every intent passage (historical reference 15)
- Word diff passages for changed authored text (historical reference 16)
- Statement text passages with layout and metadata (historical reference 17)
- Guarantee text change with compact revision metadata (historical reference 18)
