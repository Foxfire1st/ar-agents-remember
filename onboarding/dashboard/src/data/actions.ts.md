# dashboard/src/data/actions.ts

## Current A8 source account

The retained action client is `postAttentionDismiss`. Its input and JSON body contain only itemId and kind; it sends no lifecycle target or gateId. The literal same-origin route is /api/actions/dismiss. Only HTTP 202 returns dismissed; other statuses and fetch failures return error. It does not retry or mutate the store. AttentionQueue owns optimistic suppression and failed-result rollback.



- The current AttentionQueue caller uses suppressAttention before posting and releaseAttention for failed results; this is caller behavior, not an execution or server-authority claim. [5]





## Governing Overview

[data overview](overview.md)

## Purpose

The same-origin attention-dismiss POST client transports itemId and kind only. Server authority decides the effect; the caller owns its local display suppression.

## Code Commentary

### Logic





`postAttentionDismiss` POSTs {itemId, kind} to /api/actions/dismiss. Only 202 returns dismissed; a non-202 response or network throw returns error, without retry or store mutation.

### Invariants And Boundaries

The helper transports an identifier/kind pair, not a gate decision or lifecycle target. Server-side validation remains the authority; the client never reports success without HTTP 202.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References


- The attention queue that calls `postAttentionDismiss`. [3]


### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
