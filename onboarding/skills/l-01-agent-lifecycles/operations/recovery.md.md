# skills/l-01-agent-lifecycles/operations/recovery.md

## Governing Overview

[overview](../overview.md)

## Purpose

The recovery operation instruction.

## Code Commentary

The instruction owns the recovery routes for parked and failed work the lifecycle can resume.

## Current composition and authoring contract

Recover the same role, canonical task, paired workspace, request IDs and role agents. Architect, Orchestrator and Manager reconcile an unknown start with the same request ID through `operations/coordination.md`; Worker, Curator, Reviewer and Investigator start no role and ask again instead. Bootstrap recovers in its own chat with its own tools. Uncertainty does not create another owner, transport or global-memory fallback. A resume restores execution, not acceptance or publication.

After a clean synchronization the reviewed result stands; the procedure is read from `operations/implementation.md#synchronize-the-leaf`. Before resuming a memory decision or write, the Curator reads the serving-build boundary in `operations/orientation.md#bind-curation-to-the-serving-build` (no leaf self-production, installs or disabled guards). This keeps an existing boundary across stages, not a new recovery bypass.

## Evidence

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- The authored source owns this contract; the distribution copy is not a separate authority. [1]

- The recovery instruction keeps same-identity recovery and the clean-sync reviewed-result rule, and sends the Curator to the serving-build binding before resuming a memory decision or write. [2]
