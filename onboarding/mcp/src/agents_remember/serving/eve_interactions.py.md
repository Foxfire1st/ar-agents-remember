# mcp/src/agents_remember/serving/eve_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/eve_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; eve's input-request schema is the external authority and is mirrored from the wire contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projected pending shape and the structured question page are AR's existing control-wire types, not eve-shaped types. | `PendingInteraction`; `InteractionQuestion`; `InteractionQuestionOption` | mcp/src/agents_remember/models/conversations/control_wire.py:1-200 |
| The mapper is the only writer: `input.requested` enqueues, `input.resolved` resolves, `authorization.*` retains and clears a challenge. | `EveEventMapper._interaction_requested`; `EveEventMapper._interaction_resolved`; `EveEventMapper._authorization_required` | mcp/src/agents_remember/serving/eve_events.py:379-435 |
| The mapper builds the strict `inputResponses` entry — an `optionId` when the response names one of the request's own choices, otherwise free text. | `EveEventMapper.response_payload` | mcp/src/agents_remember/serving/eve_events.py:205-220 |
| A pending request also refuses further ordinary delivery until it is answered. | `EveSessionAdapter.preflight_operation` | mcp/src/agents_remember/serving/eve_adapter.py:342-363 |
| Cases cover the request becoming a pending interaction, the response targeting it, and free text versus option ids with unknown ids refused. | `EveAdapterSubmissionTests` | mcp/tests/test_eve_adapter.py:371-603 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| eve's pause/resume contract — one `input.requested` answered by one exact `inputResponses` entry — is the published protocol this queue serves. | `INTERACTION_REQUEST_EVENT_TYPE`; `INTERACTION_RESOLVED_EVENT_TYPE` | mcp/src/agents_remember/serving/eve_protocol.py:59-63 |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **no content impact from the A2
  revision.** This file is byte-identical between the A1 and A2 candidates of the same change set, so
  the body is retained unchanged; the pass refreshed the verification metadata to the leaf's current
  base `e9300687` and rewrote all three citation tables into the `Finding | Anchor | Source` shape
  (identifier alone in Anchor, `path:start-end` plain in Source). No claim was re-worded and no hash or
  fingerprint was invented; the governed closeout stamps the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a file added by the native
  eve session-adapter change set. Records the duplicate-id refusal, the bounded-limit refusal over
  eviction, and the deliberate placement of staleness in eve rather than in this queue. Verification
  metadata is pinned to the leaf's base commit `67b21aeb` because the candidate is deliberately
  uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was
  invented here.
