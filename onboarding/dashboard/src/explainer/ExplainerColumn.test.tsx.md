# dashboard/src/explainer/ExplainerColumn.test.tsx

## Governing Overview

[Route overview](../overview.md)

The directly mounted Operations-mode column follows the placeholder through Build to a live seat. A scripted agent-not-found followed by supported ready retries the selection in the same iframe. A separate matching-clear case closes the request form in this component fixture.

## Purpose

Specifies the review page's explainer column rule by rule: the selection, the placeholder that starts nothing, the form, the build, a Send aimed at an archived explainer, Retire, and that no model turn starts.

## Code Commentary

- The server is scripted and every request counted, so each case states what was read and what was posted.
- A closed column issues no request at all; an open one reads the state once and asks for no document chat, warmup or dispatch.
- The build cases assert the posted body, each step's mark and the whole percentage, and that the request goes out once.
- A refused build keeps the picks and the text, names the step and the server's reason, and reuses the same request id on the next press.
- The frame is asserted to be the same DOM node across menu selections, so choosing a chat never remounts it.
- A mid-build regression case holds `phase: 'building'` with a non-null mid-build identity for over 8 seconds and asserts zero `ar.open` messages while hidden, then exactly one `ar.open` on `live` in generation 1; the tray placement case also pins that `paseo-frame-agent-problem` Retry stays outside `TrayColumnDock` and posts nothing for archived notices.

## Evidence

- An open column reads the state once, posts nothing and reads no document chat, warmup or dispatch [1]
- A closed column issues no request at all [2]
- A Send with nothing to send is refused by the form and posts nothing
- The case `keeps his request when the build fails, and names the step` shows a refused build keeping the request and reusing its id [4]

- Retired at the fifth freeze d59c3493: dashboard/src/explainer/ExplainerColumn.test.tsx:365-377 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The directly mounted Operations-mode column follows the placeholder through Build to a live seat, retries transient agent-not-found on same-frame ready, and clears the request form on matching clear. [5]
- The mid-build regression case emits zero ar.open while building for > 8 s and exactly one on live, and the tray case pins Retry outside TrayColumnDock with zero POST on archived notices. [6]
