# dashboard/src/panels/review/ExpressionCards.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R31's card-state and grouping cases (12), over the real served cards body.** The entries start from
`gitTrees.cards.captured.json` (the converted scratch leaf's 11 entries, provenance in
`gitTrees.capture-provenance.json`); each state a real leaf did not produce (unresolved, unavailable, missing
rationale, shared range, stale) is derived from a real entry with targeted, sometimes multi-field, test-only edits. The
payload the full-file read needs is `gitTrees.family.captured.json`'s. A small `Harness` holds the open path the way
the workspace does.

## Code Commentary

### Logic

- **Each card state (5):** a changed range is a diff and an unchanged range is shown once and labelled; an
  unresolved side shows its reason and never a guessed range or a diff; an unavailable side is labelled
  unavailable, distinct from a file absent on that side; a missing rationale is a named gap and no text is written;
  a proof entry shows its facet in place of a role and a rationale.
- **Grouping by (path, range) (4):** two regions of one file are two cards with their own rationale; members at the
  same path and range share one card, each with its own rationale; entries whose side did not resolve are never
  merged, and unchanged is counted apart from changed; the family order puts the selected member first.
- **Review fixes (3):**
  - F1: clicking **Full file** on the second of two cards of one path gives exactly one content block, inside that
    card, and exactly one source-content read; clicking again closes it.
  - F2: over the real walkFinal capture, the bounded family gives "These cards cover the loaded n of m members",
    and cardScope(complete) is asserted undefined; the rendered scope-line check uses the bounded family. R2-5 (in the same case): a family whose sides load disjoint members
    gives `loaded <= total`, with total 2.
  - F4: a stale after side renders "RLZ-D43E5CF2 stale on the after side" (`data-currentness=stale`), and a current
    entry shows no mark.

### Conventions

- Only `fetch` is stubbed (for the F1 read); other inputs start from captured bodies and include targeted multi-field derivations (identity, range, state, change and family-member populations).

### Invariants And Boundaries

- These cases prove the two candidate invariants recorded on `focusedCards.ts` and `ExpressionCards.tsx`: grouping
  with the rationale above the excerpt and a missing rationale shown as a gap; a bounded roster stating the loaded
  n of m. The reviewer's mutation checks (restoring `card.path === openPath`, removing `ScopeLine`, forcing
  `cardScope` undefined, suppressing `notCurrent`, dropping the unresolved key guard) each fail a case here.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` lives outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References


### Cross-Repo References

No cross-repo boundary is crossed by this file.

- The real bodies the entries start from.  Anchor: "const cardsBody = captured<ReviewTreesResult>('gitTrees.cards.captured.json');"; "captured<ReviewResult>('gitTrees.family.captured.json')" [1]
- Each card state.  Anchor: "draws a changed range as its real diff and an unchanged range once, labelled unchanged"; "shows an unresolved side with its reason and never a guessed range or a diff"; "labels an unavailable side unavailable, distinct from a file absent on that side"; "names a missing rationale as a gap and never writes text of its own"; "gives a proof entry its facet in place of a role and a rationale" [2]
- Grouping by (path, range) and the family order.  Anchor: "grouping by (path, range)" [3]
- The F1, F2 (with R2-5) and F4 cases.  Anchor: "opens one full file, in the card that asked, with one read (F1)"; "cover only the loaded members and points to the walk (F2)"; "marks an entry that is not current on its side with its MIK-R03 state (F4)" [4]
