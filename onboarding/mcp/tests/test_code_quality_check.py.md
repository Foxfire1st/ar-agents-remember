# mcp/tests/test_code_quality_check.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Sample repository and shared constants for quality-selection consumers.

## Code Commentary

### Logic

write_sample_repository creates an uncommitted temporary Git fixture with product ownership for pkg, an empty verification owner list, pytest discovery, lint/type/coverage settings and representative source/test/script files. run_git is the bounded command helper. No quality tests remain in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The filename does not establish complexity or coverage enforcement. Fixture configuration supports consuming tests and must not restore removed percentage gates.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Run git. [1]
- Write sample repository. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
