# skills/l-01-agent-lifecycles/operations/curation.md

## Memory review and ownership

Curator owns reconciliation, memory authoring, full quality/coherence evidence, and direct Reviewer handover; Manager retains transaction, closeout, and acceptance authority. Curation is evidence, not a gate. Separate MEMORY review lane/budget rules live in `operations/review.md#rounds`.

## Message/file transport

Message-file payload rules live in `reference/message-handover.md`; `operations/curation.md` directs sending the memory candidate directly to Reviewer via `role_message` (sibling role, leaf refs, whole IDs) and writing the coherence record before turn end.

## Governing Overview

[overview](../overview.md)

## Purpose

The curation operation instruction: Curators use it to reconcile a leaf's intent, code and memory and to prepare its memory handover; Managers use it to assign that work and keep transaction and acceptance authority.

## Foundation carrier and writer admission

Before first or resumed knowledge foundation, Manager reads `reference/curator/repository-foundation.md#enter-through-the-real-foundation-task`. Missing, unapproved, or mismatched requirement packets are rejected; atomic leaves review at master integration.

## Code Commentary

`operations/curation.md` (36 lines) defines the concise Tier-1 curation workflow: verify writer outputs resolve in `workspace.memoryRoot`, read `worktree_status` (informational), require a readable worklist before ingest, read scoped `knowledge_read` plus full `knowledge_diff` before semantic changes, and record staleness known at task intake as the task's curation work; then (1) reconcile intent/code and verify card sentences vs code, (2) ingest invariants in scope and update families only with justification plus re-examined guarantee, (3) route notes to file/route/entity or Operational-Notes (edit entities for real changes only), and (4) update cards/sidecars/prose and run leaf-scoped `route_index_refresh`.

Under `### Checks and gates`, curation checks enabled repos before asking about updates, reports sidecars, overviews/indexes/entities, `git diff --check`, `knowledge_integrity_check` and full `memory_quality_check` (scoped checks never substitute; rerun until `curatorActionableCount=0` and `qualityChecklistStatus=ready-for-closeout`), notes that closeout runs the stale `dependent` check (detailed in `reference/curator/exceptions-and-recovery.md`), and requires a non-authoring seat for `OM-2` independent fact-check. Manager-only text summarizes Curator prohibitions; on `checklistStatus=coherence-required`, Curator runs `curator_coherence` `prepare`->`publish`->`validate` before closeout without re-validating post-closeout trees. Curator keeps partial/refused handovers partial, sends memory candidate to Reviewer via `role_message`, sends evidenced code concerns to Worker and Reviewer without repairing code or authoring false knowledge, and routes Manager/sync/cross-leaf notices per line 36.

- Full memory_quality_check, the Manager-leaf-closeout stale dependent-document knowledge_read (detailed in reference/curator/exceptions-and-recovery.md), and the independent non-authoring OM-2 fact-check are separate curation obligations. [2]


## Current composition and authoring contract

Audience markers (`<!-- ar:roles all -->`, `<!-- ar:roles manager -->`, `<!-- ar:roles curator -->`) separate Manager-only foundation pointer and Curator-prohibition summary from Curator-only workflow/handover steps and shared checks/gates/notices. Detailed family-history, encountered-records, report-only, card-cut, and recovery procedures live in `reference/curator/*` linked from `roles/curator.md`.

## Evidence


- Current curation keeps Manager transaction ownership separate, requires full memory_quality_check, the Manager-leaf-closeout stale dependent-document read (detailed in reference/curator/exceptions-and-recovery.md) and the independent OM-2 fact-check, and pairs with separate MEMORY review (operations/review.md). Bounded repairs and genuine stops live in reference/curator/exceptions-and-recovery.md and scoped correct-write recovery in core/every-role.md; none of this grants Git, closeout or acceptance authority. [4]



- Restating a family guarantee needs a `changed` family history row with the Curator's effect, the writer fills the family revision, and families are read back and prepared-context locations attributed. [13]

- Current curation verifies card sentences against source, delegates bounded encountered-memory repairs (beyond quality-check findings, named, without a broad sweep) to reference/curator/exceptions-and-recovery.md, routes code concerns, requirement decisions and cross-leaf work to their owners, and requires full checks and the independent OM-2 fact-check before handover. [14]


- MEMORY review stays separately sealed/counted and never opens or resets CODE review. Beyond the settings limit the architect or developer authorizes the pass and Manager records it. Curator owns corrected input/body/coherence work; transaction steps and external effects stay with their owners. The installed-build quality/coherence outcome and direct Reviewer handover remain separate from independent acceptance. [1]


- Foundation authoring is regular work in the real Architect task, with its leaf admission, actual enclosure and task/Manager ownership; no incidental code delta is required. Setup reads and reports state. [3]

- Successful preparation precedes publication with one judgment per candidate, or an empty list, and validation. [15]
