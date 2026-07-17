# dashboard/src/panels/session-cockpit/QueuePreview.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/QueuePreview.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Renders the compact FEUI-L5 queue projection beside the shared composer using only server-
authoritative queued submission rows.

## Code Commentary

### Logic

The component derives its rows from the per-session reliable-submit store, shows bounded operator-
useful identity/state, and exposes no control of its own. Pop-back remains the composer's Alt+Up
action against the authority route; this view never mutates queue order or removes optimistic rows.

### Invariants And Boundaries

- Only authoritative queued rows render; locally sending, ambiguous, dispatching, withdrawn, and
  settled records are not represented as queued work.
- The preview does not reveal backend raw evidence or another source's private text.
- Empty queue is a normal absent projection, not proof that no adapter operation is active.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The shared composer mounts the preview and owns the Alt+Up action. | — | [../SessionComposer.tsx](../SessionComposer.tsx) |
| The lifecycle client hydrates only raw-free authoritative status rows. | — | [../../data/submissionLifecycleClient.ts](../../data/submissionLifecycleClient.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is a repository-local cockpit projection. | — | — |

## Update History

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; documented the read-only authoritative
  queue projection and its privacy/non-optimism boundary. Verification metadata remains pinned to
  the leaf base until closeout.
