# skills/l-01-agent-lifecycles/criteria/code-seam.md

## Governing Overview

[skills/l-01-agent-lifecycles overview](../overview.md)

## Purpose

The `code-seam` reviewer criterion: verify production wiring end to end, hunt fail-open
shapes, require validate-then-mutate, and prove quiescence (D1-D4) when a change touches a
reusable primitive or a feedback actor. It is the criteria-catalog home of the
escalation-storm catching evidence and the "no event, message, or row outranks system
health" ruled invariant.

## Code Commentary

### Logic

The criterion's D4 quiescence question demands a multi-cycle zero-input simulation for any
feedback actor whose output is a member of its own input class. Its ruled invariant says
notification rows coalesce — a re-firing condition updates its ONE existing row (date, tries,
attempt) and never appends a sibling. The catching evidence records the 2026-07-09
escalation-storm meltdown (every ladder rung transition minted a new pending row) as the D4
seed and the HFX2-L7 O(n^2) re-fold as the scaling seed.

### Conventions

Criterion files are reviewer-facing doctrine: candidate criteria get promoted with a second
catching engagement, and catching evidence must name the exact leaf/commit that caught the
defect class.

### Invariants And Boundaries

- The coalescing invariant is doctrine: one row per root cause, purgeable stores, and the
  durable artifact on disk never being the queue row.
- Since 260713-TES-L5 the wording says "date, tries, attempt" — "rung" is gone with the
  retired escalation ladder; the escalation-storm history stays as catching evidence, not a
  live mechanism.

### Todos

None.


## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker and curator targeted/scoped check records and preserves any failed or not-run state.

## Evidence

### Docs References

No relevant external documentation found after checking the resolved source registry; the
reviewer criteria catalog and the cited catching leaves are the authority.

- No external/domain document defines this criterion; catching evidence is leaf-cited. [1]

### Repo-Internal References

- The canonical criterion file's standing/candidate structure, mirrored into the packaged runtime copies. [2]

### Cross-Repo References

No meaningful cross-repo references found.

Same-repository reviewer doctrine only.
