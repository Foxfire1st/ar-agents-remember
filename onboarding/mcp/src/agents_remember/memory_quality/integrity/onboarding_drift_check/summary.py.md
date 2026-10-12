# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`summary.py` runs a bounded onboarding drift summary for context packets,
`drift_check`, and the closeout memory quality gate. On a converted tree the summary is built from
`converted_knowledge_check` and nothing else: it names how many reference anchors are current and how
many are stale against the code, which files the knowledge validator refuses, and the two roots that
were read. The legacy classification is never called for a converted tree — a converted card has no
metadata table, so legacy discovery would answer an unread "checked, 0" instead of measuring.

## Code Commentary

### Landing-report scope

The converted summary explicitly calls the shared converted checker with `include_landing=False`. It remains a validator/reference-state summary; the landing census belongs to quality-check callers rather than this drift-summary route; admitted leaf callers carry their leaf base. Skipping landing acquisition here changes no summary count, filing mode, reference-state classification or existing validator refusal.

- The converted drift summary suppresses landing acquisition while preserving validator/reference measurements. [13]


### Logic

The helper discovers sidecar onboarding, inline onboarding, and entity catalog
rows through `drift.py` and returns counts plus a bounded actionable sample. A read files nothing
at all (rule 6): the Markdown report and the observer snapshot are written only for an explicit
report-producing caller (`output.write_report`), and readers of the snapshot directory tolerate its
absence. `not_checked()`
provides the stable context-packet response when callers do not request drift.

