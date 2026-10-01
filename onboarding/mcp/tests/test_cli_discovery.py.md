# test_cli_discovery.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Trusted CLI settings discovery through temporary directory trees.

## Code Commentary

### Logic

Same-directory convention settings beat registration, but a nearer registration beats a farther convention. Malformed, missing-config-argument and foreign-server registrations are skipped. A miss names both searched patterns and the resolved starting directory.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Usable fixture settings point to an existing absolute coordination directory. The retained four cases do not include the old placeholder-template or missing-target-file tests.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Convention wins over registration in the same directory. [1]
- Nearest directory wins across levels. [2]
- Malformed and foreign registrations are skipped. [3]
- Miss raises with both patterns and the origin. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
