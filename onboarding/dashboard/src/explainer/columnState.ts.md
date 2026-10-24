# dashboard/src/explainer/columnState.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer column's state: what the column reads, the form it opens, what Send and Retire call, and the one frame target it keeps.

## Code Commentary

- An inactive column, or one without a leaf, reads nothing at all; an active one reads the state once and asks again only on Retry or while a build runs.
- A running build or an in-flight Send is re-read on a fixed dashboard cadence, and the interval clears as soon as neither holds.
- His words go out as they are: the route composes the references, their notes, the images and the text into the first turn once, so a reference-only Send carries no text.
- A Send posts once, keeps its request id until it is accepted, refuses a second press in flight, and on acceptance clears the picks, the text and the form.
- Retire keeps its receipt id while the retirement is unfinished, so a retry resumes the same receipt rather than starting another.

## Evidence

- A build and an in-flight Send are re-read on an interval that clears when both stop [1]
- A Send carries the text unchanged with the stale parts the form pre-filled [2]
- One call states the whole column: the read, the form, the rows, Send and Retire, and the frame target and shown chat [3]
