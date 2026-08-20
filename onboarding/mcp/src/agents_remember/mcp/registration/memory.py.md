# mcp/src/agents_remember/mcp/registration/memory.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/mcp/registration/memory.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df`                 |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00|
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

The two read-only checks are named for what they measure: `drift_check` is the **task-start**
worklist
(classifies how far onboarding has drifted since it was last verified — a nonzero actionable count
after code changes is expected, not a failure). A contract-scoped `memory_quality_check` is the
curator's full pre-closeout repair worklist and is repeated as the hard post-refresh closeout gate;
`ok=false` means enforced findings exist, not that the tool failed. A full scoped call also replaces
one operational checklist under the enclosure `reports/` directory and returns the zeroable
curator count/status; subset and unscoped calls write no checklist. The application layer supplies
the leaf base only as temporary comparison provenance for unstamped cards.

Since 260815-DAG-L15 the `memory_quality_check` registration takes keyword-only `wait: bool = True`
and `run_id: str | None = None` (L15-R7, the 2026-08-19 timeout class). `run_id` dispatches to the
poll payload (the identical full result when completed; `run-not-found` means the run was evicted or
the server restarted — rerun). `wait=false` dispatches to the start payload and returns
`{status, runId}` to poll. The synchronous path and its 5-argument payload are byte-unchanged, so
existing callers and tests are unaffected.

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
- `drift_check` identifies update work; contract-scoped `memory_quality_check` must be repaired and
  rerun by the curator before handoff, then repeated by closeout after real-commit metadata refresh.
- Registration documents the checklist as the only write of a full scoped quality call: code and
  memory remain unchanged, and dirty-source/full-quality `ok` is not the curator's zeroable gate.
- The async `wait`/`run_id` surface is keyword-only and additive: `wait=True` (the default) keeps
  the exact synchronous behavior and payload.
- Everything these tools do lives in `application/memory_tools.py` and the memory-quality package;
  this module chooses nothing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders for the carryover plan and report-filing apply pair. | `memory_carryover_plan_payload`; `memory_carryover_apply_payload` | mcp/src/agents_remember/mcp/tools/memory.py:219-230; mcp/src/agents_remember/mcp/tools/memory.py:233-254 |
| The start/poll payload builders behind the `wait=false`/`run_id` branches (L15-R7). | `memory_quality_check_start_payload`; `memory_quality_check_poll_payload` | mcp/src/agents_remember/mcp/tools/memory.py:71-91; mcp/src/agents_remember/mcp/tools/memory.py:93-100 |
| The `MemoryBranches` parameter object. | `MemoryBranches` | mcp/src/agents_remember/application/memory_tools.py:604-610 |
| The `CarryoverSelection` parameter object. | `CarryoverSelection` | mcp/src/agents_remember/application/memory_tools.py:617-634 |
| The `CarryoverCommitMessages` parameter object. | `CarryoverCommitMessages` | mcp/src/agents_remember/application/memory_tools.py:637-642 |
| Baseline branch packing and drift gating are proved by `test_memory_baseline_adopt_groups_the_two_branches_and_gates_on_drift`. | `test_memory_baseline_adopt_groups_the_two_branches_and_gates_on_drift` | mcp/tests/test_mcp_registration_wiring_tests_1.py:402-418 |
| Carryover selection packing is proved by `test_memory_carryover_plan_packs_the_selection`. | `test_memory_carryover_plan_packs_the_selection` | mcp/tests/test_mcp_registration_wiring_tests_1.py:420-446 |
| Apply intent and default-message packing is proved by `test_memory_carryover_apply_carries_the_intent_note_and_default_messages`. | `test_memory_carryover_apply_carries_the_intent_note_and_default_messages` | mcp/tests/test_mcp_registration_wiring_tests_1.py:428-450 |
| The async registration branches are proved through the live FastMCP schema. | `test_memory_quality_check_wait_false_starts_a_background_run`; `test_memory_quality_check_run_id_polls_the_run` | mcp/tests/test_mcp_registration_wiring_tests_1.py:316-325; mcp/tests/test_mcp_registration_wiring_tests_1.py:327-334 |

## 260815-DAG-L3 Curator Attestation Registration

The `memory_quality_check` registration now states that a full contract-scoped run atomically
replaces both the rendered curator checklist and its structured, report-digest-bound JSON
attestation; subset and unscoped calls write neither artifact.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260815-DAG-L15 Async Quality Registration

The public `memory_quality_check` tool gained keyword-only `wait` (default True) and `run_id`
(L15-R7): `wait=false` starts the check as a background run and returns `{status, runId}`; a poll
with `run_id` returns the identical full result, and `run-not-found` means evicted/restarted —
rerun. The docstring documents the flow for the curator attestation path. The sync path is
byte-unchanged, preserving the existing contract and tests.

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: `memory_quality_check` registration gained keyword-only
  `wait`/`run_id` with start/poll dispatch (L15-R7); the synchronous path is unchanged. Verified at
  code commit de3a0fd9.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented the paired structured curator
  attestation on the public memory-quality tool; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T16:54+02:00 — Documented the single enclosure-local checklist side effect and the
  curator-specific zeroable count/status while preserving code/memory read-only behavior.
- 2026-08-11T14:40+02:00 — Clarified the contract-scoped quality tool as the curator's complete
  pre-closeout worklist and regenerated shifted application-model citations; real-commit metadata
  remains closeout-owned.
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
