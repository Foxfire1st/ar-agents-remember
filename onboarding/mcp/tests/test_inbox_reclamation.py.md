# mcp/tests/test_inbox_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| ConfirmedGonePolicyTests and ReconcileAndCompactTests are implemented in this suite. | `ConfirmedGonePolicyTests`, `ReconcileAndCompactTests` | mcp/tests/test_inbox_reclamation.py:87-181; mcp/tests/test_inbox_reclamation.py:184-249 |
| The store transaction resolves and compacts the selected entries atomically. | `reconcile_and_compact` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:234-275 |
| The supervisor ordering places resolution/compaction before redelivery. | "redelivery" | mcp/src/agents_remember/kernel/_agentic_settings_sections.py:295-295 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer residual correction: bounded the class claim to
  `ConfirmedGonePolicyTests` and `ReconcileAndCompactTests` through their complete suite range.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
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
