# mcp/src/agents_remember/serving/explainer.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The read side of the explainer page: `explainer_composition` wires the seat service, and the reads are assembled here from the frame store's retained revisions, the leaf's agreed number, grades and the moved-notice account, bound to the selected comparison. The HTTP handlers that serve those reads live in `serving/explainer_routes.py`, and no read here starts a model.

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
- History, message, request id and comparison number are validated before the seat is touched
- A Send against a comparison the leaf has left is refused with both numbers
- A planning leaf's comparison is built at the contract's line tips with nothing else substituted
- An unresolvable line falls back only to its fork base, never to the repository's HEAD
- Cancel reports whether a turn stopped and whether publication was prevented

- Comparison/evidence preparation rechecks operands; retained state carries its own claims and staleness; Update/Retire clear notices after service results; explicit removal and planned reads retain owner refusals; cancel preserves host uncertainty and measured revision equality. 

- Comparison/evidence preparation rechecks operands; retained state carries its own claims and staleness; Update/Retire clear notices after service results; explicit removal and planned reads retain owner refusals; cancel preserves host uncertainty and measured revision equality. [7]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/explainer.py:1104-1136 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/explainer.py:338-366 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/src/agents_remember/serving/explainer.py:403-476 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/src/agents_remember/serving/explainer.py:508-526 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/src/agents_remember/serving/explainer.py:1333-1364 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/src/agents_remember/serving/explainer.py::handle_cancel - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/explainer.py::handle_planned - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/explainer.py::handle_retire - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/explainer.py::handle_update - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/explainer.py::handle_remove_revisions - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/explainer.py::_prepare - the bytes it recorded now occur 6 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/explainer.py::_prepared_trees - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
