# mcp/tests/test_causal_failure_localization.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Exact-node causal blocking and reproducible runtime-failure records.

## Code Commentary

### Logic

A temporary package has one dependent test and one independent same-file test. Forcing the owner preflight failure names only the exact dependent node and keeps the artifact non-accepting. Runtime classification distinguishes socket, timeout and OS failures and records worker, seed, duration and process topology.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Suppression is exact-node rather than whole-file. Unclassified failures require classification before retry; this reduced suite does not separately prove every historical process-family case.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Failed owner blocks only source proved exact nodes. [1]
- Observed runtime failures retain exact retry inputs. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
