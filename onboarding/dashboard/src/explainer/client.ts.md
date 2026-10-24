# dashboard/src/explainer/client.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer's four routes as the dashboard reads and posts them: one state read and the Send, Update and Retire presses, each answer parsed into the shape the column draws.

## Code Commentary

- Every answer the dashboard cannot read becomes an unavailable read with a sentence, or a refusal with a reason and the server's detail; nothing here throws at the page.
- Parsing accepts the host's several spellings: a seat word or a seat record, an owner under kind, owner or comparison_owner, a build under build or building, snake_case retire receipts.
- An archived or retired seat reads as no seat, while an unrecognised seat word makes the whole read unavailable rather than guessing.
- A build request id and a retire receipt id are single-segment identifiers, so a retry can reuse the exact same one.
- Nothing here starts a model turn: the state route is a read, and the three posts exist only for a press the developer made.

## Evidence

- Two addresses are the same only when repository, master and leaf all match [1]
- Revisions parse into rows, dropping any row without a revision number or a binding [2]
- A Send posts once, carrying the text, the picks, the planned flag and the stale ids [3]
- An update posts the same body shape as a build, differing only in what it carries [4]
- A refused Retire returns its reason and detail instead of throwing, and a parsed one carries both counts and what remains [5]
