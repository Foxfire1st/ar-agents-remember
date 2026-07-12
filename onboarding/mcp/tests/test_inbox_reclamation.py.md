# mcp/tests/test_inbox_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:40+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
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
deterministic without mutating the live coordination inbox.

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
| The regression classes and no-op event guard are implemented in this suite. | L81-L170; L185-L342 | [test_inbox_reclamation.py](agents-remember/mcp/tests/test_inbox_reclamation.py) |
| The tested transaction resolves and compacts before redelivery. | L346-L387 | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: created the new regression sidecar from the
  final reviewer PASS delta, including positive-gone, fail-closed, boundedness, race, retention,
  event-accuracy, and no-op-silence coverage. Verification metadata remains blank until commit.
