# mcp/tests/test_mik_r53_onboarding_gate.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This module protects MIK-R53 Part A's source-bound onboarding judgments: a current row is the answer, `updated` additionally requires a counted card/reference change, and a later source change reopens the item. It exercises model, writer, worklist and gate boundaries using synthetic memory and temporary Git fixtures. The independent fact-check requirement is a lifecycle duty, not a test-proven closeout gate here.

## Code Commentary

### Logic

Row fixtures distinguish old and new source blobs. Tests exclude realization/proof-only changes and mechanical reference maintenance from counted changes, while allowing authored reference changes. Writer cases verify generated source bindings and `absent` for deletion. Gate cases require exact current source equality and reject rowless counted edits, stale rows, or `updated` without a counted change.

The attempt fixtures retain the winning row's individual history-file closed flag: a closed first attempt's sourceless row stays valid until an open row supersedes it. Product-owned closeout/reopen fixtures compare the candidate against the leaf's paired memory base, not merely the operation's HEAD, and ensure stale cached counted flags cannot override that base.

Symlink fixtures preserve mode-120000 identity and link-byte blobs. File anchors on links remain possible, but the writer, conversion, worklist resolver, carry mapper and base-side classifier must not parse link bytes as symbol definitions, even when those bytes look like Python. Those tests distinguish source-side modes when a path was a symlink in the base but a regular file in the candidate.

### Invariants And Boundaries

- A counted card edit without the current trace row answers nothing; an unrelated realization entry does not count as an onboarding review.
- Legacy sourceless rows in open history files answer nothing; closed-file validity must follow the winning row, not a merged owner's overall flag.
- Current `no_impact` and current eligible `updated` are distinct statements; the old main-line writer's limited schema is not evidence that the candidate's new row contract is satisfied.
- Temporary Git commits and product-owned closeout fixtures are isolated test setup. This card reports assertion intent, not a new test PASS or a production transaction.

## Evidence

### Repo-Internal References

- Row schema and counted-change assertions exclude realizes/proves-only maintenance. [1]
- Writer assertions bind sources from the candidate and record deletion as absent. [2]
- Currency, counted-change and legacy open/closed boundaries are tested separately. [3]
- Worklist and generic gate cases keep rowless or stale counted edits open. [4]
- The winning row retains its own attempt's closed flag. [5]
- Paired-base comparisons and stale-counted-flag regressions distinguish operation HEAD from the leaf base. [6]
- Symbol resolution on mode-120000 entries is refused across writer, conversion and worklist/carry paths. [7]
