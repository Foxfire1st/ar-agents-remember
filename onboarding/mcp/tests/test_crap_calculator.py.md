# mcp/tests/test_crap_calculator.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

CRAP diagnostic arithmetic and branch-measured function scoring.

## Code Commentary

### Logic

The formula uses a coverage ratio; the fixture joins Radon complexity with Coverage.py executable-line and branch information. A partially covered branchy function receives a higher score than a fully covered simple function. Reports without branch measurement refuse instead of fabricating a ratio.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

These tests validate measurement, not a coverage percentage floor or blocking CRAP threshold. CLI rendering and historical rollup matrices are not retained cases here.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Crap score formula uses coverage ratio. [1]
- Calculates function scores from radon and coverage json. [2]
- A report without branch measurement is refused. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
