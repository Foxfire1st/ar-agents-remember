# mcp/tests/test_knowledge_read_boundary.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R74 rule 6: a read changes no branch, tag or HEAD, no worktree file, no Git index, no task document and no requirement packet.** A test runs every read against scratch clones and compares before and after — refs and HEAD, the index file, the working trees, the task folder — and fails on any difference outside (a) `runtime/` caches, (b) a recorded comparison with its pin ref, and (c) a preview's worklist, reports and judged-tree objects.

## Code Commentary

The main roster case runs every registered read; a second case mutates one read to create a directory and shows the harness catching it, so the first case cannot pass vacuously. Enclosure reads record only comparisons and previews; reviewer GET routes, miscellaneous description-called reads, memory-backed reads, seat status previews and dry runs, code-search plan/refusal reads, diagnostic/watcher/skill reads, and the remaining dashboard GETs each read without writing. The oracle lives in `read_boundary_oracle_test_support.py`.

The converted-drift case applies the same before/after filing oracle to drift and registered
baseline-status calls. Its original run caught report, observer-snapshot and directory creation;
the repaired branch removes those differences. The response assertions check dictionary shape,
not individual returned fields, and the fixture serializes an array-valued sidecar. This case is
therefore a filing-boundary witness, not proof of clean-card measurement or returned pointer
values; the summary/projection owners carry those separate contracts.

## Evidence

- Every registered read leaves nothing but cache [1]
- A mutated read is caught, so the roster cannot pass vacuously [2]
- Enclosure reads record only comparisons and previews [3]
- Review GET routes read without writing [4]
- Remaining dashboard GETs read without writing [5]

- Converted drift and registered baseline status are exercised under the filing oracle; dictionary assertions and the array-valued fixture do not establish clean-card or returned-field semantics. \[6] [6]
