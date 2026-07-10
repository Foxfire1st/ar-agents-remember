# mcp/tests/test_projection_scaling_cs6.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_projection_scaling_cs6.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-07-10T01:14+02:00                         |
| lastVerifiedCommitHash |                                                `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`|
| lastVerifiedCommitDate |                                                2026-07-10T22:30:19+02:00|
| governingOverview      | `../overview.md`                               |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`; existing test sidecars are governed by the package overview.

## Purpose

`test_projection_scaling_cs6.py` pins the projection tick fixes from HFX2-L12 fix round 2. It focuses on the 1-second projection path surfaces that previously double-folded gate logs, double-walked task JSON, re-ran git status per leaf, re-parsed unchanged lifecycle logs, and silently allowed task-document body payload growth.

## Code Commentary

### 260707-HFX2-L13 F6/F7 Two-Size And Cache Proof

`LifecycleLogCacheTests` instruments the real `EventStore.read_log` parse boundary. A cold pass must
parse once; a later heartbeat-sidecar change must update the merged event view without another log
parse, closing round-1 B2. Task-document scaling cases at two corpus sizes assert the broadcast is
windowed, every summary has a `bodyRevision`, and reader-body byte cost is zero. Separate cases prove
series summaries are body-free and the on-demand reader returns full content.

### Logic

`GateReadFoldTests` counts `GateStore.read()` calls and proves `read_gates()` folds each gate log once per tick. `TaskDocSharedCacheTests` proves task and series readers share the same parsed task-json cache. `GitStatusCacheTests` proves `_safe_status_payload()` is TTL-cached. `LifecycleLogCacheTests` proves unchanged lifecycle logs are not re-read at two event-log sizes. `TaskDocumentsPayloadBudgetTests` characterizes the still-unbounded task-doc body payload and proves the write-path guardrail logs only when over budget and is rate-limited.

### Conventions

The tests patch module-level seams only inside `try/finally` blocks, clear the relevant caches before assertions, and use deterministic counters instead of wall-clock where possible.

### Invariants And Boundaries

F6 payload windowing is not implemented here; the test deliberately characterizes the unbounded body cost and pins the guardrail that HFX2-L13 will turn into a bounded broadcast contract.

### Todos

Replace the F6 characterization with a bounded assertion when HFX2-L13 moves full task bodies out of the always-on projection.

## Docs References

No external documentation governs these repo-local projection scaling regressions.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test file covers gate one-read folds, shared task-doc cache, git status TTL, lifecycle-log cache, and task-doc payload guardrail. | L44-L73; L76-L118; L121-L141; L144-L184; L186-L242 | [mcp/tests/test_projection_scaling_cs6.py](agents-remember/mcp/tests/test_projection_scaling_cs6.py) |
| Projection store implements lifecycle-log caching and over-budget task-document payload warnings. | L93-L130; L248-L274 | [mcp/src/agents_remember/observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| Snapshot readers implement the shared task-document cache, single-read gate fold, and git-status TTL cache. | L113-L155; L485-L516; L603-L665 | [mcp/src/agents_remember/observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6/F7/B2: revived the lifecycle-log cache instrument,
  proved sidecar merge without reparse, and added body-free/windowed broadcast plus on-demand body
  regressions. Verification metadata remains pinned until closeout stamps the eventual L13 code
  commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: created for the projection CS-6 scaling regressions added in fix round 2. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
