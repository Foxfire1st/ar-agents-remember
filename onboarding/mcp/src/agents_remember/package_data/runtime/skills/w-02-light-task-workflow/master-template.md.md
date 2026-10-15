# `w-02-light-task-workflow` master-template.md

## Purpose

This is the packaged synchronized copy of the canonical `skills/w-02-light-task-workflow/master-template.md` scaffold for a master plus light leaf series. It describes the series convention, master index and per-leaf scaffold; it is not an independent canonical runtime owner.

## Code Commentary

### Logic

The synchronized master template projects only formal review-handoff attempts, excludes internal
protocol events from counts, and links lightweight leaf records to content-addressed expanded
evidence.

Escalation is decided by the architect lifecycle when one plan becomes several slices. A wrapper holds the master and flat numbered leaf files; numbers are stable creation IDs, the Sub-tasks list is an index, and each leaf's exact same-master `waitsFor` through `task_doc` derives Order. The master owns an integration branch/root contract, while each active leaf has its own enclosure, work branch and worktree, then closes out behind its commit gate, integrates and finalizes that edge. The scaffold names Objective, the filtered requirement/attempt summaries, Sub-tasks, Single Release, Shared Decisions, Open Questions and References. Fixed prose uses `objective`, `requirements`, `design`, `nonGoals`, `acceptance`; decisions and the index use `append_decision`/`set_subtask`, not duplicate prose sections.

### Conventions

Sub-task files remain flat and append-friendly with stable creation numbers. The master's Sub-tasks list is an index, not an authoritative execution-order list: the product derives Order from exact leaf `waitsFor` task IDs. Create a new JSON-primary master through `task_doc` `create` with `kind:"master"` in the wrapper, then create its indexed child documents before leaf `waitsFor` writes. The master scaffold is a render specification, not a Markdown-only new-master authoring route. Existing hand-authored Markdown remains unchanged until intentionally migrated, and a Markdown-only master cannot satisfy the prerequisite for those writes. The historical hand-rolled origin (`260601_l01-lifecycle-reshape`) is retained as provenance, not the current scheduling contract. This packaged source does not prove installation or migration. [5]

### Invariants And Boundaries

The master series uses one integration branch plus a distinct enclosure/worktree per active leaf, never one shared worktree for all slices. Only the master owns the version bump/release. Each leaf closes out, integrates into the master and finalizes its own edge. Usage rules require relevant targeted/requirement checks with honest failed or not-run reporting and append-only decision logs; they distinguish those checks from explicit full tests, full code quality and independent review. The earlier series-convention sentence still asks for suite-green checks; this card preserves that source tension rather than pretending it was removed.

### Todos

No current todo is recorded for this template.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Curation is the exception: the curator always runs the complete memory-quality operation as part of curation, and closeout and integration carry its completed result as a prerequisite, while full code quality, full tests, certification, and review remain explicit operations rather than automatic closeout or integration prerequisites.

### Docs References

No external domain documentation applies to this repository-local template.

No relevant external documentation found.

## Packaged Index Scaffold

The Sub-tasks scaffold declares an index and exact waitsFor-derived Order. Fixed fields and primary/adjacent constraints replace the stale execution-order/dependency-prose account, without discarding the separate attempt and targeted-check lessons.

- Current index/waitsFor and fixed-content authoring rules. \[3] [3]

- Exactly one owned primary requirement; adjacent constraints do not confer closure. \[4] [4]
## Evidence

### Repo-Internal References

- Packaged skill names the template companion and defines stable-ID/waitsFor composition plus master/leaf worktree invariant. [1]

- Packaged workflow distinguishes master integration branch from per-leaf enclosure/worktree, closeout, integration and finalization; master alone releases. [2]
As of HFX-L6 the escalation line names the architect lifecycle's `decide` step plainly.

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.

## Series-Contract Notes

The master template's execution model now says a master provides the integration branch and each active sub-task gets its own leaf enclosure/worktree, replacing the previous single shared worktree guidance.

## M38 Series Requirement Projection

The master projects stable approved requirement IDs/versions and packet links, without rewriting the corpus. Each leaf owns exactly one primary requirement revision and separately names adjacent dependency/preservation constraints; it cannot claim to close those adjacent requirements. A revision may have multiple independently executable leaf manifestations, but a leaf closing several independent requirements must be split. Each primary gets worker evidence and independent accepted/rejected adjudication; the master cannot pass with a rejected ID or an accepted-but-worker-blocked manifestation. Durable-evidence promotion remains a separate hold. The packaged file is a synchronized projection only. Immutable version-addressed packet links and durable corpus approval remain unchanged.

## M40-M45 Master-Summary Projection

The packaged master scaffold exposes attempts, rejection history, current state, dominant class,
and leaf-journal refs through a rebuildable observation that is explicitly never a task,
lifecycle, closeout, integration, or queue authority.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

- The master scaffold is a render specification; use task_doc create kind master, then indexed children, before waitsFor; existing Markdown remains until intentional migration. [5]
