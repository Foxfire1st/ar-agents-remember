# test_install_runtime.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Runtime installation preservation and watcher recovery tests.

## Code Commentary

### Logic

Installing managed assets preserves provider state, database data and central logs while removing obsolete generated runtime assets. Dependency installation failure still attempts watcher restart and status recovery. Existing global settings remain byte-identical; dry run counts a seed without writing it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Temporary fixtures and watcher doubles do not operate live providers. Copy-if-missing settings behavior must not overwrite developer configuration.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Runtime install preserves docker provider state. [1]
- Runtime install provider dependency failure attempts watcher recovery. [2]
- Existing settings file is never clobbered. [3]
- Dry run counts the seed without writing. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
