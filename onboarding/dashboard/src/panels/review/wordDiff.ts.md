# dashboard/src/panels/review/wordDiff.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/wordDiff.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:18:53+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured. The requirement packets `MIK-R35@v1` and the adopted `ICR-R35@v1`,
and the leaf's rulings (`35_word-level-intent-diff.json`), live outside the code and memory repositories, so they are
named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of rules 1, 1a, 2, 3, 4 and 8. | "every byte of the text is in exactly one token"; "Nothing is normalized, trimmed or summarized." | dashboard/src/panels/review/wordDiff.ts:1-19 |
| The named rewrite ratio and the alignment bound. | "export const REWRITE_RATIO = 0.5;"; "export const DIFF_CELL_LIMIT = 2_000_000;" | dashboard/src/panels/review/wordDiff.ts:21-26 |
| The diff's parts and its three answers. | "export interface DiffPart {"; "export type TextDiff =" | dashboard/src/panels/review/wordDiff.ts:28-45 |
| Whitespace-preserving tokens. | "export function tokenize(text: string): string[] {" | dashboard/src/panels/review/wordDiff.ts:49-51 |
| The token LCS with prefix and suffix set aside, and the coarse fallback past the bound. | "function editScript("; "function middleScript(" | dashboard/src/panels/review/wordDiff.ts:67-85; dashboard/src/panels/review/wordDiff.ts:87-117 |
| A replaced phrase as one removed and one added run. | "function regions(parts: DiffPart[]): DiffPart[] {"; "function betweenChanges(" | dashboard/src/panels/review/wordDiff.ts:150-171; dashboard/src/panels/review/wordDiff.ts:174-178 |
| The decision: identical, whitespace-only with all whitespace removed (F3), or words with the ratio. | "export function textDiff(before: string, after: string): TextDiff {" | dashboard/src/panels/review/wordDiff.ts:180-206 |
| Exact reassembly of each side. | "export function sideText(" | dashboard/src/panels/review/wordDiff.ts:210-216 |
| Whitespace made visible and named. | "export function visibleWhitespace("; "export function describeWhitespace(" | dashboard/src/panels/review/wordDiff.ts:219-223; dashboard/src/panels/review/wordDiff.ts:226-242 |
| Rule 1a: LCS by exact text, moved items out before gap pairing, gaps paired only on equal counts. | "export function alignLists("; "function movedPairs("; "function gapRows(" | dashboard/src/panels/review/wordDiff.ts:258-280; dashboard/src/panels/review/wordDiff.ts:283-300; dashboard/src/panels/review/wordDiff.ts:302-330 |
| The renderer that draws it. | "export function IntentStatementBody({" | dashboard/src/panels/review/IntentWordDiff.tsx:559-613 |
| The unit cases. | "reassembles both exact texts from its parts, whatever the change"; "takes moved items out of the gaps before pairing, and pairs equal texts one to one" | dashboard/src/panels/review/wordDiff.test.ts:65-80; dashboard/src/panels/review/wordDiff.test.ts:200-213 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T13:18:53+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): created this card for the new pure module MIK-R35 adds, recording rulings Q2 (`REWRITE_RATIO = 0.5`, counting over the longer side, exactly 0.5 not a rewrite; 2026-09-30T11:53:13), Q5 (rule 1a as written), F3 (whitespace-only with all whitespace removed; 12:16:39) and the R2-2 note (12:43:15), plus one candidate invariant. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
