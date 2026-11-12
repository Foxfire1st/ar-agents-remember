# skills/l-01-agent-lifecycles/criteria/code-seam.md

## Governing Overview

[overview](../overview.md)

## Purpose

The code-seam criteria and the shared review rules for all five criteria catalogs. The shared
rules cover baseline coverage, the two routes for a finding after sealing, baseline exploration
lenses and the promotion ratchet. The standing code-seam criteria verify production wiring end to
end (CS-1), hunt fail-open shapes (CS-2), require validate-then-mutate (CS-3) and check scaling,
bounded resources, reclamation and quiescence for every loop, store, log or queue a change touches
(CS-6) and check every line a change adds or alters against the repository's `system/coding-guidelines.md`
(CS-7). The file holds the "no event, message or row outranks system health" invariant.

## Code Commentary

### Logic

CS-7 reads `system/coding-guidelines.md` under `workspace.memoryRoot`, where present, and checks every line the change adds or alters in source code, tests and product messages against it, in particular its Source Comment Scope with the bounded `L<leaf>-R<n>` / `L<leaf>-S<n>` requirement-identifier exception; a line that breaks it is a finding. Doctrine D-6 is now only a pointer to CS-7.

The quiescence property of CS-6 demands a multi-cycle zero-input simulation for any
feedback actor whose output is a member of its own input class. Its ruled invariant says
notification rows coalesce — a re-firing condition updates its ONE existing row (date, tries,
attempt) and never appends a sibling. The candidates CS-4 (reused-primitive affordance parity, one catch) and CS-5
(cross-repository side-effect safety, zero catches) run under baseline exploration, and a separate
rule treats a new UI control that duplicates an existing primitive as a finding.

### Conventions

Criterion files are reviewer-facing doctrine: a candidate is promoted after catching a real defect
in two separate first-review engagements, with its catching evidence cited; a standing criterion
that catches nothing for five consecutive engagements is demoted to spot-check, and an automatable
one moves to a scoped diagnostic. The Reviewer proposes these changes; the loop owner accepts them.

### Invariants And Boundaries

- The coalescing invariant is doctrine: one row per root cause, purgeable stores, and the
  durable artifact on disk never being the queue row.

### Todos

None.

## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker and curator targeted/scoped check records and preserves any failed or not-run state.

The current criterion also treats a new UI control that duplicates an existing primitive as a finding and names the primitive to reuse. This is a check within the requested review, not another automatic review gate.

## Evidence
### Docs References

No relevant external documentation found after checking the resolved source registry; the
reviewer criteria catalog is the authority; the file keeps candidate catch counts, not catching leaves.

- No external or domain document defines these criteria; promotion cites catching evidence. [1]

### Repo-Internal References

- The canonical criterion file's standing/candidate structure, mirrored into the packaged runtime copies. [2]

### Cross-Repo References

No meaningful cross-repo references found.

Same-repository reviewer doctrine only.

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. The following whole-file reference locates that authored contract; it does not convert inherited statements into executed or whole-card acceptance.

- The authored source owns this contract; the distribution copy is not a separate authority. [3]

- The criterion also treats a new UI control that duplicates an existing primitive as a finding and names the primitive to reuse. This is a check within the requested review, not another automatic review gate. [4]
