# mcp/src/agents_remember/application/prepared_certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/prepared_certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T11:05+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
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
| The certification's own source index, or a named refusal with a next step. | `_admitted_source_index` | mcp/src/agents_remember/application/prepared_certification.py:415-437 |
| The candidate route whose register record the closeout gate sees. | `_run` | mcp/src/agents_remember/application/prepared_certification.py:440-554 |
| The reopened handoff this certification reads. | `_current` | mcp/src/agents_remember/application/prepared_certification.py:144-152 |
| The scope authority preserved while final HEAD-based checks read the proved view. | `_PreparedScopeAuthority` | mcp/src/agents_remember/application/prepared_certification.py:156-196 |
| Publication of the selected code artifacts and the final catalog. | `_export` | mcp/src/agents_remember/application/prepared_certification.py:592-641 |
| The emitted final catalog. | `_manifest` | mcp/src/agents_remember/application/prepared_certification.py:644-693 |
| Selection of the original Gate-5 result/certificate. | `_select` | mcp/src/agents_remember/application/prepared_certification.py:696-746 |
| The adapter the lifecycle owner drives. | `PreparedMemoryCertificationAdapter` | mcp/src/agents_remember/application/prepared_certification.py:749-813 |
| The index acquisition the refusal wraps. | `open_repository_index`; `RepositoryIndex` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:323-390 |
| The typed error the acquisition failure becomes. | `SourceIndexError` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:64-65 |
| The route value the certification reads. | `Trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:30-78 |
| The case pinning the gate's own declared check group degrading the same way. | `test_the_closeout_gates_own_check_group_degrades_the_same_way` | mcp/tests/test_citation_index_resilience.py:631-656 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

- 2026-09-17T11:05+02:00 — 260915-CAPS-L14 curator: **moved this card to follow its source** and refreshed it against the current module. The source left `worktrees/integration/closeout/` for the application rank in `806649b9` and this card was left behind, so it resolved to a file that no longer exists and the module read as unonboarded. Corrected the title, `path`, and the governing-overview link to `overview.md` (the application route overview), re-derived **every** reference range against the 813-line source, and documented this leaf's change: `_run` now acquires its index through the new `_admitted_source_index`, which converts a `SourceIndexError` into a named `CertificationContractError` (`citation-source-index-unavailable`) carrying the cause and the operator move, so the closeout gate cannot be bricked by an index it did not choose while satisfiable caps still skip and report. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.

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

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
