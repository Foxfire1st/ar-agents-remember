# mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Retains helpers for running a declared memory-quality check group and combining two quality
results. No production caller was found by the production AST/reference census with CLI and declared entry-point inspection. The source's closeout
docstrings and failure text describe their former use; they do not establish current closeout
execution. Current closeout consumes the exact memory-quality attestation separately.

## Code Commentary

### Logic

`run_memory_quality_phase` asks the injected `MemoryQualityPort` for a drift context rooted at the
active code checkout, runs exactly the supplied check group, and raises when `ok` is false. The
optional `unstamped_code_commit` passes through as comparison context. Failure text includes at
most five finding summaries; a successful call returns the full quality-service result.

`combine_memory_quality` merges the supplied check maps and findings, sums ordinary and
report-only counts, bounds the report-only sample to 50 rows, and records service-declared check
groups under `closeoutPhases`. The first result can be empty; the second must provide the indexed
fields. This is result composition when directly called, not a live closeout gate.

### Invariants And Boundaries

- The helpers own neither commits nor approval, lineage, metadata refresh or transaction ordering.
- A failed quality result raises; it is never converted into a warning.
- Group names come from `MemoryQualityPort.check_groups()`.
- These functions do not implement identical-copy grouping or trace judging. The curator's trace
  gate owns that work; closeout checks its attestation rather than invoking this phase runner.

### Todos

The retained module docstrings and refusal wording still name the former closeout pipeline.
There is no executable `_closeout_quality_preflight` caller in the final source tree.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository-local closeout adapter.

No relevant external documentation is configured.

### Repo-Internal References

- One phase builds the service-owned drift context, runs the exact check group, and refuses on a non-clean result with bounded evidence. [1]
- The combined result preserves both phase check maps, findings, counts, bounded report-only evidence, and declared phase membership. [2]

- The retained runner executes a supplied check group when directly called. No production call of either helper was found by the production AST/reference census with CLI and declared entry-point inspection; the current closeout owner imports neither helper. [3]

- The external-memory commit owner runs the refresh and the memory/ledger commits; it no longer combines a memory-quality gate result. [4]
- The memory-quality port declares drift context, check groups and quality execution. [5]

- The injected service bundle keeps memory quality and certification continuation as distinct ports. [6]


### Cross-Repo References

No cross-repository interface is owned by this internal closeout helper.

No applicable cross-repository source was found.
