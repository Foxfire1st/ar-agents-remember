# mcp/src/agents_remember/mcp/registration/memory.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/mcp/registration/memory.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-08-02T01:05+02:00                                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                 |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                              |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

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
- Everything these tools do lives in `application/memory_tools.py` and the memory-quality package;
  this module chooses nothing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders for the carryover plan and report-filing apply pair. | `memory_carryover_plan_payload`; `memory_carryover_apply_payload` | mcp/src/agents_remember/mcp/tools/memory.py:163-174; mcp/src/agents_remember/mcp/tools/memory.py:177-198 |
| The `MemoryBranches` parameter object. | `MemoryBranches` | mcp/src/agents_remember/application/memory_tools.py:406-412 |
| The `CarryoverSelection` parameter object. | `CarryoverSelection` | mcp/src/agents_remember/application/memory_tools.py:411-427 |
| The `CarryoverCommitMessages` parameter object. | `CarryoverCommitMessages` | mcp/src/agents_remember/application/memory_tools.py:438-444 |
| Baseline branch packing and drift gating are proved by `test_memory_baseline_adopt_groups_the_two_branches_and_gates_on_drift`. | `test_memory_baseline_adopt_groups_the_two_branches_and_gates_on_drift` | mcp/tests/test_mcp_registration_wiring_tests_1.py:373-389 |
| Carryover selection packing is proved by `test_memory_carryover_plan_packs_the_selection`. | `test_memory_carryover_plan_packs_the_selection` | mcp/tests/test_mcp_registration_wiring_tests_1.py:391-415 |
| Apply intent and default-message packing is proved by `test_memory_carryover_apply_carries_the_intent_note_and_default_messages`. | `test_memory_carryover_apply_carries_the_intent_note_and_default_messages` | mcp/tests/test_mcp_registration_wiring_tests_1.py:417-438 |

## Update History
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): expanded the payload-builder claim to cover both the carryover plan builder (163-174) and the report-filing apply builder (177-198); parameter objects and registration tests retained; the scoped fixer confirmed the final ranges with no writes.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 7 table citations for carryover payloads, branch selection, commit messages, and related tests; fixer-generated ranges verified.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The eight memory
  declarations moved out of `server.py`; adopt and the carryover pair now pack their arguments into
  `MemoryBranches` / `CarryoverSelection` / `CarryoverCommitMessages` in the body. Verification
  metadata pinned to the pre-change commit until closeout stamps the L2 code commit.
