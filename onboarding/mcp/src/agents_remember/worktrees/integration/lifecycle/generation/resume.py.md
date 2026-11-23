# mcp/src/agents_remember/worktrees/integration/lifecycle/generation/resume.py

## Governing Overview

[Generation overview](overview.md)

## Purpose

Owns the pure same-generation transition used to recover a retained direct landing.

## Code Commentary

### Logic

`requeued_same_generation` prepares the next attempt of the accepted direct generation at status `running` and phase `direct-preflight`. It increments the attempt, clears its finished time, failure, guidance and cancellation request, and resets only `reconciled-unchanged` mutation legs to `pre-mutation`, preserving the old observations in mutation history.

### Conventions

Resume copies the validated record; it does not create a successor generation or replace immutable accepted input.

### Invariants And Boundaries

- Commit-proven evidence stays intact.
- Same-generation recovery keeps the accepted generation, input and prior mutation history.

### Todos

None recorded.

### Historical CCR private preparation

Before ordinary journal execution was retired, requeueing preserves the same generation and increments its attempt while selecting the closeout phase through `closeout_recovery_phase`. Private preparation therefore resumes as `recovering-private-preparation`; direct landing keeps its independent `direct-preflight` path.


- The retained direct generation advances one attempt at running/direct-preflight. Only reconciled-unchanged legs reset and proven output is kept. [1]


## Evidence

### Docs References

No configured Domain Documentation source applies to this pure transition.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References


- The retained direct generation advances one attempt at running/direct-preflight. Only reconciled-unchanged legs reset and proven output is kept. [2]


- The retained direct generation advances one attempt at running/direct-preflight. Only reconciled-unchanged legs reset and proven output is kept. [3]


### Cross-Repo References

No cross-repository boundary is owned here.

No separately configured cross-repository source is used for this card.

## Historical 260821-CLIVE same-generation claim recovery

In the former ordinary closeout journal path, a retained closeout claim resumes the same generation in `recovering-after-claim`; it does not
return to generic `queued` phase or create a successor; its status is still `queued`. Leg-specific mutation evidence is reset only
according to the existing recovery rules. Claim identity remains the exact journaled door and
operation generation.
