# mcp/src/agents_remember/mcp/registration/memory.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/mcp/registration/memory.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-07-31T15:31+02:00                                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                 |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                              |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_memory_tools(server, config)` declares the eight memory-root tools: `drift_check`,
`memory_quality_check`, `route_index_refresh`, `memory_init`, `memory_baseline_status`,
`memory_baseline_adopt`, `memory_carryover_plan`, `memory_carryover_apply`.

## Code Commentary

### Logic

The two read-only gates are named for when they run: `drift_check` is the **task-start** gate
(classifies how far onboarding has drifted since it was last verified — a nonzero actionable count
after code changes is expected, not a failure), `memory_quality_check` is the **closeout** gate
(`ok=false` means findings exist, not that the tool failed).

Three declarations pack:

- `memory_baseline_adopt` — `source_branch` + `work_branch` become `MemoryBranches`.
- `memory_carryover_plan` / `memory_carryover_apply` — the five refs the plan compares
  (`repo_id`, `source_memory`, `official_code_ref`, `source_code_ref`, `old_base`) plus
  `replace_existing` become one `CarryoverSelection`, and apply's two commit messages become
  `CarryoverCommitMessages`. The `intent_note` stays a separate argument: it is the approval, not
  part of the selection.

The mutating/approval-gated ones say so in their docstrings — `memory_baseline_adopt` writes the
ledger and commits memory and is gated on clean drift unless `accept_drift=true`;
`memory_carryover_apply` may only run after the code has landed officially and after
`memory_carryover_plan` has been reviewed.

### Invariants And Boundaries

- The signature stays flat; the parameter objects are built in the body.
- `drift_check` is task-start guidance, `memory_quality_check` is the closeout quality gate — do not
  swap them in prose or hints.
- Everything these tools do lives in `controllers/memory_tools.py` and the memory-quality package;
  this module chooses nothing.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The payload builders, including the report-filing carryover pair. | [tools/memory.py](agents-remember/mcp/src/agents_remember/mcp/tools/memory.py) |
| `MemoryBranches`, `CarryoverSelection`, `CarryoverCommitMessages`. | [controllers/memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |
| Defaults and packing proved through a live server. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The eight memory
  declarations moved out of `server.py`; adopt and the carryover pair now pack their arguments into
  `MemoryBranches` / `CarryoverSelection` / `CarryoverCommitMessages` in the body. Verification
  metadata pinned to the pre-change commit until closeout stamps the L2 code commit.
