# dashboard/src/panels/review/explainer/explainerApi.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The explanation view's routes and answers: state, revisions, update, removal, selective regeneration and the isolated frame's channel, read leniently enough to accept the spellings the chat column's client also reads.

## Code Commentary

- Reads are GETs on the leaf's own routes; the explicit Update, selective-regeneration and removal presses use POSTs. No read resumes, starts or generates anything.
- A non-JSON answer, a refused answer or an HTTP failure becomes a named refusal carried to the view, never an empty page.
- The parsers accept both spellings of the owner, the number, the seat and the stale list, so an answer one client accepts does not fail here.
- The frame is the host's existing isolated channel opened for an exact revision with that revision's own binding; an answer that names no page is a refusal rather than a session with holes.
- The planned read answers null for anything that is not a planned page, including a refusal, so the caller shows its own named problem.
- Removal posts the selector's own numbers and never filters the pinned revision here; the host refuses a pinned removal as well.

## Evidence

- A refused, non-JSON or failed answer becomes a named refusal instead of a parsed page [1]
- The state answer is read field by field, with the seat, the saved page, the stale record, the claims and the moved notice [2]
- Retained revisions keep their binding, time, kind, agreement, pin and removal receipt [3]
- The planned read answers null rather than a fabricated page when the route fails [4]
- A channel that does not name a page, its sandbox, its document and a script choice is refused [5]
- The revision's channel is opened with its binding, comparison and compare slot [6]
