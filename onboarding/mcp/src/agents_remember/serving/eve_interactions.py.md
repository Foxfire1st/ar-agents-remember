# mcp/src/agents_remember/serving/eve_interactions.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The bounded pending-interaction queue for one eve session. eve pauses a run on `input.requested` and
resumes it only when the caller posts a structured `inputResponses` entry for the exact `requestId`
it raised, so those requests are the adapter's **only authority for answering a paused run**. They
are retained exactly, keyed by that id, and bounded.

## Code Commentary

### Logic

`EveInteractionQueue` is an `OrderedDict` of `PendingInteraction` keyed by eve's own `requestId`, with
a positive `limit` validated in `__post_init__`. `add_input_request` projects eve's strict request
schema (`requestId`, `kind`, `prompt`, `options`) into the AR `PendingInteraction` shape, defaulting
`kind` to `"input"`, `prompt` to the request id, and building both a flat `choices` tuple and a
structured `questions` page from the same option list. `add_authorization` retains one
`authorization.required` challenge under the deterministic id from `authorization_interaction_id`.

`head()` returns the oldest pending request, which is what `AdapterSnapshot.pending_interaction`
exposes singularly. `resolve(interaction_id)` drops one request and answers whether it was actually
pending, which is what lets a response for an already-answered or cancelled request be refused
locally instead of being forwarded.

### Conventions

- Every refusal is a `HarnessControlError` naming the id or the bound it hit.
- The queue is ordered, so `request_ids()` and `head()` are stable across reads.
- `raw` retains eve's own frame verbatim beside the projected AR fields.
- `Clock` is injected, so `created_at` is deterministic under test.

### Invariants And Boundaries

- **A duplicate `requestId` raises rather than overwriting.** eve raises each request once, so a
  repeat is a protocol divergence, not an update.
- **The bound is a refusal, not an eviction.** At `limit`, the excess request raises
  `"eve pending input queue reached its bounded limit"` instead of silently dropping an older
  request — dropping one would destroy the only authority for resuming that prompt.
- **Staleness is decided by eve, not here.** A response for a request that is no longer pending is
  refused locally, and eve itself treats an answered-or-cancelled request id as stale and never lets
  it authorize the earlier tool call. This module does not implement its own expiry.
- The projected `questions` page mirrors eve's option list one-for-one; it is a rendering projection
  and carries no authority of its own.
- `clear()` exists for session teardown and is the only path that discards pending requests without a
  resolution.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; eve's input-request schema is the external authority and is mirrored from the wire contract.

### Repo-Internal References

- The projected pending shape and the structured question page are AR's existing control-wire types, not eve-shaped types. [1]
- The mapper is the only writer: `input.requested` enqueues, `input.resolved` resolves, `authorization.*` retains and clears a challenge. [2]
- The mapper builds the strict `inputResponses` entry — an `optionId` when the response names one of the request's own choices, otherwise free text. [3]
- A pending request also refuses further ordinary delivery until it is answered. [4]
- Cases cover the request becoming a pending interaction, the response targeting it, and free text versus option ids with unknown ids refused. [5]

### Cross-Repo References

- eve's pause/resume contract — one `input.requested` answered by one exact `inputResponses` entry — is the published protocol this queue serves. [6]
