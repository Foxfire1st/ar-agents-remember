# dashboard/src/panels/review/ExpressionCards.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Reading-block controls keep one explanation per authored entry, explicit unresolved state and stable CodeMirror drawings during layout rebuilds.

## Code Commentary

### Logic

- The harness now mounts ReviewBlockCard from the change-set model and captured entry data, rather than the removed ExpressionCards whole-file surface. Changed, unchanged, unresolved, unavailable and absent entries retain their explicit range/count/state distinctions; missing rationale has its exact named gap, and proof entries retain their role and facet.
- Two entries with the same invariant, path and range still draw two explanation cards and retain their separate rationales. Line labels open on click, Enter and Space, while a click within a text selection does not toggle the range.
- Changed split panes expose exactly 20 document lines per side in the supplied range and unchanged content exposes 27, with no added line for a terminal newline. A stale locator keeps its named label and leaves current source unmarked; no Full file control or source-content request is present.
- The actual rendered changed pane carries mint insertions, alarm removals, signed compact line counts and the supplied removed text. Split and unified selectors reach CodeMirror rows; spacer rows are hatched and changed rows have no outline box. A separately mounted general DiffPane does not receive the review-page-only removed-text rule.
- Rationale keeps the entry ID, invariant, role and exact supplied text together. Earlier rationale has its own Before line; revised-state text stays outside the cut text, full text is available in the title and no hidden disclosure owns the explanation.
- When split or inline rendering rebuilds a collapsed range, a MutationObserver-held last complete drawing keeps the prior editor markup, line counts and gutters until the replacement editor is actually drawn, then removes the held snapshot.

### Invariants And Boundaries

These declared component controls use captured entries plus explicitly edited states and inspect editor documents, DOM attributes and shipped selectors. They did not run here and do not measure browser geometry or independently certify the producer snapshot.

## Evidence

- Declared check and its fixture assertions. [6]
- Declared check and its fixture assertions. [7]
- Declared check and its fixture assertions. [8]
- Declared check and its fixture assertions. [9]
- Declared check and its fixture assertions. [10]
- Declared check and its fixture assertions. [11]
- Declared check and its fixture assertions. [12]
- Declared check and its fixture assertions. [13]
- Declared check and its fixture assertions. [14]
- Declared check and its fixture assertions. [15]
- Declared check and its fixture assertions. [16]
- Declared check and its fixture assertions. [17]
- Declared check and its fixture assertions. [18]
- Declared check and its fixture assertions. [19]
- Declared check and its fixture assertions. [20]
- Declared check and its fixture assertions. [21]
- Declared check and its fixture assertions. [22]
- Declared check and its fixture assertions. [23]
- Declared check and its fixture assertions. [24]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ExpressionCards.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> **MIK-R31's card-state and grouping cases, over the real served cards body.** The entries start from
> `gitTrees.cards.captured.json` (the converted scratch leaf's 11 entries, provenance in
> `gitTrees.capture-provenance.json`); each state a real leaf did not produce (unresolved, unavailable, missing
> rationale, shared range, stale) is derived from a real entry with targeted, sometimes multi-field, test-only edits. The
> payload the full-file read needs is `gitTrees.family.captured.json`'s. A small `Harness` holds the open path the way
> the workspace does.
>
> ## Code Commentary
>
> ### Logic
>
> - **Each card state (5):** a changed range is a diff and an unchanged range is shown once and labelled; an
>   unresolved side shows its reason and never a guessed range or a diff; an unavailable side is labelled
>   unavailable, distinct from a file absent on that side; a missing rationale is a named gap and no text is written;
>   a proof entry shows its facet in place of a role and a rationale.
> - **Grouping by (path, range) (4):** two regions of one file are two cards with their own rationale; members at the
>   same path and range share one card, each with its own rationale; entries whose side did not resolve are never
>   merged, and unchanged is counted apart from changed; the family order puts the selected member first.
> - **Review fixes:**
>   - F1: clicking **Full file** on the second of two cards of one path gives exactly one content block, inside that
>     card, and exactly one source-content read; clicking again closes it.
>   - F2: current truncated and complete captures separately supply the bounded and whole-roster controls. A disjoint-side derivation checks that the union genuinely exceeds the widest-side total while loaded never exceeds that total. A further case keeps loaded==total distinct from incomplete after content: name the unread/missing/unreadable side and never say "load the rest".
>   - F4: a stale after side renders "RLZ-D43E5CF2 stale on the after side" (`data-currentness=stale`), and a current
>     entry shows no mark.
>
> ### Conventions
>
> - Only `fetch` is stubbed (for the F1 read); other inputs start from captured bodies and include targeted multi-field derivations (identity, range, state, change and family-member populations).
>
> ### Invariants And Boundaries
>
> - These cases prove the two candidate invariants recorded on `focusedCards.ts` and `ExpressionCards.tsx`: grouping
>   with the rationale above the excerpt and a missing rationale shown as a gap; a bounded roster stating the loaded
>   n of m. The reviewer's mutation checks (restoring `card.path === openPath`, removing `ScopeLine`, forcing
>   `cardScope` undefined, suppressing `notCurrent`, dropping the unresolved key guard) each fail a case here.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R31@v1` lives outside the repositories.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
>
> - The real bodies the entries start from.  Anchor: "const cardsBody = captured<ReviewTreesResult>('gitTrees.cards.captured.json');"; "captured<ReviewResult>('gitTrees.family.captured.json')" (historical reference 1)
> - Each card state.  Anchor: "draws a changed range as its real diff and an unchanged range once, labelled unchanged"; "shows an unresolved side with its reason and never a guessed range or a diff"; "labels an unavailable side unavailable, distinct from a file absent on that side"; "names a missing rationale as a gap and never writes text of its own"; "gives a proof entry its facet in place of a role and a rationale" (historical reference 2)
> - Grouping by (path, range) and the family order.  Anchor: "grouping by (path, range)" (historical reference 3)
> - The F1, F2 (with R2-5) and F4 cases.  Anchor: "opens one full file, in the card that asked, with one read (F1)"; "cover only the loaded members and points to the walk (F2)"; "marks an entry that is not current on its side with its MIK-R03 state (F4)" (historical reference 4)
>
> - F2 uses separate bounded and complete captures, checks the disjoint-member union against the widest-side total, and distinguishes incomplete after content even when loaded equals total: identify the unread, missing or unreadable side without offering a false load-the-rest action. (historical reference 5)
