# mcp/src/agents_remember/application/prepared_certification.py

## Governing Overview

[application overview](overview.md)

## Purpose

Real memory certification against a proved private code view.

This adapter is the **application-rank** owner of the closeout certification. It was cut out of
`memory_quality` by `deb032fb` ("move the closeout certification adapter out of memory_quality") —
`memory_quality` is a pre-closeout service and must not depend on the closeout plane — and it moved
on to the application rank in `806649b9`, which is why its card lives under `application/`.

## Code Commentary

### Logic

The adapter preserves canonical logical scope roots while final HEAD-based checks read the proved
physical code output. It reopens task authority and curator coherence, executes the actual affected
closure and complete memory checks, and records missing onboarding and route-index drift in final
certification. Publication retains original selected code artifacts, emits the actual final catalog
and selects the original Gate-5 result/certificate through the lifecycle owner. Red evidence remains
selected and raises a typed failure; the adapter does not manufacture curator judgments or repair
findings. `observe` invokes the same actual affected-closure and full memory checks through `_run`,
but publishes no replacement terminal; it is not a cheap identity-only lookup.

`_run` acquires its source index **through `_admitted_source_index`**, over
`Trees(logical_code, memory, candidate_tree=candidate.code.candidateTree)` — the explicit candidate
route, which is why the closeout gate sees the register record that route produces.

### The closeout gate cannot be bricked by an index it did not choose

`_admitted_source_index` wraps `open_repository_index(trees, verify_integrity=True)` and converts a
`SourceIndexError` into a **named refusal with a next step**. When the citation source index cannot
be acquired — past the ~2 GiB hard stop, over the 100k file-count cap, a malformed
`onboarding.citationIndex` block, an unreadable checkout — the candidate is refused with the cause
and the operator move, rather than a bare `ValueError` or a traceback. The refusal is a
`CertificationContractError` carrying

```
"closeout certification admission refused"
  code:     "citation-source-index-unavailable"
  path:     "citationSourceIndex"
  expected: "an acquirable citation source index for the candidate code tree"
  observed: <the underlying SourceIndexError message>
```

Caps that **can** be satisfied never reach here: they skip and report. This is the closeout-side
half of the same contract the citation index itself states — a bound that is exceeded is a
reported, actionable state, never a silent omission and never a whole-tree refusal of the quality
surface.

### The onboarding gate at closeout (MIK-R30)

`_realize_prepared_memory` now asks `leaf_onboarding_trace_sides(current.contract, memory_tree=memory)`
first. With sides (a converted K_B or K_C), it runs `validate_onboarding_traces_for_context`, which refuses
naming every missing trace, every unreadable input and today's missing onboarding. With `None` it runs
today's `validate_onboarding_refresh_plan_for_context` and `validate_route_overview_refresh_plan_for_context`
exactly as before. This file is outside MIK-R30's Scope list, but rule 6 names "the closeout validator", and
the architect accepted it as necessary wiring (ruling 2026-09-29T18:49:50 (6)).

- The closeout validator's dispatch between the two gates. [1]
- The refusal names each missing trace. [2]

### The prepared path fails closed on converted memory (MIK-R09, L09 gap 3)

`_realize_prepared_memory` now first asks `worktrees.knowledge_gate.prepared_closeout_refusal(contract)`. This
certified (prepared) path binds its memory commit to the exact curator-attested candidate, so it cannot write
`closed: true` into the leaf's history file (MIK-R07 rule 7, MIK-R09 rule 3). On converted memory it therefore refuses
through the path's own `refuse(...)` (`CertificationContractError`, code
`prepared-closeout-knowledge-history-unclosable`), naming why and that the leaf should close out through the worktree
closeout commit; a marker probe Git cannot answer refuses too. Unconverted memory gets `None` and runs exactly as
before. The path has no production caller today (ruling 2026-09-30T14:38:47 gap 3: "fails closed on converted memory
with a named reason until it can close the history file"); `certification/execution.py::execute_selected_closeout`
carries the same check at its entry. Tested by `test_the_prepared_closeout_path_fails_closed_on_converted_memory`.

- The refusal before anything is realized. [3]
- Both prepared entry points refuse on converted memory. [4]

### Conventions

Use the named source owners directly. The module was introduced in landed commit
`245057ab16e19afdaabd5c188c9576b22e0c0870`; the existing metadata owner still owns the pending
verification stamp.

### Invariants And Boundaries

- The documented types and paths do not themselves establish execution, certification, delivery or
  acceptance. Those claims require the corresponding owning runtime evidence.
- The adapter refuses by name through a typed `CertificationContractError`; it does not repair a
  red finding and does not manufacture a curator judgment.
- The source index it admits is the **candidate** route's index, so the exclusion register that
  produced the population is the one that route records.
- **L37.** `_realize_prepared_memory` asks `prepared_closeout_lock` right after the unclosable-history check:
  unconverted memory in a repository that holds converted memory is refused with `unconverted-memory-locked`
  (MIK-R09 rule 6), before anything is realized. `_run` passes `knowledge_base=context_check_base(physical_code,
  context)` to the final memory-quality run, so its `knowledge.converted` check uses the converted base when
  `HEAD` is unconverted (review R3-1).

### Todos

No source-local TODO is asserted here.

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- The certification's own source index, or a named refusal with a next step. [5]
- The candidate route whose register record the closeout gate sees. [6]
- The reopened handoff this certification reads. [7]
- The scope authority preserved while final HEAD-based checks read the proved view. [8]
- Publication of the selected code artifacts and the final catalog. [9]
- The emitted final catalog. [10]
- Selection of the original Gate-5 result/certificate. [11]
- The adapter the lifecycle owner drives. [12]
- The index acquisition the refusal wraps. [13]
- The typed error the acquisition failure becomes. [14]
- The route value the certification reads. [15]
- The case pinning the gate's own declared check group degrading the same way. [16]

- The prepared closeout refuses unclosable converted memory, then locked unconverted memory. [17]

### Cross-Repo References

No cross-repository source is needed for this card.
