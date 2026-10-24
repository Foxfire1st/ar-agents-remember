# dashboard/src/explainer/ExplainerColumn.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specifies the review page's explainer column rule by rule: the selection, the placeholder that starts nothing, the form, the build, a Send aimed at an archived explainer, Retire, and that no model turn starts.

## Code Commentary

- The server is scripted and every request counted, so each case states what was read and what was posted.
- A closed column issues no request at all; an open one reads the state once and asks for no document chat, warmup or dispatch.
- The build cases assert the posted body, each step's mark and the whole percentage, and that the request goes out once.
- A refused build keeps the picks and the text, names the step and the server's reason, and reuses the same request id on the next press.
- The frame is asserted to be the same DOM node across menu selections, so choosing a chat never remounts it.

## Evidence

- An open column reads the state once, posts nothing and reads no document chat, warmup or dispatch [1]
- A closed column issues no request at all [2]
- A Send with nothing to send is refused by the form and posts nothing [3]
- The case `keeps his request when the build fails, and names the step` shows a refused build keeping the request and reusing its id [4]
