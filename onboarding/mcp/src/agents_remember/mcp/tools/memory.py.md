# mcp/src/agents_remember/mcp/tools/memory.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/mcp/tools/memory.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                                      |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Memory, drift, route-index, baseline, and carryover payload builders.

## Code Commentary

L23 adds the MCP payload adapter for guarded, contract-scoped `citation_fix`, preserving operation scope and dry-run semantics.

### Logic

Holds `drift_check_payload`, the three typed memory-quality payload builders,
`route_index_refresh_payload`, `memory_init_payload`,
`memory_baseline_status_payload`, `memory_baseline_adopt_payload`,
`memory_carryover_plan_payload`, and `memory_carryover_apply_payload`. Each returns through
`base._tool_payload`. The quality trio accepts the exact sync, start, or poll request model and
forwards it to `application.memory_quality.controller`; it does not unpack, reinterpret, or
reproduce controller failures.

Three of them take parameter objects (260731-EFA-L2): `memory_baseline_adopt_payload(config,
repo_id, *, accept_drift=False, branches: MemoryBranches = DEFAULT_MEMORY_BRANCHES,
dry_run=False)`; `memory_carryover_plan_payload(config, selection: CarryoverSelection)`; and
`memory_carryover_apply_payload(config, selection: CarryoverSelection, *, intent_note,
include_review_required=None, messages: CarryoverCommitMessages = DEFAULT_CARRYOVER_MESSAGES)`.
`intent_note` deliberately stays outside `CarryoverSelection` — it is the approval, not part of what
is being carried. These unrelated carryover signatures remain flat; memory quality is the
deliberate nested discriminated request contract published by `mcp/registration/memory.py`.

The two carryover builders additionally file the full application entry point result under
`temp/tool-reports/memory_carryover_plan/` / `.../memory_carryover_apply/` via
`write_tool_report`, then return `compact_carryover_payload(full, reportPath)`:
per-decision `source_path` lists in `decisions` (each list capped at
`MAX_INLINE_CARRYOVER_PATHS` = 25 with a `... (+N more in report)` marker),
`carriedPaths` for apply, and `reportPath` inline. The `candidates` array — and
`carried`, which apply duplicated verbatim — never reach the wire; before this,
a 28-file apply response cost 7.7k tokens (GitHub #52).

### Invariants And Boundaries

- Transport-thin: quality behavior lives in `application.memory_quality.controller`; other
  memory/drift behavior lives in `application.memory_tools` and the memory/onboarding-drift
  packages. Wire-shape compaction is the one
  exception that belongs here (mirroring `tools/providers.py` and
  `tools/core.py`): the application entry point keeps returning the full result, and the
  report is written BEFORE compaction so forensic detail is never lost.
- Decision facts stay inline (per-decision path lists, commits, intent note);
  only derivable per-record verbosity (onboarding paths, repeated
  evidence/reason strings) moves to the report.
- The effectful builders (`route_index_refresh_payload`, `memory_init_payload`,
  `memory_baseline_adopt_payload`) default `dry_run=False` (act-by-default),
  matching the server registration; `dry_run=true` previews.
- Sync/start/poll builders accept their matching strict DTO and wrap the controller result verbatim;
  no compatibility overload or local failure translation is permitted.

## 260821-DAGQC-L2 Typed Quality Adapters

`memory_quality_check_payload`, `memory_quality_check_start_payload`, and
`memory_quality_check_poll_payload` form one transport-thin set over the controller API. Their
signatures make it impossible to call a poll adapter with execution fields or start work with a poll
request, while `_tool_payload` remains the shared public response validator.

## 2026-08-26 Application-Owner Relocation

The transport continues to delegate memory-quality execution without reinterpretation, but the
canonical application owner now lives at `application.memory_quality.controller`. This is a
package extraction only: sync/start/poll semantics and response finalization remain owned by that
controller.

## Update History

- 2026-08-26T10:44:52+02:00 — Updated the canonical memory-quality application-owner path after the package extraction; transport behavior is unchanged.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: rewired the quality payload trio to strict sync/start/poll DTOs and the single controller API; removed flat wait/run-id interpretation from this layer. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added `memory_quality_check_start_payload` /
  `memory_quality_check_poll_payload` wrapping the async application envelopes (L15-R7, incl. the
  `ok`-header gate-repair fix). Verified at code commit de3a0fd9.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `memory_baseline_adopt_payload` took `branches:
  MemoryBranches`; the carryover pair took `selection: CarryoverSelection` (positional) and apply
  took `messages: CarryoverCommitMessages`, keeping `intent_note` separate. Compaction, report
  filing and the act-by-default `dry_run` contract are unchanged. Verification metadata pinned until
  closeout stamps the L2 code commit.
- 2026-06-10T09:00+02:00 — Carryover plan/apply responses compacted for 2.5.2 (GitHub #52): full result filed via `write_tool_report`, wire keeps per-decision capped path lists + `carriedPaths` + `reportPath`, drops `candidates`/`carried` (apply previously repeated every record twice; 7.7k tokens for a 28-file carryover).
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the effectful memory payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
