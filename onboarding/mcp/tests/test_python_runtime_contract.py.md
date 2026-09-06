# mcp/tests/test_python_runtime_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_runtime_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `eb05a872780112640359232063168639d20fa87b`|
| lastVerifiedCommitDate | 2026-09-03T06:19:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Runs the Python builder installer against controlled command fixtures to prove a full clone is validated before atomic no-clobber publication, a valid existing builder is reused, and a foreign builder is refused without deleting its marker. This file no longer asserts every package/CI Python-version surface or the old publisher-race matrix.

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
| Runtime builder is fully cloned atomically published and reused | `test_runtime_builder_is_fully_cloned_atomically_published_and_reused` | mcp/tests/test_python_runtime_contract.py:154-184 |
| Existing foreign builder is refused and preserved | `test_existing_foreign_builder_is_refused_and_preserved` | mcp/tests/test_python_runtime_contract.py:187-200 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): documented the new hermetic installer-contract tests (full clone, atomic no-clobber publication, cleanup, reuse, foreign-path refusal, publisher races) and refreshed the citation anchors for the runtime-contract/capability tests. Verification metadata rebased from `60e429d1` to the bootstrap repair owning commit.

- 2026-08-29T16:10+02:00 — Created for the project-wide Python 3.13.15 cutover and native-pidfd
  acceptance boundary. Verification remains closeout-owned.
