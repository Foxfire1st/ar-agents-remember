# mcp/src/agents_remember/serving/explainer.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The explainer's HTTP routes on the review page — build, Send, Update, Retire, cancel, state, stale, revisions, removal and planned — as transport over one composed seat service.

## Code Commentary

- `explainer_composition` answers an unwired composition when either the comparison owner or the wiring is missing, and every route then refuses `explainer-unavailable` with a 503: a page that cannot build, update or retire says so instead of serving an empty one.
- Reads start no model; the state payload is assembled from the frame store's retained revisions, the leaf's agreed number, the grades, their staleness and the moved-notice account.
- A Send names the comparison it was composed against, and a leaf that has moved on is refused `comparison-moved` with both numbers and a refresh flag rather than being answered against a different comparison.
- A planning leaf binds the master line's tips instead of a recorded comparison: the line's own tip wins even after its fork base advances, the base engages only while the line holds no commit, and the repository's HEAD is never substituted.
- Validation sits at the edge: history is one of live, recorded or planned, a comparison number is a non-negative integer, a message and a request id are bounded, a receipt id must be one file name, and a removal names between one and 1024 integers.
- Cancel measures the frame store's ready revision around the host's named cancel, so a turn that raced publication is reported truthfully and the last ready revision is kept.

Packet preparation uses the injected comparison/evidence ports, carries the bound owner/reference and document/supplemental receipts, and rechecks a planned tip binding before it prepares; movement or missing required sources refuses instead of preparing different operands. State reads select the retained on-screen revision and expose its binding, parts, claims, grade/part staleness, carried hunks, agreed revision and task byte usage. The explicit seat record keeps agent id and generation null before an identity exists.

Update and Retire clear the leaf's process-local moved notice only after their service call returns; counts that cannot be measured remain marked unavailable. Revision removal admits a nonempty list of at most 1024 integers (excluding booleans) through the injected frame-store owner, returns exact removed/remaining/pinned/bytes-freed facts and preserves its named refusal. Planned GET requires a planning leaf, a resolved contract and the canonical leaf document. Cancel returns the exact host outcome, including uncertainty, and reports only whether the ready revision stayed equal around that act as `publicationPrevented`; equality does not erase an already-published revision.

## Evidence

- A process that cannot compose the seat service refuses every route by name [1]
- History, message, request id and comparison number are validated before the seat is touched [2]
- A Send against a comparison the leaf has left is refused with both numbers [3]
- A planning leaf's comparison is built at the contract's line tips with nothing else substituted [4]
- An unresolvable line falls back only to its fork base, never to the repository's HEAD [5]
- Cancel reports whether a turn stopped and whether publication was prevented [6]

- Comparison/evidence preparation rechecks operands; retained state carries its own claims and staleness; Update/Retire clear notices after service results; explicit removal and planned reads retain owner refusals; cancel preserves host uncertainty and measured revision equality. [7]
