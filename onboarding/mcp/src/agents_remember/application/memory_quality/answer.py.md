# mcp/src/agents_remember/application/memory_quality/answer.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Projects full memory-quality run outcomes into caller-sized status answers without changing execution, finding classification or checklist authority.

## Code Commentary

### Landing-report scope

Results that executed the converted drift slot additionally expose the whole cut-card and added-file counts, including zero counts for a clean population. First rows are slim and bounded by the shared status-entry limit and omitted when empty. Complete lists stay in the logged whole result; a full leaf publication also renders them in its checklist, while subset and diagnostic results have no new checklist promise. Projection does not promote report-only landing facts into blocking work orders.

- The converted answer carries complete landing counts and bounded slim first rows without narrowing retained results. [5]


Sync and completed-poll answers carry outcome, counts by finding kind, ordered blocking work orders and locations. Blocking rows are selected from repair findings, missing cards and stale indexes in repair-loop order; reasons are shortened only in the answer, not in the retained whole result. Start/poll outcomes preserve running/refused/completed state and scope-bound follow-up arguments. A failed coherence takeover keeps its code and next action, including task_doc for a missing task parent. A missing report is disclosed rather than treated as absence of findings.

### Compact proof and route-index cache diagnostics

For an ordinary completed result, `quality_result_answer` additionally carries
`invariantsWithoutProofCount` only when it is a nonnegative integer and not a Boolean. A zero is retained;
missing, negative and other typed values are omitted.

A dictionary-valued `routeIndexCacheBuild` is projected into a fresh compact dictionary containing only
present `builtCount` and `staleCount` keys, without additional validation of those two values. When
`buildErrors` is a list, the answer adds its length as `buildErrorCount`, including zero for an empty
list; it does not carry the error bodies. An empty input dictionary still produces an empty cache-build
dictionary. A non-dictionary cache-build value is omitted. Scope refusals return through their separate
projection before these fields are considered.

These are projections of the supplied whole result, not fresh proof discovery or cache-building work.
They do not change `ok`, the selected status or the existing blocking-list computation; complete error
details remain outside this compact selection.


## Evidence

### Repo-Internal References

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.


- Completed results retain status, blocking totals and report locations. [1]

- The bounded blocking list preserves repair-loop order and whole-population count. [2]
- A taken-over failure retains its own code and recovery action. [3]
- Poll projection distinguishes live, absent and completed runs. [4]

- Ordinary results project a nonnegative non-Boolean proof count and a bounded-key cache-build summary with a list-derived buildErrorCount. [6]
