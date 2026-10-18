# dashboard/src/panels/review/IntentWordDiff.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render supplied intent wording and family guarantees as readable passages, with removal/addition marks, explicit one-sided states and local layout choices. `wordDiff.ts` owns segmentation/alignment; `intent-passage/model.ts` prepares shared text/list results; this module draws them. The complete previous account is retained below as historical, not as an active dataset-review API or current performance measurement.

## Code Commentary

### Scope and prepared values

`TreeComparisonScope` exposes a supplied boolean. `IntentWordDiffScope` derives it from the payload’s parsed tree-comparison token, and `useTreeComparison` reads it. This is context wiring for callers, not an internal precondition enforced by every exported renderer. In particular, current `guaranteeFact(entry)` no longer accepts the old `tree` boolean: a same-revision guarantee whose text differs gets `same_revision_text_changed` whenever that helper is called.

`IntentStatementBody` builds a memoized map only for fields named by changed wording. A statement is prepared only when both supplied statement sides are present. Other fields go through `preparePassage`, including the projected flag. The same prepared map supplies layout eligibility and drawing; the old `offersLayout`/`drawsPassage`/`wordsPassage` recomputation path is gone. Do not carry the earlier duplicate-computation timing note into the current account.

`preparePassage` computes a text diff for two strings, or list alignment for two arrays only when not projected. Changed list pairs carry their own prepared text diffs. `passageHasWords` checks those results, so identical/whitespace-only/projected/one-sided data does not manufacture a word-layout control.

### Drawing and layout

- `IntentTextPassage` uses a supplied diff or memoizes `textDiff(before, after)`, then delegates to `TextPassageBody`. Identical text appears once. Whitespace-only changes show the after text plus both exact texts with visible whitespace.
- A word passage uses the browser-local prose preference. An inline-preferred rewrite falls back to side-by-side with the actual rewrite reason; **Show inline** records this passage’s current NUL-separated text-pair token in local React state. This is neither persisted preference nor a global cache or proof that arbitrary text-pair encodings cannot collide.
- `Prose` preserves same runs and draws changed runs through `Mark`. A removal uses `del`/strike and an addition `ins`/underline, plus visually hidden change announcements. Whitespace glyphs are hidden from assistive technology and announced in words with a separating space. Side-by-side filters added runs from Before and removed runs from After.
- `ListPassage` consumes prepared rows; it no longer performs alignment itself. Unchanged rows stay plain, changed pairs use their prepared passage, moved rows name their original/new positions, and added/removed rows use marks. Cell-limit and unpaired-gap notes are displayed and linked to applicable added/removed rows with `aria-describedby`.
- Projected array fields are joined and labelled as supplied, not aligned into invented items. Two strings use a passage; the remaining field branch emits its known-one-sided label and selected supplied value. This is the literal consumed-shape branch, not a general validator of arbitrary objects.

### Statement and guarantee boundaries

`StatementText` falls back to `KnowledgeStatements` whenever either statement side is not present; it does not diff against an unavailable/absent side. Added/removed selections use `OneSidedStatement`: its counterpart is called known absent only when that side’s state is `absent`; otherwise its actual state/detail is named. Other selection routing belongs to the caller; this function itself branches explicitly on added/removed and the supplied wording, rather than implementing a removed ambiguous-state protocol.

`guaranteeTextChange` needs both guarantees and differing supplied joint-guarantee strings, not different revision identities. `GuaranteeTextChange` shows revision metadata, a same-revision-text-differs note when applicable, the passage with layout offered for words, and a revision-record disclosure. `OneSidedGuaranteeLabel` treats only `not_recorded` as known absence; unreadable/other states retain a qualified label.

### Changes and limits

Actual BASE/current source adds shared passage preparation, optional prepared diffs, accessible list notes and the exported passage wrapper, and removes the tree parameter from `guaranteeFact`. These are changes, not comment-only preservation. This card does not certify every caller’s routing, algorithmic byte reassembly, a newly executed accessibility/viewport test, or a timing/performance result. It changes no typed invariant or original producer list.

## Evidence

No domain documentation source is configured. Findings below cite the actual renderer and preparation owner. Historical packets/rulings in the retained account are provenance, not a fresh execution grade.

- Supplied tree-comparison context and payload-token wiring. [19]
- Browser-local layout control delegates the selected preference. [20]
- Removal/addition and whitespace announcements are rendered with semantic marks. [21]
- Same runs and side-filtered Before/After prose preserve the supplied parts. [22]
- Whitespace-only output includes the after text and both exact whitespace-visible texts. [23]
- Prepared or memoized text diffs flow into local layout, rewrite and coarse rendering. [24]
- Prepared list rows, fallback notes and described-by links are rendered together. [25]
- One-sided statements distinguish known absence from supplied non-present states. [26]
- Projected lists and string/remaining field branches consume the actual supplied shapes. [27]
- Present-side checks and shared prepared-map layout/drawing belong to the statement renderer. [28]
- Guarantee text comparison and the current one-argument fact helper compare supplied text. [29]
- Changed guarantees preserve revision metadata and word-passage layout controls. [30]
- Only not_recorded gives the known-absent one-sided guarantee label. [31]
- Shared preparation aligns nonprojected arrays and prepares changed-pair diffs for both layout and drawing. [32]

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
