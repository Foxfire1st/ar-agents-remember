# mcp/tests/test_closeout_memory_certification_reuse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_memory_certification_reuse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:46:49+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Exercises selected Gate-5 reuse using actual memory producers, immutable evidence and lifecycle journal compare-and-swap. The code executor remains an explicit Node fixture adapter. The test continuation observes real current memory inputs and records pending finalization; it does not install the production memory/finalization adapter or commit protected refs.

## Code Commentary

### Logic

`_scan` runs the full registered memory-check population over the fixture repositories, including drift rows, missing-onboarding census and stale/extra route-index checks. `_write_source_cards` describes actual committed fixture source and builds route indexes. `_publish_actual_coherence` consumes that scan, writes the canonical checklist and publishes coherence through its predecessor-checked owner with the isolated fixture task identity. It requires no unresolved source candidates.

`_fixture` installs and commits a generic profile with a 256 KiB result-document limit before admission, creates memory cards and publishes actual coherence. It calls the real door owner directly because the ordinary queue convenience helper supplies synthetic upstream curator evidence. Public admission and the real runtime establish selected ownership. The injected code executor produces the first four terminals; the unbound continuation must refuse before the fixture installs its memory boundary.

`_certify_memory` observes the current pair, opens the candidate-bound citation index, compiles R06 scope and R07 affected closure, executes the production range-resolution executor and passes actual full-check results plus current coherence to R08. `_publish_fifth` binds that result to the frozen plan, retains required earlier artifact bytes and writes an immutable report generation. Each fifth-gate rail maps to its matching R08 catalog item and references the exact published result-document bytes. Normal result/certificate compilers and the object store produce and reopen originals before the journal owner selects them.

The continuation freshly observes memory twice around finalization. Its memory runner raises if current Gate 5 is rerun; its finalizer returns a nonzero pending result without committing. Tests require current inputs to select finalization only, allow identical pending reentry without another journal change, preserve an inherited fifth terminal across a metadata successor and require a bound observer. Actual memory edits require a successor. Memory movement or cancellation during the second observation prevents finalization while preserving original terminals and physical evidence.

### Conventions

The fixture uses actual small source and memory repositories. Authored cards and task metadata establish its isolated world; passing check and catalog facts come from production owners rather than hand-authored all-green dictionaries. Code execution and finalization remain explicit injected boundaries.

### Invariants And Boundaries

- Current memory inputs are freshly observed; original certificates provide historical input rather than current authority.
- Gate-5 evidence maps to the actual R08 catalog and physically published result bytes.
- Reused terminals retain original object/publication bytes, including across metadata successors.
- Reentry and refusal preserve the journal or its explicitly requested cancellation transition and keep original proofs intact.
- The pending finalizer does not establish production L35/L36 installation, protected-ref publication or closeout acceptance.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this file. | N/A | N/A |

## Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The scan executes the full check population and actual coverage/index owners. | `_scan` | mcp/tests/test_closeout_memory_certification_reuse.py:173-225 |
| Fixture cards describe real committed source and receive generated indexes. | `_write_source_cards` | mcp/tests/test_closeout_memory_certification_reuse.py:228-262 |
| Coherence publication consumes actual scan findings and predecessor bindings. | `_publish_actual_coherence` | mcp/tests/test_closeout_memory_certification_reuse.py:265-317 |
| Current observation, candidate indexing, affected execution and R08 use actual owners. | `_certify_memory` | mcp/tests/test_closeout_memory_certification_reuse.py:320-383 |
| Fifth-gate evidence binds physical publication bytes before stored objects are selected by CAS. | `_publish_fifth` | mcp/tests/test_closeout_memory_certification_reuse.py:386-512 |
| Public selected ownership is real while code execution uses an injected Node adapter. | `_fixture` | mcp/tests/test_closeout_memory_certification_reuse.py:523-592 |
| Fresh inputs lead to pending finalization without committing. | `_Continuation` | mcp/tests/test_closeout_memory_certification_reuse.py:595-623 |
| Current Gate 5 resumes finalization only; identical pending reentry preserves the journal. | `test_current_producer_backed_gate_five_resumes_only_finalization` | mcp/tests/test_closeout_memory_certification_reuse.py:648-680 |
| An original fifth terminal cannot replace a missing current observer. | `test_selected_fifth_terminal_requires_a_bound_current_memory_observer` | mcp/tests/test_closeout_memory_certification_reuse.py:683-696 |
| Metadata successors retain the exact fifth terminal and original certificate chain. | `test_metadata_successor_selects_the_exact_inherited_fifth_terminal` | mcp/tests/test_closeout_memory_certification_reuse.py:699-753 |
| Actual memory movement requires a successor without overwriting original evidence. | `test_changed_actual_memory_requires_a_successor_before_selected_gate_five_replacement` | mcp/tests/test_closeout_memory_certification_reuse.py:756-774 |
| Second-observation memory movement or cancellation prevents finalization. | `test_second_actual_memory_observation_fences_finalization` | mcp/tests/test_closeout_memory_certification_reuse.py:778-799 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented genuine memory producers, original catalog/publication bindings, selected reuse and the pending test finalizer. Existing compiler-fixture documentation remains at its own owner. This source verification makes no gate or acceptance claim.
