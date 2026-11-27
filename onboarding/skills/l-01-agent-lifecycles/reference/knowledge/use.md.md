# skills/l-01-agent-lifecycles/reference/knowledge/use.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Explains how all nine roles combine attributed repository knowledge with direct code inspection at their working step, choose and complete `knowledge_read` views, and follow per-role boundaries across all eight non-Bootstrap roles (Architect, Orchestrator, Manager, Worker, Reviewer, Investigator, Curator, and Consolidator).

## Code Commentary

A fuller `read_ar_files` reply can include the source file's rule text. A compact reply can name a missing saved brief. Open a current saved `briefs/<path>.md` in the memory root when present. The next write covering the file or its folder renews a missing or older saved brief when the writer can refresh it. `knowledge_read` (`view="impact"`, `view="search"`, `view="records"`, `view="dependent"`, and structural/specialist views) provides direct attributed-knowledge retrieval while keeping retrieved claims subordinate to reading source code and running tests.

The workflow starts with `knowledge_read` (`view="impact"` for files/folders or `view="search"` for concepts/terms) or a text search, then batch-reads verbatim record text via `view="records"` (up to 25 text IDs, paginated up to 20 per page) without opening JSON files one by one, and uses `view="dependent"` with `staleOnly=true, compact=true` for closeout triage (full rows when an evidence receipt requires them). Calls bind `memoryRoot` on `agents-remember-task` with automatic code-tree pairing from `contractPath`, `repo_id`, or `memoryRoot` (overridden by `repositoryRoot`/`codeTreeId`), page every view through `continuation` until complete, and reserve native file opens for source code, tests, saved briefs, onboarding cards, and any record detail not carried by `records` or `impact`. Stale memory may orient only when labelled stale and checked against code; a recorded proof describes what a test demonstrates rather than a fresh passing run; refusals, partial indexes, and unverified currentness are reported as gaps; and setting facts come from their authority (`server_info`, resolved memory settings, user settings), never from omitted compact fields.

Role sections cover all eight non-Bootstrap roles with anti-overreach boundaries: Architect (`impact`/`search`/`records` for diagnosis/planning; `consolidation_proposal` only for consolidation planning), Orchestrator (`impact`/`search`/`records` for sprint scope/overlap/rulings; read-only compact `dependent` triage only), Manager (`impact`/`search`/`records` for leaf scope/rulings; compact `dependent` closeout triage without replacing Curator/Consolidator authoring or full receipts), Worker (`impact`/`records` pre-edit and on failing-test `proves` links alongside briefs; no memory authoring, `writers`/`consolidation_proposal`, or dependent sign-off), Reviewer (`impact`/`search`/`records` on every changed file plus memory-lane `dependent(staleOnly=true)` receipts without filtering the diff), Investigator (`search`/`impact`/`records`/`dependent` alongside code/logs without editing code/memory/tasks), Curator (`impact`/`search`/`records` pre-authoring and compact/full `dependent` verification at closeout), and Consolidator (`impact`/`search`/`records` on `consolidationList` families/rules and compact/full `dependent` verification with zero code edits). `view="writers"` and `view="consolidation_proposal"` remain specialist consolidation surfaces.

## Evidence



- Knowledge and code reads are used together, and stale memory is labelled. [1]


- Reads bind the selected memory root with automatic code-tree pairing, use text-bearing `impact`, `search`, and `records` views plus compact `dependent` triage, page to completion, and reserve native file opens for source code, tests, briefs, and uncarried documents. [2]

- Recorded proofs are not passing runs, and gaps and counts are reported without claiming completeness. [3]
- Setting facts come from their owning source. [4]

- Per-role sections apply `knowledge_read` across all eight non-Bootstrap roles (Architect, Orchestrator, Manager, Worker, Reviewer, Investigator, Curator, and Consolidator) with anti-overreach boundaries and without filtering the review diff. [5]





- The Reviewer role reference index links this file under Baseline/knowledge. [6]





- The knowledge-use detail names `briefs/<path>.md` under the memory root. The Worker role directs the pre-edit brief read. Fuller runtime rows can include rule text. Compact rows can retain a pointer even when the saved brief is missing. [8]
