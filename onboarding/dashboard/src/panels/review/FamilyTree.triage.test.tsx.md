# dashboard/src/panels/review/FamilyTree.triage.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/FamilyTree.triage.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The family tree with change facts: badges, breakdown, order and `j`/`k` traversal (MIK-R33 rules 1 to 8), over the
store-authored comparison's served bodies** (`triage.family`, `triage.familyPage`, `triage.shared`) and, for the
dataset case, `familyReview.complete.captured.json`. The tree is the real component inside a reviewer keymap zone, with
a textarea, a contenteditable region and a PTY-zone control beside it. 18 cases.

## Code Commentary

### Logic

- **Change-kind badges (8):** every occurrence's delivered kind and marks and the family's guarantee badge; the shared
  member (`membership` where it joined, `unchanged` elsewhere); a reworded revision reads `intent` with the note beside
  a genuinely unchanged member (ruling 16:22:22 item 5); "why unknown" visible and in the node's description, never its
  name (R3-1); each fact once per node (the text note and the guarantee badge not repeated); an undescribed member reads
  `unknown` and says why (SYNTHETIC; mutation R-C2); an unknown guarantee says why (SYNTHETIC; mutation R-C10); a
  dataset review adds nothing (no badge, breakdown or controls; landed order).
- **Triage order (2):** changes first with unchanged siblings kept, the control switching to authored order and storing
  it; triage order when storage is unavailable (`readTreeOrder` over a throwing and an absent storage).
- **Next and previous change (5):** `j` from the top visits A, H, B, C, D, G and stays at the end with a polite "No
  later change…" and the selection scrolled into view; `k` walks back and lands on a revised member's first row; a
  filter showing only FAM-F00002 visits its guarantee row, then P, then F; past a partial family's returned members
  focus moves to the continuation control with the message, and the next `j` moves on; inert in the filter input, a
  textarea, contenteditable, the PTY zone, with ctrl, and outside the zone; registered with the keymap owner, listed for
  the `?` reference and rebindable to `N`.
- **One statement per fact on a member (3; merge round and R3-1, SYNTHETIC facts and scope over INV-GGGGGG):** the
  change kind, its reason, then the membership, each labelled; a followed marker's **Attribution unknown** on the
  membership line, drawn first, described after the kind, the name carrying no fact; MIK-L34's own note kept where no
  change facts are delivered (a dataset row), with the note as that row's description.

### Conventions

Vitest with Testing Library; `announcement` reads the computed accessible name and description the role query
computes; `press` fires keys at the focused element; SYNTHETIC facts and scopes are labelled in the case names.

### Invariants And Boundaries

Proves the candidate invariants recorded on `ChangeBadges.tsx.md` (each fact once per node) and `changeTriage.ts.md`
(siblings kept; traversal stops at, never loads, a continuation).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite's statement: the real tree inside a reviewer zone over the store-authored bodies. | "The tree is the real component inside a reviewer" | dashboard/src/panels/review/FamilyTree.triage.test.tsx:1-26 |
| The harness: the zone with a textarea, a contenteditable region and a terminal-zone control. | `Harness`; "data-kbzone=\"pty\"" | dashboard/src/panels/review/FamilyTree.triage.test.tsx:30-68 |
| Badges: kinds, marks, the shared member, the reworded revision, why unknown, one statement, undescribed members, the dataset review. | "never calls a reworded revision unchanged: intent, noted, beside a genuinely unchanged member"; "states each fact once per node: the text note and the guarantee badge are not repeated" | dashboard/src/panels/review/FamilyTree.triage.test.tsx:113-283 |
| Triage order and its control; triage when storage is unavailable. | "falls back to triage order when storage is unavailable" | dashboard/src/panels/review/FamilyTree.triage.test.tsx:285-329 |
| Traversal: displayed order, ends, filter, the partial-family stop, inertness, the keymap owner. | "visits every non-unchanged occurrence in displayed order and stays at either end"; "stops at the continuation control past the returned members of a partial family"; "is inert in text fields, contenteditable regions, the terminal zone and outside the reviewer" | dashboard/src/panels/review/FamilyTree.triage.test.tsx:331-468 |
| One statement per fact on a member, with and without a followed marker, and L34's note on a dataset row. | "puts a followed marker's Attribution unknown on the membership line, drawn first, described after the kind" | dashboard/src/panels/review/FamilyTree.triage.test.tsx:476-640 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new tree test (18 cases), recording rulings 2026-09-30T16:22:22 (items 5 and 9), 17:47:43 (review R1 F3's mutations; one statement per fact), the merge round and 21:55:02 (R3-1). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
