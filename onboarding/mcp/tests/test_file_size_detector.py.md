# mcp/tests/test_file_size_detector.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

File-size measurement and report-versus-enforcement command selection.

## Code Commentary

### Logic

Newline counting matches wc-style measurement: 1199 stays below the hard limit while 1200 produces one hard-limit finding. The wrapper includes --report when unarmed and omits it when armed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The remaining cases do not assert every historical size band, CLI exit or empty-measurement path. Size reporting is distinct from restoring test-count or coverage requirements.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Measure counts newlines like wc and flags only hard limit. [1]
- Unarmed step reports and armed step fails. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
