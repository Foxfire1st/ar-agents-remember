# dashboard/src/panels/knowledge-reader/readerParts.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/knowledge-reader/readerParts.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The shared pieces of the knowledge reader (MIK-R29): navigation links, state badges, a decision in full, and
onboarding prose whose `[n]` markers link to their resolved references.** Every link here is a navigation: it
changes the reader's address (and so the URL), never local state (rule 5).

## Code Commentary

### Logic

- **Navigation.** `ReaderNavContext` carries the repository, memory tree and `go`; `useReaderNav` refuses to
  render a link outside the reader. `RecordLink` opens a record's truth view (a target the tree does not hold
  shows "(not in this tree)"), `PathLink` a path view, and `CodeLink` the code view at an anchor's locator
  (`codeAddress`). `TargetLink` picks the right one for any link or reference end: code or test, route, record,
  or another target (a requirement is named by ID, version and packet).
- **Entries.** `EntryRow` shows an entry's ID, kind, MIK-R03 state, role, its code link at the locator, the
  facet for a proof, the rationale and the state's reason.
- **A decision in full (the rule carried from L13).** `DecisionCard` shows the derived status as the badge (and
  the stored status when it differs, "(recorded …)"), the context, every alternative in order with its status,
  reason, `reconsider when` and the targets it reopens on (`AlternativeItem`), what it supersedes and is
  superseded by, and what it governs. An unreadable decision is named (`Unavailable`).
- **Prose with references (ruling 2026-09-30T09:42:58, F4).** `ProseWithReferences` renders the onboarding
  Markdown with `remarkReferenceMarkers`, a remark plugin that links `[n]` only in **text nodes** of the parsed
  Markdown: a code span or fenced block holds its text in `value` and is never rewritten, and an existing link's
  text is skipped. A marker with a known reference number becomes a button that highlights and scrolls to that
  reference; `ReferenceList` lists every reference with **every** target. Absent prose is said as such;
  unavailable prose or references are named.

### Conventions

- `StateBadge` tones states (current, stale, unverifiable, superseded and so on) through `BADGE_TONE`.
- Panda CSS owns the looks.

### Invariants And Boundaries

- **Rule 5: every link is a navigation.** Nothing here keeps view state except the focused reference.
- **A decision is shown whole wherever it appears** (the rule carried from L13): every view that shows a
  decision uses `DecisionCard`.
- Proved by `KnowledgeReader.test.tsx`: the file case (six markers, reference 2 lists 3 targets, the decision in
  full), the directory case (superseded-by link), and the code-span case (`reports[0]` and a fenced
  `candidates[3]` kept, only [1] and [2] linked); the reviewer's mutant that also rewrites code nodes was killed.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: every link is a navigation. | "Every link is a navigation: it changes the reader's address" | dashboard/src/panels/knowledge-reader/readerParts.tsx:1-4 |
| The navigation context. | `ReaderNav`; `ReaderNavContext`; `useReaderNav` | dashboard/src/panels/knowledge-reader/readerParts.tsx:24-36 |
| A part that could not be read, named. | `Unavailable` | dashboard/src/panels/knowledge-reader/readerParts.tsx:169-175 |
| Record, path and code links. | `RecordLink`; `PathLink`; `CodeLink` | dashboard/src/panels/knowledge-reader/readerParts.tsx:177-199; dashboard/src/panels/knowledge-reader/readerParts.tsx:201-214; dashboard/src/panels/knowledge-reader/readerParts.tsx:216-230 |
| Any link or reference end, as a navigation. | `TargetLink` | dashboard/src/panels/knowledge-reader/readerParts.tsx:259-266 |
| One entry with its state and code link. | `EntryRow` | dashboard/src/panels/knowledge-reader/readerParts.tsx:270-302 |
| An alternative with its reason and `reconsider when`; the decision header with the derived status. | `AlternativeItem`; `DecisionHeader` | dashboard/src/panels/knowledge-reader/readerParts.tsx:304-324; dashboard/src/panels/knowledge-reader/readerParts.tsx:346-358 |
| A decision in full, wherever it appears. | `DecisionCard` | dashboard/src/panels/knowledge-reader/readerParts.tsx:361-389 |
| Markers linked in text nodes only (F4). | `splitMarkers`; `linkMarkers`; `remarkReferenceMarkers` | dashboard/src/panels/knowledge-reader/readerParts.tsx:409-424; dashboard/src/panels/knowledge-reader/readerParts.tsx:426-435; dashboard/src/panels/knowledge-reader/readerParts.tsx:438-440 |
| The reference list and the prose with its markers. | `ReferenceList`; `ProseWithReferences` | dashboard/src/panels/knowledge-reader/readerParts.tsx:442-474; dashboard/src/panels/knowledge-reader/readerParts.tsx:477-534 |
| The file case and the code-span case. | "opens a file with its prose, resolved references, entries, families and linked records"; "links [n] markers in prose text only, never inside code spans or fences" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:118-155; dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:400-416 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new shared parts MIK-R29 adds, recording the carried L13 rule (a decision in full wherever it appears) and ruling 09:42:58 F4 (markers never rewritten inside code spans or fences). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
