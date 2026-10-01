# l-01-agent-lifecycles/templates/turn-report.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This template is the **mandatory worker hand-off artifact** of the `l-01-agent-lifecycles` report-template library. A worker fills it at **every** hand-off so a leaf's work survives session death and a respawned successor onboards from **state, not the transcript**. It is the leaf's single artifact of record.

**The relay does not inspect it.** 260915-CAPS-L1 reconciled this template's wording with the shipped
truth boundary: the lifecycle-owned relay derives and delivers the worker's mechanical turn-ended state
signal, the owner is woken with it, and **the manager** then detects a missing or malformed report and
nudges — never a seat-local watcher, and never an artifact-inspecting notifier (uniform-mechanism
ruling 2026-07-07). The truth boundary itself is authored once in `../core/acceptance.md`, and the
check duty this report records is authored in `../operations/closeout.md` § The targeted-check
contract. The template now says so in its own header.

## Code Commentary

### Logic

The synchronized report separates internal protocol-event rows from formal review-handoff attempt
records and gives each lightweight attempt a content-addressed expanded-evidence anchor.

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/turn-report.md`. It has three parts: a prose header naming the artifact and its writer (`roles/worker.md`), a numbered **Rules** block, and a fenced **Shape** the worker copies verbatim — a metadata table (leaf / master / worker / worktree / status / checks / written) followed by the sections *What Was Done*, *Issues Hit*, *Solved On The Spot*, *What Is Left*, *Onboarding Refreshed*, *Escalations*, and the closing **Respawn State** block that onboards a successor from state alone.

### Conventions

The report is written in the **main loop** from the worker's own work plus any sub-agent summaries — never delegated to a sub-agent. It states facts (what changed, what broke, what is proven green, what remains) rather than a narrative, and lives durably in the series notes (`notes/reports/<leaf>-worker-report.md`), referenced from the leaf `task_doc` and posted through the inbox with `messageKind: turn-report`.

### Invariants And Boundaries

The report is mandatory at every hand-off, and a missing one is nudged — by the HFX2-L2 supervisor
sweep mechanically, never a manager hand-rolling its own watch over the artifact (uniform-mechanism
ruling 2026-07-07, 260707-HFX2-L5). The **Respawn State** section must let a fresh successor continue **without reading any transcript**. A plan delta beyond blank-filling does not belong in *Solved On The Spot* — it is escalated to the manager and recorded under *Escalations*.

### Todos

No TODO markers are present in this report template.


## CCR-R12@v5 Handoff Boundary

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

### Docs References

No external domain documentation applies to this repository-local report template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

This bundle copy is the shape the worker job writes at every hand-off; the frame catalogs it as a per-role artifact obligation.

- Sync-propagated bundle copy of the canonical templates source. [1]
- The worker writes the turn report in its main loop and never delegates it; the template governs its shape. [2]
- The truth boundary this template obeys has one home. [3]
- The check duty this report records has one home. [4]

### Cross-Repo References

No sibling repository evidence is needed for this report template.

No meaningful cross-repo references found.

## M38 Turn-Report Projection

The synchronized report shape repeats a complete acceptance envelope for every stable requirement
ID and now contains a dedicated Checks section with exact commands and outcomes, closing the former
brief/report mismatch. It separately records durable-evidence promotion and curator observations;
neither substitutes for requirement evidence.
Packet inspection now records the version-addressed path, approved state, matching ID/version, and
durable corpus ruling before delivery evidence can be review-passable.

## M40/M43 Turn-Report Projection

The installed report is the append-only worker side of the leaf journal. Each record binds exact
requirement/manifestation, attempt/predecessor, candidate, envelope, checks, append time, and
classified findings; prior records are immutable.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## CCR-L42 current candidate

The turn-report template now requires review mode, sealed baseline and outstanding IDs, fixed/unfixed subset dispositions, and a clear separation between worker diagnostic checks and review or certification round accounting.
