# skills/w-02-light-task-workflow/master-template.md

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This template defines a master plus flat light-subtask series when one task no longer fits a
single-page plan. It connects one integration branch and multiple leaf enclosures to the approved
requirement corpus.

## Current Source Qualification

Each sub-task slice is committed through this skill's own closeout behind an explicit commit gate, integrated into the master integration branch and finalized for that parent-child edge; the master still owns the single release. The inherited wording that names a worktree-manager skill for that closeout describes the retired owner.

## Code Commentary

### Logic

The master carries a filtered table of stable IDs, exact versions, canonical packet links, and
manifestation leaves. Each leaf names exactly one primary revision and may reference adjacent
dependency or preservation constraints. Subtasks close incrementally into the master branch;
the master owns the single release boundary.

The scaffold includes a Requirement Attempt Summary with attempts, rejection history/count,
current state, dominant open failure class, and authoritative leaf-journal links. It is regenerated
from immutable worker/reviewer records and is explicitly non-gating; leaf journals win every
conflict or stale-summary case.

Only formal review-handoff attempts appear in that summary. Internal implementation/test/evidence
runs remain separate protocol events. Leaf records stay lightweight and requirement-specific by
linking content-addressed frozen expanded evidence instead of copying the complete master corpus.

An unrelated later candidate does not reopen an accepted attempt; only the two bounded
invalidation authorities apply.

### Conventions

- Flat numbered files are stable creation identities; the master's Sub-tasks list is an index,
  not execution order. Author exact same-master task IDs in each leaf's `waitsFor` through
  `task_doc`; the product derives Order from them. [5]
- One master integration branch holds all leaf integrations.
- Each active subtask receives its own enclosure/worktree.
- Decision logs stay append-only.

### Invariants And Boundaries

- Corpus approval precedes both master and leaf creation. Create a new JSON-primary master
  through `task_doc` `create` with `kind:"master"` first, then create its indexed child documents
  before leaf `waitsFor` writes. Existing hand-authored Markdown remains unchanged until
  intentionally migrated; a Markdown-only master cannot meet the prerequisite for those writes. [6]
- A master summarizes but never rewrites requirement contracts.
- No leaf may claim closure of multiple independently falsifiable requirements.
- Every revision appears in worker evidence and independent adjudication.
- Requirement version changes invalidate and rebrief only affected work.
- The summary is observation, never requirement, task, lifecycle, closeout, integration, or queue
  authority.

### Todos

None.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Full quality, full tests, full memory quality, certification, and review remain explicit operations and are not automatic closeout or integration prerequisites.

## Evidence

### Docs References

No external Domain Documentation source governs this topology template.

### Repo-Internal References

- The master projects requirements to manifestation subtasks. [1]

- Each subtask names one primary revision and adjacent constraints separately. [2]

- Usage rules preserve approval, versioning, and evidence boundaries. [3]

- The master summary exposes attempt state while preserving leaf-journal authority and a non-gating boundary. [4]
### Cross-Repo References

The target repository supplies its integration, check, and release policy; this template supplies
only lifecycle topology.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

- Flat numbers are stable creation IDs; Sub-tasks is an index and exact same-master waitsFor authored through task_doc derives Order. [5]

- After corpus approval, create a JSON-primary master first, then indexed child documents before waitsFor writes; no Markdown-only new-master route or automatic migration. [6]

## Inherited Source-Epoch Commentary

The following account preserves the former distribution-copy card and its useful explanations, history and warnings. It is inherited scope, not a second current contract or a fresh certification of its dated/currentness, tool, provider, registry, execution or permission claims. The canonical account above retains its existing attribution and qualifications; the authored source below is the authority for the file. Historical reference labels in this quotation are provenance labels, not reference identities of this card.

