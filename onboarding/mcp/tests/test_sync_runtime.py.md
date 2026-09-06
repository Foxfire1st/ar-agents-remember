# test_sync_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_sync_runtime.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                         |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks sync-runtime target replacement removes stale files and excludes cache directories. The default target roster is confined to MCP package data rather than harness starter directories. It is an actual temporary-tree copy test, not proof that installed runtime projections have just been refreshed.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync target replaces target with source tree | `test_sync_target_replaces_target_with_source_tree` | mcp/tests/test_sync_runtime.py:24-47 |
| Default targets only write to mcp package data | `test_default_targets_only_write_to_mcp_package_data` | mcp/tests/test_sync_runtime.py:49-61 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-04T18:43+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 4 citation rows with exact anchors (`load_sync_runtime` + `SCRIPT_PATH` extent and the three named test functions) and ledger-verified ranges. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_sync_runtime.py` and moved the lines this card cites, so the Citations column no
  longer pointed at the code its rows name. Corrected the ranges (L48-L69 → L48-L71; L71-L83 →
  L73-L85). The behaviour described is unchanged — the file's AST is identical to the base
  revision — this is a citation repair only. Verification metadata pinned until closeout stamps
  the L2 commit.

- 2026-06-08T11:53+02:00: Created onboarding for the focused runtime sync helper tests. Verification metadata is pending until the code commit exists.
