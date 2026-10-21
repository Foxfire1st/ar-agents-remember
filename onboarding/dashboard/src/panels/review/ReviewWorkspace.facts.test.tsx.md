# dashboard/src/panels/review/ReviewWorkspace.facts.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Mounted review-page controls separate movement presentation, subject read state and the one leaf-wide code/worklist answer.

## Code Commentary

### Logic

- The full ReviewSurface uses retained L37 answers with explicit synthetic movement overlays. Eight owner-state/presence rows check the branch-status chip and its popover: current, moved, not measured and unavailable remain distinct, while both raw owner records survive once in closed provenance details.
- The popover omits synthetic identity text, but the raw JSON preserves every supplied extra owner field. Null or absent owners appear as not measured; stale is presented as moved.
- A held subject read leaves the existing chip element and branch status in place. Its answer supplies the next movement owners; a later failed subject read remains unavailable in its subject slot and leaves that chip intact.
- The retained leaf-wide answer establishes the actual count of unchanged-record/code-changed invariants, marks an unread tree row code changed and supplies Worklist 518 open.
- When summary/lane reads fail and the leaf-wide read is held, file attribution is unavailable and Worklist remains pending. Releasing the leaf-wide answer fills Worklist without inventing a zero file count or converting the failed lane to available.

### Invariants And Boundaries

Synthetic movement objects deliberately preserve owner-specific fields and test presentation/wiring, not native movement classification. Captured L37 answers and held fetches do not prove an installed runtime or executed test result.

## Evidence

- Declared check and its fixture assertions. [3]
- Declared check and its fixture assertions. [4]
- Declared check and its fixture assertions. [5]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewWorkspace.facts.test.tsx
>
> ## Governing Overview
>
> [Owning route overview](overview.md)
>
> ## Purpose
>
> Document the synthetic presentation and fixture obligations declared by the actual workspace wiring tests.
>
> ## Code Commentary
>
> The captured task payload and synthetic leaf-wide code/worklist/outline facts exercise `ReviewWorkspace`, not a replacement child renderer. `Probe` passes its real exported `ReadingStatus` through the workspace's `reading` prop. Movement fixtures deliberately include owner-specific extra fields; they are presentation inputs, not model-valid native producer examples.
>
> The shared movement assertions require complete supplied-owner JSON equality, exactly one open facts block, marked state/facts roots, no semantic/reason duplicate in any default-closed disclosure, and a separate closed comparison-identity container. Even current-owner statements remain open. The state line retains both channels without identity text.
>
> ### Declared Assertions
>
> - `it.each` owner-state rows: current/current, stale/stale, not-measured/not-measured, unavailable/unavailable and mixed stale/not-measured, under `keeps both movement owners open for %s`.
> - `it.each` presence rows: sync only, external only and neither owner, under `keeps the movement presence boundary for %s`; absent owners retain fallback words and both absent means no facts block.
> - `it('does not reveal previous movement facts while the next subject is pending or failed', ...)`: previous answer → real workspace pending read → failed read with that same old payload → new answer. Both non-answer checkpoints require no old facts/epoch; recovery requires the new full facts only.
> - `it('wires the one held leaf read into summary, unread tree rows and Worklist status', ...)` retains the leaf-wide code/worklist wiring check.
> - `it('separates file attribution from open work and does not call an unmeasured inventory empty', ...)` retains the separate inventory/attribution/open-work check.
>
> The predecessor's assertion that movement reasons belong in closed details is replaced, not retained as authority or a current test name. The last two case bodies are preserved. This is a source declaration/matrix inventory, not a collected-case total or new execution result.
>
> ### Evidence Boundary
>
> No fresh test, native host, real browser, model classifier, geometry or timing was executed by this documentation pass. Historical producer/Reviewer run receipts retain their exact source and scope; CODE PASS is not MEMORY acceptance.
>
> ## Evidence
>
> - Synthetic captured-payload wiring covers complete open movement facts and marked roots, owner-state/presence matrices, retained previous-payload pending/failure/new-answer transitions, leaf-wide code/worklist wiring and unmeasured inventory distinct from open work; it is not native movement-classifier proof. (historical reference 1)
> - The actual workspace retains the previous payload through pending and failed reads without showing its movement facts, then exposes only the new answer; shared helpers assert full JSON equality, root markers, no closed duplicate and separate closed identities. (historical reference 2)
