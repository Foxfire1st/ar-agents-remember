# dashboard/src/panels/review/explainer/ExplanationSwitch.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The top line's Review | Explanation control: it opens the explainer's page in the reading column, and its own label reports that a build is running, how many parts are stale, or that the explainer is retired.

## Code Commentary

- It belongs to the page's top line, outside the page it switches to, and it reads no state: the counts arrive as props from the page's single read.
- `explanationMarks` builds the label's suffix, and a build mark outranks the stale count of the page the build will replace.
- Both tabs are real tabs: `aria-selected` states which view is shown, and the explanation tab's title explains either the build or the page.
- Pressing either tab only reports a switch to its caller; nothing here fetches, starts a build or resumes anything.
- Every label fact is optional, so a caller holding no read still renders the plain control.

## Evidence

- A build mark outranks the stale count, and retirement adds its own word to the label [1]
- Both tabs report the shown view, and the explanation tab carries the stale, building and retired facts [2]
- The label's three facts are optional props, so the plain control renders without a read [3]
