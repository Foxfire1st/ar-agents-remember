# mcp/tests/test_cgc_watch_guard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_cgc_watch_guard.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

CGC watcher guard behavior through a stub Redis module.

## Code Commentary

### Logic

The host loader injects Redis exception stubs before importing the runner asset. Retained cases bound readiness waiting, preserve an already indexed graph, and verify main reaches the cgc watch exec boundary after graph checks.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No live Redis or CGC backend is started. The retained graph case proves preservation, not every historical poisoned-graph deletion path.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Wait for ready gives up after deadline. | `test_wait_for_ready_gives_up_after_deadline` | mcp/tests/test_cgc_watch_guard.py:67-70 |
| Clear poisoned graph keeps indexed graph. | `test_clear_poisoned_graph_keeps_indexed_graph` | mcp/tests/test_cgc_watch_guard.py:72-79 |
| Main checks graph then execs cgc. | `test_main_checks_graph_then_execs_cgc` | mcp/tests/test_cgc_watch_guard.py:81-92 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: split test-path resolution, packaged entrypoint, Dockerfile copy, and Compose entrypoint so each whole claim has one owner.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_cgc_watch_guard.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3
  line(s) with no token change whatsoever. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-06-09T23:55+02:00: Created with the guard's unit tests after the CRAP report flagged `wait_for_ready` at the 30.0 threshold (0% coverage on a CC-5 function).
