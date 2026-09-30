# dashboard/src/panels/review/wordDiff.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/wordDiff.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:18:53+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The word diff's decisions, as unit cases (MIK-R35; 12 cases, no DOM):** tokens, marks, exact reconstruction,
whitespace-only, the rewrite ratio, the coarse bound and the list alignment of rule 1a. The texts are the real
INV-2TQGXFAX wording of the converted scratch leaf (`gitTrees.invariant.captured.json`), edited the way each case
describes.

## Code Commentary

### Logic

- **Tokens:** every byte is kept (words with their punctuation, whitespace runs as they are), and the tokens of the
  real statement join back to it.
- **A changed text field (5):** the conforming example ("is refused" → "is rejected and reported" marked in place
  within one sentence, 3 of 30 words changed, no rewrite); exact reassembly of both texts over seven pairs,
  including an empty side, reversal and a whitespace change beside a word change; a rewritten phrase as one removed
  and one added run; a whitespace change beside a word change kept as its own exact mark (with the glyph and
  wording helpers); and the byte decision — identical, whitespace-only (including `"a,b"` → `"a, b"` and
  `"answered, and"` → `"answered,and"`, review R1 F3), or words.
- **The rewrite ratio (2):** `REWRITE_RATIO` is `0.5`; 2 of 4 changed words is exactly the ratio and not a rewrite,
  3 of 4 is; an insertion counts against the longer side. A middle past `DIFF_CELL_LIMIT` (800 words replaced) is
  one removed and one added run, still exact.
- **Rule 1a (4):** inserted and removed items keep the aligned ones unchanged; a gap with equal counts pairs for a
  word diff, an unequal gap never pairs; a reordered item is `moved` and nothing is paired by position ("X,A,B"
  against "A,B,C"); moved items leave the gaps before pairing, and two equal moved texts pair one to one in order.

### Conventions

- Pure calls into `wordDiff.ts`; the `words` helper throws when a diff is not a word diff, so a wrong decision fails
  loudly.

### Invariants And Boundaries

- These cases pin rule 8 (exact reconstruction) and rule 1a's never-positional alignment. The worker's mutations M2
  (`>=` for the ratio), M3 (moved items left in the gaps) and M9 (no whitespace absorption) are caught by the focused
  suite this file belongs to, and G9 (whitespace-only decided by word sequence) fails this file's byte-decision case
  (worker report, `checks/l35-mutations.txt` and `checks/l35-fix-mutations.txt`).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1` live outside the
repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real wording the cases start from. | "gitTrees.invariant.captured.json"; "const STATEMENT =" | dashboard/src/panels/review/wordDiff.test.ts:1-20 |
| Tokens keep every byte. | "keeps every byte: words with their punctuation, and whitespace runs as they are" | dashboard/src/panels/review/wordDiff.test.ts:27-44 |
| The conforming example, exact reassembly, runs, whitespace marks and the byte decision (F3). | "marks the replaced words in place within one sentence (the conforming example)"; "reassembles both exact texts from its parts, whatever the change"; "decides by bytes: identical, whitespace only, or words" | dashboard/src/panels/review/wordDiff.test.ts:46-112 |
| The named ratio, exactly 0.5 not above it, and the coarse bound. | "is the named renderer constant 0.5, compared with changed words over the longer side"; "marks a middle too long to align as one removed and one added run, still exact" | dashboard/src/panels/review/wordDiff.test.ts:114-148 |
| Rule 1a: insertions, removals, equal-count pairing, moved items, never positional. | "describe('list alignment (rule 1a)'"; "shows a reordered item as moved, never pairing by position across the list" | dashboard/src/panels/review/wordDiff.test.ts:150-214 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T13:18:53+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): created this card for the new unit test module, recording ruling Q2 (the ratio constant and exactly 0.5 not a rewrite; 2026-09-30T11:53:13) and review R1 F3 (the whitespace-only cases; 12:16:39). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
