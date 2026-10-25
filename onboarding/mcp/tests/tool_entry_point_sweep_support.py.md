# mcp/tests/tool_entry_point_sweep_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The hermetic world and the vocabulary classifier the entry-point sweep runs in: one disposable coordination root, one registered server, one client session per call, and the single classifier both the sweep and its positive controls use.

## Code Commentary

`EntryPointWorld` carries the merged-tree world with real code and memory repositories, authors a master and a leaf, and opens one real leaf enclosure through the tools. `call` invokes one registered tool exactly as a consumer does; `census`, `git_census`, `coordination_census` and `repository_state` read the world back by path and digest, and `coordination_boundary` splits a move by whether it lies in one of the declared write zones. `benign` supplies one invocation per public tool. `prepare` performs no per-tool ambient arrangement, and `sweep` invokes the roster in registration order while storing `prepared_state` and `state_after` as the fixed fixture label `"none"`; those strings are not state observations. `classify` assigns one of the declared arms, using `_raised_arm`, `_returned_arm`, `refusal_marks` and `_whole_result`; `_raised_arm` separates boundary validation from argument validation by which model refused. `_whole_result` reads a usable mapping from the answer's log file when one is available; otherwise it returns the delivered payload, including when the log cannot be read or decoded. This describes the existing classifier's evidence boundary, not a guarantee that every answer has a logged whole result.

## Invariants And Boundaries

The classifier is one implementation, so a control that passes proves the sweep and not a second reading of it. Refusal marks are read from the payload, never from the arm the classifier assigned. Git lock and pid files are transient and never evidence, and the timeout class is the sweep's own deadline rather than a product exception to classify.

## Evidence

### Repo-Internal References


- One classifier assigns the declared arms, separating the two raise shapes by model identity rather than by wording. [1]



- The census reads the world by digest, with the coordination boundary split by declared write zone. [2]


- A usable logged whole-result mapping is read from disk; an absent, unreadable or non-mapping log leaves the delivered payload as the classifier input. [3]

- Preparation is a no-op and sweep state fields are fixed none labels rather than observations. [4]
