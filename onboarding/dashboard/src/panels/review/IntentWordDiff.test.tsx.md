# dashboard/src/panels/review/IntentWordDiff.test.tsx

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1`, the leaf's rulings
and the reviewer's probes (`notes/reports/260928-MIK-L35-review-R1-checks/`) live outside the repositories, so they
are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real bodies the cases start from, and the accessible-text reader. [1]
- The one-field successor, per-side rows and the tree or dataset scope. [2]
- The conforming example, condition-only, R2-1, list alignment and applicability cases. [3]
- Ruling Q4 on both paths, and the three F1 probes. [4]
- F4's cases and the same-revision label. [5]
- Whitespace-only, the rewrite and the preference. [6]
- One-sided, unavailable, ambiguous and dataset statements. [7]
- The family guarantee. [8]
- F2's labels: the navigator's guarantee and member tag, and the details fact. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
