# dashboard/src/panels/review/ReviewWorkspace.facts.test.tsx

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Document the synthetic presentation and fixture obligations declared by the actual workspace wiring tests.

## Code Commentary

The captured task payload and synthetic leaf-wide code/worklist/outline facts exercise `ReviewWorkspace`, not a replacement child renderer. `Probe` passes its real exported `ReadingStatus` through the workspace's `reading` prop. Movement fixtures deliberately include owner-specific extra fields; they are presentation inputs, not model-valid native producer examples.

The shared movement assertions require complete supplied-owner JSON equality, exactly one open facts block, marked state/facts roots, no semantic/reason duplicate in any default-closed disclosure, and a separate closed comparison-identity container. Even current-owner statements remain open. The state line retains both channels without identity text.

### Declared Assertions

- `it.each` owner-state rows: current/current, stale/stale, not-measured/not-measured, unavailable/unavailable and mixed stale/not-measured, under `keeps both movement owners open for %s`.
- `it.each` presence rows: sync only, external only and neither owner, under `keeps the movement presence boundary for %s`; absent owners retain fallback words and both absent means no facts block.
- `it('does not reveal previous movement facts while the next subject is pending or failed', ...)`: previous answer → real workspace pending read → failed read with that same old payload → new answer. Both non-answer checkpoints require no old facts/epoch; recovery requires the new full facts only.
- `it('wires the one held leaf read into summary, unread tree rows and Worklist status', ...)` retains the leaf-wide code/worklist wiring check.
- `it('separates file attribution from open work and does not call an unmeasured inventory empty', ...)` retains the separate inventory/attribution/open-work check.

The predecessor's assertion that movement reasons belong in closed details is replaced, not retained as authority or a current test name. The last two case bodies are preserved. This is a source declaration/matrix inventory, not a collected-case total or new execution result.

### Evidence Boundary

No fresh test, native host, real browser, model classifier, geometry or timing was executed by this documentation pass. Historical producer/Reviewer run receipts retain their exact source and scope; CODE PASS is not MEMORY acceptance.

## Evidence

- Synthetic captured-payload wiring covers complete open movement facts and marked roots, owner-state/presence matrices, retained previous-payload pending/failure/new-answer transitions, leaf-wide code/worklist wiring and unmeasured inventory distinct from open work; it is not native movement-classifier proof. [1]
- The actual workspace retains the previous payload through pending and failed reads without showing its movement facts, then exposes only the new answer; shared helpers assert full JSON equality, root markers, no closed duplicate and separate closed identities. [2]
