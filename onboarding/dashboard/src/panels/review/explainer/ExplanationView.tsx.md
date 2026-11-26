# dashboard/src/panels/review/explainer/ExplanationView.tsx

## Governing Overview

[Route overview](../../overview.md)

Each saved or comparison frame uses the matching validated revision’s inventory, with same-revision saved explanation fields available before the revision rows arrive. An omitted inventory can supply a separate plain reason under that frame.

## Purpose

The Explanation reading body for the bound comparison: browser announcements and failures, first-request and build states, and retained revisions displayed in isolated frames.

## Code Commentary

- `ExplanationView` places a nonempty `statusLine` above `ExplanationBody`. `FrameMeta` supplies the standfirst, revision controls and header details; the right comparison slot omits controls and details.
- Without a last-render failure, `statusLine` returns `browserNotice.notice`, with or without a shown page. With a failure, it returns `failureLine` only when a revision is shown; otherwise it returns null and the empty-state component can display the failure. The failure line above a retained page calls that page an earlier revision rather than this request’s answer.
- `ExplanationBody` chooses the initial reading sentence, the unreadable card with Retry, a body without a revision, or the retained-revision body. Without a revision, an open request or failed build uses `ExplanationRequest`; a build with steps uses that request component, while a build without steps uses `BuildingPlaceholder`.
- `SingleSavedPage` renders one `RevisionFrame` with its caption, binding, staleness props and `FrameMeta`, followed by `RetiredNotice`.
- Comparison renders two `CompareColumn` components, each with its own merged revision state, caption, binding and staleness props. `SavedPage` adds one retirement notice after the pair.
- The surrounding review switch, tree and chat stay outside this reading body, and it never rebinds silently: Update names the comparison on screen, and regeneration either sends once to a live seat or opens the prefilled first-request form.
- Judgment chips and `Ungraded (n)` headings are mounted into the reading cards' DOM outside React, and cleanup removes exactly what was created.

The empty panel offers an end-to-end explanation. It also describes the optional grades that can order the review tree.

## Evidence

- An unreadable answer names its reason and offers Retry instead of an empty page [3]

- A chosen or compared revision's own state is read on demand, not taken from the page's default [5]
- Judgment chips and ungraded headings are added to reading cards and removed on cleanup [6]


- The panel draws one line for the browser sentence, read from the state. [7]
- The failure line names the page below an earlier revision rather than the answer to this request. [8]

- With no page, the empty block names what is missing and the command. [10]




- The body chooses the initial reading sentence, unreadable card, body without a revision, or retained-revision body. [1]
- A saved page renders one revision frame and its FrameMeta, then a plain inventory omission reason if present and any retirement notice. [4]
- A last-render failure is omitted from the top-level line without a shown revision; absent a failure, the pending browser announcement can appear with or without a page. [9]

- The empty view describes the end-to-end explanation and optional grades and exposes an explicit Ask action. [2]
