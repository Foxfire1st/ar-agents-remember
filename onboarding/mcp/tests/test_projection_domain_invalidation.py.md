# mcp/tests/test_projection_domain_invalidation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_projection_domain_invalidation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Proves projection heartbeats and narrow watcher changes skip unrelated heavy readers while domain
replacement reclaims deleted rows.

## Code Commentary

### Logic

One regression instruments reader calls across full, heartbeat, and lifecycle-only refreshes.
Another runs task-domain replacement at two corpus sizes and verifies changed/new rows replace the
snapshot while deleted rows disappear. Together they pin both CPU scaling and bounded retention.

### Conventions

Two corpus sizes prevent a fixture-size-only optimization from satisfying the tests.

### Invariants And Boundaries

- Heartbeats do not enumerate heavy workspace domains.
- Lifecycle invalidation stays within lifecycle-dependent reads.
- Task refresh is a complete replacement, not an append-only cache.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Retained domain state under test. | `ProjectionInputState`, `ProjectionReaders`, `ProjectionRefresh` | mcp/src/agents_remember/serving/projections/projection_inputs.py:93-117; mcp/src/agents_remember/serving/projections/projection_inputs.py:178-186; mcp/src/agents_remember/serving/projections/projection_inputs.py:189-407 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:05:00+02:00 — Curator W3-B02 repaired 1 Repo-Internal citation row, resolving 2 manifest findings with exact retained-state and invalidation anchors; verification metadata was preserved.
- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 collapsed
  `ProjectionInputState.read`'s loose arguments into two parameter objects, `ProjectionReaders`
  (lifecycle, repo_surfaces, landing_state) and `RefreshPass` (now, refresh), so all five
  `state.read(...)` call sites here were respelled and the explicit `landing_state=None` now comes
  from the `ProjectionReaders` default. No test was added, removed, or renamed; the instrumented
  reader counts, the two corpus sizes, and every assertion are unchanged, and this card describes
  refresh behavior rather than the call signature.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  domain-invalidation and reclamation regressions. Verification metadata remains blank until
  commit.
