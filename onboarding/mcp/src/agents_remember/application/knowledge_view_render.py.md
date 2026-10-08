# mcp/src/agents_remember/application/knowledge_view_render.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Candidate selection and ordering for the five knowledge views. Final row projections live in `knowledge_view_rows.py`; both halves share this module's candidates, ordering and classification.

## Code Commentary

### Logic

Only declared ordering inputs are admitted. Candidates lacking an authored determination or registered mechanical rule are withheld with an unresolved limitation. Recorded identity supplies the stable tiebreak, never a guessed path, symbol or route ranking.

`authored_decision` reads the text decision's own `decider`, `reason` and canonical `outcome`. A silent decider may use the record's author reference; a non-canonical decimal outcome never becomes a priority. The retired typed `DecisionPayload` model is not a production dependency.

A single realization frontier supplies path-seeded source-context, invariant and family selections. No seed selects unrestricted content; a held path realized nowhere selects nothing rather than widening to all. Families and member locations follow recorded membership and retain the recorded role, path and locator.

### Invariants And Boundaries

Emitted candidates are classified authored or mechanical, never default-classed. The application seam admits the offset once and passes it to the row renderer; no second token parse or position-zero fallback exists. Retaining text decisions restores no canonical facet model or writer.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Everything this card asserts is checkable inside the shipped candidate: the module's own docstring and
constants, the two model modules it imports its vocabulary and provenance classes from, the reader port
it consumes, the seam that calls it, and the cases that protect its properties — the determinism
differential in one test file and the ordering-and-admission cases in the other. The design document the
renderer's docstring cites by path lives outside this code worktree, so it is quoted as the module's own
statement rather than cited as a file.

- The docstring that states the four properties together and the CR20-6 intake decision behind the authored side. [1]

- The text-decision reader consumes recorded fields and canonical outcome prefixes; the canonical facet payload type is retired. [3]

- The two generated-content rules the module classifies under: a recorded trigger identity and a payload byte-equality consequence. [4]
- The three generated-content rules the module classifies under: a recorded trigger identity, a payload byte-equality consequence, and the registered rule a membership-derived row names. [5]
- One authored determination read from a stored facet — the canonical-spelling rule that decides whether it is a priority at all, and the reader that turns one facet row into it with the envelope actor used only when the payload is silent. [6]
- The pre-classification working type and the ordering pass's outcome, both frozen dataclasses rather than models. [7]
- The declared key each admitted input produces (including the sentinel that orders an unprioritised row after every prioritised one and the rule that the priority is read from the candidate's own subject), and the exception that replaces a default order with its raise site and the two-member class closure the caller turns into a recorded limitation. [8]
- The total sort key ending in record identity and the registered rule ids an ordering touched. [9]
- The position that carries the class of the input, and the no-consequence statement built from either branch with its paging helper. [10]
- The attachment read that fetches a subject's own decisions, and the rule that only one declared position may order. [11]
- The per-view selection functions and the five renderers they feed, each returning rows with the limitations, the rule ids and the selection's own size. [12]
- The two projections that carry a row's recorded location into the response, the candidate builder each copies from rather than re-deriving, and the single decoder both share with the source-context view. [13]
- The renderer's own ordering-and-paging step with the token-tail offset recovery, and the two views that carry the classification fields and the queue shapes. [14]
- The queue row that separates a machine work item from an attributed curator disposition, with the disposition vocabulary version it states. [15]
- The four admitted ordering inputs and the closed two-member class set the module imports instead of re-declaring, the registry holding one ordering rule per admitted input, and the declared stable tiebreak every position must name. [16]
- The limitation record a withheld value becomes, the position shape, and the refusal of one subject at two positions. [17]
- The reader port the module reads through and the store-side reader that answers it, including the per-kind row cache. [18]
- The seam that calls the renderers, screens the ordering input before any read, and accounts withheld rows as unresolved references. [19]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A view renders over one reader port bound to one
repository namespace, every subject it emits is a store-local record identity or revision identity, and
no construct here reads a path prefix, a file extension or a repository location.

No meaningful cross-repo references found.
