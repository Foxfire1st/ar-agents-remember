# dashboard/src/panels/review/wordDiff.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Pure string/list alignment for intent-wording presentation. The renderer and prepared-passage owner
consume these outputs; this module reads no store and changes no recorded text or revision choice.
Current classification is token-sensitive, and current list alignment has a real cell-budget fallback.
The previous all-whitespace-stripped and unbounded-list accounts below are historical, not the
current algorithm or an unqualified candidate invariant.

## Code Commentary

Tokenization preserves each supplied JavaScript string as runs of whitespace/non-whitespace, with
punctuation attached. Exact strings are identical. Unequal strings are whitespace-only only when
their ordered non-whitespace token arrays match; splitting a word or joining must not into mustnot
is a word change, not invisible whitespace normalization. This is not locale-aware segmentation or
raw-file byte decoding. CJK runs and zero-width-space handling follow the actual regex.

Text diff removes an exact common prefix/suffix, aligns the middle by token LCS with removal-first
ties, and groups replacement runs and shared whitespace without changing either supplied string.
Above the declared cell limit the middle is one removed and one added run with coarse metadata.
sideText rebuilds before/after from same plus the appropriate changes. The rewrite ratio is the
longer side's non-unchanged words over its word count; only greater than0.5 triggers rewrite.

List alignment first checks the whole list-product cell budget. Above it every supplied item remains
an ordered removed/added row with cell_limit; a common middle or matching position is not guessed
as a pair. Within budget exact-text LCS anchors and one-to-one moved-item queues precede gap pairing.
Remaining equal-sized gaps pair in order; unequal gaps remain removed/added with unpaired_gap.
The prepared-passage/renderer owners propagate and show those reasons; this module does not draw
controls or certify a latency, memory-allocation or installed rendering budget.

## Invariants And Boundaries

Presentation conserves supplied string/list content; it does not adjudicate meaning. A cell-table
bound is not a bound on total output size or every allocation. The old card's whitespace-joining
example, Infinity call and not-ingested-candidate wording are retained only as prior account.
The changed token/budget guards and their actual stored cases are examined independently; source
inspection and parser spans are not fresh test, CODE or whole-MEMORY acceptance.

<details>
<summary>Historical prior account — retained, not the current contract</summary>

# dashboard/src/panels/review/wordDiff.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The pure half of the word-level intent diff (MIK-R35, adopting ICR-R35@v1).** It decides what a changed authored
text field marks, with no rendering: whitespace-preserving word tokens, the token diff and its removed and added
runs, the identical / whitespace-only / words decision, the rewrite ratio, and the rule 1a alignment of ordered
lists (conditions, exclusions). `IntentWordDiff.tsx` draws what it decides. It holds no state and reads no store.

## Code Commentary

### Logic

- **Tokens (rule 2).** `tokenize` splits a text into runs of non-whitespace (a word with its punctuation attached)
  and runs of whitespace, so every byte is in exactly one token and the tokens concatenate back to the text.
- **The diff.** `editScript` sets the common prefix and suffix aside, then aligns the middle by a token LCS
  (`middleScript` over `lcsTable`, a `Uint16Array` or `Uint32Array` table). Where two scripts are equally long a
  removal is taken before an addition. `merged` joins adjacent parts of one kind, and `regions` makes a replaced
  phrase read as one removed run followed by one added run: whitespace kept **between two changes**
  (`betweenChanges`) joins the region on both sides, while each side's own sequence is untouched.
- **The bound.** When the middle's table would exceed `DIFF_CELL_LIMIT` (2,000,000 cells), the middle is marked as one
  removed run and one added run (`coarse: true`). The texts stay exact; only the marking is coarser, and the passage
  says so.
- **The decision (`textDiff`).** Equal strings are `identical` (rule 1: text differs means byte inequality). Texts
  that are equal once **all** their whitespace is removed are `whitespace_only` (rule 3; review R1 F3, ruled
  2026-09-30T12:16:39). This includes a space inserted into or removed from a word, such as `"a,b"` → `"a, b"`.
  Everything else is `words`, with its parts, `changedWords`, `longerWords`, `ratio` and `rewrite`.
- **The rewrite ratio (rule 4; ruling Q2, 2026-09-30T11:53:13).** `REWRITE_RATIO = 0.5` is the named renderer
  constant. The changed words are the words of the longer side that are not unchanged (`max(removed, added)` words;
  whitespace runs are not counted), so the ratio lies in [0, 1]. A passage is a rewrite only when the ratio is
  **above** the constant: exactly 0.5 is not a rewrite.
- **Truth (rule 8).** `sideText` reassembles the before text from the `same` and `removed` parts and the after text
  from the `same` and `added` parts, byte for byte. Nothing is normalized, trimmed or summarized.
