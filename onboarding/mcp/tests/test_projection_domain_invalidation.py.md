# mcp/tests/test_projection_domain_invalidation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_projection_domain_invalidation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

| Finding | Source Path |
| --- | --- |
| Retained domain state under test. | [projection_inputs.py](agents-remember/mcp/src/agents_remember/observer/projection_inputs.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

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
