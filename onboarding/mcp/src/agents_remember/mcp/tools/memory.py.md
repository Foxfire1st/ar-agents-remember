# mcp/src/agents_remember/mcp/tools/memory.py

## Governing Overview

[overview.md](overview.md)

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
  packages. Two exceptions belong here: wire-shape compaction (mirroring `tools/providers.py`
  and `tools/core.py`), where the application entry point keeps returning the full result and
  the report is written BEFORE compaction so forensic detail is never lost; and the one
  configured-authority refusal, where the two citation builders answer a
  `ConfiguredContractAuthorityError` instead of letting it reach the choke point.
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

## 260928-MIK-L37 The Converted Citation Fix Response Is Bounded

`citation_fix_payload` passes the tool's result through `bounded_citation_fix`. For a converted tree's result
(`status: "converted"`) every list is capped at `MAX_INLINE_CITATION_ITEMS` (50): `stale`, `rewrittenSidecars` and
`unreadableSidecars`, and inside `authoring` `authoredCards`, `createdSidecars`, `unresolvedTargets` and `refused`
(`_bounded_lists`). Each list gets `<name>Count` with the full number; `truncated` names the capped lists, and
`truncatedNote` says how to get the rest: name one card, or run the command line's dry run. An unconverted tree's
result is passed through unchanged, because its complete repair list is that fixer's contract.

- A converted tree's citation-fix result is bounded for transport; a legacy result passes through. [1]
- Each named list capped, with its full count. [2]
- The response caps every list, says so, and keeps the full counts. [3]

## The Citation Tools Answer A Configured-Authority Mismatch

`citation_fix_payload` and `citation_migrate_payload` call their application entry point inside a `try`
that catches exactly `ConfiguredContractAuthorityError`. The catch returns `_citation_authority_refusal`:
`ok: false`, `status: configured-contract-authority-invalid`, the `repoId` and `contractPath` it was called
with, a `detail` naming the failing side and name, and `nextAction: developer-decision` — the remedy every
sibling answer to the same condition carries. Every other error, an `AuthorityError` among them,
propagates unchanged: the two entry points answer only the one condition the product knows how to
name, and any other failure still raises and loses the envelope. `ENVELOPE_LOSING_RAISERS` stays
empty because the sweep's probe meets only that condition. The refusal is built once, so the two
tools cannot answer the same condition differently; `citation_fix`'s answer still passes through
`bounded_citation_fix`.

- The two citation tools answer a configured-contract authority mismatch with the product's named refusal and next action. [4]
- The refusal carries the failing side and name in its detail, for both tools. [5]

- Only that error is translated: every other error, an `AuthorityError` among them, still propagates unchanged. [6]
