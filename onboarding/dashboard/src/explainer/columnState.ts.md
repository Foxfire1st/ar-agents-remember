# dashboard/src/explainer/columnState.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer column's state: what the column reads, the form it opens, what Send and Retire call, and the one frame target it keeps.

## Code Commentary

- The active leaf column reads state and subscribes to explainer changes. A running build, in-flight Send or bounded delivery follow can keep polling active. A failed Send enters this follow only while the state has not named a build. The follow deadline stops reads inside the timer callback, while effect cleanup clears the timer. Explicit Retry can request another read.
- The requester’s words go out as written: the route composes the references, their notes, the images and the text into the first turn once, so a reference-only Send carries no text.
- A Send posts once, keeps its request id until it is accepted, refuses a second press in flight, and on acceptance clears the picks, the text and the form.
- Retire keeps its receipt id while the retirement is unfinished, so a retry resumes the same receipt rather than starting another.
- `computeFrameTarget` returns `null` whenever `showFrame` is false (no non-explainer row selected; phase `placeholder`, `first-request`, `building`, or `retired`), so `useExplainerColumn` never exposes a frame target while the frame is hidden; when a non-explainer row is explicitly selected from the header menu, `showFrame` (`Boolean(selectedRow) || phase === 'live' || phase === 'closed'`) is true and `computeFrameTarget` returns that selected row's target.

## Evidence


- The active leaf column reads state and subscribes to explainer changes. A running build, in-flight Send or bounded delivery follow can keep polling active. A failed Send enters this follow only while the state has not named a build. The follow deadline stops reads inside the timer callback, while effect cleanup clears the timer. Explicit Retry can request another read. [1]

- A Send carries the text unchanged with the stale parts the form pre-filled [2]

- One call states the whole column (read, form, rows, Send, Retire, shown chat) and computeFrameTarget gates frameTarget on showFrame (Boolean(selectedRow) || phase === 'live' || phase === 'closed'), returning null whenever showFrame is false (no non-explainer row selected; phase placeholder, first-request, building, or retired). [3]
