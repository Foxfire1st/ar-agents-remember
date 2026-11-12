# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py

## Governing Overview

[Generation overview](overview.md)

## Purpose

Owns the pure same-generation transition used to retry or recover retained lifecycle intent.

## Code Commentary

### Logic

`requeued_same_generation` requires any current worker-termination record to prove exit, archives that proof, and resets only `reconciled-unchanged` mutation legs to `pre-mutation` while retaining their history. It increments the attempt and clears transient failure/cancellation state. Direct landing receives status `running` and phase `direct-preflight`; other operations receive status `queued`. A retained closeout claim keeps phase `recovering-after-claim`, while other queued operations receive phase `queued`.

### Conventions

Resume copies the validated record; it does not create a successor generation or replace immutable accepted input.

### Invariants And Boundaries

- Unproven worker termination blocks resume.
- Commit-proven evidence is never reset.
- Same-generation recovery preserves prior mutation and termination history.

### Todos

None recorded.

### CCR private preparation boundary

Requeueing preserves the same generation and increments its attempt while selecting the closeout phase through `closeout_recovery_phase`. Private preparation therefore resumes as `recovering-private-preparation`; direct landing keeps its independent `direct-preflight` path.

- The current `requeued_same_generation` boundary implements the preparation contract above. [1]

## Evidence

### Docs References

No configured Domain Documentation source applies to this pure transition.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Resume requires exited worker proof and archives it. [2]
- Only unchanged mutation evidence is reset; attempt and transient execution state advance within the same record. [3]

### Cross-Repo References

No cross-repository boundary is owned here.

No separately configured cross-repository source is used for this card.

## 260821-CLIVE Same-Generation Claim Recovery

A retained closeout claim resumes the same generation in `recovering-after-claim`; it does not
return to generic `queued` phase or create a successor; its status is still `queued`. Leg-specific mutation evidence is reset only
according to the existing recovery rules. Claim identity remains the exact journaled door and
operation generation.
