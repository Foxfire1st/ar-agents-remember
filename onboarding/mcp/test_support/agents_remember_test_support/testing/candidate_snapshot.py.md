# mcp/test_support/agents_remember_test_support/testing/candidate_snapshot.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/candidate_snapshot.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Produces the exact Git working-candidate identity used by non-accepting Dagger evidence.

## Code Commentary

### Logic

`candidate_snapshot` hashes the HEAD commit/tree, exact staged candidate tree, and every changed,
deleted, and untracked non-ignored path, including executable bits and symlink target text. Paths
are confined before bytes are read.

### Conventions

The digest is a working-candidate identity, not a substitute commit.

### Invariants And Boundaries

- Missing Git facts or non-file candidate entries refuse.
- Ignored dependency/cache directories do not become candidate content.

### Todos

None.

## Docs References

No external contract applies.

## Repo-Internal References

`evidence_provenance.py` embeds this payload in cadence, retry, and measurement evidence;
`route_measurement.py` proves it is unchanged across all measured runs.

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T04:37+02:00 — Added exact staged candidate-tree identity and removed the retired
  direct-evidence consumer.
- 2026-08-27T11:08+02:00 — Created for complete-candidate route binding.
