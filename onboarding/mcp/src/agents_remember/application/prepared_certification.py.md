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

### Landing-report scope

The final quality run binds the context's admitted leaf-base resolver alongside its unchanged converted validator-base port. Landing cut/addition observations therefore keep the leaf-base epoch even when this consumer checks a proved physical code view. This wiring grants no new certification, prepared-closeout or transaction authority; existing refusals remain owned by their current guards.

- The proved-view quality run passes the leaf landing port without replacing its validator or certification guards. [18]


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

`_realize_prepared_memory` asks `leaf_onboarding_trace_sides(current.contract, memory_tree=memory)`
when reached after its prepared-history and cutover guards. With converted sides, it captures
`worktree_code_blobs(physical_code, change.changed_paths)` from the proved physical code view and
passes one `OnboardingTraceInputs` into `validate_onboarding_traces_for_context`: the captured blobs,
the `working_paths`, and the persisted worklist run's identical-copy groups, read by
`_identical_changes` (MIK-R177). The groups are admitted only when that run describes this candidate
— its recorded code base commit, code candidate tree and memory base commit — and no group lists a
member that has since gained an onboarding card (`_pairing_mismatch`, `_card_mismatch`). A run older
than the certified candidate therefore fails closed: the trace stays open and the refusal names the
run's value, the candidate's value and the `agents-remember knowledge-worklist --contract …`
recompute. The remedy is that recompute, never a silent regroup; the validator judges no ungrouped
items and no other candidate's groups. Capture failure keeps its own named
`RuntimeError("the code candidate's blobs cannot be read: …")`, not
`CertificationContractError`. The trace validator names missing traces and unreadable inputs.
The retained `None` branch calls the two legacy plan validators; its existence grants no ordinary
unconverted prepared-closeout permission. This file was accepted as necessary MIK-R30 closeout
wiring (ruling 2026-09-29T18:49:50 (6)); the new blob forwarding grants no prepared-closeout authority.

- The guarded closeout dispatch: capture candidate blobs from the proved physical view and forward them, with the candidate-bound run's groups, to the converted trace validator. [1]
- The trace refusal names missing traces and a stale or unreadable run; blob capture has its own named RuntimeError boundary. [2]

### The prepared path fails closed on converted memory (MIK-R09, L09 gap 3)

`_realize_prepared_memory` now first asks `worktrees.knowledge_gate.prepared_closeout_refusal(contract)`. This
certified (prepared) path binds its memory commit to the exact curator-attested candidate, so it cannot write
`closed: true` into the leaf's history file (MIK-R07 rule 7, MIK-R09 rule 3). On converted memory it therefore refuses
through the path's own `refuse(...)` (`CertificationContractError`, code
`prepared-closeout-knowledge-history-unclosable`), naming why and that the leaf should close out through the worktree
closeout commit; a marker probe Git cannot answer refuses too. The unclosable-history helper returns `None` for unconverted memory, but the following cutover
lock refuses ordinary unconverted memory even when no converted line exists (MIK-R46). The path is wired through `certify_prepared_memory` and the default
`PreparedMemoryCertificationAdapter`; `certification/execution.py::execute_selected_closeout`
carries the same check at its entry. Tested by `test_the_prepared_closeout_path_fails_closed_on_converted_memory`.

The refusal before anything is realized.

Anchor: "unclosable = prepared_closeout_refusal(request.handoff.contract)" [3] |  | mcp/src/agents_remember/application/prepared_certification.py:357-359 |
- Both prepared entry points refuse on converted memory. [4]

### Conventions

Use the named source owners directly. The module was introduced in landed commit
`245057ab16e19afdaabd5c188c9576b22e0c0870`; the existing metadata owner still owns the pending
verification stamp.

### Invariants And Boundaries

- The documented types and paths do not themselves establish execution, certification, delivery or
  acceptance. Those claims require the corresponding owning runtime evidence.
- Certification-contract admissions refuse by name through `CertificationContractError`; the
  converted trace branch instead raises a named `RuntimeError` if code-blob capture fails, and
  its trace validator may raise `RuntimeError` for missing traces. Neither repairs red findings
  nor manufactures curator judgments.
- The source index it admits is the **candidate** route's index, so the exclusion register that
  produced the population is the one that route records.
- **L37.** `_realize_prepared_memory` asks `prepared_closeout_lock` right after the unclosable-history check:
  ordinary unconverted memory is refused with `unconverted-memory-locked`, whether or not the repository
  holds converted memory elsewhere
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

- Current source delta inspected statically: Document physical candidate-blob forwarding and RuntimeError boundary; preserve guards, remove obsolete L46 legacy permission. [19]