Since 260731-EFA-L4 all three builders return the shared
`models.DriftSummaryPacket` TypedDict rather than a bare `dict[str, Any]`:
cit:([`not_checked`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:31-32) → `{"status": "notChecked"}`, `run_drift_summary(...)`
cit:([`run_drift_summary`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:35-90) → `{"status": "error", "error": ...}` when the onboarding root does not
exist cit:(["if not context.onboarding_root.exists()"], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:42-42) and otherwise the `summarize_rows` result, and `summarize_rows(...)`
cit:([`summarize_rows`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:93-108) → the `checked` packet carrying `count`/`actionableCount`/`reportPath`/
`actionableSample`. This module is therefore the **producer of every `DriftStatus`
member**, and the two wire models (`models/drift.py::DriftSummary` for the context
packet, `models/memory.py::DriftCheckResponse` for the tool) validate against the
same declaration instead of each restating the enum. The `error` status this file
has always produced is the one the context-packet model used to be missing — so
the packet crashed on precisely the call meant to explain a missing onboarding
root. No return value here changed; the shape was named, not altered.

Slice 3b adds `_write_drift_snapshot(code_repository_root, context, rows)`: at the
end of `run_drift_summary`, for a report-producing caller, it persists what the run already computed as a durable
`ar-drift-snapshot/v1` JSON (counts by classification + `actionableCount` + the
per-sidecar rows + `checkedAt` + the current branch) under
`observer.paths.drift_snapshot_dir(coordination_root)`. The observer reducer reads
that snapshot cheaply with a staleness age instead of re-running the
git-per-sidecar classification on a poll cadence (the b1 decision). The write is
**best-effort** (`try/except OSError`), so the dashboard snapshot can never fail
the drift run that produced it. Task 29 extends the snapshot payload with `sourceRoot`, `memoryRoot`,
and optional `reportPath`, giving actionable-drift attention rows enough provenance to identify the
affected repo/memory/report instead of showing a sparse stale alarm.

Task 32 routes the snapshot filename through
`observer.drift_snapshots.drift_snapshot_path(...)` instead of rebuilding the
`<repo>__<branch>.json` path locally. The drift producer, observer pruning, and
cleanup now share one filename contract.

`DriftSummaryOutput` makes internal report materialization explicit. Ordinary drift calls retain
the bounded actionable sample; registered drift/context read callers pass `write_report=False`.
Both legacy and converted branches then file neither a Markdown report nor an observer snapshot,
and omit `reportPath`. Converted measurement still runs through `converted_knowledge_check` and
returns its measured fields unchanged. An internal caller retaining the default `True` remains a
producer. The full leaf quality caller names its enclosure checklist and requests serialized rows;
when it suppresses intermediate filing, that same flag suppresses the observer write as well.

### Invariants And Boundaries

- Summary generation delegates classification to `drift.py`.
- Actionable classifications are limited to drifted, missing verification,
  missing, orphaned, and unsupported rows; the `ACTIONABLE_CLASSIFICATIONS` set
  is now imported from the shared `models.py`, not defined locally here.
- **This module is the drift-status producer; `models.py` is its declaration.**
  Every packet returned here must be a `DriftSummaryPacket`, and a new status
  belongs on `models.DriftStatus` — never as a bare string returned only from
  here, because the two wire models validate against that alias and would refuse
  the packet at the boundary.
- **Status and output mode decide which keys ride.** `checked` carries
  `count`/`actionableCount`/`actionableSample`, and `reportPath` only when filing was requested; `error` carries
  `error`; `notChecked` carries nothing. They are `NotRequired` on the TypedDict,
  so consumers narrow on `status` and read with `.get`.
- A standalone drift report stays under coordination temp. A full leaf quality call may name the
  enclosure's temporary `reports/` checklist path and suppress this module's Markdown write; no
  report ever enters durable memory content.
- The slice-3b drift snapshot is a best-effort write under `logs/observer/drift/`;
  a write failure is swallowed so it never fails the drift run, and its schema/dir
  come from `observer.paths` so producer and reader share one on-disk contract.
- The concrete snapshot filename comes from `observer.drift_snapshots`, so producer
  writes, projection pruning, and cleanup deletion cannot drift apart.
- Snapshot provenance (`sourceRoot`, `memoryRoot`, `reportPath`, `checkedAt`) is copied from the drift
  run context/report, not inferred by the dashboard observer.

## Evidence

### Repo-Internal References

- Tier 3 unresolved: context packets and skill-facing drift tools call this summary helper; `context_packet.py` calls `run_drift_summary`, while `skill_tools.py` exposes `skills_install_tool` and no drift-summary call. [1]
- The memory quality runner wraps actionable rows from this summary as integrity findings, reading the status-conditional keys with `.get`. [2]
- The drift-snapshot dir + schema the b1 write targets (shared with the reader). [6]
- The shared drift-snapshot filename helper now used by the producer. [7]
- The observer reader that consumes the persisted snapshot. [8]
- `_write_drift_snapshot` persists source/memory/report provenance beside counts and rows. [9]
- A converted tree takes `_run_converted_summary`: `status: checked` with `basis: converted-references`,
  the two roots, `sidecarCount`, `count` over observed code/test anchors, `states: {current, stale}`,
  `actionableCount` as the stale count with a bounded `actionableSample`, `violationCount` with a
  bounded `violationSample` of refusing findings, `reportOnlyCount`, and `unreadableSidecars`. Counts
  are exact; only the samples are bounded. A tree that cannot be read returns `status: error` with the
  reason and no counts. An optional `KnowledgeBasePort` base selects the comparison base; the memory
  layer owns no base, the application callers that own a contract bind it.

- A converted tree is measured from the converted check alone; legacy discovery never runs there. [10]
- The converted result names every measured field; zero means empty, never unread. [11]
- The converted branch gates report, observer snapshot and reportPath together; unfiled reads retain the same measured packet. [12]

- `ACTIONABLE_CLASSIFICATIONS` and, since 260731-EFA-L4, `DriftSummaryPacket`/`DriftStatus` are sourced from the shared models module (`DriftStatus` declared in `models/drift.py`). [3]
- The context-packet wire model that validates this packet's `status` — the one that used to lack `error`. [4]
- The tool response model that validates the same packet. [5]
