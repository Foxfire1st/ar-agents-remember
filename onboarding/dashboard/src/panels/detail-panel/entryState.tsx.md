# dashboard/src/panels/detail-panel/entryState.tsx

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

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- Why the pattern exists, and why the disclosure is outside the button. [1]
- The closed disclosure with its accessible summary. [2]
- The brief word per shared token. [3]
- The owner's full sentence, with nothing invented. [4]
- The disclosure styles. [5]
- The two consumers. [6]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