> # `w-02-light-task-workflow` master-template.md
>
> ## Purpose
>
> This is the canonical scaffold for a `w-02-light-task-workflow` skill **master + light sub-task series** — the composition that
> replaces the retired heavy workflow when a task outgrows a single-page plan. It defines the series
> convention, the master `task.md` scaffold, and the per-slice sub-task scaffold.
>
> ## Code Commentary
>
> ### Logic
>
> The synchronized master template projects only formal review-handoff attempts, excludes internal
> protocol events from counts, and links lightweight leaf records to content-addressed expanded
> evidence.
>
> The file states when to escalate to a series (`l-01-agent-lifecycles` architect lifecycle `decide` step, once size is apparent), the
> series convention (one wrapper folder = master `task.md` + flat numbered `NN_<name>.md` sub-task files
> in execution order), and the lifecycle: **one task = one workflow = one worktree**, a commit per slice
> via `c-09-git-worktree-manager` skill closeout behind a commit gate, the worktree open across slices, and a single integrate +
> `lifecycle_finalize_task` + release at the end with the master owning the version bump. It then gives a master `task.md` scaffold
> (Objective, Sub-tasks execution order, Single Release, Shared Decisions, Open Questions, References)
> and a sub-task `NN_<name>.md` scaffold, plus usage rules.
>
> ### Conventions
>
> Sub-task files are flat and numbered, never nested phase folders. File numbers are stable creation IDs
> while the master's Sub-tasks list is the authoritative execution order. The template was derived from
> the hand-rolled master this very lifecycle-reshape series used (`260601_l01-lifecycle-reshape`).
>
> ### Invariants And Boundaries
>
> A master series runs in one shared worktree (never one per sub-task). Only the master records the
> version bump and release; sub-tasks never bump. `lifecycle_finalize_task` proves the landed edge and
> performs terminal cleanup/task-document reconciliation after integration. Each slice reports its relevant targeted checks, including any
> failed or not-run result, before its commit transaction. Decision
> logs are append-only in both the master and the sub-task files.
>
> ### Todos
>
> No current todo is recorded for this template.
>
>
> ## CCR-R12@v5 Light-Task Boundary
>
> A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Curation is the exception: the curator always runs the complete memory-quality operation as part of curation, and closeout and integration carry its completed result as a prerequisite, while full code quality, full tests, certification, and review remain explicit operations rather than automatic closeout or integration prerequisites.
>
> ### Docs References
>
> No external domain documentation applies to this repository-local template.
>
> No relevant external documentation found.
>
> ## Evidence
>
> ### Repo-Internal References
>
> - The `w-02-light-task-workflow` skill lists `master-template.md` as a companion and adds the master-task composition section + invariant 13. (historical reference 1)
> - The `w-02-light-task-workflow` skill workflow's "Master Task Series" section describes the one-worktree / commit-per-slice / one-integrate lifecycle. (historical reference 2)
>
> As of HFX-L6 the escalation line names the architect lifecycle's `decide` step plainly.
>
> ### Cross-Repo References
>
> No sibling repository evidence is needed for this template.
>
> No meaningful cross-repo references found.
>
> ## Series-Contract Notes
>
> The master template's execution model now says a master provides the integration branch and each active sub-task gets its own leaf enclosure/worktree, replacing the previous single shared worktree guidance.
>
> ## M38 Series Requirement Projection
>
> Master and leaf scaffolds now use stable series-qualified IDs, declare ownership, and require each
> leaf handoff/review pair to cover its exact leaf-owned plus inherited master set. Every row receives
> worker evidence and independent accepted/rejected adjudication; any rejection prevents completion.
> The durable-evidence promotion hold point is recorded separately. This installed file is a
> synchronized projection only.
> Filtered rows link immutable version-addressed packets carrying their durable corpus approval;
> neither master nor leaf rewrites or silently upgrades an approved revision.
>
> ## M40-M45 Master-Summary Projection
>
> The installed master scaffold exposes attempts, rejection history, current state, dominant class,
> and leaf-journal refs through a rebuildable observation that is explicitly never a task,
> lifecycle, closeout, integration, or queue authority.
>
> ## 2026-08-27 Attempt Boundary Clarification
>
> This packaged projection preserves the canonical phase boundary: validate before append; a
> malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
> a malformed handed-off attempt requires independent rejection before successor handoff.

Inherited reference 1 commentary (not a revalidated target):

> The `w-02-light-task-workflow` skill lists `master-template.md` as a companion and adds the master-task composition section + invariant 13.
>
> Anchor: `# w-02-light-task-workflow Light Task Workflow`

Inherited reference 2 commentary (not a revalidated target):

> The `w-02-light-task-workflow` skill workflow's "Master Task Series" section describes the one-worktree / commit-per-slice / one-integrate lifecycle.
>
> Anchor: `# Light Task Workflow`

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [7]
