# mcp/src/agents_remember/tasks/master_order.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Derive an ordinary master’s state-aware Order from its explicitly indexed task rows and their waitsFor fields; never persist derived waves or authorize execution.

## Code Commentary

MasterOrderTask carries the review state and the existing ready_ids filter excludes a non-go present review; dependency/cycle readiness rules remain.

Child loading opens only row.file paths and accepts prepared overrides before disk reads. Missing/invalid/non-subTask children are skipped. A view is absent for non-master/sprint input or when no matching listed child carries nonempty waitsFor. A matching child document supplies its authoritative status, title and dependencies; only an absent matching child falls back to the master row’s status. Unknown dependency IDs remain synthetic gone/fileless facts.

The iterative ordered SCC calculation identifies legacy cycles, including self-cycles, from the full stored dependency population before excluding Completed tasks from the scheduling graph. Unfinished members retain those full-population component identities. A component containing inProgress, gone or abandoned state anchors at wave zero; other unfinished components follow prerequisite waves with a minimum of one. Every member of a stored cycle, including Completed members, receives the unfinished component’s wave, or -1 when the entire cycle is Completed, and keeps its cycle flag. Other Completed tasks remain outside the unfinished wave graph. Only planning, noncycle tasks whose prerequisites are Completed and whose native intentReview is absent or go enter ready_ids; derive_master_order indexes cycle IDs as a set for repeated membership checks. The predecessor’s unfinished-only SCC/cycle scope is historical, not the RF01 rule. This ordinary-master calculation is not the sprint frontier’s terminal-resolution policy and is not a start gate.

## Current source contract

load_master_children turns each declared row.file into a Path and skips references with no name before applying the JSON suffix. Existing unreadable/invalid-child handling still skips OSError, ValueError and ValidationError. This protects the order-preview read path without changing dependency scheduling, manufacturing a directory census or introducing an alignment_sweep._preview function.

- Skips nameless row.file Path values before reading explicit children. [3]

## Evidence

Retained authoring-row wording:

Finding: Explicit child loading prefers canonical child status and falls back only when absent; SCC/wave construction remains display-only.

Anchor:

Source: mcp/src/agents_remember/tasks/master_order.py

Retained authoring-row wording:

Finding: MasterOrderTask carries the review state and the existing ready_ids filter excludes a non-go present review; dependency/cycle readiness rules remain.

Anchor:

Source: mcp/src/agents_remember/tasks/master_order.py

- Explicit child loading prefers canonical child status and falls back only when absent; SCC/wave construction remains display-only. [1]
- MasterOrderTask carries the review state and the existing ready_ids filter excludes a non-go present review; dependency/cycle readiness rules remain. [2]
