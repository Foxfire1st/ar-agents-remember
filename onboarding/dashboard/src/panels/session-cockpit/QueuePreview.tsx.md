# dashboard/src/panels/session-cockpit/QueuePreview.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/QueuePreview.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared composer mounts the preview and owns the Alt+Up action. | "withdrawing queued message…" | dashboard/src/panels/sessionComposerHooks.ts:143-143 |
| The lifecycle client hydrates only raw-free authoritative status rows. | "if (!isLifecycleState(state)) throw new Error(\"invalid submission status\");" | dashboard/src/data/submissionLifecycleClient.ts:217-217 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-local cockpit projection. | — | — |

## Current L5I Maintenance

The queue head can offer `steer` only when the active projection proves an interrupt capability and
a real working turn. Steering requests that exact-turn interrupt; it never withdraws, duplicates,
or locally reorders queued messages, so the server dispatches the same head after settlement.

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 2 citation claims; scoped result 0 findings.

- 2026-07-24T13:17:17Z — Curator: documented wire-evidenced queue steering and its no-local-queue-
  mutation boundary; verification fields remain pre-commit.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; documented the read-only authoritative
  queue projection and its privacy/non-optimism boundary. Verification metadata remains pinned to
  the leaf base until closeout.
