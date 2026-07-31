# mcp/tests/test_inbox_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:40+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp tests overview](../overview.md)

## Purpose

Focused regressions for confirmed-gone inbox reclamation, its same-sweep store transaction, and
the supervisor's aggregate observer event.

## Code Commentary

### Logic

The suite covers terminal catalog proof, compacted-tombstone plus one deduplicated tmux snapshot,
tmux presence and command failure retention, protected message kinds, subjectless/model-authored
exclusion, stale pending non-resurrection, consume authority, unchanged TTL fallback, persisted
folded-id removal counts, same-sweep compaction before redelivery, body-free aggregate events,
and silence across three no-op sweeps with a kept candidate.

### Conventions

Tests inject the tmux snapshotter and use temporary inbox roots so evidence and lock behavior are
deterministic without mutating the live coordination inbox. The shared `_inbox_entry` factory
builds each row through `create_operator_inbox_entry`'s parameter objects — `InboxMessage`
(carrying `ask`, `response`, `message_kind`, and an `InboxSubject`), `InboxRouting` wrapping an
`InboxAddress`, and `InboxPoster` — with `kind` typed as `InboxMessageKind`, so the protected-kind
and subjectless variants are spelled in the production vocabulary rather than through a cast.

### Invariants And Boundaries

- These are backend retention and supervisor regressions; they do not authorize live inbox,
  dashboard, task, or service mutation.
- The focused suite supplements, but does not replace, the manager-owned full repository gate.

### Todos

None. Reviewer residuals F3-F6 are follow-up implementation work, not missing L5 coverage.

## Docs References

No domain documentation is configured; the L5 task contract and production source are the direct
evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain source was available. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The regression classes and no-op event guard are implemented in this suite. | L87-L174; L189-L348 | [test_inbox_reclamation.py](agents-remember/mcp/tests/test_inbox_reclamation.py) |
| The tested transaction resolves and compacts before redelivery. | L362-L403 | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: recorded the inbox-entry parameter objects and
  re-anchored the self-citations. `_inbox_entry` now calls `create_operator_inbox_entry` with
  `InboxMessage` (holding `InboxSubject`), `InboxRouting` over `InboxAddress`, and `InboxPoster`,
  and its `kind` argument is typed `InboxMessageKind` so the former `# type: ignore[arg-type]` is
  gone; the Conventions paragraph now says so. The widened imports and two reflows moved the suite
  down six lines, so the Repo-Internal citation was corrected from L81-L170; L185-L342 to
  L87-L174; L189-L348, verified against the current class and test boundaries. No case was added,
  removed, or renamed. Verification metadata remains pinned until closeout.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: created the new regression sidecar from the
  final reviewer PASS delta, including positive-gone, fail-closed, boundedness, race, retention,
  event-accuracy, and no-op-silence coverage. Verification metadata remains blank until commit.
