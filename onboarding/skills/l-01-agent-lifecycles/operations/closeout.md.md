# skills/l-01-agent-lifecycles/operations/closeout.md

## Governing Overview

[overview](../overview.md)

## Purpose

The closeout operation instruction.

## Code Commentary

The instruction defines the evidence and authority boundaries around an existing paired closeout; `worktree_closeout_preview` and `worktree_closeout_apply` on `agents-remember-task` own the transaction procedure. It binds the accepted inputs and evidence, names the invariant-gate judgment at each publication step and the refusal codes `knowledge-gate-refused` and `direct-landing-knowledge-gate-refused`, sends gate findings to the Curator, and allows no completion claim before the owning tool's result is read back. Closeout is never a Worker, Reviewer or Curator task.

A Manager or Orchestrator coordinates the closeout under supplied task authority. In a flat run with neither, the owning Architect may coordinate the same transaction only with the developer's explicit commit approval for that closeout, or with authority the developer delegated for the series and recorded in the task document. Targeted-check results are carried under the closeout preview's accepted code and memory input, with failures, unrun checks and missing evidence kept visible.

## Evidence

No separate reference list: the file's sidecar carries the realization entries for its current anchors.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- The authored source owns this contract; the distribution copy is not a separate authority. [1]
