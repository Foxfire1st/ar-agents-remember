# dashboard/src/explainer/FirstRequestForm.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The first request's form: the locked role capsule, the developer's references with their notes, the words, the fixed target and the Send press.

## Code Commentary

- The form composes nothing and sends nothing; the Send press belongs to the column, and the form only says what will go out.
- Send stays disabled while there is nothing to send and while a Send is in flight, when it reads Sending…; an empty message is allowed when references carry the request.
- Each reference shows the note it was added with and the × that removes it, and a form with none says a ⊕ on a block or an invariant adds the first.
- The capsule is marked as going with the first request only, and the target is fixed to a new explainer for the task.
- A refused Send names its step and keeps the request in the form for another press; a stale prefill names the parts and the count of stale grades.

## Evidence

- Send is refused while there is nothing to send and while a Send is in flight [1]
- The empty message is named as the end-to-end review rather than an error [2]
- With no reference the form says one ⊕ adds the first and later ⊕ clicks add more to the same form [3]
- The form says what sending does: it builds the workspace for the binding, then delivers the request as the first turn [4]
