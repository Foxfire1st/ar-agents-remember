# dashboard/src/panels/review/IntentWordDiff.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/IntentWordDiff.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:18:53+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R35's rendering cases (30), with accessible-text assertions.** The knowledge pane and member rows start from
the real served invariant review of the converted scratch leaf (`gitTrees.invariant.captured.json`, a tree
comparison `review:trees:1`), and the family cases from `gitTrees.family.captured.json`; `review()` derives the
second revision by changing exactly the field each case is about, as `statementWording.test.tsx` does, and mounts
the real `SelectedStatement` inside `IntentWordDiffScope`. Assertions read what assistive technology reads
(`spoken`: visually hidden announcements included, `aria-hidden` glyphs excluded), not only the styling.

## Code Commentary

### Logic

- **A tree comparison statement (19):**
  - the statement marked in place in one passage, read as "…links is removed: refused added: rejected and reported
    with…", with `<del>` / `<ins>` elements and no `diff-pane`;
  - a condition-only revision: the changed condition marked in place and the statement once;
  - R2-1: a paired condition whose only change is whitespace offers no layout control;
  - conditions and exclusions aligned by exact text (unchanged, moved, added, removed), with no control;
  - a changed applicability as its own passage;
  - **ruling Q4:** only the selected revisions' field rows are read, on tree and dataset reviews alike (another
    record's `applicability` row is ignored, the subject's own row is read);
  - **review R1 F1**, three probe cases: one revision whose texts differ when the after row is not on the page, the
    before row is not on the page, or the member is listed on the after side only (moved in, wording touched) —
    each reads "Changed statement · revision r2 → r2 · the same revision on both sides; its text differs", no
    "unchanged" testid, and the marked comma;
  - F4's X9/X10: one revision with identical text reads "Statement unchanged · same recorded revision", with or
    without rows;
  - F4's X11: an applicability recorded on one side only reads as a known absence, with no diff and no control;
  - F4's X13: a list the comparison only reported joined is shown as reported, never aligned;
  - F4's X19: a whitespace change inside a changed passage is drawn as `·` / `··` and announced "removed: 1 space
    added: 2 spaces";
  - "Wording unchanged" kept for a new revision whose every field is identical;
  - the same revision with different text diffed and labelled (ruling Q1);
  - the boundary example: a trailing space renders once as "whitespace-only change" with both exact texts disclosed;
  - a rewrite shown side by side with its reason, and "Show inline" switching that passage;
  - the toggle switching every passage and writing `review.intent-diff.layout.v1`;
  - inline when storage throws on read, and a throwing `setItem` still switching.
- **One-sided, unavailable and ambiguous statements (4):** added and removed statements with the known-absent line;
  an unreadable side named as unreadable and never diffed against; no diff for an ambiguous or unresolved selection;
  a dataset review keeping the landed rendering (its `diff-pane`, no passage, no control).
- **The family guarantee (4):** a changed guarantee word-diffed with compact revision metadata and a control; one
  revision with different text diffed (and `guaranteeTextChange` null for identical text or a missing side); no
  control for a whitespace-only guarantee; a one-sided guarantee labelled a known absence only when the other side is
  `not_recorded`.
- **Labels of one revision whose texts differ (3; review R1 F2):** the navigator's joint guarantee shows both texts
  ("Joint guarantee · before · same revision, text differs") on a tree comparison and stays "Joint guarantee ·
  unchanged" for a dataset or identical text; the member tag reads "· same revision · text differs", "· same
  revision" (a side's content not on the page) or "· unchanged revision" (dataset, identical); the centre details'
  fact is `same_revision_text_changed` only on a tree comparison.

### Conventions

- `afterEach` resets the preference store to inline and clears `localStorage`, so no case leaks its layout.
- The successor revision id and the display versions `r2`/`r3` are the derivation's own values; the `rows` option
  shapes the member rows per side (`MemberSides`) or `'none'` so the pane and its field rows answer.

### Invariants And Boundaries

- These cases prove the three candidate invariants recorded on `IntentWordDiff.tsx.md` at unit level, and the one on
  `SubjectReview.tsx.md` (each side's text only from that side's own row, or from its pane or filtered field rows).
  Every mutation the worker ran (M1–M11, R1–R2, G1–G12) and the reviewer's R1 survivors (X9–X11, X13, X19) are
  caught by the focused suite (this file, `wordDiff.test.ts` and `ReviewSurface.wordDiff.test.tsx`); the reviewer's
  Y12, the one R2 survivor, fails the R2-1 case here.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1`, the leaf's rulings
and the reviewer's probes (`notes/reports/260928-MIK-L35-review-R1-checks/`) live outside the repositories, so they
are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The real bodies the cases start from, and the accessible-text reader. | "const payload = captured('gitTrees.invariant.captured.json');"; "function spoken(node: Node): string {" | dashboard/src/panels/review/IntentWordDiff.test.tsx:33-63 |
| The one-field successor, per-side rows and the tree or dataset scope. | "function review(change: Partial<ReviewFamilyMember> = {}, options: Options = {}) {" | dashboard/src/panels/review/IntentWordDiff.test.tsx:65-113 |
| The conforming example, condition-only, R2-1, list alignment and applicability cases. | "marks the changed words of the statement in place, in one passage"; "offers no layout control when a paired condition changed only its whitespace" | dashboard/src/panels/review/IntentWordDiff.test.tsx:118-198 |
| Ruling Q4 on both paths, and the three F1 probes. | "reads only the selected revisions' field rows, on tree and dataset reviews alike"; "diffs one revision whose texts differ when %s" | dashboard/src/panels/review/IntentWordDiff.test.tsx:200-264 |
| F4's cases and the same-revision label. | "labels an applicability recorded on one side only as a known absence, with no diff"; "shows a list the comparison only reported joined as reported, never aligned"; "diffs one revision whose text differs between the two sides, and says so" | dashboard/src/panels/review/IntentWordDiff.test.tsx:266-349 |
| Whitespace-only, the rewrite and the preference. | "renders a whitespace-only change once, labelled, with both exact texts disclosed"; "shows a rewrite side by side by default, says why, and can still show it inline" | dashboard/src/panels/review/IntentWordDiff.test.tsx:351-422 |
| One-sided, unavailable, ambiguous and dataset statements. | "describe('one-sided, unavailable and ambiguous statements'" | dashboard/src/panels/review/IntentWordDiff.test.tsx:424-505 |
| The family guarantee. | "describe('the family guarantee'" | dashboard/src/panels/review/IntentWordDiff.test.tsx:507-580 |
| F2's labels: the navigator's guarantee and member tag, and the details fact. | "describe('labels of one revision whose texts differ'" | dashboard/src/panels/review/IntentWordDiff.test.tsx:582-655 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T13:18:53+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): created this card for the new test module (30 cases), recording rulings Q1, Q2, Q3 and Q4 (2026-09-30T11:53:13), review R1 F1 (the three probes), F2 (the labels), F3, F4 (X9–X11, X13, X19) and F5 (12:16:39), and R2-1's added case (12:43:15). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
