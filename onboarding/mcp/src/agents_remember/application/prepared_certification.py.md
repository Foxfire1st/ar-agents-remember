# mcp/src/agents_remember/application/prepared_certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/prepared_certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea` |
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The closeout validator's dispatch between the two gates. | `_realize_prepared_memory`; `validate_onboarding_traces_for_context` | mcp/src/agents_remember/application/prepared_certification.py:346-428 |
| The refusal names each missing trace. | `test_a_missing_trace_is_one_named_repair_finding_and_the_closeout_refuses` | mcp/tests/test_onboarding_trace_gate.py:335-349 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The refusal before anything is realized. | "unclosable = prepared_closeout_refusal(request.handoff.contract)" | mcp/src/agents_remember/application/prepared_certification.py:350-352 |
| Both prepared entry points refuse on converted memory. | `test_the_prepared_closeout_path_fails_closed_on_converted_memory` | mcp/tests/test_knowledge_closeout_gate.py:1034-1046 |

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

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The certification's own source index, or a named refusal with a next step. | `_admitted_source_index` | mcp/src/agents_remember/application/prepared_certification.py:431-453 |
| The candidate route whose register record the closeout gate sees. | `_run` | mcp/src/agents_remember/application/prepared_certification.py:456-575 |
| The reopened handoff this certification reads. | `_current` | mcp/src/agents_remember/application/prepared_certification.py:150-158 |
| The scope authority preserved while final HEAD-based checks read the proved view. | `_PreparedScopeAuthority` | mcp/src/agents_remember/application/prepared_certification.py:161-202 |
| Publication of the selected code artifacts and the final catalog. | `_export` | mcp/src/agents_remember/application/prepared_certification.py:613-662 |
| The emitted final catalog. | `_manifest` | mcp/src/agents_remember/application/prepared_certification.py:665-714 |
| Selection of the original Gate-5 result/certificate. | `_select` | mcp/src/agents_remember/application/prepared_certification.py:717-767 |
| The adapter the lifecycle owner drives. | `PreparedMemoryCertificationAdapter` | mcp/src/agents_remember/application/prepared_certification.py:770-834 |
| The index acquisition the refusal wraps. | `open_repository_index`; `RepositoryIndex` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:180-274; mcp/src/agents_remember/memory_quality/style/citations/source_index.py:360-431 |
| The typed error the acquisition failure becomes. | `SourceIndexError` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:64-65 |
| The route value the certification reads. | `Trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:37-148 |
| The case pinning the gate's own declared check group degrading the same way. | `test_the_closeout_gates_own_check_group_degrades_the_same_way` | mcp/tests/test_citation_index_resilience.py:631-656 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** New subsection "The prepared path fails closed on converted memory (MIK-R09, L09 gap 3)": `_realize_prepared_memory` refuses `prepared-closeout-knowledge-history-unclosable` on converted memory before anything is realized (ruling 14:38:47 gap 3); two rows. The rows the installed fixer normalised are kept.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the subsection "The onboarding gate at closeout (MIK-R30)": the converted-tree dispatch in `_realize_prepared_memory`, with architect ruling 2026-09-29T18:49:50 (6) accepting this file as wiring. Rows below the import and the dispatch were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.




### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.


- 2026-09-17T11:05+02:00 — 260915-CAPS-L14 curator: **moved this card to follow its source** and refreshed it against the current module. The source left `worktrees/integration/closeout/` for the application rank in `806649b9` and this card was left behind, so it resolved to a file that no longer exists and the module read as unonboarded. Corrected the title, `path`, and the governing-overview link to `overview.md` (the application route overview), re-derived **every** reference range against the 813-line source, and documented this leaf's change: `_run` now acquires its index through the new `_admitted_source_index`, which converts a `SourceIndexError` into a named `CertificationContractError` (`citation-source-index-unavailable`) carrying the cause and the operator move, so the closeout gate cannot be bricked by an index it did not choose while satisfiable caps still skip and report. Verification metadata is left at this leaf's synced base `0346da9c` with a recorded working candidate, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.
- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `_current` at mcp/src/agents_remember/application/prepared_certification.py:140-148, `_PreparedScopeAuthority` at mcp/src/agents_remember/application/prepared_certification.py:151-192, `_export` at mcp/src/agents_remember/application/prepared_certification.py:564-613, `_manifest` at mcp/src/agents_remember/application/prepared_certification.py:616-665, `_select` at mcp/src/agents_remember/application/prepared_certification.py:668-718, `PreparedMemoryCertificationAdapter` at mcp/src/agents_remember/application/prepared_certification.py:721-785.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_PreparedScopeAuthority` repointed to mcp/src/agents_remember/application/prepared_certification.py:151-192. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_export` repointed to mcp/src/agents_remember/application/prepared_certification.py:564-613. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/application/prepared_certification.py:721-785. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 54 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances; re-read the reopened claim in the row 50 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances; re-read the reopened claim in the row 51 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances
- 2026-09-11T10:26:37+02:00 — Moved the mirrored sidecar from `mcp/src/agents_remember/memory_quality/prepared_certification.py` to `mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py`. Relocated with the de-entanglement cut (commit `deb032fb`, "move the closeout certification adapter out of memory_quality"): `memory_quality` is a pre-closeout service and must not depend on the closeout plane, so the closeout-facing adapter moved to the closeout side. The source blob is byte-identical to the pre-move file; every cited anchor range was re-verified against the new path and is unchanged. Governing overview link repointed to the closeout integration overview. Verification metadata refreshed to code commit `2fa5e81f4da44a0a87f1a700c5363a9d563e7f9d`.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_current` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:140-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_export` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:564-613. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_manifest` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:616-665. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_select` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:668-718. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:721-785. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:45:44+00:00: CCR-L24 preparation reviewed `_export`, `_manifest`, `_select`, and `PreparedMemoryCertificationAdapter` against the current source; wording retained and ranges regenerated. Verification metadata remains pinned pending final pair composition.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_export` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:323-372. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_manifest` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:375-424. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_select` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:427-476. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:479-542. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
