# dashboard/src/panels/detail-panel/entryState.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/detail-panel/entryState.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:06:50+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The **brief-state-plus-disclosure** pattern the task entry's controls share (ICR-R16 at the entry, leaf
`260921-ICR-L47`). A refusal or an unrecorded range is answered, never swallowed, but printing the
owner's whole paragraph inside and beside every entry control turned the task header into a wall of
backend prose. So a control carries a one- or two-word state, and the full explanation sits in a
`<details>` disclosure beside it.

## Code Commentary

### Logic

- `EntryStateDetails({ testId, label, children })` renders a closed `<details>` whose `<summary>` is a
  `?` with the accessible name `"<label>: details"`, and a paragraph body. It sits **outside** the
  button, because interactive content inside a button is not a disclosure a keyboard can open.
- `briefProblem(problem)` maps the shared `ReviewFailure.token` to the brief word: `not-initialized` →
  `no knowledge yet`, `network` → `offline`, `unreadable` → `unreadable`, `not-found` → `not found`,
  anything else → `unavailable`.
- `problemSentence(problem)` is the whole explanation in the owner's words: `<code>: <detail>`, then
  `offending input: …` and `next: …` only when published, joined with ` — `.

### Conventions

Styles `entryStateDetails`, `entryStateSummary`, `entryStateBody` come from `./styles`. The token is the
shared classification, so the entry and the review surface cannot call the same code two different things.

### Invariants And Boundaries

- Nothing is invented: absent `offendingInput`/`nextAction` are omitted, not filled.
- The disclosure is closed by default; a control never prints the paragraph inline.
- Used by both `IntentReviewEntry` and the change-set controls in `changeSetBar.tsx`.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Why the pattern exists, and why the disclosure is outside the button. | "interactive content inside a button" | dashboard/src/panels/detail-panel/entryState.tsx:1-7 |
| The closed disclosure with its accessible summary. | `EntryStateDetails`; "details" | dashboard/src/panels/detail-panel/entryState.tsx:13-31 |
| The brief word per shared token. | `briefProblem`; "no knowledge yet"; "offline" | dashboard/src/panels/detail-panel/entryState.tsx:35-48 |
| The owner's full sentence, with nothing invented. | `problemSentence`; "offending input: " | dashboard/src/panels/detail-panel/entryState.tsx:52-60 |
| The disclosure styles. | `entryStateDetails`; `entryStateSummary`; `entryStateBody` | dashboard/src/panels/detail-panel/styles.ts:175-202 |
| The two consumers. | `EntryStateDetails`; `briefProblem`; `problemSentence` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:24-80; dashboard/src/panels/detail-panel/changeSetBar.tsx:185-259 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the shared brief-state and disclosure helpers (`ICR-R24@v3`, ICR-R16 at the entry). The verification pair names the code base; closeout owns the real stamp.
