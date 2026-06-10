# test_carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_carryover.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:50+02:00                     |
| lastVerifiedCommitHash | `7e730de0465266ef19c31ceaffa29475b7bc3a79`                                  |
| lastVerifiedCommitDate | 2026-06-10T05:35:29+02:00|

## Purpose

Tests for branch-memory carryover planning and apply (`memory/carryover.py`),
focused on the issue #56 route-overview candidate and index-regeneration
behavior.

## Code Commentary

### Logic

`CarryoverFixture` builds a real code repo (main + landed `task/one` branch
touching `src/app/feature.py`), a ledgered official memory repo, and a source
memory tree with the feature sidecar. Plan tests prove: a differing route
overview whose route covers a landed path becomes a `route-overview` candidate
keyed by the normalized route and is `review-required`; a route without landed
paths produces no candidate; identical branch/official content (root route `.`)
auto-carries for metadata re-verification; sidecar candidates keep the
`file-sidecar` default kind. Apply tests prove: an explicitly included
overview is copied, restamped to the official head, and official-side
`overview.index.json` files are regenerated and committed
(`route_index_refresh.state == "refreshed"`); a non-official checkout skips
index regeneration with a reported reason; a no-carry apply reports the
skipped index refresh.

### Invariants And Boundaries

Self-contained git/onboarding fixtures (no imports from other test modules);
exercises the service API (`build_plan_for_request` /
`apply_carryover_for_request`), not the CLI adapters. The legacy sidecar
evidence-tier coverage stays in `test_worktree_support.py`'s c-11 tests.

## Docs References

No external documentation is needed for this standard-library test.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Module under test. | [carryover.py](agents-remember-md/mcp/src/agents_remember/memory/carryover.py) |
| Evidence-tier and ledger-mapping carryover coverage lives beside the worktree tests. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-10T05:50+02:00 — Created with the route-overview carryover candidates and guarded index regeneration (issue #56 sub-task 3).