- **Whitespace shown and announced.** `visibleWhitespace` draws spaces, tabs, line breaks and carriage returns as
  glyphs (`·`, `→`, `↵`, `␍`, `␣`) for the whitespace-only disclosure and for a whitespace mark;
  `describeWhitespace` names them in words ("2 spaces, 1 line break") for assistive technology.
- **List alignment (rule 1a, `alignLists`).** Items are aligned by exact text, never by position across the whole
  list: (1) the LCS of items is `unchanged`; (2) an item outside it whose exact text also occurs outside it on the
  other side is `moved`, equal texts paired one to one in order (`movedPairs`), and moved items leave the gaps before
  any gap is paired; (3) in each gap between aligned items the remaining items pair in order as `changed` (and are
  word-diffed) only when the gap holds as many on each side, otherwise they are `removed` and `added` (`gapRows`).
  Lists are always aligned exactly, whatever their length (`editScript(..., Infinity)`), because a coarse script
  would pair items by position.

### Conventions

- Pure functions and exported types only (`DiffPart`, `TextDiff`, `ListRow`); positions in `ListRow` are 0-based.
- The two constants are exported so the tests assert them (`REWRITE_RATIO` in both test files).

### Invariants And Boundaries

- **Candidate invariant (not ingested): a changed intent field reads as one passage with removed and added words
  marked in place, and both texts are reconstructed byte for byte.** Realized by `textDiff` and `regions` here and
  `TextPassage` in `IntentWordDiff.tsx`; proved by `wordDiff.test.ts` (the exact-reassembly case over seven pairs,
  including the coarse case) and the accessible-text cases of `IntentWordDiff.test.tsx`.
- The diff is presentation only: it never changes stored text or revision selection (packet Exclusions).
- Limits that follow from rule 2 as written (review R1 note 6): CJK text without spaces is one token, so any edit
  reads as a full rewrite, and a zero-width space (U+200B) is not whitespace. A whitespace deletion that joins two
  words ("must not" → "mustnot") is labelled whitespace-only with both exact texts disclosed (review R2-2, accepted
  as a note at 2026-09-30T12:43:15).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured. The requirement packets `MIK-R35@v1` and the adopted `ICR-R35@v1`,
and the leaf's rulings (`35_word-level-intent-diff.json`), live outside the code and memory repositories, so they are
named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of rules 1, 1a, 2, 3, 4 and 8. (historical reference 1)
- The named rewrite ratio and the alignment bound. (historical reference 2)
- The diff's parts and its three answers. (historical reference 3)
- Whitespace-preserving tokens. (historical reference 4)
- The token LCS with prefix and suffix set aside, and the coarse fallback past the bound. (historical reference 5)
- A replaced phrase as one removed and one added run. (historical reference 6)
- The decision: identical, whitespace-only with all whitespace removed (F3), or words with the ratio. (historical reference 7)
- Exact reassembly of each side. (historical reference 8)
- Whitespace made visible and named. (historical reference 9)
- Rule 1a: LCS by exact text, moved items out before gap pairing, gaps paired only on equal counts. (historical reference 10)
- The renderer that draws it. (historical reference 11)
- The unit cases. (historical reference 12)

### Cross-Repo References

No cross-repo boundary is crossed by this file.

</details>

## Evidence

No Domain Documentation entries are configured. Current owner/caller and stored assertions provide
source evidence, not a new execution result.

- The current pure diff owner preserves supplied string sequences, classifies whitespace by ordered non-whitespace tokens and states its coarse-alignment boundary. [1]
- Rewrite ratio is the named0.5 constant and the dynamic-programming alignment cell limit is2,000,000, not a total rendering budget. [2]
- Diff parts carry exact strings and the result distinguishes identical, whitespace-only and words with coarse/ratio metadata. [3]
- Tokenization retains whitespace/non-whitespace runs and the whitespace predicate uses its declared JavaScript regex. [4]
- Token LCS sets aside exact common prefix/suffix and marks an over-cell-limit middle as one removed and one added run. [5]
- Changed regions group removed/added runs and shared whitespace between changes without normalizing the side strings. [6]
- Whitespace-only requires identical ordered non-whitespace tokens; joining/splitting a word reaches words, with changed-word ratio and strict rewrite threshold. [7]
- sideText rebuilds each supplied string from same plus its own change runs; this API does not claim raw-file byte decoding preservation. [8]
- Whitespace is rendered as visible glyphs and counted descriptive names without changing the supplied text. [9]
- Within the cell bound, exact-text LCS/move pairing precedes gap pairing; over budget or unequal gaps produce explicit removed/added rows with reasons. [10]

- The actual statement renderer consumes prepared text/list passages and names coarse/unpaired reasons without moving diff computation into this pure module. [11]

- Stored assertions cover exact string reassembly, token-boundary changes, coarse middle/list bounds and duplicate move pairing; these are inspected cases, not fresh execution. [12]
