# mcp/tests/source_selection_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/source_selection_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:46:49+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Supplies explicit source-selection values for compiler and executor contract tests. These values exercise canonical models and applicability compilation without claiming that a Git observer inspected a repository.

## Code Commentary

### Logic

`source_selection_fixture` builds a `CandidateSourceSelection` with a supplied candidate tree, configurable comparison commit and changed paths, and a fixed fixture base tree. It computes `selectionDigest` from that payload before model validation. The default changed path lies inside the fixture's declared scenario dependency prefix.

`ambient_selection_fixture` constructs one declared dependency-prefix selector and calls the production `compile_source_applicability` owner in targeted mode. Its argument selects either the declared scenario path or an empty change population. The declaration includes an evidence path and an explicit not-applicable reason.

`write_ambient_selection` writes the typed result as JSON plus a newline to `source-selection.json` below the supplied directory. This fixture input locator is distinct from the declaration's eventual `source-selection/ambient-role.json` evidence path.

### Conventions

Use these helpers for modeled observations. Tests claiming actual candidate Git membership or comparison-base observation must use the repository observer. The writer expects an existing root and returns the file it wrote.

### Invariants And Boundaries

- The selection digest covers the exact fixture payload and changed-path population.
- Applicability is compiled from a declared prefix contract; no production repository scope is inferred.
- Fixed hexadecimal identities and written JSON are fixture data, not checkout observation or scenario-execution evidence.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this file. | N/A | N/A |

## Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate identities and changed paths are explicit fixture values with a canonical digest. | `source_selection_fixture` | mcp/tests/source_selection_test_support.py:20-35 |
| Targeted applicability is compiled from the declared fixture dependency prefix. | `ambient_selection_fixture` | mcp/tests/source_selection_test_support.py:38-55 |
| The writer emits typed selection to a concrete test input file. | `write_ambient_selection` | mcp/tests/source_selection_test_support.py:58-61 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented synthetic observation, canonical applicability and serialization boundaries. This source verification makes no gate or acceptance claim.
