# mcp/tests/test_final_codex_certificate.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate-4 certificate binding to a completed two-fresh-pass run.

## Code Commentary

### Logic

A complete green run produces a content-bound certificate for the exact candidate and plan with its three predecessor identities. An incomplete red run cannot publish, and a candidate mismatch refuses.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

These standalone fixture tests validate certificate issuance, not live Codex execution. The older exhaustive stale/retry/incomplete matrix is not wholly retained.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Green two fresh pass publishes bound certificate. [1]
- Red manifest cannot publish. [2]
- Candidate mismatch refuses. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
