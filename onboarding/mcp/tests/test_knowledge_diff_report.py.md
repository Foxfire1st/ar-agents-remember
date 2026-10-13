# mcp/tests/test_knowledge_diff_report.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Protect the naming comparison report, failure cleanup and per-answer resource/caching boundaries.

## Code Commentary

Hermetic converted Git repositories distinguish added/deleted/modified names and tree identities from the complete report patches. Names of deleted records remain absent when opened; the answer does not carry revised record prose. An empty comparison still publishes a complete report.

Failure controls separately check unwritable destinations, failed replace, mid-stream failure and cleanup failure. Successful cleanup preserves earlier final bytes and removes partial files; failed cleanup reports an actual sibling .part residual and carries that truth to the caller. This is not a universal no-residue promise.

Resource witnesses exercise admitted/refused report sizes, budget-family accounting, unmeasurable usage, repeated whole report content, paged realization identity coverage, cache reuse and declaration/line work at two sizes. Prepared work-count contrast is not a live aggregate CPU/RSS benchmark. The entry-point placement control checks a parseable report with a reports path component, not a universal runtime-path proof.

## Evidence

- Comparison answers identify the trees and record changes while the report retains patches. [1]
- Cleanup failure exposes a real sibling partial file rather than claiming absence. [2]
- The locator work witness counts actual declaration and line visits without replacing the retained contrast. [3]
- Report admission charges existing report bytes beside logs. [4]
